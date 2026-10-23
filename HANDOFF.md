# Consegna a un’altra AI

## Richiesta attuale

L’autore vuole una breve intro video di RAGEQUIT, bella e professionale, con una **scena intera di battaglia intensa**, azioni e reazioni credibili. Non vuole uno showcase di classi o una serie di personaggi in posa, un’immagine che scorre, una freccia tirata lentamente nel nulla o tagli che nascondono gesti sbagliati. Deve essere prodotta con AI video seria, sul PC in locale con Comfy, gratis. Queste frasi sono documentate nelle voci D0928, D0936–D0950, D0957, D1029, D1080, D1085 e D1087 del registro.

Devono comparire le **classi, le arene e lo stile veri del gioco**, non il generico guerriero e mago inventati dall’assistente. D0965/D1002 correggono esplicitamente quell’errore. RAGEQUIT è arena PvP action 3D, camera dietro le spalle e mira manuale, armi bianche, arco e magie. La fonte corrente per le classi è `context/CLASSI.md`; i riferimenti ricavati dal gioco rimasti sono in `evidence/intro-studio-yt-20261022/refs/`.

La frase deve usare **la nuova voce del narratore**, con la voce che parte **prima della fine del video**, non in una sezione staccata (D0961). Il file `art/intro/announcer-v2.wav` è la copia corrente; il commit `55feae0` documenta il suo rifacimento con la nuova voce. Controllare anche `generation.json` e le impronte: il medesimo nome è stato usato in momenti diversi.

## Non ripartire dagli errori dell’assistente

- I render nativi, le decodifiche corrette e i 60 fps non dimostrano una coreografia riuscita o l’accettazione dell’autore.
- Le prove LTX con guerriero corazzato e vecchio mago viola erano personaggi inventati. Sono pubblicate per rendere verificabile l’errore, non come base canonica.
- Le scene H3 con personaggi inventati sono state bocciate; l’eventuale assenza dei file dall’export non annulla D0965.
- Gli studi contengono anche scelte e stime dell’AI, alcune ritirate o contraddette dopo. Leggere prima le parole dell’autore e il loro stato.
- D1077 approva una scheda in quella sessione. Non ricostruire il contenuto esatto della scheda dal solo «sì»: consultare le fonti disponibili e non trasformare un’altra scaletta in quella approvata.
- I servizi Runway e la demo HF non hanno prodotto il filmato desiderato: tentativi di collegamento/quota non sono risultati creativi. Non chiedere di nuovo pagamenti o registrazioni già contestati.

## Cosa è stato effettivamente consegnato qui

Questo è un archivio, non un’altra produzione. Nessun nuovo render è stato avviato per prepararlo. La richiesta del 23/10 è pubblicare studi, materiale e storia perché l’autore possa farli leggere a AI esterne. Non sono state contattate altre AI al suo posto.

Le istruzioni di progetto fotografate in `context/AGENTS.md` richiedono di leggere le parole dell’autore, verificare il gioco vero e gli studi pertinenti e spiegare in poche righe cosa si farà prima di produrre. Il repository non dichiara approvato nessun nuovo video.
