# RAGEQUIT — «NON LASCIARGLI SPAZIO»

**Proposta di produzione, NON intro approvata.** Non sostituisce il video installato.

## Identità che non si cambia

- **Tempestblade = Serath**: capelli bianchi, corazza argentata con oro antico, **spada singola nella sinistra**, ali non visibili a riposo. Modello reale `context/CLASSI.md` e `evidence/intro-studio-yt-20261022/refs/ref_tempestblade_full.png`.
- **Pyromancer = Morigesh**: pelle **blu pallido, spenta**, corna/ornamenti, abiti di corda e osso, **bambola e ago**; non un mago generico con bastone. Fonte `ref_pyromancer_full.png`.
- Combattimento action PvP 3D con mira manuale. Nessuna abilità o ambientazione aggiunta come se esistesse nel gioco.
- Colore controllato, materiali ruvidi, niente patina lucida da AI, niente saturazione artificiale.

## La scena — proposta per un'intro *molto breve*

**Un solo scontro continuo, non un showcase.** Durata indicativa **8–9 secondi totali**, da adattare al movimento e alla voce, non un requisito imposto all'autore. Il combattimento parte *già in corso*. Due personaggi sempre in rapporto spaziale leggibile. Il titolo compare solo dopo una conseguenza di gioco.

| Tempo indicativo | Azione visibile e conseguenza | Regia / suono |
|---|---|---|
| 0–1,4 s | Tempestblade entra nel campo dalla sinistra con un fendente; Pyromancer arretra sotto pressione, la spada sfiora il corpo ma **manca**. | Carrello laterale basso, entrambe in campo. Suono del fendente che attraversa l'aria, niente impatto fasullo. |
| 1,4–2,8 s | Pyromancer esegue **Backdraft**, saltando indietro; la fiammata apre spazio. Tempestblade assorbe l'inerzia del colpo mancato e cambia appoggio. | Stessa direzione di camera. La distanza fra i corpi cresce davvero. Non tagliare durante i piedi. |
| 2,8–4,8 s | Pyromancer crea **Ember Field** davanti alla spadaccina e lancia **Flame Wave** attraverso il campo: il terreno esplode. Tempestblade usa **Slipstream Step** per uscire lateralmente dall'area, non «para il fuoco». | La camera aggira lievemente, mantenendo il terreno marcato e la geografia. L'esplosione illumina brevemente, poi torna l'esposizione normale. |
| 4,8–6,5 s | La Tempestblade emerge dal fumo alla distanza ravvicinata; **Rising Gale** solleva Pyromancer. L'azione arriva alla conseguenza: Morigesh perde contatto col terreno. | Non interrompere prima della reazione. Breve picco sonoro, camera che segue il movimento in alto. |
| 6,5–8,5 s | La voce dell'annunciatore comincia **sullo scontro**, poi il movimento ascendente copre la transizione verso il **logo RAGEQUIT originale**, che resta leggibile. | Usare `art/intro/announcer-v2.wav` (verificare durata e parole effettive); sincronizzare «WELCOME TO RAGEQUIT!» col culmine, l'eventuale «FRAG THEM ALL!» sul titolo solo se presente o approvato nella voce. Nessun narratore nuovo inventato. |

**Perché questa scena è diversa dalle precedenti bocciate:** non c'è una palla di fuoco semplicemente parata, un'ascia contro il terreno, un duello di pose, una freccia lenta senza bersaglio o una sequenza di quattro presentazioni. Qui ogni gesto cambia la distanza, costringe una difesa e ha una reazione in campo. L'ambiente resta neutro finché non si ottiene un riferimento verificato della mappa vera; NON chiamarlo mappa canonica.

## Riferimenti effettivamente consultati

- **Paragon – Morigesh Cinematic Launch e Serath Announce**: studi nell'archivio `evidence/intro-studio-yt-20261022/report-paragon.md`. Servono per i modelli e l'energia del gesto, non per riusare immagini o trailer di Epic.
- **Spellbreak Official Launch Cinematic** (Epic/PlayStation): magia con traiettoria e forma leggibili; nel nostro caso sempre causa → evasione → effetto.
- **SMITE e Paragon**: montaggio deciso sulla reazione al colpo, non su una posa eroica; studi locali `report-smite.md`, `report-paragon.md`.

## Percorso di generazione AI senza nuovi servizi a pagamento

1. **Fissare il fotogramma di partenza** con i due corpi riferiti, una sola arena non specifica e una postura di combattimento reale; evitare di inventare dettagli facciali o nuove armi.
2. Per prova di movimento, usare il template **LTX-2.3 I2V** ufficiale in ComfyUI, controllando nel template la revisione caricata. Non trattare il solo prompt come controllo sufficiente della coreografia.
3. Chiedere **un'unica azione consecutiva** e valutare prima di generare il resto. Se il modello spezza l'anatomia o trasforma i modelli, **scartare**. Un video fluido ma errato resta errato.
4. Solo dopo un'azione riuscita, costruire il raccordo con **primo/ultimo frame** se disponibile nel workflow; evitare salti arbitrari che nascondono un mancato contatto.
5. Mixare le tracce originali (`announcer-v2.wav`, suoni dell'archivio dove licenza e origine sono note), quindi titolo originale. Non usare audio di trailer esterni.

### Prompt I2V operativo — singolo movimento, in inglese

> Cinematic action shot already in progress in a 3D skill-based fantasy PvP arena, one continuous tracking camera, no cuts. Use the two exactly referenced game characters, preserving both identities, faces, hair, clothing, weapons and colors. The silver-armored white-haired female Tempestblade with a sword in her LEFT hand lunges and swings at close range toward the pale muted-blue-skinned Pyromancer with ritual bone and rope garments, holding her original doll and needle. The Pyromancer narrowly avoids the sword by jumping backward in a Backdraft dodge; her retreating weight, foot contact, cloth and dust are physical, and the sword clearly misses. The Tempestblade must finish her swing and recover her balance, pivoting to face the retreating opponent. Every movement is full-body, fast, grounded, connected and continuous, with genuine animation of legs, pelvis and shoulders. Rough realistic game materials, subdued natural colors, controlled smoke, believable directional lighting, sharp silhouettes, no heroic posing, no unmotivated camera moves. Both fighters visible and spatially consistent throughout.

### Prompt I2V per la prosecuzione **solo se il primo segmento riesce**

> Continue the same uninterrupted duel with the same two exact characters and consistent spatial positions. The Pyromancer places a low burning Ember Field on the stone between herself and the oncoming Tempestblade and sends a Flame Wave across it, making the marked ground erupt. The Tempestblade visibly sidesteps out of the blast with her short Slipstream Step and closes the gap; her sword is still in her left hand. The Tempestblade's Rising Gale lifts the Pyromancer just above the ground, and the Pyromancer reacts visibly, loses footing and rises. The camera maintains the geography, movement direction, proportions, clothing and faces. Show the outcome of every action, no disconnected poses or abrupt unexplained jumps.

**Negative guidance:** glossy plastic skin/armor; saturated cyan, neon orange or purple; different face, costume, body or weapon; blue-smurf skin; staffs; extra characters; missing hands; extra limbs; warped joints; slow motion throughout; idle posing; flat slideshow; random explosions; flash covering the whole action; title inside the generated battle frames; repeated looped motion; strobing; arbitrary cuts.

## Soglia di qualità: non montare né pubblicare se manca uno di questi

- Volti, armi e mani invariati dai riferimenti, pelle Morigesh non satura.
- Ogni fendente **tocca o manca** in modo visibile; ogni schivata sposta effettivamente il corpo.
- Un solo spazio di battaglia continuo; nessuna magia che nasce dal nulla o si trasforma in un'altra.
- Gesti e reazioni fluidi **anche senza musica**; audio aggiunto dopo, non usato per camuffare errori.
- L'annunciatore comincia prima che lo scontro finisca; titolo e voce non diventano un secondo trailer separato.

**Stato:** solo direzione nuova + specifica riproducibile. Non esiste ancora un render animato valido di questa scena. Il fotogramma di previsualizzazione è un test da confrontare con le mesh reali e non una certificazione della loro fedeltà.
