# Shopee Indonesia multi-effects — second expansion batch

[Home](README.md) · [First 16 Shopee additions](shopee-multifx.md) · [Marketplace discovery](shopee-indonesia.md) · [Resume](RESUME.md) · [Methodology](METHODOLOGY.md)

**8 new partial records · checked 2026-10-14.** Together with the existing67 records, the catalogue now contains **75 distinct models across10 comparison pages**. Each new model was researched and committed separately before this integration. This is not an exhaustive Shopee inventory or a claim of current checkout stock. All used-price cells genuinely remain unverified in this batch.

Model links open the full finding, original technical sources, exact seller/item, dated price evidence, firmware context and unresolved fields. **? = unverified, not No.** Older manual values are explicitly versioned; later firmware is not assumed identical.

## 1. Hardware, expression and IDR prices

Dimensions are **W×D×H, mm**, except explicitly unresolved source orientation. Compact ≤200×140; medium ≤300×200 but not compact; large otherwise. Cable and pedal clearance are additional. K/F/B = independently adjustable rotary controls / main footswitches / separate buttons; push-encoders once, toe/power/ground switches separate.

### No built-in expression

| Model / full evidence | External expression | K/F/B | Dimensions; weight | Size class | Used IDR | Retail IDR observation |
|---|---|---|---|---|---|---|
| [M-VAVE ANN Blackbox][ann] | No dedicated EXP jack; MIDI-controller expansion is not a verified EXP mapping | 2/2/7 | 113×109×41 source L/W;410g | Compact either orientation | ? | **Rp1.089.000**, Vi Music Store; variant/stock unconfirmed |
| [M-VAVE TANK-PRO][tank] | Yes,1×TRS EXP | 5/4/12 | 260×100×52;**815g manual vs800g page** | Medium | ? | **Rp1.900.000**, Seven Stereo; old cached delivery dates, stock unconfirmed |
| [TC-Helicon Play Acoustic][acoustic] | PEDAL is Switch-3; continuous EXP not established | 2/3/10 | 200×156×45;950g | Medium | ? | **Rp5.100.000**, NEO MUSIC; stock/condition unconfirmed |
| [TC-Helicon VoiceLive Play][play] | PEDAL is Switch-3; continuous EXP not established | 2/3/10 | ?;? primary verification pending | Unknown | ? | **Rp5.280.000, SOLD OUT**, Asia Pro Sound; historical ask |

### Built-in expression

| Model / full evidence | External expression / toe | K/F/B | Dimensions; weight | Size class | Used IDR | Retail IDR observation |
|---|---|---|---|---|---|---|
| [Boin Audio BG300][bg300] | No external jack in linked manual; pressure switching | 1/2/4 | **193.5×125×56.5;454g manual profile**, revision caveat | Compact, manual profile | ? | **Rp1.749.990**, Primanada With Battery; revision/stock unconfirmed |
| [Scorpion KMF-10][kmf] | No external jack shown; toe mechanism ? | 4/2/9 | 243×165×59;710g | Medium | ? | **Rp1.350.000**, Imagination Music; stock/condition unconfirmed |
| [JOYO GEM BOX II][joyo2] | No external jack; toe-pressure switching | 2/2/5 | 243×137×62;720g without batteries | Medium | ? | **Rp1.750.000**, TOKOAUDIOPRO; stock/condition unconfirmed |
| [JOYO GEM BOX III][joyo3] | 1×EXP2; built-in toe switch | 8/3/17 | ?;? | Unknown | ? | **Rp4.800.000**, GH MUSIC; mixed cheaper variants excluded |

These are separate **asking-price observations**, not completed-sale statistics or active market ranges. Delivery, authenticity, included accessories and condition were not independently confirmed. BG300's separate Nafiri Rp1.500.000 observation has conflicting stock markers and a conflicting hardware description; it is not merged into an active range. Low prices on mixed GEM BOX III variations are not accepted as full-unit prices without identifying the selected variant.

## 2. Displays

| Model | Main display | Published diagonal | Color mode | Touchscreen |
|---|---|---|---|---|
| TANK-PRO | LCD | **2.4 inches** | Color, manual theme settings | ? |
| ANN Blackbox | Graphical screen, technology ? | ? | Color, manual on-screen icon colors | ? |
| BG300 | LCD in linked manual | **1.7 inches manual vs1.77 retailer**; revision conflict | Color | ? |
| KMF-10 | Graphical screen, technology ? | ? | Color, official photograph | ? |
| GEM BOX II | Graphical LCD | ? | ?; do not infer monochrome from manual print style | ? |
| GEM BOX III | Graphical LCD | ? | Color, manual interface illustrations | ? |
| VoiceLive Play | Graphical LCD | ? | ?; button colors are not screen colors | ? |
| Play Acoustic | Backlit graphical LCD | ? | ?; blue backlight alone is insufficient | ? |

No diagonal was measured from a photograph. A complete display field with an explicit unknown is not a verified specification. The two TC-Helicon records retain original-manual context while current firmware and hardware documentation are pending.

## 3. Processing, memory, acoustic/synth and loading

| Model | Simultaneous processing and choices | Memory organization | Synth / acoustic distinction | IR / NAM / captures |
|---|---|---|---|---|
| TANK-PRO | **10 reorderable**, DSP-limited; WAH14, FX1/FX2 shared20 each, DS30, AMP90, CAB90, EQ8, MOD20, DLY27, REV18 | **120 editable =60 factory sounds+60 effects-off starting setups** | Synth/acoustic simulator ? | Mono WAV44.1k/24-bit,1024/2048; AM4DATA imports with official NAM conversion workflow, **not unrestricted native NAM** |
| ANN Blackbox | **6 reorderable+one internal FX combination**, not7 free slots; FX3 configs, AMP20, MOD7, DLY5, REV6, CAB20 | **80 editable,40 factory-filled** | Guitar/bass amp banks; synth/acoustic sim ? | 20 CAB locations, mono WAV44.1k/24-bit/1024; proprietary AM formats; exact NAM conversion compatibility/native support unresolved |
| BG300 | **8**; NR1, FX8, DRV5, AMP15, CAB15+5 user, MOD6, DLY7, RVB7; **64 factory choices in manual vs70 retailer** | **50 factory+50 user=100**, linked manual | Synth/acoustic sim ? | **5 user IR slots**; length/format and NAM/capture support ? |
| KMF-10 | **5**; drive12,mod12,delay6,reverb4,dynamic4,filter3;18amp/cab wording varies across brand pages | Brand literally says **10–59**; actual storage organization ? | Synth/acoustic sim ? | **512-point factory IR processing**, user import/capacity and NAM ? |
| GEM BOX II | **8 fixed**; FX10,DS23,AMP7,NS1,EQ1,MOD11,DLY6,RVB7=66 | **80 factory+80 user=160**; only user bank writable | **Acoustic A/B simulators**; synth not established | No digital import connection in complete manual; factory amp processing is not IR/NAM loading |
| GEM BOX III | **9 reorderable**; FX/COMP8,DS/OD20,AMP61,CAB26,NS3,EQ4,MOD19,DLY9,RVB7=157 | **300 editable**; v1.0.0 factory99+blank201, not99+300 | **3 acoustic simulators**; synth not established | WAV IR yes; **1024 current page vs512 manual**; amp-model import not proven NAM |
| VoiceLive Play | **7 FX+Tone**; v1.0 µMod24,DLY18(+13 filters),RVB28,harmony15,double4,HardTune7,transducer8;8 active Tone styles | Saving documented; current factory/user/total counts ? | Vocal harmony/pitch/robot/formant effects; not a guitar synth/acoustic modeler | IR/NAM/capture imports not established |
| Play Acoustic | **7 vocal FX+Tone plus dedicated guitar chain**; v1.0 harmony28,double10,DLY18(+13 filters),RVB28 advertised,µMod24,transducer8; guitar RVB36,µMod6 | Counts ?; **v1.0 guitar settings global**, current firmware behavior pending | **BodyRez acoustic-pickup processing**, not proof of electric-to-acoustic sim or body-IR import | IR/NAM/capture imports not established |

Counts include amps/cabs where noted and are not sound-quality rankings. Shared FX libraries, IR locations and factory-filled patches are not extra unique algorithms or additional memory. Play Acoustic's old reverb list repeats one name; the advertised28 is retained with that discrepancy in its finding.

## 4. Power, apps, I/O and stage use

| Model | Power / battery / USB operation | Apps | Key I/O and performance details |
|---|---|---|---|
| TANK-PRO | **3000mAh/3.7V;USB5V/1A rating,5V/2A recommendation**; use while charging yes | M-EFCS Windows/macOS/iOS/Android | ¼″ in;stereo¼″+stereoXLR out;3.5mm phones;TRS EXP/MIDI-in;USB-C;**150.8s looper,100 rhythms** |
| ANN Blackbox | **2000mAh/3.7V;USB5V≥300mA**, battery or USB power explicitly documented | M-EFCS Windows/macOS/iOS/Android | ¼″ mono in/out,separate3.5mm stereo phones,USB-C;44.1k/24-bit audio/loopback;looper/drums not established |
| BG300 | **2000mAh/3.7V,USB5V/2A manual**, retailer9V claim conflicts | Windows/macOS/Android/iOS documented; current app identity/versions ? | ¼″ in/stereo out,phones-panel versus final-table inconsistency,USB-C;**2×2 USB44.1k/16-bit**;drums,tuner |
| KMF-10 | **6AA or9V centre-negative**; **300mA page vs500mA rear marking**;USB power ? | Editor and USB functions ? | AUX,¼″ in,shared¼″ out/phones,USB-C;**25s looper,6genres/40+styles** |
| GEM BOX II | **4AA or9V300mA centre-negative supply**;noUSB | No documented digital editor interface | ¼″ in/sharedstereoout-phones,AUX,DC;**180s looper,40drums+10metronomes** |
| GEM BOX III | **9V1A centre-negative supply**;battery/USB power ? | JOYO STUDIO Windows/macOS;current OS compatibility ? | ¼″ in;2¼″+2XLR out;3.5mm aux/phones;EXP2;USB-B;**52s looper,40drums+10metronomes** |
| VoiceLive Play | **12V400mA panel**;polarity/battery/USB power ? | VoiceSupport Windows/macOS **librarian/updater**,not confirmed full editor | XLR mic/stereoXLR out,aux/phones,Switch-3,USB Mini-B;**v1.0 looper15s undo/30s without**,current firmware pending |
| Play Acoustic | **12V400mA specified supply**;polarity/battery/USB power ? | VoiceSupport Windows/macOS **librarian/updater** | **48V XLR mic+¼″ guitar**;2XLR out,aux/phones,Switch-3,USB Mini-B;BodyRez/anti-feedback;**v1.0 looper15/30s**,current firmware pending |

## Source conflicts and next research

The individual notes retain **TANK-PRO weight**, **BG300 manual/revision/display/power/I/O**, **KMF-10 power/presets**, **GEM BOX III IR length**, and **TC-Helicon current firmware/memory/display/software** uncertainties. Do not fill those with sibling-model specifications.

**Next: HeadRush Core**, then Flamma FV01 and Donner Arena2000, followed by remaining Shopee-listed MOOER/Hotone/NUX/Zoom/Line6 families. Original JOYO GEM BOX remains discovery-only: a similarly titled manual contains MOOER identifiers, so it was not promoted to a JOYO-verified record. The earlier BOSS display/IDR migration remains deferred, not discarded.

[tank]: findings/2026-10-14-mvave-tank-pro.md
[ann]: findings/2026-10-14-mvave-ann-blackbox.md
[bg300]: findings/2026-10-14-boin-audio-bg300.md
[kmf]: findings/2026-10-14-scorpion-kmf-10.md
[joyo2]: findings/2026-10-14-joyo-gembox-ii.md
[joyo3]: findings/2026-10-14-joyo-gembox-iii.md
[play]: findings/2026-10-14-tchelicon-voicelive-play.md
[acoustic]: findings/2026-10-14-tchelicon-play-acoustic.md
