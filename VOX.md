# VOX multi-effects

## ToneLab LE

Guitar multi-effects; distinct from original ToneLab, SE, ST and EX. Checked2026-10-17; partial. Bass suitability and ownership unestablished.

<!-- comparison evidence begins -->

| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression | Built-in expression with under-pedal switch; cannot toggle an assigned volume/amp parameter. External EXP absent from complete port inventory. | [English pp17,55][TLLE-E] |
| K/F/B | **12 / 7 / 17**, text-derived:5 model selectors+6 value knobs+rear LEVEL;4 program+2 BANK+CONTROL footswitches;7 model/insert/cabinet buttons+10 setting/navigation buttons. Pedal switch and rear STANDBY additional. Visual corroboration pending. | [English pp12–18][TLLE-E] |
| Display | Name/value/bank display; diagonal, technology, color and touch unverified. | [English p14][TLLE-E] |
| Dimensions / mass | **500×249×80mm WDH**. **Conflict: Japanese J2 4.5kg; English E1 4.2kg**. Revision/region basis unresolved; do not average. | [Japanese p52][TLLE-J]; [English p55][TLLE-E] |
| Processing / category choices | Amp16;cabinet11;pedal16;modulation11;delay11;reverb11;noise reduction1. One each pedal/modulation/delay/reverb concurrently with amp/cabinet; complete simultaneous-block accounting unverified. 12AX7/ECC83 Valve Reactor. | [Japanese pp9,52][TLLE-J] |
| Factory / user memory | **120 writable programs**,30 banks×4. **40 factory sounds repeated across banks1–10,11–20,21–30**; not120 unique factory sounds or120 additional presets. | [Japanese pp7,9][TLLE-J] |
| Synth / acoustic | ACOUSTIC pedal simulates acoustic guitar; synth-engine capability unverified. | [English p35][TLLE-E] |
| I/O | INPUT;INSERT SEND/RETURN;two OUTPUTs;HEADPHONES;optical S/PDIF;MIDI IN/OUT;AC input. No USB in complete inventory; connector sizes/routing pending. | [Japanese p52][TLLE-J] |
| Power / battery / USB | **9V AC**, supplied **3.0A adapter rating**, not measured draw. DC polarity inapplicable. Battery operation unverified; no USB connector. | [Japanese p52][TLLE-J] |
| IR / NAM / capture | User IR,native/converted NAM and proprietary capture loading unverified. | Unresolved |
| Editor / software | **ToneLab LE Sound Editor** edits/manages programs; supported platforms and current availability unverified. Requires bidirectional MIDI through an external interface; some USB-MIDI interfaces cannot carry its SysEx. Match MIDI channels and enable SYEX OUT for editor parameter transmission. ST software is not evidence for LE. | [Japanese p9][TLLE-J]; [English pp51–52][TLLE-E] |
| Audio output / headphones | Headphones do not mute main outputs; rear LEVEL controls both. L/MONO for mono; choose Ln1/Ln2 for phones, Ln1 for optical output, Ln2 for three-band EQ. AMP/LINE disabled when amp model off. | [English pp18–21][TLLE-E] |
| Routing / live limits | INSERT precedes PEDAL. Bank preselection leaves current sound active until program selection. Key Lock disables knobs/buttons/selectors. Actual valve requires warm-up before sound. Dedicated spillover unverified. | [English pp13,20,22–23][TLLE-E] |
| Routing / MIDI backup | Programs can be saved/restored via MIDI exclusive data using sequencer/data filer. Optical output level adjustable separately −12 to+12dB; above0 may clip some programs. | [English p20][TLLE-E] |
| Looper / Hold Delay | **Mono Hold Delay1–8000ms**, automatically assigned to CONTROL; activating it holds the current delay sound. This documents delay freezing, not saved-loop storage or an independent overdubbing looper. Audio persistence remains unverified. | [English p43][TLLE-E] |
| Looper / drums / live | Chain reorders modulation/delay/reverb. Programmable CONTROL supports tap/insert/rotary functions. Dedicated looper,drums,scenes and trails unverified. | [Japanese pp9,11][TLLE-J] |

### Separate IDR hardware offers

| Condition | Evidence | Source |
|---|---|---|
| Used | **Rp2,260,000**, title explicitly Second. **Inside Studio Solo**,shop1887861133/item52514565252,Kab.Sukoharjo. Checked2026-10-17; exact HTML opened, three-week cache with26–27Sep delivery. Stock,working state,adapter/bundle,warranty and selected variant unverified. Model-selection URL parameter267809844474 retained; no variant options exposed. Late-arrival Rp10,000 compensation is not a discount; shipping/taxes/checkout unknown. Cached asking price only. | [Exact Shopee item][TLLE-S] |
| New | Unknown; no qualified new hardware offer established. | — |


### ToneLab LE — converters and expression initialization

| Field | Finding / qualification | Evidence |
|---|---|---|
| Processing / converters | **24-bit A/D and D/A;44.1 kHz**. These internal specifications do not establish USB audio; the recorded ports have no USB. | [English p55][TLLE-E] |
| Expression / EXP INIT | Global, automatically saved: OFF applies current pedal position immediately on program change; ON initializes the assigned parameter to its saved value. VOLUME, D/INPUT and R/INPUT always follow current position regardless. Per-program target/endpoints still require storing. | [English pp47–48][TLLE-E] |
| Expression / editing versus performance | Ordinary pedal targets edit the parameter value that will be written. OFF, VOLUME, M/PITCH, D/INPUT and R/INPUT do not edit stored parameters. Changing target initializes its MIN/MAX range. | [English pp47–48][TLLE-E] |
| Live / tap-factor limits | MOD TAP/DLY TAP support twelve factors:1/6,1/4,1/3,1/2,2/3,3/4,1,4/3,3/2,2,3,4. Maximum tap interval10s; this is not a maximum delay-time specification. Changing CONTROL assignment resets FACTOR to1; it has no effect for other targets. | [English p49][TLLE-E] |

### ToneLab LE — calibration and routing limits

| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression / calibration | Use a hand. Power on holding EXP-CTL-CHAIN + ▲: EXP MAX. Move pedal forward, release hand, press GLOBAL: EXP MIN. Move pedal back, release hand, press GLOBAL: COMPLETE, then normal operation. EXIT/TUNE cancels; ERROR returns to EXP MAX to repeat. This is not the AX3000G sequence; toe-switch threshold adjustment remains unverified. | [English p50][TLLE-E] |
| Processing / chain order | Six serial orders, saved per program: MD-DL-RV, MD-RV-DL, DL-MD-RV, DL-RV-MD, RV-MD-DL, RV-DL-MD. MD=modulation, DL=delay, RV=reverb. This does not establish arbitrary block placement or parallel routing. | [English p25][TLLE-E] |
| I/O / Ln2 EQ limits | Three-band output EQ requires Ln2 and an enabled amp model; unavailable with AP1/AP2/AP3/Ln1 or amp modeling off. Controls are input TRIM, LO GAIN, MID FREQ, MID GAIN and HI GAIN. | [English pp25–26][TLLE-E] |
<!-- comparison evidence ends -->

Primary Japanese J2 manual is manufacturer-hosted. English manufacturer-authored E1 mirror identifies ©2006 VOX AMPLIFICATION LTD, ToneLab LE and MIDI chart2006-04-20; category/memory/dimensions/ports match J2, but weight differs. English pagination differs from Japanese. No full-file hash or visual control certification. Both PDFs viewed as browser text; no software/manual/dependency saved or installed.

[TLLE-J]: https://voxamps.com/wp-content/uploads/2024/05/ToneLabLE_OM_J2.pdf
[TLLE-E]: https://www.voxshowroom.com/ct/manuals/ToneLabLE_OwnersManual.pdf
[TLLE-S]: https://shopee.co.id/Vox-Valvetronix-ToneLab-LE-Efek-Gitar-Second-i.1887861133.52514565252?extraParams=%7B%22display_model_id%22%3A267809844474%2C%22model_selection_logic%22%3A3%7D

## ToneLab ST

Guitar multi-effects; separate from LE/SE/EX. Checked2026-10-17; partial. Bass suitability/ownership unestablished.

<!-- comparison evidence begins -->

| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression | Built-in with firm-forward switching; volume cannot be toggled off. External EXP absent from complete ports. | [Manual pp6–7][TLST-M] |
| K/F/B | **12 / 2 / 9**, text-derived:AMP selector+five amp controls;PEDAL selector/edit;MOD/DELAY selector/edit;REVERB;rear LEVEL. UP/DOWN footswitches;AMP,CAB,PEDAL,MOD/DELAY,TAP,REVERB,WRITE,EXIT/TUNE,EXP PARAM buttons. Toe,STANDBY and AMP/LINE switch additional. Visual check pending. | [Manual pp2–7][TLST-M] |
| Display | Program/value LED display; diagonal,color,touch unverified. | [Manual p5][TLST-M] |
| Dimensions / mass | **270×180×70mm WDH;1.6kg**. Product metric row wrongly labels first dimension H; its inch row identifies W. | [Product][TLST-P] |
| Processing / category choices | **33 amps;11 cabinets;11 pedal;11 MOD/DELAY;3 reverbs;1 noise reduction**. Manufacturer claims up to eight simultaneous types; detailed block accounting pending. | [Product][TLST-P]; [Manual p1][TLST-M] |
| Category choices / combinations | **25 effects=11 PEDAL+11 MOD/DELAY+3 reverb**, with noise reduction separately listed. ACOUSTIC and drive/compressor choices share PEDAL. MOD/DELAY has8 modulation/pitch/filter choices plus Echo Plus,Delay,Chorus+Delay; not separate freely combinable modulation and delay slots. Chorus+Delay fixes chorus depth. | [Manual pp18–22][TLST-M] |
| Routing / pitch and delay | Pitch Shifter supports chords,±12 semitones and detune. Delay types40–1480ms;TAP+EDIT adjusts feedback. Assigning FILTRON to expression changes it from envelope sensitivity to direct cutoff control. | [Manual pp21–22][TLST-M] |
| Factory / user memory | **100=50 user0–49+50 preset50–99**. Initial user fill unverified. | [Manual p9][TLST-M] |
| Synth / acoustic | **Acoustic simulation yes:ACOUSTIC** in PEDAL; recommended low-output single-coil neck pickup. Dedicated synth engine remains unverified. | [Manual p19][TLST-M] |
| I/O | INPUT;stereo-mini AUX;shared stereo/mono OUTPUT/PHONES;USB-B;DC. No DIN MIDI or FX loop in complete inventory. Mono output cable takes left channel only. | [Manual pp7–9][TLST-M] |
| Power / battery / USB | **12V DC;540mA consumption**. Polarity,battery and USB bus operation unverified. | [Product][TLST-P] |
| IR / NAM / capture | User IR,native/converted NAM and captures unverified. | Unresolved |
| Editor / USB audio | **Librarian**, not confirmed full editor. Historical requirements:XP SP3/Vista SP1+,MacOSX10.4+ G4/Intel. Windows MIDI driver for librarian;ASIO driver for audio. USB playback bypasses effects. Current OS support unverified. | [Manual p28][TLST-M] |
| Looper / drums / live | Looper,drums,scenes,trails unverified. Tube warm-up delays initial sound. | [Manual p9][TLST-M] |

### Separate IDR hardware offers

| Condition | Evidence | Source |
|---|---|---|
| Used | Unknown; exact item does not establish condition. | — |
| New | Unknown; exact item does not establish condition. | — |
| Conditional historical observation | **Rp1,200,000**, herykurniawanipunk, Kab. Lombok Barat, shop94150896/item21882548072. Checked2026-10-17; last-week cache, exact HTML opened, stale9–11Oct delivery. Condition, stock, variant, adapter/bundle, warranty and working state unverified; shipping/tax/checkout total unknown. Late-arrival compensation is not discount. Not a confirmed new/used range or current-stock check. | [Exact ST item][TLST-S] |
| Additional condition-unverified historical observation | **Rp960,000; Habis**, BANKO MUSIC STORE, Kab. Bandung; shop1452686572/item29530564104. Checked2026-10-18;five-month search cache, direct open failed. Relative “Besok” delivery is stale cache text. Condition, working state, revision, adapter/bundle, warranty, voucher and present stock unknown; not assigned used/new. | [Indexed exact ST item][TLST-S2] |


### ToneLab ST — pedal recall and panel lock

| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression / position persistence | Saving normally stores the current pedal position as the assigned parameter value. Exceptions: volume, delay/reverb input levels, pitch-shifter PITCH and FILTRON cutoff. Assignment/endpoints save per program; amp GAIN assignment survives changing amp model. | [Manual pp24–26][TLST-M] |
| Live / key lock and bank navigation | Hold EXIT/TUNE about2s to lock top-panel switches/selectors/knobs; repeat to unlock. Holding UP or DOWN while pressing EXIT/TUNE moves the program number by10. | [Manual p5][TLST-M] |
| Memory / save exclusions | Rear LEVEL and AMP/LINE are not program-stored or covered by Original Value indication. Unsaved edits disappear on program change/power-off; WRITE targets users0–49. | [Manual pp11–12][TLST-M] |

### ToneLab ST — calibration and conversion

| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression / calibration and switching force | Use a foot, as hand operation may fail. Power on holding EXP PARAM + WRITE, then release. Press forward to switch the assigned effect: this establishes switching weight. Slowly return the pedal, remove foot, then gently advance it and remove foot. WRITE completes; EXIT/TUNE cancels. Failed adjustment repeats from the switching-weight step. Display glyphs are missing from extracted text and remain unverified. | [Manual p27][TLST-M] |
| Processing / converters | **24-bit A/D and D/A; 44.1 kHz** internal sampling. USB audio bit depth and selectable host rates are not specified here. | [Manual p33][TLST-M] |
| Memory / factory initialization | Reset returns saved programs to factory contents. Power on holding EXIT/TUNE + EXP PARAM; release when UP/DOWN LEDs blink, then WRITE confirms. EXIT/TUNE cancels before confirmation; do not interrupt initialization. This differs from pedal calibration. | [Manual p29][TLST-M] |
<!-- comparison evidence ends -->

### Condition-unverified Shopee hardware

[Exact ST item][TLST-S],**Rp1,200,000**,herykurniawanipunk,shop94150896/item21882548072,Kab.Lombok Barat. Checked2026-10-17; exact HTML opened with last-week cache and9–11Oct delivery. Condition,stock,variant,adapter/bundle,warranty and working state unverified. Late-arrival Rp10,000 compensation is not a discount; shipping/tax/checkout unknown. Excluded from condition-specific price columns. No dependencies,software or manual files saved/installed; manual viewed as browser text.

[TLST-M]: https://voxamps.com/wp-content/uploads/support/TonelabST_OwnersManual.pdf
[TLST-P]: https://voxamps.com/en-gb/product/tonelab-st/
[TLST-S]: https://shopee.co.id/vox-tonelab-st-i.94150896.21882548072

Additional unresolved identity lead checked2026-10-18: Ayx Music, Kab. Lamongan, shop58780289/item17149906599, **Rp1,750,000; Habis**, two-month search cache. Title says ST, but URL says EX; direct open failed. Do not assign to either exact model without corroboration. Condition, working state, bundle/adapter, warranty, voucher and present stock unknown. [Conflicting-title/URL lead][TLST-S3].

[TLST-S2]: https://shopee.co.id/VOX-ToneLab-ST-Digital-multi-efek-gitar-Original-i.1452686572.29530564104
[TLST-S3]: https://shopee.co.id/efek-vox-tonelab-EX-masi-bgus-i.58780289.17149906599

## ToneLab SE

Guitar multi-effects; separate from LE/ST/EX. Checked2026-10-17; partial. Bass suitability and ownership unestablished.

<!-- comparison evidence begins -->

| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression | **Two built-in expression pedals with under-pedal switches**; assigned volume/amp parameters cannot be toggled. External EXP absent from complete ports. | [Manual pp1,10,63][TLSE-M] |
| K/F/B | **13 /9 /19**, text-derived:6 model selectors+6 value knobs+rear LEVEL;4 program+2 BANK+A/B+FX ON/OFF+CONTROL footswitches;8 model/INSERT/PRES-NR+9 navigation/global+2 controller-setup buttons. Two pedal switches and STANDBY additional. Visual corroboration pending. | [Manual pp4–11][TLSE-M] |
| Display | Diagonal,technology,color,touch unverified. | Unresolved |
| Dimensions / mass | **710×249×76mm WDH;6.2kg**; large. | [Manual p63][TLSE-M] |
| Processing / category choices | Amp16;cabinet11;pedal16;modulation11;delay11;reverb11;noise reduction1. One per effect category concurrently; full simultaneous-block count pending. 12AX7/ECC83 Valve Reactor. | [Manual pp1,63][TLSE-M] |
| Model-total disagreement / cabinet | Specifications and selector description say11 cabinets; signal diagram labels one channel10 and the other11. Retain diagram discrepancy; no inferred channel limitation. | [Manual pp4,6,63][TLSE-M] |
| Audio output / headphones | Headphones do not mute main outputs; rear LEVEL controls both. Mono uses L/MONO. OUT SEL:AP for guitar amp,Ln for mixer/recorder. Valve warm-up delays initial sound. | [Manual pp11–13][TLSE-M] |
| Routing / controls | INSERT precedes PEDAL;MOD/DELAY/REVERB chain order editable. FX ON/OFF hold0.5s bypasses;hold1s mutes and activates tuner. | [Manual pp4–5,10][TLSE-M] |
| Factory / user memory | **96 writable memories**,24×4;32 factory programs repeated across three eight-bank groups. | [Manual piv,p1][TLSE-M] |
| Synth / acoustic | **ACOUSTIC simulation yes**, in PEDAL, with BODY/BASS/TREBLE; low-output single-coil neck pickup recommended. Dedicated synth engine unverified. | [Manual pp34–35][TLSE-M] |
| I/O | INPUT;INSERT SEND/RETURN;two balanced/unbalanced TRS OUTPUTs;PHONES;MIDI IN/OUT;AC input. No USB or S/PDIF in complete inventory. | [Manual p63][TLSE-M] |
| Power / battery / USB | **9V AC;18W consumption**. Included3.0A supply rating is not measured draw. DC polarity inapplicable;battery unverified;noUSB. | [Manual p63][TLSE-M] |
| IR / NAM / capture | User IR,native/converted NAM,capture loading unverified. | Unresolved |
| Editor / software | **ToneLabSE Sound Editor** edits/manages programs;platforms/current support unverified. Computer connection needs bidirectional MIDI and matching channels; some USB-MIDI interfaces cannot transfer its SysEx. No ST software inference. | [Manual pp2,56–57][TLSE-M] |
| Looper / Hold Delay | **Mono1–8000ms Hold Delay**. Assign HOLD DLY to CONTROL to freeze delay sound when switched on. Saved-loop storage and independent overdubbing are not established by this feature. | [Manual p45][TLSE-M] |
| Looper / drums / live | A/B switches stored amp,cabinet,noise-reduction combinations within a program. Looper,drums,scenes,trails unverified. | [Manual p1][TLSE-M] |

### Separate IDR hardware offers

| Condition | Evidence | Source |
|---|---|---|
| Used | Unknown; exact offer lacks condition evidence. | — |
| New | Unknown; exact offer lacks condition evidence. | — |
| Conditional historical observation | **Rp3,850,000; Habis/sold out**, BANKO MUSIC STORE, Kab. Bandung, shop1452686572/item41751511183. Checked2026-10-17; month-old opened HTML, stale26Aug delivery. Condition, working state, variant, adapter/bundle and warranty unverified; shipping/tax/checkout unknown. Late-arrival compensation is not discount. Historical ask, not live stock, completed sale or confirmed new/used range. | [Exact SE item][TLSE-S] |


### ToneLab SE — converters and dual-pedal control

| Field | Finding / qualification | Evidence |
|---|---|---|
| Processing / converters | **20-bit A/D and D/A;44.1 kHz**. These are SE specifications; no LE/ST/EX converter values substituted. | [Japanese p63][TLSE-M] |
| Expression / independent initialization | EXP1INIT/EXP2INIT are separate, global and automatically remembered. OFF applies current pedal position on program change; ON recalls the saved sound. Per-program target/MIN/MAX settings require saving; changing target resets its range. | [Japanese pp51–53][TLSE-M] |
| Expression / Quick Assign | Hold EXPRESSION1s to assign the displayed eligible parameter to pedal1; hold CONTROL1s for pedal2. Changing the effect clears its target except amp targets and delay/reverb input levels. An off target effect cannot be controlled. | [Japanese pp50–52][TLSE-M] |
| Expression / calibration | Use a **hand**. Power on with EXPRESSION+CHAIN for pedal1, CONTROL+CHAIN for pedal2. Move fully back, release, GLOBAL; move fully forward, release, GLOBAL. EXIT cancels; ERROR restarts at MIN. No hardware operation performed. | [Japanese p55][TLSE-M] |

### ToneLab SE — channel recall and performance limits

| Field | Finding / qualification | Evidence |
|---|---|---|
| Memory / channel hold | Global CH HOLD: OFF recalls the destination program’s saved A/B channel; ON retains the current channel across program changes. Factory default OFF. | [Japanese p16][TLSE-M] |
| Live / effects mode and key lock | Effects mode assigns switches1–4 to PEDAL/MOD/DELAY/REVERB and BANK DOWN to INSERT; BANK UP is inactive. With no external insert connected, INPUT remains active regardless of INSERT LED. Holding EXIT1s toggles key lock; pedals and EXIT remain operable. Power cycling clears the lock. | [Japanese pp15–17][TLSE-M] |
| Processing / chain orders | Six serial MOD/DELAY/REVERB permutations, saved per program: MD-DL-RV, MD-RV-DL, DL-MD-RV, DL-RV-MD, RV-MD-DL, RV-DL-MD. | [Japanese p20][TLSE-M] |
| Live / tap factors | MOD TAP/DLY TAP factors:1/6,1/4,1/3,1/2,2/3,3/4,1,4/3,3/2,2,3,4. Tap interval maximum10s, not a delay-time limit. Other CONTROL targets ignore FACTOR; changing target resets it to1. | [Japanese p54][TLSE-M] |
<!-- comparison evidence ends -->

### Condition-unverified sold-out Shopee hardware

[Exact SE item][TLSE-S],**Rp3,850,000**,**Habis/sold out**,BANKO MUSIC STORE,shop1452686572/item41751511183,Kab.Bandung. Checked2026-10-17; exact HTML opened,last-month cache,26Aug delivery stale. Condition,working state,variant,adapter/bundle,warranty unverified. Rp10,000 late-arrival compensation not discount;shipping/tax/checkout unknown. Excluded from used/new prices;not live stock or completed sale.

Manufacturer-hosted Japanese J1 manual viewed as browser text;printed pagination differs from PDF index. No manual/software/dependencies saved or installed. Controls,display,algorithm detail,modern software support and import/power/live restrictions remain unresolved.

[TLSE-M]: https://voxamps.com/wp-content/uploads/2022/03/ToneLabSE_OM_J1.pdf
[TLSE-S]: https://shopee.co.id/Multi-FX-VOX-Tonelab-SE-Twin-Pedal-Multi-Effect-i.1452686572.41751511183

## StompLab 2B

Bass multi-effects,also named IIB/SL2B; distinct from IB/IIG. Checked2026-10-18;partial. Ownership unestablished.

<!-- comparison evidence begins -->

| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression | Built-in;firm press toggles assigned function. External EXP absent from complete ports. | [Manual pp5–6][SL2B-M] |
| K/F/B | **3 /2 /4**,text-derived:CATEGORY,VALUE1/2;UP/DOWN;EDIT,▲,▼,expression-setting. Rear POWER and pedal switch additional;visual check pending. | [Manual pp4–6][SL2B-M] |
| Display | Program/value display;diagonal,color,touch unverified. | [Manual p4][SL2B-M] |
| Dimensions / mass | **207×125×64mm WDH;780g**. | [Product][SL2B-P] |
| Processing / category choices | **61 variations;up to8 simultaneous including NR**. Pedal9;Amp10/Drive8;cabinet12;modulation9;delay8;reverb3;NR1. AMP/DRIVE is one shared category. Qualified total below. | [Manual p3][SL2B-M]; [Product][SL2B-P] |
| Category choices / total reconciliation | Listed choices sum60:9+10+8+12+9+8+3+1. Manual p15 explicitly lists **Volume Pedal:1** alongside those categories;the published entries therefore sum61 including volume. This counts category alternatives,not61independent algorithms. Seven editable categories plus volume explain up to8;amp and drive are alternatives. | [Manual pp9–10,78–79][SL2B-M] |
| Routing / expression behavior | Volume uses current pedal position on program change;other targets wait until pedal movement. WAH selection automatically assigns expression. Bypass includes NR;holding both switches1s mutes;exiting does not change program. | [Manual pp8–10][SL2B-M] |
| Power / auto-off | Factory-enabled auto-off after1h without controls or audio input. Setting survives power-off;EDIT+UP at power-on disables it. Restart requires power-on. | [Manual p7][SL2B-M] |
| Factory / user memory | **120:100 read-only presets00–99+20 writable U0–U9/u0–u9**. Initial user fill unverified. | [Manual pp3,7][SL2B-M] |
| Synth / acoustic | ACOUSTIC pedal listed;function details and dedicated synth engine unverified. | [Product][SL2B-P] |
| I/O | Mono INPUT;shared stereo OUTPUT/PHONES;DC. NoUSB,DIN MIDI,AUX or loop in complete inventory. | [Manual pp5–6][SL2B-M]; [Product][SL2B-P] |
| Power / battery / USB | **9VDC or4AA;approximately200mA;7.5h alkaline**. **Center-negative through the named KA181 adapter evidence chain**,not direct inspection of the inlet marking;barrel dimensions remain unverified. NoUSB. | [Product][SL2B-P];[IIB manual p77][SL2B-M];[Korg KA181 specification](https://www.korg.com/jp/products/tuners/pitchblack_x_mini/specifications.php) |
| IR / NAM / capture | User IR,native/converted NAM,captures unverified. | Unresolved |
| Editor / software | Editor/platforms unverified. | Unresolved |
| Looper / drums / live | Tuner in bypass/mute;looper,drums,scenes,trails unverified. | [Manual p3][SL2B-M] |
| Conversion / tuner specifications | Ownmanual p15:**24bit A/D andD/A**;sample rate unverified. Tuner detects**A0–E6**,reference**438–445Hz**. These are published ranges,not accuracy measurements. | [Manual][SL2B-M] p15 |
| Acoustic / parameter and overload limits | Appendix p78 lists **ACOUSTIC(AC),TONE0–10**,pedal-assignable;no secondparameter. Manual p15 warns high-output humbuckers or excessiveAMP/DRgain may cause high-frequency distortion withAC;lower instrument level/gain. This confirms a named effect andcontrols,not a full description of its acoustic-body model or a dedicated synthesizer. | [Manual][SL2B-M] pp15,78 |
| Category choices / modulation and delay variants | Ownmanual pp80–81 lists MOD:**CEChorus,MultiChorus,Flanger,ORGPhase,TwinTrem,G4Rotary,PitchShift,Filtron1Auto,Filtron2Manual**. PitchShift offers−12…+12 anddt(detune);polyphonic tracking unverified. DLY:**AnalogDelay1–4 andEcho1–4**,withhigher variant numbers increasing feedback;not eight unrelated delay architectures. REV:**Room,Spring,Hall**. TIME0.1…10 values are parameter scales,not verified milliseconds/seconds. | [Manual][SL2B-M] pp80–81 |
| Cabinet / parameter limits | Twelve factory cabinet entries include **CUSTOM**,whoseCharacter spans0…20. This adjustable factory entry is not evidence ofuserIR import. GLOBAL selectsAP(AMP) orLn(LINE),plusMasterLevel0…10. | [Manual][SL2B-M] pp80–81 |

### Separate IDR hardware offers

| Condition | Evidence | Source |
|---|---|---|
| Used | Unknown;condition unconfirmed. | — |
| New | Unknown;condition unconfirmed. | — |
| Conditional historical observation | **Rp1,520,000**, Seven Stereo Music & Audio Store, Kota Bandung, shop16879370/item1349945522; checked2026-10-17, opened two-week cache. Earlier two-month index marked Habis; current stock, condition, variant, adapter/bundle, warranty and working state unverified. Stale August delivery and late-arrival compensation do not establish stock or discount; shipping/tax/checkout unknown. Not a verified new or used price. | [Exact item][SL2B-S] |
| New-title indexed ask;Habis | **Rp950.000**, [spot_reuseshop.id,shop258736226/item10788059230](https://shopee.co.id/BASS-EFFECT-VOX-STOMPLAB-2B-NEW%21%21%21-i.258736226.10788059230),KotaJakartaSelatan. Rechecked2026-10-17;2monthsearchcache,directCachemiss. Title saysNEW;condition not independently confirmed. **Habis**;working status,adapter/bundle,warranty,variant,shipping/tax andcheckout unknown. Late-delivery compensation not deducted;not an available new-price range orcompleted sale. Earlier observation below retained. | Exact indexed hardware title;no fresh stock certification. |
| Unallocated variant/voucher display;Habis | **Rp1,367,000** displayed withvoucher;Salomo Musik,KotaJakartaUtara,shop1776275/item4688514198. Checked2026-10-18,directreader2weekcache;earliersearch2months. Options SL2B and+Adaptor visible;selected option andprice allocation unresolved. Not accepted as bare-unit oradapter-bundle price,new/used price,oravailable stock. Voucher text spendRp10RB/discount10% retained without recalculation;eligibility/cap/checkout unknown. Working state,warranty,shipping/tax unknown;relative delivery andlatecompensation up toRp10,000 do notoverrideHabis orreduce price. | [Exact listing](https://shopee.co.id/Vox-SL2B-Multi-Effects-Bass-Pedal-Multi-Efek-Bass-Pedal-Vox-Stomplab-2B-SL2B-Original-i.1776275.4688514198) |


### StompLab 2B — saved settings and pedal limits

Checked2026-10-18 against the [exact IIB manufacturer manual][SL2B-M]. Printed page numbers retained;no hardware operation performed.

| Field | Manual qualification |
|---|---|
| Expression / range persistence | Pp10–11 permit separate heel/toe parameter endpoints. Unsaved ranges revert on program change or power-off. Saving after pedal movement stores its current parameter value,except volume,delay/reverb input levels and pitch-shift pitch;the manual labels the delay exception **PDL**,while its following instruction says **DLY**. Preserve that label discrepancy. |
| Memory / global persistence | P12: output-device **AP/Ln selection persists** across power-off; **master volume resets to7.0**. Unsaved program edits are lost on program change/power-off. P14 factory reload erases stored user-created programs;this is not an additional writable bank. |
| Live / tuner reference reset | P9: reference adjustment **438–445Hz** returns to **440Hz after power-off**. This differs from the persistent output-device selection. |


### StompLab 2B — amplifier and drive category detail

Checked2026-10-18 against the [manufacturer appendix][SL2B-M],printed pp78–80.

| Field | Exact-model category evidence |
|---|---|
| Processing / AMP choices | P79 lists **seven clean models**: VALVE1,VALVE2,CLASSIC,SCOOPED,LA STUDIO,GOLD PANEL,JAZZ; **three overdriven amp models**: STUDIO,AC100,UK MAJOR. These account for ten amps;not ten simultaneous blocks. |
| Processing / DRIVE and EQ controls | The same shared AMP/DRIVE category has **four drive/distortion and four fuzz choices**. Clean choices use limiter sensitivity;overdriven/drive/fuzz choices use gain. Low/high/mid controls belong to AMP/DRIVE rather than independent EQ slots;clean choices include adjustable mid frequency. Exact frequency values are not published by the0–10 scale. |
| Processing / PEDAL choices | P78 lists nine entries: compression,exciter,wah,envelope wah,octave,acoustic processing,vibe,tone andring modulation. Wah has two internal model settings;these do not add two more PEDAL entries. Ring modulation does not independently establish a dedicated bass-synth oscillator architecture. |


### StompLab 2B — adapter polarity evidence chain

Checked2026-10-18.

| Field | Evidence / limit |
|---|---|
| Power / named adapter polarity | Exact IIB [Japanese manual p77][SL2B-M] names optional **KA181**. [Korg’s KA181 specification](https://www.korg.com/jp/products/tuners/pitchblack_x_mini/specifications.php) explicitly calls that adapter **9V,center-negative**. Thus center-negative is supported through the named compatible adapter;this is an evidence-chain inference,not visual confirmation of the StompLab inlet marking. No tuner current draw or other tuner specification is transferred. Barrel dimensions remain unverified. |
| Physical controls / value lock | Exact IIB manual p4:holding EDIT2s in Program Select locks VALUE1/2;repeat to unlock. Lock is unavailable in Edit mode. It does not lock CATEGORY or establish stored lock persistence. |

Panel screenshots failed in the browser tool;no visual control-count,display-color ortouchscreen verification is claimed. Existing text-derived K/F/B remains qualified. On2026-10-18,the official manual URL failed reopening;the earlier identified IIB evidence is retained,not newly recertified. Korg’s named-adapter page reopened andstill explicitly specifies9V center-negative;no tuner current orother tuner specification is transferred.

<!-- comparison evidence ends -->

### Condition-unverified exact hardware

[Exact item][SL2B-S],**Rp1,520,000**,Seven Stereo Music & Audio Store,shop16879370/item1349945522,Kota Bandung. Checked2026-10-17;exact HTML opened,two-week cache;earlier two-month index said Habis and19–21Aug delivery. Present stock,condition,variant,adapter/bundle,warranty and working state unverified. Late-arrival Rp10,000 compensation is not discount;shipping/tax/checkout unknown. Excluded from used/new columns. Separate NEW-title sold-out item258736226/10788059230 Rp950000 remains index-only,not a live retail quote. No files/software/dependencies downloaded or installed;manual browser text only.

[SL2B-M]: https://voxamps.com/wp-content/uploads/2019/12/SL_IIB_OM_EFGSJ1.pdf
[SL2B-P]: https://voxamps.com/ja/product/stomplab-2b/
[SL2B-S]: https://shopee.co.id/Vox-StompLab-2B-Bass-Modelling-Effect-Processor-i.16879370.1349945522

## StompLab 1G

Guitar multi-effects;distinct from2G,1B,2B. Checked2026-10-17;partial. Bass suitability andownership unestablished.

<!-- comparison evidence begins -->

| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression | **No built-in expression/toe switch;no external EXP socket** in complete panel inventory. FIX WAH is knob-controlled,not pedal wah. | [Manual pp4–6,62][SL1G-M] |
| K/F/B | **3 / 2 / 3**,text-derived:CATEGORY,VALUE1,VALUE2;UP/DOWN pedals;EDIT andtwo arrow buttons. Rear POWER button additional;visual corroboration pending. | [Manual pp4–6][SL1G-M] |
| Display | Diagonal,color,touch andtechnology unverified. | Unresolved |
| Dimensions / mass | **145×125×57mm WDH;590g**. | [Official product][SL1G-P] |
| Processing / category choices | **103**:8 Pedal+44 Amp+18 Drive+12 Cabinet+9 Modulation+8 Delay+3 Reverb+1 Noise Reduction;sum103,not simultaneous count. English cabinet list names11 despite12heading;German includes UK T75 4×12. **Seven simultaneous including NR**;AMP/DRIVE shares one category. Seven categories:Pedal,AMP/DR,Cabinet,NR,Modulation,Delay,Reverb. | [Official product][SL1G-P];[German product][SL1G-D];[Manual pp4,9][SL1G-M] |
| Factory / user memory | **120=100 read-only00–99+20 writableU0–U9/u0–u9**. WRITE required;unsaved edits lost on program change/power-off. Initial user fill pending. | [Official product][SL1G-P];[Manual pp7,10][SL1G-M] |
| Synth / acoustic | Pedal category lists Acoustic;dedicated simulation behavior pending. Synth unverified. | [Official product][SL1G-P] |
| I/O | Complete rear inventory:mono INPUT,shared stereo OUTPUT/PHONES,DC9V andPOWER;no AUX,USB,MIDI,loop orEXP socket. | [German product][SL1G-D];[Manual p6][SL1G-M] |
| Routing / output target | A1 UK-style mid-forward open combo; A2 clean US-style open combo; A3 closed 4×12 stack; Ln line, headphones, power-amp input or recorder. Output target persists; global master resets to **7.0 at power-on**. Lo/Hi controls belong to AMP/DR and stop with that block. | [Manual pp5,8–13][SL1G-M] |
| Power / battery / USB | **9V DC,approximately200mA;4AA,7.5h alkaline**. Polarity andUSB power unverified. English AC-adapter wording describes supply,not proof of9VAC input. Regional included-battery wording differs. | [German product][SL1G-D];[English product][SL1G-P] |
| IR / NAM / capture | User IR,native/converted NAM andcapture imports unverified. | Unresolved |
| Editor / software | No USB/MIDI connector in manual inventory;USB audio unavailable through such a port. Editor/imports unverified. | [Manual pp4–6][SL1G-M] |
| Looper / drums / live | Tuner A0–E6;reference438–445Hz. **Auto-off after1h without controls orinput audio**,default enabled;EDIT+UP at startup disables,EDIT+DOWN enables;setting persists,restart required after shutdown. Both footswitches bypass all effects including NR; hold about 1 s for mute. Either switch exits without changing program. Calibration resets to 440 Hz after power loss. Hold EDIT 2 s to lock VALUE controls in Program mode. Looper/drums/trails unverified. | [Official product][SL1G-P];[Manual pp7–11][SL1G-M] |

### Separate IDR hardware offers

| Condition | Evidence | Source |
|---|---|---|
| Used | **Rp850,000**,SECOND-title hardware,Habis;historical cached ask,not working-condition/current-stock guarantee. Checked 2026-10-17; seller gitar second, shop 61848168 / item 20091595478, Kab. Polewali Mandar. Two-month cache with stale August delivery. Variant, adapter/bundle, warranty, working state, shipping/tax and usable vouchers unknown; late-delivery compensation is not a discount. | [gitar second item][SL1G-S] |
| New | Unknown;no qualified retail/new offer. | — |

[gitar second item][SL1G-S],shop61848168/item20091595478,Kab.Polewali Mandar. Exact HTML opened,two-month cache;direct20–23Augdelivery versus indexed4–7Aug,both stale. Variant,bundle/adapter,warranty andworking state unknown. Rp10,000late-arrival compensation not discount;shipping/tax/checkout unknown. Not completed-sale evidence. Other condition-unverified exact1Gasks retained inledger;shop-only andmixed1G/2G offers excluded.

Manufacturer1Gproduct pages opened;earlier J1 candidate inaccessible;**official EFGSJ2 manual now opened**. No sibling specifications imported. English cabinet list omission andregional battery inclusion conflict retained;no files ordependencies downloaded.

[SL1G-P]: https://voxamps.com/en-gb/product/stomplab-1g/
[SL1G-D]: https://voxamps.com/de/produkt/stomplab-1g/
[SL1G-S]: https://shopee.co.id/VOX-STOMPLAB-1G-MULTIEFEK-GUITAR-MULTIEFFECT-MULTI-EFFECT-PEDAL-GITAR-MULTI-EFEK-SECOND-i.61848168.20091595478

Official EFGSJ2 manual identifies StompLab IG;pp4–6 provide complete controls/connectors andp9category architecture. ACOUSTIC parameter table p62 lists TONE0–10;function details remain qualified. This is text-derived verification,no visual count certification.

[SL1G-M]: https://voxamps.com/wp-content/uploads/2019/12/SL_IG_OM_EFGSJ2.pdf

### Global output and stage behavior

Output compensation:A1 UK-style mid-forward open combo,A2 clean US-style open combo,A3 closed4×12stack,Ln line/headphones/power-amp input/recorder. Target mode persists;global master resets to7.0 at power-on.

Both footswitches together bypass all effects including NR;holding about1s mutes. Tuner operates in either state;one switch exits without changing program. Tuner calibration resets to440Hz after power loss. EDIT held2s locks VALUE knobs in Program mode.

Lo/Hi controls belong toAMP/DR andstop with that block. ACOUSTIC distortion troubleshooting recommends lower drive/guitar output;it does not establish extra simulation capabilities. Manual p13 confirms62Amp/Drive choices,consistent with44+18. [EFGSJ2 pp5,8–13][SL1G-M].

<!-- comparison evidence ends -->

## StompLab 2G

Guitar multi-effects with built-in expression, distinct from 1G and 2B. Checked 2026-10-17; partial. Ownership and bass suitability unestablished.

<!-- comparison evidence begins -->

| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression | **Built-in expression with pressure switching** of assigned target; wah,volume andeffect parameters. No external EXP socket in complete rear inventory. Only blinking-LED parameters are assignable;heel/toe ranges are editable and require saving. Volume follows pedal position immediately on program recall;other targets wait for pedal movement. Instantaneous position cannot be saved for volume,delay input,reverb input or MOD pitch-shift pitch; these remain assignable targets. Assignment ranges require WRITE. | [Official IIG manual pp3–6,10–12][SL2G-M] |
| K/F/B | **3 / 2 / 4**, text-derived: CATEGORY,VALUE1/2;UP/DOWN footswitches;EDIT,up/down buttons,expression-setting button. Pedal pressure switch and rear POWER additional. Visual corroboration pending. | [Manual pp4–5][SL2G-M] |
| Display | Program/value readout plus tuner andexpression LEDs. Diagonal,technology,color andtouch unverified. | [Manual pp4–5][SL2G-M] |
| Dimensions / mass | **207×125×64 mm W×D×H; 780 g**. English also prints21.72oz, inconsistent with780g; retain conflict. Medium horizontal footprint. | [VOX English][SL2G-E];[German][SL2G-D] |
| Processing / category choices | **104** advertised total. Category choices: pedal8, amp44, drive18, cabinet12, modulation9, delay8, reverb3, noise reduction1, plus expression/volume. Not104 simultaneous blocks. **Amp and drive share AMP/DR**;Lo/Hi are its parameters,not extra blocks. Volume block operates when expression isassignedVOLUME. Exact IIG manual confirms **eight simultaneous effects includingNR**,superseding series-wide7–8 ambiguity. German list includes UK T75 absent from English's11-name list under12 heading. | [English][SL2G-E];[German][SL2G-D];[Japanese][SL2G-J];[Manual p3][SL2G-M] |
| Factory / user memory | **100 preset +20 user =120**. **WRITE required**;program change/power-off loses unsaved edits. Writing replaces destination. Initial user fill pending. | [Manual p12][SL2G-M] |
| Synth / acoustic | ACOUSTIC in pedal list; dedicated simulation behavior and synth capability unverified. | [VOX German][SL2G-D] |
| I/O | Complete rear inventory: **INPUT,shared OUTPUT/PHONES,DC9V andPOWER**. No USB,MIDI,AUX,send/return or externalEXP in inventory. Audio socket sizes pending. | [Manual pp5–6][SL2G-M] |
| Power / battery / USB | **9V DC, approximately200mA;4AA,7.5h alkaline**, optional adapter. Polarity unverified; noUSB socket,so noUSB operation. English calls battery set included for testing; German excludes batteries: regional bundle conflict. | [VOX German][SL2G-D];[English][SL2G-E] |
| IR / NAM / capture | UserIR, native/converted NAM and proprietary capture import unverified. | Unresolved |
| Editor / software | No USB port in complete inventory. Model-specific editor/platform availability unverified. | Unresolved |
| Looper / drums / live | Tuner A0–E6, reference438–445Hz. Output profilesA1 UKopen combo,A2 cleanUSopen,A3closedstack,Ln line/headphone/poweramp/recorder. Profile persists;master resets7.0. Tuner calibration resets440Hz. Looper,drums,trails/scenes unverified. | [Manual pp9,12–13][SL2G-M] |

### Expression storage limits

Rev.EFGSJ1 p11 says current pedal position can be stored except volume,delay input,reverb input andMOD pitch-shift pitch. This does not prohibit assigning those targets;it limits saved instantaneous values. Assignment ranges require WRITE. [Official manual pp10–12][SL2G-M]

### Separate IDR hardware offers

| Condition | Evidence | Source |
|---|---|---|
| Used | Unknown; condition not established. | — |
| New | Unknown; condition not established. | — |
| Conditional historical observation | **Rp1,725,000; Habis**, maju jaya gallery, Kab. Malang, shop33360096/item27573361035. Checked2026-10-17, month-old opened cache; two-month search omitted stock marker. Condition, variant, adapter/bundle, working state, warranty, usable vouchers and checkout total unknown. August/September delivery text is stale; late-arrival compensation is not discount. Not a verified new/used price or live stock. | [Exact item](https://shopee.co.id/pedal-efek-gitar-multi-effect-digital-VOX-stomplab-2G-i.33360096.27573361035) |

<!-- comparison evidence ends -->

### Condition-unverified hardware leads

[maju jaya gallery](https://shopee.co.id/pedal-efek-gitar-multi-effect-digital-VOX-stomplab-2G-i.33360096.27573361035), shop33360096/item27573361035, Kab.Malang: Rp1,725,000, **Habis** in month-old opened cache. Condition, variant, bundle and working state unknown. Search2-month cache omitted stock marker; opened cache supersedes that omission, not live confirmation. Aug19–22 andSep9–10 delivery claims stale.

[SadewaMusikAudio](https://shopee.co.id/EFEK-DIGITAL-VOX-STOMPLAB-2G-MULTIEFEK-STOMP-LAB-IIG-MULTI-EFEK-II-2-G-i.171167271.23686028621), shop171167271/item23686028621, Kab.Bantul: Rp1,000,000–1,100,000, **Habis**, last-week search index. Lengkap/Unit Only variations have unresolved price mapping; condition/working state unknown.

Both checked2026-10-17. Rp10,000 late-arrival compensation is not a purchase discount; shipping/tax/checkout unknown. Neither is a qualified used/new price. Official 84-page IIG manual EFGSJ1 is now readable;title/introduction explicitly identify StompLab IIG. Control inventory is text-derived;no sibling specifications transferred.

[SL2G-E]: https://voxamps.com/product/stomplab-2g/
[SL2G-D]: https://voxamps.com/de/produkt/stomplab-2g/
[SL2G-J]: https://voxamps.com/ja/product/stomplab-2g/

[SL2G-M]: https://voxamps.com/wp-content/uploads/2019/12/SL_IIG_OM_EFGSJ1.pdf

## ToneLab EX

Checked 2026-10-17. Partial guitar multi-effects record; distinct from LE/ST/SE. [VOX manual E1](https://voxamps.com/wp-content/uploads/support/ToneLabEX_OM_E1.pdf),44pages,©2010;web text read,no download orvisual audit.

| Field | Evidence / gaps |
|---|---|
| Expression | Built-in;full-forward activation toggles assigned effect except volume. External EXP/toe mechanism unknown. |
| Controls | **15 rotary /6 footswitches /12 panel buttons**, derived from numbered manual text. Rotary:13top+2rear;foot:program1–4+BankUp/Down. Pedal activation and2rear switches separate;not visually audited. |
| Display | Bank/value display;diagonal,color,touch unknown. |
| Processing / choices | **33amps,11cabinets;45effects includingNR**:26pedal(11stand-alone+4Pedal1+11Pedal2),11modulation,4delay,3reverb,1NR. Own product page calls this **44effects+1NR**;same subtotal basis. Up to9simultaneous includingNR/volume. Eleven stand-alone pedals **replace amp**,not ordinary single-function hardware. |
| Presets | **100factory+100editableuser=200**. |
| Synth / acoustic | **Pedal2 ACOUSTIC converts electric to acoustic-guitar timbre**;single-coil neck pickup recommended. TECHNO FUZZ combines distortion with synth-like sounds;not proof of a general synthesizer engine. |
| Dimensions / weight | E1 manual: **394W×238D×82H mm;3kg**. Own product page: **394W×238D×72H mm;3kg**. Height conflict unresolved;not averaged. |
| I/O | Guitarinput,stereo miniAUX,shared stereo/monoOUTPUT/PHONES,USB-B,DC12V. Two1-inch speakers,approx0.3W×2;output plug mutes speakers. No externalEXP/MIDI-DIN/FXloop in rear inventory. |
| Power | **12V DC,700mA consumption**;polarity symbol unread. Battery/USBpower unknown. |
| USB / software | USB audio and **Windows/Mac librarian** documented;dated support limits below. Windows audio requiresASIOdriver. USB playback bypasses effects. Full editor/currentOS compatibility unknown;driver≠editor. |
| IR / NAM / captures | UserIR,native/convertedNAM,capture import unknown. |
| Preset / save scope | Unsaved edits disappear on program change/power-off. WRITE overwrites user banks01–25;factory banks26–50 are read-only. StompBox on/off edits survive return toProgramSelect but require WRITE before changing programs/poweringoff. RearLEVEL,SPEAKERLEVEL,TotalEqualizer andAMP/LINE settings are not saved perprogram or shown byOriginalValue indication. |
| Live / equalizer and noise reduction | TotalEQ works only inLINE:High/Low boost andTrim each−10…+10 (manual gives values withoutdB units). LowerTrim if boost clips. NR is perprogram;minimum disables,and excessive settings can truncate notes. |
| Looper / drums / live | Looper/drums/scenes unknown;Program Select/Stomp Box modes,tuner,QuickAssign. |

Save/EQ findings: [own E1 manual](https://voxamps.com/wp-content/uploads/support/ToneLabEX_OM_E1.pdf),printed11,13–15,checked2026-10-17 as browser text.

### ToneLab EX — separate IDR hardware offers

| Condition / seller | IDR evidence | Exact item |
|---|---|---|
| Used | Unknown | — |
| New | Verified new-condition price unknown | — |
| Condition unverified / bejita,Kab.Tulang Bawang Barat | **Rp1.700.000**;index2months,checked2026-10-17;directopen failed. Stock,selectedvariant,adapter/bundle,warranty,voucher,shipping/tax unknown. August delivery estimate andlate-arrival voucher do not prove stock ordiscount. | [4466947/42755664991](https://shopee.co.id/Vox-Tonelab-Ex-i.4466947.42755664991) |

Separate casing item80816302/22315555452,Rp250.000,is not processor-price evidence. Guitar scope verified;no bass/vocal membership inferred.
### ToneLab EX — controls and pedal allocation

Checked 2026-10-17 against the [E1 manufacturer manual](https://voxamps.com/wp-content/uploads/support/ToneLabEX_OM_E1.pdf), pp2–8,22–24. Text-derived count, not a photographic audit:

| Group | Controls counted |
|---|---|
| Rotary15 | Amp selector+GAIN/TREBLE/MIDDLE/BASS/REVERB/VOLUME(7);Pedal1(1);Pedal2 selector+EDIT(2);Mod selector+EDIT(2);Delay(1);rear OUTPUT LEVEL+SPEAKER LEVEL(2) |
| Foot6 | BankUp/Down andProgram1–4 |
| Buttons12 | AMPS,STAND ALONE,CABINET;Pedal1/Pedal2 on-off;Mod on-off/TAP;Delay on-off/TAP;EXIT/TUNE,WRITE,EXPRESSION |

Rear power andAMP/LINE switches plus expression activation are additional. Pedal1 choices:COMP,VOX V847,TONE,ENERGIZER. Stand-alone11 andPedal2 eleven combine withPedal1 four toexplain the26pedal subtotal;stand-alone still excludes amp modeling.

Acoustic simulation is explicitly electric-to-acoustic,not merely anacoustic amplifier preset. TECHNO FUZZ’s synth wording describes its timbre;broader synth architecture remains unverified.
### ToneLab EX — librarian and dated platform support

Checked 2026-10-17. The [official Windows chart,2023-02-20](https://voxamps.com/wp-content/uploads/2023/02/Win_CompatibilityChart-VOX_en_20230220.pdf) lists EX USB audio,USB MIDI,EX ASIO driver andSound Librarian separately. All four show Yes for **Windows8.1 32/64-bit**, then **End Of Support** for Windows10 21H2/22H2 andWindows11 21H2/22H2. MIDI/librarian require the VOX USB-MIDI driver. These dated rows do not establish current Windows releases or actual failure on unsupported systems.

The [official Mac chart,2020-06-19](https://voxamps.com/wp-content/uploads/2020/06/Mac_CompatibilityChart-VOX_en_20200619.pdf) lists EX USB audio,USB MIDI andSound Librarian as Yes on **macOS10.12/10.13/10.14**, and **End Of Support on10.15 Catalina**. Librarian has an unsigned-certificate qualification. The chart’s general Apple-standard-driver advice does not override EX’s model-specific end-of-support rows. Newer macOS/Apple Silicon support remains unverified.

This verifies a **program librarian**, not acomplete parameter editor. A third-party driver database surfaced newer generic driver packages;these were not downloaded or accepted as model/application support evidence. Power polarity remains unread.
### ToneLab EX — product-page reconciliation

Checked 2026-10-17 against the [own VOX product page](https://voxamps.com/product/tonelab-ex/),SKU TONELABEX,marked legacy/no longer produced. That label does not prove absence of Indonesian stock.

The page lists **394W×238D×72H mm**, while E1 p39 lists **394W×238D×82H mm**. Both give3kg. Preserve the10mm height disagreement;no measured unit orrevision explanation established. Its **44 effect types plus1 noise reduction** reconcile with E1’s45includingNR;TotalEqualizer is listed separately andavailable only inLINE mode. Its0.6W speaker figure agrees arithmetically with the manual’sapprox0.3W×2,not anadditional output.

The page exposes generic VOX2ch Windows audio-driver2.0.0 notes,including2in/2out,44.1kHz,24-bit device audio and32-bit application transport. Without anexplicit exact-model driver applicability statement,these are not promoted to verified ToneLabEX interface specifications ornew librarian compatibility. Product Downloads currently resolves to the homepage in the web link extraction;no setup guide orsoftware fetched.

### ToneLab EX — expression save and range limits

| Field | Finding / qualification |
|---|---|
| Expression / position recall | Pedal position is normally saved as the assigned parameter value. Exceptions: volume, delay/reverb input levels, PITCH pitch, FILTRON cutoff and TALK MOD vowel. These exceptions do not establish how every target initializes after recall. [Own manual p31](https://voxamps.com/wp-content/uploads/support/ToneLabEX_OM_E1.pdf) |
| Expression / range and reassignment | Assignment and endpoint ranges save per program. Delay/reverb input-level endpoints are automatic and cannot be edited. Changing effect normally clears assignment; gain assignment survives changing amp/stand-alone type. EXPRESSION+EXIT/TUNE clears assignment manually. [Own manual pp32–33](https://voxamps.com/wp-content/uploads/support/ToneLabEX_OM_E1.pdf) |
| Expression / sensitivity calibration | Power on holding EXPRESSION+WRITE. Using a foot, advance to establish switching pressure, slowly return, release foot, then gently advance and release. WRITE confirms; EXIT/TUNE cancels. This documents calibration, not a hardware operation performed. [Own manual p34](https://voxamps.com/wp-content/uploads/support/ToneLabEX_OM_E1.pdf) |

## StompLab 1B

<!-- comparison evidence begins -->

Checked 2026-10-18. **Bass multi-effects**, also styled StompLab IB; distinct from expression-equipped IIB. Partial record; no dependencies or manuals downloaded.

| Field | Evidence / gaps |
|---|---|
| Instrument / expression | Bass-focused. Built-in expression pedal belongs to IIB, not IB in the Japanese family description. External EXP and toe switching unverified. [VOX Japanese][SL1B-J] |
| K/F/B | Rotary / footswitch / panel-button counts unknown; no sibling counts transferred. |
| Display | Diagonal, resolution, technology, color and touch unknown. |
| Dimensions / weight | **145×125×57 mm W×D×H; 590 g**. [VOX English][SL1B-E] |
| Processing / choices | **60 choices**: pedal9, amp10, drive8, cabinet12, modulation9, delay8, reverb3, noise reduction1. These are library alternatives, not simultaneous blocks. Japanese family description says7–8 simultaneous including NR; exact IB ceiling remains unverified. [English][SL1B-E];[Japanese][SL1B-J] |
| Factory / user memory | **100 preset +20 user =120**. Initial user fill and factory write protection unverified. [German][SL1B-D] |
| Synth / acoustic | ACOUSTIC is a named pedal choice; simulation behavior and synth architecture unverified. [English][SL1B-E] |
| I/O | One normal mono input; one stereo output/phones. Socket sizes and complete port inventory unverified; USB, MIDI, AUX, external EXP and effects loop not established. [English][SL1B-E] |
| Conversion | 24-bit AD/DA; sample rate and USB audio unknown. [English][SL1B-E] |
| Power / battery / USB | **9V DC, approximately200mA consumption**, or4AA; approximately7.5h alkaline. Optional adapter; polarity, barrel dimensions and USB power unknown. Do not transfer IIB adapter identity. [German][SL1B-D] |
| IR / NAM / capture | User IR, native/converted NAM and proprietary capture import unknown. |
| Editor / software | Editor availability and supported Windows/macOS/mobile versions unknown. |
| Looper / drums / live | Tuner A0–E6; calibration438–445Hz. Looper, drums, scenes, trails and routing details unknown. [German][SL1B-D] |
| Used IDR / new IDR | **Unknown / unknown**. Exact Indonesian Shopee searches for stomplab 1b, stomplab ib and stomplab1b returned no exact offer on2026-10-18; this does not establish unavailability. Condition, stock, region, warranty, vouchers and checkout total unknown. |
| Power / bundle | English specifies test batteries included; German excludes batteries. Preserve regional conflict; actual seller bundle unknown. [English][SL1B-E];[German][SL1B-D] |

### StompLab 1B category inventory

Manufacturer category counts reconcile to60. AMP and DRIVE counts do not establish independent simultaneous slots. [VOX English][SL1B-E]

| Category | Named choices |
|---|---|
| Pedal9 | Compression; Exciter; Fixed Wah; Auto Wah; Brn Octave; Acoustic; U-Vibe; Tone; Ring Mod |
| Amp10 | Valve1; Valve2; Classic; Scooped; LA Studio; Gold Panel; Jazz; Studio; AC100; UK Major |
| Drive8 | Tube OD; Fat Distortion; Orange Distortion; Shred Distortion; Fuzz; Octa Fuzz; Techno Fuzz; Crusher |
| Cabinet12 | LA4×10; LA1×18; Metal4×10; UK4×12; UK4×15; Classic8×10; Modern4×10; Studio1×15; Jazz1×15; AC2×15; Combi; Custom |
| Modulation9 | CE Chorus; Multi Chorus; Flanger; Org Phase; Twin Tremolo; G4 Rotary; Pitch Shift; Filtron1(auto); Filtron2(manual) |
| Delay8 | Analog Delay1–4; Echo1–4 |
| Reverb3 | Room; Spring; Hall |
| NR1 | Noise reduction |

<!-- comparison evidence ends -->

Source access: English and German exact-model product bodies opened as browser text. Japanese exact-model specifications read in search cache; direct reopening timed out. No own IB manual inspected; family claims remain qualified.

[SL1B-E]: https://voxamps.com/product/stomplab-1b/
[SL1B-D]: https://voxamps.com/de/produkt/stomplab-ib/
[SL1B-J]: https://voxamps.com/ja/product/stomplab-1b/
