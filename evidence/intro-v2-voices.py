from pathlib import Path
import json, torch, soundfile as sf
from qwen_tts import Qwen3TTSModel

out=Path(__file__).resolve().parent/'intro-v2-work'
out.mkdir(exist_ok=True)
model=Qwen3TTSModel.from_pretrained('Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign',device_map='cuda:0',dtype=torch.bfloat16,attn_implementation='sdpa')
styles=[
 (111, 'A mature male monster with a thunderously deep bass voice and extremely coarse gravelly rasp. Very low chest rumble, harsh hoarse throat, audible vocal fry, brutal aggressive delivery. Like a giant orc growling a battle command. English words clear and forceful. Never smooth or polished. Speak at a normal pace, not slowly.'),
 (222, 'English male voice. An enormous sixty-year-old warrior with a very low, thick, coarse bass voice. Severely raspy, gravelly, growling, hoarse and guttural, with deep chest resonance. A fierce arena announcer barking short commands, breath and harsh throat texture audible. Strong and threatening, no whisper, no singing. Normal speech tempo.'),
 (333, '英语，男性，极低沉的男低音，粗犷沙哑的嗓音，强烈的喉音和声带沙沙感，像巨大的兽人战士在怒吼。胸腔共鸣极强，音调非常低，威严、凶狠、有力量。每个英文单词清晰，正常语速，不要温柔，不要光滑的播音腔。')
]
for seed,style in styles:
 torch.manual_seed(seed)
 wavs,sr=model.generate_voice_design(text='WELCOME TO RAGE QUIT! FRAG THEM ALL!',language='English',instruct=style,max_new_tokens=220,temperature=.8,top_p=.9)
 path=out/f'voice-{seed}.wav'
 sf.write(path,wavs[0],sr)
 (out/f'voice-{seed}-prompt.txt').write_text(style,encoding='utf-8')
 print(json.dumps({'file':str(path),'seconds':len(wavs[0])/sr}),flush=True)
