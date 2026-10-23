"""D0645: real match events -> seven announcer voices, captured from the game audio mix.
Run with run-unreal-python.ps1 -Sound -AnnouncerReport. Two PIE matches, no saved-user settings.
"""
import json,os,time,traceback
from pathlib import Path
import unreal
OUT=Path(os.environ['RQ_OUT']);START=time.monotonic()
LEVEL=unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
S={'phase':'start','case':0,'at':0.,'busy':False,'done':False,'handle':None}
R={'success':False,'checks':{},'events':[],'errors':[]}
def write(): (OUT/'report.json').write_text(json.dumps(R,indent=2),encoding='utf-8')
def finish(error=None):
 if S['done']: return
 S['done']=True
 if error: R['errors'].append(error)
 csv=OUT/'announcer.csv'
 if csv.exists():
  R['events']=[line.split(',') for line in csv.read_text().splitlines() if line.strip()]
  names=[r[1] for r in R['events']]
  for name in ('FIGHT','PLAYER_ELIMINATED','ENEMY_SLAIN','YOU_DIED','MATCH_OVER','VICTORY','DEFEAT'):
   R['checks']['played_'+name]=name in names
  R['checks']['two_starts']=names.count('FIGHT')==2
  R['checks']['two_ends']=names.count('MATCH_OVER')==2
  R['checks']['results_once']=names.count('VICTORY')==1 and names.count('DEFEAT')==1
 R['success']=bool(R['checks']) and all(R['checks'].values()) and not R['errors'];write()
 if S['handle'] is not None: unreal.unregister_slate_post_tick_callback(S['handle'])
 if unreal.EditorLevelLibrary.get_pie_worlds(False): LEVEL.editor_request_end_play()
 unreal.EditorPythonScripting.set_keep_python_script_alive(False)
def phase(name,now): S['phase']=name;S['at']=now;write()
def tick(delta):
 if S['busy'] or S['done']: return
 S['busy']=True
 try:
  if time.monotonic()-START>240: raise RuntimeError('Timeout '+S['phase'])
  worlds=unreal.EditorLevelLibrary.get_pie_worlds(False)
  if S['phase']=='start': LEVEL.editor_request_begin_play();phase('waiting',0);return
  if S['phase']=='restart':
   if worlds: return
   LEVEL.editor_request_begin_play();phase('waiting',0);return
  if not worlds: return
  w=worlds[0];pc=unreal.GameplayStatics.get_player_controller(w,0)
  p=pc.get_controlled_pawn() if pc else None
  bots=[a for a in unreal.GameplayStatics.get_all_actors_of_class(w,unreal.RagequitCombatCharacter) if a!=p and a.get_controller() and unreal.LyraHealthComponent.find_health_component(a).get_health()>0]
  now=unreal.GameplayStatics.get_time_seconds(w);since=now-S['at']
  if pc and pc.player_state and S['phase'] not in ('result','closing') and unreal.RagequitCombatHUD.get_match_result(pc.player_state)!=0:
   phase('result',now);return
  if not p or len(bots)<2: return
  # Keep bots from changing the scripted score; deaths still go through DealValidationHit and the real game mode.
  # rq.TrainingAttack 0 holds the native bot logic; do not invent a pawn API.
  if S['phase']=='waiting':
   if not S.get('recording'):
    unreal.AudioMixerLibrary.start_recording_output(w,35.);S['recording']=True
   if now<4.5: return
   S['killer']=bots[0].get_controller()
   p.deal_validation_hit(bots[0],5000.) if S['case']==0 else bots[0].deal_validation_hit(p,5000.)
   phase('first',now);return
  if S['phase']=='first' and since>3.0:
   bots[0].deal_validation_hit(bots[1],5000.) if S['case']==0 else S['killer'].get_controlled_pawn().deal_validation_hit(p,5000.)
   phase('second',now);return
  if S['phase']=='second' and since>3.0:
   bots[0].deal_validation_hit(p,5000.) if S['case']==0 else S['killer'].get_controlled_pawn().deal_validation_hit(p,5000.)
   phase('third',now);return
  if S['phase'] in ('third','fourth') and since>4.0:
   if unreal.RagequitCombatHUD.get_match_result(pc.player_state)!=0:
    phase('result',now);return
   p.deal_validation_hit(bots[0],5000.) if S['case']==0 else S['killer'].get_controlled_pawn().deal_validation_hit(p,5000.)
   phase('fourth',now);return
  if S['phase']=='result' and since>5.0:
   unreal.AudioMixerLibrary.stop_recording_output(w,unreal.AudioRecordingExportType.WAV_FILE,'match-'+str(S['case']),str(OUT))
   phase('closing',now);return
  if S['phase']=='closing' and since>2.0:
   if S['case']==0:
    S['case']=1;S['recording']=False;LEVEL.editor_request_end_play();phase('restart',0)
   else: finish()
 except Exception: finish(traceback.format_exc())
 finally: S['busy']=False
try:
 unreal.EditorPythonScripting.set_keep_python_script_alive(True)
 for cmd in ('PixelStreaming2.Editor.AutoStreamPIE 0','rq.Pickups 0','rq.TrainingAttack 0','rq.MatchMode 1',
             'rq.BotCount 3','rq.KillsToWin 1','rq.MatchPhases 1','rq.Countdown 2','rq.RoundDuel 0','rq.BotSkills 0'):
  unreal.SystemLibrary.execute_console_command(None,cmd)
 LEVEL.load_level('/Game/Ragequit/Maps/Arenas/L_Arena_Sunken')
 S['handle']=unreal.register_slate_post_tick_callback(tick);write()
except Exception: finish(traceback.format_exc())
