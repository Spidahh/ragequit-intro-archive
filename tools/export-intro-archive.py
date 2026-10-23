import json,re,shutil,hashlib,subprocess,datetime
from pathlib import Path
SRC=Path('E:/PROGETTI/ragequit')
DST=Path('E:/PROGETTI/ragequit-intro-archive')
DST.mkdir(exist_ok=False)
copied=[];excluded=[];redactions=[]
TEXT={'.json','.jsonl','.md','.txt','.py','.ps1','.sh','.csv','.log','.html'}
secrets=re.compile(r'(?:github_pat_[A-Za-z0-9_]{20,}|gh[pousr]_[A-Za-z0-9]{25,}|hf_[A-Za-z0-9]{25,}|sk-(?:proj-)?[A-Za-z0-9_-]{30,}|-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----)')
signed=re.compile(r'https?://[^\s"<>]*[?&](?:X-Amz-|X-Goog-|Signature=|Policy=)[^\s"<>]*',re.I)
def clean(s,where):
    s,n=secrets.subn('[REDACTED_CREDENTIAL]',s)
    s,m=signed.subn('[REDACTED_TEMPORARY_SIGNED_URL]',s)
    if n or m:redactions.append({'file':str(where),'credentials':n,'temporary_urls':m})
    return s
def put(rel,text):
    p=DST/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(clean(text,rel),encoding='utf8')
def copy(p,rel=None):
    rel=Path(rel) if rel else p.relative_to(SRC)
    out=DST/rel;out.parent.mkdir(parents=True,exist_ok=True)
    if p.suffix.lower() in TEXT:
        out.write_text(clean(p.read_text(encoding='utf-8-sig',errors='replace'),rel),encoding='utf8')
    else:shutil.copy2(p,out)
    copied.append({'source':str(p),'file':rel.as_posix(),'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()})
for p in (SRC/'art/intro').rglob('*'):
    if p.is_file():copy(p)
for p in (SRC/'tools').rglob('*'):
    if p.is_file() and any(x in p.name.lower() for x in ['intro','announcer']):copy(p)
for p in [SRC/'DOCUMENTAZIONE/STUDI/INTRO-DIREZIONI-21-10-2026.md',SRC/'DOCUMENTAZIONE/CLASSI.md',SRC/'DOCUMENTAZIONE/CREDITI-UNREAL.md',SRC/'AGENTS.md']:
    copy(p,Path('context')/p.name)
for name in ['T_UI_Logo.png','T_UI_LogoSlash.png']:
    copy(SRC/'art/ui/menu'/name)
movie=SRC/'unreal/Content/Movies/RagequitIntro.mp4'
if movie.exists():copy(movie,'baseline/RagequitIntro-installed.mp4')
selected=[]
for p in (SRC/'.verify').iterdir():
    if not any(t in p.name.lower() for t in ['intro','announcer','video2','ltx25']):continue
    if any(t in p.name.lower() for t in ['runtime','install']):
        excluded.append({'source':str(p),'reason':'Runtime/dependencies, not authored intro material'});continue
    selected.extend([x for x in p.rglob('*') if x.is_file()] if p.is_dir() else [p])
for p in selected:
    rel=p.relative_to(SRC/'.verify')
    if p.suffix.lower() not in TEXT|{'.png','.jpg','.jpeg','.mp4','.wav','.webp'}:continue
    if p.name=='export-intro-archive.py':continue
    parts=[s.lower() for s in rel.parts]
    reason=None
    if 'intro-studio-yt-20261022' in parts:
        if any(x in parts for x in ['video','frames','sheets']) or p.suffix=='.wav' or p.name.endswith('.transcript.txt'):
            reason='Third-party trailer source media/transcripts; source URLs and analytical measurements published instead'
    elif re.fullmatch(r'\d{5,}\.png',p.name):reason='Reproducible decoded/interpolated intermediate frame; source movie retained'
    if p.stat().st_size>95*1024**2:reason='Large intermediate above regular GitHub file budget; recorded for retrieval'
    if reason:excluded.append({'source':str(p),'bytes':p.stat().st_size,'reason':reason});continue
    copy(p,Path('evidence')/rel)
comfy=Path('C:/Users/magis/.codex/tools/comfyui-ltx/output/RAGEQUIT_LTX23')
if comfy.exists():
    for p in comfy.glob('*.mp4'):copy(p,Path('evidence/ltx23-native-outputs')/p.name)
refs=[]
for p in (SRC/'.verify/intro-studio-yt-20261022/video').glob('*.info.json'):
    d=json.loads(p.read_text(encoding='utf8'))
    refs.append({k:d.get(k) for k in ['id','title','webpage_url','uploader','duration','fps','license']})
put('sources/trailer-references.json',json.dumps(refs,ensure_ascii=False,indent=2))
rows=[]
for line in (SRC/'DOCUMENTAZIONE/DIRETTIVE/direttive.jsonl').read_text(encoding='utf8').splitlines():
    d=json.loads(line);n=int(d['id'][1:]);text=json.dumps(d,ensure_ascii=False)
    if 928<=n<=1093 or n==1212 or (re.search(r'intro|filmato|narrator|announcer',text,re.I) and 'arene' not in d.get('temi',[])):
        rows.append(d)
put('history/author-records.jsonl','\n'.join(json.dumps(d,ensure_ascii=False) for d in rows)+'\n')
put('history/AUTHOR-CHRONOLOGY.md','# Parole, decisioni e bocciature dal registro autore\n\nSono righe originali, non tutte direttive: leggere tipo e stato. Le voci superate sono storia, non requisiti attuali. La finestra 928–1093 include risposte contestuali e richieste di metodo.\n\n'+'\n\n'.join('## '+d['id']+' · '+d.get('data','')+' · '+d.get('tipo','')+' · '+d.get('stato','')+'\n\n'+d.get('parole',d.get('testo',''))+ ('\n\nNota registrata dall’assistente: '+d['testo'] if d.get('parole') and d.get('testo') else '') for d in rows))
session=Path('C:/Users/magis/.codex/sessions/2026/10/21/rollout-2026-10-21T22-29-15-01a16027-602c-7e60-8070-7d94758f789f.jsonl')
msgs=[]
for line in session.open(encoding='utf8'):
    try:r=json.loads(line)
    except ValueError:continue
    x=r.get('payload',{})
    if r.get('type')!='response_item' or x.get('type')!='message' or x.get('role') not in ['user','assistant']:continue
    if x.get('role')=='assistant' and x.get('phase') not in ['commentary','final']:continue
    text='\n'.join(c.get('text','') for c in x.get('content',[]) if c.get('type') in ['input_text','output_text'])
    if not text.strip():continue
    if text.startswith(('# AGENTS.md','<environment_context>','<external_codex_apps_open_page>')):continue
    text=re.sub(r'<in-app-browser-context[\s\S]*?</in-app-browser-context>','',text).strip()
    msgs.append({'date':r.get('timestamp'),'role':x.get('role'),'phase':x.get('phase'),'text':clean(text,'history/conversation')})
put('history/conversation.jsonl','\n'.join(json.dumps(m,ensure_ascii=False) for m in msgs)+'\n')
put('history/CONVERSATION.md','# Conversazione disponibile di questa chat\n\nMessaggi dell’utente e risposte visibili dell’assistente, in ordine. Esclusi ragionamento interno, istruzioni di sistema/sviluppatore, chiamate e output grezzi degli strumenti. Le affermazioni dell’assistente sono storiche e possono essere errate; non sono approvazioni dell’autore. Altre chat sono rappresentate solo dalle registrazioni autore e dai documenti presenti.\n\n'+'\n\n---\n\n'.join('### '+str(m['date'])+' · '+m['role']+'\n\n'+m['text'] for m in msgs))
log=subprocess.check_output(['git','log','--all','--date=iso-strict','--format=%H %ad %s','--','art/intro','tools/intro-ltx23.py','tools/create-announcer-pack.py','DOCUMENTAZIONE/STUDI/INTRO-DIREZIONI-21-10-2026.md'],cwd=SRC,text=True,encoding='utf8')
put('history/source-commits.txt',log)
proof=[]
for line in (SRC/'DOCUMENTAZIONE/PROVE/prove.jsonl').read_text(encoding='utf8').splitlines():
    if re.search(r'intro|announcer|video2',line,re.I):proof.append(line)
put('evidence/proof-register.jsonl','\n'.join(proof)+'\n')
put('MANIFEST.json',json.dumps({'created':'2026-10-23','source_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=SRC,text=True).strip(),'source_dirty':True,'included':copied,'excluded':excluded,'redactions':redactions,'scope':'Public research and handoff archive. No new video production; no assertion of acceptance.'},ensure_ascii=False,indent=2))
print(json.dumps({'destination':str(DST),'files_copied':len(copied),'bytes':sum(x['bytes'] for x in copied),'excluded':len(excluded),'messages':len(msgs),'author_records':len(rows),'redacted_files':len(redactions)}))
