"""Local LTX-2.3 generation using the official Comfy-Org two-stage recipe.

Requires the separately installed local ComfyUI and recorded public model files.
Optional first-frame guidance uses the template's native LTX nodes.
No cloud APIs, account credentials or billing. Never replaces the game movie.
"""
import argparse,json,hashlib,time,subprocess
from pathlib import Path
import requests

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'art/intro/ltx23-20261022'
SERVER='http://127.0.0.1:8197'
CHECKPOINT='ltx-2.3-22b-dev-fp8.safetensors'
LORA='ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors'
ENCODER='gemma_3_12B_it_fp4_mixed.safetensors'
UPSCALER='ltx-2.3-spatial-upscaler-x2-1.1.safetensors'

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def build(seed=144713,seconds=5,width=1024,height=576,image=None,quality=False,native=False,vbvr=False):
    text=(OUT/'scene-prompt.txt').read_text(encoding='utf-8')
    frames=seconds*24+1
    g={}
    def n(i,kind,**inputs):g[str(i)]={'class_type':kind,'inputs':inputs}
    def link(i,slot=0):return [str(i),slot]
    n(1,'CheckpointLoaderSimple',ckpt_name=CHECKPOINT)
    n(2,'LTXAVTextEncoderLoader',text_encoder=ENCODER,ckpt_name=CHECKPOINT,device='default')
    n(3,'CLIPTextEncode',clip=link(2),text=text)
    n(4,'CLIPTextEncode',clip=link(2),text='')
    n(5,'LTXVConditioning',positive=link(3),negative=link(4),frame_rate=24.)
    n(6,'LoraLoaderModelOnly',model=link(1),lora_name=LORA,strength_model=.5)
    n(7,'LTXVAudioVAELoader',ckpt_name=CHECKPOINT)
    n(8,'EmptyLTXVLatentVideo',width=width//2,height=height//2,length=frames,batch_size=1)
    n(9,'LTXVEmptyLatentAudio',audio_vae=link(7),frames_number=frames,frame_rate=24,batch_size=1)
    n(10,'LTXVConcatAVLatent',video_latent=link(8),audio_latent=link(9))
    n(11,'RandomNoise',noise_seed=seed)
    n(12,'CFGGuider',model=link(6),positive=link(5),negative=link(5,1),cfg=1.)
    n(13,'KSamplerSelect',sampler_name='euler')
    n(14,'ManualSigmas',sigmas='1.0, 0.99375, 0.9875, 0.98125, 0.975, 0.909375, 0.725, 0.421875, 0.0')
    n(15,'SamplerCustomAdvanced',noise=link(11),guider=link(12),sampler=link(13),sigmas=link(14),latent_image=link(10))
    n(16,'LTXVSeparateAVLatent',av_latent=link(15))
    n(17,'LTXVCropGuides',positive=link(5),negative=link(5,1),latent=link(16))
    n(18,'LatentUpscaleModelLoader',model_name=UPSCALER)
    n(19,'LTXVLatentUpsampler',samples=link(16),upscale_model=link(18),vae=link(1,2))
    n(20,'LTXVConcatAVLatent',video_latent=link(19),audio_latent=link(16,1))
    n(21,'CFGGuider',model=link(6),positive=link(17),negative=link(17,1),cfg=1.)
    n(22,'RandomNoise',noise_seed=42)
    n(23,'ManualSigmas',sigmas='0.85, 0.7250, 0.4219, 0.0')
    n(24,'SamplerCustomAdvanced',noise=link(22),guider=link(21),sampler=link(13),sigmas=link(23),latent_image=link(20))
    n(25,'LTXVSeparateAVLatent',av_latent=link(24))
    n(26,'VAEDecodeTiled',samples=link(25),vae=link(1,2),tile_size=768,overlap=64,temporal_size=4096,temporal_overlap=4)
    n(27,'LTXVAudioVAEDecode',samples=link(25,1),audio_vae=link(7))
    n(28,'CreateVideo',images=link(26),audio=link(27),fps=24.)
    n(29,'SaveVideo',video=link(28),filename_prefix='RAGEQUIT_LTX23/duel-'+str(seed),format='auto')
    if image:
        n(30,'LoadImage',image=image)
        n(31,'LTXVPreprocess',image=link(30),img_compression=18)
        n(32,'LTXVImgToVideoInplace',vae=link(1,2),image=link(31),latent=link(8),strength=.7,bypass=False)
        g['10']['inputs']['video_latent']=link(32)
        n(33,'LTXVImgToVideoInplace',vae=link(1,2),image=link(31),latent=link(19),strength=1.,bypass=False)
        g['20']['inputs']['video_latent']=link(33)
    if quality:
        n(34,'LTXVSpatioTemporalGuidance',model=link(1),scale=1.,blocks='29',start_percent=0.,end_percent=1.)
        n(12,'LTXVDualCFGGuider',model=link(34),positive=link(5),negative=link(5,1),video_cfg=3.,audio_cfg=7.)
        n(14,'LTXVScheduler',steps=30,max_shift=2.05,base_shift=.95,stretch=True,terminal=.1,latent=link(8))
        g['4']['inputs']['text']='Blurry, distorted anatomy, extra limbs, changing outfits, disappearing weapons, merging people, slow motion.'
        if image:g['32']['inputs']['strength']=1.
    if vbvr:
        n(35,'LoraLoaderModelOnly',model=link(1),lora_name='Ltx2.3-Licon-VBVR-I2V-390K-R32.safetensors',strength_model=.75)
        if quality:g['34']['inputs']['model']=link(35)
        else:g['6']['inputs']['model']=link(35)
    if native:
        g['8']['inputs'].update(width=width,height=height)
        g['25']['inputs']['av_latent']=link(15)
    return g

def submit(args):
    OUT.mkdir(parents=True,exist_ok=True)
    for attempt in range(30):
        try:
            requests.get(SERVER+'/system_stats',timeout=3).raise_for_status()
            break
        except requests.RequestException:
            if attempt==29:raise
            time.sleep(1)
    g=build(args.seed,args.seconds,args.width,args.height,args.image,args.quality,args.native,args.vbvr)
    (OUT/'workflow-api.json').write_text(json.dumps(g,indent=2),encoding='utf-8')
    req=requests.post(SERVER+'/prompt',json={'prompt':g,'client_id':'ragequit-intro-ltx23'},timeout=60)
    result=req.json()
    (OUT/'submission.json').write_text(json.dumps({'request':'D0949/D0955','result':result,
        'http_status':req.status_code,'seed':args.seed,'seconds':args.seconds,'size':[args.width,args.height],
        'spend':0,'time':time.strftime('%Y-%m-%dT%H:%M:%S'),'source':'Comfy-Org official LTX-2.3 T2V workflow',
        'changes':('Dev first stage: no distilled LoRA, 30-step LTX scheduler, dual CFG 3/7, STG 1 on block 29; '
                   'distilled second stage unchanged. Prompt enhancement omitted.' if args.quality else
                   'Prompt enhancement omitted; original two-stage distilled sigma schedules.'),
        'image_guide':args.image,
        'dev_guidance':args.quality,
        'single_stage_native':args.native,'vbvr_strength':.75 if args.vbvr else 0,
        'image_guide_sha256':sha(OUT/'reference.png') if args.image else None,
        'prompt_sha256':sha(OUT/'scene-prompt.txt')},indent=2),encoding='utf-8')
    print(json.dumps(result),flush=True);req.raise_for_status()

def status():
    submission=json.loads((OUT/'submission.json').read_text())
    pid=submission['result']['prompt_id']
    h=requests.get(SERVER+'/history/'+pid,timeout=30).json()
    if h:
        (OUT/'history.json').write_text(json.dumps(h,indent=2),encoding='utf-8')
        row=h[pid]
        state=row.get('status',{})
        errors=[{'node':m[1].get('node_id'),'message':m[1].get('exception_message')}
                for m in state.get('messages',[]) if m[0]=='execution_error']
        print(json.dumps({'status':state.get('status_str'),'completed':state.get('completed'),
                          'errors':errors,'outputs':row.get('outputs')}))
    else:
        queue=requests.get(SERVER+'/queue',timeout=30).json()
        print(json.dumps({'status':'running or queued','prompt_id':pid,
                          'running':len(queue.get('queue_running',[])),
                          'pending':len(queue.get('queue_pending',[]))}))

def finish():
    """Package a selected native take at original speed and frame rate."""
    source=OUT/'scene-native.mp4'
    probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams',
        '-show_format','-of','json',str(source)]))
    v=next(s for s in probe['streams'] if s['codec_type']=='video')
    action=float(v['duration']);duration=round((action+2.05)*24)/24
    graph=(f'[0:v]scale=1920:1080:flags=lanczos,setsar=1,fps=24[act];'
        f'color=c=black:s=1920x1080:r=24:d={duration-action}[black];'
        '[act][black]concat=n=2:v=1:a=0[bg];'
        f'[1:v]scale=1270:-1,format=rgba,fade=t=in:st={action+.07}:d=0.12:alpha=1[letters];'
        f'[2:v]scale=1270:-1,format=rgba,fade=t=in:st={action}:d=0.08:alpha=1[slash];'
        f"[bg][slash]overlay=x='(W-w)/2+max(0,{action+.1}-t)*5000':y='(H-h)/2':enable='gte(t,{action})'[s];"
        f"[s][letters]overlay=x='(W-w)/2':y='(H-h)/2':enable='gte(t,{action+.07})',fade=t=out:st={duration-.18}:d=0.18[v];"
        f'[0:a]aresample=48000,apad,atrim=duration={duration},volume=0.7[native];'
        '[3:a]aresample=48000,adelay=3200|3200,volume=0.88[voice];'
        f'[native][voice]amix=inputs=2:normalize=0,alimiter=limit=0.95,atrim=duration={duration},afade=t=out:st={duration-.15}:d=0.15[a]')
    final=OUT/'ragequit-ltx23.mp4'
    subprocess.run(['ffmpeg','-v','warning','-y','-i',str(source),
        '-loop','1','-framerate','24','-i',str(ROOT/'art/ui/menu/T_UI_Logo.png'),
        '-loop','1','-framerate','24','-i',str(ROOT/'art/ui/menu/T_UI_LogoSlash.png'),
        '-i',str(ROOT/'art/intro/announcer-v2.wav'),'-filter_complex',graph,
        '-map','[v]','-map','[a]','-t',str(duration),'-r','24','-c:v','libx264',
        '-crf','16','-preset','slow','-pix_fmt','yuv420p','-c:a','aac','-b:a','256k',
        '-ar','48000','-ac','2','-movflags','+faststart',str(final)],check=True)
    subprocess.run(['ffmpeg','-v','error','-i',str(final),'-f','null','-'],check=True)
    final_probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams',
        '-show_format','-of','json',str(final)]))
    report={'native_sha256':sha(source),'output_sha256':sha(final),'native_probe':probe,
        'reference_sha256':sha(OUT/'reference.png'),
        'prompt_sha256':sha(OUT/'scene-prompt.txt'),
        'workflow_sha256':sha(OUT/'workflow-api.json'),
        'output_probe':final_probe,'speed':1,'interpolation':False,'upscale':'Lanczos to 1080p',
        'action_seconds':action,'logo_at':action,'voice_at':3.2,
        'voice_sha256':sha(ROOT/'art/intro/announcer-v2.wav'),
        'full_decode':'passed','author_approval':'pending','installed':False,'spend':0,
        'installed_movie_sha256':sha(ROOT/'unreal/Content/Movies/RagequitIntro.mp4')}
    (OUT/'provenance.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps({'output':str(final),'duration':duration}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['submit','status','finish'])
    p.add_argument('--seed',type=int,default=144713);p.add_argument('--seconds',type=int,default=5)
    p.add_argument('--width',type=int,default=1024);p.add_argument('--height',type=int,default=576)
    p.add_argument('--image',help='Reference filename already copied into the owned ComfyUI input directory')
    p.add_argument('--quality',action='store_true',help='Dev first stage, 30 steps, dual CFG 3/7 and native STG 1')
    p.add_argument('--native',action='store_true',help='Generate directly at requested resolution, omit latent upscale/refinement')
    p.add_argument('--vbvr',action='store_true',help='Use public LiconStudio VBVR 390K adapter at 0.75')
    args=p.parse_args()
    {'submit':lambda:submit(args),'status':status,'finish':finish}[args.mode]()
