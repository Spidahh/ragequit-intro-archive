# RAGEQUIT — istruzioni correnti

## PRIMA DI TUTTO: un solo sistema per le direttive dell'autore — vale per OGNI AI

L'autore, il 6/10/2026: «il sistema che comanda le ai e immagazzina conoscenza sul progetto e direttiva deve essere uno
perfettamente fatto, non file separati che non riesci a far comunicare», «deve funzionare per tutte le ai».

Quel sistema è **`tools/direttive.py`** con l'archivio unico `DOCUMENTAZIONE/DIRETTIVE/direttive.jsonl`: ogni messaggio
dell'autore integrale, le regole che valgono, ciò che ha bocciato, i fatti da sapere. Qualunque AI tu sia (Claude, Codex,
ChatGPT, Gemini, altro):

| Se… | fai |
|---|---|
| puoi lanciare comandi sul PC | `python E:/PROGETTI/ragequit/tools/direttive.py prima <argomento> <parole chiave>` **prima** di proporre o toccare qualcosa (vedi la procedura qui sotto) |
| non puoi lanciare comandi | leggi il blocco «LE DIRETTIVE CHE VALGONO» qui sotto: è generato dall'archivio ed è completo |
| lavori dal dossier senza il PC | leggi `21-DIRETTIVE-AUTORE.md` nel dossier: stesso contenuto, generato |
| l'autore scrive qualcosa | salvalo SUBITO, parola per parola: `... parole "testo esatto"`; se non puoi lanciare comandi, riportalo in cima alla tua risposta di consegna perché lo salvi chi può |
| ne esce una regola o una bocciatura | `... regola --tema … --testo … --parole …` / `... bocciato …` (`--supera D0123` se ne sostituisce una), poi `... export` e commit su `main` di `direttive.jsonl`, `DIRETTIVE.html` e `AGENTS.md` |

Argomenti: metodo, documenti, menu, skill, classi, grafica, immagini, arene, combattimento, effetti, pacchetto, prove,
multiplayer, gioco. **Non si creano altri file di regole**: se un documento contraddice l'archivio, vale l'archivio.
L'archivio sta sulla copia principale `E:\PROGETTI\ragequit` (ramo `main` locale); un worktree può essere vecchio di
centinaia di commit e non fa testo.

## PRIMA DI OGNI LAVORO: tre passi, sempre, in quest'ordine

L'autore, 22/10: «la devi smettere di inventare cose o fare cose sbagliate non so più come dirtelo» (D1002). Quella mattina
un'intro video è stata fatta guardando solo regole e bocciature, non le sue richieste: personaggi inventati che non sono le
classi di RAGEQUIT, ore di GPU buttate (D0965). Non si salta nessun passo, per nessun lavoro.

1. **Le sue parole.** `python tools/direttive.py prima <argomento> <parole chiave>` (es. `prima immagini intro video`): in
   cima escono TUTTI i suoi messaggi su quella cosa che valgono ancora, dal primo (quelli che ha fatto cancellare non escono).
   Si leggono tutti; le bocciature dicono solo cosa non va. Le chiavi si scelgono larghe (`intro video filmato`).
2. **Il gioco vero e i giochi simili.** Ciò che si fa usa le cose di RAGEQUIT (le sue classi, le sue arene, il suo stile, il
   logo, la voce del narratore), mai personaggi, ambienti o stili inventati. Si guarda come lo fanno i giochi dello stesso
   genere (arena PvP con classi, camera dietro le spalle, mirino: D0612) e si arriva a una conclusione (D0489, D0394).
3. **La scheda, prima di produrre.** Per ciò che lui vede (immagini, video, suoni, menu, aspetto), prima di generare o
   cambiare qualcosa gli si scrive in poche righe: le sue frasi su quella cosa, cosa fanno i giochi simili, cosa si farà
   esattamente (D0393, D0489). Solo dopo si produce; la scheda si controlla di nuovo sul risultato prima di consegnarlo:
   ogni sua frase rispettata, niente di inventato.

## LE DIRETTIVE CHE VALGONO

<!-- DIRETTIVE:INIZIO (generato da tools/direttive.py export: non modificare a mano) -->

### Metodo
- Ogni suo messaggio si salva subito, parola per parola, in questo archivio (`direttive.py parole`). *(D0145)*
- Per aprire pagine web o servizi si usa il browser del PC su cui gira l'AI, non quello del dispositivo da cui l'autore è collegato. *(D0219)*
- Niente domande a cui si può rispondere da soli studiando il gioco, i file e i giochi simili. *(D0321)*
- Quando dice di fare si fa, fino in fondo, senza fermarsi: fatti, non testo. *(D0322)*
- Vale tutto quello che ha scritto nel tempo, non solo l'ultimo messaggio. I file del progetto si leggono ogni volta prima di lavorare e si rispettano. *(D0323)*
- Una cosa bocciata non si ripropone, nemmeno ritoccata: si ripensa, non si fa una piccola modifica. *(D0324)*
- Tutto gratis. *(D0327)*
- Le regole non si inventano. Un suo dubbio o una sua domanda non è una regola, e una regola non si ricava da un messaggio vecchio. *(D0330)*
- Una modifica chiesta per un momento e una cosa che non gli è piaciuta riguardano quella cosa, quella volta: non sono divieti assoluti e non diventano regole generali. *(D0361)*
- Quando la scelta è una cosa che lui vede (aspetto, menu, classi), prima gli si dice in breve la soluzione. Alle sue domande si risponde, a tutte, in modo che capisca. *(D0393)*
- Si parte da ciò che funziona nei giochi simili, con dati, matematica e standard; non da invenzioni proprie e non da giudizi a occhio. *(D0394)*
- Gli esempi e le immagini dati all'inizio servivano a far capire il gioco: non sono riferimenti adesso che il gioco è maturato. Una cosa vecchia va riletta alla luce di com'è il gioco oggi; questo si capisce da soli, senza che lo dica lui. *(D0402)*
- Le cose nuove si caricano sempre su GitHub: dopo ogni commit su main (tools/publish-github.py, parte da solo). *(D0482)*
- Prima di modificare una cosa si studia come la fanno i giochi simili. Lo studio arriva a una conclusione e la conclusione gli si espone. *(D0489)*
- Si fa quello che chiede, fino in fondo. Quando dice di migliorare il gioco in autonomia si lavora senza fermarsi, ma non con scelte a caso: ogni cosa che si vede prima si studia sui giochi simili e gli si mostra (D0489, D0393). *(D0493)*
- Tutto si fa sempre al massimo e per bene: ricco, dettagliato, preciso, curato. Mai cose semplici, base, dozzinali o abbozzate, nemmeno come prima proposta. Nella grafica: sfumature, luce, materia, colori particolari, dettagli. *(D0511)*
- 8/10: finito quello che ha chiesto non ci si ferma: si continua a provare il gioco, cercare e capire gli errori fatti, correggerli, e ad abilitare e far funzionare ogni elemento. *(D0571)*
- Ogni pagina e schermata si progetta sul gioco completo: gli elementi di un gioco arena PvP action con personaggi (account con livello, profilo e statistiche, classificate con gradi e stagioni, classifica, amici e gruppo, chat, negozio e valuta, pass e sblocchi, cosmetici, missioni, ricerca partita, partite private, spettatore e replay, tornei, lingua e accessibilita', segnalazioni) hanno il loro posto nella grafica e nel progetto anche se non sono ancora fatti (parole dell'8/10: D0525, D0527). L'elenco lo si ricava dal genere, ma un elemento dell'elenco non si mette in una schermata solo perche' e' nell'elenco: il 9/10 ha fatto togliere il riquadro NEWS dalla HOME («non mi serve e non l'ho mai chiesto»); le notizie non sono nell'elenco. *(D0593)*
- Si fa tutto. Nessun messaggio di consegna con un elenco di cose «non fatte»: ciò che resta (difetti visti, cose mai controllate, cose di aspetto) si fa prima di scrivere, e gli si mostra il risultato. *(D0632)*
- Codex non contatta Claude senza il permesso esplicito dell'autore. Le proposte di Codex devono essere prima approvate dall'autore prima di essere passate a Claude. *(D0723)*
- Tutte le modifiche si fanno solo con la skin principale: le skin secondarie non si guardano e non ci si perde tempo. Vale per tutta l'ARMORY: e' una cosa in piu' e aspetta la fine di tutto. *(D0767)*
- Si migliora il gioco come uno sviluppatore vero, di propria iniziativa: renderlo sempre un gioco migliore nei dettagli, nelle cose principali e nelle idee, non solo eseguire le richieste. Non solo le animazioni: come si lanciano le abilità e come si vedono, gli effetti a schermo, le regole e le meccaniche, il divertimento, la sfida, il feeling di gioco, le comodità (QoL); sempre pensando a un FPS con abilità, action 3D. Resta D0493: ciò che si vede si studia prima sui giochi simili e gli si mostra. *(D0857)*
- Ogni volta che chiede qualcosa (un lavoro da fare, una domanda, un compito) non si è approssimativi e non ci si sbriga. Prima si capisce quali asset servono per tutto e si trovano i migliori gratuiti; una volta ottenuti ci si costruisce sopra. Niente cose provvisorie che poi restano fisse. Quando si fa una cosa gli si dice: attenzione, mancano queste cose. Vale per tutto quello che si fa, non solo per il gioco. *(D0874)*
- Il gioco si aggiorna a strati: prima si migliorano le cose principali, poi quelle minori. *(D0875)*
- I suoi accessi ai servizi (Fab, Epic e gli altri) si salvano e restano fissi: non deve rifare l'accesso ogni volta. Il browser con il suo accesso non si chiude e non si azzera. *(D0885)*
- Prima si finisce il gioco vero e proprio: personaggi (come si vedono e si muovono), abilità, effetti, tutta la grafica e l'audio, e si toglie ciò che è inutile e vecchio. Le arene si fanno dopo: sono elementi esterni. *(D0895)*
- Non si rifanno le cose già provate che funzionano e sono belle: si lavora su ciò che manca o è fatto male. *(D0896)*
- Prima di fare cose nuove si correggono le vecchie: si butta tutto il vecchio (piani, voci, documenti, codice, dati e asset superati) e si bonifica, così vecchio e nuovo non si mescolano e tutto è a posto. *(D0903)*
- Prima di fare una cosa, compreso pianificare e organizzare il lavoro di un gioco, si cercano skill, plugin, sistemi, siti e servizi gia' pronti che la fanno, e si usano; non si parte da zero e non si improvvisa. Detto piu' volte: D0001, D0630, D0655, D0656, D0740, D0840, D0914. *(D0915)*
- Le decisioni del lavoro le prende l'assistente: design, regole, asset, ordine (quello del piano su tutto il gioco, PIANO-COMPLETO.md §6). Non si fanno all'autore liste di domande o di scelte: si decide studiando i giochi simili e si mostra il risultato. Si può usare qualsiasi cosa sia sul PC, comprese le animazioni già presenti per le mosse che mancano (non vuol dire rifare i corpi, D0901). *(D0921)*
- Non si inventa niente e non si fanno cose sbagliate: ogni lavoro parte dalle sue parole su quella cosa (le sue richieste nell'archivio, anche le prime) e dalle cose vere del gioco (classi, arene, stile). Quello che manca si cerca, non si riempie con idee proprie. *(D1002)*
- Le soluzioni per il gioco si prendono dal codice e dai dati dei giochi fatti bene (il codice di Epic: Lyra, il Game Animation Sample, la logica originale degli eroi Paragon; ricerche e documenti tecnici che spiegano come si fa un gioco), non dal giudizio a occhio dell'assistente su foto e immagini: l'assistente non vede come un giocatore e non confronta i giochi guardando le immagini. *(D1117)*
- Metodo di lavoro su tutto il gioco: si legge il codice dei giochi fatti bene, si trova dove il codice di RAGEQUIT fa diverso, si cambia il codice e si controlla la logica leggendo il codice. Niente verifiche visive (foto, confronti di immagini) e niente giri di prove per ogni modifica: al massimo una prova automatica del pacchetto prima di pubblicarlo. Non si sprecano tempo e crediti. *(D1123)*

### Documenti
- Un solo sistema, fatto bene, comanda le AI e conserva direttive e conoscenza del progetto. Deve funzionare per tutte le AI. Niente file di regole separati. *(D0331)*
- Tutto deve avere un senso e uno scopo. Le cose inutili, i documenti vecchi e le regole vecchie si cancellano: niente cartelle, file e versioni che non si sa se servono. *(D0332)*

### Menu
- Vuole che gli elementi siano amalgamati fra loro (ombre, luce, effetti) e che non si notino stacchi, come se fossero appiccicati uno sopra l'altro. I bordi attorno alle figure si possono mettere, fatti bene. *(D0363)*
- Gli elementi dello stesso tipo devono essere coerenti fra loro: allineati e con misure simili, non ognuno messo a caso con una dimensione diversa. Non vuol dire tutto uguale. Vale per ogni elemento del gioco. *(D0391)*
- Vuole menu moderni e fighi, quasi anime, hardcore: font freschi, bei colori, sfondi e immagini fighe, tutto in stile Ragequit. La scelta delle classi con un simbolo e una spiegazione per ogni classe. *(D0398)*
- I testi in generale un po' piu' piccoli, senza esagerare: gli elementi devono respirare e non sembrare attaccati fra loro, con piu' ordine e piu' spazio per le informazioni. Ma non rimpicciolire troppo: non passare all'eccesso opposto. *(D0590)*
- Dopo l'analisi dei menu, Codex mostra nella chat le immagini delle modifiche proposte, senza aspettare che l'autore debba richiederle di nuovo. *(D0730)*
- D0771: autore approva la proposta completa menu-progetto-funzioni-20261013 alla revisione card-finish e autorizza Codex a integrarla realmente nel gioco e renderla il riferimento definitivo condiviso da tutte le AI. Per i menu questa versione sostituisce la vecchia struttura Lama: HOME con illustrazione Ragequit e classe/gruppo; PLAY proprietario della configurazione; CLASSES con roster in basso 5x2; gerarchia PLAY/CLASSES separata da CAREER/ARMORY/STORE e finitura condivisa delle 30 schermate. Lo stile HUD di D0523 resta distinto. I valori illustrativi della proposta non sostituiscono dati del gioco, kit o sblocchi. Fonte accettata e impronte conservate nella voce del registro ELEMENTI menu-card-finish-20261013. Restano D0767 (solo skin principale, Armory dedicata alla fine), D0769 (icone delle spell a cura dell autore) e D0723 (nessun contatto con Claude senza permesso esplicito). *(D0776)*

### Skill
- Nel menu le abilità di ogni personaggio si spiegano: simboli più un testo chiaro, semplice, facile da tradurre, che faccia capire cosa fa l'abilità. *(D0342)*

### Classi
- Nel roster devono esserci, distribuite fra le classi: un'arma che spara come un arco, diverse armi da mischia, magie, blocco, cura, salto e presa al volo con un colpo istantaneo, muri, prese (grab), stun, freeze, lock, invisibilità, accecamenti, root, magie a palombella (tipo Magma Storm di Darkfall), colpi caricati, rampini, teletrasporti, balzi, parate. *(D0261)*
- Le classi devono essere diverse fra loro, non tutte uguali con gli stessi colpi, e ognuna ha un modo per uscire dallo scontro (escape). Kit spettacolari: esplosioni, sbalzi, freeze, stun, attacchi speciali. Si copiano le belle idee dei kit di tutti i giochi action PvP con abilità, non solo SMITE; non si mischiano kit che non si conoscono. *(D0344)*
- Le classi possono essere più di dieci: quelle in più si tengono per il futuro. *(D0345)*
- I modelli dei personaggi possono venire da qualsiasi fonte che vada bene per il gioco, non solo Paragon: gratuiti e con una grafica simile fra loro. Un modello si sceglie se combacia col personaggio e con la sua arma. *(D0400)*
- Rampino del Reaper sul muro, invisibilita' del Reaper per un attimo dopo Shadow Slip e nemico trascinato nella carica (Juggernaut, Impaler): il si' dell'autore c'e', si fanno. La palombella no. *(D0451)*
- Ogni classe si difende in un modo suo, diverso dalle altre. I maghi non parano: schivano, si teletrasportano e simili. C'e' la classe che non schiva ma para. Le altre hanno altri tipi di meccaniche. Non si da' la stessa difesa a tutte le classi e non gli si chiede se i maghi parano. *(D0675)*
- Se si lavora sulle classi, le classi devono essere complete prima di implementarle: nel design e in tutto. Prima si scrive (o si aggiorna) il sistema delle classi presenti: come sono, come migliorarle e gli elementi del gioco da usare. Per ogni corpo (per esempio un modello senza arma usato come mago) prima si sa quali magie e abilita' deve usare, poi si controlla che abbia animazioni decenti per farle. Ogni AI che tocca le classi deve conoscere quel disegno. *(D0775)*
- Per ogni classe si cerca il modello giusto fra tutti quelli che ci sono, e si può cambiare: tutti gli scambi di modello che servono. Un'abilità si può adattare al modello solo quando è logico (se il modello ha la scivolata, la sua abilità è la scivolata), purché resti in linea con la classe. *(D0779)*
- La difesa dei maghi (gli scatti e i teletrasporti dei quattro maghi: Backdraft, Phase Step, Ice Glide, Stone Step) consuma solo stamina, senza cooldown, come la parata. Il tasto destro della Deadeye è la freccia che inchioda (radica chi colpisce). *(D0837)*
- Nessuna classe ha un attacco base a mitragliatrice: vale per tutte, non solo per l'arciere; ogni attacco base a distanza va calibrato perché i melee riescano ad avvicinarsi. Le frecce dell'arciere partono solo tese del tutto, tutte, anche quelle delle abilità: il tasto sinistro si tiene premuto e, se la tensione non è completa, non parte nessuna freccia. Il tasto destro fa un'altra cosa. *(D0852)*

### Grafica
- Il gioco deve sembrare molto meno AI: via le immagini in stile AI, con sfondi super colorati e strani. Le cose fatte male si sostituiscono tutte. *(D0348)*
- La grafica deve essere una sola, uguale in tutto il gioco, e la decide lui. *(D0365)*
- Stile unico dell'interfaccia: la proposta «Lama» (FOTO-08-10/LAMA-menu.png, LAMA-partita.png): taglio diagonale, lista di parole grandi oblique con la scelta su una lama rossa, simboli delle classi nei rombi (non foto dei modelli), sfondo dei menu = l'immagine dell'arena gotica in fiamme data dall'autore; in partita punteggio su lame col tempo nel rombo, vita a lama col numero grande, tasti a parallelogramma. *(D0523)*
- Niente figure, linee o immagini disegnate o generate dall'AI con script al posto delle figure vere: dove serve una figura ci va quella vera (personaggio, arena) o niente. *(D0557)*
- I pacchetti del negozio Fab si usano tutti quando servono al gioco, anche quelli che non ha ancora. Nessun pacchetto si blocca o si esclude perche' in un altro momento non serviva, e su quali usare non si aggiungono regole. (Quelli gia' presi sono sul PC in C:\ProgramData\Epic\EpicGamesLauncher\VaultCache, elenco in VaultCache\FabLibrary; gli eroi Paragon gia' nel progetto hanno voci, reazioni, morti ed effetti propri.) *(D0623)*
- Tutti gli elementi grafici da generare si chiedono a Codex: Claude non li genera e non li scarica, scrive a Codex cosa serve. *(D0787)*

### Immagini
- Gli asset e le scelte di aspetto nuove glieli si fa vedere: non si danno per buoni senza che li abbia visti. *(D0396)*
- Le figure dei personaggi nelle schermate sono le carte della tavola «THE TEN CLASSES» dell'8/10 (FOTO-08-10/SCHERMATE/00-i-dieci-eroi-trovati.png): render ufficiali degli eroi dalla wiki di Predecessor dentro la carta dello stile Lama. L'autore le ha accettate («vanno bene, lascia»). Nota: quei render sono di Omeda Studios, non fanno parte dei pacchetti Paragon regalati da Epic: rischio di licenza da ricordare prima di pubblicare. *(D0545)*

### Arene
- Arena: grossa e complessa, con spazio per combattere, piani veri (non una scala con un terrazzino), barriere vere, livelli, oggetti e power-up. *(D0350)*

### Combattimento
- Chi ha la parata deve avere la stamina, e parando riceve comunque un po' di danno. *(D0601)*
- La parata è un'abilità che consuma stamina: niente cooldown, si può usare sempre e la limita solo la stamina che finisce (resta D0601: parando si prende comunque un po' di danno). *(D0832)*
- RAGEQUIT è un FPS con la mira: nessun sistema mira, corregge la mira o sceglie il bersaglio al posto del giocatore (aggancio, mira assistita, colpi che inseguono, correzioni automatiche verso il nemico) e nessun sistema che con un gioco di mira non c'entra. *(D0863)*

### Effetti
- Niente effetti grafici vicino alle mani dei personaggi quando lanciano qualcosa: vanno tolti tutti, non hanno senso. (Gia' chiesto piu' volte: D0384 del 4/10.) *(D0600)*

### Prove
- 8/10: le prove si fanno alla fine, quando tutto e' finito (non in mezzo al lavoro); alla fine vanno fatte tutte e deve risultare tutto a posto. *(D0568)*
- Ogni prova fatta si segna (che cosa controlla, su quali file, esito, rapporto) in un registro che vale per tutte le sessioni e tutte le AI; una prova già fatta non si ripete finché non cambia qualcosa di ciò che controlla. *(D0905)*

### Multiplayer
- Nel gioco ci sono sia la LAN sia Internet: HOST LAN / JOIN LAN restano nel menu PLAY, non si tolgono. *(D0420)*
- Su Internet si gioca collegandosi a un server: nessun giocatore ospita la partita. La LAN resta (vedi D0420). *(D0478)*
- Ordine dei lavori (8/10): prima si finiscono tutte le schermate rimaste e si fanno funzionare tutti i sistemi; l'online e' l'ultima cosa. *(D0549)*

### Gioco
- Tutto il gioco in inglese. *(D0356)*
- Il gioco ha una copia sola: le prove non si fanno sdoppiandolo. *(D0357)*
- Deve sembrare un gioco normale e professionale, finito e completo, con impostazioni standard. *(D0358)*
- Un gioco PvP con classi e skill. Le sottoclassi non esistono: non si mettono nelle schermate. I bot non sono una priorità: nel gioco non serviranno. *(D0533)*
- Impostazioni da gioco competitivo: niente effetti che i giocatori seri disattivano (scossa della camera, sfocatura di movimento, profondità di campo, aberrazione cromatica, grana, riflessi della lente); i valori di partenza sono quelli pro. *(D0811)*
- Che gioco e' RAGEQUIT: un'arena PvP 3D action quasi FPS (camera dietro le spalle, mirino al centro, tutto mirato a mano) con classi e abilita': combattono con armi bianche (ascia, scudo, lancia, falce, spade, clave), arco e magie, MAI con pistole o armi da fuoco. I paragoni si fanno solo con giochi di questo genere; mai con sparatutto con le pistole (Quake, Unreal Tournament, Overwatch), MMO (Darkfall) o giochi visti dall'alto (Battlerite). *(D1014)*

### Critiche e richieste di un momento
Riguardano quella cosa, quella volta. **Non sono divieti generali.** Servono a non rifare lo stesso errore sulla stessa cosa.
- [menu] Schermata classi ritoccata a piccoli passi (sfondo scuro vuoto, poi foto dell'arena e palco, poi roster a icone piatte): «sempre uguale», «spoglia». *(D0200)*
- [classi] I kit attuali di Impaler, Tempestblade, Warmaster, Juggernaut, Stoneguard e Sentinel (scheda del dossier 20 §11-12, nei dati del gioco dal 6/10): senza escape, tutti uguali, fanno tutti le stesse cose. Bocciati anche gli studi che li hanno prodotti. *(D0244)*
- [menu] Schermata delle classi del 7/10 mattina (SCHERMATA-CLASSI-nel-gioco.png): stemmi con uno sfondo enorme sopra le figure dei personaggi nelle caselle; pannello delle abilità compresso, con tutto schiacciato dentro; figure appiccicate sulla scena senza amalgama. *(D0303)*
- [menu] PROPOSTA-classi-07-10.png (7/10 mattina): caselle alte e strette con le figure tagliate, pannello piatto a tutta altezza, figura con nebbia ai piedi. *(D0305)*
- [skill, menu] Modi già provati e bocciati per spiegare le abilità: sigle; frasi scritte male; targhette di parole-chiave; disegni dall'alto messi senza chiedere; tabella di frasi e numeri; soli simboli senza testo; i simboli del kit (cono, linea, bersaglio, orologio, scoppio); filmati; disegnini e icone brutte accanto alle skill; un elenco di opzioni fra cui farlo scegliere. Il modo giusto si trova con una ricerca su come fanno i giochi. *(D0343)*
- [menu] 6/10, scelta classi: sotto i nomi erano state messe etichette (HUNTER e simili) che non aveva chiesto; poi tolte senza mettere altro. *(D0367)*
- [metodo] 3-4/10: finito un lavoro, ha chiesto di cercare problemi simili e di trovare sistemi migliori per ridurre gli errori. *(D0368)*
- [metodo] 5/10: mentre un'altra AI organizzava le classi, ha chiesto di continuare sul resto senza disturbarla. *(D0369)*
- [metodo, gioco] 6/10: non voleva che il gioco fosse riportato a com'era quella mattina. *(D0370)*
- [menu] 29/09, provando i menu di quel giorno: sembravano zoomati, con cose enormi, scritte che non entravano, elementi rotti, messi male e non allineati. *(D0371)*
- [menu] 26/09: non gli è piaciuta l'anteprima del personaggio che era stata messa nel menu principale. *(D0372)*
- [menu] 6/10, scelta classi: un modello al centro dello schermo che usciva dal nulla, senza sfondo e senza cornice; anteprime tagliate male e un po' sgranate; proporzioni di elementi, testi, immagini e tasti da aggiustare. *(D0373)*
- [menu] 5/10: i menu erano «bruttini», con una fila di tasti inutile; ha ricordato di pensarli per tutte le classi. *(D0374)*
- [menu, classi] 6/10: nelle caselle delle classi erano state tolte le icone e messe le facce dei modelli, senza che lo chiedesse. 29/09: nella schermata c'erano due Reaver, due Binder: ha chiesto di toglierli. *(D0375)*
- [menu] 5/10, scelta classi: dati scritti che non servivano e «passive» che non si capiva cosa fossero. *(D0376)*
- [menu] 29/09: nel menu iniziale si sentivano gli uccellini. *(D0377)*
- [classi] 6/10 notte, scelta dei corpi: skin scelte per colore; i pugnali della skin lasciati insieme al falcetto; la falce data a un corpo con pose per due lame. 7/10: ha chiesto di controllare le animazioni per le abilità nuove (un corpo non recolor è meglio, non obbligatorio). *(D0378)*
- [grafica] 29/09: i corpi sembravano fatti male, con le gambe per i fatti loro, e non coincidevano con le immagini dei menu. *(D0379)*
- [grafica] 16/08: non gli piaceva l'effetto retrogaming, e le immagini fatte tutte con la stessa tecnica, lo stesso sfumato e gli stessi colori. *(D0380)*
- [immagini] 5/10: ha chiesto di generare le immagini mancanti o provvisorie e di aggiornare l'enciclopedia degli asset. *(D0381)*
- [combattimento] 30/09: non si capiva niente quando ti tiravano le spell. *(D0382)*
- [combattimento, prove] 3/10: ha detto di non fare prove sulla durata dei combattimenti, che le faceva lui. *(D0383)*
- [effetti] 4/10: un effetto grigio enorme usciva dalle mani di chi lanciava. *(D0384)*
- [menu] Il pulsante TRY IT nella pagina CLASSES: tolto, resta solo LOCK IN. *(D0409)*
- [prove, multiplayer] 6/10 sera: ha chiesto di non fare prove in quel momento perché gli serviva il gioco libero, e ha detto che per il momento il gioco online si poteva anche interrompere mentre cambiava e finiva il gioco. *(D0411)*
- [classi] La palombella per Ember Field del Pyromancer: non si fa. Ember Field resta com'e' nel gioco. *(D0441)*
- [grafica] 8/10, HUD: la vita del giocatore in basso a sinistra (va sopra le icone delle abilita', al centro) e le due barre in alto nel duello come in un picchiaduro (Tekken): non e' un fight game. *(D0467)*
- [menu, grafica] 8/10, interfaccia (UI/UX) del gioco: troppo semplice e brutta, fatta senza uno studio. *(D0490)*
- [metodo, gioco] 8/10: il gioco e' pieno di errori da principiante; ha chiesto un metodo per trovare tutti gli errori fatti e sistemarli, ragionando da sviluppatore esperto. *(D0494)*
- [menu] 8/10, proposte di stile: le foto dei modelli 3D usate come immagini nei menu (brutte). Vuole ritratti o al massimo simboli. Delle tre proposte la prima (Lama) e' la migliore; come sfondo ha dato lui un'immagine (arena gotica in fiamme). *(D0521)*
- [menu] 8/10, schermata VERSUS del caricamento: al posto dell'avversario (NORMAL BOT) c'era un rombo disegnato con delle linee invece della figura vera del personaggio. Niente forme disegnate al posto delle figure. *(D0555)*
- [prove] 8/10 pomeriggio: con le schermate finite e fotografate, due ore di prove del cancello prima del pacchetto: le ha fatte fermare. Pacchetto fatto direttamente (tools/package-unreal.ps1 -Shipping) sul commit 3014a965. *(D0565)*
- [metodo, prove] 9/10, 01:05, andando a dormire: l'assistente va avanti da solo con tutte le tappe, senza fermarsi; il riesame di tutto in cerca di problemi si fa alla fine, non a meta'. *(D0582)*
- [menu] HOME del 9/10 mattina: il riquadro NEWS (non gli serve e non l'ha mai chiesto: tolto); i riquadri PARTY, SEASON PASS e DAILY MISSIONS in colonna sul lato destro e il simbolo della classe enorme riempivano il centro dello schermo: i riquadri vanno sulla riga in basso, che era libera (o sul lato), e il centro deve respirare. *(D0592)*
- [combattimento] 9/10 sera, dopo aver provato il pacchetto delle 16:52: molti colpi non colpiscono, o non fanno danno, o ne fanno poco; il combattimento e' troppo arcade e poco profondo. Ha chiesto di studiare questi problemi e il perche', e di capire gli errori di base per non rifarli. La falce data al personaggio (Reaper) non si muove ed e' in una posizione storta. *(D0602)*
- [combattimento, metodo] 9/10 sera: per togliere l'effetto arcade avevo proposto e stavo per fare quattro cose scelte da me (stamina per tutte le classi, passo avanti nei colpi da mischia, colpi leggeri che non interrompono, colpi pesanti piu' lenti) senza aver studiato come fanno i giochi simili: strategie a caso. Ha chiesto di studiare e capire, cercando dagli altri giochi simili. *(D0608)*
- [combattimento, metodo] 9/10 notte: lo studio del combattimento (DOCUMENTAZIONE/STUDI/COMBATTIMENTO-GIOCHI-SIMILI.html) metteva come parente piu' stretto Battlerite, un gioco visto dall'alto, e scartava i giochi in prima persona: genere sbagliato. RAGEQUIT e' un 3D action quasi FPS (mirino al centro, camera dietro le spalle): si guardano i giochi di quel genere. *(D0612)*
- [combattimento] 10/10 notte: lo studio rifatto sui giochi col mirino (D0613) portava solo numeri (quanto toglie un colpo, tempi, velocita'). Non e' quello che chiede: vuole una soluzione al combattimento, non ai soli numeri. Quello che va capito da quei giochi e' il feeling: cosa succede quando parte il colpo, quando va a vuoto e quando colpisce l'avversario. Oggi non succede niente. *(D0615)*
- [metodo] 10/10, 01:10 circa, andando a dormire dopo aver dato il via al lavoro sul colpo: continuare tutta la notte senza fermarsi e senza chiedere autorizzazioni, con pieno potere di decidere; finite le migliorie del colpo cercare altri problemi simili e continuare a migliorare il gioco, ogni cosa perfetta; migliorare la sua richiesta ed eseguirla; fermarsi solo quando riscrive lui. (Richiesta di quella notte, non una regola generale.) *(D0620)*
- [classi, grafica, prove] 12/10: autore rifiuta come risolti i corpi e le gambe della Shipping D0655. Riaprire la verifica dei modelli visibili e delle animazioni; i precedenti controlli automatici non equivalgono ad accettazione. *(D0661)*
- [combattimento, classi, metodo] 13/10: l'assistente aveva proposto la guardia tenuta per tutte le classi (presa da Darkfall: para chiunque) e chiesto se anche i maghi dovessero parare. Sbagliato: i maghi schivano o si teletrasportano, ogni classe ha la sua difesa (regola del 13/10). *(D0676)*
- [metodo, gioco] 13/10: dopo l'analisi esterna e le soluzioni proposte: l'assistente guarda sempre e solo la grafica; il gioco non e' fatto solo di grafica e ha moltissimi altri problemi. Ha chiesto di correggere tutti i problemi trovati e di trovarne e correggerne altri. *(D0677)*
- [combattimento, classi, metodo] 13/10: nell'analisi e nelle soluzioni l'assistente ha usato Darkfall come motivo per decidere le regole di RAGEQUIT (niente schivata «perche' in Darkfall non c'e'», guardia per tutti, tre barre). Darkfall e' un altro gioco: RAGEQUIT e' un'arena con classi e abilita'. L'autore aveva nominato Darkfall una sola volta, per l'esempio di una magia (D0261). Lo studio che lo mette come «famiglia» del gioco (D0613) e' di un'AI, non una sua regola: una regola del gioco non si ricava da quel paragone. *(D0681)*
- [grafica, arene, classi, metodo] 13/10, colori di personaggi e arena: (1) nelle foto di prova i modelli schiariti erano troppo chiari e luminosi rispetto alla mappa; (2) da quella critica avevo dedotto io «non tocco i personaggi, lavoro solo sull'arena»: deduzione mia, sbagliata e rifiutata. Si fa tutto cio' che serve, personaggi compresi, finche' personaggi e mappa stanno bene insieme; (3) sette giri di foto di prova di fila invece di mettere la correzione nel gioco: basta prove a caso, si corregge nel gioco e si verifica li'. *(D0706)*
- [menu, metodo, prove] 13/10 pomeriggio: (1) le proposte di Codex per i menu (mockup HOME e piano di rifinitura in .verify/codex-menu-*): bocciate, non si implementano; (2) mentre girava il cancello completo sul commit 26a0f323 (le stesse prove gia' passate nella giornata, rifatte da capo): niente prove tutte uguali a ripetizione; cancello fermato alla tredicesima tappa verde e pacchetto fatto direttamente (tools/package-unreal.ps1 -Shipping), come l'8/10 (D0565). *(D0715)*
- [menu, metodo] 13/10, proposte menu di Codex: l'autore ha chiesto di migliorare i separatori, non di eliminarli. Ritirata l'indicazione del piano di sostituire separatori e bordi interni con solo spazio/allineamento; la critica non costituisce un divieto generale di bordi. *(D0724)*
- [menu, metodo] 13/10, autore respinge le scelte precedenti di Codex per questi menu e tutta la serie di 13 proposte .verify/menu-proposte-riesame-20261013: ancora troppo simili al menu esistente, con selezione classi di nuovo in una colonna a sinistra. Il prompt di Codex imponeva esplicitamente quella colonna: era una scelta dell'assistente, contraria alla correzione dichiarata. Ritirati la serie e i suoi consigli; non sono direttive dell'autore e non sono da implementare. Le parole dell'autore rimangono distinte dalle scelte di Codex. *(D0745)*
- [menu] Il messaggio D0746 respinge la proposta classi piatta di Codex in .verify/menu-proposta-classi-struttura-20261013: la precedente resa grafica era considerata piu bella. Questo confronto non approva la vecchia serie e non autorizza modifiche al gioco. D0747 richiede una proposta per ogni pagina. *(D0748)*
- [menu, grafica] Nella serie di 30 proposte menu del 13/10 lo sfondo e troppo acceso e arancione, con una resa generica AI. La critica riguarda la resa mostrata e non costituisce un divieto generale di ogni fuoco, calore o colore arancione. *(D0752)*
- [menu, grafica] Nelle proposte menu mostrate manca il gioco di livelli chiesto: superfici piatte, con peso e trattamento troppo simili. La correzione deve mostrare profondita e gerarchia fra sfondo, contenitori e azioni, oltre alla correzione dei colori. Questo testo descrive la critica specifica, non approva una nuova soluzione. *(D0753)*
- [menu, metodo] Nella proposta menu-proposte-livelli del 13/10 la numerazione vicino a PLAY non ha uno scopo; CLASSES e ARMORY hanno peso troppo simile, e gruppo, pass e missioni sono tre rettangoli equivalenti pur avendo funzioni diverse. La richiesta D0754 e di ristudiare tutta la struttura e preparare un progetto, non solo cambiare colori o cornici. Questa e una critica alla proposta mostrata: non approva una nuova disposizione e non autorizza contatti con Claude. *(D0755)*
- [menu] D0756: autore dice vabene alla proposta menu-progetto-funzioni e limita il lavoro a due correzioni. HOME: troppi testi e azioni in colonna, classe e PLAY da riordinare con il gruppo separato. PLAY: testo delle mappe vicino ai bordi e impostazioni di partita mescolate, comprese le azioni per ospitare; raggrupparle per funzione. Il resto della proposta si conserva. Questo messaggio autorizza queste correzioni della proposta, non il contatto con Claude. *(D0757)*
- [menu] D0758: nella revisione della HOME di menu-progetto-funzioni, mostrare mappa e modalita non ha senso dato che si scelgono nella pagina PLAY. Autore chiede contenuti logici e collegamenti coerenti fra le pagine. Correggere questa duplicazione e il percorso della proposta; non e una richiesta di cambiare le altre schermate o di contattare Claude. *(D0759)*
- [menu, grafica, immagini] D0760: la HOME di menu-progetto-funzioni e troppo vuota. Lo sfondo richiesto e una immagine di RAGEQUIT: non una mappa o una cattura in-game, e non con la resa AI troppo accesa della precedente proposta. Correggere presenza visiva e sfondo della HOME; questa critica non approva il nuovo artwork e non autorizza contatti con Claude. *(D0761)*
- [metodo, menu, classi] 13/10 notte (23:39), mandato per questa notte, riscritto: (1) Claude si coordina con Codex, che sta rifacendo i menu, e i menu si aggiustano insieme a lui: i menu devono seguire le classi e i corpi nuovi. (2) Si procede senza fermarsi finche' non e' finito tutto, senza chiedere pareri: decide Claude, seguendo gli insegnamenti dell'autore gia' in archivio. (3) Da fare: le classi con i personaggi nuovi (corpi, abilita', animazioni), il controllo e il debug di tutto, i menu con Codex, e tutto il resto che era rimasto da fare. (4) Solo le prove essenziali. Resta dal messaggio della sera (ex D0769): le icone delle abilita' le fa fare l'autore, nessuna AI ci lavora o le propone. E' la richiesta di questa notte, non una regola generale. *(D0784)*
- [prove] 15/10 notte: per misurare tre stanze online avevo lanciato dieci copie del gioco insieme sul suo PC e il PC si è bloccato. Niente prove con tante copie: le prove grandi online le fa lui con i suoi amici. *(D0800)*
- [grafica] 15/10: dietro tutte le pagine del menu tranne la HOME (PLAY, ROOMS, FRIENDS, impostazioni, attese, risultati, caricamento) c'era ancora la foto della mappa presa dal gioco (T_UI_ArenaScene_Ziggurat in LamaGround); l'aveva già detto il 13/10 (D0761: un'immagine di RAGEQUIT, non la mappa e non un'immagine in-game). La pagina ROOMS nuova era stata costruita sopra senza controllare. *(D0805)*
- [menu, grafica, skill, metodo] 15/10 mattina, dopo aver aperto il gioco (pacchetto 53f02424) durante il controllo generale D0806: tutta la grafica del gioco dozzinale. Dietro i personaggi sfondi grigi piatti in ogni immagine (chiede colori o forme, qualcosa di serio); gradienti e colori inesistenti; testi che non entrano nei tasti e nelle cornici; bottoni orribili o non fatti; sfondi brutti; texture mancanti nelle abilita'; il gioco non somiglia al progetto approvato dei menu. Il controllo generale aveva guardato regole, rete e server e lasciato la grafica com'era: richiesta di rifinire ogni dettaglio grafico. *(D0808)*
- [prove, metodo] 15/10 pomeriggio: durante la finitura (D0808) un giro di galleria completa per ogni ritocco (carica, ricarica, fascia, pavimento della zona): «test del cazzo sempre uguali che non portano ad un cazzo, io voglio risultati e cose serie e finite, non cazzate che devi ricontrollare ogni giro». Si corregge e si controlla una volta, alla fine, sul pacchetto. *(D0812)*
- [menu, grafica, combattimento] 16/10 mattina, dopo il pacchetto package-20261015-162154-186: il gioco pieno di problemi. Spesso i colpi non colpiscono, o colpiscono e non fanno danno; problemi grafici; i menu nel gioco somigliano al progetto approvato di Codex (D0771/D0776, .verify/menu-approved-card-finish-20261013) ma non sono quello: dozzinali, senza dettagli e rifiniture, con tante piccole cose sbagliate, mentre bastava seguire le figure. *(D0819)*
- [metodo, gioco, combattimento] 16/10 mattina, subito dopo D0819: i difetti sono molti di piu' di quelli elencati dall'assistente. Va rivisto tutto, non solo la grafica: a livello tecnico, come si fa per un videogioco FPS action 3D con abilita'. L'assistente ha dato per scontate troppe cose. *(D0821)*
- [combattimento] 17/10 sera, dopo i pacchetti del 17/10: la parata con il cooldown; gli attacchi base a distanza a raffica (l'arco a mitragliatrice) che fanno stravincere i ranged; l'uso della stamina e i cooldown sbagliati; alcune definitive e alcune abilità fatte male; il gioco che gracchia e lagga. E il metodo: un mese di prove visive che ripetono gli stessi errori e sciupano token. Ha chiesto una ricerca vera che risolva i problemi, non prove a caso. *(D0834)*
- [gioco, classi, combattimento, prove] 20/10 mattina, dopo il pacchetto del 19/10 giocato in locale contro un bot: il gioco ancora pieno di problemi di ogni tipo: animazioni che si vedono male, pezzi che escono dal corpo, l'arco della Deadeye che nella corsa entra nella testa e diventa enorme, scatti, desync, abilita' che non funzionano bene; gli stessi errori da mesi. Ha chiesto di smettere di inventare e di aggiustare tutto, perche' il gioco sembri professionale. *(D0847)*
- [metodo, classi] 20/10 pomeriggio: dopo la consegna l'assistente gli ha chiesto di nuovo se le frecce delle abilità dovessero tendersi del tutto e se anche i maghi dovessero avere un limite all'attacco base, cose già dette (D0849): non si richiede ciò che ha già deciso. *(D0853)*
- [combattimento] 20/10 sera: l'aggancio del bersaglio col tasto centrale (dal 27/09, T1 E58: girava la camera sul nemico a ogni fotogramma e i dardi a ricerca preferivano il bersaglio agganciato) era una mira automatica che nessuno aveva chiesto; nella proposta P6 l'assistente voleva toglierlo solo per dardi e frecce. *(D0860)*
- [combattimento, grafica] 20/10 sera, proposta P2 dello studio ABILITA-E-FEELING: un suono dedicato per la definitiva pronta al posto di quello del FIRST BLOOD: non serve, resta quello. *(D0861)*
- [metodo, gioco] 20/10 sera: dopo aver aggiunto al progetto una ventina di pacchetti audio di Fab senza aver deciso prima a cosa servisse ciascuno, l'assistente ha proposto di toglierne dal progetto la metà perché inutili. Bocciato: i pacchetti scaricati si tengono; si scarica il resto che può servire, soprattutto quello che non è audio, anche per sostituire cose che ci sono già ma sono brutte; poi si decide quali usare fra tutto ciò che si possiede e si scrive un piano. *(D0876)*
- [metodo] 20/10 sera: mentre l'assistente usava il controllo dello schermo per scaricare dal launcher di Epic, lo strumento abbassava le sue finestre (Brave, WhatsApp...) a ogni foto e clic. Vuole che resti sul secondo schermo e non lo disturbi. *(D0879)*
- [metodo, arene, classi, menu] 21/10 mattina: la proposta dello strato 1 guardava quasi solo i suoni; corpi, arene e menu (la parte che si vede di più) non avevano ancora asset scelti né mostrati nel gioco. *(D0889)*
- [metodo] 21/10: l'assistente non si era segnato quello che l'autore fa (pacchetti presi, accessi, scelte) e cambiava strada da solo invece di essere scrupoloso. *(D0897)*
- [classi, grafica, metodo] 21/10: nel piano annunciato all'autore l'assistente aveva messo «poi i corpi» (strato 2 del piano asset: corpi alternativi, corse e animazioni nuove). Rifiutato: corpi e animazioni, sistemati in mesi di lavoro, non si cambiano né si rifanno. Il lavoro è su suono, effetti, SFX, come si vedono i colpi, le abilità, i salti e gli elementi vari. *(D0901)*
- [metodo] 21/10, dopo la consegna dello strato 1 (suoni ed effetti, pacchetto package-20261021-090630-749): l'assistente ha fatto solo i suoni e pochi effetti, mentre l'autore aveva chiesto di aggiustare tutto il gioco, ogni cosa. Ha chiesto un piano serio: cosa e' gia' fatto, cosa no, cosa manca; l'elenco completo degli elementi del gioco; ogni tipo di asset da aggiustare. *(D0910)*
- [metodo, immagini] 21/10 sera: la pagina con foto prese dal gioco e suoni da ascoltare (Effetti e suoni RAGEQUIT, claude.ai/artifact/5QR93bm91LHxdq2qS6ELcC) e le riprese fatte per prepararla: tempo perso, non si capisce. Ha chiesto di fare il gioco e farlo bene. *(D0927)*
- [immagini] D0931: autore boccia la prima prova L istante prima (ragequit-istante-prima-v1.mp4): non capisce il risultato e non percepisce animazioni; la giudica inutile. La v1 non va integrata. La critica riguarda questo filmato e non cancella le opzioni 01 e 03, tenute in sospeso da D0930. *(D0932)*
- [immagini] D0934: autore boccia anche ragequit-istante-prima-v2.mp4 della direzione 02. Richiede produrre le altre proposte e usare skill, plugin e strumenti interni o esterni per animazione meno scattosa, piu fluida e professionale. Non e approvazione delle nuove produzioni. *(D0935)*
- [immagini] D0936: autore richiede migliorare Scontro corale, primo filmato delle alternative: braccio troppo lento, stacchi che non risolvono il gesto, arciera storta nella seconda scena e molte imperfezioni. Chiede ricerca vera su montaggio, skill, plugin e strumenti per correggere ritmo, anatomia e fluidita. La richiesta mantiene in lavoro questa direzione; non approva il filmato. *(D0937)*
- [immagini] D0938: autore boccia Scontro corale v2. Arciera che tira lentamente nel nulla, assenza di azione e conseguenze, ritmo ancora lento. Le correzioni tecniche di retiming e interpolazione non risolvono la richiesta di un filmato professionale. Richiede uso reale di programmi esterni e skill; non approva questa versione. *(D0939)*
- [immagini] Autore contesta il passaggio proposto verso Runway perche a pagamento. Resta D0327: tutto gratis. Nessun collegamento o acquisto e richiesto per proseguire la revisione dell'intro. *(D0941)*
- [immagini] Autore boccia ragequit-duello.mp4: realizzazione sbagliata, percepita come un frame che scorre anziche un combattimento credibile di film o anime. Chiede di smettere con questi rifacimenti ripetuti e contesta il metodo. Non proporre di nuovo questa produzione come riuscita. *(D0947)*
- [immagini] D0949: autore respinge la proposta di coreografare e renderizzare la scena in 3D. Richiede un video finto generato da una AI video capace; il vincolo gratuito D0327 resta. Non e approvazione di un modello o di una produzione specifica. *(D0950)*
- [immagini] 22/10 mattina: intro fatta con MiniMax H3 in ComfyUI (.verify/intro-h3-20261022, RAGEQUIT-intro-anteprima-720p.mp4): personaggi inventati (berserker col corno e strega mascherata) che non sono le classi di RAGEQUIT, arena e stile generici; non c'entra niente col gioco e lo stile non piace. La critica riguarda questo video. *(D0965)*
- [immagini] 22/10 pomeriggio: scheda dell'intro proposta in chat (Sentinel contro Pyromancer, circa 13 s di duello nell'arena gotica: palla di fuoco parata, ascia che spacca il pavimento, onda di fuoco, scontro al centro, logo dall'esplosione): non gli piace. Riguarda questa scena. *(D1061)*
- [immagini] 22/10 pomeriggio, intro: le inquadrature di posa di un personaggio alla volta (Pyromancer dietro il fuoco rituale, Tempestblade che atterra, primi piani di occhi e mano sulla spada) non vanno: vuole scene di battaglia intense, i personaggi che combattono, non uno showcase. Riguarda questa scaletta. *(D1080)*
- [immagini] 22/10 pomeriggio, fotogramma chiave b01 dell'intro (Tempestblade contro Pyromancer): effetto AI, personaggi lucidi come plastica, colori accesi e saturi, la Pyromancer blu puffo invece del blu pallido e opaco del gioco. *(D1093)*
- [arene] 23/10: autore rifiuta Iron Court e le tre arene mostrate: ambienti brutti e ripetitivi, materiali che sembrano una sola texture; illuminazione troppo chiara o troppo scura. Le immagini promozionali e i precedenti controlli tecnici non costituiscono accettazione. Riaperta la qualita visiva e funzionale delle tre mappe. *(D1211)*

### Da sapere
I fatti sul progetto (stato dei lavori, cosa è stato trovato) non stanno qui: `python tools/direttive.py prima <argomento>`.

<!-- DIRETTIVE:FINE -->

## Da dove si legge e dove si lavora

1. **Direttive dell'autore** (sopra, o `python tools/direttive.py prima <argomento>`): vincono su tutto.
2. Questo file: regole tecniche del repository.
3. [DOCUMENTAZIONE/README.md](DOCUMENTAZIONE/README.md): l'unica lista dei documenti, in ordine di priorità. Un documento che
   non è in quella lista non è una fonte. Stato del gioco, cose aperte e registro in `PIANO-DEFINITIVO.md`; comandi in
   `SVILUPPO.md`.

Un documento superato si cancella, non si archivia.

**Worktree e GitHub.** Le sessioni aperte in `.claude/worktrees/` nascono da `origin/main` (repository privata
`Spidahh/Ragequit`). L'autore, l'8/10: «devi sempre fcaricare su git hub le cose nuove»: dopo ogni commit su `main` lo stato
si carica da solo (`tools/publish-github.py`, aggancio post-commit; a mano lo stesso comando). Un worktree aperto prima
dell'ultimo caricamento ha file vecchi: vale `E:\PROGETTI\ragequit`, ramo `main`, e lì si committa.

**Più sessioni insieme.** Prima di toccare un file: `git status` e `git log --oneline -15` su `main`. Un file con modifiche
non salvate è di un'altra sessione: non si sovrascrive e non si sposta. Commit piccoli su `main`, uno per operazione finita,
documenti nello stesso commit. Un solo editor, cottura o compilazione pesante alla volta; non si chiudono i processi altrui.

## Cartella: ogni posto ha uno scopo

| Percorso | Contenuto |
| --- | --- |
| `unreal/` | L'unico progetto giocabile: Unreal 5.8.3 (CL 58210709) + Lyra. Git locale **senza remote**, escluso da questo repository |
| `game/` | Copia pubblica dei soli sorgenti propri, generata da `tools/sync-public-project.py`; non si modifica a mano |
| `art/` | Caratteri, icone e grafiche sorgente che i generatori importano nel gioco |
| `tools/` | Comandi di sviluppo ([indice](tools/README.md)); gli script dell'editor stanno in `tools/unreal/` |
| `services/` | Servizi del gioco online (matchmaker) |
| `DOCUMENTAZIONE/` | Vedi la sua [lista](DOCUMENTAZIONE/README.md): `DIRETTIVE/`, `ELEMENTI/` |
| `.verify/` | Rapporti e catture delle prove, sorgenti delle animazioni, base Lyra; nascosta, non svuotare |
| `E:\PROGETTI\ragequit-dossier` | Repository privata per le AI senza il PC: testo, dati esportati, schermate. Mai codice, asset o credenziali |
| `E:\PROGETTI\_DA-CANCELLARE\` | Fuori dal progetto: ciò che viene tolto finisce lì con un elenco, così il gioco e le AI non lo vedono più |

File nuovi: nella cartella del loro scopo, mai una cartella in radice per una consegna o una data. Una grafica importata va in `art/`. Prima di spostare codice o strumenti si leggono i consumatori:
i percorsi usati da import, MCP, Unreal e cottura sono dipendenze vere.

## Registro degli elementi

Le risorse del gioco sono schedate in [ELEMENTI](DOCUMENTAZIONE/ELEMENTI/LEGGIMI.md) (`02 - ELEMENTI DEL GIOCO`). Prima di
aggiungere una risorsa al gioco se ne registra la scheda con `tools/elementi.py save --file`, poi `export`. Nessun catalogo parallelo.

## Versionamento e pubblicazione

- `origin` di questo repository (`Spidahh/Ragequit`) dall'8/10 è **privato**; vale comunque: `unreal/` contiene Lyra e risorse Fab: non gli si aggiunge un remote e non
  si pubblicano sorgenti o asset di terzi (Fab, Lyra, Mixamo, Paragon). Licenze in [CREDITI-UNREAL.md](DOCUMENTAZIONE/CREDITI-UNREAL.md).
- I sorgenti si modificano in `unreal/`; `game/` si rigenera (`sync-public-project.py`, `--check` prima di pubblicare).
- Il dossier si aggiorna a ogni pacchetto consegnato (`python tools/sync-dossier.py`), commit e push di quella sola repository.
- Le versioni browser e Godot sono state ritirate il 24/09: non si ripristinano.

## Lavoro sul gioco

- **Una copia sola del gioco:** `01 - AVVIA UNREAL.lnk` apre `unreal/Saved/ShippingBuilds/Windows/Ragequit.exe`. Il pacchetto si
  fa solo dal cancello `tools/gate.ps1 -Package`. Il pacchetto presente si legge in `game/project-state.json`.
- **Prove: una volta sola per stato del gioco (D0905).** Ogni lancio di `tools/run-unreal-python.ps1` si segna da solo in
  `DOCUMENTAZIONE/PROVE/prove.jsonl`; una prova che solo guarda (test-, capture-, inspect-, diag-, measure-, audit-, export-,
  verify-), gia' verde con la stessa impronta (script, parametri, variabili RQ_*, motore, Source/Config/Content/Plugins), non
  riparte e ridà il suo rapporto. Prima di provare qualcosa: `python tools/prove.py elenco`; una prova fatta fuori dal
  lanciatore si segna con `python tools/prove.py segna-fuori`. `-Ripeti` solo se serve davvero.
- Codice presente o compilato non vuol dire gioco riuscito: una prova vecchia non certifica la build di oggi. Ogni schermata
  si guarda alla grandezza vera prima di consegnarla (`tools/test-unreal-menu-gallery.ps1`).
- Editor con Unreal MCP e `tools/ue-mcp.py`; le API Python si controllano sullo stub prima di usarle. Live Coding solo dentro
  i corpi delle funzioni; header, reflection e costruttori vogliono editor chiuso e build Editor. Mai editor o prove durante
  un aggiornamento del motore.
- Simulazione, danno ed esito sono autoritativi sul server. Prima di cambiare un effetto si leggono tutti i suoi consumatori,
  locali e di rete. I test di rete accodano l'input sul tick nativo: Python nell'editor forza le RPC a esecuzione locale.
- Il menu aspetta la chiusura di CommonLoadingScreen prima della pausa; i viaggi aspettano un frame completo non in pausa.
  Vanno conservati tutti e due: evitano il blocco del menu e l'ensure TaskSyncManager.
- Un asset entra nei montaggi solo con unità, scheletro e dipendenze giusti e dopo una riapertura. Le clip valide sono
  `Combat/Motion/Combat_Source_*`; le vecchie `Combat/Source_*` con root a scala 100 sono scartate.
- Dopo una modifica a montaggi, dati o camera si rilanciano i generatori indicati in `SVILUPPO.md`.
