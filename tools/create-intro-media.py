"""Create the standalone, reviewable intro. Run in .verify/intro-runtime, never in Unreal.

voice: local Qwen3 VoiceDesign; wan-video: free hosted animation; mix: original logo + audio.
Generated footage is a visual proposal, not approved or integrated game content.
"""
from pathlib import Path
import argparse
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'art/intro'
VOICE_STYLE = (
    'A male basso profondo: extremely deep, low-pitched, rumbling bass voice with thick gravelly '
    'throat resonance. A huge brutal orc warlord with a rough, hoarse growl and massive vocal weight. '
    'Menacing, forceful, aggressive American English. Speak slowly and deliberately, with a short '
    'pause between the sentences. Proclaim RAGE QUIT, then give the fierce command FRAG THEM ALL.'
)
VIDEO_PROMPT = (
    'A strange hand drawn dark fantasy animated film, angular ink drawing and bold gouache colors. '
    'A tall thin wizard in ivory robes on the left fights a massive black armored warrior with a crimson '
    'cloak on the right. The warrior steps forward and swings his broad sword down with both hands. '
    'The wizard raises his crooked staff and blocks the blade. The weapons collide and recoil, '
    'sending a short burst of sparks. Then the wizard thrusts his staff forward, releasing a pale blue '
    'magical shockwave from its head into the warrior, who staggers backwards. The robes and cape '
    'follow the physical motion. Each action has anticipation, contact and a visible reaction. '
    'The camera stays in a wide side view showing both figures and weapons, with a slow subtle push in. '
    'Sparse leaning gothic arches and red banners behind them, flickering braziers. '
    'Two consistent figures throughout, coherent anatomy, consistent ink and gouache illustration '
    'with exaggerated figurative design, restricted ivory, black, red and cold cyan palette. '
    'No realistic CGI, no video game graphics, no text, no logos, no cuts.'
)

def run(args):
    subprocess.run([str(x) for x in args], check=True)

def voice(seed):
    import torch
    import soundfile as sf
    from qwen_tts import Qwen3TTSModel
    torch.manual_seed(seed)
    model = Qwen3TTSModel.from_pretrained(
        'Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign', device_map='cuda:0',
        dtype=torch.bfloat16, attn_implementation='sdpa')
    wavs, sr = model.generate_voice_design(
        text='Welcome to Rage quit! ... FRAG THEM ALL!', language='English',
        instruct=VOICE_STYLE, max_new_tokens=300, temperature=0.85,
        top_p=0.95, repetition_penalty=1.08)
    path = OUT / f'announcer-{seed}.wav'
    sf.write(path, wavs[0], sr)
    print(json.dumps({'path': str(path), 'seconds': len(wavs[0])/sr, 'sample_rate': sr}), flush=True)
    (OUT / 'voice-prompt.txt').write_text(VOICE_STYLE, encoding='utf-8')

def voice_process(announcer):
    run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',announcer,
         '-af','rubberband=pitch=0.840896:tempo=0.95:formant=preserved,highpass=f=65,lowpass=f=11000',
         OUT/'announcer-orc-v1.wav'])

def voice_process_v2(announcer):
    run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',announcer,
         '-af','silenceremove=start_periods=1:start_threshold=-40dB:stop_periods=-1:stop_duration=0.25:stop_threshold=-40dB,'
         'rubberband=pitch=0.707107:tempo=1.08:formant=shifted,highpass=f=45,bass=g=3:f=90,equalizer=f=2400:t=q:w=0.8:g=3,'
         'acompressor=threshold=0.10:ratio=4:attack=5:release=70,'
         'asoftclip=type=tanh:threshold=0.45:output=0.9,loudnorm=I=-15:TP=-1.5:LRA=7',OUT/'announcer-v2.wav'])

def video(image, seed, seconds=5.0):
    import torch
    from diffusers import LTXImageToVideoPipeline
    from diffusers.utils import load_image, export_to_video
    pipe = LTXImageToVideoPipeline.from_pretrained(
        'Lightricks/LTX-Video-0.9.5', torch_dtype=torch.bfloat16)
    pipe.enable_model_cpu_offload()
    pipe.vae.enable_tiling()
    frames = pipe(
        image=load_image(str(image)), prompt=VIDEO_PROMPT,
        negative_prompt='photorealistic, CGI, 3d render, video game, morphing, extra limbs, extra weapons, '
                        'static image, blurry, inconsistent character, deformed hands, camera cuts, text, watermark',
        width=768, height=448, num_frames=round(seconds*24)//8*8+1, num_inference_steps=40,
        guidance_scale=4.0, generator=torch.Generator(device='cuda').manual_seed(seed)
    ).frames[0]
    path = OUT / f'fight-{seed}.mp4'
    export_to_video(frames, str(path), fps=24)
    frames[-1].save(OUT / f'fight-{seed}-last.png')
    (OUT / 'video-prompt.txt').write_text(VIDEO_PROMPT, encoding='utf-8')
    print(json.dumps({'path': str(path), 'frames': len(frames)}), flush=True)

def hosted_video(image, seed, seconds=5.0):
    """Official free ZeroGPU demo; upload only this generated keyframe, no project files."""
    from gradio_client import Client, handle_file
    import shutil
    client = Client('Lightricks/ltx-video-distilled', verbose=False)
    result = client.predict(
        prompt=VIDEO_PROMPT,
        negative_prompt='photorealistic, CGI, 3d render, video game, morphing, extra limbs, '
                        'extra weapons, static image, inconsistent character, deformed hands, text',
        input_image_filepath=handle_file(str(image)), input_video_filepath=None,
        height_ui=448, width_ui=768, mode='image-to-video', duration_ui=seconds,
        ui_frames_to_use=9, seed_ui=seed, randomize_seed=False,
        ui_guidance_scale=1.0, improve_texture_flag=True, api_name='/image_to_video')
    print(json.dumps(result), flush=True)
    path = OUT / f'fight-{seed}.mp4'
    shutil.copyfile(result[0]['video'], path)
    (OUT/'video-prompt.txt').write_text(VIDEO_PROMPT, encoding='utf-8')
    print(json.dumps({'path': str(path)}), flush=True)

def wan_video(image, seed, seconds=5.0):
    import base64
    from gradio_client import Client
    client = Client('prithivMLmods/Wan2.2-Fast', verbose=False)
    result = client.predict(
        image_b64='data:image/png;base64,'+base64.b64encode(image.read_bytes()).decode('ascii'),
        prompt=VIDEO_PROMPT, steps=4,
        negative_prompt='static image, motionless figures, slideshow, morphing weapons, extra limbs, '
                        'photorealistic, CGI, video game, text, watermark',
        duration_seconds=min(seconds, 5.0), guidance_scale=1.0, guidance_scale_2=1.0,
        seed=seed, randomize_seed=False, api_name='/generate_video')
    path = OUT/f'fight-{seed}.mp4'
    path.write_bytes(base64.b64decode(result['video'].split(',', 1)[1]))
    (OUT/'video-prompt.txt').write_text(VIDEO_PROMPT, encoding='utf-8')
    print(json.dumps({'path':str(path), 'seed':result.get('seed'), 'bytes':path.stat().st_size}), flush=True)

def score(duration, fast=False):
    """Original restrained sound bed, steel collision and spell impact; no copied game audio."""
    import numpy as np
    import soundfile as sf
    from scipy.signal import butter, sosfilt
    sr = 48000
    t = np.arange(round(duration*sr))/sr
    rng = np.random.default_rng(314)
    # A quiet breathy low drone, leaving the announcer foreground clear.
    drone = .018*(np.sin(2*np.pi*43*t) + .4*np.sin(2*np.pi*64.5*t))
    wind = sosfilt(butter(2, [140, 850], 'bandpass', fs=sr, output='sos'), rng.normal(size=len(t)))
    y = drone + .016*wind
    def add(at, x):
        a = round(at*sr); b = min(len(y), a+len(x)); y[a:b] += x[:b-a]
    def impact(at, strength):
        q = np.arange(int(sr*.65))/sr
        x = .23*np.sin(2*np.pi*(105*q-30*q*q))*np.exp(-q*9)
        for freq in (740, 1291, 2207):
            x += .075*np.sin(2*np.pi*freq*q)*np.exp(-q*19)
        x += .12*rng.normal(size=len(q))*np.exp(-q*75)
        add(at, strength*x)
    # Timings are refined against the actual generated contact before delivery.
    impact(.4 if fast else .9, .8)
    impact(.9 if fast else 2.8, .95)
    impact(1.8 if fast else 5.45, .55)
    q = np.arange(int(sr*.6))/sr
    whoosh = sosfilt(butter(2, [400, 5500], 'bandpass', fs=sr, output='sos'), rng.normal(size=len(q)))
    add(.12 if fast else .28, .10*whoosh*np.sin(np.pi*q/.6)**2)
    add(.65 if fast else 2.3, .14*whoosh*np.sin(np.pi*q/.6)**2)
    # Width only on background: the spoken line stays centered.
    left = y
    right = .92*y+.08*np.roll(y, round(sr*.011))
    sf.write(OUT/'sound-bed.wav', np.column_stack([left,right]), sr)

def combat_score(duration):
    """Foley from owned packs, rendered only into the film; never distribute source WAVs."""
    import numpy as np
    import soundfile as sf
    from scipy.signal import resample_poly, butter, sosfilt
    from math import gcd
    library = ROOT/'.verify/ragequit-unreal/hit-feel-wav-20261010-010346/wav'
    sr = 48000
    track = np.zeros((round(duration*sr), 2), dtype=np.float64)
    events = []
    def add(name, at, level, pan=0., rate=1., maximum=1.0, reverse=False):
        path = library/(name+'.wav')
        y, rate_in = sf.read(path, always_2d=True)
        y = y.mean(axis=1)
        divisor = gcd(sr, rate_in)
        y = resample_poly(y, sr//divisor, rate_in//divisor)
        if rate != 1.: y = resample_poly(y, 1000, round(rate*1000))
        # Remove leading silence and align the acoustic attack to the actual contact.
        peak = np.max(np.abs(y))
        active = np.flatnonzero(np.abs(y) > peak*.035)
        if len(active): y = y[max(0,active[0]-96):]
        y = y[:round(maximum*sr)]
        if reverse: y = y[::-1].copy()
        y = sosfilt(butter(2, 55, 'highpass', fs=sr, output='sos'), y)
        y = y/max(np.max(np.abs(y)), 1e-8)*level
        fade = min(len(y)//3, round(sr*.06))
        y[:96] *= np.linspace(0,1,min(96,len(y)))
        y[-fade:] *= np.linspace(1,0,fade)
        pos = round(at*sr); n = min(len(y),len(track)-pos)
        gains = np.sqrt([(1-pan)/2,(1+pan)/2])
        stereo = y[:n,None]*gains
        track[pos:pos+n] += stereo
        # Short room reflections retain the dry, immediate impact.
        for delay, gain in ((.037,.12),(.073,.06)):
            offset=pos+round(delay*sr); count=min(n,len(track)-offset)
            if count>0: track[offset:offset+count] += stereo[:count,::-1]*gain
        events.append(dict(source=str(path.relative_to(ROOT)),seconds=at,level=level,rate=rate))
    add('Draw_Weapon_Metal_1-1', .02, .18, .2, maximum=.3)
    add('Whoosh_1-1', .22, .48, .2, rate=1.15, maximum=.3)
    add('Shield_Wood_Impact_2-1', .50, .57, -.1, rate=.91, maximum=.42)
    add('Shield_Metal_Impact_1-3', .50, .70, .12, rate=.94, maximum=.55)
    add('Punch_2-1', .51, .26, maximum=.2)
    add('Whoosh_4-1', .81, .44, -.2, rate=1.18, maximum=.3)
    add('Shield_Metal_Impact_1-3', 1.10, .59, .1, rate=1.16, maximum=.45)
    add('Wood_Chop_1-4', 1.10, .44, -.1, rate=.88, maximum=.35)
    add('Rock_Impact_37', 1.13, .28, maximum=.45)
    add('Whoosh_1-1', 1.48, .32, -.1, rate=.82, maximum=.34)
    add('Whoosh_4-1', 1.56, .33, rate=.8, maximum=.22, reverse=True)
    add('Rock_Impact_11', 1.80, .66, rate=.72, maximum=.75)
    add('Blacksmithing_1-1', 1.80, .40, rate=.76, maximum=.6)
    # Rapid decay under the announcer; no tonal computer-like drone or beeps.
    timeline=np.arange(len(track))/sr
    track *= (1-.75*np.clip((timeline-1.95)/.35,0,1))[:,None]
    track = np.tanh(track*1.1)/1.1
    sf.write(OUT/'combat-bed-v3.wav',track,sr,subtype='PCM_24')
    (OUT/'sound-events-v3.json').write_text(json.dumps(events,indent=2),encoding='utf-8')

def mix_v3(footage, announcer):
    import soundfile as sf
    y,sr=sf.read(announcer)
    duration=1.9+len(y)/sr+.55
    combat_score(duration)
    logo=ROOT/'art/ui/menu/T_UI_Logo.png'
    slash=ROOT/'art/ui/menu/T_UI_LogoSlash.png'
    vf=(
        f'[0:v]scale=1344:756,crop=1280:720,setsar=1,tpad=stop_mode=clone:stop_duration={duration},'
        f'trim=duration={duration},fps=60,vignette=PI/5,'
        "eq=brightness='-0.72*min(max((t-1.67)/0.28,0),1)':eval=frame,fade=t=in:st=0:d=0.06[base];"
        '[1:v]scale=1040:-1,format=rgba,colorchannelmixer=rr=0.965:gg=0.937:bb=0.886,'
        'fade=t=in:st=1.89:d=0.12:alpha=1[letters];'
        '[2:v]scale=1040:-1,format=rgba,colorchannelmixer=rr=0.702:gg=0.071:bb=0.165,'
        'fade=t=in:st=1.76:d=0.06:alpha=1[slash];'
        "[base][slash]overlay=x='(W-w)/2+max(0,1.86-t)*4200':y='(H-h)/2':enable='gte(t,1.76)'[mark];"
        "[mark][letters]overlay=x='(W-w)/2':y='(H-h)/2+max(0,2.01-t)*180':enable='gte(t,1.89)',"
        f'fade=t=out:st={duration-.22}:d=0.22[v];'
        '[3:a]aformat=sample_rates=48000:channel_layouts=stereo,adelay=1900|1900[voice];'
        '[4:a]volume=1.2[combat];'
        f'[voice][combat]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=0.94,atrim=duration={duration}[a]')
    run(['ffmpeg','-hide_banner','-loglevel','warning','-y','-i',footage,'-loop','1','-i',logo,
         '-loop','1','-i',slash,'-i',announcer,'-i',OUT/'combat-bed-v3.wav','-filter_complex',vf,
         '-map','[v]','-map','[a]','-t',str(duration),'-c:v','libx264','-crf','17','-pix_fmt','yuv420p',
         '-c:a','aac','-ar','48000','-ac','2','-b:a','256k','-movflags','+faststart',OUT/'ragequit-intro-v3.mp4'])

def mix_v2(footage, announcer):
    """Fast interpolated fight followed by the existing logo and a new guttural voice."""
    import soundfile as sf
    y, sr = sf.read(announcer)
    duration = 1.9 + len(y)/sr + .55
    score(duration, fast=True)
    logo = ROOT/'art/ui/menu/T_UI_Logo.png'
    slash = ROOT/'art/ui/menu/T_UI_LogoSlash.png'
    vf = (
        f'[0:v]scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,setsar=1,'
        f'tpad=stop_mode=clone:stop_duration={duration},trim=duration={duration},fps=60,'
        'fade=t=in:st=0:d=0.08,fade=t=out:st=1.65:d=0.3[base];'
        '[1:v]scale=1000:-1,format=rgba,colorchannelmixer=rr=0.965:gg=0.937:bb=0.886,'
        'fade=t=in:st=1.95:d=0.16:alpha=1[letters];'
        '[2:v]scale=1000:-1,format=rgba,colorchannelmixer=rr=0.702:gg=0.071:bb=0.165,'
        'fade=t=in:st=1.8:d=0.10:alpha=1[slash];'
        '[base][slash]overlay=(W-w)/2:(H-h)/2:enable=gte(t\\,1.8)[mark];'
        f'[mark][letters]overlay=(W-w)/2:(H-h)/2:enable=gte(t\\,1.95),fade=t=out:st={duration-.2}:d=0.2[v];'
        '[3:a]aformat=sample_rates=48000:channel_layouts=stereo,adelay=1900|1900,volume=1.0[voice];'
        '[4:a]volume=0.55[bed];'
        f'[voice][bed]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=0.93,atrim=duration={duration}[a]'
    )
    run(['ffmpeg','-hide_banner','-loglevel','warning','-y','-i',footage,
         '-loop','1','-i',logo,'-loop','1','-i',slash,'-i',announcer,'-i',OUT/'sound-bed.wav',
         '-filter_complex',vf,'-map','[v]','-map','[a]','-t',str(duration),
         '-c:v','libx264','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-ar','48000','-ac','2','-b:a','192k',
         '-movflags','+faststart',OUT/'ragequit-intro-v2.mp4'])
    print(json.dumps({'path':str(OUT/'ragequit-intro-v2.mp4'),'seconds':duration}),flush=True)

def mix(footage, announcer):
    import soundfile as sf
    voice_data, sr = sf.read(announcer)
    voice_duration = len(voice_data)/sr
    duration = max(10.0, 5.3+voice_duration+.55)
    score(duration)
    # The original white lettering and red slash are preserved, never regenerated.
    # Full shot for five seconds, then a darkened hold from its actual final frame;
    # the logo arrives with the announcement. No illustration is scripted.
    logo = ROOT/'art/ui/menu/T_UI_Logo.png'
    slash = ROOT/'art/ui/menu/T_UI_LogoSlash.png'
    vf = (
        f'[0:v]scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,setsar=1,'
        f'tpad=stop_mode=clone:stop_duration={duration},trim=duration={duration},fps=24,'
        'fade=t=in:st=0:d=0.25,fade=t=out:st=4.7:d=1.2[base];'
        '[1:v]scale=920:-1,format=rgba,colorchannelmixer=rr=0.965:gg=0.937:bb=0.886,'
        'fade=t=in:st=5.7:d=0.65:alpha=1[letters];'
        '[2:v]scale=920:-1,format=rgba,colorchannelmixer=rr=0.702:gg=0.071:bb=0.165,'
        'fade=t=in:st=5.18:d=0.22:alpha=1[slash];'
        '[base][slash]overlay=(W-w)/2:(H-h)/2:enable=gte(t\\,5.18)[mark];'
        f'[mark][letters]overlay=(W-w)/2:(H-h)/2:enable=gte(t\\,5.7),fade=t=out:st={duration-.35}:d=0.35[v];'
        '[3:a]highpass=f=65,lowpass=f=11000,bass=g=3:f=120,acompressor=threshold=0.12:ratio=3:attack=8:release=90,'
        'aecho=0.8:0.85:65|115:0.10|0.055,adelay=5200|5200,'
        'aformat=sample_rates=48000:channel_layouts=stereo,volume=2.5[voice];'
        '[4:a]volume=0.7[bed];'
        f'[voice][bed]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=0.93,atrim=duration={duration}[a]'
    )
    run(['ffmpeg','-hide_banner','-loglevel','warning','-y','-i',footage,
         '-loop','1','-i',logo,'-loop','1','-i',slash,'-i',announcer,'-i',OUT/'sound-bed.wav',
         '-filter_complex',vf,'-map','[v]','-map','[a]','-t',str(duration),
         '-c:v','libx264','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-ar','48000','-ac','2','-b:a','192k',
         '-movflags','+faststart',OUT/'ragequit-intro-v1.mp4'])
    print(json.dumps({'path': str(OUT/'ragequit-intro-v1.mp4'), 'seconds':duration}), flush=True)

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('stage', choices=['voice','voice-process','voice-process-v2','video','hosted-video','wan-video','mix','mix-v2','mix-v3'])
    p.add_argument('--seed', type=int, default=42)
    p.add_argument('--image', type=Path)
    p.add_argument('--footage', type=Path)
    p.add_argument('--announcer', type=Path)
    p.add_argument('--prompt-file', type=Path)
    p.add_argument('--seconds', type=float, default=5.0)
    p.add_argument('--out-dir', type=Path)
    args = p.parse_args()
    if args.out_dir: OUT = args.out_dir.resolve()
    OUT.mkdir(parents=True, exist_ok=True)
    if args.prompt_file: VIDEO_PROMPT = args.prompt_file.read_text(encoding='utf-8')
    if args.stage == 'voice': voice(args.seed)
    elif args.stage in ('voice-process','voice-process-v2'):
        if not args.announcer: p.error('--announcer required')
        if args.stage == 'voice-process-v2': voice_process_v2(args.announcer)
        else: voice_process(args.announcer)
    elif args.stage in ('video','hosted-video','wan-video'):
        if not args.image: p.error('--image required')
        if args.stage == 'video': video(args.image, args.seed, args.seconds)
        elif args.stage == 'hosted-video': hosted_video(args.image, args.seed, args.seconds)
        else: wan_video(args.image, args.seed, args.seconds)
    else:
        if not args.footage or not args.announcer: p.error('--footage and --announcer required')
        if args.stage == 'mix-v3': mix_v3(args.footage, args.announcer)
        elif args.stage == 'mix-v2': mix_v2(args.footage, args.announcer)
        else: mix(args.footage, args.announcer)
