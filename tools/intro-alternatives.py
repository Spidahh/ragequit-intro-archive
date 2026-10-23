"""D0934: production helpers for the two remaining intro directions.

Source animation: free hosted Wan2.2 14B and existing local LTX 0.9.5,
with a receipt for each request.
Finishing: installed RIFE v4.6 per shot (never across editorial cuts), FFmpeg.
Game movie is never replaced. No paid APIs or credentials.
"""
import argparse
import base64
import hashlib
import json
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'art/intro/alternative-20261021'
WORK = ROOT / '.verify/intro-alternatives-20261021'
RIFE = ROOT / '.verify/rife-runtime/rife-ncnn-vulkan-20221029-windows'


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def run(args):
    subprocess.run([str(x) for x in args], check=True)


def animate(a):
    from gradio_client import Client
    out = DEST / a.direction
    out.mkdir(parents=True, exist_ok=True)
    receipt = out / (a.shot + '-generation.json')
    report = {'request': 'D0934', 'provider': 'prithivMLmods/Wan2.2-Fast',
              'model': 'Wan2.2 I2V 14B, Lightning LoRA', 'spend': 0,
              'image': str(a.image), 'image_sha256': sha(a.image),
              'prompt': a.prompt.read_text(encoding='utf-8-sig'),
              'steps': 4, 'seconds_requested': a.seconds, 'seed': a.seed,
              'status': 'submitted', 'time': time.strftime('%Y-%m-%dT%H:%M:%S')}
    receipt.write_text(json.dumps(report, indent=2), encoding='utf-8')
    try:
        client = Client('prithivMLmods/Wan2.2-Fast', verbose=False)
        result = client.predict(
            image_b64='data:image/png;base64,' + base64.b64encode(a.image.read_bytes()).decode('ascii'),
            prompt=report['prompt'], steps=4,
            negative_prompt='still image, freeze frame, slideshow, stop motion, jerky animation, '
            'teleporting limbs, weapon morphing, dissolving faces, new characters, extra limbs, '
            'unmotivated cuts, oversaturated, neon hands, text, logo, watermark',
            duration_seconds=a.seconds, guidance_scale=1.0, guidance_scale_2=1.0,
            seed=a.seed, randomize_seed=False, api_name='/generate_video')
        p = out / (a.shot + '-native.mp4')
        p.write_bytes(base64.b64decode(result['video'].split(',', 1)[1]))
        run(['ffmpeg', '-v', 'error', '-i', p, '-f', 'null', '-'])
        report.update(status='completed', output=str(p), sha256=sha(p),
                      provider_metadata={k:v for k,v in result.items() if k != 'video'})
    except Exception as e:
        report.update(status='failed', error=str(e))
        raise
    finally:
        receipt.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps({'file': str(p), 'status': report['status']}), flush=True)


def smooth(a):
    source = DEST / a.direction / (a.shot + '-native.mp4')
    work = WORK / a.direction / (a.shot+'-'+sha(source)[:12])
    raw, interp = work / 'raw', work / 'rife'
    raw.mkdir(parents=True, exist_ok=True)
    interp.mkdir(parents=True, exist_ok=True)
    probe = json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-of','json',str(source)]))
    video = next(v for v in probe['streams'] if v['codec_type']=='video')
    fps = float(__import__('fractions').Fraction(video['r_frame_rate']))
    run(['ffmpeg','-v','error','-y','-i',source,raw/'frame_%08d.png'])
    frames = len(list(raw.glob('*.png')))
    # Preserve duration. RIFE v4 supports arbitrary frame counts; 60 Hz is not
    # achieved by accelerating a 24 Hz clip or duplicating its source frames.
    count = round(frames * 60 / fps)
    run([RIFE/'rife-ncnn-vulkan.exe','-i',raw,'-o',interp,'-n',count,
         '-m',RIFE/'rife-v4.6','-g','0','-j','2:2:2','-f','%08d.png'])
    target = DEST / a.direction / (a.shot + '-smooth.mp4')
    run(['ffmpeg','-v','error','-y','-framerate','60','-i',interp/'%08d.png',
         '-vf','scale=1920:1080:flags=lanczos,setsar=1','-c:v','libx264',
         '-crf','16','-preset','slow','-pix_fmt','yuv420p',target])
    report={'method':'RIFE v4.6, per shot, no interpolation across cuts',
            'source':str(source),'source_sha256':sha(source),'native_fps':fps,
            'native_frames':frames,'interpolated_frames':count,'output_fps':60,
            'output':str(target),'output_sha256':sha(target),
            'quality_boundary':'Temporal interpolation does not correct choreography or guarantee artistic quality.'}
    (target.with_suffix('.json')).write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report),flush=True)


def finish(a):
    import importlib.util
    import numpy as np
    import soundfile as sf
    from scipy.signal import butter, sosfilt
    spec=importlib.util.spec_from_file_location('intro_audio',ROOT/'tools/assemble-intro-istante.py')
    audio=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audio)
    work=WORK/a.direction
    work.mkdir(parents=True,exist_ok=True)
    out=DEST/a.direction
    shots=[('a',.12,4.9),('b',.12,3.5)] if a.direction=='corale' else [('a',.35,5.0)]
    inputs=[]
    filters=[]
    for i,(name,start,end) in enumerate(shots):
        inputs+=['-i',out/(name+'-smooth.mp4')]
        filters.append('[%d:v]trim=start=%s:end=%s,setpts=PTS-STARTPTS[v%d]'%(i,start,end,i))
    filters.append(''.join('[v%d]'%i for i in range(len(shots)))+'concat=n=%d:v=1:a=0[v]'%len(shots))
    action=work/'action.mp4'
    run(['ffmpeg','-v','error','-y',*inputs,'-filter_complex',';'.join(filters),'-map','[v]',
         '-c:v','libx264','-crf','16','-pix_fmt','yuv420p',action])
    action_seconds=sum(end-start for _,start,end in shots)
    title=action_seconds+.08
    duration=title+4.25
    sr=48000
    track=np.zeros((round(duration*sr),2))
    events=[]
    def add(name,at,gain,pan=0.,speed=1.,length=.8):
        y=audio.read(name,speed)[:round(sr*length)]
        y=sosfilt(butter(2,65,'highpass',fs=sr,output='sos'),y)
        n=min(len(y)//3,round(sr*.08))
        y[:96]*=np.linspace(0,1,96)
        y[-n:]*=np.linspace(1,0,n)
        y=y[:,None]*gain*np.sqrt([(1-pan)/2,(1+pan)/2])
        at=max(0.,at)
        start=round(at*sr)
        count=min(len(y),len(track)-start)
        track[start:start+count]+=y[:count]
        offset=start+round(.061*sr)
        count=min(len(y),len(track)-offset)
        if count>0:
            track[offset:offset+count]+=y[:count,::-1]*.07
        events.append({'source':name,'at':at,'gain':gain,'pan':pan,'speed':speed,
                       'source_sha256':sha(audio.LIB/(name+'.wav'))})
    if a.direction=='corale':
        for name,at,gain,pan,speed in [
            ('Whoosh_4-1',.18,.19,.3,1.1),('Shield_Metal_Impact_1-3',.68,.45,-.25,.94),
            ('Rock_Impact_11',.70,.12,-.25,1.1),('Draw_Weapon_Metal_1-1',1.55,.13,-.3,.9),
            ('Whoosh_1-1',2.55,.15,-.2,.85),('Whoosh_1-1',4.22,.22,.15,1.1),
            ('Whoosh_4-1',4.9,.16,-.35,1.2),('Whoosh_1-1',6.0,.24,.35,1.1),
            ('Whoosh_1-1',7.45,.4,.1,.92),('Rock_Impact_11',7.65,.12,-.2,1.15)]:
            add(name,at,gain,pan,speed)
    else:
        for name,at,gain,pan,speed in [
            ('Whoosh_4-1',.0,.20,.3,.85),('Shield_Metal_Impact_1-3',.22,.32,-.25,.9),
            ('Whoosh_4-1',1.55,.20,.15,.95),('Whoosh_1-1',2.45,.38,-.2,.95),
            ('Shield_Metal_Impact_1-3',2.88,.42,0.,.88),('Whoosh_1-1',3.6,.18,.2,.9)]:
            add(name,at,gain,pan,speed)
    add('Blacksmithing_1-1',title,.27,0.,.72,1.2)
    add('Rock_Impact_37',title,.20,0.,.62,1.25)
    voice=ROOT/'art/intro/announcer-v2.wav'
    y,rate=sf.read(voice,always_2d=True)
    if rate!=sr:
        import math
        from scipy.signal import resample_poly
        d=math.gcd(rate,sr)
        y=resample_poly(y,sr//d,rate//d,axis=0)
    if y.shape[1]==1:
        y=np.repeat(y,2,axis=1)
    at=round((title+.12)*sr)
    track[at:at+len(y)]+=y[:,:2]*.88
    track=np.tanh(track*1.05)/1.05
    peak=float(abs(track).max())
    if peak>.92:
        track*=.92/peak
    track[-round(.25*sr):]*=np.linspace(1,0,round(.25*sr))[:,None]
    mix=work/'mix.wav'
    sf.write(mix,track,sr,subtype='PCM_24')
    letters=ROOT/'art/ui/menu/T_UI_Logo.png'
    slash=ROOT/'art/ui/menu/T_UI_LogoSlash.png'
    vf=(f'[0:v]tpad=stop_mode=clone:stop_duration=4.5,trim=duration={duration},'
        f"eq=brightness='-0.75*min(max((t-{action_seconds-.08})/0.22,0),1)':eval=frame:"
        'saturation=0.92:contrast=1.025,fade=t=in:st=0:d=0.1[base];'
        f'[1:v]scale=1270:-1,format=rgba,fade=t=in:st={title+.08}:d=0.16:alpha=1[letters];'
        f'[2:v]scale=1270:-1,format=rgba,fade=t=in:st={title}:d=0.12:alpha=1[slash];'
        f"[base][slash]overlay=x='(W-w)/2+max(0,{title+.1}-t)*5000':y='(H-h)/2':enable='gte(t,{title})'[s];"
        f"[s][letters]overlay=x='(W-w)/2':y='(H-h)/2':enable='gte(t,{title+.08})',"
        f'fade=t=out:st={duration-.25}:d=0.25[v]')
    final=out/('ragequit-'+a.direction+'-v1.mp4')
    run(['ffmpeg','-v','warning','-y','-i',action,'-loop','1','-i',letters,'-loop','1','-i',slash,
         '-i',mix,'-filter_complex',vf,'-map','[v]','-map','3:a','-t',duration,
         '-r','60','-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p',
         '-c:a','aac','-b:a','256k','-ar','48000','-ac','2','-movflags','+faststart',final])
    run(['ffmpeg','-v','error','-i',final,'-f','null','-'])
    probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(final)]))
    v=next(x for x in probe['streams'] if x['codec_type']=='video')
    au=next(x for x in probe['streams'] if x['codec_type']=='audio')
    if (v['width'],v['height'],v['r_frame_rate'],au['channels'])!=(1920,1080,'60/1',2):
        raise RuntimeError('Unexpected final delivery format')
    report={'request':'D0934','direction':a.direction,'artistic_approval':'pending author review',
            'installed':False,'output':str(final),'sha256':sha(final),'action_seconds':action_seconds,
            'duration':duration,'shots':shots,'audio_events':events,'voice':str(voice),'voice_sha256':sha(voice),
            'audio_peak':float(abs(track).max()),'audio_samples_at_or_above_1':int(np.sum(abs(track)>=1)),
            'decode':'full FFmpeg decode passed','probe':probe,
            'installed_intro_sha256':sha(ROOT/'unreal/Content/Movies/RagequitIntro.mp4'),
            'native_resolution_boundary':'Native animation dimensions and cadence are in each shot receipt; RIFE intermediate frames and Lanczos upscale to 1920x1080. Not native 1080p.',
            'source_receipts':{name:json.loads((out/(name+'-generation.json')).read_text()) for name,_,_ in shots},
            'interpolation_receipts':{name:json.loads((out/(name+'-smooth.json')).read_text()) for name,_,_ in shots},
            'tools':{'imagegen':'built-in keyframe generation','animation':'hosted Wan2.2 14B and existing local LTX 0.9.5 as recorded per shot',
                     'interpolation':'RIFE v4.6, per shot, 60 Hz','finishing':'FFmpeg, original logo and accepted announcer, owned Foley'},
            'script_sha256':sha(__file__)}
    (out/'provenance.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps({'file':str(final),'seconds':duration,'sha256':sha(final)}),flush=True)


def ltx(a):
    import torch
    from diffusers import LTXImageToVideoPipeline
    from diffusers.utils import load_image,export_to_video
    out=DEST/a.direction
    if (out/(a.shot+'-native.mp4')).exists():
        raise RuntimeError('Native shot already exists: choose a new shot id for another production attempt.')
    report={'request':'D0934','model':'Lightricks/LTX-Video-0.9.5','provider':'local existing cached model',
            'spend':0,'image':str(a.image),'image_sha256':sha(a.image),'prompt':a.prompt.read_text(encoding='utf-8-sig'),
            'steps':40,'guidance':4.,'seed':a.seed,'size':[768,448],'native_fps':24,'frames':121,'status':'running'}
    receipt=out/(a.shot+'-generation.json')
    receipt.write_text(json.dumps(report,indent=2),encoding='utf-8')
    try:
        pipe=LTXImageToVideoPipeline.from_pretrained('Lightricks/LTX-Video-0.9.5',torch_dtype=torch.bfloat16,local_files_only=True)
        pipe.enable_model_cpu_offload()
        pipe.vae.enable_tiling()
        result=pipe(image=load_image(str(a.image)),prompt=report['prompt'],
                    negative_prompt='extra weapons, duplicate scythe, two scythes, weapon morphing, extra limbs, '
                    'unmotivated cuts, static image, blurry, deformation, camera shake, text, watermark',
                    width=768,height=448,num_frames=121,num_inference_steps=40,guidance_scale=4.,
                    generator=torch.Generator(device='cuda').manual_seed(a.seed)).frames[0]
        target=out/(a.shot+'-native.mp4')
        export_to_video(result,str(target),fps=24)
        run(['ffmpeg','-v','error','-i',target,'-f','null','-'])
        report.update(status='completed',output=str(target),sha256=sha(target))
    except Exception as e:
        report.update(status='failed',error=str(e))
        raise
    finally:
        receipt.write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps({'file':str(target),'status':report['status']}),flush=True)


if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('mode',choices=['animate','smooth','finish','ltx'])
    p.add_argument('--direction',required=True,choices=['corale','illustrata'])
    p.add_argument('--shot',default='a')
    p.add_argument('--image',type=Path)
    p.add_argument('--prompt',type=Path)
    p.add_argument('--seed',type=int,default=721)
    p.add_argument('--seconds',type=float,default=5.)
    a=p.parse_args()
    {'animate':animate,'smooth':smooth,'finish':finish,'ltx':ltx}[a.mode](a)
