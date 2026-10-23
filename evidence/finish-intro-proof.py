import json
from pathlib import Path
p=Path('E:/PROGETTI/ragequit/.verify/ragequit-unreal/intro-window-20261011-021703')
r=json.loads((p/'report.json').read_text());fs=r['frames'];lines=[]
for i,f in enumerate(fs):
    lines += ["file 'frames/"+f['file']+"'",'duration '+str(fs[i+1]['time']-f['time'] if i+1<len(fs) else .1)]
(p/'frames.ffconcat').write_text('\n'.join(lines)+'\n',encoding='utf-8')
r['visual_review']={'fight':True,'logo':True,'transition_to_menu':True,'fresh_profile_name_prompt':True,'sound_capture':False}
(p/'report.json').write_text(json.dumps(r,indent=2),encoding='utf-8')
ident='639231e000d24129a3f480088f3cb533'
root=Path('E:/PROGETTI/ragequit')
row=json.loads((root/'DOCUMENTAZIONE/ELEMENTI/voci'/(ident+'.json')).read_text(encoding='utf-8-sig'))
row.update(status='Integrato',notes='Video 1 originale nel pacchetto: avvio normale verificato visivamente, scontro e logo seguiti dal menu. Profilo isolato nuovo mostra la normale richiesta del nome. Video 2 intatto.',evidence='gate-20261010-202724: 24/24; prelaunch-20261010-233555: 54/54; intro-window-20261011-021703: 185 fotogrammi della sola finestra di gioco, scontro/logo/menu verificati. Runtime EB05578002C5A7A3501B7AE8B4D05C15D8523AFD27D725EAE2D46AE3766395D4 invariato; film SHA256 identico alla sorgente. Registrazione video senza audio; controllo audio sorgente e voci nei rapporti precedenti.')
(root/'.verify/intro-verified-item.json').write_text(json.dumps(row,ensure_ascii=False),encoding='utf-8')
