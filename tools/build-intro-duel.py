"""D0938: two connected physical action beats, followed by original title/voice.

Run with .verify/intro-runtime/Scripts/python.exe. Does not install the movie.
Animation uses the same recorded local Wan experts; finishing uses RIFE/FFmpeg.
"""
import argparse,hashlib,importlib.util,json,math,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'art/intro/duello-azione-20261022'
WORK=ROOT/'.verify/intro-action-20261022/finish'
RIFE=ROOT/'.verify/rife-runtime/rife-ncnn-vulkan-20221029-windows'

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def run(args):
    subprocess.run([str(x) for x in args],check=True)

def module(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/'tools'/file)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m

def animate(shot):
    m=module('refiner','refine-intro-corale.py')
    m.OUT=OUT;m.WORK=WORK
    m.animate({'contact':1295,'counter':6614}[shot],image=OUT/(shot+'.png'),
              prompt_path=OUT/(shot+'-motion.txt'),label=shot,request='D0938')

def finish():
    import numpy as np
    import soundfile as sf
    from scipy.signal import butter,resample_poly,sosfilt
    sound=module('intro_sound','assemble-intro-istante.py')
    shots=[]
    for name in ('contact','counter'):
        source=OUT/(name+'-native.mp4')
        raw=WORK/name/'raw';smooth=WORK/name/'smooth'
        raw.mkdir(parents=True,exist_ok=True);smooth.mkdir(parents=True,exist_ok=True)
        run(['ffmpeg','-v','error','-y','-i',source,raw/'%08d.png'])
        run([RIFE/'rife-ncnn-vulkan.exe','-i',raw,'-o',smooth,'-n','120',
             '-m',RIFE/'rife-v4.6','-g','0','-j','2:2:2','-f','%08d.png'])
        movie=WORK/(name+'.mp4')
        frames=120 if name=='contact' else 66
        run(['ffmpeg','-v','error','-y','-framerate','60','-i',smooth/'%08d.png',
             '-frames:v',frames,'-vf','scale=1920:1080:flags=lanczos,setsar=1','-c:v','libx264','-crf','16','-pix_fmt','yuv420p',movie])
        shots.append({'name':name,'source_sha256':sha(source),'source_frames':81,'source_fps':24,
            'retime_frames_before_trim':120,'output_frames':frames,'output_fps':60,'duration':frames/60,'speed':1.6875,
            'trim_reason':'Remove idle tail after landing' if name=='counter' else None,
            'generation':json.loads((OUT/(name+'-generation.json')).read_text())})
    action=WORK/'action.mp4'
    run(['ffmpeg','-v','error','-y','-i',WORK/'contact.mp4','-i',WORK/'counter.mp4',
         '-filter_complex','[0:v][1:v]concat=n=2:v=1:a=0[v]','-map','[v]',
         '-c:v','libx264','-crf','16','-pix_fmt','yuv420p',action])
    duration=5.2;sr=48000
    mix=np.zeros((round(duration*sr),2),dtype=np.float64)
    events=[]
    def add(name,at,gain,pan=0.,speed=1.,length=.7):
        y=sound.read(name,speed)[:round(length*sr)]
        y=sosfilt(butter(2,60,'highpass',fs=sr,output='sos'),y)
        f=min(len(y)//4,round(.05*sr))
        y[:96]*=np.linspace(0,1,96);y[-f:]*=np.linspace(1,0,f)
        y=y[:,None]*np.sqrt([(1-pan)/2,(1+pan)/2])*gain
        start=round(at*sr);count=min(len(y),len(mix)-start)
        mix[start:start+count]+=y[:count]
        events.append({'source':name,'at':at,'gain':gain,'speed':speed,'sha256':sha(sound.LIB/(name+'.wav'))})
    add('Shield_Metal_Impact_1-3',.02,.38,-.15,.95,.48)
    add('Punch_2-1',.02,.28,.1,.9,.35)
    add('Whoosh_4-1',.15,.14,.35,1.25,.4)
    add('Rock_Impact_37',1.03,.25,.4,.85,.55)
    add('Hit_Generic_5-1',1.05,.2,.3,.9,.4)
    # Counterattack timings are checked against the selected frames.
    add('Rock_Impact_11',2.03,.19,.3,.85,.6)
    add('Whoosh_1-1',2.17,.23,-.25,.8,.65)
    add('Rock_Impact_37',2.56,.26,-.4,.8,.6)
    add('Blacksmithing_1-1',3.1,.19,0.,.75,.8)
    add('Rock_Impact_37',3.1,.13,0.,.7,.7)
    voice=ROOT/'art/intro/announcer-v2.wav'
    y,rate=sf.read(voice,always_2d=True);d=math.gcd(sr,rate)
    y=resample_poly(y,sr//d,rate//d,axis=0)
    if y.shape[1]==1:y=np.repeat(y,2,axis=1)
    voice_at=1.12;start=round(voice_at*sr)
    mix[start:start+len(y)]+=y[:,:2]*.88
    mix=np.tanh(mix*1.05)/1.05
    peak=float(abs(mix).max())
    if peak>.92:mix*=.92/peak
    mix[-round(.2*sr):]*=np.linspace(1,0,round(.2*sr))[:,None]
    wav=WORK/'mix.wav';sf.write(wav,mix,sr,subtype='PCM_24')
    graph=(f'[0:v]tpad=stop_mode=clone:stop_duration=2.1,trim=duration={duration},'
           'fade=t=out:st=3.05:d=0.16[bg];'
           '[1:v]scale=1270:-1,format=rgba,fade=t=in:st=3.17:d=0.1:alpha=1[letters];'
           '[2:v]scale=1270:-1,format=rgba,fade=t=in:st=3.1:d=0.09:alpha=1[slash];'
           "[bg][slash]overlay=x='(W-w)/2+max(0,3.2-t)*5000':y='(H-h)/2':enable='gte(t,3.1)'[s];"
           "[s][letters]overlay=x='(W-w)/2':y='(H-h)/2':enable='gte(t,3.17)',fade=t=out:st=5:d=0.2[v]")
    final=OUT/'ragequit-duello.mp4'
    run(['ffmpeg','-v','warning','-y','-i',action,'-loop','1','-i',ROOT/'art/ui/menu/T_UI_Logo.png',
         '-loop','1','-i',ROOT/'art/ui/menu/T_UI_LogoSlash.png','-i',wav,'-filter_complex',graph,
         '-map','[v]','-map','3:a','-t',duration,'-r','60','-c:v','libx264','-crf','16','-preset','slow',
         '-pix_fmt','yuv420p','-c:a','aac','-b:a','256k','-ar','48000','-ac','2','-movflags','+faststart',final])
    run(['ffmpeg','-v','error','-i',final,'-f','null','-'])
    probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(final)]))
    v=next(s for s in probe['streams'] if s['codec_type']=='video')
    a=next(s for s in probe['streams'] if s['codec_type']=='audio')
    assert (v['width'],v['height'],v['r_frame_rate'],a['channels'])==(1920,1080,'60/1',2)
    report={'request':'D0938','output':str(final),'sha256':sha(final),'duration':duration,'shots':shots,
            'action':'Shield contact displaces mage; mage counterattacks from a low position; warrior reacts.',
            'audio':{'events':events,'voice_at':voice_at,'voice_sha256':sha(voice),
                     'peak':float(abs(mix).max()),'samples_at_or_above_1':int(np.sum(abs(mix)>=1))},
            'decode':'Full FFmpeg decode passed','probe':probe,'artistic_approval':'pending author review',
            'native_boundary':'1024x576 at 24 fps; retimed 1.6875x and interpolated per shot, then upscaled.',
            'installed':False,'installed_movie_sha256':sha(ROOT/'unreal/Content/Movies/RagequitIntro.mp4'),
            'script_sha256':sha(__file__)}
    (OUT/'provenance.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps({'output':str(final),'sha256':sha(final)}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['animate','finish'])
    p.add_argument('--shot',choices=['contact','counter'],default='contact');args=p.parse_args()
    OUT.mkdir(parents=True,exist_ok=True);WORK.mkdir(parents=True,exist_ok=True)
    animate(args.shot) if args.mode=='animate' else finish()
