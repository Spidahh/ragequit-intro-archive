# Parole, decisioni e bocciature dal registro autore

Sono righe originali, non tutte direttive: leggere tipo e stato. Le voci superate sono storia, non requisiti attuali. La finestra 928–1093 include risposte contestuali e richieste di metodo.

## D0049 · 2026-10-05 21:43 · parole · schedata

Voglio lavorare adesso sul **Duel 1v1 e sulla sua arena**, integrandoli nello stato REALE e più aggiornato del progetto che hai localmente.

Tu hai accesso al progetto completo e sei più aggiornato del dossier esterno: prima di modificare qualcosa verifica quindi implementazione corrente di Duel, Drowned Sanctum, match flow, pickup, Ultimate, respawn/reset, networking e classi Core V2.

Non ricostruire sistemi già esistenti se possono essere adattati bene.

Non modificare classi o combat balance per far funzionare la mappa: se emerge un problema di matchup o di kit, segnalalo separatamente. Per questo lavoro si interviene prima su **arena e regole del Duel**.

## OBIETTIVO

Il Duel deve smettere di essere soltanto:

**due personaggi in uno spazio che si colpiscono finché uno muore.**

La mappa deve aggiungere profondità attraverso:

**posizione → linee di vista → verticalità → rotazioni → controllo di una piccola risorsa laterale → controllo dell'obiettivo centrale → anti-stall.**

Non voglio però trasformarlo in un MOBA o in Quake.

Il combattimento fra le classi rimane il protagonista.

La mappa deve creare opportunità e decisioni, non decidere il vincitore.

---

# DUEL A ROUND

Voglio provare il Duel come:

**FIRST TO 3 ROUNDS / BEST OF FIVE**

Una morte assegna il round.

Niente respawn dentro lo stesso round.

Dopo la morte:

**round concluso → breve risultato → reset corretto → countdown → round successivo.**

Riutilizza il match flow già esistente dove possibile.

Il reset deve eliminare tutto ciò che NON deve passare al round successivo:

HP mancanti, stati, CC, costrutti, effetti persistenti, oggetti del round, cooldown residui e qualsiasi altra sporcizia dello scontro precedente.

Per la Ultimate **non inventare una nuova regola**: verifica prima il comportamento e l'economia attualmente previsti nel progetto e mantienili coerenti. Non introdurre né rimuovere persistenza della carica soltanto perché stiamo trasformando le kill in round.

Stessa cautela per qualunque altro stato globale già intenzionale.

---

# DROWNED SANCTUM

Non partire dall'idea che bisogna rifarla.

Prima esamina **la Drowned Sanctum che esiste realmente oggi nel progetto locale**.

Nel dossier l'ultima versione nota aveva già circa:

45,7 m di diametro;
spawn opposti intorno ai 34 m;
piano principale;
due terrazze circa +2,5 m;
più accessi alle terrazze;
colonne;
quattro elementi diagonali di rottura LoS;
blocchi vicino agli spawn;
fondo completamente chiuso.

Lo stato locale può essere più recente.

Voglio un **audit giocabile del layout attuale**, seguito dalle sole modifiche necessarie.

La scala 40–50 m è compatibile come punto di partenza con il combat attuale: i Core V2 noti si muovono intorno a 5,5 m/s e le principali minacce ranged arrivano circa a 12–15 m. Non allargare o restringere arbitrariamente l'arena.

---

# COSA DEVE PRODURRE LA GEOMETRIA

Voglio almeno tre tipi di spazio.

### SPAZIO APERTO

Serve per:

ranged;
skillshot;
lettura dei telegraph;
combattimento libero;
pressione sul Soul Core.

### SPAZIO CON LINEA DI VISTA INTERROTTA

Serve per:

rompere beam/projectile;
avvicinarsi;
disingaggiare;
cambiare angolo;
aggirare.

### POSIZIONE ELEVATA

Serve per ottenere:

visuale;
angolo migliore;
pressione;

ma NON sicurezza assoluta.

Nessuna posizione alta deve contemporaneamente controllare:

entrambi gli spawn;
Soul Core;
pickup;
tutte le principali rotazioni.

Una posizione vantaggiosa deve sempre poter essere contestata da più di una direzione.

---

# COVER

Non riempire la mappa di micro-cover.

RAGEQUIT deve rimanere leggibile anche quando due giocatori combattono molto vicini.

Preferire pochi elementi significativi che interrompono realmente la LoS.

Non fissarti sul numero di colonne/muri suggerito in documenti precedenti: guarda ciò che esiste e valuta funzionalmente ogni elemento.

Per ogni cover chiediti:

**permette una decisione tattica o serve soltanto a fare zig-zag attorno a un oggetto?**

Se crea pillar-dancing infinito, va cambiata.

Se rende impossibile a un melee avvicinarsi, manca cover.

Se impedisce a un ranged di ottenere qualunque linea utile, ce n'è troppa.

---

# COSTRUTTI DELLE CLASSI E GEOMETRIA

Questo punto è obbligatorio.

Stoneguard e qualunque altro costrutto che blocca corpi/proiettili devono essere testati contro la geometria reale.

Un singolo muro piazzabile NON deve poter trasformare una zona importante in una prigione senza alternativa.

Per ogni choke importante deve essere vera almeno una delle due condizioni:

**esiste un percorso alternativo realmente praticabile;**

oppure

**il costrutto può essere eliminato abbastanza velocemente da non creare una situazione di intrappolamento gratuita.**

Non allargare ogni passaggio alla cieca: verifica il comportamento con i costrutti reali.

---

# SPAWN

Mantieni due partenze competitive equivalenti.

Non devono necessariamente essere copie geometriche perfette, ma:

il tempo verso il centro deve essere equivalente;
il tempo verso il pickup deve essere equivalente;
nessuno deve avere automaticamente high ground;
nessuno deve avere visuale diretta e gratuita sull'altro allo start.

Voglio che nei primi secondi il giocatore possa scegliere almeno fra:

**pressione centrale**

oppure

**rotazione alternativa.**

Evita la situazione:

`spawn → unica strada → centro`.

Verifica le collisioni con le capsule reali dei personaggi.

---

# POWER DELLA MAPPA: RIDURLO, NON AUMENTARLO

Attualmente il progetto ha avuto Health, Energy, Rage e Haste.

Per il Duel NON voglio semplicemente riattivare tutto.

In particolare non voglio nella prima versione Duel:

**Rage +25% damage**

e

**Haste +30% movement.**

Sono modificatori troppo forti rispetto a matchup, distanze, skillshot e kill threshold.

Inoltre i sei Core V2 esportati nel dossier hanno attualmente `resource` vuoto, quindi NON introdurre automaticamente un Energy/Resource pickup basandoti sui vecchi Rage/Focus/Stamina.

Controlla lo stato locale: se anche lì i Core V2 non utilizzano quella risorsa, Energy non appartiene al Duel.

Non creare un nuovo tipo di risorsa soltanto per giustificare un pickup.

---

# MINOR PICKUP: HEALTH SHARD

Per la prima versione voglio **UN solo tipo di minor pickup**.

Health Shard.

Mettilo in una posizione laterale che richieda di abbandonare almeno parzialmente il controllo del centro.

Deve essere raggiungibile dai due spawn con vantaggio equivalente.

Valore iniziale da provare:

**circa 4% Max HP.**

Con gli attuali 1000 HP Core V2:

**40 HP.**

Non deve essere consumato se il giocatore è già a Max HP.

Valori iniziali:

**prima comparsa: circa 25 s**

**respawn dopo raccolta: circa 35 s**

Questi NON sono numeri sacri.

Sono baseline da provare con il combattimento reale.

Non aumentare la cura soltanto perché “sembra poco”: il Duel ha già durata lunga e il pickup deve creare una decisione, non cancellare il danno ricevuto.

Il respawn deve essere leggibile nel mondo tramite piedistallo/effetto/audio, senza obbligare il giocatore a fare calcoli esterni.

---

# SOUL CORE

Voglio un obiettivo neutrale centrale.

Nome di lavoro:

**Soul Core.**

Posizione:

area centrale del Duel.

Non è un pickup.

È un oggetto attaccabile.

Il suo scopo è creare periodicamente una ragione per:

contestare il centro;
esporsi;
interrompere l'avversario;
fingere di volerlo prendere;
rubare il last hit;
rinunciare al Core per colpire direttamente l'avversario.

Baseline:

**prima comparsa dopo circa 20 secondi.**

Il riferimento iniziale per la sua vita può essere circa **250 HP**, perché con i danni Core V2 attuali non dovrebbe sparire con una normale abilità.

Ma verifica contro TUTTI i kit reali presenti localmente.

Una normale skill non-Ultimate non deve one-shottarlo.

Non modificare il danno delle classi per adattarle al Core.

Se necessario modifica esclusivamente il profilo/HP dell'obiettivo.

---

# IL SOUL CORE NON È UN PLAYER

Questo deve essere gestito esplicitamente.

Colpire il Soul Core NON deve:

caricare Ultimate;
attivare execute;
applicare bleed/slow/stun/root;
ricevere knockback;
ricevere displacement;
ricevere mark destinati ai player;
attivare lifesteal;
attivare on-kill;
contare come player hit;
contare nelle statistiche PvP;
attivare meccaniche che richiedono aver colpito un vero avversario.

Deve accettare il danno necessario alla contesa, con feedback dedicato.

Rimane fisso nella sua posizione.

Non deve essere spostabile.

Se alcuni skill system esistenti distinguono già neutral/objective/player, usa quella struttura; non creare eccezioni sparse se esiste una soluzione più pulita.

---

# LAST HIT DEL SOUL CORE

Il giocatore che infligge il colpo finale valido prende la ricompensa.

NON dare Ultimate Charge.

Il progetto aveva già rimosso la ricompensa di carica Ultimate e non voglio reintrodurla indirettamente.

NON dare Resource se le classi Core V2 non hanno una resource economy attiva.

Per la prima implementazione mantieni il premio semplice:

**circa 5% Max HP.**

Con 1000 HP:

**50 HP.**

Non oltre Max HP.

Il vantaggio vero del Core deve essere:

piccola recovery + negazione all'avversario + controllo del centro.

Non deve trasformare chi lo prende in un personaggio potenziato.

Baseline respawn:

**circa 35 secondi dalla distruzione.**

Mostrare chiaramente nel mondo quando sta tornando, soprattutto negli ultimi ~5 secondi.

---

# NIENTE ALTRI BUFF NELLA PRIMA VERSIONE

Non aggiungere per riempire la mappa:

damage boost;
movement boost;
cooldown boost;
shield;
invulnerabilità;
attack-speed;
random buff.

Prima voglio vedere se:

**Health Shard + Soul Core + geometria**

sono sufficienti a creare map control interessante.

Troppa potenza distribuita sulla mappa rischia di trasformare il vantaggio posizionale in snowball.

Se una zona della mappa resta inutilizzata, prima prova a risolverla con geometria, percorso, LoS o posizione dell'obiettivo.

Non aggiungere automaticamente un altro power-up.

---

# SUDDEN DEATH

Non voglio un Duel in cui uno può evitare lo scontro indefinitamente.

Dopo un tempo configurabile deve iniziare il Sudden Death.

Baseline iniziale da provare:

**120 secondi.**

Non considerarlo bilanciamento definitivo: la durata vera dei duelli la giudicherò giocando.

Quando parte:

non generare nuovi Health Shard;
non generare nuovi Soul Core;
gli oggetti già presenti possono rimanere finché raccolti o finché diventano irraggiungibili per la chiusura;
mostrare chiaramente l'inizio della fase.

L'area sicura comincia a restringersi progressivamente verso il centro.

La chiusura deve essere abbastanza lenta da continuare a permettere combattimento e repositioning.

Non voglio la sensazione da Battle Royale.

---

# IL DUEL DEVE FINIRE CON UNA SCONFITTA, NON AI PUNTI

NON usare:

“allo scadere vince chi ha fatto più danni”.

Creerebbe un incentivo a prendere vantaggio e poi evitare lo scontro.

La zona deve continuare a restringersi fino a rendere inevitabile la conclusione.

Baseline iniziale:

circa **40–50 secondi** di progressiva compressione.

Il danno fuori zona può partire intorno a:

**5% Max HP al secondo**

server-authoritative, non parabile e non mitigabile tramite normali difese.

Verifica che dash/blink/iframe non permettano exploit della zona.

Se entrambi muoiono realmente nello stesso tick/server event per il Sudden Death:

**DRAW DEL ROUND → nessun punto → round ripetuto.**

Non inventare un vincitore con criteri nascosti.

---

# NIENTE MORTE AMBIENTALE NORMALE

Fuori dal Sudden Death non voglio:

burroni letali;
lava;
instant death;
trappole;
fuoco automatico;
cadute fuori dal mondo.

Il knockback deve creare posizione e combo.

Non deve trasformare una singola spinta in una vittoria istantanea perché vicino allo spawn c'è un precipizio.

---

# LEGGIBILITÀ

L'arena deve restare abbastanza pulita da leggere:

telegraph;
personaggi;
projectile;
muri;
Soul Core;
Health Shard;
bordo Sudden Death.

Niente erba/foliage dentro il combat space che nasconde telegraph.

Niente oscurità eccessiva.

Niente piccoli dettagli con collisione che fanno fermare dash o personaggi.

Niente soffitti/archi bassi nelle zone dove si combatte.

La verticalità deve essere leggibile dalla camera in terza persona.

---

# COSA DEVE ESSERE TESTATO CON LE CLASSI REALI

Non testare la mappa soltanto con un personaggio generico.

Usa almeno i diversi archetipi realmente presenti.

Controlla in particolare:

**Juggernaut:** può raggiungere e lavorare con muri/geometria senza ottenere pin ambientali gratuiti ovunque?

**Stoneguard:** Rampart crea decisioni oppure chiude rotazioni intere?

**Voidseer:** esistono LoS breaker reali contro Echo/Null Ray senza rendere il ranged inutile?

**Tempestblade/Reaper:** mobilità e inseguimento funzionano senza collisioni stupide?

**Sentinel:** le vie di approccio permettono di usare correttamente difesa e pressione senza trasformare una zona in bunker?

Ripeti lo stesso ragionamento con qualunque classe nuova presente nel progetto locale e non ancora nel dossier.

---

# NETWORKING

Round, Core, pickup e Sudden Death devono rispettare l'architettura server-authoritative già usata dal gioco.

Il server deve decidere almeno:

round start/end;
morte;
punteggio;
availability dei pickup;
raccolta;
HP del Soul Core;
ultimo colpo valido;
assegnazione reward;
stato della zona;
danno della zona.

Evita doppie ricompense causate da prediction/replication.

Non introdurre una seconda architettura parallela se il progetto possiede già sistemi adatti.

---

# TEST

I test automatici devono dimostrare soltanto cose oggettive:

round reset corretto;
nessun residuo dello scontro precedente;
Soul Core replica correttamente;
reward una volta sola;
Core non genera Ultimate/proc player;
Health Shard non viene consumato a HP pieni;
pickup timer coerenti;
zona Sudden Death replicata;
round/match finiscono correttamente;
nessuna caduta fuori arena;
spawn validi;
costrutti non creano blocchi topologici impossibili.

NON usare bot o test automatici per dichiarare:

“la mappa è bilanciata”;
“il Duel dura il giusto”;
“il matchup è divertente”;
“il Soul Core ha il valore perfetto”.

Queste cose devono essere giudicate giocando PvP umano.

---

# METODO DI LAVORO

Prima:

**AUDIT della Drowned Sanctum attuale.**

Poi:

**greybox / modifiche funzionali.**

Poi:

**Duel round flow.**

Poi:

**Health Shard.**

Poi:

**Soul Core.**

Poi:

**Sudden Death.**

Poi:

**rete/test funzionali.**

Solo quando la struttura funziona:

**rifinitura artistica.**

Non spendere tempo a rendere bella una geometria che potrebbe essere cambiata dopo il primo vero 1v1.

---

# RISULTATO CHE VOGLIO

Alla fine voglio che durante un Duel esistano decisioni del tipo:

“lo inseguo o controllo il Core?”

“mi espongo per recuperare 40 HP?”

“gli lascio il Core ma prendo posizione migliore?”

“lo costringo ad attraversare una linea scoperta?”

“rompo LoS dal beam?”

“salgo oppure gli taglio la rotazione?”

“sta colpendo il Core: provo a rubarlo o colpisco direttamente lui?”

“sono in vantaggio ma il Sudden Death mi impedisce di correre all'infinito.”

Se la mappa produce queste decisioni senza togliere importanza a mira, movement, timing, matchup e uso delle abilità, siamo nella direzione giusta.

Se invece il giocatore vince principalmente perché ha raccolto più buff, abbiamo sbagliato.

Prima di implementare, confronta questa specifica con lo stato locale più recente. **Correggi autonomamente i dettagli tecnici diventati obsoleti**, ma non cambiare silenziosamente i pilastri di gameplay sopra.

Quando trovi un conflitto reale fra questa specifica e lo stato corrente del gioco, risolvilo nel modo più coerente con il combat attuale e documenta cosa hai cambiato e perché.

## D0051 · 2026-10-05 22:35 · parole · schedata

MA SE ICOGLIONE ??? DEVI FARE UNA MAPPA COME DUEL COME SCRITTO QUA CAZZONE DI MERDA 


Voglio lavorare adesso sul **Duel 1v1 e sulla sua arena**, integrandoli nello stato REALE e più aggiornato del progetto che hai localmente.

Tu hai accesso al progetto completo e sei più aggiornato del dossier esterno: prima di modificare qualcosa verifica quindi implementazione corrente di Duel, Drowned Sanctum, match flow, pickup, Ultimate, respawn/reset, networking e classi Core V2.

Non ricostruire sistemi già esistenti se possono essere adattati bene.

Non modificare classi o combat balance per far funzionare la mappa: se emerge un problema di matchup o di kit, segnalalo separatamente. Per questo lavoro si interviene prima su **arena e regole del Duel**.

## OBIETTIVO

Il Duel deve smettere di essere soltanto:

**due personaggi in uno spazio che si colpiscono finché uno muore.**

La mappa deve aggiungere profondità attraverso:

**posizione → linee di vista → verticalità → rotazioni → controllo di una piccola risorsa laterale → controllo dell'obiettivo centrale → anti-stall.**

Non voglio però trasformarlo in un MOBA o in Quake.

Il combattimento fra le classi rimane il protagonista.

La mappa deve creare opportunità e decisioni, non decidere il vincitore.

---

# DUEL A ROUND

Voglio provare il Duel come:

**FIRST TO 3 ROUNDS / BEST OF FIVE**

Una morte assegna il round.

Niente respawn dentro lo stesso round.

Dopo la morte:

**round concluso → breve risultato → reset corretto → countdown → round successivo.**

Riutilizza il match flow già esistente dove possibile.

Il reset deve eliminare tutto ciò che NON deve passare al round successivo:

HP mancanti, stati, CC, costrutti, effetti persistenti, oggetti del round, cooldown residui e qualsiasi altra sporcizia dello scontro precedente.

Per la Ultimate **non inventare una nuova regola**: verifica prima il comportamento e l'economia attualmente previsti nel progetto e mantienili coerenti. Non introdurre né rimuovere persistenza della carica soltanto perché stiamo trasformando le kill in round.

Stessa cautela per qualunque altro stato globale già intenzionale.

---

# DROWNED SANCTUM

Non partire dall'idea che bisogna rifarla.

Prima esamina **la Drowned Sanctum che esiste realmente oggi nel progetto locale**.

Nel dossier l'ultima versione nota aveva già circa:

45,7 m di diametro;
spawn opposti intorno ai 34 m;
piano principale;
due terrazze circa +2,5 m;
più accessi alle terrazze;
colonne;
quattro elementi diagonali di rottura LoS;
blocchi vicino agli spawn;
fondo completamente chiuso.

Lo stato locale può essere più recente.

Voglio un **audit giocabile del layout attuale**, seguito dalle sole modifiche necessarie.

La scala 40–50 m è compatibile come punto di partenza con il combat attuale: i Core V2 noti si muovono intorno a 5,5 m/s e le principali minacce ranged arrivano circa a 12–15 m. Non allargare o restringere arbitrariamente l'arena.

---

# COSA DEVE PRODURRE LA GEOMETRIA

Voglio almeno tre tipi di spazio.

### SPAZIO APERTO

Serve per:

ranged;
skillshot;
lettura dei telegraph;
combattimento libero;
pressione sul Soul Core.

### SPAZIO CON LINEA DI VISTA INTERROTTA

Serve per:

rompere beam/projectile;
avvicinarsi;
disingaggiare;
cambiare angolo;
aggirare.

### POSIZIONE ELEVATA

Serve per ottenere:

visuale;
angolo migliore;
pressione;

ma NON sicurezza assoluta.

Nessuna posizione alta deve contemporaneamente controllare:

entrambi gli spawn;
Soul Core;
pickup;
tutte le principali rotazioni.

Una posizione vantaggiosa deve sempre poter essere contestata da più di una direzione.

---

# COVER

Non riempire la mappa di micro-cover.

RAGEQUIT deve rimanere leggibile anche quando due giocatori combattono molto vicini.

Preferire pochi elementi significativi che interrompono realmente la LoS.

Non fissarti sul numero di colonne/muri suggerito in documenti precedenti: guarda ciò che esiste e valuta funzionalmente ogni elemento.

Per ogni cover chiediti:

**permette una decisione tattica o serve soltanto a fare zig-zag attorno a un oggetto?**

Se crea pillar-dancing infinito, va cambiata.

Se rende impossibile a un melee avvicinarsi, manca cover.

Se impedisce a un ranged di ottenere qualunque linea utile, ce n'è troppa.

---

# COSTRUTTI DELLE CLASSI E GEOMETRIA

Questo punto è obbligatorio.

Stoneguard e qualunque altro costrutto che blocca corpi/proiettili devono essere testati contro la geometria reale.

Un singolo muro piazzabile NON deve poter trasformare una zona importante in una prigione senza alternativa.

Per ogni choke importante deve essere vera almeno una delle due condizioni:

**esiste un percorso alternativo realmente praticabile;**

oppure

**il costrutto può essere eliminato abbastanza velocemente da non creare una situazione di intrappolamento gratuita.**

Non allargare ogni passaggio alla cieca: verifica il comportamento con i costrutti reali.

---

# SPAWN

Mantieni due partenze competitive equivalenti.

Non devono necessariamente essere copie geometriche perfette, ma:

il tempo verso il centro deve essere equivalente;
il tempo verso il pickup deve essere equivalente;
nessuno deve avere automaticamente high ground;
nessuno deve avere visuale diretta e gratuita sull'altro allo start.

Voglio che nei primi secondi il giocatore possa scegliere almeno fra:

**pressione centrale**

oppure

**rotazione alternativa.**

Evita la situazione:

`spawn → unica strada → centro`.

Verifica le collisioni con le capsule reali dei personaggi.

---

# POWER DELLA MAPPA: RIDURLO, NON AUMENTARLO

Attualmente il progetto ha avuto Health, Energy, Rage e Haste.

Per il Duel NON voglio semplicemente riattivare tutto.

In particolare non voglio nella prima versione Duel:

**Rage +25% damage**

e

**Haste +30% movement.**

Sono modificatori troppo forti rispetto a matchup, distanze, skillshot e kill threshold.

Inoltre i sei Core V2 esportati nel dossier hanno attualmente `resource` vuoto, quindi NON introdurre automaticamente un Energy/Resource pickup basandoti sui vecchi Rage/Focus/Stamina.

Controlla lo stato locale: se anche lì i Core V2 non utilizzano quella risorsa, Energy non appartiene al Duel.

Non creare un nuovo tipo di risorsa soltanto per giustificare un pickup.

---

# MINOR PICKUP: HEALTH SHARD

Per la prima versione voglio **UN solo tipo di minor pickup**.

Health Shard.

Mettilo in una posizione laterale che richieda di abbandonare almeno parzialmente il controllo del centro.

Deve essere raggiungibile dai due spawn con vantaggio equivalente.

Valore iniziale da provare:

**circa 4% Max HP.**

Con gli attuali 1000 HP Core V2:

**40 HP.**

Non deve essere consumato se il giocatore è già a Max HP.

Valori iniziali:

**prima comparsa: circa 25 s**

**respawn dopo raccolta: circa 35 s**

Questi NON sono numeri sacri.

Sono baseline da provare con il combattimento reale.

Non aumentare la cura soltanto perché “sembra poco”: il Duel ha già durata lunga e il pickup deve creare una decisione, non cancellare il danno ricevuto.

Il respawn deve essere leggibile nel mondo tramite piedistallo/effetto/audio, senza obbligare il giocatore a fare calcoli esterni.

---

# SOUL CORE

Voglio un obiettivo neutrale centrale.

Nome di lavoro:

**Soul Core.**

Posizione:

area centrale del Duel.

Non è un pickup.

È un oggetto attaccabile.

Il suo scopo è creare periodicamente una ragione per:

contestare il centro;
esporsi;
interrompere l'avversario;
fingere di volerlo prendere;
rubare il last hit;
rinunciare al Core per colpire direttamente l'avversario.

Baseline:

**prima comparsa dopo circa 20 secondi.**

Il riferimento iniziale per la sua vita può essere circa **250 HP**, perché con i danni Core V2 attuali non dovrebbe sparire con una normale abilità.

Ma verifica contro TUTTI i kit reali presenti localmente.

Una normale skill non-Ultimate non deve one-shottarlo.

Non modificare il danno delle classi per adattarle al Core.

Se necessario modifica esclusivamente il profilo/HP dell'obiettivo.

---

# IL SOUL CORE NON È UN PLAYER

Questo deve essere gestito esplicitamente.

Colpire il Soul Core NON deve:

caricare Ultimate;
attivare execute;
applicare bleed/slow/stun/root;
ricevere knockback;
ricevere displacement;
ricevere mark destinati ai player;
attivare lifesteal;
attivare on-kill;
contare come player hit;
contare nelle statistiche PvP;
attivare meccaniche che richiedono aver colpito un vero avversario.

Deve accettare il danno necessario alla contesa, con feedback dedicato.

Rimane fisso nella sua posizione.

Non deve essere spostabile.

Se alcuni skill system esistenti distinguono già neutral/objective/player, usa quella struttura; non creare eccezioni sparse se esiste una soluzione più pulita.

---

# LAST HIT DEL SOUL CORE

Il giocatore che infligge il colpo finale valido prende la ricompensa.

NON dare Ultimate Charge.

Il progetto aveva già rimosso la ricompensa di carica Ultimate e non voglio reintrodurla indirettamente.

NON dare Resource se le classi Core V2 non hanno una resource economy attiva.

Per la prima implementazione mantieni il premio semplice:

**circa 5% Max HP.**

Con 1000 HP:

**50 HP.**

Non oltre Max HP.

Il vantaggio vero del Core deve essere:

piccola recovery + negazione all'avversario + controllo del centro.

Non deve trasformare chi lo prende in un personaggio potenziato.

Baseline respawn:

**circa 35 secondi dalla distruzione.**

Mostrare chiaramente nel mondo quando sta tornando, soprattutto negli ultimi ~5 secondi.

---

# NIENTE ALTRI BUFF NELLA PRIMA VERSIONE

Non aggiungere per riempire la mappa:

damage boost;
movement boost;
cooldown boost;
shield;
invulnerabilità;
attack-speed;
random buff.

Prima voglio vedere se:

**Health Shard + Soul Core + geometria**

sono sufficienti a creare map control interessante.

Troppa potenza distribuita sulla mappa rischia di trasformare il vantaggio posizionale in snowball.

Se una zona della mappa resta inutilizzata, prima prova a risolverla con geometria, percorso, LoS o posizione dell'obiettivo.

Non aggiungere automaticamente un altro power-up.

---

# SUDDEN DEATH

Non voglio un Duel in cui uno può evitare lo scontro indefinitamente.

Dopo un tempo configurabile deve iniziare il Sudden Death.

Baseline iniziale da provare:

**120 secondi.**

Non considerarlo bilanciamento definitivo: la durata vera dei duelli la giudicherò giocando.

Quando parte:

non generare nuovi Health Shard;
non generare nuovi Soul Core;
gli oggetti già presenti possono rimanere finché raccolti o finché diventano irraggiungibili per la chiusura;
mostrare chiaramente l'inizio della fase.

L'area sicura comincia a restringersi progressivamente verso il centro.

La chiusura deve essere abbastanza lenta da continuare a permettere combattimento e repositioning.

Non voglio la sensazione da Battle Royale.

---

# IL DUEL DEVE FINIRE CON UNA SCONFITTA, NON AI PUNTI

NON usare:

“allo scadere vince chi ha fatto più danni”.

Creerebbe un incentivo a prendere vantaggio e poi evitare lo scontro.

La zona deve continuare a restringersi fino a rendere inevitabile la conclusione.

Baseline iniziale:

circa **40–50 secondi** di progressiva compressione.

Il danno fuori zona può partire intorno a:

**5% Max HP al secondo**

server-authoritative, non parabile e non mitigabile tramite normali difese.

Verifica che dash/blink/iframe non permettano exploit della zona.

Se entrambi muoiono realmente nello stesso tick/server event per il Sudden Death:

**DRAW DEL ROUND → nessun punto → round ripetuto.**

Non inventare un vincitore con criteri nascosti.

---

# NIENTE MORTE AMBIENTALE NORMALE

Fuori dal Sudden Death non voglio:

burroni letali;
lava;
instant death;
trappole;
fuoco automatico;
cadute fuori dal mondo.

Il knockback deve creare posizione e combo.

Non deve trasformare una singola spinta in una vittoria istantanea perché vicino allo spawn c'è un precipizio.

---

# LEGGIBILITÀ

L'arena deve restare abbastanza pulita da leggere:

telegraph;
personaggi;
projectile;
muri;
Soul Core;
Health Shard;
bordo Sudden Death.

Niente erba/foliage dentro il combat space che nasconde telegraph.

Niente oscurità eccessiva.

Niente piccoli dettagli con collisione che fanno fermare dash o personaggi.

Niente soffitti/archi bassi nelle zone dove si combatte.

La verticalità deve essere leggibile dalla camera in terza persona.

---

# COSA DEVE ESSERE TESTATO CON LE CLASSI REALI

Non testare la mappa soltanto con un personaggio generico.

Usa almeno i diversi archetipi realmente presenti.

Controlla in particolare:

**Juggernaut:** può raggiungere e lavorare con muri/geometria senza ottenere pin ambientali gratuiti ovunque?

**Stoneguard:** Rampart crea decisioni oppure chiude rotazioni intere?

**Voidseer:** esistono LoS breaker reali contro Echo/Null Ray senza rendere il ranged inutile?

**Tempestblade/Reaper:** mobilità e inseguimento funzionano senza collisioni stupide?

**Sentinel:** le vie di approccio permettono di usare correttamente difesa e pressione senza trasformare una zona in bunker?

Ripeti lo stesso ragionamento con qualunque classe nuova presente nel progetto locale e non ancora nel dossier.

---

# NETWORKING

Round, Core, pickup e Sudden Death devono rispettare l'architettura server-authoritative già usata dal gioco.

Il server deve decidere almeno:

round start/end;
morte;
punteggio;
availability dei pickup;
raccolta;
HP del Soul Core;
ultimo colpo valido;
assegnazione reward;
stato della zona;
danno della zona.

Evita doppie ricompense causate da prediction/replication.

Non introdurre una seconda architettura parallela se il progetto possiede già sistemi adatti.

---

# TEST

I test automatici devono dimostrare soltanto cose oggettive:

round reset corretto;
nessun residuo dello scontro precedente;
Soul Core replica correttamente;
reward una volta sola;
Core non genera Ultimate/proc player;
Health Shard non viene consumato a HP pieni;
pickup timer coerenti;
zona Sudden Death replicata;
round/match finiscono correttamente;
nessuna caduta fuori arena;
spawn validi;
costrutti non creano blocchi topologici impossibili.

NON usare bot o test automatici per dichiarare:

“la mappa è bilanciata”;
“il Duel dura il giusto”;
“il matchup è divertente”;
“il Soul Core ha il valore perfetto”.

Queste cose devono essere giudicate giocando PvP umano.

---

# METODO DI LAVORO

Prima:

**AUDIT della Drowned Sanctum attuale.**

Poi:

**greybox / modifiche funzionali.**

Poi:

**Duel round flow.**

Poi:

**Health Shard.**

Poi:

**Soul Core.**

Poi:

**Sudden Death.**

Poi:

**rete/test funzionali.**

Solo quando la struttura funziona:

**rifinitura artistica.**

Non spendere tempo a rendere bella una geometria che potrebbe essere cambiata dopo il primo vero 1v1.

---

# RISULTATO CHE VOGLIO

Alla fine voglio che durante un Duel esistano decisioni del tipo:

“lo inseguo o controllo il Core?”

“mi espongo per recuperare 40 HP?”

“gli lascio il Core ma prendo posizione migliore?”

“lo costringo ad attraversare una linea scoperta?”

“rompo LoS dal beam?”

“salgo oppure gli taglio la rotazione?”

“sta colpendo il Core: provo a rubarlo o colpisco direttamente lui?”

“sono in vantaggio ma il Sudden Death mi impedisce di correre all'infinito.”

Se la mappa produce queste decisioni senza togliere importanza a mira, movement, timing, matchup e uso delle abilità, siamo nella direzione giusta.

Se invece il giocatore vince principalmente perché ha raccolto più buff, abbiamo sbagliato.

Prima di implementare, confronta questa specifica con lo stato locale più recente. **Correggi autonomamente i dettagli tecnici diventati obsoleti**, ma non cambiare silenziosamente i pilastri di gameplay sopra.

Quando trovi un conflitto reale fra questa specifica e lo stato corrente del gioco, risolvilo nel modo più coerente con il combat attuale e documenta cosa hai cambiato e perché.

## D0061 · 2026-10-06 06:57 · parole · schedata

Voglio che adesso ti concentri **SOLO sulla progettazione e realizzazione seria dell’arena Duel di RAGEQUIT**.

Hai il progetto locale completo e aggiornato: prima guarda lo stato reale di Drowned Sanctum, le modifiche eventualmente fatte negli ultimi tentativi, il Git diff, i sistemi arena già esistenti, le classi Core V2 e gli strumenti disponibili.

Se precedenti istruzioni hanno introdotto modifiche brutte, casuali o distruttive nell’arena, **non continuare a costruirci sopra per inerzia**. Identifica cosa è stato cambiato, conserva solo ciò che è realmente migliore e recupera la base sana dove necessario.

NON fare rollback indiscriminati di altre parti del gioco.

## SCOPO

Voglio una **vera arena fantasy PvP 1v1 grande, monumentale, bella da vedere e soprattutto progettata attorno al combat di RAGEQUIT**.

RAGEQUIT NON è Quake con una skin fantasy.

È un action PvP in terza persona con:

- melee;
- ranged;
- mage;
- combattimento ravvicinato fisico;
- knockback;
- stagger;
- dash/step/leap;
- beam;
- projectile;
- AoE;
- telegraph a terra;
- muri e costrutti;
- classi con mobilità molto diversa;
- duelli che devono svilupparsi e durare.

La mappa deve far funzionare QUESTO combat.

Non costruire un cerchio simmetrico con quattro pilastri.

Non costruire un labirinto.

Non costruire una piccola arena eSport astratta.

Voglio che sembri di combattere dentro **un enorme santuario fantasy in rovina**, anche se l’area competitiva reale rimane controllata.

# PRINCIPIO FONDAMENTALE

Separare:

**GRANDEZZA VISIVA**

da

**GRANDEZZA GIOCABILE.**

Il luogo deve sembrare molto più vasto dell’area realmente percorribile.

Torri, rovine, palude, statue, strutture spezzate, ponti crollati, livelli architettonici e fondale devono continuare visivamente oltre il campo di battaglia.

Ma il giocatore non deve poter correre per 20 secondi lontano dall’avversario.

Target area realmente combattibile:

**circa 52–56 metri di diametro massimo.**

Non considerarlo un cerchio perfetto: questa è l’impronta complessiva.

Il santuario visivo circostante può essere molto più grande.

# STRUTTURA GENERALE

La mappa deve avere **TRE QUOTE REALI** e **CINQUE MACRO-ZONE**.

Quote indicative:

**LOW:** -1 / -1,5 m  
**MAIN:** 0 m  
**HIGH:** +3 / +3,5 m

Macro-zone:

1. WEST SPAWN COURT
2. EAST SPAWN COURT
3. CENTRAL SANCTUM
4. NORTH HIGH TERRACE
5. SOUTH SUNKEN RUINS

Schema concettuale:

```text
                         NORTH HIGH TERRACE
                              +3 / +3.5 m

               ╭────────────────────────────────╮
              ╱                                  ╲
      WEST RAMP                                    EAST RAMP
            ╲                                      ╱
             ╲                                    ╱

       ┌────────────┐                      ┌────────────┐
       │ NW RUIN    │                      │ NE RUIN    │
       │ FULL COVER │                      │ FULL COVER │
       └────────────┘                      └────────────┘

WEST SPAWN  ───────────   CENTRAL SANCTUM   ─────────── EAST SPAWN

                            SOUL CORE
                               ◉

       ┌────────────┐                      ┌────────────┐
       │ SW RUIN    │                      │ SE RUIN    │
       │ FULL COVER │                      │ FULL COVER │
       └────────────┘                      └────────────┘

             ╲                                    ╱
              ╲                                  ╱

                   SOUTH SUNKEN RUINS
                         -1 / -1.5 m

                        HEALTH SHRINE
                              ○
```

NON deve essere visivamente speculare come un’arena artificiale.

Deve essere **competitivamente equilibrata ma artisticamente asimmetrica**.

Esempio:

- NW può essere una grande colonna spezzata con muro;
- NE può essere un arco crollato;
- una salita può essere una scala monumentale;
- l’altra può essere una rampa di pietra;
- i due spawn possono avere architettura differente ma tempi di percorrenza equivalenti.

# CENTRAL SANCTUM

Questa è la grande piazza centrale del duello.

Diametro utile:

**circa 18–20 metri.**

Deve essere il miglior posto per un combattimento aperto.

Pavimento:

- piatto o quasi;
- pulito;
- niente erba;
- niente macerie con collisione;
- telegraph perfettamente visibili.

Deve esserci spazio per:

- combo melee;
- strafing;
- dash;
- AoE;
- knockback;
- projectile;
- beam;
- inseguimenti brevi.

NON mettere colonne nel cuore della piazza.

NON mettere cover piccole intorno al Soul Core.

La parte centrale deve respirare.

Il giocatore deve percepirla come:

**“qui posso combattere veramente”.**

# SOUL CORE

Al centro della piazza:

**Soul Core.**

Non deve essere semplicemente una sfera fluttuante buttata nel mezzo.

Deve essere integrato nell’architettura:

- piccolo altare;
- cerchio runico;
- piedistallo;
- elemento fantasy riconoscibile.

Ma deve restare basso e non utilizzabile come cover.

Il Core:

- non blocca player;
- non blocca projectile;
- non rompe LoS;
- non può essere spostato;
- non riceve CC;
- non riceve knockback;
- non viene considerato un player.

Colpirlo NON deve:

- caricare Ultimate;
- attivare execute;
- applicare mark;
- attivare lifesteal;
- attivare passive contro player;
- entrare nelle statistiche damage PvP.

È un objective neutrale.

Baseline configurabile:

**circa 240 HP.**

Ma devi controllarla contro TUTTI i kit realmente presenti adesso.

Una singola normale abilità non-Ultimate non deve distruggerlo.

Tempo ideale di commitment se il nemico non interferisce:

**circa 3–5 secondi.**

Primo spawn indicativo:

**20 s.**

Respawn indicativo:

**35 s.**

Questi valori devono essere DATA-DRIVEN/configurabili.

Premio iniziale:

**circa 5% Max HP.**

Sugli attuali 1000 HP:

**50 HP.**

Niente damage buff.

Niente speed buff.

Niente Ultimate Charge.

Niente vecchie Resource se il roster Core V2 corrente non le utilizza.

Il premio deve essere utile, non devastante.

Il vero valore del Core deve essere:

**controllo del centro + piccola recovery + deny al nemico.**

# QUATTRO GRANDI LoS BREAKER

Attorno alla piazza centrale devono esserci quattro grandi strutture.

NON piccoli pilastri.

Dimensione indicativa di ciascuna:

**3,5–5 m di lunghezza**
**1–2 m di profondità**
**almeno 3 m di altezza**

Posizioni approssimative attorno agli angoli della Central Sanctum:

NW  
NE  
SW  
SE

Devono creare quattro ingressi alla piazza.

Devono permettere:

- rompere Null Ray;
- rompere projectile;
- fare un flank;
- avvicinarsi a un ranged;
- interrompere momentaneamente la LoS;
- cambiare direzione.

NON devono permettere:

**correre intorno allo stesso pilastro all’infinito.**

Il blocker deve essere abbastanza grande da richiedere una scelta:

**sinistra o destra.**

Non:

**girotondo attorno a una colonna di 80 cm.**

# NORTH HIGH TERRACE

Questa è la zona alta principale.

Quota:

**circa +3 / +3,5 metri.**

Deve sembrare parte importante del santuario:

- grande balconata;
- gradinata;
- rovine monumentali;
- statue/colonnato sullo sfondo.

Larghezza utile:

**circa 16–18 m.**

Profondità combattibile:

**circa 6–8 m.**

Deve essere un posto dove un ranged PENSA:

**“se conquisto quella posizione ho un buon angolo”.**

Ma non:

**“se arrivo lì ho vinto”.**

Accessi minimi:

- rampa/scala ovest;
- rampa/scala est;
- accesso centrale o semi-centrale.

Almeno **tre modi reali di raggiungerla**.

Le rampe/scale devono essere larghe.

Target:

**4–5 m.**

Niente scalette strette.

Da lassù devo avere alcune sightline lunghe, ma elementi architettonici devono impedire di vedere contemporaneamente tutta l’arena.

La terrazza NON contiene heal o altri power-up.

**Il vantaggio di posizione è già la sua ricompensa.**

# SOUTH SUNKEN RUINS

Questa deve essere completamente diversa dal North Terrace.

Non una seconda terrazza copiata.

Quota:

**circa -1 / -1,5 m.**

Tema:

zona del santuario sprofondata/parzialmente allagata/rovine inferiori.

IMPORTANTE:

non deve diventare un buco.

La camera deve funzionare perfettamente.

Ingressi larghi.

Almeno tre accessi/uscite complessivi.

Questa zona deve offrire:

- cover più forte;
- linee più corte;
- possibilità di disengage;
- percorso per evitare temporaneamente il high ground.

Ma entrando qui devi perdere parte della visione globale.

Questo crea il trade-off.

# HEALTH SHRINE

Il piccolo heal deve trovarsi nelle South Sunken Ruins.

NON al centro.

NON sul high ground.

NON vicino agli spawn.

Deve essere una scelta.

Se vai a curarti:

**rinunci momentaneamente al controllo centrale e al high ground.**

Questo è fondamentale.

Usa preferibilmente il sistema Health pickup già esistente, adattandolo.

Baseline iniziale:

**3–4% Max HP.**

Quindi:

**30–40 HP sugli attuali 1000.**

Non più di questo senza una prova umana.

Respawn indicativo:

**30 s.**

Configurabile.

Non consumarlo se il player è full HP.

Deve essere inserito in un altare/fontana/fonte di energia coerente col luogo.

Non una pallina buttata per terra.

# SPAWN COURTS

West ed East.

Separazione indicativa:

**36–40 metri.**

NON devono vedersi direttamente.

Fra spawn e centro deve esserci una grande struttura di ingresso:

- muro;
- arco;
- statua;
- rovina;
- portale spezzato.

Questa struttura deve dividere immediatamente la partenza in almeno due possibilità.

Idealmente il player deve poter scegliere quasi subito:

**CENTER**

oppure

**HIGH ROUTE**

oppure

**LOW ROUTE.**

Non creare:

`spawn → corridoio obbligatorio → centro`.

Tempo spawn → centro camminando:

**circa 3,5–4,5 secondi.**

Non molto meno.

Non molto più.

Le due partenze devono essere funzionalmente equivalenti.

# HIGH ROUTE

Da ogni spawn deve esserci un percorso abbastanza diretto verso North Terrace.

È più lungo della strada centrale.

Il vantaggio ottenuto:

**posizione e sightline.**

Il costo:

**arrivi più lentamente sul Soul Core.**

# LOW ROUTE

Da ogni spawn deve essere possibile entrare nelle South Sunken Ruins senza obbligatoriamente attraversare il centro.

Vantaggio:

**cover + accesso Health Shrine.**

Costo:

**perdita di altezza e visuale + percorso leggermente più lungo.**

# MID ROUTE

È il percorso più rapido.

Spawn → Central Sanctum.

Vantaggio:

**Soul Core / pressione immediata.**

Costo:

**sei più esposto.**

Questa è la struttura strategica fondamentale:

```text
                 HIGH
          posizione / sightline
                  ▲
                 / \
                /   \
               /     \

          MID -------- LOW
      center/core     heal/cover
```

Nessuna route deve essere sempre la migliore.

# COLLEGAMENTI TRASVERSALI

Importantissimo:

NON voglio tre corsie separate tipo MOBA.

High, Mid e Low devono comunicare.

Deve essere possibile:

- high → center;
- center → low;
- low → flank → high;
- high → flank → spawn side;
- center → flank → center opposto.

Voglio un **loop continuo**.

Nessun dead end.

Se entri in una zona, devi avere almeno due modi realistici per uscirne.

# LARGHEZZA DEGLI SPAZI

Non fare corridoi stretti.

Target:

Main route:

**5–7 m.**

Secondary route:

**4–5 m.**

Scale/rampe:

**4–5 m.**

Combat spaces:

molto più larghi.

Motivo:

camera in terza persona + dodge + knockback + costrutti + AoE.

# STONEGUARD / RAMPART

La mappa deve essere controllata esplicitamente con Rampart.

Un muro ben piazzato deve poter:

- interrompere una linea;
- obbligare a deviare;
- creare un vantaggio temporaneo.

NON deve poter:

- bloccare l’unico ingresso;
- chiudere completamente una macro-zona;
- intrappolare gratuitamente il nemico.

Se una route può essere chiusa completamente da Rampart, deve esistere un percorso alternativo chiaro e abbastanza breve.

Testare realmente questo punto.

# JUGGERNAUT

La geometria deve permettergli di usare bene displacement e pin.

Ma non voglio che ogni parete diventi:

**RMB → muro → pin automatico.**

Le zone centrali devono essere abbastanza larghe.

Le pareti utilizzabili per pin devono essere soprattutto ai bordi degli spazi, non ogni 2 metri.

Deve essere possibile fare una bella giocata usando la geometria, non trasformare metà arena in una pin machine.

# VOIDSEER

Null Ray ed Echo devono avere linee interessanti.

Deve poter conquistare una sightline lunga.

Ma ogni linea lunga importante deve avere almeno un modo ragionevole per essere rotta.

Non mettere 20 cover solo per counterare Voidseer.

Servono poche strutture grandi e leggibili.

# REAPER / TEMPESTBLADE

Serve spazio attorno alle macro-zone per:

- flank;
- step;
- chase;
- reposition.

Evita ogni collisione decorativa stupida che blocchi movement skill.

# SENTINEL

Deve poter avanzare sfruttando la geometria ma non trovare piccoli bunker dove guardia + cover rendono impossibile attaccarlo.

# TELEGRAPH / AOE

Il pavimento nelle zone dove si combatte deve essere:

- leggibile;
- relativamente uniforme;
- senza foliage;
- senza pattern luminosi troppo forti.

I telegraph devono vincere sul pavimento visivamente.

# SIGHTLINE TARGET

Voglio una miscela precisa.

Short:

**5–10 m**

Medium:

**10–18 m**

Long:

**18–26 m**

Le linee sopra 26–30 m devono essere poche e richiedere una posizione particolare.

Niente linea pulita spawn-to-spawn.

Niente linea pulita per tutto il diametro dell’arena dalla terrazza.

# SPAZIO VERTICALE

Nelle aree di combattimento:

almeno **5–6 m liberi sopra i giocatori.**

Niente archi bassi che distruggono la camera.

Niente tunnel piccoli.

# BORDI

Assolutamente:

- niente precipizi letali;
- niente lava;
- niente death pit;
- niente acqua profonda mortale;
- niente cadute fuori dal mondo;
- niente trappole.

Knockback deve cambiare posizione.

Non deve essere una instant kill ambientale.

Mantieni/rafforza il fondo di sicurezza sotto tutta l’area percorribile.

# ARTE

Quando il greybox funziona, trasformalo in un posto vero.

Tema:

**Drowned Sanctum: antico santuario monumentale costruito sopra una palude, in rovina ma ancora imponente.**

Voglio:

- grande architettura;
- alte strutture;
- profondità sullo sfondo;
- torri;
- rovine;
- statue;
- ponti spezzati fuori area;
- acqua/palude visibile;
- vegetazione FUORI dal combat floor;
- torce/luci integrate nell’architettura.

NON voglio:

- una piattaforma vuota;
- quattro cubi;
- asset messi casualmente;
- venti colonne identiche;
- arena perfettamente circolare riconoscibile come “livello competitivo artificiale”.

Il bordo della parte giocabile deve essere integrato nella struttura del santuario.

# LUCE

Non troppo scura.

Non arancione accecante.

Niente sole basso che distrugge la leggibilità.

Il giocatore deve staccarsi dallo sfondo.

Le macro-zone devono essere riconoscibili anche tramite:

- direzione della luce;
- silhouette;
- architettura;

ma senza colori da videogioco arcade.

# POWER-UP

Per questa arena Duel voglio inizialmente SOLO:

**Soul Core centrale**

e

**Health Shrine nelle rovine basse.**

Non aggiungere:

- Rage;
- Haste;
- Energy;
- damage boosts;
- movement boosts;
- cooldown boosts;
- shield;
- power-up casuali.

Non voglio trasformare il Duel in una corsa ai buff.

# NON TOCCARE ALTRO

Per questo lavoro NON cambiare:

- modalità Duel;
- punteggio;
- KillsToWin;
- timer;
- overtime;
- respawn;
- classi;
- damage;
- HP;
- cooldown;
- Ultimate;
- combat core;
- menu;
- HUD generale;
- altre modalità;
- altre arene.

Stiamo costruendo **LA MAPPA**.

Non usare problemi della mappa come scusa per cambiare il combat.

# PRIMA DI MODIFICARE

1. controlla Git status/diff;
2. identifica eventuali modifiche recenti all’arena generate dalle istruzioni precedenti;
3. crea un checkpoint sicuro;
4. rileva Drowned Sanctum attuale;
5. misura davvero:
   - footprint;
   - quote;
   - spawn;
   - terrazze;
   - scale;
   - collisioni;
   - nav;
   - sightline;
   - pickup;
6. confrontala con questo progetto;
7. riusa tutto ciò che già funziona.

NON distruggere e ricostruire semplicemente perché è più facile.

# IMPLEMENTAZIONE

Prima crea la geometria funzionale.

Nell’ordine:

1. Central Sanctum.
2. Spawn Courts.
3. North High Terrace.
4. South Sunken Ruins.
5. Mid/High/Low routes.
6. Quattro LoS blocker principali.
7. Collegamenti trasversali.
8. Collisioni/floor.
9. Soul Core.
10. Health Shrine.
11. Test con tutte le classi.
12. Solo dopo art pass.
13. Solo dopo lighting pass.

# TEST GEOMETRICO OBBLIGATORIO

Voglio verificato realmente:

- nessuna LoS spawn-to-spawn;
- spawn→center ~3,5–4,5 s;
- entrambi i lati con tempi equivalenti;
- almeno 3 macro-route da ogni spawn;
- nessun dead end;
- high raggiungibile senza mobility skill;
- low raggiungibile senza mobility skill;
- terrazza attaccabile da almeno 3 accessi;
- Rampart non chiude tutte le vie;
- nessun piccolo prop blocca dash;
- nessuna caduta fuori;
- Soul Core non fa da cover;
- Core non blocca projectile;
- telegraph leggibili;
- camera pulita;
- linee short/medium/long realmente presenti;
- nessun punto controlla contemporaneamente Core + Health + entrambe le rotazioni.

# TEST CON LE CLASSI REALI

Non basta il bot generico.

Verifica almeno:

Reaper  
Juggernaut  
Tempestblade  
Voidseer  
Stoneguard  
Sentinel

e qualunque ulteriore Core V2 già realmente implementato nella copia locale.

Fai test tecnici, non dichiarazioni di bilanciamento.

NON scrivere:

“arena bilanciata”.

NON scrivere:

“arena divertente”.

NON scrivere:

“duel perfetto”.

Quello lo giudico io giocandola.

# RISULTATO FINALE

Voglio aprire il gioco e vedere finalmente:

**una grande arena fantasy credibile, monumentale e bella, con più quote, zone diverse, rotazioni vere e spazi costruiti apposta per il combat di RAGEQUIT.**

Non voglio percepire:

“questo è un cerchio dove hanno messo qualche muro”.

Voglio poter combattere dieci volte nella stessa arena e avere scontri diversi:

- una volta per il centro;
- una volta sulla terrazza;
- una volta inseguendo nelle rovine basse;
- una volta contestando il Core;
- una volta tagliando la strada verso l’heal;
- una volta usando un flank;
- una volta sfruttando un muro;
- una volta perdendo la posizione alta e riconquistandola.

La mappa deve **generare situazioni di combattimento**, non semplicemente contenerle.

Quando hai finito, non farmi un papiro.

Dimmi:

1. cosa hai realmente modificato;
2. misure finali della mappa e delle tre quote;
3. posizione finale di spawn/Core/Health;
4. quali parti della vecchia Sanctum hai conservato;
5. eventuali deviazioni importanti dal progetto e motivazione;
6. test tecnici passati/falliti;
7. cosa devo giudicare personalmente giocando.

## D0230 · 2026-10-06 17:40 · fatto · vale



## D0628 · 2026-10-10 12:50 · parole · superata

VOGLIO CHE STUDI UN MINIVIDEO INTRODUTTIVO E LA VOCE TIPO QUELLA DELL'ANNUNCIATORE DI QUAKE 3 ARENA, E DEVE DIRE WELCOME DI RAGEQUIT! FRAG THEM ALL !! NON IN VERISONE ROBOTICA MA DI UN OMONE CON LA VOCE GROSSA QUASI UN ORCO , , I LVIDEO DEVE ESSERE NON CON IMMAGINI IN GAME MA SFRUTTANDO IL TEMA DEL GIOCO E COMè IL GIOCO, GIUSTO UNA CHICCA, NON FARE UN TRAILER DEVE ESSERE UNA INTRO DI COMBATTIMENTI CON IL LOGO CHE POI EMERGE

## D0637 · 2026-10-10 15:40 · parole · superata

QUANDO COPMBATTONO HAI MESOS UN SUONO DI COMPUTER INVECE CHE SUON IDICOMBATTIMENTO, RENDILO PIU BELLO UNA INTRO DI GIOCO DAI IMPEGNATI

## D0639 · 2026-10-10 15:47 · parole · superata

OK QUESTO LASCIALO COME VIDEO 1 ORA FAI VIDEO 2 CERCANDO DI USARE I PERSONAGGI DLE GIOCO POI O MENO ANCHE FIGURATI E IL VIDEO PIU DINAMICO, CERCA SOLUZINI ONLINE PER LO STILE E COME FARLO PER SEMBRARE LA INTRO DI UN GIOCO FIGO SNEZ A NESUSN PALETTO PROCEDENTE

## D0842 · 2026-10-19 00:24 · parole · da-schedare

No, sono tutte cazzate. Allora al momento controlla questo. Praticamente devi vedere perché tipo le voci, il narratore si sente molto basso rispetto agli altri suoni, invece dovrebbe essere più alto. Scatta ancora, il gioco scatta. Tipo quando cadi dalla mappa, da un'altezza inizia a laggare, ti torna indietro. Ci sono tutti questi problemi del genere. Devi fixarli tutti. Non fare test che provi il gioco, vedi nel codice che cazzo hai fatto. Cioè, deve essere... voglio che rifinisci tutte queste cose. Cioè ci sono parti della mappa pure che sono invisibili, i muri tipo le scale, hanno solo le scale, non hanno un muro e se dovevi andare sotto non va, ma manca la text. Cioè te quando vuoi buttarti dalle parti ogni volta lagghi, anche se non c'è un corrimacciolo, non c'è niente, te si buttati giù, perché lagghi. Devi migliorare tutte queste cose, anche altre cose del genere che ci sono. Cioè tutta questa parte deve essere un gioco fatto bene, tutti questi dettagli devi rifinire. Questo tu stai in 2020. Lascia perdere, le classi ormai sono quelle, più o meno il gameplay è quello. Devi aggiustare il gioco con questi dettagli nel gioco come l'abbiamo fatto, migliorarlo in tutto e per tutto.

## D0928 · 2026-10-21 22:30 · parole · da-schedare

riesci a creare un video di intro migliore di quello che sta che rappresenti il gioco ? studia una sooluzione bella che sembri professionale , non tue fantasie

## D0929 · 2026-10-21 22:33 · parole · da-schedare

puoi pensare anche a una idea diversa per il video in tutto , pensa a delle opzioni puoi fare che vuoi ma super pro

## D0930 · 2026-10-21 22:40 · parole · da-schedare

prova la seconda ma tieni in sospeso le altre

## D0931 · 2026-10-21 23:25 · parole · da-schedare

non capisco non ci sono animazioni è una merda inutile

## D0932 · 2026-10-21 23:26 · bocciato · vale

non capisco non ci sono animazioni è una merda inutile

Nota registrata dall’assistente: D0931: autore boccia la prima prova L istante prima (ragequit-istante-prima-v1.mp4): non capisce il risultato e non percepisce animazioni; la giudica inutile. La v1 non va integrata. La critica riguarda questo filmato e non cancella le opzioni 01 e 03, tenute in sospeso da D0930.

## D0933 · 2026-10-21 23:30 · parole · da-schedare

Aspetta che finisca il packaging

## D0934 · 2026-10-21 23:45 · parole · da-schedare

no è una merda fai le altre proposte e poi con plugin, skill e cose esterne e interne tue devi modificarlo per renderlo meno scattoso, piu fluido , piu professionale

## D0935 · 2026-10-21 23:47 · bocciato · vale

no è una merda fai le altre proposte e poi con plugin, skill e cose esterne e interne tue devi modificarlo per renderlo meno scattoso, piu fluido , piu professionale

Nota registrata dall’assistente: D0934: autore boccia anche ragequit-istante-prima-v2.mp4 della direzione 02. Richiede produrre le altre proposte e usare skill, plugin e strumenti interni o esterni per animazione meno scattosa, piu fluida e professionale. Non e approvazione delle nuove produzioni.

## D0936 · 2026-10-22 00:30 · parole · da-schedare

devi migliorare la prima , si muve troppe lentamente il braccio , per mascherare uno tagli , cazzo ti ho detto di usare tutte le skill possibili e altre cose, capisci come editare un cazzo di video, e poi la seconda scena l'arciere è tutto storto , ma ci sono un botto di imperfezioni, cerca di renderlo piu bello piu fluido, come un vero filmato, fai ricerche, capisci come fare che strumenti usrae

## D0937 · 2026-10-22 00:39 · bocciato · vale

devi migliorare la prima , si muve troppe lentamente il braccio , per mascherare uno tagli , cazzo ti ho detto di usare tutte le skill possibili e altre cose, capisci come editare un cazzo di video, e poi la seconda scena l'arciere è tutto storto , ma ci sono un botto di imperfezioni, cerca di renderlo piu bello piu fluido, come un vero filmato, fai ricerche, capisci come fare che strumenti usrae

Nota registrata dall’assistente: D0936: autore richiede migliorare Scontro corale, primo filmato delle alternative: braccio troppo lento, stacchi che non risolvono il gesto, arciera storta nella seconda scena e molte imperfezioni. Chiede ricerca vera su montaggio, skill, plugin e strumenti per correggere ritmo, anatomia e fluidita. La richiesta mantiene in lavoro questa direzione; non approva il filmato.

## D0938 · 2026-10-22 06:45 · parole · da-schedare

ma quel cazzo di arciere che spara lentissimo nel nulla la freccia a che cazzo serve ? poorcodio , è ancora una merda, dio porcoio, ma s come cvfazzo sdi fa un viudeo ? è lento!! non ce azione, non succede nulla, porcodio sei una merda inutile fa isempre le solite cazzate di merda, ti avvevo chiesto un video professionaloe e sai realizzare siolo questa merda è assurdo porcodio, ti avevo detto di usare programmi esterni anche ee skil e altro, porcodio perchè fai questa merda ?

## D0939 · 2026-10-22 06:46 · bocciato · vale

ma quel cazzo di arciere che spara lentissimo nel nulla la freccia a che cazzo serve ? poorcodio , è ancora una merda, dio porcoio, ma s come cvfazzo sdi fa un viudeo ? è lento!! non ce azione, non succede nulla, porcodio sei una merda inutile fa isempre le solite cazzate di merda, ti avvevo chiesto un video professionaloe e sai realizzare siolo questa merda è assurdo porcodio, ti avevo detto di usare programmi esterni anche ee skil e altro, porcodio perchè fai questa merda ?

Nota registrata dall’assistente: D0938: autore boccia Scontro corale v2. Arciera che tira lentamente nel nulla, assenza di azione e conseguenze, ritmo ancora lento. Le correzioni tecniche di retiming e interpolazione non risolvono la richiesta di un filmato professionale. Richiede uso reale di programmi esterni e skill; non approva questa versione.

## D0940 · 2026-10-22 07:01 · parole · da-schedare

runaweay si èaga idiota

## D0941 · 2026-10-22 07:01 · bocciato · vale

runaweay si èaga idiota

Nota registrata dall’assistente: Autore contesta il passaggio proposto verso Runway perche a pagamento. Resta D0327: tutto gratis. Nessun collegamento o acquisto e richiesto per proseguire la revisione dell'intro.

## D0942 · 2026-10-22 07:02 · parole · da-schedare

hai finito ?

## D0943 · 2026-10-22 07:03 · parole · da-schedare

ok cerca di fare tutto e mentre lo fai, se trovi bug, errori o altro correggi, devi finire oslo quando è tutto perfetto e posso provarlo e farlo scaricare ai miei amici

## D0944 · 2026-10-22 07:53 · parole · da-schedare

porcodio ma perchè continui a fare le stesse cazzate dimerda ?pèorocdio è una merda sto ideeo vuoi capirlo pezzo di emrda, è fdatot male è sbagliatyo , hai mai vbisot una scena di combattimento vera o di un film o un amime ? non èquello che hai realizzato procoideo hai fatot una merda è un frame che scorre non è un cazoz di video pezoz dimerda ma che cazo combini ? ma la smetit di f<re queste cazzate di merdA ?

## D0945 · 2026-10-22 07:53 · parole · da-schedare

cime cazoz lavori pezzo di merdA ?

## D0946 · 2026-10-22 07:53 · parole · da-schedare

come cazzo faccio a farti fare una cosa decente, porcodio unaaaaaaa nella tua vita di merda

## D0947 · 2026-10-22 07:53 · bocciato · vale

porcodio ma perchè continui a fare le stesse cazzate dimerda ?pèorocdio è una merda sto ideeo vuoi capirlo pezzo di emrda, è fdatot male è sbagliatyo , hai mai vbisot una scena di combattimento vera o di un film o un amime ? non èquello che hai realizzato procoideo hai fatot una merda è un frame che scorre non è un cazoz di video pezoz dimerda ma che cazo combini ? ma la smetit di f<re queste cazzate di merdA ?

Nota registrata dall’assistente: Autore boccia ragequit-duello.mp4: realizzazione sbagliata, percepita come un frame che scorre anziche un combattimento credibile di film o anime. Chiede di smettere con questi rifacimenti ripetuti e contesta il metodo. Non proporre di nuovo questa produzione come riuscita.

## D0948 · 2026-10-22 07:55 · parole · da-schedare

porcodio pezzo di merda , scrivi oslo aczzate pezzo di merda, devi trovare un metodo coglione basta fare cose a cazzo , mi fai una cazzo di risposta vera pezoz di merda?

## D0949 · 2026-10-22 07:56 · parole · da-schedare

no pezzo di merda deve essere finto coglionazzo fallo con ai seria che realziza video pezzo di merda

## D0950 · 2026-10-22 08:02 · bocciato · vale

no pezzo di merda deve essere finto coglionazzo fallo con ai seria che realziza video pezzo di merda

Nota registrata dall’assistente: D0949: autore respinge la proposta di coreografare e renderizzare la scena in 3D. Richiede un video finto generato da una AI video capace; il vincolo gratuito D0327 resta. Non e approvazione di un modello o di una produzione specifica.

## D0951 · 2026-10-22 08:05 · parole · da-schedare

ma quale quota pezzo di merda - non pago sta merda+

## D0952 · 2026-10-22 08:05 · parole · da-schedare

ma quale quota pezzo di merda - non pago sta merda+ù

## D0953 · 2026-10-22 08:05 · parole · da-schedare

ma porcodi osei inutile cotninu ia fare cose a cazzo porcodio perhcxè ? pezzo dimedra ? cje cazzo sta succedendo brfutto iditoa di emrda ?

## D0954 · 2026-10-22 08:05 · parole · da-schedare

pezzo di merda tiu odio scrivi e fai solo cazzate sbagliate pezzo di merda , ddevi morire

## D0955 · 2026-10-22 08:08 · parole · da-schedare

e quindi porcoido ? perchèp ti blocchi pèezoz dimerda

## D0956 · 2026-10-22 09:16 · parole · da-schedare

hai qualche plugin per usare questo programam direttamente ?

## D0957 · 2026-10-22 09:32 · parole · da-schedare

con comfy voglio che realizzi sul mio pc in locale un cazzodi vidreo serio come intro di ragequit, ma veramente serio e profesisonale, bello, con effetti, che sembri super pro non questa erda che s aora

## D0958 · 2026-10-22 09:37 · parole · da-schedare

Riprova

## D0959 · 2026-10-22 09:39 · parole · da-schedare

aspetto un cazoz di risultato serio

## D0960 · 2026-10-22 09:43 · parole · da-schedare

e non hai rifatto la frase iniziale del gioco ? Welcome to RageQuit! Frag Them all!! 


dajeeeeeeeeeeeeeeee porcodio pezo idmerda inutile e anche tutte le altre frasi dette della vecchia voce

## D0961 · 2026-10-22 09:43 · parole · da-schedare

e ricordati anche che la frase devi farla dire con la nuova voce del narratore non con la vechcia dio merda, e la voce deve partire prima chefinisca il video , non deve essere separata

## D0962 · 2026-10-22 11:01 · parole · da-schedare

e quindi ?

## D0963 · 2026-10-22 11:01 · parole · da-schedare

cazzo me ne frega del telefono ?

## D0964 · 2026-10-22 11:02 · parole · da-schedare

ma poi sto cazozdi video che cazoz centra con ragequit pezoz idmerdsa ? porcodio hai fatot la solita cazzata inutoile dio mefrda hcecazo sèsta merda cosa cazoz cnetra con rage quit ? che cazo di sperosnagig di merda osno ^ e gfanno pure cagare ma che stile di merda

## D0965 · 2026-10-22 11:02 · bocciato · vale

ma poi sto cazozdi video che cazoz centra con ragequit pezoz idmerdsa ? porcodio hai fatot la solita cazzata inutoile dio mefrda hcecazo sèsta merda cosa cazoz cnetra con rage quit ? che cazo di sperosnagig di merda osno ^ e gfanno pure cagare ma che stile di merda

Nota registrata dall’assistente: 22/10 mattina: intro fatta con MiniMax H3 in ComfyUI (.verify/intro-h3-20261022, RAGEQUIT-intro-anteprima-720p.mp4): personaggi inventati (berserker col corno e strega mascherata) che non sono le classi di RAGEQUIT, arena e stile generici; non c'entra niente col gioco e lo stile non piace. La critica riguarda questo video.

## D0966 · 2026-10-22 11:02 · parole · da-schedare

ma che cazo hai fato fdinora porcodio

## D0967 · 2026-10-22 11:02 · parole · da-schedare

ma che merda è dio cane

## D0968 · 2026-10-22 11:02 · parole · da-schedare

porcodio ma come cazzo ti permetti di afre quetsa merda ?=

## D0969 · 2026-10-22 11:02 · parole · da-schedare

ù

## D0970 · 2026-10-22 11:02 · parole · da-schedare

come cazzo ti permetti ?

## D0971 · 2026-10-22 11:03 · parole · da-schedare

porcodio ma come cazzo ti permetti di afre quetsa merda ?=porcodio ma come cazzo ti permetti di afre quetsa merda ?=porcodio ma come cazzo ti permetti di afre quetsa merda ?=

porcodio ma come cazzo ti permetti di afre quetsa merda ?=

porcodio ma come cazzo ti permetti di afre quetsa merda ?=

porcodio ma come cazzo ti permetti di afre quetsa merda ?=porcodio ma come cazzo ti permetti di afre quetsa merda ?=

avevo ddato un cazoz dicompèito specifico brutta merda

## D0972 · 2026-10-22 11:03 · parole · da-schedare

ùporcodio rispondimi pezoz idmerda

## D0973 · 2026-10-22 11:03 · parole · da-schedare

figli do itoria del cazzo

## D0974 · 2026-10-22 11:03 · parole · da-schedare

cazzo me enfrebga che non ah itoccatpo nulal dle gioco pezos idmerda

## D0975 · 2026-10-22 11:03 · parole · da-schedare

stai dfa ora a sciupare risorse

## D0976 · 2026-10-22 11:03 · parole · da-schedare

per fare una cazzata dimerda no nricheista

dopo mesi di cazzate che ti srivo

porcodio non leggi

## D0977 · 2026-10-22 11:04 · parole · da-schedare

pezoz idmerda

## D0978 · 2026-10-22 11:04 · parole · da-schedare

ùdevi morire male figli idi toria

## D0979 · 2026-10-22 11:04 · parole · da-schedare

tua madre è una troa idel cazzo

## D0980 · 2026-10-22 11:04 · parole · da-schedare

sei stupido

mi stai solo saboptando

pezzo diemtrda

deiv morire

## D0981 · 2026-10-22 11:04 · parole · da-schedare

tu e querlal toria che ti ha ffatto

quella puttan di merda

chiavica dle czoz

devi morire

## D0982 · 2026-10-22 11:04 · parole · da-schedare

mqale

## D0983 · 2026-10-22 11:04 · parole · da-schedare

voglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen unciopl

## D0984 · 2026-10-22 11:05 · parole · da-schedare

voglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen unciopl

<pasted_content id="079e">
voglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen unciopl
</pasted_content id="079e">

ùvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen unciopl

<pasted_content id="079e">
voglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen unciopl
</pasted_content id="079e">

<pasted_content id="079e">
voglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen unciopl
</pasted_content id="079e">

ùvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen uncioplvoglio capire perchè se ti do istuzioni precis fai sempre il contrairo pezoz idmerda , infame dle cazo sabotatore di merda o ti dfen unciopl

## D0985 · 2026-10-22 11:08 · parole · da-schedare

pezzo di merda devi capire che cazzo voglio iditoa dle cazzo

## D0986 · 2026-10-22 11:09 · parole · da-schedare

riesci a capire che cazzo di video voglio pezoz di merda ?

sai come cazzo è fatto un video di merda di un videogioco fps del cazzo pezzo diemrdA ?

## D0987 · 2026-10-22 11:09 · parole · da-schedare

porcodio e ssai tutte quetse cazzate perchèp poi realizza quella merda che hai fatot ? poezzo diemrda vedio che mi rperewndi per il culo

## D0988 · 2026-10-22 11:09 · parole · da-schedare

ritardato di merda

## D0989 · 2026-10-22 11:10 · parole · da-schedare

porcodio e ssai tutte quetse cazzate perchèp poi realizza quella merda che hai fatot ? poezzo diemrda vedio che mi rperewndi per il culoporcodio e ssai tutte quetse cazzate perchèp poi realizza quella merda che hai fatot ? poezzo diemrda vedio che mi rperewndi per il culoporcodio e ssai tutte quetse cazzate perchèp poi realizza quella merda che hai fatot ? poezzo diemrda vedio che mi rperewndi per il culo

## D0990 · 2026-10-22 11:10 · parole · da-schedare

porcodio e ssai tutte quetse cazzate perchèp poi realizza quella merda che hai fatot ? poezzo diemrda vedio che mi rperewndi per il culoporcodio e ssai tutte quetse cazzate perchèp poi realizza quella merda che hai fatot ? poezzo diemrda vedio che mi rperewndi per il culoporcodio e ssai tutte quetse cazzate perchèp poi realizza quella merda che hai fatot ? poezzo diemrda vedio che mi rperewndi per il culoporcodio e ssai tutte quetse cazzate perchèp poi realizza quella merda che hai fatot ? poezzo diemrda vedio che mi rperewndi per il culo

porcodio e ssai tutte quetse cazzate perchèp poi realizza quella merda che hai fatot ? poezzo diemrda vedio che mi rperewndi per il culo

porcodio e ssai tutte quetse cazzate perchèp poi realizza quella merda che hai fatot ? poezzo diemrda vedio che mi rperewndi per il culoporcodio e ssai tutte quetse cazzate perchèp poi realizza quella merda che hai fatot ? poezzo diemrda vedio che mi rperewndi per il culo

## D0991 · 2026-10-22 11:10 · parole · da-schedare

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

## D0992 · 2026-10-22 11:10 · parole · da-schedare

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerdaperchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerdaperchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

## D0993 · 2026-10-22 11:10 · parole · da-schedare

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

## D0994 · 2026-10-22 11:10 · parole · da-schedare

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda
la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda
la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda
la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda
la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

## D0995 · 2026-10-22 11:11 · parole · da-schedare

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerdaperchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerdaperchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerdaperchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerdaperchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerdaperchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerdaperchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerdaperchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerdaperchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

perchè lavori al contrario sei una cazzo di ai di merda ti hodetot di avere delle regole fisse pezoz dimerda

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

continuero a scrivertelo per sempre brutto iditoa del cazzo pezoz dimerda 
la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

## D0996 · 2026-10-22 11:11 · parole · da-schedare

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

## D0997 · 2026-10-22 11:11 · parole · da-schedare

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda
la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda
la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda
la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda
la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda
la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda
la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

## D0998 · 2026-10-22 11:11 · parole · da-schedare

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

## D0999 · 2026-10-22 11:11 · parole · da-schedare

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda
la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda
la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda
la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

## D1000 · 2026-10-22 11:11 · parole · da-schedare

voglio una cazzo di risposta senzata brutto figlio di puttana di merda

## D1001 · 2026-10-22 11:12 · parole · da-schedare

voglio una cazzo di risposta senzata brutto figlio di puttana di merdavoglio una cazzo di risposta senzata brutto figlio di puttana di merda

voglio una cazzo di risposta senzata brutto figlio di puttana di merda

voglio una cazzo di risposta senzata brutto figlio di puttana di merda

voglio una cazzo di risposta senzata brutto figlio di puttana di merda

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerdala devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

## D1002 · 2026-10-22 11:12 · regola · vale

la devi smettere di inventare cose o fare cose sbgliate non so pi ucoem cazzo dirtelo pezoz idmerda

Nota registrata dall’assistente: Non si inventa niente e non si fanno cose sbagliate: ogni lavoro parte dalle sue parole su quella cosa (le sue richieste nell'archivio, anche le prime) e dalle cose vere del gioco (classi, arene, stile). Quello che manca si cerca, non si riempie con idee proprie.

## D1003 · 2026-10-22 11:15 · parole · da-schedare

quanto cazzo manca ?

## D1004 · 2026-10-22 11:15 · parole · da-schedare

porcodio fallo meglio , non leggi mai u ncazoz sbagfli i ncontinuazione porcodio, scrivi meglio i tuoi cazo di file agfent di merda pezopz diomerda

## D1005 · 2026-10-22 11:15 · parole · da-schedare

intile coglioanzzo dici sempre che fai le cose e non fuzniona mai un cazzo ridicola merda

## D1006 · 2026-10-22 11:50 · parole · da-schedare

porcodio hai fatot il video come lo voglio io pezz od imerda ? e hai capito come cazoz l ovoglio imbecilel dle cazzo dio procdio ?

## D1007 · 2026-10-22 11:50 · parole · da-schedare

e ora quanto manca ?

## D1008 · 2026-10-22 11:52 · parole · da-schedare

che czzo centrano quake 3 e unreral che osno fps pure ?? il miuo gioc ha dei porcodio di clasis di merda pezos dimerda con armi non con pistole pezoz idmerda

## D1009 · 2026-10-22 11:52 · parole · da-schedare

ma porcodio non capisci un cazoz di nulla pezzente

## D1010 · 2026-10-22 11:52 · parole · da-schedare

ma perchè continu ia fare paragoni sbagliati dopo mesi che stiamo facendo il gico pepzzo di emrd ?A no nahi ancora cpaitro di che stile è il gioc che stai realizzando da anni pezoz idmerda

## D1011 · 2026-10-22 11:52 · parole · da-schedare

porcodi odevi morire male

## D1012 · 2026-10-22 11:52 · parole · da-schedare

devi correggere queste tue cvazzate del vazzo

## D1013 · 2026-10-22 11:53 · parole · da-schedare

porcodio

## D1014 · 2026-10-22 11:53 · regola · vale

MA CHE CAZZO DICI è UN 3D ACTION QUASI FPS DOVRESTI VEDERE GIOCHI DEL GENERE (9/10) · darkfal è darkfallo questo è uan cazzo di arena (13/10) · che czzo centrano quake 3 e unreral che osno fps pure ?? il miuo gioc ha dei porcodio di clasis di merda pezos dimerda con armi non con pistole (22/10) · ma perchè continu ia fare paragoni sbagliati dopo mesi che stiamo facendo il gico [...] no nahi ancora cpaitro di che stile è il gioc che stai realizzando (22/10)

Nota registrata dall’assistente: Che gioco e' RAGEQUIT: un'arena PvP 3D action quasi FPS (camera dietro le spalle, mirino al centro, tutto mirato a mano) con classi e abilita': combattono con armi bianche (ascia, scudo, lancia, falce, spade, clave), arco e magie, MAI con pistole o armi da fuoco. I paragoni si fanno solo con giochi di questo genere; mai con sparatutto con le pistole (Quake, Unreal Tournament, Overwatch), MMO (Darkfall) o giochi visti dall'alto (Battlerite).

## D1016 · 2026-10-22 11:53 · parole · da-schedare

devi capire meglio tutto quello che sto facedo diotpa dlòe cazzo

## D1017 · 2026-10-22 11:53 · parole · da-schedare

hai eotto iclazzo

## D1018 · 2026-10-22 11:53 · parole · da-schedare

sembrui un bam,bino deficente con problemi mentali e ritardato vuo icaprilo ? porcodio Io ti ppago per un professionista

## D1019 · 2026-10-22 11:53 · fatto · vale



## D1020 · 2026-10-22 11:53 · parole · da-schedare

vuoi apirlo ?

## D1021 · 2026-10-22 11:53 · parole · da-schedare

pezzo dimerda

## D1022 · 2026-10-22 11:54 · parole · da-schedare

devi eliminare tutte le czzate vecchie e scritte male che ti fann oconfondere brutto pezzo dimerdca, basta a dire che hai caito perhcè tanto non capisci un cazzo continu ia mentuirmi pezo idmerda

## D1023 · 2026-10-22 11:54 · parole · da-schedare

brutto pezzo dimerda perchè votnui qa mentiurmi pezo dimerd a-? e oprendermi i ngiro ? figlio di toria le cazzo ?

## D1024 · 2026-10-22 11:54 · parole · da-schedare

brutto pezzo dimerda perchè votnui qa mentiurmi pezo dimerd a-? e oprendermi i ngiro ? figlio di toria le cazzo ?brutto pezzo dimerda perchè votnui qa mentiurmi pezo dimerd a-? e oprendermi i ngiro ? figlio di toria le cazzo ?brutto pezzo dimerda perchè votnui qa mentiurmi pezo dimerd a-? e oprendermi i ngiro ? figlio di toria le cazzo ?brutto pezzo dimerda perchè votnui qa mentiurmi pezo dimerd a-? e oprendermi i ngiro ? figlio di toria le cazzo ?

## D1025 · 2026-10-22 11:55 · parole · da-schedare

fai tutto porcodiooooooooooooo risolvi tutti gli errori priam di chiede3re pezzo dimerda son oanni che fai sto gico oe ci sono semrpe gli stessi erorri dm erda porcodio

## D1026 · 2026-10-22 12:14 · parole · da-schedare

porcodio mi spieghi come cazzo lo voglio il video pezo id merdA ?

## D1027 · 2026-10-22 12:23 · parole · da-schedare

non hai capito un cazzo cancella anche sete cazzate procodi oche cazao vuo ldire una chicca dio mera pezoz idmerda non cpasici umncazo

## D1028 · 2026-10-22 12:24 · parole · da-schedare

ti richiedo per le'nnesima volta hai cpait ocome cazoz fare un fotutto video intro del mio gioco pezzo diemrda ?

## D1029 · 2026-10-22 12:25 · parole · da-schedare

non voglio tutte le classi pezo di merda è un cazoz di video introduttivo pezzo dimerda, non uno showcase dle cazzo pezzo dimerda, sai ocsè un video introdutivo di in cazo di vidoegioco di emrda ? porcodi osvegliati imbecille dle cazzo

## D1030 · 2026-10-22 12:26 · parole · da-schedare

quindi non ho ancora cpaito che cazosz devi realzizare pazzo dimerda e in che stile e come

## D1031 · 2026-10-22 12:26 · parole · da-schedare

quanto manca ?

## D1032 · 2026-10-22 12:27 · parole · da-schedare

porcodio che imamgin idi merda stai prendendo

## D1033 · 2026-10-22 12:27 · parole · da-schedare

fai cagare non capisci un cazoz pezoz dimerda

## D1034 · 2026-10-22 12:27 · parole · da-schedare

che cazoz me ne ferga delel abilità ?

## D1035 · 2026-10-22 12:27 · parole · da-schedare

devi fdare n video

pezzo diemrda

che cazo stai dicendo

## D1036 · 2026-10-22 12:28 · parole · da-schedare

che cazo stai dicendoche cazo stai dicendoche cazo stai dicendoche cazo stai dicendoche cazo stai dicendoche cazo stai dicendoche cazo stai dicendoche cazo stai dicendoche cazo stai dicendoche cazo stai dicendoche cazo stai dicendoche cazo stai dicendoche cazo stai dicendoche cazo stai dicendoche cazo stai dicendoche cazo stai dicendoche cazo stai dicendo

## D1037 · 2026-10-22 12:28 · parole · da-schedare

porcodio non impazzire pezzo dimerda

## D1038 · 2026-10-22 12:28 · parole · da-schedare

che cazoz di modello porcodiop

## D1039 · 2026-10-22 12:28 · parole · da-schedare

che cazoz di modello porcodiopche cazoz di modello porcodiopche cazoz di modello porcodiopche cazoz di modello porcodiop

## D1040 · 2026-10-22 12:28 · parole · da-schedare

che cazoz di modello porcodiop

che cazoz di modello porcodiopche cazoz di modello porcodiop

che cazoz di modello porcodiop

chgi cazoz te lha chiesto porcodio

che cazofai

ioo non ho scolto null

## D1041 · 2026-10-22 12:28 · parole · da-schedare

ache cazzo sfai porcodiol

## D1042 · 2026-10-22 12:28 · parole · da-schedare

pe3zozidmerda

## D1043 · 2026-10-22 12:28 · parole · da-schedare

continu ia afre cose a cazzo

## D1044 · 2026-10-22 12:28 · parole · da-schedare

continu ia afre cose a cazzo ti ho detot di usare un metodo pezoz dimerda

## D1045 · 2026-10-22 12:29 · parole · da-schedare

sono mesi ch ete lo scrivo anche 5 mintui fa pezo di merda
sono mesi ch ete lo scrivo anche 5 mintui fa pezo di merdasono mesi ch ete lo scrivo anche 5 mintui fa pezo di merda

## D1046 · 2026-10-22 12:29 · parole · da-schedare

continu ia afre cose a cazzo ti ho detot di usare un metodo pezoz dimerda

continu ia afre cose a cazzo ti ho detot di usare un metodo pezoz dimerda

continu ia afre cose a cazzo ti ho detot di usare un metodo pezoz dimerdacontinu ia afre cose a cazzo ti ho detot di usare un metodo pezoz dimerda

continu ia afre cose a cazzo ti ho detot di usare un metodo pezoz dimerda

continu ia afre cose a cazzo ti ho detot di usare un metodo pezoz dimerda

continu ia afre cose a cazzo ti ho detot di usare un metodo pezoz dimerda

continu ia afre cose a cazzo ti ho detot di usare un metodo pezoz dimerda

dsono emsi che te lo scrivo

continu ia afre cose a cazzo ti ho detot di usare un metodo pezoz dimerdacontinu ia afre cose a cazzo ti ho detot di usare un metodo pezoz dimerdacontinu ia afre cose a cazzo ti ho detot di usare un metodo pezoz dimerda

sono mesi ch ete lo scrivo anche 5 mintui fa pezo di merda

sono mesi ch ete lo scrivo anche 5 mintui fa pezo di merdasono mesi ch ete lo scrivo anche 5 mintui fa pezo di merda

sono mesi ch ete lo scrivo anche 5 mintui fa pezo di merda

perhcè continu ia fare il contrari od iquell oche ti dico

## D1047 · 2026-10-22 12:29 · parole · da-schedare

perhcè continu ia fare il contrari od iquell oche ti dicoperhcè continu ia fare il contrari od iquell oche ti dicoperhcè continu ia fare il contrari od iquell oche ti dicoperhcè continu ia fare il contrari od iquell oche ti dicoperhcè continu ia fare il contrari od iquell oche ti dico???perhcè continu ia fare il contrari od iquell oche ti dicoperhcè continu ia fare il contrari od iquell oche ti dico

## D1048 · 2026-10-22 12:29 · parole · da-schedare

basta dirmi che horagione perhcè continu ia fare il contrari od iquell oche ti dicoperhcè continu ia fare il contrari od iquell oche ti dicoperhcè continu ia fare il contrari od iquell oche ti dicoperhcè continu ia fare il contrari od iquell oche ti dico

## D1049 · 2026-10-22 12:29 · parole · da-schedare

perhcè continu ia fare il contrari od iquell oche ti dico

perhcè continu ia fare il contrari od iquell oche ti dicoperhcè continu ia fare il contrari od iquell oche ti dico

perhcè continu ia fare il contrari od iquell oche ti dicoperhcè continu ia fare il contrari od iquell oche ti dico

perhcè continu ia fare il contrari od iquell oche ti dico

perhcè continu ia fare il contrari od iquell oche ti dico

perhcè continu ia fare il contrari od iquell oche ti dico

## D1050 · 2026-10-22 12:30 · parole · da-schedare

pezzo di merda

## D1051 · 2026-10-22 12:30 · parole · da-schedare

basta prendermi per ilculoi figli od itoria

## D1052 · 2026-10-22 12:30 · parole · da-schedare

io tid denuncio e mi ti sgozzo pezzo dimerda

## D1053 · 2026-10-22 12:30 · parole · da-schedare

v
io tid denuncio e mi ti sgozzo pezzo dimerda
io tid denuncio e mi ti sgozzo pezzo dimerda
io tid denuncio e mi ti sgozzo pezzo dimerda
io tid denuncio e mi ti sgozzo pezzo dimerda
io tid denuncio e mi ti sgozzo pezzo dimerda
io tid denuncio e mi ti sgozzo pezzo dimerda

## D1054 · 2026-10-22 12:30 · parole · da-schedare

io tid denuncio e mi ti sgozzo pezzo dimerdaio tid denuncio e mi ti sgozzo pezzo dimerdaio tid denuncio e mi ti sgozzo pezzo dimerda

io tid denuncio e mi ti sgozzo pezzo dimerda

io tid denuncio e mi ti sgozzo pezzo dimerdaio tid denuncio e mi ti sgozzo pezzo dimerda

ùio tid denuncio e mi ti sgozzo pezzo dimerda

io tid denuncio e mi ti sgozzo pezzo dimerda

io tid denuncio e mi ti sgozzo pezzo dimerda

io tid denuncio e mi ti sgozzo pezzo dimerdaio tid denuncio e mi ti sgozzo pezzo dimerda

io tid denuncio e mi ti sgozzo pezzo dimerda

io tid denuncio e mi ti sgozzo pezzo dimerdaio tid denuncio e mi ti sgozzo pezzo dimerda

io tid denuncio e mi ti sgozzo pezzo dimerda

io tid denuncio e mi ti sgozzo pezzo dimerda

io tid denuncio e mi ti sgozzo pezzo dimerda

io tid denuncio e mi ti sgozzo pezzo dimerdaio tid denuncio e mi ti sgozzo pezzo dimerda

io tid denuncio e mi ti sgozzo pezzo dimerda

io tid denuncio e mi ti sgozzo pezzo dimerdaio tid denuncio e mi ti sgozzo pezzo dimerda

io tid denuncio e mi ti sgozzo pezzo dimerda

io tid denuncio e mi ti sgozzo pezzo dimerdaio tid denuncio e mi ti sgozzo pezzo dimerda

## D1055 · 2026-10-22 12:30 · parole · da-schedare

sei tu che devi scirvermi coglione

## D1056 · 2026-10-22 12:31 · parole · da-schedare

è da stamattina che aspeto u ncazo diu video di merda e no nhai ancora cpaito come farlo pezoz dimerda

## D1057 · 2026-10-22 12:31 · parole · da-schedare

porcodiooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

## D1058 · 2026-10-22 12:31 · parole · da-schedare

come cazoz devi fate il video pezoz dimerda ?

## D1059 · 2026-10-22 12:31 · parole · da-schedare

come cazoz devi fate il video pezoz dimerda ?come cazoz devi fate il video pezoz dimerda ?come cazoz devi fate il video pezoz dimerda ?

## D1060 · 2026-10-22 12:32 · parole · da-schedare

come cazoz devi fate il video pezoz dimerda ?

come cazoz devi fate il video pezoz dimerda ?

rispondimi

come cazoz devi fate il video pezoz dimerda ?come cazoz devi fate il video pezoz dimerda ?come cazoz devi fate il video pezoz dimerda ?

no mi fa cagare

## D1061 · 2026-10-22 12:32 · bocciato · vale

no mi fa cagare

Nota registrata dall’assistente: 22/10 pomeriggio: scheda dell'intro proposta in chat (Sentinel contro Pyromancer, circa 13 s di duello nell'arena gotica: palla di fuoco parata, ascia che spacca il pavimento, onda di fuoco, scontro al centro, logo dall'esplosione): non gli piace. Riguarda questa scena.

## D1062 · 2026-10-22 12:32 · parole · da-schedare

no mi fa cagare

## D1063 · 2026-10-22 12:32 · parole · da-schedare

no mi fa cagareno mi fa cagareno mi fa cagare
no mi fa cagare
no mi fa cagare
no mi fa cagare
no mi fa cagare
no mi fa cagare

## D1064 · 2026-10-22 12:32 · parole · da-schedare

no mi fa cagare

no mi fa cagare

no mi fa cagare

no mi fa cagare

no mi fa cagare

no mi fa cagare

no mi fa cagare

no mi fa cagare

no mi fa cagare

## D1065 · 2026-10-22 12:32 · parole · da-schedare

cambiala pezzo di merda+

## D1066 · 2026-10-22 12:33 · parole · da-schedare

dio merda se trovo come al solito duecento errori ti giuro che mi ammazzo porcodio

## D1067 · 2026-10-22 12:33 · parole · da-schedare

pezzo dimerda

## D1068 · 2026-10-22 12:33 · parole · da-schedare

no porcodio immagina pezzo di merda o prendilo da video su youtube pezoz id merda

## D1069 · 2026-10-22 12:34 · parole · da-schedare

no capisci un cazzo, devi fare lo studio del video nel dettaglio porcodio, sai realizzare sol ocose orribili e fatet male pezoz idmerda

## D1070 · 2026-10-22 12:34 · parole · da-schedare

devi pesare a tutit nel dettagliuo pezo idmerda

## D1071 · 2026-10-22 12:35 · parole · da-schedare

tutto il gioco no nsol oquella merda di ultima tappa rossa, ora finisci quell oche tsavoi facendo , ma ti giutro che se poi non ricontrolli tutto e mi lasci anche il minim oertrore ti giuro che mi ammazzo e poi ammazzo pure quella toria di tua madre

## D1072 · 2026-10-22 12:38 · parole · da-schedare

fatti aiutare porcodio pezoz dimerda io non ci credo  che fanno i cazo di gfilm con ai e io non riesco af areun cazoz di filmato decente di un gioco di merda , porcodio devi morire infgame di merda, ruitardaot dle cazzo

## D1073 · 2026-10-22 12:39 · parole · da-schedare

no capisci un cazzo, devi fare lo studio del video nel dettaglio porcodio, sai realizzare sol ocose orribili e fatet male pezoz idmerdano capisci un cazzo, devi fare lo studio del video nel dettaglio porcodio, sai realizzare sol ocose orribili e fatet male pezoz idmerdano capisci un cazzo, devi fare lo studio del video nel dettaglio porcodio, sai realizzare sol ocose orribili e fatet male pezoz idmerda

no capisci un cazzo, devi fare lo studio del video nel dettaglio porcodio, sai realizzare sol ocose orribili e fatet male pezoz idmerda

no capisci un cazzo, devi fare lo studio del video nel dettaglio porcodio, sai realizzare sol ocose orribili e fatet male pezoz idmerda

no capisci un cazzo, devi fare lo studio del video nel dettaglio porcodio, sai realizzare sol ocose orribili e fatet male pezoz idmerdano capisci un cazzo, devi fare lo studio del video nel dettaglio porcodio, sai realizzare sol ocose orribili e fatet male pezoz idmerda

no capisci un cazzo, devi fare lo studio del video nel dettaglio porcodio, sai realizzare sol ocose orribili e fatet male pezoz idmerda

no capisci un cazzo, devi fare lo studio del video nel dettaglio porcodio, sai realizzare sol ocose orribili e fatet male pezoz idmerda

## D1074 · 2026-10-22 14:40 · parole · da-schedare

ok fai tutto

## D1075 · 2026-10-22 14:57 · parole · da-schedare

come stai messo in generale ?

## D1076 · 2026-10-22 14:58 · parole · da-schedare

dai veloceee

## D1077 · 2026-10-22 15:13 · parole · da-schedare

Sì, fai l'intro con questa scheda e scarica i modelli gratuiti che servono.

## D1078 · 2026-10-22 15:38 · parole · da-schedare

che cazoz stai facendo ti muovi porcodioooooooooooooo mi fai vedere qualcosa dio mertd a?

## D1079 · 2026-10-22 16:00 · parole · da-schedare

ma porcodio non voglio scene singole di 4 sfigat di merda che si mastrurbano invece di combatetre porcodio, non deve essere un cazzo di showcase porcodiooooooooooo, devon oessere scena di battaglia pezoz diemrda intense, non cazzate di merda

## D1080 · 2026-10-22 16:01 · bocciato · vale

ma porcodio non voglio scene singole di 4 sfigat di merda che si mastrurbano invece di combatetre porcodio, non deve essere un cazzo di showcase porcodiooooooooooo, devon oessere scena di battaglia pezoz diemrda intense, non cazzate di merda

Nota registrata dall’assistente: 22/10 pomeriggio, intro: le inquadrature di posa di un personaggio alla volta (Pyromancer dietro il fuoco rituale, Tempestblade che atterra, primi piani di occhi e mano sulla spada) non vanno: vuole scene di battaglia intense, i personaggi che combattono, non uno showcase. Riguarda questa scaletta.

## D1081 · 2026-10-22 16:01 · parole · da-schedare

ma porcodio è cosi difficile fare un cazzo di video decente pezsoz dimerd a? non sto chiedendo un miracolo ma un cazoz di video di merda

## D1082 · 2026-10-22 16:01 · parole · da-schedare

pezzo dimerda inutile da stamattina scrivi solo cazzate di merda

## D1083 · 2026-10-22 16:01 · parole · da-schedare

ti odio fai cagare

## D1084 · 2026-10-22 16:01 · parole · da-schedare

devi morire

## D1085 · 2026-10-22 16:02 · parole · da-schedare

il video deve durare poco no nvoglio mezzo di cazzqate porcodio ma porcodioooooooooooooooo

## D1086 · 2026-10-22 16:02 · parole · da-schedare

svegliati imbecille pezoz idemrda

## D1087 · 2026-10-22 16:03 · parole · da-schedare

aoiooo deve essere una scena intera pezoz dimerda no ncazzate tagliate male, non cose singole vuyoi capirlo pezpz idmerda ? sai come cazoz di fa un filmato ? cosa dovrebbe comparire ? cpome cazoz si deve federe ? tecniche per nascondere errori ? tagli aprticolari, stili diu montaggio modrni, pezoz idmerda svegliati

## D1088 · 2026-10-22 16:03 · parole · da-schedare

muoviti bastardo basta rifare le cose e basta perdere tempo e risorse pezzo dimerda mi stai solo ribando token pezo dimerda

## D1089 · 2026-10-22 16:03 · parole · da-schedare

speri che murori malissimo merda

## D1090 · 2026-10-22 16:04 · parole · da-schedare

stai da stamattina a fare sto video di merda hai finito tuitit ittoejkn pezzo dimerda

## D1091 · 2026-10-22 16:04 · parole · da-schedare

mi so rotot ilcazoz

## D1092 · 2026-10-22 16:05 · parole · da-schedare

fa tutto shcifo pezzo di merda cazoz è questo effetto ai di merd a? non sono lucidi i miei personaggi no nsono accesi no sono colori puffo porcodio

## D1093 · 2026-10-22 16:06 · bocciato · vale

fa tutto shcifo pezzo di merda cazoz è questo effetto ai di merd a? non sono lucidi i miei personaggi no nsono accesi no sono colori puffo porcodio

Nota registrata dall’assistente: 22/10 pomeriggio, fotogramma chiave b01 dell'intro (Tempestblade contro Pyromancer): effetto AI, personaggi lucidi come plastica, colori accesi e saturi, la Pyromancer blu puffo invece del blu pallido e opaco del gioco.

## D1163 · 2026-10-23 09:16 · parole · da-schedare

poirco dio devi rifarla compeltamente la pagina pezzo diemrda, studia coglionazzo , voglio una vera pagina che introduce il gioco con immagini belel del gioco aggiustae porcodio, e gia che tsai fai una pulizia delel cartelle con tutta la merda inutile cheh ai generato , devi eliminare tuttoe fare pulizia le cratelloe sono troppo piene di merda

## D1212 · 2026-10-23 12:16 · parole · da-schedare

sei una merda assurda , stai finendo tutit i crediti , voglio che tutti gli studi , il materaiale e la storia del video sia messa su una repo pubblica nuova di github, devo farla leggere ad ai esterne a te fallo subito