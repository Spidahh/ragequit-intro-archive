import concurrent.futures,json,time,os
from pathlib import Path
os.environ['HF_HUB_DISABLE_PROGRESS_BARS']='1'
from huggingface_hub import hf_hub_download,HfApi
base=Path('C:/Users/magis/.codex/tools/comfyui-ltx/models')
jobs=[('Lightricks/LTX-2.3-fp8','ltx-2.3-22b-dev-fp8.safetensors','checkpoints'),
      ('Comfy-Org/ltx-2','split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors','text_encoders'),
      ('Comfy-Org/ltx-2.3','split_files/loras/ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors','loras'),
      ('Lightricks/LTX-2.3','ltx-2.3-spatial-upscaler-x2-1.1.safetensors','latent_upscale_models')]
report={'request':'D0949/D0955','spend':0,'source':'Official Comfy-Org LTX-2.3 T2V template','status':'downloading','files':[]}
receipt=Path(__file__).parent/'downloads.json'
def save():receipt.write_text(json.dumps(report,indent=2),encoding='utf-8')
api=HfApi()
for repo,file,directory in jobs:
    info=api.model_info(repo,files_metadata=True)
    entry=next(x for x in info.siblings if x.rfilename==file)
    report['files'].append({'repo':repo,'revision':info.sha,'file':file,'directory':directory,
                            'bytes':entry.size,'sha256':entry.lfs.sha256 if entry.lfs else None,'status':'pending'})
save()
def get(row):
    target=base/row['directory'];target.mkdir(parents=True,exist_ok=True)
    # Download directly to the correct directory; nested source paths are then
    # moved within that directory, avoiding duplicate multi-GB cache copies.
    row['status']='downloading';save()
    print('Downloading '+row['file']+' ('+str(round(row['bytes']/1e9,2))+' GB)',flush=True)
    path=Path(hf_hub_download(row['repo'],row['file'],revision=row['revision'],local_dir=target))
    final=target/path.name
    if path!=final:path.replace(final)
    row.update(status='complete',path=str(final),finished=time.strftime('%Y-%m-%dT%H:%M:%S'))
    save();print('Complete '+final.name,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    futures=[pool.submit(get,row) for row in report['files']]
    for f in concurrent.futures.as_completed(futures):f.result()
report['status']='complete';save()
