# TC Electronic multi-effects

[Repository](README.md) · [Guitar](ALL-GUITAR.md) · [Vocal](ALL-VOCAL.md)

## M100

Checked 2026-10-17; partial. Guitar/vocal instrument and mixer-path processor; direct microphone preamp/phantom and bass suitability unverified. Ownership unknown.

<!-- comparison evidence begins -->

| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression | No built-in pedal; external footswitch bypass is documented, expression/toe support unresolved. | [Product][M100-P]; [QSG pp24–25][M100-M] |
| K/F/B | **5 rotary / 0 built-in footswitches / 2 buttons**: Input, Output, Mix, Effects, Parameter; Bypass, Tap/Select. Text inventory; visual confirmation pending. | [QSG pp24–25][M100-M] |
| Display | Status/level LEDs; published screen specifications unresolved. | [QSG pp24–25][M100-M] |
| Processing / categories | **16 selectable programs**, not16 simultaneous blocks: Cathedral, Concert, Club, Chamber, Gold Plate, Gated Reverb, Reverse Reverb, Ambience, Delay, Chorus, Flanger, Phaser, Rotary, Pitch Shift, Delay+Reverb, Chorus+Reverb. Combined programs establish multiple processing functions. | [Product][M100-P]; [QSG pp36–37][M100-M] |
| Editor / firmware transport | Current QSG has a dedicated **MIDI IN SysEx .syx update procedure**, naming MIDI communication software such as MIDI-OX. This corroborates the MIDI connector statement, but establishes neither a patch editor nor supported OS versions. Applicability to older hardware remains unresolved. No update performed. | [QSG p69][M100-M] |
| Categories / parameter controls | Reverbs: time + Brilliance toggle; Ambience: room size + Brilliance. Delay: repeats + tap interval. Chorus/Flanger/Phaser: intensity + tap tempo. Rotary: intensity + speed toggle. Pitch Shift: **±12 semitones** + Detune toggle. Combined effects: delay/reverb or chorus/reverb ratio; Tap/Select controls delay interval or reverb time respectively. Numerical timing limits unverified. | [QSG p58][M100-M] |
| Preset memory | Parameter changes retained temporarily until power-off; user-store capacity unresolved. | [QSG pp24–25][M100-M] |
| Synth / acoustic | Dedicated synth/acoustic conversion unresolved; pitch shifting is documented. | [QSG pp36–37][M100-M] |
| I/O | Two quarter-inch inputs, two impedance-balanced TRS outputs, TS footswitch bypass, power. Current QSG also lists **MIDI DIN for CC/control and firmware updates**; hardware revision applicability pending. | [QSG pp24–25,92–93][M100-M] |
| I/O / input conflict | Product says balanced/unbalanced inputs; QSG specifications say unbalanced TS, approximately7.5kΩ. Preserve discrepancy; output impedance approximately220Ω. | [Product][M100-P]; [QSG pp92–93][M100-M] |
| Power / battery / USB | **12 V DC/400 mA external supply; approximately3.5 W consumption**. Polarity, actual current, battery and USB operation unresolved. Regional mains supply variants; no universal-mains assumption. | [QSG pp92–93][M100-M] |
| Dimensions / mass | **46 H ×191 W ×99 D mm;0.6kg**. | [QSG pp92–93][M100-M] |
| IR / NAM / capture | Import/capture support unresolved. | Unresolved |
| Editor / platforms | MIDI update statement does not establish computer editor or supported OS. | [QSG pp24–25][M100-M] |
| Live / routing | Mono/stereo operation; Input1 for mono, dry/wet Mix, tap tempo or parameter selection. Looper/drums/scenes unresolved. | [Product][M100-P]; [QSG pp24–25][M100-M] |
| Instrument scope | QSG explicitly describes guitar and vocal applications, including combined delay/reverb. Vocal inclusion concerns mixer/instrument processing, not direct microphone input, phantom power or harmony. | [QSG pp36–37][M100-M] |

### Separate IDR hardware offers

| Condition | Evidence | Source |
|---|---|---|
| Used | No qualified offer. | — |
| New | No condition-confirmed offer. | — |
| Unverified condition | **Rp1.950.000**, Imagination Music Store, shop19576516/item6955147985, Kota Jakarta Pusat. Checked2026-10-17; index crawled last month, preorder15days with September16 estimate. Historical ask, not live stock/checkout. | [Item][M100-O] |

<!-- comparison evidence ends -->

Working state, authenticity, hardware revision, bundle, adapter, warranty, shipping/tax and voucher eligibility unresolved. Direct QSG open failed; indexed official text readable. No filesystem download or visual inspection claimed.

[M100-P]: https://www.tcelectronic.com/en/products/0828-AAH
[M100-M]: https://mediadl.musictribe.com/media/PLM/data/docs/P0CAH/QSG_TE_0828-AAH_M100_WW.pdf
[M100-O]: https://shopee.co.id/TC-Electronic-M100-Stereo-Multi-Effects-Processor-i.19576516.6955147985

## PLETHORA X3

Checked 2026-10-17; partial. Guitar multi-effects; bass/vocal suitability and ownership unverified.

<!-- comparison evidence begins -->

| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression | No built-in treadle; **three pressure-sensitive MASH footswitches** provide assignable expression. External EXP socket absent from complete specification connector list; toe separate unresolved. | [Product][PX3-P]; [QSG p23][PX3-M] |
| K/F/B | **5 rotary /3 footswitches /0 separate buttons** from complete textual control inventory:Effect,TonePrint,three parameter knobs;three MASH. Play/Edit and Board selector switches separate;push encoders counted once. Earlier button uncertainty resolved by inventory,not visual inspection. | [QSG controls/specifications][PX3-M];[original V0.0 copy pp18–19,63][PX3-QM] |
| Display | Multiple LCD readouts referenced; diagonal/color/touch unresolved. | [QSG p22][PX3-M] |
| Processing / categories | **Three effect slots**, flexible order; numerical DSP restrictions pending. Current product lists Phaser, Vibe, Looper, Reverb, Delay, Octaver, Pitch Shifter, Chorus, Compressor, Doubler, Flanger, Tremolo, Harmony, Gate, Vibrato, Vintage Echo. Later own-applicable additions and count basis below;complete latest library unverified. | [Product][PX3-P] |
| Categories / documented choice counts | Product lists **16**:modulation6,pitch/octave/harmony3,delay2,and reverb/compression/doubler/gate/looper1 each. **1.5.6 adds Infinite Sample Sustainer**,giving17 known effects;Tap/Tuner utility separate. Derived union,not a certified complete newest library. | [Own product][PX3-P];[Shared release notes][PX3-F156] |
| Categories / Infinite restriction | Firmware**1.5.6,2025-03-23** sustainer holds notes/chords but omits standalone Infinite’s reverb and Kill Dry;reverb needs another slot. Sample sustain does not establish an oscillator synth. | [Shared release notes][PX3-F156] |
| Editor / newer effect requirement | Infinite editing needs **TonePrint4.6.18 and refreshed content**. Earlier4.2+ guide requirement is not enough for this later effect. Installed versions/currentOS support unverified. | [Shared release notes][PX3-F156] |
| Live / newer footswitch modes | **1.5.6 adds momentary and momentary+MASH**;effect engages while held. Second-foot-function None renamed Latching. | [Shared release notes][PX3-F156] |
| Live / tempo synchronization | **1.4.3,2023-10-19** adds per-slot global Tempo Sync,MIDI clock,and Tap/Tuner utility. MIDI expression explicitly works without an analog EXP socket. | [Original release-history conversion][PX3-FM] |
| Memory / restore points | **1.4.3** supports restore-point create/apply/export/import;apply/import replaces user TonePrints,Boards/settings **and firmware version**. Import also replaces local restore point. Not an IR loader. | [Original release-history conversion][PX3-FM] |
| Live / saving exception | EDIT-mode parameter changes auto-save. **PLAY-mode HOT KNOB tweaks do not auto-save** and serve live adjustment only. This qualifies the product’s broad auto-save statement. HOT KNOBZ are assigned in Board settings. | [QSG pp18–19][PX3-M] |
| Controls / push encoders | EFFECT and TONEPRINT both have documented press actions; TonePrint hold opens UniTune, press again or any footswitch exits. These presses belong to the rotary encoders, not extra separate buttons. PLAY/EDIT and BOARD remain selector switches. | [QSG pp18–19][PX3-M] |
| Live / secondary footswitch functions | PLAY-mode hold can invoke **MASH, RAMP or TAP TEMPO**, configured per Board. MIDI In/Thru can remotely control switches, Board changes and effect parameters. USB Mini-B connects TonePrint App on computer/mobile and performs firmware updates; this is not USB audio/power proof. | [QSG pp18–19][PX3-M] |
| Expression / MIDI control | Shared official X5/X3 table maps **CC100 Global Expression**, CC107–109 Hot Knobs; slots1–3 MASH on CC70/75/80 and expression modifiers CC71/76/81. MIDI expression is distinct from a dedicated analog EXP socket or toe switch. | [Official MIDI CC table][PX3-C] |
| Live / MIDI looper | CC110 Record,111 Play,112 Clear,113 Pause; values0–24 target slot1,25–50 slot2,51–76 slot3. Table marks slots4–5 **X5-only**. CC92 tap,93 tuner,94/95 Board down/up. This proves X3 looper command support, not recording duration. | [Official MIDI CC table][PX3-C] |
| Processing / published latency | **0.8–2.4ms** in own-model specification table. Not a fixed value for every Board,measured result or Board-change/loading time. | [QSG p23][PX3-M];[original copy p63][PX3-QM] |
| Editor / Bluetooth operating limits | **4.2 Low Energy,2.402–2.48GHz,40 RF channels,8dBm**;range≤10m measured in open space,obstacles reduce it. RF channels are not audio channels;audio streaming remains unverified. | [Original QSG copy p63][PX3-QM] |
| Preset memory | **Up to127 boards;75 TonePrint slots per effect**; separate from three simultaneous slots. EDIT settings auto-save; PLAY HOT KNOB tweaks do not. Factory-filled subset unresolved. | [Product][PX3-P] |
| Synth / acoustic | Dedicated synth/acoustic conversion unresolved; octave/pitch/harmony do not establish these. | Unresolved |
| I/O | Two unbalanced quarter-inch TS inputs (**1MΩ**), two unbalanced TS outputs; MIDI In/Thru five-pin DIN; Mini-B USB; DC input. USB audio/power unverified. | [QSG p23][PX3-M] |
| Power / battery / USB | **9V DC center-negative**,5.5/2.1mm; guide specifies **>600mA included supply**. Actual draw/battery/USB power unresolved. | [QSG p23][PX3-M] |
| Dimensions / mass | **56.02H ×176.53W ×116.75D mm;0.775kg**. | [QSG p23][PX3-M] |
| IR / NAM / capture | End-of-chain cabinet simulation documented; user IR, native/converted NAM and capture loading unresolved. | [Product][PX3-P] |
| Editor / platforms | TonePrint mobile app **4.2+**, Apple/Google app stores, Bluetooth pairing; only one USB/Bluetooth device connection at once. Editor supports customization, exact desktop OS compatibility pending. Bluetooth4.2LE; audio streaming not established. | [Product][PX3-P]; [QSG pp22–23][PX3-M] |
| Live / routing | Tape Deck Looper, UniTune tuner, Quick Swap order changes, selectable left/right signal direction, cab sim and MASH mappings. Loop duration/drums/scenes pending. | [Product][PX3-P] |

### Separate IDR hardware offers

| Condition | Evidence | Source |
|---|---|---|
| Used | No condition-confirmed offer. | — |
| New | No condition-confirmed offer. | — |
| Unverified condition | **Rp6.180.000**, NEO MUSIC, shop158235298/item28021818540,Kota Sukabumi; three-month crawl, July2 arrival text. | [Item1][PX3-O1] |
| Unverified condition | **Rp7.508.100**, Gelora Musik Serpong,shop306155985/item23943061836,Kab.Tangerang; five-month crawl, delivery unavailable. | [Item2][PX3-O2] |


### PLETHORA X3 — bypass specification and named base inventory

Checked2026-10-18.

| Field | Evidence / qualification |
|---|---|
| I/O / bypass specification | Own-model quick guide V0.0,printedp63,lists **True Bypass**. This is a manufacturer specification,not a measured bypass test orproof of trails/power-failure behavior. [Manufacturer-authored copy][PX3-QM] |
| Category choices / exact base names16 | HELIX PHASER;VISCOUS VIBE;TAPE DECK LOOPER;HALL OF FAME2 REVERB;FLASHBACK2 DELAY;SUB N UP OCTAVER;BRAINWAVES PITCH SHIFTER;CORONA CHORUS;HYPERGRAVITY COMPRESSOR;MIMIQ DOUBLER;VORTEX FLANGER;PIPELINE TAP TREMOLO;QUINTESSENCE HARMONY;SENTRY NOISE GATE;SHAKER VIBRATO;ALTER EGO VINTAGE ECHO. These are the own-model product page’s16base entries already counted above,not16simultaneous effects;laterInfinite addition remains separate. [Exact manufacturer product][PX3-P] |

<!-- comparison evidence ends -->

Checked2026-10-17; historical indexed asks, not current stock/checkout. Condition,variant,bundle,adapter,working state,authenticity,warranty,shipping/tax,vouchers unresolved. No download or visual inspection claimed.

[PX3-P]: https://www.tcelectronic.com/en/products/0709-AIS
[PX3-M]: https://mediadl.musictribe.com/media/PLM/data/docs/P0EB4/PLETHORA-X3_QSG_EN.pdf
[PX3-O1]: https://shopee.co.id/TC-Electronic-PLETHORA-X3-TonePrint-Pedalboard-with-up-to-127-Boards-3-Pedal-Slots-i.158235298.28021818540
[PX3-O2]: https://shopee.co.id/Multi-Efek-Pedal-Gitar-TC-Electronic-Plethora-X3-TonePrint-i.306155985.23943061836

[PX3-C]: https://mediadl.musictribe.com/download/software/tcelectronic/Plethora_X5/PX5_3_MIDI_CC_table.pdf

Newer firmware evidence checked2026-10-17. Shared manufacturer notes explicitly mark1.4.3 and1.5.6 forPX5/PX3;older PX5-only entries were not assigned toX3. Original conversion matches manufacturer-hosted indexed1.5.6 text;no generatedFAQ used. No software/firmware was downloaded or installed.

[PX3-F156]: https://cdn.mediavalet.com/aunsw/musictribe/7oqt3nY_P0ypQrubxyiAZA/ZxnHhPbDPka4xmUQl3N2-Q/Original/Plethora_X5_X3_Release_notes_FW_v1_5_6.pdf
[PX3-FM]: https://manuals.plus/m/fab495897f61212f13d7fd3403d4a371bcb2d147dc9c72fd72db55684cdb91f7

Control-count recheck2026-10-17 uses the complete13-callout own-model text and specifications. Manufacturer endpoint returned502;readable manufacturer-authored35-page multilingual copy identifies PLETHORA X3,V0.0,©2022 andmatches indexed officialcontrols/specifications. Its printedp63 corresponds to official English-onlyp23;pagination differs. Screens/photos were not inspected.

[PX3-QM]: https://www.adorama.com/col/productManuals/TC79AIS861.pdf

## PLETHORA X5

Checked 2026-10-17; partial. Guitar/bass shared processor; ownership and vocal suitability unverified.

<!-- comparison evidence begins -->

| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression | No built-in treadle; **five MASH pressure switches**, each maps up to three parameters. External TRS EXP input; toe behavior unresolved. | [Product][PX5-P]; [QSG pp14–15][PX5-M] |
| K/F/B | **5 rotary / 5 footswitches / 0 separate buttons in the textual control inventory**. EFFECT/TONEPRINT push encoders and three parameter knobs. Specifications explicitly classify PLAY/EDIT and BOARD as selector switches, despite the controls prose calling PLAY/EDIT a knob. Encoder presses counted once; visual corroboration pending. | [QSG pp14–15,33][PX5-M] |
| Display | LCD displays show slot effects or editing information; diagonal/color/touch unresolved. | [QSG pp14–15][PX5-M] |
| Processing / categories | **Up to five TonePrint pedals per Board**, freely ordered. Compression, modulation, pitch, gate, reverb/delay documented; complete firmware-qualified catalogue pending. | [Product][PX5-P] |
| Categories / firmware1.5.6 sustainer | **2025-03-23 adds Infinite Sample Sustainer**,holding notes/chords. PLETHORA version omits its standalone pedal’s reverb section and **Kill Dry**;another Hall of Fame slot can add reverb. Not proof of an oscillator synth. | [Newer official notes][PX5-F156] |
| Editor / sustainer compatibility | Editing Infinite TonePrints requires **TonePrint4.6.18 plus updated app content**. Historical4.5.5 requirement remains for the older release;not sufficient evidence for this effect. Installed versions unknown. | [Newer official notes1.5.6][PX5-F156] |
| Live / firmware1.5.6 switching | Adds **momentary**,effect active only while pressed,and momentary+MASH modes. Second-foot-function menu renames None to Latching. This is switch behavior,not extra physical switches. | [Newer official notes][PX5-F156] |
| Live / firmware1.4.3 tempo | **2023-10-19** adds per-slot Tempo Sync to global tempo,MIDI clock sync,and Tap/Tuner utility. Unsynced slots remain independent;temporary parameter-modifier changes return to global tempo. | [Original release-note conversion][PX5-FM] |
| Memory / restore-point scope | **1.4.3 restore points cover user content and firmware**. Applying/importing overwrites stored TonePrints,Boards/settings and changes firmware to the snapshot’s version;system import also overwrites the local restore point. This is not an IR/capture loader. | [Original release-note conversion][PX5-FM] |
| Editor / historical firmware requirements | **Firmware1.3.11,2022-03-03** recommends TonePrint app **4.5.5+** for full new-effect benefit. Units on1.0.101 require intermediate1.1.55 before1.2.18 or later. This is historical compatibility evidence, not a latest-firmware claim. | [Official release notes][PX5-F] |
| Processing / firmware bypass change | Firmware1.3.6 limited FlashbackII/AlterEgo feedback to80% when bypassed in buffered mode. **1.3.11 respects higher feedback**, permitting self-oscillating bypass trails. Modulation/low-end and vibrato-subtype fixes also documented. | [Official release notes][PX5-F] |
| Editor / firmware transport | Guide describes USB mass-storage transfer of a .bin file followed by power-cycle installation. This proves update transport, not USB audio or bus power. No update or download performed. | [Official release notes][PX5-F] |
| Processing / latency | Published **0.8–2.4 ms** latency range; do not infer one fixed value for every Board. | [QSG p33][PX5-M] |
| Editor / Bluetooth specification | **Bluetooth4.2 Low Energy**, up to10m in open space; structures affect range. Pair through global Bluetooth settings and TonePrint app. This establishes app connectivity, not Bluetooth audio streaming. | [QSG pp32–33][PX5-M] |
| Categories / historical firmware additions | **1.3.6,2022-01-13** adds Alter Ego Vintage Echo. Also documents reversed chain-order display, improved external EXP/MIDI response and faster Board changes. These are dated changes, not a complete current library. | [Official release notes][PX5-F] |
| Categories / firmware1.2.18 additions | **2020-12-18 adds Viscous Vibe,Helix Phaser,Tape Deck Looper**. Viscous Vibe defaults to Ramp as its second footswitch function;MASH can replace it in Board settings. These dated additions do not establish the complete current catalogue. | [Own X5 release notes][PX5-F] |
| Live / Board navigation versus Quick Swap | Optional global two-switch navigation:**1+2 Board Down;2+3 Board Up**. While board number shows,1/3 continue down/up. **Disable this mode for Quick Swap**. Introduced1.2.18;not proof of seller firmware. | [Own X5 release notes][PX5-F] |
| Expression / Hot Knob scope | The three Hot Knob assignments are **Board-level settings**,controlling multiple pedal parameters in Play mode;not three additional audio blocks. | [Own X5 release notes1.2.18][PX5-F] |
| Memory / automatic storage | Product documents automatic settings storage as edits occur. This does not establish a factory-filled Board count or persistent audio-loop storage. | [Product][PX5-P] |
| Live / buffered no-trails | Firmware1.3.6 adds **Buffered / No Trails**, retaining buffering while cutting delay/reverb tails when disengaged. Distinguish it from buffered trailing behavior and the later1.3.11 feedback change. | [Official release notes][PX5-F] |
| Expression / MIDI mapping | **CC100 Global Expression** maps0–125 to0–100%; Hot Knobs CC107–109. MASH for slots1–5:CC70/75/80/85/90; expression modifiers CC71/76/81/86/91. Physical EXP and MIDI expression are separate control paths. | [Official X5/X3 MIDI table][PX5-C] |
| Live / MIDI looper mapping | CC110 Record,111 Play,112 Clear,113 Pause. Values0–24/25–50/51–76/77–102/103–127 target slots1–5 respectively. Slots4–5 explicitly X5-only. CC92 tap,93 tuner,94/95 Board down/up. | [Official X5/X3 MIDI table][PX5-C] |
| Preset memory | **127 custom Boards;75 TonePrint slots per pedal**. Factory-filled subset unresolved; Board count is not simultaneous block count. | [Product][PX5-P] |
| Synth / acoustic | Dedicated synth/acoustic conversion unresolved. | Unresolved |
| I/O | Stereo quarter-inch TS inputs/outputs; TS Send/Return insert; TRS EXP; MIDI In/Thru; USB for computer TonePrint/update; DC input. USB audio/power unresolved. | [QSG pp14–15][PX5-M] |
| Power / battery / USB | **9V DC,>600mA included supply**,5.5/2.1mm centre-negative. Actual draw,battery/USB operation unresolved. | [QSG controls/specifications][PX5-M] |
| Dimensions / mass | Guide prints **298.5×116×53mm under H×W×D**,1.4kg. Axis-label inconsistency preserved; no silent normalization or size-bin assignment. | [QSG specifications][PX5-M] |
| IR / NAM / capture | **Nine global proprietary cabinet simulations**, including bass use. User IR/native or converted NAM/capture support unresolved. | [Product][PX5-P] |
| Editor / platforms | Own X5 release notes, **1.1.55 dated 2020-11-09**, explicitly list TonePrint desktop editor for **Mac and PC**, and mobile app for **iOS and Android**. Historical platform evidence only: current supported OS versions, processor architecture and present app availability remain unverified. Bluetooth/USB app connectivity does not establish USB audio or power. | [Official release notes, version1.1.55 section][PX5-F]; [QSG pp14–15][PX5-M] |
| Live / looper | RAM looper: **40s stereo/80s mono**, up to five instances per Board. Multiple instances do not imply five times shared memory capacity. Drums/scenes unresolved. | [Product][PX5-P] |
| Live / routing | Insert allows external drive or four-cable setup; Quick Swap reorders effects. | [Product][PX5-P] |
| Bass capability | Own product explicitly offers bass-oriented cabinet simulation; shared bass inclusion does not certify every effect equally on bass. | [Product][PX5-P] |

### Separate IDR hardware offers

| Condition | Evidence | Source |
|---|---|---|
| Used | No qualified offer. | — |
| New | No condition-confirmed offer. | — |
| Unverified condition | **Rp9.105.200**,NEO MUSIC,shop158235298/item27271818642,Kota Sukabumi. Checked2026-10-17; three-month indexed crawl,July2 delivery text. Historical ask, not current stock/checkout. | [Item][PX5-O] |

<!-- comparison evidence ends -->

Variant,bundle,adapter,working state,authenticity,warranty,shipping/tax,vouchers unresolved. No download or visual inspection claimed. All facts from own-model sources; no X3 specification substitution.

[PX5-P]: https://www.tcelectronic.com/en/products/0709-AIK
[PX5-M]: https://mediadl.musictribe.com/media/PLM/data/docs/P0D9M/QSG_TE_0709-AIK_PLETHORA-X5_WW.pdf
[PX5-O]: https://shopee.co.id/TC-Electronic-PLETHORA-X5-TonePrint-Pedal-Board-Loaded-with-Favorite-FX-and-5-MASH-Footswitches-i.158235298.27271818642

[PX5-F]: https://mediadl.musictribe.com/media/PLM/data/docs/P0D9M/Release-Notes_TE_P0D9M_PLETHORA-X5_Firmware-Update_v1.3.11_2022-03-03_Rev.2.pdf

[PX5-C]: https://mediadl.musictribe.com/download/software/tcelectronic/Plethora_X5/PX5_3_MIDI_CC_table.pdf

Newer documentation checked2026-10-17: manufacturer-hosted indexed1.5.6 text explicitly names both PX5/PX3 andmatches the converted16-page release-history body,including older own-X5 revisions already verified. Direct manufacturer CDN fetch failed500;conversion used only as original release text,not generated FAQs. Neither1.5.6 latest-status nor seller-installed firmware certified.

[PX5-F156]: https://cdn.mediavalet.com/aunsw/musictribe/7oqt3nY_P0ypQrubxyiAZA/ZxnHhPbDPka4xmUQl3N2-Q/Original/Plethora_X5_X3_Release_notes_FW_v1_5_6.pdf
[PX5-FM]: https://manuals.plus/m/fab495897f61212f13d7fd3403d4a371bcb2d147dc9c72fd72db55684cdb91f7

## M350

Checked2026-10-17. Partial dual-engine rack multi-effects. [Manufacturer English manual](https://cdn.mediavalet.com/aunsw/musictribe/oexFf_5Xrkic0GfCn2XAEw/j6PZVTEe-UynlIA4ETJYOA/Original/tc_electronic_m350_manual_english.pdf),34pages,Rev1.1/SW1.00,productE60505812;webtext only,no download/visualaudit.

| Field | Evidence / gaps |
|---|---|
| Expression | No builtin pedal;¼TRS socket takes **momentary bypass(tip)/tap(ring)** switches. ContinuousEXP/toe support unestablished. |
| Controls | **10rotaries**,derived text;integratedfoot0;separatebuttons count unresolved becauseBYPASS described asknob. |
| Display | Two seven-segmentdigits+LEDs;diagonal/color/touch unknown. |
| Processing / choices | **2engines:15delay/effects choices+15reverbs**,eachplusOff. Serial ordualinput/commonoutput;analog-only parallel option. |
| Presets | **99user memories;256factory selector combinations**,not256storedpatches. Advertised355 does notmean355editablememories. |
| Synth / acoustic | Dedicated synth/acousticconversion unknown. |
| Dimensions / weight | **483×44×105.6mm;1.5kg**;published19×1.75×4.2inch order. |
| I/O | Balanced¼L/Rinputs/outputs;RCA S/PDIFin/out;DIN MIDIin/out;¼pedal;ACmains. Headphones/XLR/USB notlisted. |
| Power | **100–240VAC50–60Hz auto;less than15W**. Internal supply;DCpolarityN/A. Battery/USBpower unknown. |
| Software | Manufacturer cutsheet advertises **AU/VST editor**;exactOS/currentcompatibility unverified. MIDI control/bulkdump documented;notUSB audio. |
| IR / NAM / captures | UserIR,native/convertedNAM,capture import unknown. |
| Looper / drums / live | Looper/drums/scenes unknown;tap/MIDIclock. Bypass mutes indualinput,passes signal inserial. |
| Instrument scope | Guitar setup requirespreamp;vocal+guitar dualinput example. Bass capability unclassified. |

[Cutsheet](https://service-tcgroup.tcelectronic.com/media/M350_Cutsheet_web.pdf) indexed manufacturer text only;direct502. Editor/355marketing distinguished frommanual memory behavior.

### M350 — separate IDR hardware offers

| Condition / seller | IDR evidence | Exact item |
|---|---|---|
| Used | Unknown | — |
| TitleNEW,condition unverified / PCdada,Kota Jakarta Barat | **Rp6.682.240;indexed PreOrder15days**,index2months,checked2026-10-17;directopenfailed. Currentstock,selectedvariation,bundle,warranty,voucher,shipping/tax unknown;Augustdelivery stale. | [1003923494/15899349001](https://shopee.co.id/%E2%9C%85-NEW-TC-electronic-M350-vocal-reverb-effect-dual-engine-digital-effect-processor-professional-stage-performance-effect-karaoke-i.1003923494.15899349001) |
| Unallocatedvariation / Puddingstoree,Kota Jakarta Barat | **Rp8.870.555;2variations;PreOrder30days**,index2months. Selectedhardwarevariant andcondition unverified;not aqualifiedmodelprice orliveprice range. | [1696675139/43128792310](https://shopee.co.id/NEW-TC-Electronic-M350-Vocal-Reverb-Effect-Dualengine-gital-Effect-Processor-Professional-Stage-Performance-Effect-Karaoke-i.1696675139.43128792310) |
### M350 — named engines and pedal control

Checked 2026-10-17 against the [Rev1.1 manufacturer manual](https://cdn.mediavalet.com/aunsw/musictribe/oexFf_5Xrkic0GfCn2XAEw/j6PZVTEe-UynlIA4ETJYOA/Original/tc_electronic_m350_manual_english.pdf),pp5,8,18–20.

| Engine | Fifteen choices, plus Off |
|---|---|
| Delay/effects | Comp;Hard Comp;De-Esser;Smooth Chorus;Lush Chorus;Instrument Flanger;Tremolo;Vintage Phaser;Smooth Phaser;Slapback Delay;PingPong Delay;Soft Delay;Triplets Delay;Studio Delay;Dynamic Delay |
| Reverb | TC Classic Hall;Cathedral;Vocal Reverb;Live Vocal;Hall Acoustic;Drum Ambience;Drum Room;Ambience;Living Room;Nearfield;Damped Room;Silver Plate;Gold Plate;Spring Vintage;Live Stage |

Hall Acoustic andDrum names describe reverb algorithms,not acoustic-guitar conversion oradrum-pattern generator. The effects selector chooses one delay/modulation/dynamics algorithm,not all simultaneously.

The¼TRS pedal input uses momentary switches: **tip bypass,ring tap tempo**. This verifies footswitch control,not analog continuous-expression support. S/PDIF output runs44.1kHz onanaloginput,or follows avalid44.1/48kHz digitalinput.

The overview’s “BYPASS knob” wording remains acontrol-count ambiguity;button count awaits qualified visual/original diagram evidence. No image was inspected orsoftware downloaded.

### M350 — analog interface and reset limits

Checked 2026-10-18 against the [manufacturer Rev1.1/SW1.00 manual,pp31–32](https://cdn.mediavalet.com/aunsw/musictribe/oexFf_5Xrkic0GfCn2XAEw/j6PZVTEe-UynlIA4ETJYOA/Original/tc_electronic_m350_manual_english.pdf),productE60505812. Text only;no local download or visual inspection.

| Field | Evidence / qualification |
|---|---|
| I/O / analog input | **21 kΩ balanced/13 kΩ unbalanced**. Maximum/minimum input levels at0dBFS: **+24/0 dBu**;sensitivity **−12 to+12 dBu with12dB headroom**. These describe gain-dependent full-scale limits,not two nominal operating standards. |
| I/O / analog output | **40 Ω balanced/20 Ω unbalanced;+14 dBu maximum**. Input and output impedances remain distinct. |
| Processing / conversion | ADC and DAC each **24-bit,128×oversampling**. **24-bit S/PDIF** supports44.1kHz,or44.1/48kHz digital input. Digital processing delay **.08ms at48kHz** is not complete analog round-trip latency. |
| Memory / factory reset | Hold TAP while reconnecting power;flashingR,then LOAD confirms;power-cycle afterward. **All User presets are lost**. MIDI bulk receive is disabled when receive channel isOF. |

The alternate MusicTribe mediadl endpoint exposed indexed specifications but direct access failed;the existing manufacturer CDN supplied the matching original manual. Editor compatibility,control-button count,screen details and qualified used/new prices remain unresolved.


### M350 — routing details and service-version display

Checked 2026-10-18 in the [same Rev1.1 manufacturer manual,pp12,22–23](https://cdn.mediavalet.com/aunsw/musictribe/oexFf_5Xrkic0GfCn2XAEw/j6PZVTEe-UynlIA4ETJYOA/Original/tc_electronic_m350_manual_english.pdf). Original text only;no local download or hardware operation.

| Field | Evidence / qualification |
|---|---|
| Routing / parallel mono setup | **Analog input only**:Dual Input switch IN,left input connected,right empty. Left is internally split to both engines,which share stereo outputs. Mixer aux use requires MIX100%wet. This is not a freely selectable digital parallel routing mode. |
| Routing / serial versus dual input | Serial passes Delay/Effects then Reverb. Dual Input processes two separate sources through the respective engines with common outputs;it does not provide isolated output pairs per source. |
| Editor / firmware-display distinction | PRESET ON/OFF held with UP/DOWN selects **AP** application or **Fr** front software version for service. These identify hardware software versions,not AU/VST editor releases or supported desktop operating systems. Existing cutsheet editor claim remains separately qualified. |

Editor installers/current OS compatibility,control-button count,display diagonal/touch and qualified used/new IDR evidence remain unresolved.


### M350 — digital clock fallback and MIDI backup

Checked 2026-10-18 from original text in the [Rev1.1/SW1.00 manufacturer manual, printed pp14–15,31](https://cdn.mediavalet.com/aunsw/musictribe/oexFf_5Xrkic0GfCn2XAEw/j6PZVTEe-UynlIA4ETJYOA/Original/tc_electronic_m350_manual_english.pdf). No download or device operation.

| Field | Evidence / qualification |
|---|---|
| I/O / digital-lock fallback | For a digital insert, the connected interface supplies master clock. If digital input is selected but no valid signal arrives within5seconds, DIGI IN flashes and M350 returns to internal clock and analog operation while continuing to seek digital input. A selected digital input therefore does not guarantee a permanently digital signal path. |
| Routing / standalone A/D conversion | With analog input feeding S/PDIF output, M350 supplies master clock and the receiving interface must follow it. Both effect selectors Off provide conversion without added effects. Using Bypass for this purpose requires Serial routing; Dual Input bypass mutes instead. This is S/PDIF conversion, not USB audio. |
| Editor / MIDI backup operation | Hold PRESET ON/OFF about2.5seconds, select Bulk Dump with arrows, then LOAD sends presets to a recording MIDI device. Receive is automatic unless MIDI Receive Channel isOF. This is backup support, not proof of AU/VST editor compatibility. |


## M-One XL

Checked 2026-10-17; partial. [Original English manual, mirrored][M1XL-M], Rev4, product E60500152: SW2.07 XL versus1.43 Standard. Manufacturer download inaccessible; mirror adds watermarks. Text-only review.

| Field | Evidence / gaps |
|---|---|
| Expression | No integrated treadle. Quarter-inch pedal input: momentary bypass1/2/both or tap; continuous EXP/toe unknown. |
| Controls | Text-derived **4 rotaries / 0 integrated footswitches / 14 buttons**, excluding power: three level/mix/balance knobs plus CONTROL wheel; visual verification pending. |
| Display | **23-character/280-icon STN LCD**; diagonal/color/touch unknown. |
| Processing / choices | **Two engines**, one selected algorithm each. Eight reverbs: Hall,Room,Small Room,Plate1,Plate2,Spring,Live,Ambience. Three delays: One Tap,Two Tap,PingPong. Chorus/flange each Classic/4-Voice; pitch Detune/Pitch Shift; parametric EQ; Compressor/Limiter; Gate/Expander; De-esser; tremolo Hard/Soft; phaser Vintage/Smooth. Small Room/PingPong explicitly XL-only. Family/mode enumeration is not an independently verified grand algorithm count. |
| Presets | **200 factory +100 user =300 locations**; factory edits save into user bank. |
| Synth / acoustic | Dedicated synthesis/acoustic conversion unknown. |
| Dimensions / weight | **483×44×195mm;1.85kg**. Published19×1.75×8.2inch conflicts with metric depth; preserve both, do not normalize. |
| I/O | Balanced XLR L/R inputs/outputs; RCA S/PDIF in/out; DIN MIDI in/out/thru; quarter-inch pedal; mains. Headphones/USB unestablished. |
| Power | **100–240VAC,50–60Hz auto; <15W**. DC polarity N/A; operating current/battery/USB power unverified. |
| Editor / platforms | MIDI control/SysEx documented. [Historical manufacturer comparison][M1XL-C] lists editor **None**; dated context references summer2003, not current software availability. Third-party editors and current OS support unverified. |
| IR / NAM / captures | User IR, native/converted NAM and captures unknown. |
| Looper / drums / routing | Six routings: dual send/return,parallel,parallel/serial,serial,stereo-linked,dual mono. Looper/drums/scenes unknown. |
| Instrument scope | Guitar-track and lead-vocal examples support guitar/vocal inclusion; bass remains unclassified. XLR does not establish mic preamp/phantom. |

### M-One XL — separate IDR hardware offers

| Condition / seller | IDR evidence | Exact item |
|---|---|---|
| Used | Unknown | — |
| New | Unknown | — |
| Unverified / d'Acoustic,Kota Pekanbaru | **Rp2.800.000**, shop480855699/item43364186361; checked2026-10-17, two-month cached page. Shop on holiday; current stock unverified. Title original is not authenticity proof. Variant,bundle,warranty,voucher,shipping/tax unknown; August delivery stale. | [Shopee][M1XL-O] |

[M1XL-M]: https://www.liveline.be/wa_files/tc_electronic_m-one_xl_manual_english.pdf
[M1XL-O]: https://shopee.co.id/Efek-TC-Electronic-M-One-XL-original-i.480855699.43364186361

Manual printed pp6–8,12–17,40 support controls, routing, memory and XL specifications. Guitar/vocal examples pp13–14; no direct passive-instrument suitability inferred.

### M-One XL — MIDI and routing qualifications

Checked2026-10-17 against [Rev4 manual][M1XL-M],printed pp12,14–15. **Bank-select conflict:** prose says CC32; map labels CC0, values0/1/2 for factory1–100/factory101–200/user1–100. Preserve mismatch; no hardware test. SysEx changes parameters/algorithms/routing; bulk dump backs up presets.

Stereo-linked copies Engine1 settings into Engine2. Dual mono keeps separate mono channels. Serial MIX controls Engine1 mix; EFFECT BAL controls dry bypass around Engine2. These differ from parallel balance behavior.

[M1XL-C]: https://service-tcgroup.tcelectronic.com/media/Rev_Comparison_02b%281%29.pdf

Comparison sheet is indexed manufacturer evidence only; direct PDF inaccessible. Original manual remains accessed through the watermarked mirror; no download performed.
