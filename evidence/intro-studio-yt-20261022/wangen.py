"""Anima un fotogramma chiave con Wan 2.2 i2v 14B (Apache 2.0), passi pieni senza LoRA veloce (la LoRA rallenta il moto).
uso: python wangen.py prompt.txt nome start.png [--end end.png] [--frames 49] [--w 1280 --h 720] [--seed 1] [--steps 20]"""
import argparse, json, time, urllib.request, os, shutil, uuid
U = "http://127.0.0.1:8188"; OUT = "C:/Users/magis/AppData/Local/Comfy-Desktop/ComfyUI-Shared/output"; INP = "C:/Users/magis/AppData/Local/Comfy-Desktop/ComfyUI-Shared/input"
NEG = "slow motion, static, still image, frozen, slideshow, panning over a still picture, blurry details, overexposed, washed out, subtitles, text, watermark, logo, worst quality, low quality, jpeg artifacts, ugly, deformed, extra limbs, extra fingers, bad hands, bad face, mutated, fused fingers, messy background, walking backwards, feathered wings"
a = argparse.ArgumentParser(); a.add_argument("prompt"); a.add_argument("name"); a.add_argument("start")
a.add_argument("--end"); a.add_argument("--frames", type=int, default=49); a.add_argument("--w", type=int, default=1280); a.add_argument("--h", type=int, default=720)
a.add_argument("--seed", type=int, default=1); a.add_argument("--steps", type=int, default=20); a.add_argument("--cfg", type=float, default=3.5); a.add_argument("--shift", type=float, default=5.0)
x = a.parse_args()
text = open(x.prompt, encoding="utf-8").read().strip(); split = x.steps // 2
def up(p):
    nm = f"rq_{uuid.uuid4().hex[:8]}_{os.path.basename(p)}"; shutil.copy(p, os.path.join(INP, nm)); return nm
g = {
 "hi": {"class_type": "UNETLoader", "inputs": {"unet_name": "wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors", "weight_dtype": "default"}},
 "lo": {"class_type": "UNETLoader", "inputs": {"unet_name": "wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors", "weight_dtype": "default"}},
 "mhi": {"class_type": "ModelSamplingSD3", "inputs": {"model": ["hi", 0], "shift": x.shift}},
 "mlo": {"class_type": "ModelSamplingSD3", "inputs": {"model": ["lo", 0], "shift": x.shift}},
 "clip": {"class_type": "CLIPLoader", "inputs": {"clip_name": "umt5_xxl_fp8_e4m3fn_scaled.safetensors", "type": "wan", "device": "default"}},
 "vae": {"class_type": "VAELoader", "inputs": {"vae_name": "wan_2.1_vae.safetensors"}},
 "pos": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["clip", 0], "text": text}},
 "neg": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["clip", 0], "text": NEG}},
 "s": {"class_type": "LoadImage", "inputs": {"image": up(x.start)}},
}
if x.end:
    g["e"] = {"class_type": "LoadImage", "inputs": {"image": up(x.end)}}
    g["i2v"] = {"class_type": "WanFirstLastFrameToVideo", "inputs": {"positive": ["pos", 0], "negative": ["neg", 0], "vae": ["vae", 0], "width": x.w, "height": x.h, "length": x.frames, "batch_size": 1, "start_image": ["s", 0], "end_image": ["e", 0]}}
else:
    g["i2v"] = {"class_type": "WanImageToVideo", "inputs": {"positive": ["pos", 0], "negative": ["neg", 0], "vae": ["vae", 0], "width": x.w, "height": x.h, "length": x.frames, "batch_size": 1, "start_image": ["s", 0]}}
g["k1"] = {"class_type": "KSamplerAdvanced", "inputs": {"model": ["mhi", 0], "add_noise": "enable", "noise_seed": x.seed, "steps": x.steps, "cfg": x.cfg, "sampler_name": "euler", "scheduler": "simple", "positive": ["i2v", 0], "negative": ["i2v", 1], "latent_image": ["i2v", 2], "start_at_step": 0, "end_at_step": split, "return_with_leftover_noise": "enable"}}
g["k2"] = {"class_type": "KSamplerAdvanced", "inputs": {"model": ["mlo", 0], "add_noise": "disable", "noise_seed": 0, "steps": x.steps, "cfg": x.cfg, "sampler_name": "euler", "scheduler": "simple", "positive": ["i2v", 0], "negative": ["i2v", 1], "latent_image": ["k1", 0], "start_at_step": split, "end_at_step": 10000, "return_with_leftover_noise": "disable"}}
g["dec"] = {"class_type": "VAEDecode", "inputs": {"samples": ["k2", 0], "vae": ["vae", 0]}}
g["vid"] = {"class_type": "CreateVideo", "inputs": {"images": ["dec", 0], "fps": 16}}
g["save"] = {"class_type": "SaveVideo", "inputs": {"video": ["vid", 0], "filename_prefix": f"ragequit_intro/clips/{x.name}", "format": "mp4", "codec": "h264"}}
try:
    pid = json.load(urllib.request.urlopen(urllib.request.Request(U + "/prompt", json.dumps({"prompt": g}).encode(), {"Content-Type": "application/json"})))["prompt_id"]
except urllib.error.HTTPError as e:
    print(e.read().decode()[:3000]); raise
t0 = time.time(); print("queued", x.name, pid, flush=True)
while True:
    time.sleep(5); h = json.load(urllib.request.urlopen(f"{U}/history/{pid}"))
    if pid in h:
        st = h[pid]["status"]
        if st.get("status_str") == "error":
            m = [mm for mm in st["messages"] if mm[0] == "execution_error"]; print("ERROR", (m[0][1]["exception_message"] if m else json.dumps(st))[:600]); raise SystemExit(1)
        for o in h[pid]["outputs"].values():
            for v in o.get("images", []) + o.get("videos", []):
                f = os.path.join(OUT, v.get("subfolder", ""), v["filename"]); dst = os.path.join(os.path.dirname(os.path.abspath(__file__)), "clips", x.name + ".mp4"); shutil.copy(f, dst); print("OUT", dst)
        json.dump(dict(name=x.name, prompt=text, start=x.start, end=x.end, frames=x.frames, w=x.w, h=x.h, seed=x.seed, steps=x.steps, cfg=x.cfg), open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "clips", x.name + ".json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        print("done in", round(time.time() - t0), "s"); break
