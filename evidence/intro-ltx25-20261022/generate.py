import json,time,shutil,subprocess,hashlib
from pathlib import Path
from gradio_client import Client
out=Path(__file__).parent
prompt=('A fully animated 2D dark fantasy action scene, expressive ink outlines and richly painted shadows. '
 'A blond warrior in black bronze armor with a red cape fights a bearded mage in a dark purple hood in a ruined stone arena. '
 'The fight is already moving at full speed in the first frame. The warrior rushes forward and swings his axe horizontally at the mage. '
 'The mage ducks sharply under the blade, and the axe strikes a stone pillar behind him, showering them with chips. '
 'The mage immediately counterattacks with a short violet burst that strikes the warrior\'s raised bronze shield. '
 'The warrior recoils one step from the impact and surges forward again while the mage dodges sideways. '
 'The camera tracks alongside both fighters in a clear medium-wide shot, following their fast footwork and connected attacks. '
 'Forceful weight shifts, sharp weapon arcs, fabric whipping with the motion, coherent faces and bodies throughout. '
 'Real-time rapid fighting, continuous physical action. Synchronized sound of boots, axe striking stone and a heavy shield clang. Wordless combat.')
r={'request':'D0949','provider':'Lightricks/LTX-2.5 official Hugging Face Space',
   'space_revision':'c42e4cd512ec0a861024699f031538eb7bf093a7','mode':'text-to-video, no starting still image',
   'prompt':prompt,'seed':144713,'size':[1024,576],'duration_requested':5.,'fps':24,
   'decoder':'conv','auto_len':False,'prompt_enhancement':False,'spend':0,'status':'submitted',
   'time':time.strftime('%Y-%m-%dT%H:%M:%S')}
p=out/'generation.json'
def save():p.write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8')
save()
try:
    c=Client('Lightricks/LTX-2.5',verbose=False)
    result=c.predict(prompt=prompt,image_path=None,height=576,width=1024,duration_s=5.,seed=144713,
        decoder='conv',auto_len=False,randomize_seed=False,do_enhance=False,api_name='/run')
    video=result[0]
    if isinstance(video,dict):video=video.get('video',video.get('path'))
    target=out/'ltx25-native.mp4';shutil.copy2(video,target)
    subprocess.run(['ffmpeg','-v','error','-i',str(target),'-f','null','-'],check=True)
    r.update(status='completed',output=str(target),sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
             returned_prompt=result[1],returned_seed=result[2],returned_length=result[3])
except Exception as e:
    r.update(status='failed',error=str(e));raise
finally:save()
print(json.dumps({'status':r['status'],'output':r.get('output')}),flush=True)
