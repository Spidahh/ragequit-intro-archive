# RAGEQUIT — Sistema delle classi

Aggiornato il 21/10/2026 — dati rimessi al gioco di oggi (PIANO-COMPLETO §7): la freccia tesa fa solo 120 (parte solo tesa del tutto, non più 24-120), Overwatch 120 a freccia (non 96: la definitiva non colpisce da sé), la Pyromancer tiene in mano la bambola e l'ago di Morigesh, i due problemi della Tempestblade. Prima: 20/10/2026 — l'arco della Deadeye scocca solo a tensione completa (D0849); prima: 20/10/2026 — correzioni da revisione del codice (D0846): armi, scudi, ali e volti seguono le clip di corsa, salti a cinque clip, barcollata con la clip dell'eroe, colpi a distanza dalla mano che si vede, dodici difetti delle abilità. Prima: 18/10/2026 — ritmo e risorse (D0836, studio STUDI/RITMO-RISORSE-AUDIO-17-10.md): la riserva paga solo le difese (parate e guardia senza ricarica, fughe a 25 senza ricarica), le abilità d'attacco a sola ricarica; l'arco della Deadeye si tende sul tasto del colpo e il tasto destro è la freccia che inchioda; i dardi dei maghi a una cadenza; scatti della mischia più frequenti; definitive a 700. Prima: 17/10/2026 — revisione delle animazioni (D0826): corpi degli eroi rifatti (una clip per direzione, gambe verso dove si va, passo e cadenza, rotazione sul posto, mira alta e bassa, morti proprie, Sparrow con l'arco abbassato fuori dal combattimento) e i gesti di nove classi in tempo coi loro tasti; ogni gesto nuovo dura in tutto quanto quello di prima (un'azione dura finché il suo montaggio non sfuma: quanto si resta fermi è una regola del gioco). Gioco guardato: pacchetto Shipping package-20261021-090630-749 (21/10 mattina), unreal 48a048cf; server online 0.3.31-1 (stesso codice).

**Regola dell'autore (D0775):** le classi devono essere complete nel disegno prima di implementarle. Questo file si aggiorna PRIMA di toccare una classe.
Generato da `tools/classi.py` da `DOCUMENTAZIONE/CLASSI/classi.json` (disegno), dall'ultima esportazione dei kit e dall'ultimo controllo delle animazioni. Non si modifica a mano.

Le dieci classi come sono nel gioco dopo i lavori del 13–14/10: il corpo, le sei abilità col gesto che fa il corpo (guardato in foto), cosa è cambiato e cosa resta da sistemare. Questo documento si aggiorna prima di toccare una classe.

## In breve

60 abilità guardate in foto: 60 con un gesto adatto, 0 debole, 0 sbagliato.

- Tre classi hanno un corpo nuovo. Cryomancer è Aurora (ghiaccio, con la sua spada), Tempestblade è Serath (ali, con una spada nostra), Geomancer è Rampage (scaglia massi).
- Nessun gesto sbagliato né debole. Prima erano 7 sbagliati e 12 deboli su 60. Il 14/10 mattina anche gli ultimi cinque deboli hanno un gesto vero del loro eroe: il Deadeye salta davvero, il Tempestblade para con la spada alta, la Cryomancer si inginocchia, il Geomancer si chiude a palla in aria, la Sentinel chiude l'elmo dietro lo scudo.
- Tre definitive nuove al posto dei tre salti uguali: Frenzy (Juggernaut), Last Bastion (Sentinel), Stone Ring (Geomancer). Il salto resta all'Impaler.
- Il colpo base non toglie più la magia. Misurato: prima 24 colpi di catena su 48 interrompevano un lancio, ora 0. Solo un'abilità a pagamento interrompe.
- I tiratori tirano al ritmo dei dati (Deadeye una freccia ogni 0,56 s invece di 0,74), chi sbaglia paga mezzo secondo, chi colpisce in mischia non resta indietro.
- Le aree si vedono prima di colpire: cerchio a terra da quando premi, forme vere, bordo più spesso che resta un secondo.
- Nei passi laterali maghi, Tempestblade, Juggernaut e Reaper tengono busto e arma verso il mirino. Impaler, Sentinel e Deadeye restano nella loro guardia, con l'arma al nemico.
- Ogni abilità ha una frase vera nel menu, coi numeri dei dati.
- Online: il server rifiutava i colpi arrivati un attimo prima della fine del recupero (a 100 ms di ritardo 20 su 43): ora li tiene, 0 rifiutati. Dice a chi gioca quando un fendente è andato a vuoto, giudica la lama dove sta chi colpisce camminando (27 fendenti su 27 d'accordo) e la controlla dall'istante giusto: il primo colpo della Sentinel, che mancava una volta su due, colpisce 30 volte su 30.

## Il roster

| Classe | Ruolo | Corpo | Arma | Come si difende | Cosa ha solo lei |
|---|---|---|---|---|---|
| Deadeye | A distanza · precisione | Sparrow | il suo arco | Schiva: Evasive Leap fa passare i colpi a vuoto. Non para. | È l'unica che tende l'arco sul tasto del colpo, con una freccia che inchioda e una definitiva di cinque frecce piene che trapassano. |
| Impaler | Ibrido · media distanza con la lancia | Feng Mao | la sua asta | Nessuna parata e nessuna schivata vera: si difende con la portata e col salto (Vault). | Il palo piantato nel terreno e l'inchiodare il nemico contro palo o muro. |
| Pyromancer | A distanza · territorio | Morigesh | la bambola e l'ago di Morigesh, che restano in mano anche mentre lancia | Schiva: Backdraft è un salto indietro che fa passare i colpi a vuoto (0,25 s). Non para. | Il campo che trasforma le altre sue magie: nessun'altra classe ha magie che si combinano così. |
| Voidseer | A distanza · manipolazione | Gideon | nessuna (mani e portale) | Si teletrasporta (Phase Step) e stordisce chi gli è vicino (Stasis Pulse: stasi). Non para e non schiva. | Il teletrasporto, la linea che torna a colpire, il blocco delle abilità del nemico (lock). |
| Tempestblade | Ibrido · movimento e aria | Serath | una nostra spada nella mano sinistra (la sua mazza non si vede) | Para: Perfect Guard ferma un colpo e rimanda indietro i dardi; costa 10 di stamina, senza ricarica, e riuscita li restituisce. Ha anche un passo veloce. | È l'unica che lancia in aria il nemico e lo colpisce al volo, e l'unica che rimanda indietro i dardi. |
| Reaper | Mischia · assassino | Sevarog | falce (nostra, al posto del suo martello) | Nessuna guardia: passa attraverso i nemici con lo scatto e sparisce per un attimo. | Rampino, invisibilità, sangue, esecuzione: quattro meccaniche che ha solo lui. |
| Cryomancer | A distanza · gelo | Aurora | la sua spada di ghiaccio (la usa come bacchetta) | Schiva: Ice Glide fa passare i colpi a vuoto (0,2 s). Non para. | La catena gelo → congelamento → frantumazione e l'accecamento della definitiva. |
| Juggernaut | Mischia · sfondamento | Grux | le sue due clave | Non para e non schiva: Ironhide (per 1,8 s i colpi non lo interrompono e prende il 30% in meno). | È l'unico che prende il corpo del nemico e lo usa contro l'arena (trascina, tira, inchioda al muro) e l'unico che non può essere interrotto. |
| Geomancer | A distanza · terra | Rampage | nessuna: le sue mani | Schiva: Stone Step è un balzo che fa passare i colpi a vuoto (0,35 s). Il muro ferma corpi e dardi. | È l'unico che costruisce muri veri nell'arena: uno solo, o sei in cerchio attorno al nemico. |
| Sentinel | Mischia · difesa | Terra | la sua ascia e il suo scudo | Para e non schiva: è la classe della parata. Lo scudo (Aegis Parry) si tiene quanto dura la stamina, senza ricarica: alzato proprio quando arriva il colpo para, dopo blocca; Shield Advance blocca davanti mentre avanza. | È l'unica con una guardia tenuta e l'unica che blocca il nemico sul posto (root). |

### Le regole dell'autore che ogni classe deve rispettare

- Nel roster ci devono essere: arco, più armi da mischia, magie, blocco, cura, salto e presa al volo, muri, prese, stun, freeze, lock, invisibilità, accecamenti, root, colpi caricati, rampini, teletrasporti, balzi, parate. (6/10)
- Le classi sono diverse fra loro, ognuna ha un modo per uscire dallo scontro; kit spettacolari: esplosioni, sbalzi, freeze, stun, attacchi speciali. Le idee si prendono dai giochi action PvP con abilità. (7/10)
- Ogni classe si difende in un modo suo. I maghi non parano: schivano o si teletrasportano. C'è la classe che para e non schiva. (13/10)
- Più magie e classi a distanza, meno mischia tutta uguale; più spesa di risorse, meno spam. (11/10)
- Un colpo base non deve impedire a un mago di lanciare; i colpi non devono spingere il nemico così lontano da rompere la combo; chi sbaglia deve poter essere punito. (12/10)
- Un modello si sceglie se combacia col personaggio e con la sua arma; per un mago prima si sa quali magie deve fare, poi si controlla che il corpo abbia i gesti. (7/10 e 13/10)
- Rampino del Reaper sul muro, invisibilità dopo Shadow Slip, nemico trascinato nella carica di Juggernaut e Impaler: approvati. La palombella di Ember Field: no. (7/10)
- Le classi complete nel disegno prima di implementarle. Solo la skin principale. (13/10)

## Deadeye — A distanza · precisione

Corpo oggi nel gioco: Sparrow. Arma: il suo arco (visibile: sì). Vita 900, velocità 5,6 m/s.

L'arciere. Tiene premuto per tendere l'arco e la freccia parte solo quando l'arco è teso del tutto: lasciato prima, non parte niente. Inchioda chi gli corre addosso e si allontana col salto.

- Difesa: Schiva: Evasive Leap fa passare i colpi a vuoto. Non para.
- Uscita: Evasive Leap (salto di 5 m nella direzione in cui ti muovi; 25 di focus, senza ricarica), la freccia che inchioda e la distanza.
- Solo lei: È l'unica che tende l'arco sul tasto del colpo, con una freccia che inchioda e una definitiva di cinque frecce piene che trapassano.

| Tasto | Abilità | Cosa fa oggi | Danno · costo · ricarica | Animazione | Giudizio | Nota | Effetti | Suoni |
|---|---|---|---|---|---|---|---|---|
| LMB | Drawn Arrow | Freccia tesa: si tiene premuto, l'arco è teso del tutto in 0,8 s e solo allora la freccia può partire (120 di danno, 100 m/s, 16 m); lasciato prima, l'arco si abbassa e non parte niente. Si tiene tesa quanto si vuole; mentre tende cammina al 70%. | 120 · gratis · — | RMB_Drawback, RMB_Loop, RMB_Fire | ADATTA | Tende l'arco davvero mentre tieni premuto, lo tiene teso quanto vuoi e poi rilascia: i tre gesti del tiro caricato di Sparrow (era il Power Shot del tasto destro). | P_Sparrow_PrimaryAttack, P_Sparrow_Primary_Ballistic_HitWorld | SW_RQ_Bow_Shoot, SW_RQ_Arrow_Thunk, SW_RQ_Bow_Draw, SW_RQ_Arrow_PassBy |
| RMB | Pinning Arrow | Freccia che inchioda: 48 di danno, chi la prende è radicato 0,8 s; 10 s di ricarica. | 48 · gratis · 10 s | idle, R_Ability_Fast_Fire | ADATTA | Il tiro veloce e pesante di Sparrow (R_Ability_Fast_Fire), la corda a 0,22 s. | P_Sparrow_RMB, P_Sparrow_Primary_Ballistic_HitWorld | SW_RQ_Bow_ShootHeavy, SW_RQ_Arrow_Thunk, SW_RQ_Arrow_PassByHeavy, SW_RQ_Warn_Deadeye_Pin |
| Q | Piercing Arrows | Piercing Arrows (era Rapid Draw): le prossime tre frecce, entro 6 s, trapassano ogni nemico sulla loro linea; ognuna si tende per intero (0,8 s). | — · gratis · 12 s | Cast | ADATTA | Nessun gesto con la mano: resta in mira e finché dura le frecce escono col suo tiro veloce. | — | SW_RQ_Bow_Nock, SW_RQ_Warn_Deadeye_Pierce |
| E | Spread Shot | Tre frecce a ventaglio che rallentano. | 82,5 · gratis · 8 s | idle, R_Ability_Fast_Fire | ADATTA | Ventaglio di frecce col gesto del tiro rapido dell'eroe. | P_Sparrow_PrimaryAttack, P_Sparrow_Primary_Ballistic_HitWorld | SW_RQ_Bow_Volley, SW_RQ_Arrow_Thunk, SW_RQ_Arrow_PassBy, SW_RQ_Warn_Deadeye_Spread |
| Shift | Evasive Leap | Salto di 5 m nella direzione in cui ti muovi: i colpi vanno a vuoto mentre ti stacchi. 25 di focus, senza ricarica. | — · 25 · — | Jump_Start, Jump_Apex, Jump_Land, Jump_Recovery | ADATTA | Salta davvero, con le sue animazioni di salto: si raccoglie, si stacca da terra fino a 1,1 m, atterra accucciata 5 m più in là dopo mezzo secondo e torna in mira. | P_Sparrow_DustKickUp, NS_Dirt_Explosion_Small | SW_RQ_Move_Dash |
| R | Overwatch | Per 7 s le prossime cinque frecce trapassano e arrivano a 18 m, 120 l'una; ognuna si tende per intero; cammini al 70%. | 120 a freccia · gratis · 65 s | Q_Ability | ADATTA | Arco puntato in alto e poi cinque frecce forti: gesto suo. | — | SW_RQ_Bow_Overwatch, SW_RQ_Warn_Bowdraw |

**Cambiato nel gioco il 13–14/10:**
- 20/10 (D0846): correndo con l'arco basso l'arco non entra più nella testa: corda, freccia e arco seguono le sue clip (prima tornavano alla posa da ferma col tiro teso, girati di 180°). Le frecce partono dall'arco che si vede, non dalla mano del manichino nascosto. I tocchi del tasto durante il recupero dopo una freccia restano in attesa; uno Shift che non può partire (radicata, senza focus) non butta più la freccia tesa. Salto: stacco, salita, pre-atterraggio e atterraggio suoi.
- Power Shot: mentre tieni premuto il corpo tende l'arco, poi rilascia.
- Rapid Draw: tolto il gesto con la mano; resta in mira e le frecce escono col tiro veloce.
- Lo scatto si chiama Evasive Leap ed è un salto: Sparrow non ha capriole né scivolate.
- Quickshot: la corda parte con la freccia (prima partiva 0,16 s prima).
- Una freccia a segno ogni 0,56 s, come dicono i dati (prima 0,74).
- Evasive Leap è un salto vero (14/10): 1,1 m sopra terra, 5 m, 0,5 s in aria; la freccia veloce si arma quando atterra, anche in rete. 5 m e non 4 perché scappi quanto lo scatto di prima: quando atterra è 2,2 m davanti a chi cammina (con 4 m era 1,2).
- 18/10 (D0833, D0836): l'arco si tende sul tasto del colpo (un tocco 24, tesa al massimo 120: roster-v3-20261018-022232); il tasto destro è la freccia che inchioda (48 e radice, misurati); Rapid Draw e Overwatch danno frecce piene subito.
- 20/10 (D0849, l'autore: «l'arciere deve tener premuto il tasto sinistro per scoccare [...] e senno completa il colpo non scocca»): la freccia parte solo a tensione completa; lasciato prima, la tensione si annulla e non parte niente, anche sul server. Prima un tocco tirava la freccia meno tesa (24) e le frecce di Rapid Draw, Overwatch e del salto partivano a un tocco, una ogni 0,6 s; ora anche quelle si tendono, solo più in fretta. Il bot lascia la corda solo a tensione completa. Tolta la memoria del tasto aggiunta la mattina del 20/10: faceva ripartire la tensione dopo il rilascio.
- 20/10 pomeriggio (D0852, l'autore: «le frecce solo tese se no non partono [...] nessuna classe deve avere una cazzo di mitragliatrice come attacco base»): ogni freccia si tende per intero, anche quelle delle abilità (la mattina Overwatch e Rapid Draw tendevano in 0,25 s, un ciclo di 0,75 s da 120: la mitragliatrice). La Q si chiama Piercing Arrows: tre frecce che trapassano (il Piercing Shot di Sparrow nel suo gioco); Overwatch dura 7 s perché cinque tensioni piene ci stiano; il salto non accorcia più la tensione. Misurato coi tasti veri (no-machine-gun): tenuto 3,5 s niente, lasciato teso una freccia, sedici tocchi niente.

**Ancora da sistemare:**
- Freccia tesa (era Power Shot): all'inizio abbassa l'arco di scatto dalla posa di riposo.

## Impaler — Ibrido · media distanza con la lancia

Corpo oggi nel gioco: Feng Mao. Arma: la sua asta (visibile: sì). Vita 1250, velocità 5,6 m/s.

Il lanciere. Tiene il nemico alla distanza della sua asta, pianta un palo nel terreno e ci inchioda contro chi sbaglia posizione.

- Difesa: Nessuna parata e nessuna schivata vera: si difende con la portata e col salto (Vault).
- Uscita: Vault: salta oltre il nemico; 25 di stamina, senza ricarica.
- Solo lei: Il palo piantato nel terreno e l'inchiodare il nemico contro palo o muro.

| Tasto | Abilità | Cosa fa oggi | Danno · costo · ricarica | Animazione | Giudizio | Nota | Effetti | Suoni |
|---|---|---|---|---|---|---|---|---|
| LMB | Long Reach | Tre colpi lunghi con l'asta; il terzo spinge indietro. | 108 + 124,2 + 140,4 · gratis · — | Melee_A_Med_InPlace, Melee_B_Med_InPlace, Melee_C_Med | ADATTA | Tre colpi lunghi con l'asta: gesti suoi; i primi due sono le sue copie sul posto (da fermo il bacino scattava avanti di un metro e poi tornava indietro). Mentre colpisce cammina a passo pieno; un colpo a vuoto costa mezzo secondo. | — | — |
| RMB | Skewer | Affondo di 7 m che trascina il primo nemico; contro un muro o il palo lo blocca 0,6 s. | 255 · gratis · 10 s | Dash_Attack | ADATTA | Affondo in corsa che trascina: gesto suo. Il nemico trascinato ora resta a 1,6 m davanti a lui (prima finiva a 6 m). | — | SW_MagicWeapon_Thrust_1, SW_RQ_Warn_Impaler_Skewer |
| Q | Stake | Lancia il palo fino a 12 m: colpisce, oppure resta piantato 4 s e sbarra la strada. Ricarica 6 s. | 150 · gratis · 6 s | Primary_D | ADATTA | Il palo parte da un colpo della sua asta (Primary_D). È un fendente largo più che un affondo: la punta è avanti per un attimo. | SM_WM_Spear | SW_RQ_Spear_Throw, SW_RQ_Stake_Thunk, SW_RQ_Warn_Impaler_Stake |
| E | Leg Sweep | Spazzata bassa attorno che rallenta. | 217,5 · gratis · 9 s | SlowAbility | ADATTA | Spazzata bassa: gesto suo. | — | SW_MagicWeapon_Swing_1, SW_RQ_Warn_Impaler_Sweep |
| Shift | Vault | Salto di 7 m oltre nemici e muretti. | — · 25 · — | LaunchPad | ADATTA | Il suo salto (LaunchPad): l'asta sopra la testa e le gambe raccolte, per i 7 m del salto alto 2,2 m (prima era Dash_Ability, un affondo da terra portato in volo). | P_FengMao_Ultimate_JumpDust, NS_Dirt_Explosion_Small | SW_RQ_Move_Leap, SW_RQ_Land_Light |
| R | Impaling Descent | Salto alto e caduta su un punto: stordisce e spinge via. | 700 · gratis · 65 s | Ultimate_V2 | ADATTA | Ultimate_V2: l'asta sopra la testa in volo e giù nel terreno all'atterraggio. L'Ultimate di prima alzava da solo il bacino di 3,76 m sopra l'arco del salto: volava a circa 8 m. | P_FengMao_Ult_Impact_01 | SW_RQ_Move_Leap, SW_RQ_Land_Heavy, SW_RQ_Warn_Descent |

**Cambiato nel gioco il 13–14/10:**
- 20/10 (D0846): l'asta corre con le sue clip (17 cm e 33° fuori posto prima); lo Stake parte dalla mano e, senza colpire nessuno, resta piantato al piede del muro o alla fine dei 12 m, come dice il disegno; Skewer non colpisce più prima dello scatto; la pioggia confronta i piedi; Vault e Impaling Descent: un tasto premuto in volo resta in attesa, e il salto verso un piano più basso esplode quando tocca terra.
- Stake parte da un colpo d'asta suo, non più da un gesto della mano; arriva a 12 m e torna ogni 6 s (prima 8 m e 12 s): è la sua arma a distanza.
- Il nemico trascinato da Skewer resta davanti a lui, a portata.
- Tolta dal testo di Vault la spinta all'atterraggio, che non c'è mai stata.
- 18/10 (D0836): la fuga va a sola stamina (25, senza ricarica), le abilità d'attacco a sola ricarica.
- 20/10: Vault e Impaling Descent: il colpo a terra 10 dB più forte, lo slancio 8 dB più piano (erano invertiti rispetto agli altri suoni).

**Doppioni:**
- Skewer e Collision Course del Juggernaut sono la stessa carica che trascina: l'avevi approvata tu per tutte e due.

**Ancora da sistemare:**
- Non ha una difesa sua: si difende con la portata e col salto.
- Il lancio del palo è un fendente, non un affondo pulito.

## Pyromancer — A distanza · territorio

Corpo oggi nel gioco: Morigesh. Arma: la bambola e l'ago di Morigesh, che restano in mano anche mentre lancia (visibile: sì). Vita 900, velocità 5,4 m/s.

La maga del fuoco. Mette a terra un campo di braci e le altre sue magie cambiano quando lo attraversano: l'onda lo fa esplodere, la lancia diventa più forte e trapassa.

- Difesa: Schiva: Backdraft è un salto indietro che fa passare i colpi a vuoto (0,25 s). Non para.
- Uscita: Backdraft: salto indietro di 4,5 m con una fiammata davanti; 25 di mana, senza ricarica.
- Solo lei: Il campo che trasforma le altre sue magie: nessun'altra classe ha magie che si combinano così.

| Tasto | Abilità | Cosa fa oggi | Danno · costo · ricarica | Animazione | Giudizio | Nota | Effetti | Suoni |
|---|---|---|---|---|---|---|---|---|
| LMB | Fire Bolt | Un dardo di fuoco. | 105 · gratis · 1,3 s | PrimaryAttack_B_Slow | ADATTA | Lancio dalla mano (PrimaryAttack_B_Slow): il fuoco parte col lancio. | P_Dragon_Fireball_Projectile, P_Dragon_Fireball_WorldImpact | SW_MagicCast_FireBall1_1, SW_MagicImpact_Fire_1 |
| RMB | Ember Field | Campo di braci a terra per 4 s: brucia e rallenta del 10%. | 24 · gratis · 12 s | Idle, Ability_Q | ADATTA | Ability_Q: un attimo della sua posa, la mano che si carica un po' più lenta, il campo parte quando la mano lancia (prima 0,25 s dopo). | NS_Fire_Floor_01 | SW_MagicCast_FireBall2_1, SW_MagicSpell_FireTrail_1, SW_RQ_Warn_Pyro_Field |
| Q | Flame Wave | Onda di fuoco larga 2 m; se attraversa il campo lo fa esplodere. | 225 · gratis · 10 s | Idle, Ability_RMB | ADATTA | Ability_RMB con lo stesso attacco: l'onda parte col lancio (prima 0,18 s dopo). | P_Dragon_Fireball_Projectile, P_LM_Explo_Hit_World | SW_MagicSpell_FireTrail_2, SW_MagicImpact_Fire_2, SW_RQ_Warn_Pyro_Wave |
| E | Fire Lance | Lancia di fuoco; attraverso il campo è più forte e trapassa. | 255 · gratis · 12 s | Idle, PrimaryAttack_C_Slow | ADATTA | PrimaryAttack_C_Slow con un attimo di posa: la lancia parte col lancio (prima 0,23 s dopo). | P_Dragon_Fireball_Projectile, P_Dragon_Fireball_WorldImpact | SW_MagicCast_FireBall2_2, SW_MagicImpact_Fire_3, SW_RQ_Warn_Pyro_Lance |
| Shift | Backdraft | Salto indietro di 4,5 m che schiva, con una fiammata davanti. | — · 25 · — | Ability_E_Targeting_Start | ADATTA | Si piega e salta indietro. | P_Dragon_Fireball_WorldImpact | SW_MagicCast_FireBall1_2 |
| R | Volcanic Break | Tre esplosioni una dopo l'altra su una linea di 15 m: fanno barcollare e spostano di 1,5 m lungo la linea. | 700 · gratis · 65 s | Ability_R | ADATTA | La sua definitiva (Ability_R) dal suo mezzo secondo: l'effetto cade sul colpo (prima mezzo secondo prima). | P_LM_Explo_Hit_World | SW_MagicSpell_MagmaEruption_1, SW_MagicSpell_RockExplosion1_1, SW_RQ_Warn_Eruption |

**Cambiato nel gioco il 13–14/10:**
- 20/10 (D0846): il volto segue le clip (occhi girati di 100° prima); Fire Bolt e Fire Lance partono dalla mano; Volcanic Break colpisce anche chi sta 1,6 m più in alto (piedi contro piedi); Ember Field e le aree tengono l'altezza del punto mirato; non salta più su e giù in aria (la salita in ciclo).
- Volcanic Break non toglie solo vita: fa barcollare e sposta chi prende.
- Un dardo a segno ogni 0,61 s, come dicono i dati (prima 0,76).
- Nei passi laterali il busto resta verso il mirino.
- 18/10 (D0836): la fuga va a sola mana (25, senza ricarica), le abilità d'attacco a sola ricarica.
- 18/10 (D0833): il dardo base a una cadenza di 1,05 s (non più a mitragliatrice).
- 20/10: la sua voce 8,7 dB sotto quella degli altri eroi (registrazione di Morigesh): VoiceVolume 2,24 (+7 dB). Fire Lance nel campo va più veloce (75 m/s; andava a 40, più piano dei suoi 60). Mentre lancia cammina al 70% come gli altri maghi (aveva un ritmo suo, 64%).
- 20/10 pomeriggio (D0852: «nessuna classe deve avere una cazzo di mitragliatrice come attacco base»): l'attacco base parte una volta per pressione (tenuto premuto ne mandava uno ogni 1,05 s finché era giù) e al massimo ogni 1,3 s, il ciclo pieno dell'arco; misurato coi tasti veri: tenuto 3,5 s un colpo, cliccando un colpo ogni 1,5 s.

**Ancora da sistemare:**
- Il corpo è una strega dei veleni: fa i gesti giusti ma non ha niente del fuoco addosso.
- Da controllare in partita: al momento del lancio il fuoco nasce sulla mano.

## Voidseer — A distanza · manipolazione

Corpo oggi nel gioco: Gideon. Arma: nessuna (mani e portale) (visibile: non serve). Vita 900, velocità 5,4 m/s.

Il mago del vuoto. Tira linee che colpiscono due volte, tira a sé con un nodo di gravità, congela chi gli sta addosso, si teletrasporta.

- Difesa: Si teletrasporta (Phase Step) e stordisce chi gli è vicino (Stasis Pulse: stasi). Non para e non schiva.
- Uscita: Phase Step: teletrasporto vero di 6 m; 25 di mana, senza ricarica.
- Solo lei: Il teletrasporto, la linea che torna a colpire, il blocco delle abilità del nemico (lock).

| Tasto | Abilità | Cosa fa oggi | Danno · costo · ricarica | Animazione | Giudizio | Nota | Effetti | Suoni |
|---|---|---|---|---|---|---|---|---|
| LMB | Null Bolt | Un dardo del vuoto. | 105 · gratis · 1,3 s | Primary_Attack_A_Medium | ADATTA | Dardo dalla mano: gesto suo. | P_Gideon_Primary_Projectile, P_Gideon_Primary_HitWorld, NS_Hit_Mystic_Once | SW_MagicCast_Projectile1_1, SW_MagicImpact_Barrier_1, SW_RQ_Bolt_Fly_Void, SW_RQ_Bolt_PassBy_Dark |
| RMB | Echo Line | Una linea che colpisce e blocca le abilità per 1 s; poi la stessa linea colpisce di nuovo. | 210 · gratis · 10 s | RMB_Cast | ADATTA | Il suo lancio (RMB_Cast): la linea parte quando le mani lanciano (prima 0,15 s prima). | — | SW_MagicCast_Projectile2_1, SW_MagicImpact_Barrier_2, SW_RQ_Warn_Void_Echo |
| Q | Gravity Knot | Un nodo a terra che tira al suo centro e rallenta. | 180 · gratis · 12 s | Burden, Idle | ADATTA | Burden: l'ultimo tratto, col lancio delle due mani; il nodo parte sul lancio (prima Burden a un terzo della velocità, finito prima del lancio). | P_Gideon_Ultimate | SW_MagicFade_Bass1_1, SW_MagicImpact_Barrier_3, SW_RQ_Warn_Void_Knot |
| E | Stasis Pulse | Scoppio tutto attorno: chi è entro 3,5 m resta in stasi 0,8 s (stordito). | 120 · gratis · 14 s | Cosmic_Rift | ADATTA | Braccia alzate e scoppio attorno (Cosmic Rift): lo scoppio quando le braccia scendono (prima 0,35 s prima). | P_Gideon_RMB_NoHitExplosion | SW_MagicCast_Generic1_1, SW_RQ_Stasis_Pulse, SW_RQ_Warn_Void_Stasis |
| Shift | Phase Step | Teletrasporto di 6 m. | — · 25 · — | Torn_Space | ADATTA | Il suo portale (Torn Space) dal suo 0,35 s: entra nel portale 0,12 s dopo il tasto, alla velocità della clip (prima la clip correva 2,1 volte). | P_Portal_Teleport_Enter | SW_MagicFade_Appear1_1 |
| R | Null Ray | Tieni premuto: dopo 0,55 s un raggio fino a 15 m brucia per 1,5 s seguendo la mira; 700 in tutto. Rilasci e si ferma. | 700 · gratis · 65 s | Blackhole_Start | ADATTA | Gesto della sua definitiva. | — | SW_MagicRiser_ChargeShoot1_1, SW_MagicBeam_HoldStrongBlast_1, SW_RQ_Warn_Void |

**Cambiato nel gioco il 13–14/10:**
- 20/10 (D0846): Phase Step sale scale e rampe (si fermava al primo gradino con la mana spesa); Null Bolt parte dalla mano che si vede; Gravity Knot cade all'altezza mirata.
- Gravity Knot tira davvero al centro (prima lasciava il nemico a un metro).
- Un dardo a segno ogni 0,63 s, come dicono i dati (prima 0,78).
- Per chi guarda da un altro computer la linea di Echo Line era disegnata storta di 65 gradi: ora segue la mira.
- Nei passi laterali il busto resta verso il mirino.
- 18/10 (D0836): la fuga va a sola mana (25, senza ricarica), le abilità d'attacco a sola ricarica.
- 18/10 (D0833): il dardo base a una cadenza di 1,05 s (non più a mitragliatrice).
- 18/10 (D0836): Null Ray 700 in 1,5 s; segue la mira ad almeno 240 gradi al secondo (il testo diceva che girava piano: falso).
- 20/10: Echo Line e Null Ray non frantumano più il congelato di Stasis Pulse (+50%, regola del Frostbinder); la finestra fragile dura quanto il congelamento più 0,6 s (era 2,2 s). Il consiglio sul raggio dice che segue la mira.
- 20/10 pomeriggio (D0852: «nessuna classe deve avere una cazzo di mitragliatrice come attacco base»): l'attacco base parte una volta per pressione (tenuto premuto ne mandava uno ogni 1,05 s finché era giù) e al massimo ogni 1,3 s, il ciclo pieno dell'arco; misurato coi tasti veri: tenuto 3,5 s un colpo, cliccando un colpo ogni 1,5 s.

## Tempestblade — Ibrido · movimento e aria

Corpo oggi nel gioco: Serath. Arma: una nostra spada nella mano sinistra (la sua mazza non si vede) (visibile: sì). Vita 950, velocità 5,7 m/s.

La spadaccina dell'aria. Lame di vento a media distanza, parata al momento giusto, un colpo d'ali che solleva il nemico e un tuffo dall'alto su chi è in volo.

- Difesa: Para: Perfect Guard ferma un colpo e rimanda indietro i dardi; costa 10 di stamina, senza ricarica, e riuscita li restituisce. Ha anche un passo veloce.
- Uscita: Slipstream Step: scatto corto; 25 di stamina, senza ricarica.
- Solo lei: È l'unica che lancia in aria il nemico e lo colpisce al volo, e l'unica che rimanda indietro i dardi.

| Tasto | Abilità | Cosa fa oggi | Danno · costo · ricarica | Animazione | Giudizio | Nota | Effetti | Suoni |
|---|---|---|---|---|---|---|---|---|
| LMB | Wind Blade | Una lama di vento fino a 9 m. | 105 · gratis · 1,3 s | RQ_Serath_Primary_Attack_A_Fast_WingsIn | ADATTA | Fendente a una mano: la lama di vento parte dalla spada, alla velocità della clip (andava 1,4 volte). | NS_Hit_Wind_Once, NE_attack01 | SW_RQ_Wind_Cast, SW_RQ_Wind_Hit, SW_RQ_Bolt_Fly_Wind, SW_RQ_Bolt_PassBy_Heavy |
| RMB | Perfect Guard | Parata di 0,45 s: ferma il primo colpo o tiro da davanti, stordisce chi colpisce e rimanda i dardi (i tiri dei kit si fermano soltanto); passa un po' di danno anche dai dardi; 10 di stamina, restituiti se riesce, nessuna ricarica; a vuoto 0,4 s senza parare né schivare. | — · 10 · — | RQ_Serath_Primary_Attack_A_Slow_WingsIn | ADATTA | Parata sua: la spada nella sinistra sale in 0,1 s sopra la testa e resta di traverso, alta e dritta, per tutta la finestra della parata; poi la riabbassa. Il gesto viene da un suo colpo lento (Primary_Attack_A_Slow). | — | SW_RQ_Guard_BladeRaise |
| Q | Rising Gale | Un colpo d'ali solleva il nemico quanto basta perché Skyfall lo prenda in volo. | 195 · gratis · 9 s | E_Ability_Wing_Flap | ADATTA | Apre le ali e le batte: il nemico si solleva col colpo d'ali. | P_WingBlast | SW_RQ_Move_Updraft, SW_RQ_Warn_Tempest_Gale |
| E | Skyfall | Salto e colpo dall'alto; chi è in aria prende più danno ed è stordito. | 240 · gratis · 10 s | In_Air_Melee | ADATTA | Ali spiegate, spada alta, colpo all'atterraggio. | NS_Zap_02_Blue | SW_RQ_Move_WindDive, SW_RQ_Land_Storm, SW_RQ_Warn_Tempest_Skyfall |
| Shift | Slipstream Step | Scatto corto. | — · 25 · — | Sprint_Fwd | ADATTA | Scatto raso terra ad ali tirate indietro: le falcate veloci quanto lo scatto (2,5 volte), poi il suo sprint (prima i piedi scivolavano tre volte il passo). | — | SW_RQ_Move_Dash |
| R | Typhoon Release | Tieni premuto e rilascia: un'onda di vento a 9 m davanti, fino a 12 m a carica piena, solleva in aria chi colpisce (700). | 700 · gratis · 65 s | Q_Ability_Intro | ADATTA | Si raccoglie con le ali socchiuse, poi le spalanca a braccia aperte: la scarica parte attorno. | P_ky_aquaStorm | SW_RQ_Typhoon_Gather, SW_RQ_Typhoon_Release, SW_RQ_Warn_Thunder |

**Cambiato nel gioco il 13–14/10:**
- 20/10 (D0846): ali, spada e protezioni seguono le clip mentre corre (le radici delle ali restano nascoste); Perfect Guard rimanda davvero i dardi (si fermavano a mezz'aria e morivano); Wind Blade dalla mano che si vede; salto completo.
- Corpo nuovo: Serath al posto di Aurora. Spada nostra in mano, la mazza non si vede mai.
- Le ali (di luce azzurra) si aprono in Rising Gale, Skyfall, scatto e definitiva; da ferma e mentre cammina non si vedono.
- Rising Gale solleva di meno: Skyfall premuto subito prende il nemico in volo.
- Nei passi laterali non corre più di profilo: busto e viso verso il mirino.
- Nei menu ha la figura nuova (render ufficiale con la spada), fatta da Codex.
- Perfect Guard ha un gesto suo (14/10): parata alta con la spada di traverso sopra la testa, su in 0,1 s e tenuta fino alla fine della finestra (0,45 s; 0,62 s quando para). Senza la macchia azzurra delle ali sulla schiena.
- 18/10 (D0836): la fuga va a sola stamina (25, senza ricarica), le abilità d'attacco a sola ricarica.
- 18/10 (D0833): il dardo base a una cadenza di 1,05 s (non più a mitragliatrice).
- 18/10 (D0832): Perfect Guard senza ricarica (era 8 s), 10 di stamina restituiti se riesce (+20 se arriva subito dopo un'altra: parry-stamina-20261018-021419); Typhoon Release solleva chi colpisce (lanciato, 700).
- 20/10: Perfect Guard a vuoto ferma 0,4 s come approvato (era 0,64 per la regola dei fendenti); un dardo rimandato rende la stamina e ne passa un po' (D0601). Typhoon arriva a 12 m a carica piena (il testo diceva 9). Passi: la corsa avanti di Serath era letta 1,5 volte più lenta, i piedi remavano (0,80 → 0,26).
- 20/10 pomeriggio (D0852: «nessuna classe deve avere una cazzo di mitragliatrice come attacco base»): l'attacco base parte una volta per pressione (tenuto premuto ne mandava uno ogni 1,05 s finché era giù) e al massimo ogni 1,3 s, il ciclo pieno dell'arco; misurato coi tasti veri: tenuto 3,5 s un colpo, cliccando un colpo ogni 1,5 s.

**Ancora da sistemare:**
- Slipstream Step non è uno scatto suo: è il suo sprint (Sprint_Fwd) fatto andare 2,5 volte più svelto per 0,36 s, poi lo sprint com'è (AM_TB_Step, rq_roster_next.py).
- La spada è SM_WM_Sword, la spada generica della classe ritirata Warmaster, non un'arma di Serath (prepare-v3-weapons.py).

## Reaper — Mischia · assassino

Corpo oggi nel gioco: Sevarog. Arma: falce (nostra, al posto del suo martello) (visibile: sì). Vita 1200, velocità 5,8 m/s.

Il mietitore. Aggancia il nemico e lo tira a sé (o si tira a un muro), lo fa sanguinare, sparisce per un attimo, uccide chi ha poca vita.

- Difesa: Nessuna guardia: passa attraverso i nemici con lo scatto e sparisce per un attimo.
- Uscita: Shadow Slip (6 m attraverso i nemici, invisibile un attimo) e il rampino sul muro; 25 di stamina, senza ricarica.
- Solo lei: Rampino, invisibilità, sangue, esecuzione: quattro meccaniche che ha solo lui.

| Tasto | Abilità | Cosa fa oggi | Danno · costo · ricarica | Animazione | Giudizio | Nota | Effetti | Suoni |
|---|---|---|---|---|---|---|---|---|
| LMB | Reaping Chain | Tre falciate larghe; la seconda e la terza fanno barcollare. | 114 + 131,1 + 148,2 · gratis · — | Swing1_Medium, Swing2_Slow, Idle | ADATTA | Tre falciate larghe: gesti suoi, ognuna alla sua velocità (la seconda andava 1,25 volte, la terza a metà); la terza è Swing1_Slow, la stessa falciata in avanti al suo ritmo pesante. Fa barcollare e lascia il nemico dentro la falce. | NS_VampireSlash_OnlySlash | — |
| RMB | Soul Hook | Una mano spettrale tira il nemico a te; su un muro tira te fin lì. | 202,5 · gratis · 12 s | Soul_Siphon | ADATTA | Mano che afferra e tira: gesto suo (Soul Siphon). | NS_Hit_Dark_Once | SW_RQ_Hook_Chain, SFX_Vefects_Shockwave_05_500ms_Cue, SW_RQ_Warn_Reaper_Hook |
| Q | Soul Drain | Colpisce attorno e ti cura per ogni nemico colpito. | 217,5 · gratis · 14 s | Subjugation | ADATTA | Subjugation dal suo 0,4 s: la mano scende al momento dell'effetto (andava 1,8 volte). | NS_Free_Magic_Hit2 | SW_MagicWeapon_Swing_3, SW_RQ_Warn_Reaper_Drain |
| E | Open Wound | Colpo pesante che fa sanguinare 4 s. | 225 · gratis · 10 s | Idle, Swing1_Medium | ADATTA | Falciata pesante: Swing1_Slow alla sua velocità (prima Swing1_Medium a metà velocità). | — | SW_RQ_Warn_Reaper_Wound |
| Shift | Shadow Slip | Scatto di 9 m attraverso i nemici; invisibile per un attimo. | — · 25 · — | Speedburst | ADATTA | Scatto: il suo Speedburst, chino in avanti con la falce (0,9 s, quanto prima: un'azione dura finché il suo montaggio non sfuma). | NS_Hit_Dark_Once | SW_MagicFade_Appear1_1 |
| R | Reap | Falciata enorme davanti (700) che scaglia indietro; uccide chi ha il 35% di vita o meno. | 250 · gratis · 70 s | Ultimate_Swing_120fps | ADATTA | La grande falciata della sua definitiva. | NS_VampireSlash_OnlySlash | SW_RQ_Reap_Sweep, SW_RQ_Warn_Growl |

**Cambiato nel gioco il 13–14/10:**
- 20/10 (D0846): l'osso della falce segue le clip di corsa e salto (fino a 124° fuori posto prima); i suoi balzi accettano i tasti premuti in volo; nessuna inclinazione aggiunta mentre la lama è viva, su nessuno schermo; salto: caduta e atterraggio suoi (prima clip di 3,3 s a dieci volte).
- La terza falciata non scaglia più via il nemico (1,5 m): lo fa barcollare e lo sposta di 30 cm.
- Chi mette a segno Soul Hook, Soul Drain o Open Wound si libera insieme a chi ha colpito.
- Nei passi laterali il busto resta verso il mirino.
- 18/10 (D0836): la fuga va a sola stamina (25, senza ricarica), le abilità d'attacco a sola ricarica.

**Ancora da sistemare:**
- Il corpo è tutto nero: nelle foto si legge male contro i muri scuri.
- Non cammina: fluttua (il suo corpo è fatto così).

## Cryomancer — A distanza · gelo

Corpo oggi nel gioco: Aurora. Arma: la sua spada di ghiaccio (la usa come bacchetta) (visibile: sì). Vita 900, velocità 5,4 m/s.

La maga del ghiaccio. Raffredda, poi congela chi è già raffreddato, poi frantuma chi è congelato. Le magie partono dalla sua spada di ghiaccio.

- Difesa: Schiva: Ice Glide fa passare i colpi a vuoto (0,2 s). Non para.
- Uscita: Ice Glide: una capriola in avanti di 5,5 m; 25 di mana, senza ricarica.
- Solo lei: La catena gelo → congelamento → frantumazione e l'accecamento della definitiva.

| Tasto | Abilità | Cosa fa oggi | Danno · costo · ricarica | Animazione | Giudizio | Nota | Effetti | Suoni |
|---|---|---|---|---|---|---|---|---|
| LMB | Frost Shard | Una scheggia di ghiaccio fino a 15 m. | 127,5 · gratis · 1,3 s | Primary_Attack_Fast_A | ADATTA | Un taglio rapido verso l'alto: la carica un po' più lenta, il taglio e il resto alla sua velocità; la scheggia parte quando la lama è avanti (prima tutta la clip a 0,7). | NS_Hit_Ice_Once | SW_RQ_Ice_ShardCast, SW_RQ_Ice_ShardHit, SW_RQ_Bolt_Fly_Ice, SW_RQ_Bolt_PassBy_Dark |
| RMB | Ice Lance | Lancia pesante: raffredda 2 s; chi è già raffreddato viene congelato 1 s. | 240 · gratis · 9 s | Ability_Q_Targeting_Intro, Primary_Attack_Slow_D | ADATTA | Un attimo della sua posa pronta, poi carica sopra la testa e cala in avanti: la lancia parte sul colpo (prima tutta la clip a 0,43, al rallentatore). | P_Aurora_Melee_SucessfulImpact | SW_RQ_Ice_LanceCast, SW_RQ_Ice_LanceHit, SW_RQ_Bolt_Fly_Ice, SW_RQ_Bolt_PassBy_Dark, SW_RQ_Warn_Cryo_Lance |
| Q | Permafrost | Si inginocchia e pianta la spada: resti ferma 0,8 s. L'area fino a 12 m è segnata da quando premi; dopo 0,8 s rallenta per 4 s e fa danno. | 45 · gratis · 14 s | Ability_E_V2 | ADATTA | Si inginocchia davvero, col corpo intero: scende in un decimo di secondo, pianta la spada a terra e resta giù fino a 0,8 s, poi si rialza (Ability_E_V2). Ferma finché è in ginocchio. | NS_Hit_Ice_Once, NS_FrostAura | SW_MagicSpell_FreezingWind_2, SW_MagicImpact_Crystal_1, SW_RQ_Warn_Cryo_Permafrost |
| E | Frost Break | Onda larga a 9 m: raffredda; congela chi è raffreddato; frantuma chi è congelato. | 210 · gratis · 12 s | Ability_Q_Targeting_Intro, Primary_Attack_Slow_B | ADATTA | Un attimo di posa, poi il fendente largo dal basso verso l'alto: l'onda parte in cima (prima la clip a 0,42). | NS_Hit_Ice_Once, P_Aurora_Freeze_Whrilwind | SW_RQ_Frost_Cast, SW_RQ_Frost_Break, SW_RQ_Warn_Cryo_Break |
| Shift | Ice Glide | Capriola in avanti di 5,5 m che schiva. | — · 25 · — | Ability_RMB_Fwd | ADATTA | Una capriola nella direzione in cui va: avanti, a destra, indietro, a sinistra (le sue quattro, DirectionMontages); atterra alla fine dello scatto. | P_Aurora_Dash_Flare | SW_RQ_Move_IceGlide |
| R | Whiteout | Dopo 1,2 s un'area fino a 14 m esplode di gelo (700) e acceca 1,5 s chi sopravvive; chi è dentro è rallentato del 45% finché non esplode. | 700 · gratis · 70 s | Ability_R_InPlace | ADATTA | Spada al cielo, braccia aperte, schianto col gelo. | NS_Hit_Ice_Once, P_Aurora_Ultimate_Explode, P_Aurora_Ultimate_InitialBlast | SW_MagicSpell_FreezingWind_2, SW_RQ_Whiteout_Burst, SW_RQ_Warn_Blizzard |

**Cambiato nel gioco il 13–14/10:**
- 20/10 (D0846): la spada segue le clip mentre corre (64° fuori posto prima); Frost Shard e Ice Lance dalla mano destra che si vede; Permafrost e Whiteout all'altezza mirata; atterraggio vero (Jump_Recovery).
- Corpo nuovo: Aurora, l'eroe del ghiaccio, al posto di Serath. La spada di ghiaccio è in mano in ogni momento.
- Nessuna magia è più un colpo di mazza mimato a mani vuote; la definitiva ha un gesto suo.
- Una scheggia a segno ogni 0,91 s, come dicono i dati (prima 1,01).
- Permafrost e Whiteout hanno il cerchio a terra da quando premi.
- Permafrost (14/10): si inginocchia e pianta la spada, ferma per 0,8 s (prima camminava piano mentre lanciava); l'area colpisce sempre 0,8 s dopo il tasto.
- 18/10 (D0836): la fuga va a sola mana (25, senza ricarica), le abilità d'attacco a sola ricarica.
- 18/10 (D0833): il dardo base a una cadenza di 1,3 s (non più a mitragliatrice).
- 18/10 (D0836): Whiteout rallenta del 45% chi è nell'area finché non esplode (misurato: slowed), 700.
- 20/10: la frantumazione è solo sua (la regola del Frostbinder la dava a tutti). Passi: la corsa indietro di Aurora era letta 1,5 volte più lenta (piedi che remavano, 0,57 → 0,07).
- 20/10 pomeriggio (D0852): l'attacco base parte una volta per pressione (tenuto premuto ripeteva); il suo ritmo era già 1,3 s (Geomancer 1,55).

**Ancora da sistemare:**
- Ice Glide è una capriola, non una scivolata.
- Il suo dardo gratis resta il più debole del roster: da rivedere quando si rimisurano i danni.

## Juggernaut — Mischia · sfondamento

Corpo oggi nel gioco: Grux. Arma: le sue due clave (visibile: sì). Vita 1350, velocità 5,6 m/s.

Il bruto. Carica e trascina il nemico contro un muro, lo aggancia e se lo porta ai piedi, lo schiaccia. Per un attimo niente lo ferma.

- Difesa: Non para e non schiva: Ironhide (per 1,8 s i colpi non lo interrompono e prende il 30% in meno).
- Uscita: Collision Course: la carica di 8 m è anche la sua via d'uscita.
- Solo lei: È l'unico che prende il corpo del nemico e lo usa contro l'arena (trascina, tira, inchioda al muro) e l'unico che non può essere interrotto.

| Tasto | Abilità | Cosa fa oggi | Danno · costo · ricarica | Animazione | Giudizio | Nota | Effetti | Suoni |
|---|---|---|---|---|---|---|---|---|
| LMB | Heavy Blows | Due mazzate pesanti; la seconda fa barcollare e tiene il nemico a portata. | 135 + 155,3 · gratis · — | PrimaryAttack_RA, PrimaryAttack_LA | ADATTA | Due mazzate pesanti, destra e sinistra: gesti suoi. La seconda fa barcollare e lascia il nemico a portata di clava. | NE_attack05 | — |
| RMB | Collision Course | Carica di 8 m che trascina il primo nemico; contro un muro lo blocca 0,6 s. | 225 · gratis · 7 s | Stampede | ADATTA | Carica a testa bassa: gesto suo. Il nemico trascinato resta a 1,6 m davanti a lui. | NS_ImpactConcrete | SW_RQ_Move_Dash, SW_RQ_Warn_Jugg_Charge |
| Q | Drag In | Aggancia chi è entro 2,2 m e lo porta ai tuoi piedi. | 217,5 · gratis · 10 s | PrimaryAttack_LB | ADATTA | Il rovescio largo verso di sé, con un passo avanti, alla velocità della clip (andava 1,23 volte): aggancia da 2,2 m e lascia il nemico a 80 cm. | — | SW_RQ_Move_Haul, SW_RQ_Warn_Jugg_Drag |
| E | Ground Crusher | Schianto davanti: più danno a chi è ai tuoi piedi; spinge, e contro un muro blocca. | 360 · gratis · 9 s | DoublePain | ADATTA | Doppia mazzata: gesto suo (DoublePain). | P_Hardknocks_AOE | SW_RQ_Move_Leap, SW_RQ_Slam_Ground, SW_RQ_Warn_Jugg_Crusher |
| Shift | Ironhide | Per 1,8 s i colpi non ti fermano e prendi il 30% in meno. | — · gratis · 12 s | Cast | ADATTA | Pianta una clava a terra e alza l'altra. | NS_Player_Buff_Looping | SW_RQ_Ironhide, SW_RQ_Warn_Jugg_Ironhide |
| R | Frenzy | Ruggito: chi è entro 4,2 m prende danno ed è scagliato via (contro un muro resta bloccato 0,6 s). Poi per 6 s corre e colpisce più in fretta e il 20% del danno torna in vita. | 700 · gratis · 65 s | Ultimate_Roar | ADATTA | Il ruggito della sua definitiva: tutto il corpo. | P_Execute_Roar_Shockwave | SW_RQ_Frenzy_Boom, SW_RQ_Warn_Roar_Titan |

**Cambiato nel gioco il 13–14/10:**
- 20/10 (D0846): Driving Strike e le cariche non colpiscono più nella rincorsa ferma; la via della carica si misura in piano (un nemico su un gradino o in salto veniva mancato).
- La definitiva è Frenzy, il ruggito di Grux, al posto del salto con schianto che avevano anche altre due classi.
- Colpo base: due mazzate invece di tre, e non scaglia più via il nemico.
- Drag In ha il suo gesto (il rovescio verso di sé) e aggancia da dove arriva la clava, non da un metro oltre.
- Drag In e subito Ground Crusher: la spinta ora c'è (prima si perdeva).
- Ironhide ha un gesto suo (la clava piantata), diverso da quello della definitiva.
- Nei passi laterali busto e viso verso il mirino.
- 18/10 (D0836): non paga niente (Ironhide a ricarica): la barra della riserva non c'è; Collision Course a 7 s.
- 20/10: Ground Crusher: il colpo a terra 10 dB più forte, lo slancio 8 dB più piano.

**Doppioni:**
- Collision Course e Skewer dell'Impaler sono la stessa carica che trascina: l'avevi approvata tu per tutte e due.

**Ancora da sistemare:**
- Alla fine della carica non c'è ancora il montante che il suo corpo avrebbe: chiede lavoro in rete, l'ho lasciato.

## Geomancer — A distanza · terra

Corpo oggi nel gioco: Rampage. Arma: nessuna: le sue mani (visibile: non serve). Vita 950, velocità 5,3 m/s.

La bestia della terra. Scaglia massi, spacca il terreno a pugni su una linea, strappa su un muro, solleva chi sta su un'area e chiude il nemico in un anello di pietra.

- Difesa: Schiva: Stone Step è un balzo che fa passare i colpi a vuoto (0,35 s). Il muro ferma corpi e dardi.
- Uscita: Stone Step: balzo di 6 m nella direzione in cui ti muovi; 25 di mana, senza ricarica.
- Solo lei: È l'unico che costruisce muri veri nell'arena: uno solo, o sei in cerchio attorno al nemico.

| Tasto | Abilità | Cosa fa oggi | Danno · costo · ricarica | Animazione | Giudizio | Nota | Effetti | Suoni |
|---|---|---|---|---|---|---|---|---|
| LMB | Heavy Stone | Una pietra pesante fino a 16 m. | 157,5 · gratis · 1,5 s | RQ_Rampage_Ability_RipNToss_Toss_InPlace | ADATTA | Carica il braccio e scaglia il masso sopra la testa: parte dalla sua mano. | P_Rampage_Rock_Flying, SM_Greystone_Statue_Chunks_shard4, P_Rampage_Rock_HitWorld | SW_MagicCast_GroundStrike_1, SW_MagicSpell_RockExplosion1_1, SW_RQ_Bolt_Fly_Stone, SW_RQ_Bolt_PassBy_Heavy |
| RMB | Fault Line | Dopo 0,6 s il terreno si spacca su una linea di 14 m e rallenta. | 255 · gratis · 12 s | Ability_GroundSmash_Start, Ability_GroundSmash_End | ADATTA | Pugni sopra la testa per l'attesa, giù al colpo. Muove solo le braccia: il busto non scende. | NS_Dirt_Explosion_Small | SW_MagicCast_GroundStrike_2, SW_MagicSpell_RockExplosion1_1, SW_RQ_Warn_Geo_Fault |
| Q | Rampart | Alza un muro di pietra per 4 s. | — · gratis · 12 s | Ability_RipNToss_Rip | ADATTA | Si china con le due braccia a terra: il muro sale. | SM_RockBig_001, NS_Hit_Basic_Once | SW_MagicCast_GroundStrike_1, SW_MagicSpell_RockExplosion1_2, SW_RQ_Warn_Geo_Rampart |
| E | Upheaval | Un'area che solleva in aria chi c'è sopra. | 195 · gratis · 12 s | Ability_RMB_Smash | ADATTA | Il suo pugno a terra (Ability_RMB_Smash): alza il braccio un po' più lento e colpisce il suolo all'effetto (prima il Cast comune a metà velocità). | P_Greystone_LeapAOE_GroundSmash | SW_MagicCast_GroundStrike_2, SW_MagicSpell_RockExplosion1_2, SW_RQ_Warn_Geo_Upheaval |
| Shift | Stone Step | Balzo di 6 m che schiva. | — · 25 · — | LaunchPad | ADATTA | Il suo salto (LaunchPad): si accuccia, si chiude a palla in aria fino a 2 m sopra terra, si riapre e atterra a braccia aperte; poca polvere all'arrivo, che non copre il corpo. | P_Rampage_Lunge_Jumpdust | SW_RQ_Move_Leap, SW_RQ_Land_Heavy |
| R | Stone Ring | Muri di pietra in cerchio attorno al punto mirato, con un varco dalla tua parte: tirano verso il centro chi è vicino; dopo 1 s la terra dentro esplode (700) e stordisce 0,8 s. | 700 · gratis · 70 s | Ability_Enrage_Start | ADATTA | Ruggisce a braccia alzate e le butta giù all'effetto, alla velocità della clip (andava 1,17 volte). La sua fine (Ability_Enrage_End) lo terrebbe fermo un secondo in più: non c'è. | P_Rampage_Lunge_ImpactNEW, P_Greystone_LeapAOE_GroundSmash | SW_MagicCast_GroundStrike_2, SW_MagicSpell_RockExplosion1_1, SW_RQ_Warn_Roar_Battle |

**Cambiato nel gioco il 13–14/10:**
- 20/10 (D0846): pinne e mani seguono le clip; Heavy Stone parte dal braccio che si vede; Stone Ring lascia entrare chi tira dentro (i muri lo fermavano fuori dopo 0,1 s); Upheaval e Stone Ring all'altezza mirata.
- Corpo nuovo: Rampage al posto di Greystone. Tutte e sei le abilità hanno un gesto suo; il masso parte dalla sua mano.
- Cammina su due zampe nelle quattro direzioni. È grande: occupa il 40% dell'altezza dello schermo (il Juggernaut il 49%).
- La definitiva è Stone Ring: sei muri in cerchio e poi l'esplosione dentro. Provata nel motore: chi esce dal varco non prende niente.
- Upheaval e la definitiva hanno il cerchio a terra da quando premi.
- Nei menu ha la sua figura (render ufficiale), fatta da Codex.
- Stone Step (14/10): il suo salto a palla, 6 m in 0,65 s e 2 m sopra terra; la polvere dell'atterraggio è piccola e breve.
- 18/10 (D0836): la fuga va a sola mana (25, senza ricarica), le abilità d'attacco a sola ricarica.
- 18/10 (D0833): il dardo base a una cadenza di 1,55 s (non più a mitragliatrice).
- 18/10 (D0836): Stone Ring tira verso il centro chi è vicino ai muri mentre salgono, poi esplode: 700.
- 20/10: lo slancio di Stone Step 8 dB più piano; il consiglio dice i 25 di mana di Stone Step (diceva 15).
- 20/10 pomeriggio (D0852): l'attacco base parte una volta per pressione (tenuto premuto ripeteva); il suo ritmo era già 1,3 s (Geomancer 1,55).

**Ancora da sistemare:**
- La sua corsa su due zampe è disegnata per 2,8 m/s e il gioco lo muove a 5,3: i passi vanno 1,8 volte più svelti e poco più lunghi (la sua gamba, disegnata curva, non regge un passo lungo; heroes-20261017-033410).
- Dopo il lancio il braccio alzato copre il mirino per due decimi di secondo.
- Il sasso in volo è piccolo rispetto ai suoi pugni.

## Sentinel — Mischia · difesa

Corpo oggi nel gioco: Terra. Arma: la sua ascia e il suo scudo (visibile: sì). Vita 1400, velocità 5,6 m/s.

La guardiana. Para col grande scudo, avanza dietro lo scudo, lancia l'ascia per bloccare il nemico sul posto.

- Difesa: Para e non schiva: è la classe della parata. Lo scudo (Aegis Parry) si tiene quanto dura la stamina, senza ricarica: alzato proprio quando arriva il colpo para, dopo blocca; Shield Advance blocca davanti mentre avanza.
- Uscita: Shield Bash: carica di 7 m.
- Solo lei: È l'unica con una guardia tenuta e l'unica che blocca il nemico sul posto (root).

| Tasto | Abilità | Cosa fa oggi | Danno · costo · ricarica | Animazione | Giudizio | Nota | Effetti | Suoni |
|---|---|---|---|---|---|---|---|---|
| LMB | Axe Chain | Tre colpi d'ascia. | 114 + 131,1 + 148,2 · gratis · — | Primary_Melee_B_slow, Primary_Melee_C_slow, Primary_Melee_D_slow | ADATTA | Tre colpi d'ascia: gesti suoi, alla loro velocità (andavano 1,1-1,3 volte). Mentre colpisce cammina a passo pieno. | NE_attack02 | — |
| RMB | Aegis Parry | Tieni premuto: lo scudo ferma colpi e tiri da davanti (passa un quinto, mai mortale); ogni colpo costa stamina, nessuna ricarica; alzato proprio quando arriva il colpo, para. | — · 8 · — | RMB_intro | ADATTA | La guardia di Terra (AM_SN_Guard): alza lo scudo davanti in 0,3 s, lo tiene finché tieni il tasto, trema quando un colpo ci batte, lo abbassa quando lasci. Prima ripeteva l'alzata dal riposo e lo scudo non restava mai su. | — | SW_RQ_Guard_ShieldRaise |
| Q | Shield Bash | Carica di 7 m dietro lo scudo: il primo nemico raggiunto è stordito 0,5 s. | 195 · gratis · 8 s | RMB_melee | ADATTA | Scudo davanti e ascia che cala all'arrivo: il suo colpo di scudo. | — | SW_RQ_Move_Dash, SW_RQ_Warn_Sentinel_Bash |
| E | Highland Hurl | Lancia l'ascia: il nemico colpito resta bloccato sul posto 1 s. | 202,5 · gratis · 11 s | E_ability | ADATTA | Lancio dell'ascia: l'ascia parte quando il braccio lancia (prima 0,12 s prima). | SM_RQ_Axe_1H_FMW_01, P_Terra_DoubleSweep_DustImpact | SW_RQ_Axe_Throw, SW_RQ_Axe_Chop, SW_RQ_Warn_Sentinel_Hurl |
| Shift | Shield Advance | Avanza dietro lo scudo. | — · gratis · 12 s | RMB_helmet_closing | ADATTA | Gesto suo, diverso dalla parata: alza lo scudo davanti, chiude l'elmo e li tiene per tutti gli 1,8 s, anche camminando (RMB_helmet_closing). La parata resta il suo RMB_intro. | NS_Player_Buff_Looping | SW_RQ_ShieldAdvance, SW_RQ_Warn_Sentinel_Advance |
| R | Last Bastion | In ginocchio dietro lo scudo: per 5 s una barriera assorbe 600 e scaglia indietro chi la colpisce con un'arma; quando finisce esplode a 4 m (300 più metà di quanto ha assorbito). Toglie root, gelo, sangue e accecamento. | — · gratis · 65 s | R_Intro | ADATTA | Alza l'ascia e scende su un ginocchio dietro lo scudo; la barriera sale quando le mani scendono (andava 1,29 volte). | P_Terra_Ultimate, P_Terra_Boom_Shockwave | SW_MagicCast_CreatingBarrier1_2, SW_RQ_Bastion_Burst, SW_RQ_Warn_Gong |

**Cambiato nel gioco il 13–14/10:**
- 20/10 (D0846): scudo, ascia e armature seguono le clip mentre corre (scudo 67° fuori posto prima, il polso tiene la sua grandezza); il tasto destro tenuto durante un colpo alza lo scudo appena può (prima andava rilasciato e ripremuto); Highland Hurl dalla mano; non salta più su e giù in aria.
- La definitiva è Last Bastion, quella di Terra: una difesa, non più il salto con schianto.
- La carica è Shield Bash: usa il suo colpo di scudo e stordisce il primo nemico (il menu lo diceva già, i dati no).
- Nei passi laterali resta com'era: lo scudo guarda il nemico.
- Shield Advance (14/10): scudo alzato ed elmo chiuso per tutta l'avanzata, da ferma e camminando; non è più il gesto della parata.
- 18/10 (D0832): la guardia senza ricarica né limite di 2 s (8 per alzarla, ogni colpo bloccato costa in proporzione alla vita che avrebbe tolto, 3,9 per 100); guardia rotta: stordita 1,2 s, poi la riserva piena (parry-stamina-20261018-021305); Shield Bash a 8 s; Last Bastion esplode quando finisce (300 misurato).
- 20/10 (controllo vecchio/nuovo): tolto il marchio della parata ereditato dalla Lifewarden (chi parava restava segnato e i colpi su di lui curavano lei); la guardia si alza con gli 8 di stamina che il tasto dice (chiedeva 10); il consiglio sulla parata dice il vero (troppo presto si blocca e passa un quinto). Passi: le corse laterali di Terra girano la radice di 90 gradi, ora la posa la tiene (scivolava al 40-49%, ora 17%).

**Ancora da sistemare:**
- In Last Bastion l'elmo non si chiude: la sua animazione lo riaprirebbe prima della fine della barriera.

## I corpi — I corpi: scelti e messi nel gioco

Sul PC hai quindici eroi Paragon: ho guardato le loro animazioni (155 fotografate in studio) e ogni classe ha il corpo che combacia con personaggio, arma e gesti. I tre cambi sono nel gioco; le foto qui sotto sono dal gioco.

| Corpo | Chi è | Gesti suoi che contano | Classe | Esito |
|---|---|---|---|---|
| Sparrow | arciera con l'arco | arco teso in tre tempi, tiro veloce, salto | Deadeye | resta |
| Feng Mao | guerriero con l'asta | affondi, spazzata, scatto con l'asta, salto e fendente | Impaler | resta |
| Morigesh | strega, lancia dalla mano | lanci, salto indietro, definitiva | Pyromancer | resta |
| Gideon | mago dei portali, mani libere | dardi, portale, braccia alzate, raggio | Voidseer | resta |
| Aurora | spadaccina del ghiaccio | anello di ghiaccio toccando terra, scivolata in otto direzioni, punta il cielo e schianta | Cryomancer | nuovo |
| Serath | angelo con le ali e una mazza | sale e si tuffa, battito d'ali, scatto ad ali aperte | Tempestblade | nuovo |
| Rampage | bestia di roccia, mani nude | strappa e lancia il masso, pugni a terra, balzo, ruggito; passi in quattro direzioni | Geomancer | nuovo |
| Sevarog | mietitore (con la nostra falce) | mano che tira, scatto, falciata enorme | Reaper | resta |
| Grux | bruto con due clave | carica, montante, doppia mazzata, ruggito | Juggernaut | resta |
| Terra | guardiana con ascia e scudo | guardia, colpo di scudo, lancio dell'ascia, si chiude dietro lo scudo | Sentinel | resta |
| Greystone | cavaliere di pietra, spada e scudo | fendenti, giro, salto con la spada, una deviazione sua | — | libero: lascia il Geomancer. Buono per una classe futura da spada e scudo |
| Countess | vampira con due lame | scatto-teletrasporto, giro, onda dalla lama | — | libera: seconda scelta per il Tempestblade |
| Muriel | androide alato senz'arma | gesti da mago veri, passi in quattro direzioni | — | libera: per un'undicesima classe |
| Murdock | agente col fucile | solo armi da fuoco | — | non adatto al gioco |
| Howitzer | alieno in un'armatura coi razzi | solo razzi e granate | — | non adatto al gioco |

- Gli altri 24 eroi Paragon sono gratis ma non sono scaricati sul PC: non ho potuto guardarne le animazioni, quindi non li propongo. Due da ricordare se un giorno li scarichi: Yin (frusta-lama e vento, rimanda indietro i dardi di suo) per il Tempestblade, Kallari (assassina che sparisce) per il Reaper.
- Gli altri personaggi che hai sul PC (il ghoul, i manichini, i personaggi stilizzati) hanno una grafica diversa da questi: non li uso.

### Cryomancer su Aurora (consigliata)

L'eroe del ghiaccio, con la sua spada di ghiaccio in mano. Sei gesti su sei adatti (Permafrost dal 14/10: si inginocchia e pianta la spada).

- La scivolata di Aurora, vista nel gioco, è una capriola in avanti.

### Tempestblade su Serath (consigliata)

Le ali si aprono nei colpi d'aria; in mano una spada nostra. Sei gesti su sei adatti (la parata dal 14/10: spada alta di traverso, presa da un suo colpo).

- Serath tiene l'arma nella sinistra: anche la spada.

### Geomancer su Rampage (consigliata)

Scaglia il masso, alza i pugni e spacca, strappa su il muro, ruggisce. Sei gesti su sei adatti (Stone Step dal 14/10: il suo salto a palla).

- Scala 0,78: grande, più largo del Juggernaut.
- La catena al polso pende e segue il braccio.

## Problemi comuni a tutte le classi

### 18/10: la riserva paga solo le difese

L'autore, il 17/10 sera (D0831): «La parata nei personaggi è un'abilità che consuma stamina. Perché c'è il cooldown [...] dovresti poterlo usare sempre, è solo che finisci la stamina», «L'arco, l'attacco base, lo devi caricare», «i melee devono cercare di avvicinarsi ai ranged»; il 18/10 ha approvato la proposta dello studio (D0836). Numeri misurati nel gioco (parry-stamina-20261018-021305 e -021419, combat-resources-20261018-021858, roster-v3-20261018-022232 e -022613).

- Riserva: 10 al secondo (piena in 10 s), ferma 0,5 s dopo una difesa pagata, 2 s quando è vuota.
- Parate senza ricarica: Perfect Guard costa 10, riuscita li restituisce (+20 se arriva entro 1,5 s dalla parata prima); la guardia della Sentinel costa 8 per alzarla e tiene finché c'è stamina, un colpo bloccato costa 0,55 per ogni punto percentuale della sua vita che avrebbe tolto; una guardia rotta stordisce 1,2 s e poi la riserva torna piena.
- La parata stordisce 0,9 s un colpo leggero, 0,6 uno pesante.
- Fughe a 25 di stamina, mana o focus, senza ricarica: quattro di fila dalla riserva piena. A zero sono rifiutate; le abilità d'attacco e il colpo base partono lo stesso (vanno a ricarica).
- Ironhide (Juggernaut) e Shield Advance (Sentinel) non sono fughe: niente costo, la loro ricarica. Il Juggernaut non paga niente e non ha la barra.
- Dardi dei maghi: un colpo per pressione, al massimo ogni 1,3 s (Geomancer 1,55); tenuto premuto non ripete (D0852). Un click fino a 0,3 s prima che il dardo sia pronto parte appena può, e il tasto ancora giù alla fine della cadenza manda il suo dardo (20/10 sera, D0857).
- Scatti della mischia più frequenti: Collision Course 7 s, Shield Bash 8 s.
- Definitive a 700 di danno; Whiteout rallenta del 45% chi è dentro finché non esplode, Stone Ring tira verso il centro chi è vicino ai muri, Typhoon solleva, Last Bastion esplode quando finisce (300 più metà di quanto ha assorbito).

### Controllo generale del 15/10: regole che valevano solo a metà

Un riesame di tutto il codice delle abilità (D0806: «fai un controllo generale e un analissi completa dle gioco, risolvi qualaissi problema») ha trovato regole scritte nei testi o nel disegno che il gioco rispettava solo in parte. Nessun numero dei kit è cambiato.

- Root e congelamento fermano anche gli scatti, i salti e il passo nel vuoto del Voidseer: prima fermavano solo la camminata e ogni classe ne usciva con Shift.
- Shadow Slip: l'invisibilità finisce alla prossima abilità anche sul server online (prima restava 1,5 s intera mentre il Reaper colpiva); chi è invisibile non ha nome e barra sopra la testa, non si aggancia col lock e non fa diventare rosso il mirino.
- Perfect Guard ferma anche i tiri dei kit (Fire Bolt, Fire Lance, Stake) e rimanda le frecce che trapassano (Power Shot); uno stordimento la spegne.
- Rampart si rompe coi colpi d'arma e coi tiri dei nemici, non con le pietre del proprio Geomancer.
- Le schivate degli scatti che partono da fermi (Backdraft) cominciano quando il corpo si muove: stessa durata di prima.
- Gravity Knot tira verso il suo centro: lanciato vicino al Voidseer tirava poco o niente.
- Reap esegue anche una Sentinel in Shield Advance sotto il 35%.
- Typhoon Release non si perde premendo Shift; una definitiva che finisce prima del suo effetto rende la carica.
- La parata della Sentinel: il server tiene anche lui l'attesa fra due parate e la durata massima (prima solo il gioco di chi gioca).
- Il Deadeye online non si vede più rifiutare la freccia successiva («NOT READY») per il ritardo della rete.
- Cambiare classe a metà vita non azzera più le attese delle abilità.
- Testi: Axe Chain, Perfect Guard, Reap e la frase del Reaper in inglese corretto; Overwatch dice che Evasive Leap la chiude; Ice Glide dice che schiva alla partenza (0,2 s su 0,36).

### Passi laterali: fatto, classe per classe

Le animazioni laterali di alcuni eroi sono disegnate col corpo di profilo. Ora il busto, le braccia e l'arma tornano verso il mirino e le gambe tengono il passo.

- Acceso per Pyromancer, Voidseer, Cryomancer, Geomancer, Tempestblade, Juggernaut, Reaper.
- Spento per Impaler, Sentinel e Deadeye: il loro passo laterale è una guardia con l'arma puntata al nemico; raddrizzati, l'asta finiva di traverso e lo scudo di taglio.

### Segni a terra: fatto

Avevi scritto: «le skill si vedono male, i segni a terra si vedono male, durano poco».

- Upheaval, la definitiva del Geomancer, Permafrost e Whiteout hanno il cerchio da quando premi, per chi lancia e per chi deve schivare.
- Le forme sono quelle che colpiscono: carica larga 1,9 m e ferma a terra, ventaglio del Deadeye a cono, linee larghe quanto colpiscono, raggio del Voidseer spesso.
- Bordo più spesso; il segno resta circa un secondo dopo il colpo. 35 controlli nel motore, con le foto prima, durante e dopo.
- Da sapere: chi lancia Spread Shot vede ancora una fascia dritta come anteprima; il cono lo vede chi deve schivare.

### Regole del combattimento del 12/10: fatte e misurate

Ogni regola ha la sua misura prima e dopo, presa nel motore.

- Il colpo base non toglie la magia: 24 su 48 prima, 0 su 48 ora. Un colpo pesante fa ancora barcollare.
- Un dardo o un'area a segno conta come colpo a segno: i tiratori tirano al ritmo dei dati.
- Dopo un colpo che fa barcollare, la spinta del tasto successivo passa (Drag In poi Ground Crusher: da 0 a 257 cm).
- Chi colpisce in mischia cammina come chi arretra. Un colpo a vuoto lascia scoperti: il colpo dopo arriva a 0,85 s.
- Chi mette a segno un'abilità di controllo si libera insieme a chi ha colpito (per sei abilità; le due cariche restano 0,25 s indietro).
- Un contrattacco fa reagire di più il corpo ma non lo scaglia più lontano (da 155 a 32 cm).

### Online

Misurando le regole in rete sono usciti difetti che c'erano da giorni. Corretti, misurati nell'editor con ritardo simulato, poi provati sulla copia Shipping (dieci classi) e su un server vero.

- Il server rifiutava il tasto arrivato pochi millisecondi prima della fine del recupero: a 100 ms di ritardo 20 colpi su 43 a vuoto e 26 su 55 sul bersaglio. Ora lo tiene e lo fa partire quando il recupero finisce: 0.
- Quando la lama di chi gioca vede il colpo a segno e il server no, il server glielo dice. Con colpi a vuoto forzati sul server: rifiutati 7 su 38 prima, 0 su 31 ora, e la catena resta in ordine.
- Chi colpisce camminando: il server lo giudicava dov'era un attimo prima e mancava 6 dei 9 colpi che il giocatore vedeva a segno. Ora sono d'accordo 27 fendenti su 27.
- La lama si controllava dal primo fotogramma dopo l'inizio del colpo: un colpo che passava sul corpo in quel pezzetto andava a vuoto. Il primo colpo d'ascia della Sentinel mancava una volta su due; ora 30 su 30. Vale per ogni colpo d'arma.
- Uno stordimento che ferma una magia conta come interruzione: metà dell'energia indietro, il tasto pronto prima, la scritta INTERRUPTED. Un colpo parato resta una parata.

### Danni: da rimisurare

I tempi per togliere tutta la vita col colpo gratis erano stati calcolati prima di queste regole (Juggernaut 5,5–8 s … Cryomancer 13–19 s).

- Con i dardi al ritmo dei dati i tiratori fanno circa un quarto di danno in più al secondo di prima.
- Cryomancer, Tempestblade e Geomancer erano i più deboli: vanno rimisurati in partita prima di toccare i numeri.

### Testi: fatti

Ogni abilità ha un suggerimento di poche parole e una frase che dice cosa fa, in inglese semplice, coi numeri dei dati (la prova dei testi lo controlla).

- Corrette le frasi false: la spinta di Vault, le «frecce forti» di Overwatch, Volcanic Break che ora dice che fa barcollare.

### Come si vedono le abilita' (15/10, D0808)

L'autore: «mancano texture nelle abilita'». Nella ripresa di ogni tasto (fx-view-20261015-115944) i segni a terra delle proprie abilita' erano dischi e bande bianche, i raggi della Voidseer un cilindro del motore bianco, i muri della Geomancer un cubo a mattoni con una cornice blu.

- I propri segni a terra nel colore della propria classe (brace del Pyromancer, viola della Voidseer, ghiaccio della Cryomancer, ocra della Geomancer), l'interno appena accennato; quelli dei nemici restano cremisi.
- Echo Line e Null Ray: un raggio d'energia viola che scorre (M_RQ_KitRay), non piu' il cilindro opaco.
- Rampart e Stone Ring: file di rocce vere (Inferno World Free, SM_RockBig_001); le regole del muro (quanto dura, cosa ferma) non cambiano.
- Le icone delle abilita' restano all'autore (D0769).

## Decisioni

**Decise la notte del 13/10** («Decidi tutto tu seguendo i miei insegnamenti». Se una non ti va, dimmelo: si cambia con un numero o tornando alla versione di prima.):

- 18/10 (D0836): la proposta dello studio del 17/10, con il tasto destro della Deadeye = la freccia che inchioda e la difesa dei maghi a sola stamina.
- I corpi: Cryomancer su Aurora, Tempestblade su Serath con la spada, Geomancer su Rampage.
- Le tre scelte che erano tue: Juggernaut con due mazzate, palo dell'Impaler più frequente, anello di muri per il Geomancer.
- Le definitive di Juggernaut e Sentinel prese dal loro corpo (ruggito, dietro lo scudo).
- Lo scatto del Deadeye è un salto.
- Rampage grande (scala 0,78) anche se il braccio alzato copre il mirino per un attimo dopo il lancio.
- Il busto verso il mirino nei passi laterali solo dove migliora; Impaler, Sentinel e Deadeye restano nella loro guardia.
- Il colore dei segni a terra di chi lancia resta quello dell'abilità (lo studio proponeva di farli bianchi).


## Ordine dei lavori

- Rimisurare i danni in partita con le regole nuove.
- ARMORY e skin secondarie delle tre classi col corpo nuovo: aspettano la fine di tutto, come hai detto.

Prove usate: corpi_nel_gioco: heroes-20261013-225423 (Cryomancer, Tempestblade), heroes-20261014-012749 (Geomancer): strisce al rallentatore di ogni abilità; gesti_e_definitive: kits-mechanics-20261014-035706…041759 (Stone Ring, Last Bastion, Frenzy dal tasto vero), roster-v3-20261014-042201 (61 su 61), kit-states-20261014-042518 (9 su 9), texts-20261014-042828 (5 su 5); regole: combat-rules-20261014-022934 (40 controlli), cast-interruption-20261014-023333, ground-marks-20261014-024648 (35 controlli), net-chaos-20261014-025222…030638; passi: gait-20261014-012356 (dieci classi) e gait-20261014-015211 (le quattro di controllo dopo la scelta classe per classe); studio: clip-studio-20261013-201930 e clip-studio-20261013-205747 (155 animazioni proprie di dodici eroi); dati: ultima esportazione dei kit (tools/unreal/dump-skills.py); cinque_gesti: heroes-20261014-104721, heroes-20261014-110825 e heroes-20261014-114244 (le cinque classi, ogni abilità mentre parte, colpisce, finisce e in movimento), gesti-mech-20261014-104321, gesti-slow-20261014-105513, gesti-guard-20261014-111047, gesti-kneel-20261014-112000 e gesti-leap5-20261014-114059 (i cinque tasti al rallentatore, di lato, di fronte e dal gioco, coi tempi senza foto; il salto da 5 m accanto a una camminata), deadeye-leap-20261014-113500 (il salto in rete, 9 su 9), roster-v3-20261014-113616 (61 su 61), sentinel-20261014-114532 (15 su 15), kit-states-20261014-110144 (9 su 9), combat-resources-20261014-110309 (75 su 75), texts-20261014-114037 (5 su 5); rete_e_lama: net-chaos-20261014-094313…103353 (avviso del colpo a vuoto, colpi a vuoto forzati, chi colpisce camminando), first-blow-20261014-135244, -135718 e -141158 (il primo colpo della Sentinel: 16 su 30, poi 30 su 30), stun-interrupts-20261014-151641 e -154201 (62 controlli), cast-interruption-20261014-151824 e -152049 (8 su 8), gate-20261014-154744 (editor), cooked-combat-20261014-170101…170959 (rete sulla copia Shipping, dieci classi), gallery-shipping-20261014-171057 e -171547 (114 su 114), E:/rq-stage/mt-sera14 (due copie in un duello su Internet); gesti_17_10: skill-gestures-20261017-044720 (i tasti cambiati, dal tasto vero), clip-studio-20261017-042856 (le clip scelte in studio), hero-moves-import-20261017-042540 (picchi delle mani), heroes-20261017-033410 (gambe).
Kit letti da `skills-dump-20261021-103119`, animazioni da `audit-native-animations-20261018-015729`.
