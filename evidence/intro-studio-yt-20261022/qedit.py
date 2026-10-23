"""Fotogramma chiave con Qwen-Image-Edit 2511 (Apache 2.0) in ComfyUI locale.
uso: python qedit.py prompt.txt nome img1 [img2 [img3]] [--seed N] [--steps 40] [--cfg 4]
img1 decide inquadratura e misura dell'uscita; img2/img3 sono riferimenti (i personaggi veri)."""
import argparse, json, time, urllib.request, os, shutil, uuid
U = "http://127.0.0.1:8188"; OUT = "C:/Users/magis/AppData/Local/Comfy-Desktop/ComfyUI-Shared/output"; INP = "C:/Users/magis/AppData/Local/Comfy-Desktop/ComfyUI-Shared/input"
a = argparse.ArgumentParser(); a.add_argument("prompt"); a.add_argument("name"); a.add_argument("images", nargs="+")
a.add_argument("--seed", type=int, default=11); a.add_argument("--steps", type=int, default=40); a.add_argument("--cfg", type=float, default=4.0); a.add_argument("--lightning", action="store_true")
x = a.parse_args()
text = open(x.prompt, encoding="utf-8").read().strip()
g = {
 "unet": {"class_type": "UNETLoader", "inputs": {"unet_name": "qwen_image_edit_2511_int8_convrot.safetensors", "weight_dtype": "default"}},
 "clip": {"class_type": "CLIPLoader", "inputs": {"clip_name": "qwen_2.5_vl_7b_fp8_scaled.safetensors", "type": "qwen_image", "device": "default"}},
 "vae": {"class_type": "VAELoader", "inputs": {"vae_name": "qwen_image_vae.safetensors"}},
 "ms": {"class_type": "ModelSamplingAuraFlow", "inputs": {"model": ["unet", 0], "shift": 3.1}},
 "norm": {"class_type": "CFGNorm", "inputs": {"model": ["ms", 0], "strength": 1.0}},
}
if x.lightning:
    g["lora"] = {"class_type": "LoraLoaderModelOnly", "inputs": {"model": ["norm", 0], "lora_name": "Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors", "strength_model": 1.0}}
    x.steps, x.cfg = 4, 1.0
for i, src in enumerate(x.images[:3], 1):
    nm = f"rq_{uuid.uuid4().hex[:8]}_{os.path.basename(src)}"; shutil.copy(src, os.path.join(INP, nm))
    g[f"img{i}"] = {"class_type": "LoadImage", "inputs": {"image": nm}}
    g[f"sc{i}"] = {"class_type": "FluxKontextImageScale", "inputs": {"image": [f"img{i}", 0]}}
def enc(p):
    d = {"clip": ["clip", 0], "prompt": p, "vae": ["vae", 0]}
    for i in range(1, min(3, len(x.images)) + 1): d[f"image{i}"] = [f"sc{i}", 0]
    return d
g["pos"] = {"class_type": "TextEncodeQwenImageEditPlus", "inputs": enc(text)}
g["neg"] = {"class_type": "TextEncodeQwenImageEditPlus", "inputs": enc("")}
g["posm"] = {"class_type": "FluxKontextMultiReferenceLatentMethod", "inputs": {"conditioning": ["pos", 0], "reference_latents_method": "index_timestep_zero"}}
g["negm"] = {"class_type": "FluxKontextMultiReferenceLatentMethod", "inputs": {"conditioning": ["neg", 0], "reference_latents_method": "index_timestep_zero"}}
g["lat"] = {"class_type": "VAEEncode", "inputs": {"pixels": ["sc1", 0], "vae": ["vae", 0]}}
g["ks"] = {"class_type": "KSampler", "inputs": {"model": ["lora" if x.lightning else "norm", 0], "seed": x.seed, "steps": x.steps, "cfg": x.cfg, "sampler_name": "euler", "scheduler": "simple", "positive": ["posm", 0], "negative": ["negm", 0], "latent_image": ["lat", 0], "denoise": 1.0}}
g["dec"] = {"class_type": "VAEDecode", "inputs": {"samples": ["ks", 0], "vae": ["vae", 0]}}
g["save"] = {"class_type": "SaveImage", "inputs": {"images": ["dec", 0], "filename_prefix": f"ragequit_intro/keys/{x.name}"}}
try:
    pid = json.load(urllib.request.urlopen(urllib.request.Request(U + "/prompt", json.dumps({"prompt": g}).encode(), {"Content-Type": "application/json"})))["prompt_id"]
except urllib.error.HTTPError as e:
    print(e.read().decode()[:3000]); raise
t0 = time.time(); print("queued", x.name, pid, flush=True)
while True:
    time.sleep(3); h = json.load(urllib.request.urlopen(f"{U}/history/{pid}"))
    if pid in h:
        st = h[pid]["status"]
        if st.get("status_str") == "error": print("ERROR", json.dumps(st)[:3000]); raise SystemExit(1)
        for o in h[pid]["outputs"].values():
            for v in o.get("images", []):
                f = os.path.join(OUT, v.get("subfolder", ""), v["filename"]); dst = os.path.join(os.path.dirname(os.path.abspath(__file__)), "keys", x.name + ".png"); shutil.copy(f, dst); print("OUT", dst)
        json.dump(dict(name=x.name, prompt=text, images=x.images, seed=x.seed, steps=x.steps, cfg=x.cfg), open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "keys", x.name + ".json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        print("done in", round(time.time() - t0), "s"); break
