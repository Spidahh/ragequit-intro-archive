"""Assemble option 02 from native Unreal frames, owned Foley, original logo/VO.

No game movie is replaced. Use the existing .verify/intro-runtime Python env.
"""
import argparse
import hashlib
import json
import math
import subprocess
from pathlib import Path
import numpy as np
import soundfile as sf
from scipy.signal import butter, resample_poly, sosfilt

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT/'art/intro/istante-prima-20261021'
WORK = ROOT/'.verify/intro-istante-mix-v2'
LIB = ROOT/'.verify/ragequit-unreal/hit-feel-wav-20261010-010346/wav'
SR = 48000
DURATION = 14.25


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(args):
    subprocess.run([str(x) for x in args], check=True)


def read(name, speed=1.):
    y, rate = sf.read(LIB/(name+'.wav'), always_2d=True)
    y=y.mean(axis=1)
    d=math.gcd(SR,rate)
    y=resample_poly(y,SR//d,rate//d)
    if speed!=1.:
        y=resample_poly(y,1000,round(1000*speed))
    active=np.flatnonzero(abs(y)>max(abs(y))*.025)
    if len(active):
        y=y[max(0,active[0]-100):]
    return y/max(max(abs(y)),1e-9)


def audio():
    WORK.mkdir(parents=True,exist_ok=True)
    sr=SR
    track=np.zeros((round(DURATION*sr),2),dtype=np.float64)
    events=[]

    def add(name, at, gain, pan=0., speed=1., length=1.4, reverse=False, low=None):
        y=read(name,speed)[:round(length*sr)]
        if reverse:
            y=y[::-1].copy()
        y=sosfilt(butter(2,55,'highpass',fs=sr,output='sos'),y)
        if low:
            y=sosfilt(butter(2,low,'lowpass',fs=sr,output='sos'),y)
        n=min(len(y)//5,round(.025*sr))
        y[:n]*=np.linspace(0,1,n)
        n=min(len(y)//3,round(.18*sr))
        y[-n:]*=np.linspace(1,0,n)
        stereo=y[:,None]*np.sqrt([(1-pan)/2,(1+pan)/2])*gain
        pos=round(at*sr)
        for delay,level in ((0,1.),(.039,.12),(.097,.055),(.183,.025)):
            start=pos+round(delay*sr)
            size=min(len(y),len(track)-start)
            if size>0:
                track[start:start+size]+=stereo[:size]*level
        events.append(dict(source=name,at=at,gain=gain,pan=pan,speed=speed,reverse=reverse,
                           sha256=digest(LIB/(name+'.wav'))))

    # Continuous action from the opening; the six-frame pause is punctuation.
    add('Draw_Weapon_Metal_1-1',.03,.17,-.35,.9,.75,low=4200)
    add('Whoosh_4-1',.53,.24,.3,1.1,.65)
    add('Shield_Metal_Impact_1-3',1.10,.16,-.3,.9,.2)
    add('Shield_Metal_Impact_1-3',1.35,.48,-.3,.9,.85)
    add('Rock_Impact_11',1.35,.19,-.25,.85,.7)
    add('Whoosh_1-1',1.78,.29,-.35,1.05,.6)
    add('Whoosh_4-1',2.76,.25,.2,.9,.8)
    add('Whoosh_1-1',3.17,.34,-.2,1.12,.7)
    add('Whoosh_4-1',3.88,.25,.4,.85,.8)
    add('Shield_Metal_Impact_1-3',4.4,.44,-.2,1.0,.8)
    add('Whoosh_1-1',4.7,.28,-.3,1.1,.65)
    add('Whoosh_4-1',5.82,.31,-.2,1.1,.65)
    add('Punch_2-1',6.1,.35,.25,.95,.6)
    add('Rock_Impact_37',7.2,.3,.3,.8,.9)
    add('Whoosh_1-1',7.74,.30,-.25,1.05,.7)
    add('Whoosh_4-1',8.55,.25,.4,.9,.9)
    add('Whoosh_1-1',9.28,.3,-.2,1.1,.65)
    add('Shield_Metal_Impact_1-3',9.8,.4,-.2,.9,.6)
    add('Blacksmithing_1-1',10.0,.36,0.,.68,1.5)
    add('Rock_Impact_37',10.0,.28,0.,.62,1.3)
    vo=ROOT/'art/intro/announcer-v2.wav'
    y,rate=sf.read(vo,always_2d=True)
    d=math.gcd(rate,sr)
    y=resample_poly(y,sr//d,rate//d,axis=0)
    if y.shape[1]==1:
        y=np.repeat(y,2,axis=1)
    y=y[:,:2]*.88
    start=round(10.1*sr)
    track[start:start+len(y)]+=y
    track=np.tanh(track*1.06)/1.06
    peak=float(abs(track).max())
    if peak>.92:
        track*=.92/peak
    track[-int(.28*sr):]*=np.linspace(1,0,int(.28*sr))[:,None]
    path=WORK/'mix.wav'
    sf.write(path,track,sr,subtype='PCM_24')
    report={'events':events,'voice':{'path':str(vo),'sha256':digest(vo),'at':10.1},
            'sample_rate':sr,'duration':DURATION,'peak':float(abs(track).max()),
            'samples_at_or_above_1':int(np.sum(abs(track)>=1.))}
    (WORK/'audio.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    return path


def assemble(render):
    DEST.mkdir(parents=True,exist_ok=True)
    mix=audio()
    native=WORK/'native.mp4'
    run(['ffmpeg','-hide_banner','-loglevel','warning','-y','-framerate','24','-i',
         render/'frames/frame_%04d.png','-frames:v','240','-c:v','libx264','-crf','15',
         '-pix_fmt','yuv420p',native])
    # Film is already rendered at 1920x1080. Logo assets are original RGBA files.
    filters=(
        f'[0:v]tpad=stop_mode=clone:stop_duration=4.25,trim=duration={DURATION},'
        "eq=brightness='-0.58*min(max((t-9.88)/0.3,0),1)':eval=frame,"
        'fade=t=in:st=0:d=0.25[base];'
        '[1:v]scale=1320:-1,format=rgba,fade=t=in:st=10.08:d=0.18:alpha=1[letters];'
        '[2:v]scale=1320:-1,format=rgba,fade=t=in:st=9.98:d=0.1:alpha=1[slash];'
        "[base][slash]overlay=x='(W-w)/2+max(0,10.1-t)*6000':y='(H-h)/2':enable='gte(t,9.98)'[s];"
        "[s][letters]overlay=x='(W-w)/2':y='(H-h)/2+max(0,10.25-t)*95':enable='gte(t,10.08)',"
        'fade=t=out:st=13.95:d=0.3[v]')
    final=DEST/'ragequit-istante-prima-v2.mp4'
    run(['ffmpeg','-hide_banner','-loglevel','warning','-y','-i',native,
         '-loop','1','-i',ROOT/'art/ui/menu/T_UI_Logo.png',
         '-loop','1','-i',ROOT/'art/ui/menu/T_UI_LogoSlash.png','-i',mix,
         '-filter_complex',filters,'-map','[v]','-map','3:a','-t',str(DURATION),
         '-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p',
         '-c:a','aac','-b:a','256k','-ar','48000','-ac','2','-movflags','+faststart',final])
    run(['ffmpeg','-hide_banner','-loglevel','error','-i',final,'-f','null','-'])
    probe=json.loads(subprocess.run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(final)],
                                   check=True,capture_output=True,text=True).stdout)
    video=next(x for x in probe['streams'] if x['codec_type']=='video')
    audio_stream=next(x for x in probe['streams'] if x['codec_type']=='audio')
    if (video['width'],video['height'],video['r_frame_rate'],audio_stream['channels'])!=(1920,1080,'24/1',2):
        raise RuntimeError('Unexpected delivery format')
    meta=json.loads((render/'report.json').read_text(encoding='utf-8'))
    if not meta.get('success') or len(meta.get('frames',[]))!=240:
        raise RuntimeError('Incomplete native render')
    report={'status':'Replacement of rejected v1; for author review, not integrated', 'author_request':'D0930; correction D0931',
            'direction':'02 — L’istante prima','other_directions':'01 and 03 retained, on hold',
            'film':final.name,'sha256':digest(final),'native_render':str(render),
            'native_method':meta,'audio':json.loads((WORK/'audio.json').read_text()),
            'decode':'Full FFmpeg decode passed','artistic_approval':'pending',
            'size':[1920,1080],'fps':24,'duration':DURATION,'image_to_video_used':False,
            'probe':probe,'script_sha256':{p.name:digest(p) for p in (ROOT/'tools/unreal/render-intro-istante.py',Path(__file__))},
            'installed_movie_sha256':digest(ROOT/'unreal/Content/Movies/RagequitIntro.mp4')}
    (DEST/'provenance-v2.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps({'file':str(final),'sha256':digest(final)}))


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--render',type=Path)
    a=p.parse_args()
    if a.render:
        assemble(a.render)
    else:
        print(audio())
