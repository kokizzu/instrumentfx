# Darkglass multi-effects

[All bass](ALL-BASS.md) · [Repository](README.md)

## Anagram

Bass multi-effects platform; checked2026-10-18,partial. Ownership unverified. Guitar cabinet choices do not independently establish guitar/vocal comparison membership. Expression accessory is a separate product,not another processor.

| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression / toe | No treadle in documented layout. External expression shares RETURN;requires signal onTRS ring(**RTS wiring**),sacrificing return use. Toe support unknown. | [Product][ANA-P] |
| Knobs / footswitches / buttons |6 endless push rotaries,3 footswitches;separate button census pending visual audit. Encoder pushes are not extra standalone buttons. | [Product][ANA-P] |
| Display |**7-inch touchscreen**;published color-mode detail unverified. | [Product][ANA-P] |
| Processing / category choices |Hexacore,32-bit48kHz;advertised12 serial/24 parallel blocks,50+effects. Exact category census andDSP/model-complexity restrictions unresolved. | [Product][ANA-P] |
| Factory / user / total memory |KosmOS1.17 PDF:42banks×3=126presets;factory area read-only,copyable toUser. Current1.18 product adds up to126 user areas;capacity perarea/full factory-user total not reconciled. Three scenes/preset in1.17. | [Manual][ANA-M];[1.18 product][ANA-P] |
| Dimensions / weight |W210×length105×H62mm;815g,mass basis unstated. | [Manual specifications][ANA-M] |
| I/O |6.35mm TS instrument;TRS SEND(stereo/mono insert);TRS RETURN(stereo/AUX/EXP);3.5mmTRS phones;2XLR+2unbalanced6.35TS outs;3.5TRS TypeA MIDIin/out;USB-C;DC. | [Manual][ANA-M] |
| Power / USB / battery |Product **9–12V center-negative≥1.7A**,9V adapter included;manual rear layout **9V2A**. Preserve rating/scope difference. USB-C PD **≥18W**;battery operation unverified. | [Product][ANA-P];[manual][ANA-M] |
| IR / NAM / captures |User cabinetIR,NAM,AIDA-X viaSuite desktop assets. NeuralAmp,NeuralPedal,NeuralLoader separate model-loading blocks. Exact native/converted architecture,size/format limits andinstance ceilings pending version-specific audit. | [Manual][ANA-M] |
| Synth / acoustic |KosmOS1.18 adds **Axioma monophonic synth**;license/bundle eligibility unverified. Acoustic simulation unverified. | [Product changelog][ANA-P] |
| Editor / USB |Darkglass Suite forupdates/library/assets;platform/minimumOS previously unknown; see versioned Suite findings below. ManualUSB AudioClass2,48kHzfixed,**3in/9out** asprinted;host/device channel direction mapping pending. USBMIDI. Bluetooth role/version pending. | [Product][ANA-P];[manual][ANA-M] |
| Looper / routing / live |Looper,tuner,parallel split/merge andscenes documented;recording duration,drums,trails restrictions unverified. | [Product][ANA-P];[manual][ANA-M] |

### Source versions and limits

[Official PDF][ANA-M] retrieved as97pages,title2026-10-12,cover **KosmOS1.17**. Read relevant introduction,layout,core concepts,loader andtechnical sections as text;not a complete97-page audit orvisual confirmation. [Current product][ANA-P] lists **KosmOS1.18.0** andAxioma;regional cached pages still1.17. Keep firmware distinctions rather than silently claiming every offer includes newest software/plugins. No firmware,software ormanual files downloaded orrun.

### Separate IDR hardware evidence

| Condition / access | Amount / qualification | Source |
|---|---|---|
| Used |Unknown;no condition-qualified ask. | — |
| New |Unknown;no condition-qualified ask. | — |
| Condition-unverified sold-out/preorder cached ask |**Rp20,350,000**,FireWorX Music Gear,Surabaya,shop72439811/item41315767273. Last-month search cache,**Habis** alongside30-day preorder andstale9–12Oct arrival. Clean exact URL failed toopen. Condition,working state,selected variant,firmware,plugin licenses,adapter/case,bundle,warranty,shipping/tax/voucher andcheckout total unknown. Rp10,000 latecompensation is not discount. | [Exact clean item](https://shopee.co.id/product/72439811/41315767273) |

Not live stock orcompleted sale. Original search URL carried advertising parameters;clean seller/item identity retained. Remaining:full model/category audit,NAM native/conversion constraints,editor platforms,hardware panel,firmware memory reconciliation andqualified used/new prices.

[ANA-P]: https://www.darkglass.com/products/anagram
[ANA-M]: https://api.darkglass.com/static/Anagram-Manual.pdf

### Anagram — versioned block-list census and NAM claims

Checked2026-10-18: [official online manual/block list](https://www.darkglass.com/pages/anagram-manual) now labels itself **v1.18.1**,while earlier indexed copy1.18.0 andPDF1.17 remain distinct. No firmware downloaded;list counts are a text audit,not installed-device verification.

| Field | Current evidence / qualification |
|---|---|
| Processing / category choices | List has **4 preamps,11 amps,22 bass cabinets,6 guitar cabinets,18 artist cabinets,12 drive/distortion,16 EQ/filter/dynamics,11 modulation/pitch,8 delay/reverb,13 utilities**. Sum **121 listed entries**,includingIR variants,loaders/system blocks andpotential licensed content. Not121 unique conventional algorithms orsimultaneous blocks;installed license/library census unresolved. |
| Processing / cabinet-list conflict | Bass-cabinet prose says6 microphones×6positions,butnames **7 microphones**(3condenser+4dynamic). Guitar section names6microphones×3positions. Do not silently collapse names orcalculate a definitive total IR library from the conflicting bass statement. |
| NAM / published concurrent claims | [Current exact product](https://www.darkglass.com/products/anagram) advertises **5 NAM A2 Full or9 A2 Lite**,running side byside,andstandard-size NAM/AIDA-X support. These are manufacturer performance claims,not all-model/mixed-chain benchmarks. Native execution versusconversion,architecture restrictions andactual DSP budget still require precise versioned documentation. |
| Looper / recording independence | Same exact product says loops continue across preset changes. This does not prove spillover forother effects orloop persistence afterpower-off;duration stillunverified. |
| Factory / user memory limits |1.18 changelog's126 user areas isnot yetreconciled with1.17's126preset capacity. Do not multiply them toinvent15,876presets. |

Full named block list remains linked rather than treated as guaranteed free factory content. Further work:memory areas,NAM architecture/limits,Suite platforms,plugin licensing,full manual/panel andqualified offers.

### Anagram — Suite compatibility and firmware limits

Checked 2026-10-18 against the [official Suite page](https://www.darkglass.com/products/darkglass-suite); no installers or firmware downloaded. Earlier versioned evidence above remains historical.

| Field | Evidence / qualification |
|---|---|
| Editor / desktop platforms | Suite **6.11.1** explicitly supports Anagram **1.18.0**. Windows heading says **Windows 10 & 11 (24H2 or later)**; the scope of that parenthesis is ambiguous. macOS **11 Big Sur+**, universal x64/arm64. Legacy Suite **1.3.6** lists other devices only, not Anagram. |
| Editor / mobile and driver separation | Suite mobile lists **iOS 15.6+ / Android 11+**, but product-dependent features mean Anagram mobile editing/asset parity remains unverified. Separate Windows USB audio driver **5.72.0**; driver availability is not editor compatibility. |
| NAM / firmware-dependent concurrency | KosmOS **1.18.1** removes the three-neural-loader-block limit and adds Blend/EQ Position to Tone3000 NAM loader. Removal does not imply unlimited DSP or settle native-versus-converted model architecture. |
| Factory / user memory area conflict | Suite changelog for **1.18.0 says up to127 user areas**; exact product page above says126. Preserve the unresolved conflict, not an assumed factory-area offset. Total preset capacity remains unverified. |

Next: version-specific NAM architecture/file constraints, licensing, full preset-area semantics, hardware panel and qualified used/new offers.

### Anagram — native NAM provenance and practical routing

Checked 2026-10-18. These are primary developer/manufacturer statements, not installed-device tests.

| Field | Evidence / qualification |
|---|---|
| NAM / native execution and architecture | [TONE3000 partnership announcement,2026-06-25](https://www.tone3000.com/blog/darkglass-anagram-nam-a2-full-natively) explicitly says **native NAM without conversion**. KosmOS **1.16** supports **A2-Full,A2-Lite andLegacy A1**, originally up tothree simultaneous instances. This establishes native playback,not onboard capture/training,all custom architectures orarbitrary file-size compatibility. Earlier native-versus-converted unknowns above are superseded within this documented scope. |
| NAM / TONE3000 block versus generic loaders | [Developer update,2026-08-11](https://www.tone3000.com/blog/darkglass-anagram-connects-directly-to-tone3000) assigns **KosmOS1.17** to TONE3000 integration: nofixed TONE3000 NAM-block limit,subject toDSP;developer tests **5 A2-Full /9 A2-Lite**,depending onother blocks. Do not equate this block-specific statement with generic neural-loader restrictions removed in1.18.1. |
| Editor / TONE3000 account workflow | Same August update: USB-C computer connection,Suite TONE3000 tab andaccount sign-in browse/load captures orpacks. Dedicated block offers NAM/IR filtering,favorites,model controls andsix-bandEQ;demo packs included withcreator permission. Account integration does not prove mobile parity,offline browsing orlicenses forall marketplace content. No captures downloaded here. |
| NAM / loader roles | [KosmOS1.17 PDF pp.77–79](https://api.darkglass.com/static/Anagram-Manual.pdf): Suite desktop transfers assets;Neural Amp adds four-bandEQ selectable before/after model,Neural Pedal adds dryblend,Neural Loader onlygain/model selection. Import classification Amps/Pedals/Miscellaneous chooses relevant loader. Allshare input/output gain andselector;cabinetIR loader hasselector,blend,level. |
| Looper / recording persistence | Same PDF pp.63–64: A play/stop,holdclear;B record/overdub,holdexit. Input/output chain position andplayback volume adjustable. Playback survives presetchanges,**RAM recordings lost onreboot**;exiting screen duringrecording stops recording. Duration remains unknown. |
| Routing / global EQ bypass | PDF pp.80–85: Output blocks selectOut1/2 or3/4 andbypass GlobalEQ whenplaced earlier;multipleoutputs allowed. Split supports fullrange orcrossover low/high rows;Merge blend/level. Send/Return independentlymono/stereo;return/loopblend andpolarity available. |

Remaining: precise file-size/rate/architecture compatibility matrix,1.18 area semantics,plugin licensing,visual hardware audit andcondition-qualified IDR asks.

### Anagram — Axioma tracking and Guitar Essentials edition boundary

Checked 2026-10-18; no plugin/manual files downloaded.

| Field | Evidence / qualification |
|---|---|
| Synth / Axioma architecture and templates | [Official nine-page Axioma manual](https://cdn.shopify.com/s/files/1/0735/5065/9813/files/Axioma_Manual.pdf?v=1789980649),read as text: **monophonic**,12 templates,two oscillators plus octave-down sub,dry/synth blend. Saw/square/triangle waveforms,oscillator coarse/fine tuning;filter cutoff,resonance,envelope/decay andattack/release. Templates are plugin starting sounds,not12 additional hardware preset locations. |
| Synth / Axioma tracking restrictions | Instrument modes:4-string bass,5-string bass,5/6-string,guitar,baritone/wide. **Does not track below open B of5-string bass**. Sensitivity controls detection,not output level. Manufacturer recommends first block andclean single-note playing;chords/double-stops are not tracked polyphonically. Guitar mode establishes this plugin’s intended input,not ordinary-offer entitlement toall Guitar Essentials content. |
| Synth / Axioma arpeggiator | Root-triggered diatonic arpeggiation:16th-note steps,Free/key selection;Major,Minor,Maj7,Min7,Minor-Major7;Up,Down,Up-Down,Random;1–3octaves. Newnotes restart pattern. This is synth arpeggiation,not documented drum accompaniment. |
| Processing / Guitar Essentials edition | [Official edition page](https://www.darkglass.com/en-int/pages/anagram-guitar-essentials) lists **12 amplifiers and3 drive pedals**,dedicated rendered interfaces;limited Sweetwater/Andertons edition,matte-black chassis/shiny-black knobs andleather case. This is a documented edition lead,not a newly counted Indonesian hardware model orproof the ordinary cached offer includes these plugins/case. |
| Editor / licensing evidence gap | Official edition links [Anagram Marketplace](https://marketplace.anagram.shop/),but browser text response was empty. Edition page establishes bundled premium guitar content;ordinary-device purchase eligibility,price,activation,transfer andused-device license retention remain unverified. Open-source component notices are not marketplace entitlement evidence. |

Next research: return toexact Shopee discovery,prioritizing an identifiable Guitar Essentials offer oranother eligible missing model. Retain unresolved file-format,area-capacity,license andpanel fields forAnagram rather than repeating unchanged searches.

### Anagram — electrical limits, latency and MIDI switching

Checked 2026-10-18 against the [KosmOS 1.17 manufacturer PDF][ANA-M], PDF pp.92–95. Text inspection; these are published specifications, not measurements of a unit.

| Field | Version-qualified evidence / boundary |
|---|---|
| I/O / analog levels and impedances | Instrument and Return: **1 MΩ, +12 dBu maximum input**. Send: **100 Ω, +12 dBu maximum output**. XLR outputs: **100 Ω, +2.2 dBu maximum**; unbalanced quarter-inch outputs: **100 Ω, +12 dBu maximum**. These different output limits are not a shared headroom rating. |
| I/O / headphones | **Less than 1 Ω** output impedance and three gain stages. Maximum headphone power/load rating remains unverified. |
| Routing / published latency | Instrument-to-any-output empty chain: **1.31 ms**; with FX Loop or Return block present: **2.62 ms**. Manufacturer cites Audio Precision APx515 DUT Delay measurement. These are not arbitrary loaded-chain or USB round-trip figures. |
| MIDI / toggle logic | Value mode: CC0–63 sets a binding off, 64–127 on. Toggle mode: any nonzero value toggles. Applies to stomp foot bindings and knob-bound toggle/bypass parameters. |
| MIDI / redundant program changes | Ignore Redundant PC on leaves the active preset untouched; off reloads its saved state. MIDI channel can be Omni. This does not resolve 1.18 multi-area addressing or capacity. |


### Anagram — global mixer, input slots and persistence limits

Checked 2026-10-18. [KosmOS 1.17 PDF][ANA-M], PDF pp.61, 66–68, 73–76; later firmware fixes are separately qualified below. Text inspection only.

| Field | Finding / boundary |
|---|---|
| Routing / mixer and mute | Six controls address Out3, Out4, XLR Out1, XLR Out2, headphones and Master. Each of the first five can be linked to Master; **Master Mute silences linked outputs only**. XLR and line pairs have separate stereo-link controls. Output levels persist across presets. |
| I/O / input-gain memories | **Six named instrument slots**, each storing input gain; **−12 to +12 dB**. Settings persist across presets and reboot. These are input setup memories, not six additional effects presets. |
| I/O / gain domain | Positive input gain is analog and can increase clipping with hot instruments; negative gain is digital. Do not assume a digital reduction adds analog input headroom. |
| Live / tuner and tempo | Reference **420–460 Hz**, default440; tempo **40–300 BPM**, default120. Tempo-synced delays follow global tempo; this does not establish external MIDI-clock behavior. |
| Firmware / mixer persistence | [Official Suite changelog](https://www.darkglass.com/products/darkglass-suite), KosmOS **1.18.1**, fixes mixer/global-EQ values not persisting after numpad entry. It also fixes saving to the wrong preset area and retains the chosen user area when trying Suite presets. Manual persistence statements therefore require firmware/method qualification. No update performed. |

USB direction remains unresolved: the 1.17 PDF labels 12 channels as 3in/9out without a complete readable host-direction routing table. Do not borrow Exponent 500 or ADAM channel assignments. The product/Suite 126-versus127 user-area conflict remains open.
