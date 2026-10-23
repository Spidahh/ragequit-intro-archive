"""Produce Unreal-ready announcer WAVs from the accepted intro voice.
Run with .verify/intro-runtime/Scripts/python.exe. No Unreal project edits.
Qwen voice-design-then-clone: https://github.com/QwenLM/Qwen3-TTS
"""
from pathlib import Path
import json, subprocess, hashlib, argparse
import numpy as np
import soundfile as sf
import torch
from qwen_tts import Qwen3TTSModel

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'art/audio/announcer'
WORK=ROOT/'.verify/announcer-pack'
LINES=[('fight','FIGHT!','match_start','All players'),
 ('player_eliminated','PLAYER ELIMINATED!','other_player_killed','Spectators or uninvolved players'),
 ('enemy_slain','ENEMY SLAIN!','local_player_kill','Killer only'),
 ('you_died','YOU DIED!','local_player_death','Victim only'),
 ('match_over','MATCH OVER!','match_end','All players'),
 ('victory','VICTORY!','local_player_victory','Winning player or team'),
 ('defeat','DEFEAT!','local_player_defeat','Losing player or team'),
 # 21/10 sera (PIANO-COMPLETO strato 3: «mancano circa 25 battute»): the same voice and chain for the rest of an arena announcer:
 # the countdown, the rounds of a duel, the match's turns, the accolades (ARagequitCombatHUD::AddAccolade) and the tournament
 ('three','THREE!','countdown_3','All players'),('two','TWO!','countdown_2','All players'),('one','ONE!','countdown_1','All players'),
 ('round_one','ROUND ONE!','round_start','Both fighters of a duel in rounds'),('round_two','ROUND TWO!','round_start','Both fighters of a duel in rounds'),
 ('round_three','ROUND THREE!','round_start','Both fighters of a duel in rounds'),('round_four','ROUND FOUR!','round_start','Both fighters of a duel in rounds'),
 ('final_round','FINAL ROUND!','round_start_last','Both fighters of a duel in rounds'),('match_point','MATCH POINT!','round_start_match_point','Both fighters of a duel in rounds'),
 ('round_won','ROUND WON!','round_end_won','The round winner'),('round_lost','ROUND LOST!','round_end_lost','The round loser'),
 ('draw',"IT'S A DRAW!",'match_draw','All players'),('overtime','OVERTIME!','overtime_start','All players'),('sudden_death','SUDDEN DEATH!','sudden_death_start','All players'),
 ('zone_closing','THE ZONE IS CLOSING!','zone_closing','Last standing fighters'),('opponent_left','YOUR OPPONENT LEFT!','forfeit','The fighter left alone'),
 ('first_blood','FIRST BLOOD!','accolade_first_blood','The killer'),('double_kill','DOUBLE KILL!','accolade_double_kill','The killer'),
 ('triple_kill','TRIPLE KILL!','accolade_triple_kill','The killer'),('rampage','RAMPAGE!','accolade_rampage','The killer'),
 ('killing_spree','KILLING SPREE!','accolade_killing_spree','The killer'),('unstoppable','UNSTOPPABLE!','accolade_unstoppable','The killer'),
 ('godlike','GODLIKE!','accolade_godlike','The killer'),('shutdown','Shut down!','accolade_shutdown','The killer'),
 ('revenge','REVENGE!','accolade_revenge','The killer'),('bounty','BOUNTY CLAIMED!','accolade_bounty','The killer'),
 ('champion','CHAMPION!','tournament_champion','The tournament winner')]

# 21/10 sera: every line is heard back before it is kept (faster-whisper small, already in this environment): the voice chain
# (an octave down, saturated) made ten of the 34 lines say something else («DRAW» heard as «Come on», «SHUTDOWN» as «shocked
# old», «ROUND ONE» as «long long»). A line not heard as written is made again with the next seed (+1000), up to TRIES times;
# the seed kept and what was heard go in the manifest. Words that sound the same count as the line (TWO / too, WON / one).
# «DRAW!» alone was never heard right in twelve seeds (one syllable an octave down): the line says «IT'S A DRAW!». A line whose
# words change keeps its key: its old takes are moved out of WORK first (they are kept by key and seed, not by words).
# «SHUTDOWN!» in one word was read as «shocked old», «shope doe» in twelve seeds: the line is written «Shut down!».
TRIES=12
# 22/10 (the author, D0960: «non hai rifatto la frase iniziale del gioco ? Welcome to RageQuit! Frag Them all!!»): the intro's
# line was still the Video 1 take (VoiceDesign, art/intro/announcer-v2.wav), not this cloned voice of the 34. --intro makes it here,
# with the same clone, chain and hearing, and writes it where the intro films take their voice (create-intro-media.py, intro-ltx23.py).
INTRO=('welcome','Welcome to Rage quit! ... Frag them all!',ROOT/'art/intro/announcer-v2.wav')
NUMBERS={'1':'one','2':'two','3':'three','4':'four'}
SOUNDS_LIKE={'welcome':('welcometoragequitfragthemall',),'two':('to','too'),'round_won':('roundone',),'opponent_left':('youropponentsleft',)}
EFFECT=('silenceremove=start_periods=1:start_threshold=-40dB:stop_periods=-1:stop_duration=0.25:stop_threshold=-40dB,'
 'rubberband=pitch=0.707107:tempo=1.08:formant=shifted,highpass=f=45,bass=g=3:f=90,equalizer=f=2400:t=q:w=0.8:g=3,'
 'acompressor=threshold=0.10:ratio=4:attack=5:release=70,asoftclip=type=tanh:threshold=0.45:output=0.9,loudnorm=I=-15:TP=-1.5:LRA=7')

def words(text):
 import re
 text=re.sub(r'\d',lambda m:' '+NUMBERS.get(m.group(0),m.group(0))+' ',text.lower())
 return re.sub(r'[^a-z]','',text)

def heard_right(key,text,heard):
 return words(heard)==words(text) or words(heard) in SOUNDS_LIKE.get(key,())

_WHISPER=None
DEVICE='cuda:0'
def hear(y,sr):
 """What a listener hears in the line: faster-whisper small on the finished clip, at 16 kHz."""
 global _WHISPER
 import torchaudio
 from faster_whisper import WhisperModel
 if _WHISPER is None: _WHISPER=WhisperModel('small',device='cuda',compute_type='float16') if DEVICE.startswith('cuda') else WhisperModel('small',device='cpu',compute_type='int8')
 mono=torchaudio.functional.resample(torch.from_numpy(np.asarray(y,dtype=np.float32)),sr,16000).numpy()
 segments,_=_WHISPER.transcribe(mono,language='en',beam_size=5)
 return ' '.join(s.text for s in segments).strip()

def raw_name(key,seed,index):
 # (the names the first takes were kept under: «fight-433», the others by their key alone)
 if key=='fight': return key+('-'+str(seed) if seed!=333 else '')+'-raw.wav'
 return key+('' if seed==333+index else '-'+str(seed))+'-raw.wav'

def make_line(model,prompt,key,text,seed,index):
 """The line made with this seed (its raw take kept in WORK) through the voice chain of Video 1: (samples, rate)."""
 raw=WORK/raw_name(key,seed,index)
 if not raw.exists():
  torch.manual_seed(seed)
  wavs,sr=model.generate_voice_clone(text=text,language='English',voice_clone_prompt=prompt,max_new_tokens=180,temperature=.7,top_p=.9,repetition_penalty=1.08)
  sf.write(raw,wavs[0],sr,subtype='FLOAT')
 processed=WORK/(key+'-processed.wav')
 subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(raw),'-af',EFFECT,'-ar','48000','-ac','1','-c:a','pcm_f32le',str(processed)],check=True)
 y,sr=sf.read(processed);active=np.flatnonzero(abs(y)>10**(-48/20))
 if not len(active): raise ValueError('Empty voice '+key)
 y=y[max(0,active[0]-round(sr*.015)):min(len(y),active[-1]+round(sr*.06))]
 fade=min(240,len(y)//4);y[:fade]*=np.linspace(0,1,fade);y[-fade:]*=np.linspace(1,0,fade)
 # Match event levels while keeping 2 dB peak headroom; dry center voice, no baked reverb.
 y*=min(10**(-2/20)/max(abs(y)),10**(-20/20)/max(np.sqrt(np.mean(y*y)),1e-9))
 return np.pad(y,(round(sr*.015),round(sr*.045))),sr

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--fight-seed',type=int,default=433)
 parser.add_argument('--no-check',action='store_true',help='keep every line as made, without hearing it back')
 parser.add_argument('--intro',action='store_true',help='make only the intro line (INTRO), not the pack')
 # (22/10: the card was full with another session's ComfyUI; the same model runs on the processor, slower, same takes per seed)
 parser.add_argument('--device',default='cuda:0',help='cuda:0 or cpu');args=parser.parse_args()
 global DEVICE;DEVICE=args.device
 OUT.mkdir(parents=True,exist_ok=True);WORK.mkdir(parents=True,exist_ok=True)
 model=Qwen3TTSModel.from_pretrained('Qwen/Qwen3-TTS-12Hz-1.7B-Base',device_map=DEVICE,dtype=torch.bfloat16 if DEVICE.startswith('cuda') else torch.float32,attn_implementation='sdpa')
 print('Creating reference from original Video 1 speaker',flush=True)
 prompt=model.create_voice_clone_prompt(ref_audio=str(ROOT/'art/intro/announcer-333.wav'),ref_text='Welcome to Rage quit! Frag them all!',x_vector_only_mode=False)
 if args.intro:
  key,text,target=INTRO
  for attempt in range(TRIES):
   seed=333+len(LINES)+1000*attempt
   y,sr=make_line(model,prompt,key,text,seed,len(LINES))
   heard=hear(y,sr);print('  %s seed %d heard %r' % (key,seed,heard),flush=True)
   if heard_right(key,text,heard): break
  else: raise ValueError('%s: never heard as %r in %d seeds' % (key,text,TRIES))
  sf.write(target,y,sr,subtype='PCM_16')
  print(json.dumps({'file':str(target.relative_to(ROOT)),'text':text,'seed':seed,'heard':heard,'seconds':len(y)/sr,'sha256':hashlib.sha256(target.read_bytes()).hexdigest()}),flush=True)
  return
 records=[]
 for index,(key,text,event,audience) in enumerate(LINES):
  base=args.fight_seed if key=='fight' else 333+index
  target=OUT/('VO_RQ_'+key.upper()+'.wav')
  heard=None
  for attempt in range(1 if args.no_check else TRIES):
   seed=base+1000*attempt
   y,sr=make_line(model,prompt,key,text,seed,index)
   if args.no_check: break
   heard=hear(y,sr)
   print('  %s seed %d heard %r' % (key,seed,heard),flush=True)
   if heard_right(key,text,heard): break
  else: raise ValueError('%s: never heard as %r in %d seeds' % (key,text,TRIES))
  sf.write(target,y,sr,subtype='PCM_16')
  info=sf.info(target)
  row={'file':target.name,'text':text,'event':event,'audience':audience,'seed':seed,'heard':heard,'seconds':info.duration,'sample_rate':info.samplerate,'channels':info.channels,'subtype':info.subtype,'peak_dbfs':float(20*np.log10(max(abs(y)))),'rms_dbfs':float(20*np.log10(np.sqrt(np.mean(y*y)))),'sha256':hashlib.sha256(target.read_bytes()).hexdigest()}
  records.append(row);print(json.dumps(row),flush=True)
 manifest={'request':'D0641','reference':'art/intro/announcer-333.wav','accepted_voice':'art/intro/announcer-v2.wav','reference_sha256':hashlib.sha256((ROOT/'art/intro/announcer-333.wav').read_bytes()).hexdigest(),'model':'Qwen/Qwen3-TTS-12Hz-1.7B-Base','method':'Clone original synthetic speaker, then same Video 1 pitch, formant, EQ and saturation chain. No Quake recording used.','license':'Generated original synthetic announcer; Qwen3 model Apache-2.0','format':'WAV PCM signed 16-bit, mono, 48000 Hz','routing':'2D centered announcer, no spatial attenuation. Kill/death clips are recipient-specific; avoid playing PLAYER ELIMINATED to killer/victim as well. Queue MATCH OVER before VICTORY/DEFEAT.','integration':'Runtime integration authorized by D0645: RagequitAnnouncer.cpp consumes authoritative match events; imported assets in /Game/Ragequit/Audio/Announcer. Current release verification in DOCUMENTAZIONE/PIANO-DEFINITIVO.md.','clips':records,'sources':['https://github.com/QwenLM/Qwen3-TTS','https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-audio-implementation-in-parrot']}
 (OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
 preview=[]
 for row in records:
  y,sr=sf.read(OUT/row['file']);preview.extend([y,np.zeros(round(sr*.65))])
 sf.write(OUT/'announcer-preview.wav',np.concatenate(preview),48000,subtype='PCM_16')
 print('PACK COMPLETE',flush=True)

if __name__=='__main__': main()
