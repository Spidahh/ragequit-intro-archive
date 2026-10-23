# RAGEQUIT Unreal — crediti e licenze delle risorse di terzi

Dal 28/09 il codice proprio di Ragequit è leggibile nella [copia pubblica `game/`](../game/README.md).
La licenza MIT riguarda il codice proprio; non concede diritti su motore, Lyra o pacchetti elencati sotto.
I caratteri in `art/fonts` mantengono le rispettive licenze OFL accanto ai file.
L'inventario pubblico degli asset riporta solo nomi e riferimenti, non i loro contenuti.

Figure Tempestblade/Geomancer del 14/10: render Omeda Studios / Predecessor, seguendo la scelta D0545.
Rampage riusa il PNG ufficiale senza ritocchi; Serath parte dal render già presente e cambia soltanto la mazza
in una spada, con image_gen. Fonte, prompt esatto, impronte e stato d'importazione nella voce ELEMENTI
`menu-updated-official-bodies-20261014`. I PNG restano privati in `.verify`; viste e texture nel Git Unreal locale.
Le catture native dei modelli restano prove del corpo e dell'arma; non sono le immagini definitive del menu.
La licenza dei modelli Epic Paragon non concede automaticamente diritti sui render Omeda: resta da verificarli
prima di una distribuzione commerciale, come per le altre figure già accettate.

Illustrazione HOME del 13/10: `T_UI_HomeKeyArt_Approved`, generata con image_gen e approvata dall'autore
(D0762, D0771/D0776). Prompt, origine e impronta nella voce `home-key-art-approved-20261013` del registro ELEMENTI.
Usa come riferimenti l'ambiente RAGEQUIT e i render di Tempestblade/Impaler già presenti nella proposta;
il sorgente resta privato in `.verify/menu-approved-card-finish-20261013` e la texture nel progetto Unreal locale.
Non viene copiata come immagine autonoma nel mirror pubblico `game/` o in `art/`. Le figure degli eroi conservano
la provenienza indicata nelle voci esistenti; l'approvazione del menu non cambia le loro licenze.

Risorse aggiunte al progetto `unreal/` il 24 settembre 2026, dalla libreria Fab
dell'autore. Sono versionate solo nel repository locale `unreal/.git`, senza
remote. **Non vanno mai pubblicate come file autonomi**: la licenza Fab Standard
permette di distribuirle solo incorporate nel gioco.

| Pacchetto | Autore | Scheda | Licenza | Cartella | Note |
|---|---|---|---|---|---|
| Lowpoly Modular Armors - Free | Polytope Studio | https://www.fab.com/listings/d32023d6-cc7c-4a6b-bbc6-b0821c3d3391 | Fab Standard | `Content/Polytope_Studio` | Dichiarato UE 5.3–5.7, aggiunto nella versione 5.7. Scheletro UE5, nessuna animazione. «Consente uso con IA: No» |
| Stylized Fantasy Provencal | StylArts (Leartes) | https://www.fab.com/listings/ced19ea1-31ed-437f-ae64-2b6b1561fede | Fab Standard | `Content/StylizedProvencal` | Richiede Virtual Texture (già attivo). «Consente uso con IA: No» |
| Stylized Newbie Weapons Pack | N-Hance Studio | https://www.fab.com/listings/f512037f-2f87-4303-8228-733ac134ad88 | Fab Standard, livello Personal | `Content/StylizedCharacter` | Il livello Personal vale sotto 100.000 USD di ricavi o finanziamenti negli ultimi 12 mesi |
| Free Magic Niagara | Lord Enot Store | https://www.fab.com/listings/d0fe50c4-6ebe-40d5-b78a-56960832f49e | Fab Standard | `Content/Free_Magic` | Copiato dalla cache del Launcher senza sovrascrivere: il Launcher segnalava un conflitto su un attore di una mappa demo (`__ExternalActors__/ThirdPerson`) portato da Polytope |
| Niagara Slash | UE Game Work | https://www.fab.com/listings/9baf4a11-d63a-4d9c-8ee1-bfedfd3eb696 | Fab Standard, livello Personal | `Content/Knife_light` | Livello Personal come sopra; D0655 usa `VFX/NE_attack01` come corpo in volo di Wind Blade, con scala separata dall'impatto |
| Raven Scythe | MightyPinecone | https://www.fab.com/listings/b7e21ec5-35e6-4680-8a3b-ffee189f8c2f | da rileggere sulla pagina (scaricata dall'autore il 6/10) | `Content/Ragequit/Weapons/Scythes/SM_RQ_Scythe_Raven` | FBX dalla cache del Launcher; 47 mila triangoli; il materiale è costruito nel progetto dalle sue cinque texture. Non segnata come generata da AI |
| Free Fantasy Scythe Pack – 7 Game-Ready Dark RPG Weapons | Yagami | https://www.fab.com/listings/5be8634a-4679-45bc-bd54-a9e1632790f4 | da rileggere sulla pagina (scaricato dall'autore il 6/10) | `Content/Ragequit/Weapons/Scythes/SM_RQ_Scythe_A…D`, `SM_RQ_Scythe_Faz`, `SM_RQ_Sword_Blood` | FBX dalla cache del Launcher; da 72 a 162 mila triangoli l'una, alte 1 m all'origine (in mano vanno scalate); solo texture del colore. Non segnato come generato da AI |
| Niagara Examples Pack | Epic Games | https://www.fab.com/listings/0e188eca-4e54-4fb2-a9ed-d8b8a565e600 | Fab Standard | `Content/NiagaraExamples` | Dichiarato UE 5.7, aggiunto nella versione 5.7. «Consente uso con IA: No» |
| Free Modular Magic SFX | Le Binh Son | https://www.fab.com/listings/f0422e67-33d3-4c6e-b7a1-1059193960de | **CC BY 4.0** | `Content/FreeModularMagicSFX` | **Attribuzione obbligatoria** nei crediti del gioco: «Free Modular Magic SFX» di Le Binh Son, CC BY 4.0, https://creativecommons.org/licenses/by/4.0/ |
| Free VFX Sampler Vol. 2 | TaprootSolutions | https://www.fab.com/listings/1a214259-caee-4644-8668-20312cf41c23 | Fab Standard | `.verify/fab-staging/` (progetto completo, non ancora nel gioco) | Distribuito come progetto: si migrano solo gli effetti scelti. «Consente uso con IA: No» |
| Paragon: Sevarog, Countess, Aurora, Gideon, Greystone, Terra (e Serath, Morigesh, Howitzer, Murdock, Minions; dal 14/10 Rampage, corpo del Geomancer: `Content/ParagonRampage`, scaricato dall'autore il 6/10, voce ELEMENTI «Corpo Geomancer: eroe Paragon Rampage»; dal 10/10 anche lo scoppio a terra di Grux, Greystone, Terra e Aurora, il vortice di Gideon e il segno dello stordimento degli stati comuni; effetti di Minions, Howitzer e Gideon: la palla di fuoco del drago, l'esplosione di Howitzer, il lampo di Gideon, `tools/unreal/prepare-spell-looks.py`) | Epic Games | schede Fab «Paragon: <eroe>» (Sevarog: https://www.fab.com/listings/a4882b5e-cfad-4830-a3dd-46a6c31a79b2); elenco in `STUDI/RISORSE-FAB-29-09.md` | Fab Standard | `Content/Paragon<Eroe>` | Scaricati dall'autore il 30/09. Dal 30/09 i corpi delle sei classi (`tools/unreal/prepare-heroes.py`). **Non versionati** (circa 30 GB). Sulle pagine: «You may not use the trademark PARAGON to advertise or name your game»: la parola Paragon non va nei testi del gioco né nella sua presentazione |
| Realistic Starter VFX Pack Vol 2 | FX Cat UA (a memoria: da rileggere sulla pagina) | scheda Fab «Realistic Starter VFX Pack Vol 2» (libreria dell'autore: `VaultCache/FabLibrary/Realistic_Starter_VFX_Pack_Vol_2-ac2818b3`) | Fab Standard (da rileggere sulla pagina) | `Content/Realistic_Starter_VFX_Pack_Vol2` | 10/10: portati nel progetto dalla cache del Launcher solo i 31 file che servono allo schizzo di sangue (`P_Blood_Splat_Cone`), alle scintille (`P_Sparks_A..G`) e all'impatto generico (`P_Default`): 2,2 MB su 111. Sistemi Cascade. |
| Paragon: Agora and Monolith Environment | Epic Games | https://www.fab.com/listings/6f401fb5-88b5-41b4-bf1b-62321414e1f0 | Fab Standard | `Content/ParagonProps`, `Content/KiteDemo`, `Content/SampleMap`, `Content/Lighting` | Scaricato dall'autore il 30/09, **non versionato**. Dal 30/09 arte dell'arena Drowned Sanctum (`L_Sanctum_Art`, copia della mappa `SampleMap/ParagonSample`, `make-arenas.py`). Modifiche ai file del pacchetto: circa 70 mesh di rocce e rovine vicine all'arena usano i loro triangoli come collisione («complessa come semplice»: senza, i personaggi le attraversavano); il piano d'acqua `SM_Plane_5x5m` e l'albero `SM_FlowerTree_01` sono tornati alla collisione predefinita (`fix-arena-collision.py`). Stesso limite sul marchio PARAGON |

## Asset propri derivati da pacchetti di terzi

Stanno sotto `/Game/Ragequit/` e restano soggetti alla licenza del pacchetto d'origine. L'origine è
anche nel tag `RagequitSource` dell'asset.

| Asset proprio | Origine | Trasformazione | Note |
|---|---|---|---|
| `/Game/Ragequit/Weapons/SM_RQ_Sword_1H_Newbie_02` | `SK_Sword_1H_Newbie_02`, Stylized Newbie Weapons Pack (N-Hance Studio, Fab Standard, Personal) | StaticMesh creata con GeometryScripting dal LOD0, con scala uniforme **0,7407** (tag `RagequitScale`); presa-punta 79,5 cm contro 108 cm dell'originale | Usa il materiale originale `MI_Sword_Newbie_Bl`, referenziato e non copiato. Script: `tools/unreal/prepare-reference-fighter.py` (24 settembre) |
| `/Game/Ragequit/Characters/Polytope/SK_Male_Armor_*` (6 mesh) | `Separate_Parts` di Lowpoly Modular Armors (Polytope Studio, Fab Standard) | Copie riassegnate allo scheletro Lyra, senza physics asset | Materiali originali del pacchetto referenziati |
| `/Game/Ragequit/Weapons/SM_RQ_Sword_1H_Newbie_01`, `SM_RQ_Dagger_1H_Newbie_01`, `SM_RQ_Axe_1H_Newbie_01` (25/09 notte) | `SK_Sword_1H_Newbie_01`, `SK_Dagger_1H_Newbie_01`, `SK_Axe_1H_Newbie_01`, Stylized Newbie Weapons Pack (N-Hance Studio, Fab Standard, Personal) | StaticMesh create con GeometryScripting dal LOD0, con la stessa scala uniforme della spada (**0,7407**, tag `RagequitScale`); materiali originali referenziati | Script `tools/unreal/prepare-loadouts.py`; seconda spada della build Skybreaker, pugnale delle build Binder; l'ascia non è usata (non entra nel pacchetto) |
| `/Game/Ragequit/Weapons/SM_RQ_Shield_Newbie_01` (25/09 notte, terzo giro) | `SK_Shield_Newbie_01`, Stylized Newbie Weapons Pack (N-Hance Studio, Fab Standard, Personal) | StaticMesh creata con GeometryScripting dal LOD0, scala uniforme **0,7407** come le armi; materiale originale `MI_Shield_Newbie_Bl` referenziato | Script `tools/unreal/prepare-loadouts.py` (`shield()`); scudo delle build Aegis |
| `/Game/Ragequit/Loadouts/Motion/RQ_ShieldArm_Sword_Regular_A`, `_A_Rec`, `_B`, `_B_Rec`, `_C` (25/09 notte, terzo giro) | clip UAL `Combat_Source_Sword_Regular_*` e `Combat_Source_Idle_Shield_Loop` (stessa provenienza delle altre clip UAL, sotto) | Copie delle clip della spada con le 44 ossa del braccio sinistro prese dalla guardia con lo scudo (clavicola ricalcolata a ogni fotogramma, tag `RagequitMethod`) | Script `tools/unreal/prepare-loadouts.py` (`shield_arm_clip()`); combo «Sword and shield» dell'Aegis |
| `/Game/Ragequit/Characters/Polytope/SK_Male_Armor_head_01`, `hair_20`, `beard_20`, `05_C_body`, `05_C_legs`, `05_C_gauntlets`, `05_C_boots`, `05_C_helmet`, `05_C_cape`, `01_A_cape` (25/09 pomeriggio) | `Separate_Parts` di Lowpoly Modular Armors (Polytope Studio, Fab Standard) | Copie sullo scheletro Lyra, senza physics asset, tag `RagequitSource` | Aspetto per classe (Reaver, Binder, Aegis). Script `tools/unreal/prepare-class-looks.py` |
| `/Game/Ragequit/UI/Glyphs/T_Glyph_*` (11 texture, 25/09 pomeriggio) | `T_Free_Spells_Arrow`, `Circle`, `Crack1`, `Cross`, `Flame`, `Flash`, `Flash2`, `Lightning`, `Runes`, `Snow`, `Star` di Free Spells Niagara (UrtanoVFX, Fab Standard, Personal) | Copie con gruppo UI, mai in streaming, al massimo 512 px | Icone delle abilità, disegnate dal materiale proprio `M_RQ_Glyph`. Script `tools/unreal/prepare-ui.py` |
| `/Game/Ragequit/UI/Glyphs/T_Icon_*` (47 texture; 16 nuove il 27/09 per i kit di Bloodrush, Stormbinder e Bulwark) | Opera propria: pittogrammi disegnati da `tools/unreal/make-icons.py` (Pillow), PNG in `art/icons/` | Stesse impostazioni dei glifi | Icone delle abilità. Script `tools/unreal/prepare-ui.py` |
| `/Game/Ragequit/UI/Sounds/SC_UI_HoverTick` (26/09 sera, T1 E43, al posto di `SC_UI_Hover`), `SC_UI_Click`, `SC_UI_Choose` (25/09 pomeriggio) | `Interface_1-1_Cue`, `Magical_Interface_5-1_Cue` e `Draw_Weapon_Metal_1-1_Cue` di Free Sounds Pack (prima il passaggio usava `ButtonHover` di Lyra, una MetaSound a volume pieno; la copia `SC_UI_Hover` resta ma non è più usata) | Copie con il volume abbassato (0,35, 0,5 e 0,6) | Suoni dei bottoni del menu. Script `tools/unreal/prepare-ui.py` |
| `/Game/Ragequit/Combat/Look/M_RQ_WorldAligned` e `MI_RQ_Floor`, `MI_RQ_Walls`, `MI_RQ_Cover` | texture `T_Rocks_Bricks`, `T_StoneWall02`, `T_StoneWall03` (colore e normale) di Stylized Fantasy Provencal (StylArts, Fab Standard) | Materiale proprio proiettato nello spazio del mondo per pavimento, muri e ripari; texture referenziate, non copiate | Script `tools/unreal/improve-arena-look.py` (24 settembre sera) |

Già presenti prima del 24 settembre (provenienze spostate qui da `godot/CREDITS.md` quando la versione Godot
è stata tolta dal progetto, 24/09):
- contenuti **Lyra** di Epic Games (UE-Only Content), base del progetto;
- **Universal Animation Library 1 e 2**, Quaternius — https://quaternius.itch.io/universal-animation-library,
  https://quaternius.itch.io/universal-animation-library-2 — edizioni Standard gratuite, **CC0 1.0**: animazioni
  di spada e di lancio dei montaggi di combattimento (`Combat/Motion/Combat_Source_*`);
- **Free Melee Weapon Pack (PBR and Stylized)**, Tesseract Assets —
  https://www.fab.com/listings/da6e582c-c12b-4768-b67f-8e248339c071 — Fab Standard, livello Personal: la spada della
  prima base (materiali `M_Sword`/`T_Sword_*`), sostituita dal 24/09 dalla spada N-Hance.

## Pacchetti Fab aggiunti dall'autore il 25/09 mattina

Aggiunti a RAGEQUIT dall'autore col Launcher (cache `VaultCache`, 10:52-10:53); dettagli e licenze dei pacchetti sono registrati qui sotto.
Licenza Fab Standard; prezzo 0 ricontrollato sulle schede pubbliche il 25/09 verso le 08:45.

- **[18] Free Spells Niagara** (UrtanoVFX, `Content/Free_Spells`, gratis col livello Personal): effetti di lancio e
  d'impatto di Mend, Barrier, Shockwave, Repulse e delle definitive Bloodbath, Meteor, Tempest, Bastion, Sanctuary
  (`tools/unreal/prepare-loadouts.py`, `FAB_FX`). In PIE finiscono tutti da soli entro 8 s (`inspect-fx-lifetime.py`,
  fx-lifetime-20260925-105638, con due controlli).
- **Free Arrow Trail** (CodePhase Games, `Content/ArrowTrail`, gratis per tutti i livelli): scie dei Bolt
  (scia di base `NS_ArrowTrail_Basic`, varianti del kit come `NS_ArrowTrail_Ice` per Cryomancer); restano accese finché c'è il proiettile.
  D0655 usa la scia neutra per Wind Blade e Stone Shard, senza ereditare il ghiaccio. Il 12/10 il listing
  [Free Arrow Trail](https://www.fab.com/listings/b8ff3ab4-0e81-4335-bbf0-fea15f6fcdfc) è stato verificato nel browser del PC:
  CodePhase Games, dieci effetti, gratuito, licenza Standard, indicazione «Consente uso con IA: No».
- **FANTASTIC - Village Pack** (Tidal Flask Studios, `Content/Fantastic_Village_Pack`) e **Lowpoly Handpainted
  Environment** (Yevheniia Yaremko, `Content/HandPaintedEnvironment`), gratis per tutti i livelli: erano l'arte delle arene
  Village Square e Forest Ruins, ritirate il 21/10 (D0903; mappe in `E:\PROGETTI\_DA-CANCELLARE\20261021-arene-vecchie`).
  Dal 21/10 HandPainted non entra più nel pacchetto; del Village Pack restano i 10 file che il gioco usa ancora.
- **Inferno World Free** (`Content/Inferno_World_Free`, gratis su Fab; installato dall'autore, versionato dal 25/09
  pomeriggio; il livello di licenza della scheda non è stato riletto: da confermare): era arte, luci e cielo dell'arena Inferno
  Pit, ritirata il 21/10; restano i 9 file che il gioco usa ancora. Unica modifica ai file del pacchetto: alcune mesh usano i
  loro triangoli come collisione («complessa come semplice», del ritaglio del 25/09).
- **Free Fire** (Vefects, `Content/Vefects/Free_Fire`; arrivato con gli altri pacchetti Vefects installati dall'autore
  il 25/09 alle 11:43 e versionato con loro; la scheda Fab non è stata riletta, licenza da confermare): il falò
  `NS_Fire_Big` delle trappole di fuoco delle arene Village Square e Forest Ruins (dal 25/09 sera al 21/10, `add-arena-hazards.py`);
  dal 10/10 il fuoco a terra `NS_Fire_Floor_01` del campo di Ember Field del Pyromancer (`prepare-spell-looks.py`).
- **Easy Shockwaves VFX** ed **Easy Impact Frames** (Vefects, `Content/Vefects`, gratis col livello Personal; aggiunti
  alle 11:43): onde d'urto e suoni di Shockwave (abilità poi tolta dalle build), Repulse, Skyfall, Bloodbath e Meteor; lampo di parata e guardia rotta.
- **SlashTrail** (SoftTofu, `Content/SlashTrail_SoftTofu`, aggiunto alle 11:47; versionate solo le cartelle Niagara,
  Resource e Material, non la DemoRoom con i personaggi Paragon): impatti delle magie, fra cui `NS_Hit_Ice_Once`
  per Cryomancer e, da D0655, `NS_Hit_Wind_Once` per Wind Blade. Il codice attenua gli impatti vicini alla lente.
  I precedenti effetti attaccati alle armi e alle mani sono stati rimossi dal gameplay secondo D0600; i riferimenti
  ai vecchi kit nei dati non descrivono sottoclassi del roster corrente. Gli shader devono essere pronti prima di giudicare una cattura.
  Per Ice Lance, D0655 sostituisce `NS_Hit_Ice_Once` con `P_Aurora_Melee_SucessfulImpact` di Paragon Aurora
  sul corpo e sul mondo: i frammenti Niagara precedenti mantenevano dimensioni proprie anche riducendo la scala.
- **Free Sounds Pack** (aggiunto alle 11:45, `Content/Free_Sounds_Pack`): sottofondo delle arene (uccelli e vento; vento
  e fuoco nel villaggio; volume x3) e urto di scudo metallico della guardia (volume x2,5); dal 25/09 pomeriggio anche il
  fruscio del fendente (`Whoosh_1-1_Cue`), il colpo di lama (`Stab_4-1_Cue`) e due suoni del menu
  (`tools/unreal/prepare-combat-audio.py`, `prepare-ui.py`). **Free Melee Weapons**
  (Tesseract, lo stesso pacchetto della spada di DA_Combat): l'ascia a una mano della Skybreaker (`SM_RQ_Axe_1H_FMW_01`,
  versionati solo SM_axe, MI_Axe, Master_Material e le tre texture T_AXE01).
- Studio degli altri pacchetti arrivati fra le 11:45 e le 11:52 (workflow del 25/09, 6 agenti con verifica): da usare
  Free Sounds Pack (ambiente delle arene, urto di scudo) e l'ascia di Free Melee Weapons (è lo stesso pacchetto Tesseract
  della spada); forse Inferno World (arena low poly) e Dynamic Falling (solo rotolate); no IdaFaber (personaggio moderno
  realistico, contiene un corpo nudo: mai da referenziare), Lab, Scifi Desert City, Megaplant Library (plugin
  sperimentali), Pack Bonus (materiali fotorealistici), Singapore Canal (borgo orientale fotorealistico), Realistic
  Starter VFX Vol.2 (Cascade realistico). Nessuno di questi è versionato.
- **29/09:** quei pacchetti non usati, più `clown_monster`, Dynamic Falling e Free Animation Library (mai usati nel gioco),
  sono stati spostati fuori dal progetto in `E:\PROGETTI\_DA-CANCELLARE\riordino-ragequit-2026-09-29\unreal-content-non-usato`.
  Per riaverli si riporta la cartella in `unreal/Content` a editor chiuso, oppure si riaggiungono da Fab.

## Free Animation Library (provenienza trovata il 25/09)

In `unreal/Content` ci sono `FreeAnimationLibrary/` (164 file, circa 188 MB, con una mappa demo) e 352 attori e
oggetti esterni di `LocomotionAnimPack` in `__ExternalActors__`/`__ExternalObjects__` (la cartella dei contenuti
`LocomotionAnimPack` manca). Il 24/09 sera la provenienza risultava sconosciuta. Il 25/09 mattina la cache dei download
del Launcher (`C:\ProgramData\Epic\EpicGamesLauncher\VaultCache\FreeAnimd61b5f5d32dcV1`, solo i nomi delle cartelle)
contiene esattamente queste tre cartelle, scritte il 24/09 alle 10:31:49 come quelle del progetto: il pacchetto è stato
aggiunto a RAGEQUIT dall'autore col Launcher, dalla sua libreria Fab. Corrisponde al listing «Free Animation Library» di
voxel vision (Fab Standard, gratis col livello Personal). Non sono nel repository `unreal/.git` (come gli altri pacchetti
Fab); il gioco può usarne le clip, citandole qui.

## Menu nuovo del 27/09: caratteri e grafiche

- **Caratteri** (in `art/fonts`, con la licenza accanto; in Unreal `/Game/Ragequit/UI/Fonts`, importati da
  `tools/unreal/prepare-ui.py`), tutti **SIL Open Font License 1.1**, scaricati da Google Fonts (repository google/fonts):
  - Big Shoulders Display (Black ed ExtraBold: istanze statiche del file variabile, fatte con fontTools; il carattere non
    ha un Reserved Font Name);
  - Barlow Condensed (Medium, SemiBold, Bold);
  - Chakra Petch (SemiBold, Bold).
  Nei Credits del gioco: «Big Shoulders Display, Barlow Condensed and Chakra Petch, under the SIL Open Font License 1.1».
- **Grafiche del menu** (`art/ui/menu`, in Unreal `/Game/Ragequit/UI/Menu`): **opera propria**. Simboli, logo, piantine
  delle arene, pennellate, anello, bagliore, grana e righe sono disegnati da zero in Python (Pillow; i simboli con
  shapely) da un workflow di agenti con revisione, il 27/09. I generatori sono in `tools/unreal/menu-art/`. Le piantine
  di Village e Ruins sono disposizioni inventate (non c'è una vista dall'alto delle arene), quella del cortile usa le
  misure vere.


## Menu illustrato del 28/09

Il fondale del menu del 28/09 (`art/ui/menu/T_Art_Menu.png`) è generato con imagegen usando il riferimento
illustrato fornito dall'autore (`image-gen-1(7).png`, già in `DOCUMENTAZIONE/IMMAGINI/MENU`, tolto dal progetto il 7/10 con i
riferimenti superati: `E:\PROGETTI\_DA-CANCELLARE\menu-riferimenti-superati-20261007`). Non deriva da Lyra o Fab.

Il kit dell'interfaccia del 29/09 sera (`art/ui/menu/kit/`) è preparato da un'altra AI (Codex) per l'autore:
- le illustrazioni sono generate con il suo generatore di immagini, partendo dallo schema a dieci schermate dell'autore;
- i pezzi d'interfaccia sono geometria SVG propria.

Non deriva da Lyra o Fab. Provenienza di ogni file in `art/ui/menu/kit/manifest.json` e `generation.json`.
Provenienza e collocazione dei sorgenti grafici: `art/README.md`. Le texture schematiche del 27/09 conservano
la provenienza descritta sopra; non sono l'autorità visiva per il menu illustrato.

## Locomozione del 28/09: Game Animation Sample

**Game Animation Sample Project — Epic Games**, versione 5.8 gia presente nella VaultCache del Launcher. Importate le clip di camminata, corsa, sprint e idle; 500 clip selezionate sono ritargettate sul Manny e collegate al database Pose Search del combattente. Fonti e derivati rimangono nel progetto Unreal locale, escluso dal repository pubblico. Credito aggiunto alla pagina Credits del gioco.

[Pagina Fab di Epic](https://www.fab.com/listings/880e319a-a59e-4ed2-b268-b32dac7fa016); [documentazione di Epic sull'uso e migrazione delle animazioni](https://dev.epicgames.com/documentation/en-us/unreal-engine/game-animation-sample-project-in-unreal-engine). La scheda Fab indica che il pacchetto e gratuito e non consente uso con AI; non e una licenza per ripubblicarne gli asset o usarli per addestramento.

Mini intro v3 (10/10): suoni di Whoosh, Shield Metal/Wood Impact, Punch, Wood Chop, Rock Impact e Blacksmithing
di **Free Sounds Pack**, gia posseduto, incorporati nel film `art/intro/ragequit-intro-v3.mp4`. Tagli, variazioni
di velocita, missaggio e brevi riflessioni. Gli originali e il letto audio separato non si pubblicano.

Video 2 (10/10): riferimenti visivi da render locali dei personaggi Paragon di Epic Games presenti nel
progetto Unreal: Gideon (Voidseer) e Serath (Warmaster). Reinterpretazioni imagegen e animazioni locali
FastWan, modello FastVideo/FastWan2.2-TI2V-5B-FullAttn-Diffusers (Apache-2.0), interpolazione RIFE.
Nessuna carta o immagine della wiki Omeda. Suoni Free Sounds Pack incorporati nel film; asset originali,
modelli, pesi e letto Foley separato restano fuori dal repository. Logo originale e voce del Video 1.

Annunciatore D0641 (10/10): sette battute originali in `art/audio/announcer`, prodotte localmente con
Qwen3-TTS-12Hz-1.7B-Base (Apache-2.0), clonando esclusivamente la voce sintetica originale creata per
il Video 1 con VoiceDesign, `announcer-333.wav`. Stesso trattamento di pitch, formanti, EQ e saturazione
del Video 1. Nessuna registrazione di Quake o di un attore usata. Manifest con provenienza e hash.

12/10 — 30 derivati scheletrici locali in `/Game/Ragequit/Characters/Heroes/ClothStable`, dai modelli Paragon già posseduti e dai corpi Warmaster senza arma già documentati. Ricostruzione dei collegamenti cloth/LOD, senza nuove risorse esterne; licenze e crediti delle sorgenti restano applicabili. L'elenco fonte/destinazione è `tools/unreal/hero-cloth-sources.json`; gli asset restano nel Git Unreal locale, esclusi dalla copia dei sorgenti su GitHub.


19/10, D0842: le sette mesh in `/Game/Ragequit/Maps/SurfaceFixes/SM_RQ_*` sono copie locali derivate dalle scale ParagonProps Monolith (Dawn/Ruins), con collisione sui triangoli e a due facce. Le otto istanze `MI_RQ_StairBack_*` mantengono materiali e texture originali tramite il parent e abilitano il retro delle superfici. Non diventano risorse originali distribuibili liberamente: restano soggette alle licenze dei pacchetti d'origine. Le corrispondenze sorgente/destinazione sono nella ricevuta `refinement-assets-20261019-002959/report.json`. Nessun pacchetto o asset binario e' ammesso nel mirror dei sorgenti o nel dossier.

Persistenza completata con `refinement-streamed-levels-20261019-005526`: le sostituzioni comprendono anche gli attori dei livelli artistici `L_Sunken_Art` e `L_Ziggurat_Art`, non solo le mappe principali. La pubblicazione finale contiene sette mesh derivate, verificati tutti i file cooked/staging/manifest; nessuna nuova licenza o risorsa esterna.

## Musica e suoni entrati nel gioco il 21/10 sera (PIANO-COMPLETO strato 3)

Licenza Fab Standard, nessuna attribuzione obbligatoria; nominati comunque nei CREDITS del gioco (riga SOUND):
- **Caves & Dungeons** (`unreal/Content/CavesAndDungeons`): la musica del menu (Decrepit Cathedral, Prison of the Astrals, Call of the Depths).
- **Combat Fantasy Free Pack** (`E:\FAB\downloads\audio_combat_fantasy_music`, importato da `tools/unreal/prepare-flow-music.py`): VERSUS
  («Your Time Draws Near»), vittoria («Destined to Win»), sconfitta («Sentinels»).
- **Viking War Horns**, **LOW END IMPACTS Vol. One**, **Interface and Item Sounds**: i suoni della partita e del menu
  (`tools/combat-sounds.json`, gruppi Match e Menu).
- L'annunciatore: 34 battute sintetiche (Qwen3-TTS, Apache-2.0) nella voce del Video 1, vedi sopra.

## Arene, strato 4 (22/10)

- **Dark Ruins Megascans Sample** e **Goddess Temple Megascans Sample** (Epic Games e Quixel, da Fab, licenza Fab Standard,
  nessuna attribuzione obbligatoria): i pezzi scelti per Sunken Sanctum (rovine di chiesa gotica: colonne, archi, finestre,
  porte, cornici, lastre, catene, campane, candele, lanterne, rune, superfici) e per The Ziggurat (pietre di Angkor, colonne
  romane, scale, rupi di cava, piante tropicali, bruciaincenso) portati dai progetti `E:\FAB\proj_dr` e `E:\FAB\projects`
  con `tools/migrate-uasset-closure.py` in `unreal/Content/DarkRuins` e `unreal/Content/GoddessTemple` (non versionati).
- **Passi nell'acqua**: «Splashing Footsteps Shallow Water» e «Splashing Stomps Impacts Shallow Water» di ChristopherJngs
  (Freesound 861369 e 861370, **CC0**), tagliati in dieci passi e otto atterraggi (`E:\FAB\downloads\audio_freesound_cc0`,
  `sources.tsv`); nominati nei CREDITS (riga SOUND). Nella stessa cartella, scaricati per le arene e non ancora nel gioco:
  paludi di craigsmith e RyanKingArt, cascate di LXX.70 e A.Deathy, tutti CC0.
- Dal 22/10 le tre mappe (`tools/unreal/list-map-packs.py`, dipendenze dure) usano: Paragon Agora e Monolith, Dark Ruins,
  Goddess Temple, MedievalDungeon, Dungeon, KiteDemo, M5VFXVOL2, WaterMaterials (**CC BY 4.0**, tharlevfx), Torn Banner,
  Sparks and Embers, Singapore Canal; non piu' Stylized Provencal, FANTASTIC Village e Inferno World. Il Soul Core e' un'orba di
  Mayu's Orb VFX Collection (**CC BY 4.0**, dm-mayu); il temporale del Sunken e' di Free Thunder Sounds (**CC BY 4.0**, Gregor
  Quendel); tutti e tre nominati nei CREDITS del gioco.

## Sistemi, strato 5 (22/10)

- **Easy Input Prompts** (Nerwy, da Fab, licenza Fab Standard, nessuna attribuzione obbligatoria; https://www.fab.com/listings/c386fea5-e723-488c-abeb-7995157375c8):
  i simboli dei tasti del pad Xbox e PlayStation e delle levette, copiati da `tools/unreal/prepare-pad-glyphs.py` in
  `/Game/Ragequit/UI/Menu/T_Pad_*` (versionati nel Git Unreal locale); nominati comunque nei CREDITS (FONTS AND INTERFACE).

## Pacchetti Fab del 20/10 sera (D0874-D0876)

Circa 115 pacchetti gratuiti presi dalla libreria Fab dell'autore il 20/10 sera; elenco, uso previsto e posizione in
[PIANO-COMPLETO.md](PIANO-COMPLETO.md) (§10 e allegati A e B). Quelli in formato Unreal stanno in `unreal/Content/<cartella>`
(non versionati, come gli eroi Paragon); quelli in FBX, OBJ, zip o texture in `E:\FAB\downloads`; tre campioni sono
progetti a parte in `E:\FAB\projects`, `E:\FAB\proj_mr`, `E:\FAB\proj_dr`. Licenza Fab Standard (Personal o Professional)
tranne questi, in **CC BY 4.0**, che chiedono l'attribuzione nei crediti del gioco quando entrano nel gioco:

| Pacchetto | Autore | Scheda |
|---|---|---|
| Battle Drum Loops (FREE Music Pack) | Cinematsic | https://www.fab.com/listings/a53de57c-0286-48ce-8855-27e50ec1d21c |
| Footsteps Mini Sound Pack | Mechanics Mechanics | https://www.fab.com/listings/baf07baa-d485-4d37-bf73-dab6a50ed4bb |
| Free Thunder Sounds | Gregor Quendel | https://www.fab.com/listings/c832a656-f75c-45fc-bdb1-8fb702a7ba90 |
| Free Niagara Particles | SoftTofuVFX | https://www.fab.com/listings/183732bc-c2fb-465c-9453-f70a1ce7ba2c |
| MagicCircle VFX | SoftTofuVFX | https://www.fab.com/listings/78873187-c121-4b6d-b776-f275b941bae2 |
| Portal Travel | FenixFX | https://www.fab.com/listings/53558156-9008-4478-a6df-f2f423b0f045 |
| Mixed VFX | G.G. | https://www.fab.com/listings/6518971c-c8ca-47d7-8611-1ff068b78dd5 |
| Mayu's Orb VFX Collection | dm-mayu | https://www.fab.com/listings/d13b3d78-9768-4952-b8e5-4cb476fa5b9f |
| Desert Castle | CraftbridgeTeam | https://www.fab.com/listings/178c1ed7-b5e8-4768-8a86-da3af516778b |
| Water Materials | tharlevfx | https://www.fab.com/listings/063155ea-d9d2-4f29-b09f-33270b0bc861 |
| Simple Water Puddles (Free) | JVAD3D Models | https://www.fab.com/listings/5718b8ac-27f7-4741-85ba-2cff7bf2f77d |
| Barbarian Banners | Snit | https://www.fab.com/listings/75f4d553-a080-41c7-a57b-98e31c6209be |
| Medieval Torch (Free) | Apex Wolf | https://www.fab.com/listings/b40acc92-21e1-4d92-9248-2ecce53fc99b |
| Animation - Getting Up 01, 02 | Klian | https://www.fab.com/listings/69dae222-05e9-4065-9030-45887986cdec |
| FREE Dramatic Death | Darkania Works | https://www.fab.com/listings/5aab4fdc-7cea-4acd-b1ff-2ca3b3706c02 |
| Ice Materials 4K | Stone Material | https://www.fab.com/listings/d55d6be8-d627-4381-b88e-e519f394abb4 |
| Gray Pavement Floor Material | Stone Material | https://www.fab.com/listings/aa6b2ecf-4bd3-42fe-af42-0792d57548de |
| Decal - Ground Cracks - Game Ready | Polytricity | https://www.fab.com/listings/b2ba37f1-2dee-4ccc-896c-87a44bfb17b9 |
| 100 RPG Fantasy SFX Pack (preso il 21/10) | Erwin's Studio | https://www.fab.com/listings/f5d46546-03be-4b15-886d-d5c847b935c5 |

Registrazioni CC0 da OpenGameArt scaricate dall'autore il 21/10 in `download/` (fuori da git): non chiedono crediti, si citano
lo stesso quando entrano nel gioco.

| Pacchetto | Autore | Licenza |
|---|---|---|
| Medieval Sound Effects: Weapon Textures e Weapon on Weapon | Ben Jaszczak, Brian Nelson (Still North Media) | CC0 |
| Impact | qubodup | CC0 |
| Footsteps Leather, Cloth, Armor | HaelDB | CC0 (anche OGA-BY 3.0; si usa CC0) |

**Nel gioco dal 21/10 (strato 1 del piano, D0901):** 116 suoni del combattimento in `/Game/Ragequit/Audio/Combat`, costruiti
da `tools/combat-sounds.json` (fonte e strato per strato di ogni suono) con `tools/build-combat-sounds.py`; i WAV costruiti stanno
in `unreal/SourceArt/Audio/Combat` (fuori da GitHub). Fonti: Small Sound Kit, General Whoosh, Whoosh SFX Pack Lite, LOW END
IMPACTS Vol. One, Essential Footsteps, Interface & Item Sounds, Health & Damage SFX, Monster Roars & Growls, SFX Essentials Free
Sample, SoundMorph MetaSounds, Free Realistic Sword (Fab Standard); Medieval SFX, Impact di qubodup e Footsteps di HaelDB (CC0); onde
gia' nel gioco di Free Sounds Pack e Free Modular Magic SFX (CC BY 4.0, attribuzione sopra). 100 RPG Fantasy SFX e 65 Free Sounds
non si usano: su Fab sono segnati fatti con l'AI (D0348).

Esclusi perché fatti con l'AI (D0348) o solo per Unity: elenco nel piano, §9. I nuovi eroi Paragon (Yin, Kwang, Kallari,
Khaimera, Shinbi, Phase, Wukong, The Fey, Riktor, Steel) hanno lo stesso limite sul marchio PARAGON degli altri.
