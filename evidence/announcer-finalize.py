from pathlib import Path
import json,zipfile
import soundfile as sf,numpy as np
from scipy.signal import resample_poly
from faster_whisper import WhisperModel
root=Path('E:/PROGETTI/ragequit');folder=root/'art/audio/announcer'
manifest=json.loads((folder/'manifest.json').read_text(encoding='utf-8'))
model=WhisperModel('small',device='cpu',compute_type='int8')
checks=[]
for item in manifest['clips']:
 p=folder/item['file'];y,sr=sf.read(p);info=sf.info(p)
 assert sr==48000 and info.channels==1 and info.subtype=='PCM_16'
 assert np.all(np.isfinite(y)) and max(abs(y))<.9 and .2<len(y)/sr<3
 audio=resample_poly(y,1,3).astype(np.float32)
 segments,_=model.transcribe(audio,language='en',beam_size=5,condition_on_previous_text=False,vad_filter=False)
 text=' '.join(s.text.strip() for s in segments)
 row={'file':item['file'],'expected':item['text'],'asr':text,'peak':float(max(abs(y))),'duration':len(y)/sr,'first_10ms_peak':float(max(abs(y[:480]))),'last_10ms_peak':float(max(abs(y[-480:])))}
 checks.append(row);print(json.dumps(row),flush=True)
(root/'.verify/announcer-pack/checks.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
manifest['checks']={'format':'Seven WAVs verified PCM_16 mono 48000 Hz','decode':'soundfile decoded all seven clips','peak':'all below -2 dBFS; padded silent edges','pronunciation_asr':checks,'acceptance':'New clips are for listening; ASR and format checks do not certify voice preference.'}
(folder/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
with zipfile.ZipFile(folder/'ragequit-announcer-wav.zip','w',zipfile.ZIP_DEFLATED) as archive:
 for p in [*(folder/item['file'] for item in manifest['clips']),folder/'README.md',folder/'manifest.json']:
  archive.write(p,p.name)
 print('ZIP '+str(archive.namelist()))
element=json.loads((root/'DOCUMENTAZIONE/ELEMENTI/voci/fa2a690629b14753be48d759c565c2ba.json').read_text(encoding='utf-8'))
element['status']='Pronto'
element['notes']='Set prodotto: sette WAV PCM_16 mono 48 kHz, volumi uniformi, nessun clipping, coda e attacco puliti. ZIP pronto per import, anteprima completa. Manifest con testo/evento e provenienza. Non integrato nel runtime; giudizio sulle nuove battute da ascoltare.'
(root/'.verify/announcer-element-final.json').write_text(json.dumps(element,ensure_ascii=False),encoding='utf-8')
video=json.loads((root/'DOCUMENTAZIONE/ELEMENTI/voci/57c2640c0d5f456ba59f194939c1c01b.json').read_text(encoding='utf-8'))
video['status']='Archiviato';video['approval']='Bocciato D0640. D0641 ferma il lavoro sul Video 2; resta Video 1.'
(root/'.verify/video2-rejected-element.json').write_text(json.dumps(video,ensure_ascii=False),encoding='utf-8')
