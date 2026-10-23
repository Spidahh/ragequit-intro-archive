"""D0936: continuous retiming and replacement of the malformed archer shot.

Uses existing FFmpeg/RIFE and local Wan2.2 14B distilled GGUF experts.
The two experts are loaded sequentially, not held together in system RAM.
Does not change the game movie or the illustrated alternative.
"""
import argparse
import contextlib
import gc
import hashlib
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'art/intro/alternative-20261021/corale/v2'
WORK=ROOT/'.verify/intro-corale-v2-20261022'
OUT.mkdir(parents=True,exist_ok=True)
WORK.mkdir(parents=True,exist_ok=True)
MODEL='jayn7/WAN2.2-I2V_A14B-DISTILL-LIGHTX2V-4STEP-GGUF'
BASE='Wan-AI/Wan2.2-I2V-A14B-Diffusers'
TEXT='FastVideo/FastWan2.2-TI2V-5B-FullAttn-Diffusers'
FILES=[noise+'_260412/wan2.2_i2v_A14b_'+noise+'_lightx2v_4step_720p_260412-Q4_K_S.gguf' for noise in ('high_noise','low_noise')]


def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):
            h.update(chunk)
    return h.hexdigest()


def run(args):
    subprocess.run([str(x) for x in args],check=True)


def retime():
    import numpy as np
    from scipy.interpolate import PchipInterpolator
    source=OUT.parent/'a-native.mp4'
    raw,interp=WORK/'a-raw',WORK/'a-120'
    raw.mkdir(exist_ok=True)
    interp.mkdir(exist_ok=True)
    run(['ffmpeg','-v','error','-y','-i',source,raw/'%08d.png'])
    rife=ROOT/'.verify/rife-runtime/rife-ncnn-vulkan-20221029-windows'
    run([rife/'rife-ncnn-vulkan.exe','-i',raw,'-o',interp,'-n','608','-m',rife/'rife-v4.6',
         '-g','0','-j','2:2:2','-f','%08d.png'])
    x=[0.,.65,1.25,1.8,3.4,4.95,81/16]
    y=[0.,.46,.96,1.27,2.04,2.83,2.90]
    spline=PchipInterpolator(x,y)
    speeds=1/spline.derivative()(np.linspace(0,x[-1],1000))
    if not np.all(np.isfinite(speeds)) or speeds.min()<=0:
        raise RuntimeError('Nonmonotone retime map')
    terms=[]
    for i in range(len(x)-1):
        t='(PTS*TB-%.10f)'%x[i]
        c=spline.c[:,i]
        terms.append('((%.12f)*%s*%s*%s+(%.12f)*%s*%s+(%.12f)*%s+(%.12f))'%
                     (c[0],t,t,t,c[1],t,t,c[2],t,c[3]))
    expr=terms[-1]
    for i in reversed(range(len(terms)-1)):
        expr='if(lt(PTS*TB,%.10f),%s,%s)'%(x[i+1],terms[i],expr)
    target=OUT/'a-retimed.mp4'
    run(['ffmpeg','-v','error','-y','-framerate','120','-i',interp/'%08d.png',
         '-vf',"setpts='("+expr+")/TB',fps=60,scale=1920:1080:flags=lanczos,setsar=1",
         '-c:v','libx264','-crf','16','-preset','slow','-pix_fmt','yuv420p',target])
    report={'request':'D0936','method':'Continuous PCHIP source-time to output-time mapping; no internal cuts',
            'source':str(source),'source_sha256':sha(source),'source_seconds':81/16,
            'source_knots':x,'output_knots':y,'interpolation':'RIFE v4.6 120 Hz before remapping, final 60 Hz',
            'speed_min':float(speeds.min()),'speed_max':float(speeds.max()),
            'output':str(target),'sha256':sha(target),'artistic_approval':'pending'}
    (OUT/'retime.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report),flush=True)


def animate(seed,image=None,prompt_path=None,label='archer',request='D0936'):
    import torch
    from huggingface_hub import hf_hub_download
    from diffusers import (WanImageToVideoPipeline,WanTransformer3DModel,AutoencoderKLWan,
                           FlowMatchEulerDiscreteScheduler,GGUFQuantizationConfig)
    from diffusers.utils import load_image,export_to_video
    from transformers import UMT5EncoderModel,AutoTokenizer
    image=Path(image) if image else OUT/'keyframe-archer.png'
    prompt=Path(prompt_path or OUT/'motion-archer.txt').read_text(encoding='utf-8-sig')
    report={'request':request,'model':MODEL,'base':BASE,'license':'Apache-2.0, inherited from LightX2V/Wan',
            'files':FILES,'seed':seed,'prompt':prompt,'image_sha256':sha(image),
            'steps':4,'expert_steps':[2,2],'guidance_scale':1.,
            'scheduler':'LightX2V WanStepDistill schedule [1000,750,500,250], shift=5; Euler step',
            'size':[1024,576],'frames':81,'fps':24,'spend':0,'status':'running','errors':[]}
    receipt=OUT/(label+'-generation.json')
    def write():
        receipt.write_text(json.dumps(report,indent=2),encoding='utf-8')
    write()
    try:
        tokenizer=AutoTokenizer.from_pretrained(TEXT,subfolder='tokenizer',local_files_only=True)
        key=hashlib.sha256(prompt.encode()).hexdigest()[:12]
        cache=WORK/(key+'-prompt.pt')
        if cache.exists():
            embed=torch.load(cache,weights_only=True)
        else:
            print('Encoding motion prompt on GPU',flush=True)
            encoder=UMT5EncoderModel.from_pretrained(TEXT,subfolder='text_encoder',torch_dtype=torch.bfloat16,
                                                     device_map='cuda',low_cpu_mem_usage=True,local_files_only=True)
            enc=WanImageToVideoPipeline(tokenizer=tokenizer,text_encoder=encoder,vae=None,transformer=None,
                                        scheduler=FlowMatchEulerDiscreteScheduler())
            with torch.no_grad():
                embed,_=enc.encode_prompt(prompt=prompt,device=torch.device('cuda'),max_sequence_length=256,
                                          num_videos_per_prompt=1,do_classifier_free_guidance=False)
            embed=embed.cpu()
            torch.save(embed,cache)
            del enc,encoder
            gc.collect()
            torch.cuda.empty_cache()
        paths=[hf_hub_download(MODEL,f,local_files_only=True) for f in FILES]
        report['checkpoint_files']=[{'file':f,'bytes':Path(p).stat().st_size,'revision':Path(p).parents[1].name} for f,p in zip(FILES,paths)]
        def load_expert(index):
            print('Loading '+('high' if index==0 else 'low')+' noise expert',flush=True)
            model=WanTransformer3DModel.from_single_file(paths[index],config=BASE,subfolder='transformer' if index==0 else 'transformer_2',
                quantization_config=GGUFQuantizationConfig(compute_dtype=torch.bfloat16),torch_dtype=torch.bfloat16,
                local_files_only=True)
            return model.to('cuda')
        class SequentialExperts(torch.nn.Module):
            def __init__(self):
                super().__init__()
                self.core=load_expert(0)
                self.config=self.core.config
                self.calls=0
            @property
            def dtype(self):
                return torch.bfloat16
            @property
            def device(self):
                return torch.device('cuda')
            def cache_context(self,*args,**kwargs):
                return contextlib.nullcontext()
            def forward(self,*args,**kwargs):
                if self.calls==2:
                    del self.core
                    gc.collect()
                    torch.cuda.empty_cache()
                    self.core=load_expert(1)
                self.calls+=1
                return self.core(*args,**kwargs)
        experts=SequentialExperts()
        vae=AutoencoderKLWan.from_pretrained(BASE,subfolder='vae',torch_dtype=torch.float32,
                                            local_files_only=True).to('cuda')
        vae.enable_tiling()
        class DistilledSchedule(FlowMatchEulerDiscreteScheduler):
            # Official LightX2V WanStepDistillScheduler.set_denoising_timesteps
            # samples the shifted 1000-step grid at [1000,750,500,250]. Using
            # Diffusers' default four-point linspace incorrectly includes t=1.
            def set_timesteps(self,num_inference_steps=None,device=None,**kwargs):
                sigmas=torch.tensor([1.,.75,.5,.25],dtype=torch.float32)
                sigmas=5*sigmas/(1+4*sigmas)
                self.timesteps=(sigmas*1000).to(device)
                self.sigmas=torch.cat([sigmas,torch.zeros(1)])
                self.num_inference_steps=4
                self._step_index=None
                self._begin_index=None
        pipe=WanImageToVideoPipeline(tokenizer=tokenizer,text_encoder=None,vae=vae,transformer=experts,
                                     scheduler=DistilledSchedule(shift=5.),boundary_ratio=None)
        def step(pipe,i,t,kwargs):
            report['last_step']=i+1
            report.setdefault('timesteps',[]).append(float(t))
            write()
            print('Denoised step '+str(i+1),flush=True)
            return kwargs
        frames=pipe(image=load_image(str(image)),prompt_embeds=embed.to('cuda'),height=576,width=1024,
                    num_frames=81,num_inference_steps=4,guidance_scale=1.,
                    generator=torch.Generator(device='cuda').manual_seed(seed),
                    callback_on_step_end=step,output_type='pil').frames[0]
        target=OUT/(label+'-native.mp4')
        export_to_video(frames,str(target),fps=24)
        run(['ffmpeg','-v','error','-i',target,'-f','null','-'])
        report.update(status='completed',output=str(target),sha256=sha(target))
    except Exception as e:
        report.update(status='failed',errors=[str(e)])
        raise
    finally:
        write()
    print(json.dumps({'file':str(target),'status':report['status']}),flush=True)


def cleanup_projectile():
    """Repair only the erroneous generated missile, retaining the full body shot.

    Track an arrow-free clean plate from the same moving shot. Annotated bounds
    cover the wrong-facing drifting projectile; blend the registered plate only
    in those bounds, never over the archer's body or bow.
    """
    import cv2
    import numpy as np
    source=OUT/'archer-native.mp4'
    cap=cv2.VideoCapture(str(source))
    frames=[]
    while True:
        ok,f=cap.read()
        if not ok:
            break
        frames.append(f)
    cap.release()
    clean=frames[0].copy()
    h,w=clean.shape[:2]
    # Early masks need a pre-release plate to avoid the lowered bow.
    # Later masks use frame 40 to retain background coverage at the right edge.
    plate_mask=np.zeros((h,w),np.uint8)
    plate_mask[160:209,560:617]=255
    clean=cv2.inpaint(clean,plate_mask,4,cv2.INPAINT_TELEA)
    region=np.zeros((h,w),np.uint8)
    region[:,600:]=255
    sift=cv2.SIFT_create(nfeatures=2400)
    plates=[clean,frames[40].copy()]
    features=[sift.detectAndCompute(cv2.cvtColor(p,cv2.COLOR_BGR2GRAY),region) for p in plates]
    matcher=cv2.BFMatcher()
    # Coordinates are native 1024x576, inspected at full resolution. Bounds
    # include shaft and fletching; the bow and character remain outside them.
    controls=[(4,570,168,765,217),(6,590,168,770,221),(8,595,172,790,225),
              (10,635,178,815,231),(12,710,188,835,239),(14,760,191,870,247),
              (16,805,196,918,255),(18,851,201,958,264),(20,888,207,1006,270),
              (22,930,213,1024,327),(24,960,227,1024,335),(26,970,235,1024,341),
              (30,980,235,1024,350),(34,1010,250,1024,350)]
    controls=[(n,x0,y0,x1,y1+45 if 14<=n<=20 else y1) for n,x0,y0,x1,y1 in controls]
    xs=np.array([v[0] for v in controls])
    masks=[]
    metrics=[]
    target=WORK/'archer-clean.mp4'
    process=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24',
        '-s',str(w)+'x'+str(h),'-r','24','-i','-','-an','-c:v','libx264','-crf','12',
        '-pix_fmt','yuv420p',str(target)],stdin=subprocess.PIPE)
    try:
        for n,f in enumerate(frames):
            if 4<=n<=34:
                pi=0 if n<14 else 1
                ck,cd=features[pi]
                k,d=sift.detectAndCompute(cv2.cvtColor(f,cv2.COLOR_BGR2GRAY),region)
                pairs=matcher.knnMatch(cd,d,k=2)
                good=[a for a,b in pairs if a.distance<.72*b.distance]
                if len(good)<15:
                    raise RuntimeError('Insufficient background tracking points at frame '+str(n))
                a=np.float32([ck[m.queryIdx].pt for m in good]).reshape(-1,1,2)
                b=np.float32([k[m.trainIdx].pt for m in good]).reshape(-1,1,2)
                matrix,inliers=cv2.findHomography(a,b,cv2.RANSAC,2.5)
                if matrix is None or int(inliers.sum())<12:
                    raise RuntimeError('Unstable clean-plate tracking at frame '+str(n))
                plate=cv2.warpPerspective(plates[pi],matrix,(w,h),flags=cv2.INTER_LANCZOS4,borderMode=cv2.BORDER_REPLICATE)
                box=[round(np.interp(n,xs,[v[i] for v in controls])) for i in range(1,5)]
                x0,y0,x1,y1=box
                mask=np.zeros((h,w),np.float32)
                mask[y0:y1,x0:x1]=1.
                # Remove the detached lower fletching fragments separately.
                if 11<=n<=22:
                    xx=round(np.interp(n,[11,18,22],[705,810,960]))
                    mask[256:294,max(600,xx-28):min(w,xx+36)]=1.
                mask=cv2.GaussianBlur(mask,(9,9),2.)[:,:,None]
                f=np.clip(f.astype(np.float32)*(1-mask)+plate.astype(np.float32)*mask,0,255).astype(np.uint8)
                metrics.append({'frame':n,'matches':len(good),'inliers':int(inliers.sum()),'bounds':box})
            process.stdin.write(f.tobytes())
    finally:
        process.stdin.close()
        status=process.wait()
    if status:
        raise RuntimeError('Clean plate encode failed')
    report={'source_sha256':sha(source),'output_sha256':sha(target),'method':'SIFT/RANSAC clean-plate registration and feathered regional compositing',
            'plate_frames':[0,40],'plate_switch_at':14,'plate_arrowhead_inpaint_bounds':[560,160,617,209],
            'edited_frames':[4,34],'body_or_bow_edited':False,'tracking':metrics,
            'reason':'Generated arrow faced backwards, drifted too slowly and split fletching.'}
    (OUT/'projectile-cleanup.json').write_text(json.dumps(report,indent=2),encoding='utf-8')


def smooth_archer():
    raw,interp=WORK/'archer-raw',WORK/'archer-60'
    raw.mkdir(exist_ok=True)
    interp.mkdir(exist_ok=True)
    source=WORK/'archer-clean.mp4'
    run(['ffmpeg','-v','error','-y','-i',source,raw/'%08d.png'])
    rife=ROOT/'.verify/rife-runtime/rife-ncnn-vulkan-20221029-windows'
    run([rife/'rife-ncnn-vulkan.exe','-i',raw,'-o',interp,'-n','203','-m',rife/'rife-v4.6',
         '-g','0','-j','2:2:2','-f','%08d.png'])
    target=OUT/'archer-smooth.mp4'
    run(['ffmpeg','-v','error','-y','-framerate','60','-i',interp/'%08d.png',
         '-vf','scale=1920:1080:flags=lanczos,setsar=1','-c:v','libx264','-crf','16',
         '-pix_fmt','yuv420p',target])
    (OUT/'archer-smooth.json').write_text(json.dumps({'source_sha256':sha(source),'sha256':sha(target),
          'native_frames':81,'native_fps':24,'output_frames':203,'output_fps':60,
          'method':'RIFE v4.6 per shot; no interpolation across the editorial cut'},indent=2),encoding='utf-8')


def composite_arrow():
    import cv2
    import numpy as np
    from PIL import Image
    asset=OUT/'arrow.png'
    im=Image.open(asset).convert('RGBA')
    im=im.crop(im.getchannel('A').getbbox())
    width=412
    im=im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS)
    arrow=np.array(im)[:,:,[2,1,0,3]].astype(np.float32)
    source=OUT/'archer-smooth.mp4'
    target=OUT/'archer-final.mp4'
    cap=cv2.VideoCapture(str(source))
    process=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s','1920x1080',
        '-r','60','-i','-','-c:v','libx264','-crf','16','-pix_fmt','yuv420p',str(target)],stdin=subprocess.PIPE)
    n=0
    try:
        while True:
            ok,frame=cap.read()
            if not ok: break
            t=n/60
            if .20<=t<=.56:
                accum=np.zeros_like(frame,dtype=np.float32)
                for dt in (-.003,-.001,.001,.003):
                    canvas=frame.astype(np.float32).copy()
                    tip=(580+2500*(t+dt-.20))*1920/1024
                    x=round(tip-width)
                    y=round(195*1080/576-arrow.shape[0]/2)
                    x0,x1=max(0,x),min(1920,x+width)
                    if x1>x0:
                        piece=arrow[:,x0-x:x1-x]
                        alpha=piece[:,:,3:]/255
                        canvas[y:y+len(piece),x0:x1]=canvas[y:y+len(piece),x0:x1]*(1-alpha)+piece[:,:,:3]*alpha
                    accum+=canvas*.25
                frame=np.clip(accum,0,255).astype(np.uint8)
            process.stdin.write(frame.tobytes())
            n+=1
    finally:
        cap.release()
        process.stdin.close()
        if process.wait(): raise RuntimeError('Arrow compositing failed')
    (OUT/'arrow-composite.json').write_text(json.dumps({'source_sha256':sha(source),'asset_sha256':sha(asset),
        'output_sha256':sha(target),'release_seconds':.20,'native_pixels_per_second':2500,
        'method':'Physical arrow alpha composite after interpolation; four temporal samples for projectile only',
        'frames':n,'figure_source':'Built-in imagegen, saved original transparent arrow asset'},indent=2),encoding='utf-8')


def finish():
    import math
    import numpy as np
    import soundfile as sf
    from scipy.signal import butter,resample_poly,sosfilt
    action=WORK/'action.mp4'
    a_seconds,b_seconds=2.9,3.3
    action_seconds=a_seconds+b_seconds
    title=action_seconds+.06
    seconds=title+4.25
    run(['ffmpeg','-v','error','-y','-i',OUT/'a-retimed.mp4','-i',OUT/'archer-final.mp4',
         '-filter_complex',f'[0:v]trim=duration={a_seconds},setpts=PTS-STARTPTS[a];'
         f'[1:v]trim=duration={b_seconds},setpts=PTS-STARTPTS[b];[a][b]concat=n=2:v=1:a=0[v]',
         '-map','[v]','-c:v','libx264','-crf','16','-pix_fmt','yuv420p',action])
    sr=48000
    mix=np.zeros((round(seconds*sr),2))
    events=[]
    foley=ROOT/'.verify/ragequit-unreal/hit-feel-wav-20261010-010346/wav'
    owned=ROOT/'.verify/ragequit-unreal/verify-fab-mat-20261020-234029/waves'
    def add(path,at,gain,pan=0.,speed=1.,length=.8,normalize=True):
        y,rate=sf.read(path,always_2d=True)
        y=y.mean(axis=1)
        d=math.gcd(rate,sr)
        y=resample_poly(y,sr//d,rate//d)
        if speed!=1.:
            y=resample_poly(y,1000,round(speed*1000))
        if normalize:
            active=np.flatnonzero(abs(y)>max(abs(y))*.025)
            if len(active):
                y=y[max(0,active[0]-100):]
        y=y[:round(sr*length)]
        y=sosfilt(butter(2,65,'highpass',fs=sr,output='sos'),y)
        if normalize:
            y/=max(float(abs(y).max()),1e-9)
        fade=min(round(.06*sr),len(y)//3)
        y[:96]*=np.linspace(0,1,96)
        y[-fade:]*=np.linspace(1,0,fade)
        y=y[:,None]*gain*np.sqrt([(1-pan)/2,(1+pan)/2])
        start=round(at*sr)
        count=min(len(y),len(mix)-start)
        mix[start:start+count]+=y[:count]
        events.append({'source':str(path),'source_sha256':sha(path),'at':at,'gain':gain,
                       'pan':pan,'speed':speed,'length':length})
    def fx(name,at,gain,pan=0.,speed=1.,length=.8):
        add(foley/(name+'.wav'),at,gain,pan,speed,length)
    fx('Whoosh_4-1',.13,.18,.25,1.1)
    fx('Shield_Metal_Impact_1-3',.50,.46,-.25,.96)
    fx('Rock_Impact_11',.50,.10,-.25,1.1)
    fx('Draw_Weapon_Metal_1-1',1.12,.12,-.25,1.2)
    fx('Whoosh_1-1',1.70,.18,-.2,1.05)
    fx('Whoosh_1-1',2.47,.22,.1,1.2)
    for i,t in enumerate((1.52,1.91,2.32,2.70)):
        name=('FEETHmn_InsJ_Footsteps_Stones_Running_Trainers_01-01_Single-02_81003.wav' if i%2 else
              'FEETHmn_InsJ_Footsteps_Stones_Running_Trainers_01-01_Single-01_56867.wav')
        add(owned/'SFX_Essentials_FREE_SAMPLE'/name,t,.09,-.25,.9,.4)
    add(owned/'SmallSoundKit/Leather_001_84677.wav',a_seconds+.12,.10,-.2,1.,.6)
    # Release timing is reviewed against the generated arrow before delivery.
    release=a_seconds+.20
    add(ROOT/'.verify/ragequit-unreal/action-feel-wav-20261010-014639/wav/SW_MagicCast_HeavyArrowShoot_1.wav',
        release,.24,0.,1.1,.5)
    fx('Whoosh_4-1',release+.03,.12,.25,1.3,.4)
    add(owned/'SmallSoundKit/Leather_002_544.wav',release+.45,.06,0.,.9,.5)
    wind=owned/'SmallSoundKit/Amb_Wind_96882.wav'
    add(wind,0.,.018,0.,1.,action_seconds+.2)
    fx('Blacksmithing_1-1',title,.27,0.,.72,1.2)
    fx('Rock_Impact_37',title,.20,0.,.62,1.25)
    voice=ROOT/'art/intro/announcer-v2.wav'
    y,rate=sf.read(voice,always_2d=True)
    d=math.gcd(rate,sr)
    y=resample_poly(y,sr//d,rate//d,axis=0)
    if y.shape[1]==1:
        y=np.repeat(y,2,axis=1)
    start=round((title+.12)*sr)
    mix[start:start+len(y)]+=y[:,:2]*.88
    mix=np.tanh(mix*1.05)/1.05
    peak=float(abs(mix).max())
    if peak>.92:
        mix*=.92/peak
    mix[-round(.25*sr):]*=np.linspace(1,0,round(.25*sr))[:,None]
    wav=WORK/'mix.wav'
    sf.write(wav,mix,sr,subtype='PCM_24')
    filters=(f'[0:v]tpad=stop_mode=clone:stop_duration=4.5,trim=duration={seconds},'
        f"eq=brightness='-0.75*min(max((t-{action_seconds-.08})/0.22,0),1)':eval=frame:"
        'saturation=0.92:contrast=1.025,fade=t=in:st=0:d=0.08[base];'
        f'[1:v]scale=1270:-1,format=rgba,fade=t=in:st={title+.08}:d=0.16:alpha=1[letters];'
        f'[2:v]scale=1270:-1,format=rgba,fade=t=in:st={title}:d=0.12:alpha=1[slash];'
        f"[base][slash]overlay=x='(W-w)/2+max(0,{title+.1}-t)*5000':y='(H-h)/2':enable='gte(t,{title})'[s];"
        f"[s][letters]overlay=x='(W-w)/2':y='(H-h)/2':enable='gte(t,{title+.08})',"
        f'fade=t=out:st={seconds-.25}:d=0.25[v]')
    final=OUT/'ragequit-corale-v2.mp4'
    run(['ffmpeg','-v','warning','-y','-i',action,'-loop','1','-i',ROOT/'art/ui/menu/T_UI_Logo.png',
         '-loop','1','-i',ROOT/'art/ui/menu/T_UI_LogoSlash.png','-i',wav,'-filter_complex',filters,
         '-map','[v]','-map','3:a','-t',seconds,'-r','60','-c:v','libx264','-crf','16','-preset','slow',
         '-pix_fmt','yuv420p','-c:a','aac','-b:a','256k','-ar','48000','-ac','2','-movflags','+faststart',final])
    run(['ffmpeg','-v','error','-i',final,'-f','null','-'])
    probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(final)]))
    report={'request':'D0936','output':str(final),'sha256':sha(final),'duration':seconds,
            'a_seconds':a_seconds,'b_seconds':b_seconds,'body_retime':json.loads((OUT/'retime.json').read_text()),
            'new_archer':json.loads((OUT/'archer-generation.json').read_text()),
            'archer_interpolation':json.loads((OUT/'archer-smooth.json').read_text()),'audio_events':events,
            'projectile_cleanup':json.loads((OUT/'projectile-cleanup.json').read_text()),
            'projectile_composite':json.loads((OUT/'arrow-composite.json').read_text()),
            'voice_sha256':sha(voice),'audio_peak':float(abs(mix).max()),'audio_samples_at_or_above_1':int(np.sum(abs(mix)>=1)),
            'decode':'Full FFmpeg decode passed','probe':probe,'artistic_approval':'pending author review',
            'installed':False,'installed_movie_sha256':sha(ROOT/'unreal/Content/Movies/RagequitIntro.mp4'),
            'boundary':'Native sources 832x480 and 1024x576; interpolation and upscale do not constitute native 1080p.',
            'script_sha256':sha(__file__)}
    (OUT/'provenance.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps({'file':str(final),'duration':seconds,'sha256':sha(final)}),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('mode',choices=['retime','animate','cleanup','smooth','composite','finish'])
    p.add_argument('--seed',type=int,default=834)
    a=p.parse_args()
    {'retime':retime,'animate':lambda:animate(a.seed),'cleanup':cleanup_projectile,'smooth':smooth_archer,'composite':composite_arrow,'finish':finish}[a.mode]()
