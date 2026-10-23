"""LTX-2.5 distilled — ZeroGPU demo on **diffusers** (upstream main, PR #14447), two-stage.

Follows the code snippets on https://huggingface.co/Lightricks/LTX-2.5-Diffusers:

  1. stage 1  `LTX2Pipeline(sigmas=DISTILLED_SIGMA_VALUES, output_type="latent")` at HALF the target
              resolution. Unguided (distillation folds guidance into the weights).
  2. upsample `LTX2LatentUpsamplePipeline` — x2 spatial, no temporal.
  3. stage 2  `LTX2Pipeline(sigmas=STAGE_2_DISTILLED_SIGMA_VALUES, latents=..., audio_latents=...,
              noise_scale=STAGE_2_DISTILLED_SIGMA_VALUES[0])` — takes its size from the upsampled
              latents. Video AND audio are both reseeded from stage 1, matching the reference
              (`DistilledPipeline` refines audio in stage 2 too and decodes the stage-2 audio latent).
  4. decode   `LTX2VideoDiffusionDecodePipeline(denormalize=False)` — LTX-2.5's neighborhood-attention
              diffusion decoder (tiled, NATTEN kernels from the Hub) — then `audio_vae` + `vocoder`
              for the audio. The convolutional VAE decoder is the default in the UI.

Two details that are easy to get wrong and are load-bearing here:

* **The normalization chain.** `output_type="latent"` returns *denormalized* latents; the upsampler
  wants denormalized ones (its default); `prepare_latents` renormalizes what you hand it; and the
  decode pipeline must therefore be told `denormalize=False`.
* **One generator for the whole call.** The reference builds a single `torch.Generator` and threads it
  through both stages, so stage 2 continues the noise stream rather than repeating stage 1's draw.
  A fresh per-stage generator on the same seed would silently diverge.
"""

import os

# ZeroGPU's MIG slice trips an NVML assert in torch's native caching allocator
# ("NVML_SUCCESS == r INTERNAL ASSERT FAILED"); cudaMallocAsync is NVML-safe. Must be set before
# torch initializes its allocator. torch 2.9 renamed the variable and warns on the old name, so set both.
os.environ.setdefault("PYTORCH_ALLOC_CONF", "backend:cudaMallocAsync")
os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "backend:cudaMallocAsync")

import hashlib
import random
import tempfile
import time
from collections import OrderedDict

import gradio as gr
import PIL.Image
import spaces
import torch
from gradio_client import Client, handle_file
from huggingface_hub import snapshot_download

from diffusers import (
    LTX2ImageToVideoPipeline,
    LTX2LatentUpsamplePipeline,
    LTX2Pipeline,
    LTX2VideoDiffusionDecodePipeline,
    LTX2VideoDiffusionDecoderModel,
)
from diffusers.models.autoencoders.ltx2_diffusion_decoder import (
    LTX2VideoVaeNeighborhoodNattenProcessor,
)
from diffusers.pipelines.ltx2.latent_upsampler import LTX2LatentUpsamplerModel
from diffusers.pipelines.ltx2.utils import (
    DEFAULT_NEGATIVE_PROMPT,
    DISTILLED_SIGMA_VALUES,
    STAGE_2_DISTILLED_SIGMA_VALUES,
)
from diffusers.utils import encode_video

HF_TOKEN = os.environ.get("HF_TOKEN")

# Lightricks' own diffusers pack. Verified equivalent to the internal mirror it replaces: same 4090
# transformer keys, byte-identical sampled tensors, identical transformer/scheduler/latent_upsampler
# configs — only the sharding differs (4 shards -> 8). Its `model_index.json` additionally lists
# `diffusion_decoder`, which `LTX2Pipeline` does not take; diffusers drops it with a warning
# ("not expected and will be ignored"), and the decoder is loaded from its subfolder below regardless.
# Gated (auto-approve): the Space's HF_TOKEN must have accepted the license or from_pretrained 403s.
MODEL_ID = os.environ.get("LTX25_MODEL_ID", "Lightricks/LTX-2.5-Diffusers")
MAX_SEED = 2**31 - 1
FRAME_RATE = 24.0


def frames_from_duration(seconds: float) -> int:
    """Snap a duration in seconds to the VAE's 8k+1 frame grid at 24 fps (2 s -> 49 frames)."""
    return max(25, int(round(float(seconds) * FRAME_RATE)) // 8 * 8 + 1)

# Auto length. The LTX-2.5 checkpoints ship a duration head, so the model can pick the clip length from the
# prompt instead of taking it from the slider. Capped below the head's own 20s default: the ZeroGPU
# reservation has to cover the worst case (the prediction only exists once the connectors have run, i.e.
# already inside the GPU call), so the ceiling is what every auto run costs a visitor's quota.
AUTO_MAX_SECONDS = 15.0
AUTO_MAX_FRAMES = int(AUTO_MAX_SECONDS * FRAME_RATE) // 8 * 8 + 1  # 361, on the VAE's 8k+1 grid

# ---------------------------------------------------------------------------------------------
# THE RECIPE — the exported constants from diffusers.pipelines.ltx2.utils, already trimmed of the
# reference's trailing 0.0 (`set_timesteps(sigmas=...)` appends its own terminal zero).
# Note the spacing is deliberately non-uniform: five values packed near 1.0, then three large jumps.
# ---------------------------------------------------------------------------------------------
STAGE_1_SIGMAS = DISTILLED_SIGMA_VALUES
STAGE_2_SIGMAS = STAGE_2_DISTILLED_SIGMA_VALUES
# Unguided in both stages: the reference uses SimpleDenoiser throughout for the distilled model.
GUIDANCE_SCALE = 1.0
AUDIO_GUIDANCE_SCALE = 1.0


def load_conditioning_image(path: str, width: int | None = None, height: int | None = None) -> PIL.Image.Image:
    """Load a conditioning image and (when a target size is given) cover-resize and center-crop to
    exactly ``width``x``height`` — so the pipeline's own resize is an identity and never distorts the
    aspect ratio. The training-matched H.264 CRF re-compression now lives in the pipeline itself
    (`image_crf`, auto-resolved to 18 for LTX-2.5), applied to the image we hand it."""
    img = PIL.Image.open(path).convert("RGB")
    if width and height:
        scale = max(width / img.width, height / img.height)
        img = img.resize((round(img.width * scale), round(img.height * scale)), PIL.Image.LANCZOS)
        left, top = (img.width - width) // 2, (img.height - height) // 2
        img = img.crop((left, top, left + width, top + height))
    return img


# Image-to-video sizing: the smaller side is pinned here and the longer side follows the input
# image's aspect ratio on the two-stage /64 grid.
I2V_SHORT_SIDE = 832
MAX_SIDE = 1536


def dims_for_image(image_w: int, image_h: int) -> tuple[int, int]:
    """Closest valid (height, width) to an uploaded image: smaller side fixed at ``I2V_SHORT_SIDE``,
    longer side the aspect-matched multiple of 64, capped at the slider maximum."""
    if image_w >= image_h:
        height = I2V_SHORT_SIDE
        width = min(MAX_SIDE, max(I2V_SHORT_SIDE, round(I2V_SHORT_SIDE * image_w / image_h / 64) * 64))
    else:
        width = I2V_SHORT_SIDE
        height = min(MAX_SIDE, max(I2V_SHORT_SIDE, round(I2V_SHORT_SIDE * image_h / image_w / 64) * 64))
    return height, width

print("[ltx25-diffusers] loading LTX-2.5 distilled (transformer + gemma4 + conv VAE + audio)...", flush=True)

# Module scope + .to("cuda") is the ZeroGPU pattern: weights placed on cuda at import are packed to
# disk by the backend and streamed into VRAM on the first @spaces.GPU entry. Loading inside the
# decorated call instead spends the whole allocation on ~60 GB of I/O; leaving them on the CPU gets
# the container OOM-killed, since transformer + encoder + connectors is ~68 GB of RAM.
# Snapshot first, without `transformer_full/`. `from_pretrained` builds its allow-patterns from every
# model-like file in the repo rather than from `model_index.json`, so it pulls BOTH DiTs -- 76 GB of
# transformer instead of 38 -- and fills the disk. Passing `ignore_patterns` to `from_pretrained` does
# not help: it is discarded before the download call.
MODEL_DIR = snapshot_download(
    MODEL_ID, ignore_patterns=["transformer_full/*"], token=HF_TOKEN, max_workers=8
)

pipe = LTX2Pipeline.from_pretrained(MODEL_DIR, dtype=torch.bfloat16)

# LTX-2.5's own decoder. It is NOT the pipeline's `vae`: encoding still goes through the convolutional
# AutoencoderKLLTX2Video (which is also what the latent upsampler needs), and this drives pixel decode.
diffusion_decoder = LTX2VideoDiffusionDecoderModel.from_pretrained(
    MODEL_DIR, subfolder="diffusion_decoder", dtype=torch.bfloat16
)
# The default processor builds a FlexAttention BlockMask; uncompiled that materialises the full score
# matrix, so NATTEN's fused kernels are the practical choice at video resolutions — and they are what
# the reference decoder calls. Fetched from the Hub (`shi-labs/natten`) via the `kernels` package.
diffusion_decoder.set_attn_processor(LTX2VideoVaeNeighborhoodNattenProcessor())
# Overlapping-tile decode: peak memory bounded by the tile size, not the video size.
diffusion_decoder.enable_tiling()

# ltx-2.3-spatial-upscaler-x2-1.1, converted to diffusers format. There is no 2.5-era upscaler; the
# partner README says to use the 2.3 one, and the distilled recipe requires it.
latent_upsampler = LTX2LatentUpsamplerModel.from_pretrained(
    MODEL_DIR, subfolder="latent_upsampler", dtype=torch.bfloat16
)

pipe.to("cuda")
diffusion_decoder.to("cuda")
latent_upsampler.to("cuda")

# The conv decoder is the fallback for large outputs, and untiled it OOMs there: stage 2 decodes at
# double the stage-1 resolution, which asked for >100 GB at 1088x1920. The reference script tiles too.
pipe.vae.enable_tiling()

AUDIO_SR = pipe.vocoder.config.output_sampling_rate

# Every auxiliary pipeline below wraps the SAME already-loaded component objects — no second copy of
# the 22B transformer or the 12B encoder.
decode_pipe = LTX2VideoDiffusionDecodePipeline(
    diffusion_decoder=diffusion_decoder, scheduler=pipe.scheduler
)
upsample_pipe = LTX2LatentUpsamplePipeline(vae=pipe.vae, latent_upsampler=latent_upsampler)

# Guarded so the Space still boots for text-to-video if image-to-video construction fails.
try:
    pipe_i2v = LTX2ImageToVideoPipeline(
        scheduler=pipe.scheduler,
        vae=pipe.vae,
        audio_vae=pipe.audio_vae,
        text_encoder=pipe.text_encoder,
        tokenizer=pipe.tokenizer,
        connectors=pipe.connectors,
        transformer=pipe.transformer,
        vocoder=pipe.vocoder,
        processor=getattr(pipe, "processor", None),
        prompt_enhancer=getattr(pipe, "prompt_enhancer", None),
        duration_head=getattr(pipe, "duration_head", None),
    )
    print(f"[ltx25-diffusers] ready, t2v + i2v (audio_sr={AUDIO_SR})", flush=True)
except Exception as exc:  # noqa: BLE001
    pipe_i2v = None
    print(f"[ltx25-diffusers] ready, t2v ONLY (i2v init failed: {exc!r})", flush=True)


# ---------------------------------------------------------------------------------------------
# AoTI: AOTInductor-compiled DiT blocks, built offline by the sibling Space
# `diffusers-internal-dev/LTX-2.5-aoti-compile` with dynamic token dims. Two artifacts because the
# graphs differ: t2v modulates with a broadcast [B, 1, ...] temb, i2v with a per-token [B, N, ...]
# one (conditioning tokens sit at t=0) — dispatched per call on temb's token dim. The .pt2 holds
# kernels only; weights come from each live block's state_dict, so eager fallback stays intact and
# a missing/incompatible artifact repo just means running uncompiled.
# ---------------------------------------------------------------------------------------------
AOTI_REPO = os.environ.get("LTX25_AOTI_REPO", "diffusers/LTX-2.5-distilled-aoti")

if os.environ.get("LTX25_AOTI", "1") != "0":
    try:
        from huggingface_hub import hf_hub_download
        from spaces.zero.torch.aoti import LazyAOTIModel, _shallow_clone_module

        _aoti = {
            variant: LazyAOTIModel(hf_hub_download(
                AOTI_REPO, "package.pt2", subfolder=f"LTX2VideoTransformerBlock.{variant}",
                token=HF_TOKEN,
            ))
            for variant in ("t2v", "i2v")
        }

        def _aoti_patch_block(block):
            weights = _shallow_clone_module(block).state_dict()
            t2v_fn = _aoti["t2v"].with_weights(weights)
            i2v_fn = _aoti["i2v"].with_weights(weights)

            def dispatch(*args, **kwargs):
                fn = t2v_fn if kwargs["temb"].shape[1] == 1 else i2v_fn
                return fn(*args, **kwargs)

            block.forward = dispatch

        _n_patched = 0
        for _m in pipe.transformer.modules():
            if _m.__class__.__name__ == "LTX2VideoTransformerBlock":
                _aoti_patch_block(_m)
                _n_patched += 1
        print(f"[aoti] patched {_n_patched} DiT blocks from {AOTI_REPO}", flush=True)
    except Exception as _aoti_exc:  # noqa: BLE001
        print(f"[aoti] running eager ({type(_aoti_exc).__name__}: {_aoti_exc})", flush=True)


# ---------------------------------------------------------------------------------------------
# Prompt enhancement — same mechanism and same Space as the native demo, so a prompt enhanced here
# and there is enhanced identically. Runs on a SEPARATE ZeroGPU Space (Gemma-4 E2B) over
# gradio_client, keeping the 12B enhancer off this Space's 22B memory budget.
# ---------------------------------------------------------------------------------------------
ENHANCER_SPACE = "diffusers-internal-dev/LTX-2.4-Prompt-Enhancer"
_enh = {"client": None, "built_at": 0.0}
# A Client is built once and reused, but the ZeroGPU proxy token it carries EXPIRES, so a
# long-lived client eventually fails every call with AppError("Expired ZeroGPU proxy token")
# and the fallback below silently hands the user their raw prompt back. Rebuild past this TTL,
# and on any failure retry once with a fresh client before giving up.
_ENH_CLIENT_TTL_S = 900

# Enhancement is a pure function of (prompt, image): the enhancer decodes greedily with a fixed seed,
# and its own code notes the seed is inert. So the same inputs always produce the same caption, and
# caching cannot change what a user gets — it only skips a redundant Gemma-4 round trip (which is a
# cold start plus a 12B load whenever the enhancer Space has gone to sleep).
#
# Keyed on the image as well as the prompt, because the enhancer both switches system prompt on
# image presence and actually looks at the pixels. Hashed by content, since Gradio writes each upload
# to a fresh temp path — keying on the path would miss every repeat.
_ENH_CACHE: OrderedDict[tuple[str, str | None], str] = OrderedDict()
_ENH_CACHE_MAX = 64


def _image_key(path: str | None) -> str | None:
    if not path:
        return None
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:16]


def _enhancer_client(fresh: bool = False) -> Client:
    if fresh or _enh["client"] is None or (time.monotonic() - _enh["built_at"]) > _ENH_CLIENT_TTL_S:
        # The enhancer Space sleeps when idle, and waking it means a ZeroGPU cold start plus a Gemma-4
        # load. httpx's default read timeout expires long before that, which silently dropped every
        # first-call enhancement back to the raw prompt.
        _enh["client"] = Client(ENHANCER_SPACE, token=HF_TOKEN, httpx_kwargs={"timeout": 300.0})
        _enh["built_at"] = time.monotonic()
    return _enh["client"]


def _enhance_remote(prompt: str, image_path: str | None) -> str:
    args = (prompt, handle_file(image_path) if image_path else None)
    try:
        return _enhancer_client().predict(*args, api_name="/enhance")
    except Exception as first:  # noqa: BLE001
        # Almost always the expired proxy token described above; a fresh client fixes it. Retried
        # once only, so a genuinely down enhancer still falls through to the caller's handler.
        print(f"[enhance] first attempt failed ({first!r}); retrying with a fresh client", flush=True)
        return _enhancer_client(fresh=True).predict(*args, api_name="/enhance")



def prep_prompt(prompt: str, image_path: str | None, do_enhance: bool) -> str:
    """Non-GPU step: rewrite the prompt before the GPU is acquired, so no GPU time is spent waiting on
    the enhancer. Falls back to the raw prompt if it is unavailable."""
    if not prompt or not prompt.strip():
        raise gr.Error("Please enter a prompt.")
    if not do_enhance:
        return prompt

    key = (prompt.strip(), _image_key(image_path))
    cached = _ENH_CACHE.get(key)
    if cached is not None:
        _ENH_CACHE.move_to_end(key)  # LRU: keep what people are actually iterating on
        print("[enhance] cache hit, skipping Gemma", flush=True)
        return cached

    try:
        enhanced = _enhance_remote(prompt.strip(), image_path) or prompt
    except Exception as e:  # noqa: BLE001
        # Surface it: a silent fallback is indistinguishable from a working enhancer in the output.
        print(f"[enhance] failed, using raw prompt: {e!r}", flush=True)
        gr.Warning(
            f"Prompt enhancement unavailable ({type(e).__name__}) — using your prompt as written."
        )
        return prompt

    # Only successes are cached, so a transient enhancer outage doesn't pin the raw prompt for good.
    _ENH_CACHE[key] = enhanced
    while len(_ENH_CACHE) > _ENH_CACHE_MAX:
        _ENH_CACHE.popitem(last=False)
    return enhanced


def _duration(prompt, image_path, height, width, num_frames, seed, decoder, auto_len=False,
              *args) -> int:
    """Estimate rather than a fixed ceiling, because ZeroGPU checks the *requested* duration against
    the visitor's remaining quota (not the actual runtime) and `size="xlarge"` doubles the request — so
    a flat maximum locks out anyone with a partly-spent quota, and a smaller request also ranks higher
    in the node queue.

    Calibrated, not guessed: 768x512x49 with the diffusion decoder measured **24.7s end to end on a
    COLD worker** (the first GPU call after a fresh boot, so weight streaming is included). The formula
    below returns ~63s for that shape — a ~2.5x margin. Stage 2 dominates the compute: 4x stage 1's
    tokens, for 3 of the 11 steps.

    With auto length the frame count is not known until the duration head has run, which happens inside
    this GPU call, so the reservation has to assume the cap. The 400s clamp binds only for the largest
    auto shapes, where the margin above absorbs it."""
    frames = AUTO_MAX_FRAMES if auto_len else int(num_frames)
    px = int(height) * int(width) * frames
    decode = 20 if decoder == "diffusion" else 8
    return int(min(400, max(60, 30 + px / 1_500_000 + decode)))


@spaces.GPU(duration=_duration, size="xlarge")
def generate(prompt, image_path, height, width, num_frames, seed, decoder, auto_len=False,
             progress=gr.Progress(track_tqdm=True)):
    """Two-stage distilled generation: 8 steps at half resolution, x2 latent upsample, 3 steps at full
    resolution, then decode. `image_path`, when supplied, conditions frame 0 (image-to-video).

    Returns the clip path and the realized frame count, which differs from `num_frames` when
    `auto_len` lets the duration head choose."""
    if image_path and pipe_i2v is None:
        raise gr.Error("Image-to-video is unavailable in this Space; remove the image to run text-to-video.")

    height, width, num_frames = int(height), int(width), int(num_frames)
    if height % 64 or width % 64:
        # The reference asserts this for two-stage: stage 1 is half of each axis and must still land on
        # the VAE's /32 spatial grid.
        raise gr.Error(f"Two-stage needs height and width divisible by 64 (got {height}x{width}).")

    active = pipe_i2v if image_path else pipe
    # ONE generator for the whole call, threaded through both stages and the decode, so the noise
    # stream advances exactly as it does in the reference.
    generator = torch.Generator("cuda").manual_seed(int(seed))

    # Stage 1 owns the length decision; `num_frames` is rebound to what it actually produced before
    # stage 2 runs, so it is deliberately NOT in `shared`. `num_frames=None` + a `max_seconds` cap is
    # the merged auto-duration API: the pipeline runs its duration head when no length is given.
    requested = None if auto_len else num_frames

    shared = dict(
        prompt=prompt,
        negative_prompt=DEFAULT_NEGATIVE_PROMPT,
        frame_rate=FRAME_RATE,
        guidance_scale=GUIDANCE_SCALE,
        audio_guidance_scale=AUDIO_GUIDANCE_SCALE,
        # The merged pipeline's guidance DEFAULTS are the SFT values and are gated independently of
        # guidance_scale: stg_scale=1.0 (> 0 -> ON) and modality_scale=3.0 (> 1 -> ON) each add a
        # blended extra transformer pass per step. The distilled reference is a single plain forward
        # (SimpleDenoiser), so every guidance knob is zeroed here explicitly — leaving them at their
        # defaults massively degrades distilled output (verified on the Egyptian-royal example).
        stg_scale=0.0,
        audio_stg_scale=0.0,
        modality_scale=1.0,
        audio_modality_scale=1.0,
        guidance_rescale=0.0,
        audio_guidance_rescale=0.0,
        spatio_temporal_guidance_blocks=None,
        generator=generator,
        return_dict=False,
    )
    if image_path:
        # Cropped (not squashed) to the target aspect, smaller side pinned by `dims_for_image`. The
        # pipeline itself applies the training-matched H.264 CRF re-compression (`image_crf` -> 18)
        # before its own (now identity) resize, at each stage.
        shared["image"] = load_conditioning_image(image_path, width, height)

    # ---- stage 1: half resolution, 8 distilled sigmas ----------------------------------------
    want = f"auto (<={AUTO_MAX_SECONDS:.0f}s)" if auto_len else num_frames
    print(f"[gen] stage 1 @ {width // 2}x{height // 2}, frames={want}", flush=True)
    s1_latents, s1_audio_latents = active(
        height=height // 2, width=width // 2, num_frames=requested,
        max_seconds=AUTO_MAX_SECONDS, sigmas=STAGE_1_SIGMAS,
        output_type="latent", **shared
    )

    # Recover the realized length from the latents ([B, C, F, H, W]) rather than re-predicting it.
    # Stage 2 has to use exactly what stage 1 produced; passing None again would run the duration
    # head a second time and be only incidentally the same answer.
    num_frames = (s1_latents.shape[2] - 1) * pipe.vae_temporal_compression_ratio + 1
    if auto_len:
        print(f"[gen] duration head chose {num_frames} frames "
              f"({num_frames / FRAME_RATE:.2f}s)", flush=True)

    # ---- x2 spatial latent upsample -----------------------------------------------------------
    # output_type="latent" already applied the latent statistics, and the upsampler is trained on
    # denormalized latents — which is its default expectation (`latents_normalized=False`).
    print("[gen] x2 latent upsample", flush=True)
    up_latents = upsample_pipe(
        latents=s1_latents, output_type="latent", return_dict=False
    )[0]

    # ---- stage 2: full resolution, 3 sigmas, reseeded from stage 1 ---------------------------
    # noise_scale == STAGE_2_SIGMAS[0] reproduces the reference's
    # `noised = noise_scale * noise + (1 - noise_scale) * latents` at the stage-2 entry sigma.
    # No height/width: stage 2 takes its size from the upsampled latents (model-card snippet).
    print(f"[gen] stage 2 @ {width}x{height}x{num_frames}", flush=True)
    want_latents = decoder == "diffusion"
    s2 = active(
        num_frames=num_frames,
        sigmas=STAGE_2_SIGMAS,
        latents=up_latents,
        audio_latents=s1_audio_latents,
        noise_scale=STAGE_2_SIGMAS[0],
        # "np", not "pt", on the conv path: encode_video hands frames to PyAV, which rejects a torch
        # tensor ("Expected numpy array with dtype `uint8` but got `float32`").
        output_type="latent" if want_latents else "np",
        **shared,
    )

    if want_latents:
        video_latents, audio_latents = s2
        # LTX-2.5's diffusion decoder. denormalize=False: output_type="latent" already applied the latent
        # statistics, so applying them again would rescale every channel by its std a second time.
        print("[gen] diffusion decode", flush=True)
        video = decode_pipe(
            video_latents, generator=generator, denormalize=False, output_type="np", return_dict=False
        )[0]
        # output_type="latent" skips the vocoder, so finish the audio by hand. These latents come back
        # denormalized already, which is what audio_vae.decode expects.
        audio_latents = audio_latents.to(pipe.audio_vae.dtype)
        mel = pipe.audio_vae.decode(audio_latents, return_dict=False)[0]
        audio = pipe.vocoder(mel)
    else:
        video, audio = s2

    # A unique path per call: handlers run concurrently on ZeroGPU, so a fixed filename would let two
    # requests clobber each other's output.
    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as fh:
        path = fh.name
    audio_kwargs = {}
    if audio is not None:
        audio_kwargs = dict(audio=audio[0].float().cpu(), audio_sample_rate=AUDIO_SR)
    encode_video(video[0], fps=FRAME_RATE, output_path=path, **audio_kwargs)
    return path, num_frames


def run(prompt, image_path, height, width, duration_s, seed, decoder, auto_len, randomize_seed,
        do_enhance):
    """CPU step (enhance, seed) then the GPU step, so the GPU is not held during enhancement."""
    if randomize_seed:
        seed = random.randint(0, MAX_SEED)
    num_frames = frames_from_duration(duration_s)
    used = prep_prompt(prompt, image_path, do_enhance)
    video, frames = generate(used, image_path, height, width, num_frames, seed, decoder, auto_len)
    # A plain string, not gr.update(visible=...): this handler is the Space's public API endpoint, and
    # returning an update would hand `gradio_client` callers a dict where they currently get text.
    return video, used, seed, f"{frames} frames ({frames / FRAME_RATE:.2f}s)"


DIFFUSERS_WEIGHTS_URL = "https://huggingface.co/Lightricks/LTX-2.5-Diffusers"
NATIVE_WEIGHTS_URL = "https://huggingface.co/Lightricks/LTX-2.5"
# PLACEHOLDER until the real blog URL exists.
BLOG_URL = "https://huggingface.co/Lightricks/LTX-2.5-Diffusers"

INTRO = f"""# ⚗️ LTX-2.5

<div>
  <a href="{NATIVE_WEIGHTS_URL}" target="_blank" rel="noopener"><strong>[ native weights ]</strong></a> &nbsp;
  <a href="{DIFFUSERS_WEIGHTS_URL}" target="_blank" rel="noopener"><strong>[ diffusers weights ]</strong></a> &nbsp;
  <a href="{BLOG_URL}" target="_blank" rel="noopener"><strong>[ blog ]</strong></a>
</div>

**LTX-2.5** Distilled (22B) — video with synchronized audio, 8 + 3 steps, no CFG.
"""

# .main.fillable keeps the column from sprawling on wide monitors; the .dark rule stops the
# container inheriting a washed-out text colour in dark mode.
CSS = """
.main.fillable {max-width: 1200px !important}
.dark .gradio-container { color: var(--body-text-color); }
"""

# Rows carry their own settings, in `_INPUTS` order:
#   prompt, image, height, width, duration (s), seed, decoder, auto_len, randomize_seed, do_enhance
# Image rows use the exact resolution `dims_for_image` picks for their image (smaller side 832), so a
# cached example matches what uploading that same image produces.
_EX_TAIL = [42, "conv", False, False, True]
EXAMPLES = [
    ["A red fox trots through a snowy pine forest at golden hour, camera tracking alongside, "
     "paws crunching in the snow", None, 832, 1472, 2.0, *_EX_TAIL],
    ["Waves crash against dark rocks at sunset, sea spray catching the light, gulls calling "
     "overhead", None, 832, 1472, 2.0, *_EX_TAIL],
    ["The kingfisher launches from the branch and skims low over the water, wings beating fast, "
     "droplets trailing behind", "examples/bird_kingfisher.jpg", 832, 1280, 2.0, *_EX_TAIL],
    ["The green aurora ripples across the starry night sky above the snow-capped mountains, "
     "wind gusting", "examples/aurora.jpg", 832, 1344, 2.0, *_EX_TAIL],
    ["Pink cherry-blossom petals drift down and gently ripple the calm pond",
     "examples/cherry_blossom_pond.jpg", 832, 1344, 2.0, *_EX_TAIL],
    # Dialogue + a single push-in, at the settings this was generated and checked at: conv decode so
    # stage 2 can tile at this size, and no enhancement, since the prompt is already in caption style.
    ["Egyptian royal in blue-and-gold headdress and high collar, white dress with golden embroidery "
     "and armbands, desert, robot soldiers in formation left and right. She walks steadily forward, "
     "head held level and gaze fixed ahead\u2014no dipping or lowering of the head. The camera performs a "
     "single, smooth push-in only: starting in a wider shot of her, the robots, and the desert, it "
     "moves steadily forward until she is in a medium or medium-close frame, then holds. She stops, "
     "posture and head still upright, and says: \"The old gods are silent. I am not.\" Robot soldiers "
     "shift or march in place; sand and fabric move with the wind. No pull-back; the only camera move "
     "is the continuous push-in.",
     None, 832, 1472, 5.0, 42, "conv", False, False, False],
]

with gr.Blocks(title="LTX-2.5 distilled · diffusers") as demo:
    gr.Markdown(INTRO)
    with gr.Row():
        with gr.Column():
            image = gr.Image(label="Input image (optional → image-to-video)", type="filepath")
            prompt = gr.Textbox(label="Prompt", lines=4)
            with gr.Accordion("Settings", open=False):
                with gr.Row():
                    width = gr.Slider(512, MAX_SIDE, value=832, step=64, label="Width (final)")
                    height = gr.Slider(512, MAX_SIDE, value=1472, step=64, label="Height (final)")
                duration = gr.Slider(
                    1.0, 5.0, value=2.0, step=0.5, label="Duration (seconds, 24 fps)",
                    info="Snapped to the VAE's frame grid (8k+1 frames).",
                )
                auto_len = gr.Checkbox(
                    value=False, label=f"Auto length — let the model choose (≤{AUTO_MAX_SECONDS:.0f}s)",
                    info="Uses LTX-2.5's duration head to pick the length from the prompt, overriding the "
                         "slider above. Off by default: the length is only known once the run is "
                         "already on the GPU, so an auto run has to reserve ZeroGPU time for the full "
                         f"{AUTO_MAX_SECONDS:.0f}s worst case whatever it ends up generating.",
                )
                gr.Number(
                    value=11, interactive=False, precision=0,
                    label="Steps (fixed: 8 in stage 1 + 3 in stage 2)",
                )
                decoder = gr.Radio(
                    ["diffusion", "conv"], value="conv", label="Video decoder",
                    info="conv = the fast convolutional VAE decoder (default). diffusion = LTX-2.5's "
                         "own neighborhood-attention diffusion decoder (tiled), matching the native "
                         "demo at a higher decode cost.",
                )
                with gr.Row():
                    seed = gr.Slider(0, MAX_SEED, value=42, step=1, label="Seed")
                    randomize_seed = gr.Checkbox(value=True, label="Randomize seed")
                enhance_toggle = gr.Checkbox(
                    value=True, label="Enhance prompt (Gemma-4)",
                    info="Rewrites your prompt into a detailed LTX-2.5-style caption via a "
                         "separate enhancer Space.",
                )
            go = gr.Button("Generate", variant="primary")
        with gr.Column():
            out_video = gr.Video(label="Result (with audio)", autoplay=True)
            enhanced_box = gr.Textbox(
                label="Prompt sent to the model (the enhanced one, when enhancement is on)",
                info="Copy it to reuse verbatim, or paste it back into the prompt box with "
                     "enhancement off to tweak it by hand.",
                lines=6, interactive=False, buttons=["copy"],  # gradio 6 dropped show_copy_button; "copy" is the built-in button
            )
            used_seed = gr.Number(label="Seed used", interactive=False)
            used_length = gr.Textbox(
                label="Length generated", interactive=False,
                info="What the duration head chose, when auto length is on.",
            )

    _INPUTS = [prompt, image, height, width, duration, seed, decoder, auto_len, randomize_seed,
               enhance_toggle]
    _OUTPUTS = [out_video, enhanced_box, used_seed, used_length]

    def set_dims_from_image(path):
        """Snap the size sliders to the closest valid resolution for the uploaded image (smaller side
        832, longer side aspect-matched on the /64 grid). Bound to `.upload`, not `.change`, so
        example rows — which set the image programmatically alongside their own sizes — never race it."""
        if not path:
            return gr.update(), gr.update()
        with PIL.Image.open(path) as im:
            h, w = dims_for_image(*im.size)
        return h, w

    image.upload(set_dims_from_image, inputs=image, outputs=[height, width])
    image.clear(lambda: (1472, 832), outputs=[height, width])

    go.click(run, _INPUTS, _OUTPUTS)

    def run_example(example_prompt, example_image, ex_height, ex_width, ex_duration,
                    ex_seed, ex_decoder, ex_auto_len, ex_randomize, ex_enhance):
        """Drive the SAME default path as the button (enhance -> two-stage generate) so a cached
        example reflects what a user actually gets. Fixed seed, no randomization.

        Enhancement happens FIRST and must actually have rewritten the prompt. gradio caches example
        outputs, so a run where the enhancer silently fell back would pin the raw prompt as the
        "enhanced" one for every later visitor — which is exactly what happened once, via an expired
        ZeroGPU proxy token. Failing before the GPU work is spent keeps the poisoned row out of the
        cache and costs nothing.
        """
        used = prep_prompt(example_prompt, example_image, ex_enhance)
        if ex_enhance and used.strip() == (example_prompt or "").strip():
            raise gr.Error(
                "Prompt enhancer unavailable, so this example was not cached — try again shortly."
            )
        # auto_len=False: cached rows must be reproducible, and a cached auto row would also hide which
        # length the head picked behind a fixed thumbnail.
        video, frames = generate(used, example_image, ex_height, ex_width,
                                 frames_from_duration(ex_duration),
                                 ex_seed, ex_decoder, ex_auto_len)
        return video, used, ex_seed, f"{frames} frames ({frames / FRAME_RATE:.2f}s)"

    gr.Examples(
        examples=EXAMPLES,
        inputs=_INPUTS,
        outputs=_OUTPUTS,
        fn=run_example,
        # lazy, not eager: ZeroGPU has no GPU attached at startup, so eager caching would fail.
        cache_examples=True,
        cache_mode="lazy",
        label="Examples — text-to-video and image-to-video",
    )

if __name__ == "__main__":
    # gradio 6 takes `css`/`theme` on launch(), not on gr.Blocks().
    demo.launch(theme=gr.themes.Citrus(), css=CSS, mcp_server=True)
