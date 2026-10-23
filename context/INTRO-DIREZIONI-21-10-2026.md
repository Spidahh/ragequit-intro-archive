# RAGEQUIT — tre direzioni per una nuova intro

21 ottobre 2026. Studio richiesto dall'autore, D0928–D0929. **D0934–D0935: bocciata anche la v2 della direzione 02; l'autore richiede produrre le altre due proposte e lavorare con skill, plugin e strumenti interni/esterni sulla fluidità e sulla finitura. 01 e 03 tornano in produzione. Nessun nuovo filmato è ancora approvato per sostituire l'intro nel gioco.** Non introduce regole, storia o meccaniche.

## Risultato cercato

Una breve apertura che rappresenti il PvP di RAGEQUIT, con identità riconoscibile e finitura professionale. L'autore autorizza a ripensare interamente l'idea del video e chiede opzioni. Il precedente mago contro guerriero è una possibilità, non il vincolo creativo di questo studio.

## Verifica del materiale corrente

- `art/intro/video-1.mp4` e `unreal/Content/Movies/RagequitIntro.mp4` hanno lo stesso SHA256: `007da5f972d870e42f74f9c0163aab5b2c4d9c5ef53a9bc7adde3188fd3c187d`.
- Filmato attuale: 6,2 s, 1280×720, H.264, 60 fps, audio AAC. Controllati con ffprobe il 21/10. Campionamento visivo a due fotogrammi al secondo in `.verify/intro-studio-20261021/intro-attuale.jpg`.
- In questo campionamento lo scontro occupa circa i primi due secondi; il resto è soprattutto marchio. I due combattenti non identificano chiaramente le classi attuali. Questa è una valutazione editoriale, non una misura del gradimento dell'autore.
- La produzione corrente documenta LTX 0.9.5, 73 frame nativi a 24 fps, accelerazione ×1,659 e interpolazione RIFE. Un file a 60 fps non dimostra un movimento ben animato.
- Il Video 2 è bocciato. Le sue tre immagini e l'animazione FastWan non sono una direzione da ripresentare con semplici cambi di colore. Le critiche D0634–D0642 sono state rilette nell'archivio vivo.
- `DOCUMENTAZIONE/CLASSI.md`, aggiornato il 21/10, distingue i dieci kit. Le immagini locali di Gideon/Voidseer e Terra/Sentinel sono riferimenti storici di identità, non prova del pacchetto odierno.
- Strumenti/materiali già presenti: Unreal 5.8, modelli e animazioni Paragon, logo originale, voce dell'intro, librerie di suoni nel progetto, FFmpeg, precedenti ambienti locali per video generativo. Le clip sincronizzate e il trattamento illustrato proposti sotto devono ancora essere prodotti.
- La skill spidah-projects è stata letta; l'hub `E:/PROGETTI/PORTFOLIO` indicato dalla skill non esiste su questo PC. Lo studio usa pertanto le fonti vive di RAGEQUIT; nessuna sincronizzazione dell'hub è stata eseguita.

## Riferimenti e cosa ne ricaviamo

I collegamenti sono riferimenti di produzione e linguaggio. Nessun loro filmato, musica o personaggio entra nell'intro. Le durate e le scene proposte sotto sono nostre scelte editoriali, non ricette dichiarate dagli studi.

1. [Spellbreak — Official Launch Cinematic, canale PlayStation](https://www.youtube.com/watch?v=gVgaivQgU48). Fonte vicina per un gioco di magie mirate: la presentazione ufficiale parla di combattimento multiplayer e combinazioni elementali. Osservati nel browser fotogrammi delle prime sequenze: personaggi stilizzati, preparazione del gesto, magia con una forma leggibile. Applicazione: rendere riconoscibile l'azione prima di riempire lo schermo di effetti. Non ne importiamo battle royale o regole.
2. [VALORANT — RETAKE, canale ufficiale](https://www.youtube.com/watch?v=hhlgphVf-1g) e [Riot: The Story of VALORANT so far](https://playvalorant.com/en-gb/news/dev/the-story-of-valorant-so-far/). Riot esplicita il rapporto fra conflitto delle cinematiche ed esperienza del gioco. Applicazione: capacità e identità dei personaggi devono sostenere la scena. Consultati presentazione e crediti, non effettuata un'analisi fotogramma per fotogramma del corto.
3. [Axis Studios — DUALITY, colorscript e immagini finali](https://axisstudios.artstation.com/projects/vDvg2E). Documenta sviluppo visivo e finitura come parti di una produzione coordinata. Applicazione: fissare luce, personaggi e palette fra le inquadrature; il nome di un modello generativo non sostituisce questa fase.
4. [Riot — A Twist of Fate](https://www.youtube.com/watch?v=tEnsqpThaFg). Riferimento per la direzione corale di scontri fra campioni. Fonte ufficiale consultata; usato come confronto di formato, non come prova che un'identica produzione sia disponibile localmente.
5. [Fortiche — RISE](https://forticheprod.com/portfolio/rise/). La scheda ufficiale lo identifica come video musicale per i Worlds 2018. Applicazione proposta: personaggi, azione e ritmo musicale possono formare una sigla; non occorre raccontare una nuova mitologia di RAGEQUIT.
6. [Fortiche — lavori](https://forticheprod.com/fortichize/) e [Arcane, sito ufficiale](https://www.arcane.com/en-gb/). Riferimento di famiglia per una title sequence autoriale. La proposta scultorea sotto è una nostra direzione e non una dichiarazione sul metodo di produzione di Arcane.
7. [Epic — Movie Render Pipeline](https://dev.epicgames.com/documentation/unreal-engine/movie-render-pipeline-in-unreal-engine). Conferma la possibilità di renderizzare offline sequenze e filmati da Unreal. Non certifica la qualità artistica della nostra scena né che il progetto abbia già una sequenza pronta.

## 01 — Scontro corale

Stato dopo D0934: **produzione video autorizzata**.

**Promessa:** far capire subito che RAGEQUIT è una sfida fra classi diverse, con mira, difese e risposte.

Circa 16–18 secondi. Una freccia della Deadeye, dopo tensione completa, attraversa il quadro; stacco sullo scudo della Sentinel che la ferma e sul peso dell'impatto. Cambio di distanza: la Sentinel avanza contro il Voidseer; il mago evita la chiusura con Phase Step, senza parare. Un ultimo inserto del Reaper rivela falce e scatto, poi il montaggio converge sul logo e sulla voce. Quattro classi bastano: non comprimere tutti e dieci i kit in una lista.

Le azioni si raccordano con direzione del movimento e suono, mantenendo chiara la geografia. Non affermiamo una modalità a squadre particolare e non attribuiamo poteri nuovi alle classi. Materiali dipinti, silhouette solide, luce controllata; nessuna ripresa di una normale partita. Il confronto di formato è A Twist of Fate; la leggibilità della magia viene dal riferimento Spellbreak.

**Valore:** rappresenta il gioco più esplicitamente delle altre due opzioni. **Costo concreto:** quattro personaggi e più contatti da coreografare; richiede più animazione e verifica di continuità. Non è automaticamente la scelta migliore perché mostra più cose.

## 02 — L'istante prima

Stato dopo D0934: **entrambe le prove video bocciate**, non integrare. Produzione precedente con geometria, pose e camera reali dentro Unreal. Script `tools/unreal/render-intro-istante.py` e `tools/assemble-intro-istante.py` conservati come traccia della prova ritirata.

**Promessa:** un'apertura breve, riconoscibile e molto curata, costruita attorno alla tensione di uno scontro.

Circa 12–14 secondi. Si entra vicinissimi a un impatto sospeso sullo scudo; la camera si sposta davvero nello spazio e scopre la Sentinel, poi il Voidseer e la traiettoria dell'attacco. Frammenti, tessuto e corpi compongono un unico istante, trattato come una scultura di avorio, metallo annerito e piccoli accenti granata. Non c'è ghiaccio e il tempo sospeso è una scelta di montaggio, non un potere del gioco. Dopo la preparazione il tempo riparte: una breve azione completa, una risposta e chiusura sul marchio.

Il tempo sospeso deve essere tridimensionale: passaggi fra primo piano e sfondo, parallasse, superfici rivelate dalla luce. Un'immagine piatta ingrandita non basta. La forma degli eroi e delle armi rimane riconoscibile anche nel trattamento scultoreo.

**Valore:** grande identità con due protagonisti e pochi momenti da animare; concentrazione del lavoro su composizione, materiali, luce e suono. **Costo concreto:** serve una scena tridimensionale curata e la ripartenza deve funzionare davvero; un concept dipinto non dimostra questo risultato.

**Il precedente consiglio dell'assistente per l'intro all'avvio è ritirato dopo il fallimento delle due prove.** I filmati prodotti non hanno realizzato la promessa della tavola.

## 03 — Sigla illustrata

Stato dopo D0934: **produzione video autorizzata**.

**Promessa:** un marchio audiovisivo aggressivo, con personalità grafica e forte ritmo.

Circa 14–18 secondi. Dettagli dei volti, armi e gesti si trasformano l'uno nel successivo: l'arco teso introduce una traiettoria; il bordo dello scudo taglia il quadro; la falce porta al cappuccio del Reaper; il vuoto del portale apre il titolo. Le transizioni sono motivate dai soggetti reali. Brevi azioni animate fra pose forti, con pittura, segno, materia e profondità a livelli. Non una carrellata di carte né un semplice slideshow con zoom.

RISE è il riferimento per il rapporto fra personaggi, azione e musica, non per copiarne la vicenda o la canzone. La nostra sigla non deve promettere un viaggio, una guerra o un antagonista che RAGEQUIT non possiede.

**Valore:** linguaggio più figurato e maggiore libertà rispetto al render dei modelli. **Costo concreto:** una serie coerente di illustrazioni originali, transizioni e brevi animazioni; una bella immagine isolata non verifica la continuità della sequenza. La musica deve avere provenienza e uso consentito, oppure essere originale: nessun brano dei riferimenti.

## Metodo di produzione proposto

Per 01 e 02: usare i modelli reali come base per identità e geometria, con camere e contatti controllati; animazioni dei kit come partenza e correzione delle pose dove lo scontro lo richiede. Render cinematografico dedicato, con trattamento artistico proposto e mostrato prima della sostituzione del video. Non basta cambiare la luce a un filmato di partita.

Per 03: fissare una tavola dei personaggi e un linguaggio pittorico comune, poi costruire transizioni e animazione breve per ogni passaggio. La generazione di immagini serve al concept e all'illustrazione, non a garantire da sola movimento e regia.

Non ripetere come soluzione principale il vecchio flusso di tre immagini indipendenti animate liberamente e accelerate: il Video 2 ha già mostrato che non è sufficiente per questa richiesta. Non è un divieto generale di usare AI, ma una conclusione sul metodo locale precedente.

Materiali riutilizzabili: logo originale, voce esistente se regge nel nuovo montaggio, modelli/animazioni ed effetti sonori di cui il progetto documenta provenienza e licenza. Niente nuovi account o acquisti richiesti dallo studio. Attenzione: le coreografie cinematografiche, il trattamento scultoreo/illustrato e l'eventuale base musicale non sono asset già pronti; costituiscono il lavoro di produzione.

## Cosa dimostra la tavola di proposta

Tavola finale: [tre-direzioni.png](../../art/intro/proposte-20261021/tre-direzioni.png).

La tavola generata con imagegen confronta tre linguaggi, usando due riferimenti locali dei personaggi. Non contiene filmati animati e non è prova di capacità produttiva, fedeltà di ogni fotogramma, qualità del mix o approvazione. La direzione 01 vi mostra un singolo momento esemplificativo, non l'intera coreografia corale. Il filmato attuale nel gioco resta invariato durante lo studio.

La prima tavola è stata corretta perché il riquadro 02 conservava pelle e armature colorate, risultando troppo vicino al riquadro 01: il materiale scultoreo deve distinguersi chiaramente, non essere soltanto un altro primo piano dello stesso scontro. Le immagini sono concept generati, non asset già accettati.

## Prima prova video della direzione 02 — D0930

Filmato: [ragequit-istante-prima-v1.mp4](../../art/intro/istante-prima-20261021/ragequit-istante-prima-v1.mp4). **BOCCIATO dall'autore, D0931/D0932: non capisce il risultato, non percepisce animazioni e lo giudica inutile. Non va integrato né ripresentato come proposta valida.** Le proposte 01 e 03 restano in sospeso.

14,25 secondi, 1920×1080, 24 fps nativi, H.264 e AAC stereo 48 kHz. Dieci secondi di scena 3D seguiti dal marchio originale e dalla voce già presente. I primi 6,5 secondi tengono sospesi i corpi mentre si sposta la camera; seguono impatto, avanzamento della Sentinel, movimento del Voidseer e fendente. Il trattamento è una prova scultorea dei modelli effettivi: non è stato usato image-to-video.

Produzione: mondo Unreal temporaneo non salvato; mesh principali dai loadout attuali, normali dei materiali dei personaggi, trattamento avorio e accenti scuri, frammenti dalla libreria Rock Collection 04 e forme dell'effetto di Gideon. Le pose sono valutate con `RagequitHeroRetarget.HoldEmote`, che aggiorna le ossa anche fuori inquadratura e applica le correzioni del personaggio. Nessuna modifica salvata a mappe, loadout o asset di gioco. Il vecchio filmato installato conserva SHA256 `007da5f972d870e42f74f9c0163aab5b2c4d9c5ef53a9bc7adde3188fd3c187d`.

I layout iniziali sono stati scartati durante la produzione per esposizione, inquadratura, forme dell'effetto e pose non aggiornate nel mondo fuori schermo; non sono versioni proposte come finite. Il render consegnato comprende 240 fotogrammi nativi in `.verify/ragequit-unreal/intro-istante-final-20261021-230529`. Il manifest [provenance.json](../../art/intro/istante-prima-20261021/provenance.json) conserva sorgenti, hash, eventi sonori, impostazioni e verifica del file.

Controlli finali: decodifica integrale FFmpeg, formato verificato con ffprobe, campionamento del montaggio completo in `.verify/intro-studio-20261021/video-v1-check.jpg`, mix senza campioni troncati (picco 0,6073). Registrati in `DOCUMENTAZIONE/PROVE/prove.jsonl` come `intro-istante-v1-file-video`. Sono verifiche tecniche e di composizione; non attestano il gradimento artistico né l'ascolto dell'autore. SHA256 del filmato: `a3ca5869f6a36ef3cadcf2b35bc781d6e8b041b319f8100ef52751521fabc570`.

## Rifacimento dopo D0931

Ritirata la struttura con 6,5 secondi di corpi fermi. La nuova versione mette lo scontro animato all'inizio e mantiene soltanto sei fotogrammi (0,25 s) di sospensione dentro il primo impatto. Lanci, parata, avanzamenti, fendenti, teletrasporti e reazioni sono distribuiti nei dieci secondi di scena; il montaggio e il suono sono rifatti su questi eventi. La camera accompagna il movimento dei corpi e non lo sostituisce. Le altre due direzioni restano in sospeso.

Il renderer registra, per ogni fotogramma, la posizione delle mani rispetto alla radice dei due attori: il controllo del movimento dei corpi esclude la camera. La soglia di movimento è un controllo tecnico, non certifica bellezza, feeling o accettazione. La v1 ha dimostrato che render 3D, decodifica e immagini campionate verdi non bastano per giudicare questa richiesta.

D0933: l'autore chiede di aspettare la fine del packaging già in corso prima di avviare il render. Il packaging non viene interrotto.

### Seconda prova animata

File di revisione: [ragequit-istante-prima-v2.mp4](../../art/intro/istante-prima-20261021/ragequit-istante-prima-v2.mp4). Dieci secondi di azione, seguiti dal titolo e dalla voce già presenti nel progetto; 14,25 secondi complessivi. La sospensione dura 0,25 secondi. Il controllo del movimento rileva 234 cambiamenti su 239 transizioni fra fotogrammi, misurando le mani rispetto alla radice degli attori, senza contare la camera. Questo dimostra movimento articolato, non qualità professionale o approvazione artistica.

Il primo tentativo di questo rifacimento si è interrotto sulla reazione additiva HitReact: usata come posa intera, provocava valori NaN nel retarget. Sostituita con RMB_HitReact e Knockback_back di Terra e Stun_Start di Gideon, tutte sequenze complete; il renderer ora rifiuta clip additive prima di passarle a HoldEmote. Corretto anche il campo iniziale, che escludeva il guerriero. Nessuna modifica al codice di gioco per aggirare il problema.

Il packaging è stato lasciato terminare prima del render. Le direzioni 01 e 03 restano in sospeso, e la v1 resta bocciata. La v2 è una nuova prova da vedere: non sostituisce il filmato installato e non è dichiarata approvata. Il manifest [provenance-v2.json](../../art/intro/istante-prima-20261021/provenance-v2.json) conserva render, sorgenti, misure e controlli del file.

## D0934 — nuove produzioni delle direzioni 01 e 03

Anche la seconda prova della direzione 02 è bocciata (D0935). Le frasi del paragrafo precedente descrivono la consegna precedente e non il suo stato attuale. Non si correggono di nuovo le statue: si torna alle altre due direzioni richieste dall'autore.

### Strumenti realmente verificati

- Skill lette: Imagegen, UE Sequencer/Cinematics, Adobe Edit Quick Cut, Game Asset Production e Spidah Projects. La pipeline Unreal precedente è stata valutata sul suo risultato bocciato; non riutilizzata per i nuovi filmati.
- Adobe Quick Cut seleziona momenti di clip esistenti; il suo contratto non include rigging, raccordo delle pose o generazione del movimento. Il render timeline di Adobe monta e ridimensiona sorgenti. Non si dichiara che questi strumenti correggano una coreografia spezzata.
- Il plugin Figma/Weave è stato interrogato: il collegamento dell'account Weave manca. Non sono stati creati account, collegamenti, abbonamenti o acquisti.
- Il servizio pubblico [Wan2.2-Fast](https://huggingface.co/spaces/prithivMLmods/Wan2.2-Fast) è stato interrogato tramite il suo client Gradio già presente. Il contratto espone Wan2.2 I2V 14B con Lightning LoRA. Ha completato gratuitamente due clip; la terza richiesta ha restituito quota ZeroGPU esaurita. Ricevuta del rifiuto conservata, nessun tentativo di aggirare la quota.
- Sul PC esistono FastWan 5B e l'ambiente di inferenza: provati come alternativa locale per il secondo scambio corale. Il modello distillato impiega tre passi come documentato da [FastVideo](https://github.com/hao-ai-lab/FastVideo/blob/main/docs/distillation/dmd.md). La clip è stata scartata dall'assistente per duplicazione della falce e deriva visiva. Il percorso FastWan sperimentale è stato tolto dal nuovo helper attivo; il filmato scartato resta nella cartella di verifica, escluso dalla consegna.
- Per il secondo scambio è stato infine usato [LTX-Video 0.9.5](https://huggingface.co/Lightricks/LTX-Video-0.9.5), già presente e usato nel progetto: 40 passi, 768×448, 121 fotogrammi a 24 fps. Nel montaggio si usa il tratto 0,12–3,50 s. Il prompt di questo tentativo è stato troncato dal limite predefinito di 128 token; non si afferma che ogni azione descritta nel prompt integrale sia stata eseguita dal modello. Il risultato è stato selezionato sulle immagini prodotte, non sulla completezza nominale del prompt.
- [RIFE ncnn Vulkan](https://github.com/nihui/rife-ncnn-vulkan), versione locale con modello 4.6 e licenza MIT, genera fotogrammi intermedi. Applicato separatamente a ogni inquadratura; gli stacchi del montaggio non vengono interpolati.
- FFmpeg assembla le clip, effettua il trattamento cromatico, compone il logo originale e il mix con Foley posseduti e voce esistente. L'ambiente locale e le risorse sono quelli già disponibili. Nessuna nuova dipendenza installata.

### Scelte per il movimento e la finitura

Tre keyframe creati separatamente con Imagegen; identità e armi riferite alla tavola di proposta e alle immagini locali dei personaggi. I [prompt integrali](../../art/intro/alternative-20261021/image-prompts.md) e i prompt di movimento sono salvati. Il movimento è generato come azione continua nella singola scena, non come passaggio fra pose HoldEmote non raccordate. La scelta produttiva può ancora presentare difetti generativi: nessun modello o numero di fotogrammi certifica il risultato professionale.

Scontro corale usa quattro classi in due scambi: Sentinel/Voidseer, poi Deadeye/Reaper. Sigla illustrata usa il duello Sentinel/Voidseer con inchiostro, carta e pennellate. La seconda è volutamente più breve del trattamento scritto iniziale: circa nove secondi con marchio e voce, anziché un riempimento di sedici secondi con movimenti ripetuti.

Le sorgenti Wan ospitate risultano 832×480, 81 fotogrammi a 16 fps; la sorgente LTX è 768×448 a 24 fps. La consegna a 1920×1080/60 fps usa interpolazione RIFE e ingrandimento Lanczos: **non è un render nativo 1080p**. Durata conservata nella conversione; nessuna accelerazione nascosta per ottenere i 60 fps. L'interpolazione attenua la cadenza temporale, non corregge anatomia, armi, contatti o una scelta di regia sbagliata. I file sono proposte da giudicare guardandole.

Sigla illustrata: [video](../../art/intro/alternative-20261021/illustrata/ragequit-illustrata-v1.mp4), [ricevuta](../../art/intro/alternative-20261021/illustrata/provenance.json). Durata 8,98 s. Controllata la decodifica integrale, il formato e il mix senza clipping; campionamento del montaggio in `.verify/intro-studio-20261021/illustrata-final-check.jpg`. Verifica tecnica registrata in prove.jsonl; approvazione artistica ancora assente.

Scontro corale: [video](../../art/intro/alternative-20261021/corale/ragequit-corale-v1.mp4), [ricevuta](../../art/intro/alternative-20261021/corale/provenance.json). Durata 12,49 s. Due scambi montati senza interpolare lo stacco; prima clip Wan, seconda LTX. Tentativi esclusi e rifiuto della quota conservati in `corale/production-attempts.json`. Controllata la decodifica integrale, il formato e il mix senza clipping; campionamento in `.verify/intro-studio-20261021/corale-final-check.jpg`. Verifica tecnica distinta dall'approvazione artistica.

Le nuove produzioni restano separate dall'intro installata. La bocciatura della direzione 02 è registrata nei suoi manifest; 01 e 03 richiedono il giudizio dell'autore sui filmati effettivi.

## D0936 — revisione dello Scontro corale

L'autore richiede correggere il braccio troppo lento e l'arciera storta, segnala numerose imperfezioni e richiede ricerca e uso effettivo di strumenti per montaggio e fluidità. La v1 non è approvata. Si lavora sulla prima direzione, senza rifare la Sigla illustrata.

### Conclusione della ricerca, prima della revisione

Il [time remapping documentato da Adobe](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-speed/different-ways-to-change-clip-speed-and-duration.html) distingue variazione di velocità e interpolazione temporale. La prima cambia il ritmo; la seconda ricostruisce fotogrammi. Un'interpolazione a 60 fps non ripara una posa anatomica sbagliata. Il gesto della prima scena è quindi rimappato lungo l'intera ripresa; la seconda scena è sostituita, non semplicemente interpolata di nuovo.

Sono stati studiati [VACE](https://github.com/ali-vilab/VACE/blob/main/UserGuide.md) per modifica video con maschere e riferimenti e [Wan Animate](https://github.com/Wan-Video/Wan2.2) per guida del movimento. Non sono dichiarati usati per la consegna: il materiale precedente dell'arciera contiene già un movimento sbagliato da non usare come guida, e aggiungere un nuovo sistema non garantisce di correggerlo. La soluzione scelta è una nuova posa iniziale e un solo gesto completo, evitando torsioni estreme e salti inventati dal modello piccolo.

La ricerca tramite Plugin Management ha trovato Runway e Higgsfield non installati; Adobe e Figma installati. Il tentativo di inizializzare Adobe ha restituito un errore interno. Runway è stato proposto per l'attivazione, non dichiarato collegato né usato. Non sono state avviate operazioni a pagamento. Le skill pertinenti lette sono Imagegen, Plugin Management, Adobe Edit Quick Cut, UE Animation e Sequencer/Cinematics e Spidah Projects. Non si dichiarano utilizzate skill estranee al problema solo per aumentarne il numero.

### Strumenti e trattamento effettivo

- Primo scambio: RIFE 4.6 produce un intermedio a 120 Hz dalla clip nativa; una curva monotona PCHIP rimappa il tempo con derivate continue, poi FFmpeg campiona a 60 Hz. L'intera sorgente di 5,0625 s diventa 2,9 s; velocità locale 1,12–2,15×, con più tempo relativo sul contatto. Nessun taglio dentro il gesto, nessuna posa saltata per mascherarlo. I fotogrammi possono naturalmente essere ricampionati nel retiming; non si afferma che ogni singolo fotogramma nativo compaia nella consegna.
- Arciera: keyframe nuovo generato con Imagegen usando l'identità di Deadeye e la scena corale come riferimenti, posa stabile e leggibile, arco intero, mani e spalle visibili. Il prompt integrale e quello di movimento sono in `art/intro/alternative-20261021/corale/v2/`. Il movimento richiesto è tensione completa → rilascio → recupero, senza il precedente salto e scambio di mischia.
- Nuovo modello locale: [Wan2.2 I2V 14B distillato LightX2V](https://huggingface.co/lightx2v/Wan2.2-Distill-Models), conversione [GGUF di jayn7](https://huggingface.co/jayn7/WAN2.2-I2V_A14B-DISTILL-LIGHTX2V-4STEP-GGUF), variante Q4_K_S del 12/4/2026, revisione `338fb8eedd8f485c9188cf1b1de541721fc81d66`. Due esperti high/low caricati sequenzialmente per non tenere entrambi in RAM. L'ambiente locale esistente è stato integrato con `gguf 0.19.0`, senza modificare il gioco. La licenza dichiarata dal convertitore segue quella Apache-2.0 di LightX2V/Wan; nessun servizio a pagamento.
- Campionamento: applicato il calendario di [WanStepDistillScheduler](https://github.com/ModelTC/LightX2V/blob/main/lightx2v/models/schedulers/wan/step_distill/scheduler.py) e la [configurazione 4090](https://github.com/ModelTC/LightX2V/blob/main/configs/distill/wan22/wan_moe_i2v_distill_4090.json): quattro passi `[1000,750,500,250]` prima dello shift 5, due per esperto, CFG disattivato. Il primo tentativo con il linspace predefinito di Diffusers non rispettava questo calendario: escluso dalla consegna, conservato in `.verify/intro-corale-v2-20261022/scheduler-linspace-attempt`. Non si confondono quattro passi generici e quattro passi del modello distillato.
- Suono: mix rimontato sulle nuove durate, Foley esistenti, passi su pietra e movimento del cuoio dai pacchetti già posseduti; voce e marchio esistenti. L'interpolazione è applicata separatamente alle scene, senza generare immagini spurie fra le due camere.

Script della revisione: `tools/refine-intro-corale.py`. La dimensione del modello, i 60 fps e la decodifica non equivalgono a qualità professionale accettata: il risultato va valutato sui corpi e sul movimento effettivi.

### Compositing e consegna della revisione

La nuova generazione risolve la torsione estrema della posa precedente, ma produce una freccia orientata male, troppo lenta e con frammenti separati. Il difetto non viene affidato all'interpolazione: OpenCV SIFT/RANSAC registra uno sfondo pulito della stessa ripresa e lo compone con maschere sfumate sui fotogrammi interessati. La piccola punta già presente nel fotogramma iniziale è rimossa dal clean plate con inpainting Telea. L'ambiente locale è integrato con `opencv-python-headless 5.0.0.93`; nessuna installazione nel progetto Unreal.

Una singola freccia fisica trasparente, creata con Imagegen e conservata con il prompt, viene composta dopo RIFE: punta verso destra, rilascio a 0,20 s della seconda scena, traiettoria a 2500 pixel nativi al secondo. Quattro campioni temporali sfumano solo il proiettile. La pulizia iniziale ha mostrato bordi neri e frammenti residui: corretti il bordo del clean plate e l'estensione delle maschere prima della consegna. Non vengono dichiarati usati VACE, Runway o Adobe per questi interventi locali.

Consegna: [ragequit-corale-v2.mp4](../../art/intro/alternative-20261021/corale/v2/ragequit-corale-v2.mp4), circa 10,52 s, con [provenienza e controlli](../../art/intro/alternative-20261021/corale/v2/provenance.json). Prima scena 2,9 s, seconda 3,3 s, logo e voce originali. Sorgenti native 832×480 e 1024×576; file finale ingrandito a 1920×1080, interpolato a 60 fps. Il filmato installato nel gioco resta quello precedente finché la proposta non viene accettata.

## D0938 — Scontro corale v2 bocciato: manca l'azione

La v2 e bocciata (D0939): la freccia parte nel nulla, non c'e un bersaglio leggibile o una conseguenza; ritmo lento e assenza di azione. Il paragrafo di consegna precedente descrive un file tecnicamente controllato, non un risultato accettato. La ricevuta della v2 ora riporta la bocciatura. Nessuna integrazione nel gioco.

Errore della revisione: retiming, interpolazione e pulizia del proiettile hanno trattato la resa del movimento senza risolvere il contenuto della scena. Queste operazioni non costituiscono una coreografia. La scena dell'arciera viene esclusa dalla nuova verifica; non si rimonta di nuovo lo stesso tiro aggiungendo velocita e suoni.

Fonti consultate in questa revisione: [Academy, Film Editing](https://www.oscars.org/sites/oscars/files/complet_film_editing_activities_guide.pdf), per relazione spaziale fra soggetti e costruzione del significato attraverso il montaggio; [Runway, Gen-4 Video Prompting](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide), per descrizione concreta del movimento, scene circoscritte e limiti di richieste troppo complesse. Questi principi informano la nuova verifica, non dimostrano che il filmato la superi e non vengono attribuiti al modello locale come garanzie.

Connessioni ricontrollate: Runway e Higgsfield non installati. Il collegamento Runway e gia stato suggerito due volte: nessuna nuova richiesta duplicata. Una richiesta effettiva al modello Kling tramite Figma/Weave restituisce account Figma non collegato a Weave; non e stata eseguita generazione esterna con questi servizi. Non sono stati sostenuti costi. La nuova prova locale deve mostrare un colpo fra due avversari visibili e una reazione fisica riconoscibile prima di qualsiasi montaggio, suono o logo; se questa azione manca, la prova resta esclusa dalla consegna.

D0940/D0941: l'autore contesta la successiva richiesta di collegare Runway perche a pagamento. Il passaggio e ritirato: non serve alcun account o abbonamento nuovo per continuare. Il tool Runway era nel frattempo comparso, ma la verifica di autenticazione ha restituito `USER_NOT_LOGGED_IN`; nessuna generazione, prova a pagamento, acquisto o attivazione di trial effettuata. Tutta la produzione successiva resta locale con risorse gratuite gia disponibili.

### Nuova proposta: duello con conseguenze visibili

File: [ragequit-duello.mp4](../../art/intro/duello-azione-20261022/ragequit-duello.mp4). La scena dell'arciera e esclusa. Due nuove inquadrature ravvicinate conservano guerriero a sinistra e mago a destra: colpo di scudo che sbilancia e fa cadere il mago; contrattacco dal terreno che fa cadere il guerriero. E una rappresentazione figurata dello scontro, non una registrazione di gameplay o una modifica ai kit delle classi.

Entrambi i keyframe sono creati con Imagegen; animazione locale con i due esperti Wan2.2 gia scaricati, stesso calendario LightX2V verificato sopra. Semi 1295 e 6614, 81 fotogrammi nativi per scena a 1024×576/24 fps. Prompt immagini, prompt movimento e ricevute sono conservati nella cartella della proposta. Prima verificate le conseguenze nei fotogrammi nativi, poi montate le scene. Il primo contrattacco e stato scartato dall'assistente per capriola al bordo e gesto con emissione vicino alla mano: prova rossa registrata, tentativo escluso conservato nella cartella di verifica. Il secondo mantiene il mago nella posizione bassa e semplifica la reazione del guerriero.

Ritmo: prima scena 2 s; seconda scena 1,1 s, dopo aver escluso l'attesa successiva alla caduta. Retiming uniforme 1,6875× e RIFE per singola ripresa, mai sullo stacco. Voce originale a 1,12 s sopra l'azione, titolo originale a 3,1 s, fine a 5,2 s. Diminuita l'attesa sul marchio rispetto alla v2. La chiusura usa una vera dissolvenza al nero, non una correzione della sola luminanza che lascia lo sfondo colorato. Foley rimontati su contatto iniziale, atterraggio del mago e del guerriero; nessun suono o proiettile della scena dell'arciera.

Script: `tools/build-intro-duel.py`, con riuso dell'inferenza di `tools/refine-intro-corale.py`. Sorgenti 1024×576; 1920×1080/60 fps ottenuti con retiming, interpolazione e ingrandimento. [Provenienza](../../art/intro/duello-azione-20261022/provenance.json) con hash, mix, formato e decodifica integrale. La revisione richiede ancora il giudizio dell'autore: azione presente e verifiche del file non certificano una qualita professionale accettata. Nessuna sostituzione dell'intro installata nel gioco, nessun costo.

### D0947-D0955: rifiuto del duello e generazione AI locale LTX

L'autore rifiuta il duello precedente: movimento percepito come un frame che scorre, azione e resa non adeguate. D0949/D0950 richiedono esplicitamente un video finto prodotto da un generatore AI; la successiva proposta di animazione manuale in Unreal e ritirata. Le proposte precedenti restano rifiutate, nessuna integrazione nel gioco.

La demo ufficiale [LTX-2.5](https://huggingface.co/spaces/Lightricks/LTX-2.5) e stata realmente interrogata: quota anonima ZeroGPU insufficiente, non un costo addebitato. Aprire la registrazione e chiedere l'accesso ha aggiunto un passaggio all'autore senza risolvere il video. Il tentativo online e escluso; nessun acquisto, abbonamento, trial o account creato.

Strada effettivamente eseguita: ComfyUI ufficiale in ambiente separato, modello [LTX-2.3 FP8](https://huggingface.co/Lightricks/LTX-2.3-fp8) pubblico, text encoder Gemma e LoRA/upscaler del [template ufficiale Comfy-Org](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_ltx2_3_t2v.json). RTX 4090 presente, server solo localhost con --offline. Manifest con revisioni e pesi in art/intro/ltx23-20261022/models.json. Software e modelli sono fuori dal gioco. Pesi soggetti alla licenza LTX Community, non dichiarati senza condizioni.

La generazione nativa completa di 121 fotogrammi a 24 fps, 1024x576 con audio, e riuscita: prima esecuzione 42,85 secondi, seconda 31,95 secondi. Questo dimostra che il blocco della demo online e superato sul PC, non che il filmato sia artisticamente riuscito. Primo risultato escluso per resa 3D antiquata e colonna davanti allo scontro; secondo escluso per sfondo da bozzetto e instabilita dell'arma. Per il terzo tentativo si applica la guida immagine ufficiale del template: riferimento nuovo Imagegen, prima fase forza 0.7, seconda 1, stessa ricetta di campionamento. I movimenti sono generati dal modello video, non da panoramiche o deformazioni scriptate dell'immagine. Le verifiche di qualita restano distinte dall'esito tecnico.

Ulteriori verifiche: quarto tentativo escluso per trasformazione del mago in un secondo guerriero; quinto escluso per calcio inventato e perdita della coerenza dell'arma. Riferimento corretto con elmo chiuso per il guerriero e vecchio mago con barba bianca e sola stoffa viola. La revisione della [guida ufficiale di prompt adherence](https://ltx.io/blog/how-to-improve-ltx-2-3-prompt-adherence) porta a una sola azione completa per clip breve e alla prova Dev, distinta dalla configurazione rapida distillata. Il [codice ufficiale TI2VidTwoStagesPipeline](https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-pipelines/src/ltx_pipelines/ti2vid_two_stages.py) usa guida nella prima fase e LoRA distillata nella seconda: adattamento Comfy con Dev senza LoRA nella prima fase, scheduler LTX 30 passi, DualCFG 3 video/7 audio, STG 1 sul blocco 29, guida immagine 1. Si tratta di un tentativo controllato, non di una garanzia di successo.

Problema operativo riscontrato: errore hostbuf_file_reader_read al ricaricamento dell'encoder; server proprio riavviato. Una generazione successiva rallenta prima del primo passo mentre sono attive due istanze Shipping di altre prove: non vengono fermate o modificate. Nuovo avvio proprio con --vram-headroom 3 --cache-ram 8 12; il campionamento torna ad avanzare. I log tecnici sono nella cartella .verify/intro-ltx23-local. Nessuna richiesta di interrompere altro lavoro all'autore.

La prova Dev a bassa risoluzione mantiene ancora movimenti non richiesti e armi incoerenti: esclusa. Successivo tentativo: generazione Dev direttamente a 960x544, 49 fotogrammi, senza passaggio a meta risoluzione, e adattatore [LiconStudio VBVR 390K](https://huggingface.co/LiconStudio/Ltx2.3-VBVR-lora-I2V) 0.75. Il modello e pubblico e non gated, licenza LTX Community; file 554.006.432 byte scaricato e SHA256 verificato. Le capacita dichiarate dal produttore su fisica e coerenza non equivalgono a un esito verificato per questa scena.

Alternative esterne verificate e non utilizzate: Fight LoRA V3 su CivitAI restituisce HTTP401 al download, nessuna richiesta di account all'autore e nessun tentativo di aggirare l'accesso. Il mirror HF riporta una licenza diversa dai permessi upstream, quindi non adottato come scorciatoia. [MiniMax H3: licenza ufficiale](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE) esclude l'Unione Europea senza autorizzazione separata: nessun download o utilizzo. LTX-2.5 e i componenti quantizzati controllati richiedono accettazione della licenza tramite account: non si ripete la richiesta di registrazione gia contestata. Queste sono verifiche concrete dei candidati, non un'affermazione che ogni alternativa gratuita al mondo sia impossibile.
