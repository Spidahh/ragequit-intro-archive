from pathlib import Path
import hashlib, json, subprocess

root = Path(__file__).resolve().parents[1]
out = root/'art/intro'
plan = root/'DOCUMENTAZIONE/PIANO-DEFINITIVO.md'
text = plan.read_text(encoding='utf-8')
start = text.index('## Studio della mini intro — 10/10/2026')
end = text.index('## Aperto', start)
section = '''## Mini intro — prova video del 10/10/2026

File: `art/intro/ragequit-intro-v1.mp4`, **10,83 secondi**, H.264 1280×720, audio AAC stereo 48 kHz.
Una proposta concreta da vedere e ascoltare, non ancora approvata dall'autore o integrata nel gioco.

Dopo la richiesta D0628 e il via alla produzione D0630, l'autore ha bocciato la direzione CGI generica
(D0633, D0634): vuole **un mago contro un guerriero, con stile strano e figurato**, non immagini in-game.
La prova usa figure illustrate a inchiostro e gouache, mago lungo e chiaro contro guerriero nero con mantello rosso.
Il guerriero affonda la spada, il mago evita il colpo e risponde col bastone e una scarica magica,
il guerriero viene respinto. Lo scontro dura circa cinque secondi; il logo originale emerge nella chiusura,
osso e rosso come Lama. Non sono usati filmati del gioco, modelli Paragon o carte Predecessor.

La voce sintetica originale dice **WELCOME TO RAGEQUIT! FRAG THEM ALL!**: Qwen3-TTS VoiceDesign locale,
indicazione di basso maschile ruvido e quasi orchesco, trattamento leggero di altezza (-3 semitoni con formanti
preservate), compressione e riverbero breve. Nessuna voce di un attore clonata o audio di Quake riutilizzato.
Il riconoscimento Whisper small sul WAV trattato restituisce “Welcome to Rage Quit!” / “Frag them all!”;
la naturalezza e la preferenza per questa voce richiedono l'ascolto dell'autore, non si deducono dal testo riconosciuto.

Produzione: skill imagegen per il fotogramma sorgente; Wan2.2-Fast nel demo gratuito ZeroGPU per lo scontro;
Qwen3 locale per la voce; FFmpeg per logo e montaggio; suoni procedurali originali. Il demo riceve solo il
fotogramma generato e il prompt, nessun file del gioco. Nessun acquisto o abbonamento.
Le prove LTX con corpi quasi immobili sono state scartate. La cartella `art/intro` contiene solo il materiale
della proposta consegnata, con prompt e provenienza in `generation.json`.

Controlli: fotogrammi dello scontro e del montaggio guardati in `.verify/intro-*-contact-sheet.png`;
153/81 fotogrammi nei tentativi LTX/Wan, la clip usata è Wan (81 a 16 fps), montaggio finale a 24 fps;
durata e tracce lette con ffprobe, decodifica completa senza errori, voce e audio presenti.
Questo certifica il file e il contenuto visto nei fotogrammi, non l'approvazione estetica.
Strumento: `tools/create-intro-media.py`; ambiente isolato `.verify/intro-runtime`, modelli in cache fuori da Git.
Scheda del registro: `639231e000d24129a3f480088f3cb533`, Pronto, approvazione in attesa.

'''
plan.write_text(text[:start]+section+text[end:],encoding='utf-8')
record_path=root/'DOCUMENTAZIONE/ELEMENTI/voci/639231e000d24129a3f480088f3cb533.json'
record=json.loads(record_path.read_text(encoding='utf-8'))
record['status']='Pronto'
record['evidence']='MP4 H.264 1280x720, 10.83 s, AAC stereo 48 kHz; fotogrammi dello scontro e logo guardati; WAV trattato riconosciuto da Whisper small con entrambe le frasi corrette.'
record['notes']='Proposta video originale, non gameplay e non integrata. Stile figurativo mago contro guerriero dopo D0633. Aspetto e voce da valutare. Generazione e trattamento documentati in art/intro/generation.json; prompt nelle sorgenti. Nessun servizio a pagamento.'
temp=root/'.verify/intro-element.json'
temp.write_text(json.dumps(record,ensure_ascii=False),encoding='utf-8')
subprocess.run(['python','tools/elementi.py','save','--file',str(temp)],cwd=root,check=True)
manifest={
    'status':'Proposta da valutare, non integrata',
    'image':{'tool':'built-in imagegen','prompt_file':'image-prompt.txt'},
    'motion':{'model':'Wan-AI/Wan2.2-I2V-A14B-Diffusers with Lightx2v LoRA','demo':'https://huggingface.co/spaces/prithivMLmods/Wan2.2-Fast','prompt_file':'fight-prompt.txt','seed':91,'steps':4,'duration_requested_seconds':5},
    'voice':{'model':'Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign','license':'Apache-2.0','prompt_file':'voice-prompt.txt','seed':73,'text':'Welcome to Rage quit! ... FRAG THEM ALL!','pitch_ratio':0.840896,'tempo':0.95,'formants':'preserved','reference_audio':None},
    'logo':{'letters':'art/ui/menu/T_UI_Logo.png','slash':'art/ui/menu/T_UI_LogoSlash.png','letters_color':'F6EFE2','slash_color':'B3122A'},
    'audio_effects':'Original procedural synthesis; no third party game samples',
    'final':{'file':'ragequit-intro-v1.mp4','width':1280,'height':720,'duration_seconds':10.833333,'audio_sample_rate':48000,'channels':2},
    'sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.iterdir() if p.is_file() and p.suffix in ['.mp4','.wav','.png']}
}
(out/'generation.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
