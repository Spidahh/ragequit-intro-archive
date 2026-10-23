# LTX-2.3 locale: produzione intro, 22/10/2026

Richiesta: D0949/D0955. Video AI inventato di combattimento, senza servizi a consumo o nuovi account. Questa cartella non sostituisce il filmato installato nel gioco.

Runtime separato: C:/Users/magis/.codex/tools/comfyui-ltx, ComfyUI ufficiale commit 1a82e6d01f395b43275c77acd289af1eb7090bb9, Torch 2.14.1+cu130. Server esclusivamente localhost:8197 con --offline. RTX 4090 24 GB. I pesi pubblici sono fuori dal repository; revisioni, dimensioni e SHA del fornitore in models.json. Nessuna credenziale richiesta o salvata.

Fonti: https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_ltx2_3_t2v.json ; https://huggingface.co/Lightricks/LTX-2.3-fp8 ; https://github.com/Lightricks/LTX-2/blob/main/LICENSE-2_x . I pesi LTX sono soggetti alla propria licenza, non dichiarati di pubblico dominio.

Recipe: otto passi a meta risoluzione, upscaling latente 2x, tre passi di rifinitura, LoRA distillata 0.5, CFG 1. Variante guidata: stesso nodo ufficiale LTXVImgToVideoInplace del template con forza 0.7 nella prima fase e 1 nella seconda. Nessuna interpolazione o accelerazione usata per nascondere difetti di azione.

Tentativi scartati internamente, non approvazioni dell'autore:
- 144713, text-to-video, 121 fotogrammi: movimento continuo ma resa da vecchio gioco 3D, azione coperta da colonna e bagliore alla mano.
- 113957, text-to-video, 121 fotogrammi: sfondo quasi bianco da bozzetto, arma instabile, coreografia non fedele. Nessuno dei due viene montato come consegna.

Prompt, workflow API, submission e history rappresentano la generazione corrente. Le precedenti prove sono conservate soltanto in .verify/intro-ltx23-local/attempt-01 e attempt-02, non spacciate per filmati finiti. L'immagine reference.png e stata creata con lo strumento integrato Imagegen come guida del modello video; non e il video finale.
