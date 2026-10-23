import subprocess,sys,json
from pathlib import Path
rows=[json.loads(x) for x in Path('DOCUMENTAZIONE/DIRETTIVE/direttive.jsonl').read_text(encoding='utf-8-sig').splitlines()]
text=next(r['parole'] for r in rows if r['id']=='D0938')
subprocess.run([sys.executable,'tools/direttive.py','bocciato','--tema','immagini','--testo','D0938: autore boccia Scontro corale v2. Arciera che tira lentamente nel nulla, assenza di azione e conseguenze, ritmo ancora lento. Le correzioni tecniche di retiming e interpolazione non risolvono la richiesta di un filmato professionale. Richiede uso reale di programmi esterni e skill; non approva questa versione.','--parole',text],check=True)
subprocess.run([sys.executable,'tools/direttive.py','export'],check=True)
p=Path('art/intro/alternative-20261021/corale/v2/provenance.json')
r=json.loads(p.read_text());r['artistic_approval']='Rejected by author D0938: slow, empty action, archer shoots into nothing; technical checks do not satisfy the request.'
p.write_text(json.dumps(r,indent=2),encoding='utf-8')
