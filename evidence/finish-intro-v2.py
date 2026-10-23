from pathlib import Path
import json, hashlib, shutil
root=Path.cwd(); work=root/'.verify/intro-v2-work'; out=root/'art/intro'
def finish():
 mappings={'keyframe.png':'duel-keyframe-v2.png','voice-333.wav':'announcer-333.wav','announcer-v2.wav':'announcer-v2.wav','voice-333-prompt.txt':'voice-prompt.txt','fight-217.mp4':'fight-217.mp4','fight-fast-60.mp4':'fight-fast-60.mp4','ragequit-intro-v2.mp4':'ragequit-intro-v2.mp4','image-prompt.txt':'image-prompt.txt','fight-prompt-short.txt':'fight-prompt.txt','sound-bed.wav':'sound-bed.wav'}
 for a in mappings: assert (work/a).is_file(), a
 discarded=Path('E:/PROGETTI/_DA-CANCELLARE/ragequit-intro-v1-bocciata-20261010')
 assert discarded.resolve().is_relative_to(Path('E:/PROGETTI/_DA-CANCELLARE').resolve())
 discarded.mkdir(exist_ok=True,parents=True)
 for p in list(out.iterdir()):
  if p.is_file(): shutil.move(str(p),str(discarded/p.name))
 (discarded/'ELENCO.txt').write_text('Intro v1 bocciata dall autore: D0635 e D0636. Sostituita integralmente dalla v2.',encoding='utf-8')
 for a,b in mappings.items(): shutil.copy2(work/a,out/b)
 d={'status':'Proposta v2 da valutare, non integrata','replaces':'V1 bocciata D0635 D0636','image':{'tool':'built-in imagegen','prompt_file':'image-prompt.txt'},'motion':{'model':'Lightricks/LTX-Video-0.9.5','execution':'local RTX4090','seed':217,'steps':40,'frames':73,'native_fps':24,'prompt_file':'fight-prompt.txt','interpolation':'RIFE ncnn Vulkan rife-v4.6, 110 frames encoded at60fps','speed_multiplier':1.659},'voice':{'model':'Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign','seed':333,'prompt_file':'voice-prompt.txt','text':'WELCOME TO RAGE QUIT! FRAG THEM ALL!','pitch_ratio':0.707107,'tempo':1.08,'formants':'shifted','reference_audio':None,'processing':'Silence trim, bass, compression and soft saturation; tools/create-intro-media.py voice-process-v2'},'logo':{'letters':'art/ui/menu/T_UI_Logo.png','slash':'art/ui/menu/T_UI_LogoSlash.png'},'final':{'file':'ragequit-intro-v2.mp4','width':1280,'height':720,'fps':60,'audio_sample_rate':48000,'channels':2},'verification':{'processed_voice_transcription':'Welcome to Rage Quit, Frag them all!','recognizer':'Whisper small','author_approval':'Pending'},'sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.iterdir() if p.is_file()}}
 (out/'generation.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
if __name__=='__main__': finish()
