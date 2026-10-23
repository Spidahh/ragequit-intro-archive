"""Assemble the three authored Video 2 shots, owned Foley and accepted announcer."""
from pathlib import Path
import subprocess, json, math
import numpy as np
import soundfile as sf
from scipy.signal import resample_poly, butter, sosfilt
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT/'.verify/video2-work'
def run(args): subprocess.run([str(x) for x in args],check=True)
def foley(duration):
    sr=48000
    track=np.zeros((round(duration*sr),2))
    lib=ROOT/'.verify/ragequit-unreal/hit-feel-wav-20261010-010346/wav'
    events=[('Draw_Weapon_Metal_1-1',.02,.20,1),('Whoosh_1-1',.20,.48,1.15),
      ('Shield_Metal_Impact_1-3',.95,.66,.94),('Punch_2-1',.95,.27,.90),
      ('Whoosh_4-1',1.15,.34,.80),('Rock_Impact_37',1.35,.35,.85),
      ('Whoosh_1-1',2.35,.50,1.20),('Whoosh_4-1',2.79,.52,1.15),
      ('Shield_Metal_Impact_1-3',3.05,.64,.86),('Rock_Impact_37',3.05,.48,.72),
      ('Rock_Impact_11',3.85,.72,.72),('Blacksmithing_1-1',3.85,.35,.76)]
    for i,(name,at,level,speed) in enumerate(events):
        y,rate=sf.read(lib/(name+'.wav'),always_2d=True)
        y=y.mean(axis=1);d=math.gcd(sr,rate)
        y=resample_poly(y,sr//d,rate//d)
        y=resample_poly(y,1000,round(speed*1000))
        active=np.flatnonzero(abs(y)>max(abs(y))*.035)
        if len(active): y=y[max(0,active[0]-96):]
        y=y[:round(sr*.7)]
        y=sosfilt(butter(2,55,'highpass',fs=sr,output='sos'),y)
        y=y/max(max(abs(y)),1e-8)*level
        y[:96]*=np.linspace(0,1,96); n=min(len(y)//3,2880);y[-n:]*=np.linspace(1,0,n)
        pan=(-.18 if i%2 else .18)
        stereo=y[:,None]*np.sqrt([(1-pan)/2,(1+pan)/2])
        pos=round(at*sr);track[pos:pos+len(y)]+=stereo
        for delay,gain in ((.037,.12),(.073,.06)):
            offset=pos+round(delay*sr);track[offset:offset+len(y)]+=stereo[:,::-1]*gain
    t=np.arange(len(track))/sr
    track*=(1-.75*np.clip((t-3.95)/.3,0,1))[:,None]
    sf.write(WORK/'combat-bed.wav',np.tanh(track*1.1)/1.1,sr,subtype='PCM_24')
    (WORK/'sound-events.json').write_text(json.dumps(events,indent=2),encoding='utf-8')
def assemble():
    voice=ROOT/'art/intro/announcer-v2.wav';y,sr=sf.read(voice)
    duration=3.4+len(y)/sr+.55
    foley(duration)
    vf=(f'[0:v]scale=1280:720,setsar=1,tpad=stop_mode=clone:stop_duration={duration},trim=duration={duration},fps=60,vignette=PI/6,'
      "eq=brightness='-0.62*min(max((t-3.82)/0.25,0),1)':eval=frame,fade=t=in:st=0:d=0.04[base];"
      '[1:v]scale=1040:-1,format=rgba,colorchannelmixer=rr=0.965:gg=0.937:bb=0.886,fade=t=in:st=3.92:d=0.10:alpha=1[letters];'
      '[2:v]scale=1040:-1,format=rgba,colorchannelmixer=rr=0.702:gg=0.071:bb=0.165,fade=t=in:st=3.82:d=0.06:alpha=1[slash];'
      "[base][slash]overlay=x='(W-w)/2+max(0,3.92-t)*4800':y='(H-h)/2':enable='gte(t,3.82)'[mark];"
      "[mark][letters]overlay=x='(W-w)/2':y='(H-h)/2+max(0,4.02-t)*220':enable='gte(t,3.92)',"
      f'fade=t=out:st={duration-.22}:d=0.22[v];'
      '[3:a]aformat=sample_rates=48000:channel_layouts=stereo,adelay=3400|3400[voice];'
      f'[voice][4:a]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=0.94,atrim=duration={duration}[a]')
    run(['ffmpeg','-hide_banner','-loglevel','warning','-y','-i',WORK/'fight.mp4',
      '-loop','1','-i',ROOT/'art/ui/menu/T_UI_Logo.png','-loop','1','-i',ROOT/'art/ui/menu/T_UI_LogoSlash.png',
      '-i',voice,'-i',WORK/'combat-bed.wav','-filter_complex',vf,'-map','[v]','-map','[a]',
      '-t',str(duration),'-c:v','libx264','-crf','17','-pix_fmt','yuv420p','-c:a','aac','-b:a','256k',
      '-ar','48000','-ac','2','-movflags','+faststart',ROOT/'art/intro/video-2.mp4'])
if __name__=='__main__': assemble()
