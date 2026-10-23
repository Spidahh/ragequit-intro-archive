# Come si fa un'intro d'azione professionale con l'AI video, in locale e gratis

Ricerca del 22/10/2026 per l'intro di RAGEQUIT. PC: Windows 11, RTX 4090 24 GB, 32 GB RAM, ComfyUI Desktop 0.42.4.
[V] = verificato su fonte primaria o sul PC; [S] = fonte secondaria; [O] = opinione o pratica di mestiere.

## 0. Prima di tutto

### Licenza di MiniMax H3: dall'Italia non è gratis
- [V] Docs Comfy (https://docs.comfy.org/tutorials/video/minimax/minimax-h3): la licenza community gratuita vale solo FUORI da USA, UE, Regno Unito e Corea del Sud (e sotto 20 M$ di fatturato, con la dicitura «Powered by MiniMax H3»). Altrimenti licenza commerciale tramite Comfy, Professional da 5.000 $/mese.
- [V] https://comfy.org/minimax/license.md: quelle regioni sono «excluded from the H3 Community License».
- [S] Nell'UE la licenza community non copre nessun uso (https://huggingface.co/MiniMaxAI/MiniMax-H3/discussions/12).
- Conseguenza: per un'intro pubblicata dall'Italia H3 viola D0327 «tutto gratis» e probabilmente la licenza. Lo stesso vale per HunyuanVideo 1.5 (licenza Tencent esclude UE, Regno Unito, Corea).
- Liberi: Wan 2.2 (i2v, flf2v, Fun Control) Apache 2.0; Wan VACE e Wan Animate 2 Apache 2.0 [S]; LTX-2.x gratis sotto 10 M$ di fatturato; Qwen-Image-Edit-2511 Apache 2.0 [O, da ricontrollare]; FLUX.2 klein 4B Apache 2.0 (9B non commerciale); SeedVR2 Apache 2.0.

### Installato davvero sul PC [V]
H3 fl2va 19,5 GB; H3 ref2va 3,8 GB (scaricamento interrotto, ne servono 19,5); SeedVR2 7B sharp 8,3 GB; Music 3; LoRA turbo H3; text encoder Qwen3-VL 32B; VAE H3 e SeedVR2.
Mancano: pesi di Wan 2.2, LTX, Wan Animate 2, VACE, Qwen-Image-Edit, SDPose, Depth Anything, interpolazione. Nessun modello immagine per i fotogrammi chiave.
Template locali utili: video_minimax_h3_fun_controlnet_union, video_minimax_h3_multiframe_reference, video_wan21_scail2_character_replacement, video_wanmove_480p, video_wan_ati, video_wan2_2_14B_fun_camera, utility_sdpose_ood_video_to_pose_map, utility_depth_anything3_video_depth_estimation, utility_sam3d_body, image_qwen_image_edit_2511(_int8), image_flux2_klein_*, utility_video_frame_interpolation.

### Perché i tentativi precedenti sono stati bocciati
| Bocciatura | Causa tecnica |
|---|---|
| «Un frame che scorre», «braccio lento», «arciera che tira lentamente nel nulla» (D0936-D0947) | Image-to-video da una sola immagine con prompt di movimento debole; i LoRA turbo/lightx2v riducono la dinamica [V docs Comfy]; retiming e interpolazione rendono il moto fluido ma senza peso. |
| Nessuna «azione e conseguenza» (D0939) | Manca il piano di reazione: nel montaggio d'azione un colpo è una coppia azione → reazione. |
| «Personaggi inventati, arena generica» (D0965) | Text-to-video senza riferimenti presi dal gioco. |

## 1. La pipeline professionale vera
1. Sceneggiatura e beat sheet (poche battute leggibili).
2. Storyboard/animatic con i tempi al fotogramma.
3. Schede personaggio e ambiente fissate prima di qualsiasi video.
4. Un fotogramma chiave approvato per inquadratura (spesso inizio e fine).
5. Video fra i fotogrammi chiave: i2v, primo/ultimo fotogramma o video guidato da posa/profondità.
6. Sovra-generazione e selezione [S]: Shy Kids «Air Head» con Sora, centinaia di generazioni per ~1,5 minuti montati (https://www.fxguide.com/fxfeatured/actually-using-sora/).
7. Montaggio, suono, upscale, grana, grade.

Personaggi coerenti: schede come riferimento (H3 ref2va fino a 9 immagini; Wan VACE ref2v; Wan Animate 2 immagine + video guida); primo/ultimo fotogramma (Wan 2.2 flf2v, LTX-2.3); chiavi a metà clip (MiniMaxH3AddGuide, LTXVAddGuide); fotogrammi chiave coerenti con Qwen-Image-Edit-2511; LoRA del personaggio (AI Toolkit, musubi-tuner: 24 GB VRAM, 64 GB RAM consigliati); **render 3D vero come base**, il metodo più robusto quando i modelli esistono già.

Pratica professionale «filmare la performance vera, poi l'AI fa lo stile» [S]: Corridor Digital «Anime Rock Paper Scissors» (attori + sfondi Unreal + SD addestrato su uno stile); pipeline «Unreal → Wan VACE v2v»; blockout come guida di profondità; Netflix «El Eternauta».
[O] Per RAGEQUIT: identità dai modelli del gioco (skin principale), movimento dalle animazioni del gioco più una camera, arena del gioco; l'AI fa il look, gli effetti e i passaggi fra pose.

## 2. Azione veloce, leggibile, d'impatto
Durata delle inquadrature misurata sui trailer scaricati (scene detection ffmpeg): Serath mediana 0,68 s; SMITE 2 reveal 0,43 s; Morigesh 1,63 s; Atlas 1,52 s; Spellbreak 1,57 s; Paragon Announce 1,31 s; To Hell & Back 1,74 s; Mirage 1,80 s. → 8-14 inquadrature in 12-15 s.
Prompt: [V] H3: `[Shot N] At 00:03.500, the camera cuts to…`, nuovo shot a ogni cambio di soggetto/spazio/stato; niente negativi (cfg 1: i divieti aggiungono i concetti). [V] LTX: azione in sequenza, al presente, 4-8 frasi. [O] verbi di contatto e di esito; niente «slow push-in» né «slow motion».
Controllo del movimento (decisivo): Wan 2.2 Fun Control 14B (posa/profondità/canny + primo fotogramma; il LoRA a 4 passi «può ridurre la dinamica» [V]); Wan Animate 2 (video guida RGB + immagine); SCAIL-2; Wan VACE 14B; LTX-2.3 IC-LoRA Union; H3 Fun ControlNet Union (licenza); Wan-Move/ATI (traiettorie). Video guida, in ordine: il gioco (Sequencer di Unreal con personaggi e animazioni veri, RGB + profondità); video veri di combattimento solo per la posa; SAM3D Body. [O] Per i colpi la profondità tiene meglio della posa (porta la sagoma dell'arma).
Primo/ultimo fotogramma corto (17-33 fotogrammi) fra pose molto diverse; con 81 fotogrammi e pose simili viene la scivolata.
LoRA veloci: turbo solo per le bozze, finale a passi pieni.
Montaggio: speed ramp (anticipazione accelerata, contatto tenuto), impact frame 1-3 fotogrammi, smear frame, hit-stop; animare a 2 o a 3 è stile; interpolare solo camera lenta e logo, mai i colpi; clip Wan a 16 fps su timeline 24 senza interpolare = 1,5× più secco.

## 3. Montaggio che nasconde gli artefatti
Tagliare sull'azione; regola dei sei di Murch (emozione > storia > ritmo…); Jackie Chan: colpo in due piani, azione e reazione; inquadrature 0,5-1,5 s; flash frame 1-2 fotogrammi sul contatto (mai lampeggi in serie); J/L cut; grana leggera e tappeto audio continuo.
Suono a strati (attacco, corpo, coda; sub, corpo, medi, alti); fruscii → whoosh → impatti (Bruce Tanis); colpi come una batteria (Daredevil). L'audio nativo dei modelli video solo per i provini. Suoni gratis: pacchetti Fab del progetto; Sonniss GDC (royalty-free, vietato usarli per addestrare AI).

## 4. Stile coerente invece del «look AI»
Cosa fa sembrare economico [S/O]: superfici troppo lisce, bordi duri, niente rumore naturale, colori diversi fra clip, movimenti lenti e fluttuanti, push-in lenti, luce generica arancione (D0752), composizioni centrate, personaggi di stock, testo generato, interpolazione ovunque, inquadrature tutte uguali.
Come si evita: il look si approva sui fotogrammi chiave (render del gioco + restyle); uno stile addestrato sulle nostre immagini approvate; upscale prima del grade, niente sharpening, LUT al 50-70 %, grana alla fine; un solo grade su tutta l'intro con la palette dei menu approvati (D0771/D0776); logo e testi composti in montaggio, mai generati.

## 5. Flusso locale raccomandato
| Passo | Strumento | Licenza |
|---|---|---|
| Animatic e tempi | Unreal Sequencer, personaggi/animazioni/arena/camera veri, RGB + profondità a 24 fps | proprio |
| Posa | SDPose | da verificare |
| Profondità | quella di Unreal, oppure Depth Anything 3 | |
| Maschere | SAM 3.1 | |
| Fotogrammi chiave e stile | Qwen-Image-Edit-2511 int8 sul render | Apache 2.0 |
| Video guidato | Wan 2.2 Fun Control 14B | Apache 2.0 |
| Personaggio dal render | Wan Animate 2 | Apache 2.0 [S] |
| Pose estreme | Wan 2.2 flf2v 17-33 fotogrammi (o LTX-2.3 flf2v) | |
| Upscale | SeedVR2 7B (già installato) | Apache 2.0 |
| Interpolazione | FILM o RIFE solo su camera lenta e logo | |
| Montaggio, grade, suono | DaVinci Resolve gratis o ffmpeg | gratis |

Impostazioni: Wan 2.2 bozze 832×480, finale 1280×720 o 960×544 + SeedVR2; colpi 33-49 fotogrammi, FLF 17-33, 81 solo piani di camera; finale 20 passi (10/10), CFG 3,5 Fun Control / 4 flf2v, euler/simple, shift 8. Wan Animate 2: 832×480, 81 fotogrammi, 6 passi lcm + lightx2v, shift 5. LTX-2.3 IC-LoRA: 768×512, 97 fotogrammi a 25 fps, 8 passi. SeedVR2 7B fino a 1080p, grana dopo.

Flusso: 1) animatic in Unreal (12-15 s, 8-14 inquadrature, ogni colpo con piano d'attacco e di reazione); 2) fotogrammi chiave stilizzati approvati prima del video (D0396); 3) generazione per inquadratura (4-8 semi, si tengono 0,5-1,5 s); 4) montaggio (taglio sull'azione, hit-stop, flash/impact frame, ramp, J/L cut, grade unico); 5) suono a strati, musica con accento sul logo, logo vero composto sopra; 6) SeedVR2 → grade → grana → export 24 fps.

Modelli gratuiti da aggiungere (~90 GB): Wan 2.2 Fun Control high/low fp8 (13,3 + 13,3 GB) con umt5 (6,3 GB) e VAE Wan; LoRA lightx2v 4 passi; Wan 2.2 i2v high/low (13,3 GB ciascuno); Wan Animate 2 int8 (15,5 GB) + clip_vision_h (1,2 GB); Qwen-Image-Edit-2511 int8 (19,1 GB) + Qwen2.5-VL 7B fp8 (8,7 GB) + VAE + Lightning; SDPose (1,8 GB); Depth Anything 3 base (0,5 GB); SAM 3.1 (1,6 GB); FILM/RIFE. Link: https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged, https://huggingface.co/Comfy-Org/Wan-Animate-2, https://huggingface.co/Comfy-Org/SDPose, https://huggingface.co/Comfy-Org/sam3.1, https://huggingface.co/Comfy-Org/frame_interpolation.

## Attenzione, mancano queste cose
1. Licenza di H3 (e di HunyuanVideo 1.5) per l'UE.
2. I pesi dei modelli sopra, ~90 GB.
3. Un modello immagine per i fotogrammi chiave.
4. L'animatic in Unreal.
5. La sceneggiatura approvata dall'autore.
6. Le tavole di stile approvate.
7. Il file ref2va di H3 incompleto (3,8 su 19,5 GB).
8. RAM 32 GB contro 64 consigliati per allenare LoRA video.
9. Rischio di licenza dei render della wiki di Predecessor (D0545): i modelli Paragon dentro Unreal sono la fonte più sicura.

Fonti principali: docs Comfy (MiniMax H3, prompt guide, Wan 2.2 Fun Control, Wan-Move, Qwen-Image-Edit-2511, SeedVR2), docs LTX (IC-LoRA, prompting), fxguide «Actually using Sora», 80.lv su Corridor, StudioBinder (Murch), No Film School (Jackie Chan), PremiumBeat e Film Editing Pro (fight editing), Designing Sound (Bruce Tanis), discussione lightx2v sul rallentamento, musubi-tuner #455.
