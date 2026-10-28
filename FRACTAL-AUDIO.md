# Fractal Audio — multi-effects

[Repository](README.md) · [Guitar comparison](ALL-GUITAR.md) · [Bass comparison](ALL-BASS.md)

<!-- brand-index begins -->
**Model and section index — A–Z, natural numeric order**

- [FM3 MKII Turbo](#fm3-mkii-turbo)
- [FM9 MKII Turbo](#fm9-mkii-turbo)
<!-- brand-index ends -->

## FM3 MKII Turbo

Partial record checked **2026-10-17**. Exact MKII Turbo hardware offers; original FM3 offers are not merged. Manufacturer's 7.x manual expressly covers both revisions; current firmware listing is newer. Unknown means unverified.

| Required field | Evidence / qualification |
|---|---|
| Manufacturer identity / revision | MKII Turbo launched July2023: over10% more DSP and larger footswitch displays than original; dimensions/mass unchanged. [Product](https://www.fractalaudio.com/fm3/) |
| Built-in / external / toe expression | No built-in pedal; two shared external pedal/switch jacks. External toe configuration unverified. [Product](https://www.fractalaudio.com/fm3/) |
| Knobs / footswitches / buttons | **8/3/12**; five push-knobs counted once. Rear power/ground-lift switches separate. Manual pp.21–24,140. |
| Display | **800×480 color LCD**, plus footswitch mini-LCDs. Diagonal/touch unverified. Manual p.140; larger Turbo switch displays do not establish color/touch. |
| Dimensions / weight | **281W×236D×103H mm;3.22kg**. Large. Manual p.140. |
| Power / battery / USB operation | **90–264VAC,47–63Hz,<40W**, grounded mains. CR2032 is backup memory battery, not operating battery. DC polarity/current not applicable to mains inlet; USB/battery operation unverified. Manual pp.24,140. |
| Simultaneous blocks / categories | CPU-limited; **12×4 grid is not guaranteed48 effects**. Exact usable block inventory/category choices unresolved. Manual pp.2,50. Current product lists300+ amp models; factory cabs2200+ and1024 user IR locations, not simultaneous blocks. [Product](https://www.fractalaudio.com/fm3/) |
| Preset / factory / user memory | **512 editable locations;8 scenes each**. Factory-filled subset unresolved. Manual pp.2,9,49. |
| Synth / acoustic functions | Acoustic instrument input documented; dedicated acoustic simulation and synth inventory unverified. Do not infer from generic multi-effects claims. |
| IR / NAM / captures | **1024 user cab IRs**, UltraRes/DynaCab; DynaCab introduced firmware7. Native NAM, converted NAM and user amp capture import unverified. [Product](https://www.fractalaudio.com/fm3/) |
| Audio / control ports | Mono¼-inch unbalanced instrument in; balanced stereo¼-inch Input2/return; balanced XLR stereo Out1; unbalanced Humbuster¼-inch stereo Out2;¼-inch stereo phones; two TRS pedal jacks; FASLINK II; MIDI IN/OUT; S/PDIF out48kHz; USB-B; unused USB-A; mains. Manual pp.23–24. |
| USB functions | **4×4 audio**, recording/reamping. **Not USB MIDI**: proprietary COMM for editor. Manual pp.24–25; [Product](https://www.fractalaudio.com/fm3/). Do not infer USB power. |
| Editor platforms / drivers | Free **FM3-Edit Mac/Windows** full editor. Listed1.07.17,2026-08-25:macOS10.13+,Windows10+64bit; Windows7 unsupported. Windows editor depends on USB audio+serial drivers. Android/iOS/Linux editor unverified. [Editor](https://www.fractalaudio.com/fm3-edit/) |
| Firmware / software revision | Downloads list **firmware13.0,2026-07-16**, compatible original/Turbo, requiring latest editor. Windows drivers listed2026-06-10:audio6.16/serial1.3; both needed. Factory presets2025-06-04 target10.00+. These listings do not verify installed firmware or every7.x manual feature against13.0. [Downloads](https://www.fractalaudio.com/fm3-downloads/) |
| Practical features | Looper,tuner,programmable tap/hold footswitches,eight layouts; FASLINK II supports up to two FC6/FC12 controllers. Loop durations/drum machine unresolved. [Product](https://www.fractalaudio.com/fm3/) |
| Bass capability | Manufacturer explicitly describes guitar/bass processing; shared bass model, not equal low-end performance certification. [Product](https://www.fractalaudio.com/fm3/) |

### Separate IDR asking-price evidence

| Condition / access | Amount | Exact seller / item and qualifications |
|---|---:|---|
| Condition-unverified indexed preorder | **Rp25.552.000** | [Hurtrock Music Store Bandung,seller11170212/item27200713719](https://shopee.co.id/Fractal-FM3-MKII-Turbo-Amp-Modeler-Multi-FX-i.11170212.27200713719). KotaBandung;three-month index says7day preorder/22July delivery;direct reader returns JavaScript shell. Checked2026-10-17;current stock,new/used,bundle,warranty,variant,voucher unverified. |
| Condition-unverified sold-out indexed ask | **Rp25.552.000** | [HurtrockMusicStore,seller182719800/item55801628505](https://shopee.co.id/Fractal-FM3-MKII-Turbo-Amp-Modeler-Multi-FX-i.182719800.55801628505). KotaBandung;three-month index says **Habis**. Separate seller/item,not independent confirmed stock or sale. |
| Verified new IDR | ? | Retail identity alone does not prove new condition. |
| Verified used IDR | ? | Not established. |

The Rp11.999 Pianeta preset and acrylic covers are not processor prices. Original FM3 seller1435419712/item29175380674 is not silently assigned Turbo specifications. No purchase/authenticity or live-stock verification.

### Sources and remaining work

- [Official FM3 Owner's Manual,7.x](https://www.fractalaudio.com/downloads/manuals/FM3/FM3-Owners-Manual.pdf), listed2023-07-12; cover explicitly includes standard and MKII Turbo. Printed page numbers above. Text read through web reader; no local download or new visual inspection.
- [Current product](https://www.fractalaudio.com/fm3/), [downloads](https://www.fractalaudio.com/fm3-downloads/), and [editor](https://www.fractalaudio.com/fm3-edit/) checked2026-10-17. Firmware packages and software were not downloaded or executed.

Remaining:per-category algorithms and concurrency, factory occupancy, display diagonal/touch, expression/toe details, synth/acoustic engines, IR format limits,NAM/capture status, looper/drums and current-condition Indonesian offers. This adds one partial model,not a verified-complete record.

### FM3 MKII Turbo — global expression-volume audit (2026-10-28)

[Official firmware7.x manual](https://www.fractalaudio.com/downloads/manuals/FM3/FM3-Owners-Manual.pdf), cover expressly includes MKII Turbo, printed pp12–13: **MIDI/Remote → Other → Input1/2 or Output1/2 Volume → PEDAL1/2 (EXP/SW TIP)** provides global volume without preset-by-preset assignment. Input control changes gain-dependent behavior; output control includes effect tails. This is separate from per-preset External Controller modifiers.

Linear10–100kΩ pedal, TRS: manual describes tip supply, ring return, sleeve ground. Calibration precedes assignment. Numeric volume endpoints and held-position recall remain unverified. Printed p108 distinguishes Volume Increment/Decrement: these save preset levels and are unsuitable for an expression sweep. Headphone/bypass/recorded-loop coverage remains unverified. Existing281W×236Dmm fails preferred fit. Onboard preset increment/decrement functions are documented separately from MIDI; default layout uses three preset choices with held bank previous/next. Firmware13 behavior not tested.

## FM9 MKII Turbo

Partial record checked **2026-10-17**. Exact MKII Turbo offer;original/MKI seller item remains separate. Current product/store establish revision. Linked2022 manual covers original/Turbo but predates MKII display revision;historical physical figures below require current corroboration.

| Required field | Evidence / qualification |
|---|---|
| Manufacturer identity / revision | Four DSP cores;**10+% extra processing over original**,larger switch displays with nearly double viewing area. [Product][f9-p]. |
| Built-in / external / toe expression | No built-in treadle;**three external pedal/switch sockets**. Toe configuration unresolved. [Product][f9-p];[Store][f9-s]. |
| Knobs / footswitches / buttons | Current:**nine footswitches**. Historical manual:**9/9/12**,six push-knobs counted once;power/ground lifts separate. Current MKII rotary/button totals need corroboration. [Product][f9-p];[Manual][f9-m] p.128. |
| Display | Color main display,nine enlarged mini displays. Historical main800×480;published diagonal/touch unverified. [Store][f9-s];[Manual][f9-m] p.128. |
| Dimensions / weight | Historical original/Turbo manual:**513W×237D×89H mm;5.44kg**,large. Exact MKII body/mass corroboration unresolved;do not borrow FM3 figures. [Manual][f9-m] p.128. |
| Simultaneous blocks / category choices | Two amp blocks,four channels each;**325+ amp choices**,57+drive,50+reverb current product headlines. CPU-dependent concurrency,complete category census unresolved.2022manual instead59+drive/60+reverb;retain revision/source conflict.14×6grid is not84 guaranteed effects. [Product][f9-p];[Manual][f9-m] p.2. |
| Preset / factory / user memory | **512 presets,8 scenes,four channels in most blocks**. Historical manual permits overwriting every location;factory-filled subset unknown. [Store][f9-s];[Manual][f9-m] p.39. |
| IR / NAM / captures | **2200+factory cabs,1024user IRs**,UltraRes/DynaCab.2022manual lists WAV/IR/SYX import and16scratchpads;current format/length limits unresolved. Native NAM,converted NAM,user amp capture import unverified. [Store][f9-s];[Manual][f9-m] p.2. |
| Synth / acoustic | Synth algorithms explicitly named;acoustic/piezo routing documented historically. Dedicated acoustic-simulation algorithm inventory unresolved;body IR enhancement differs. [Product][f9-p];[Manual][f9-m] p.38. |
| I/O | Instrument¼-inch input;two balanced stereo¼-inch input pairs;three stereo outputs:Out1 XLR+Humbuster¼-inch,Out2 XLR,Out3 Humbuster¼-inch;phones;three pedal jacks;FASLINKII;S/PDIFin/out48kHz. Manual addsUSB-B,MIDIDINin/out-thru,mains. Humbuster is not ordinary balanced output. [Product][f9-p];[Manual][f9-m] pp.21–22,128. |
| USB functions | **8×8audio plusUSB MIDI**,record/play/reamp;distinct from FM3 proprietaryCOMM-only MIDI limitation. USB audio does not prove USB power. [Product][f9-p];[Store][f9-s]. |
| Power / battery / USB operation | Historical manual:**90–264VAC,47–63Hz,<40W**;CR2032backs memory,not operating battery. Current MKII consumption confirmation unresolved. DCpolarity/current not applicable to mains inlet;USB/battery operation unverified. [Manual][f9-m] p.128. |
| Editor platforms / drivers | **FM9-Edit Mac/Windows**,full editor/librarian. Current1.03.22,2026-08-25;macOS10.13+Intel/M1,Windows10+64bit;Windows7unsupported. Mobile/Linux editor unresolved. [Editor][f9-e]. |
| Firmware / software revision | Downloads list**12.0,2026-07-07**,original/Turbo compatible;requires latest editor. WindowsUSBdriver6.16,2026-06-10,Windows10+x86/x64/ARM;older7/8need5.12. Factory presets9.02,2025-06-04,target9.x+. USBfirmware1.04separate hardware-revision update. Installed firmware unknown;manual remains3.x. [Downloads][f9-d]. |
| Practical features | Current product lists**two-minute looper**,eight tap/hold switch layouts,up to twoFC6/FC12controllers;store claims gapless switching,minimum firmware unresolved. Mono/stereo/speed looper duration qualifications anddrums remain unverified. [Product][f9-p];[Store][f9-s]. |
| Bass capability | Exact MKII Turbo store explicitly supports guitar/bass;shared bass,not inferred from amp controls. [Store][f9-s]. |

### FM9 MKII Turbo — separate IDR asking-price evidence

| Condition / access | Amount | Exact hardware offer / qualifications |
|---|---:|---|
| Condition-unverified indexed retail ask | **Rp44.395.000** | [Hurtrock Music Store Bandung,seller11170212/item25331147281](https://shopee.co.id/Fractal-FM9-MKII-Turbo-Amp-Modeler-Multi-FX-i.11170212.25331147281). KotaBandung;two-week search index exactMKII Turbo title;direct reader JavaScript shell. Checked2026-10-17;current stock,new/used,variant,bundle,warranty,voucher,authenticity andinstalled firmware unverified. Late-delivery compensation not an applied discount. |
| Verified new IDR | ? | Retail identity does not establish new condition. |
| Verified used IDR | ? | No qualified offer. |

Rp36m seller1354606623/item43322190869 titlesFM9MKI and has inconsistent oldFM3 URL slug;not a Turbo offer. Preset packs and accessories excluded.

[f9-p]: https://www.fractalaudio.com/fm9/
[f9-s]: https://shop.fractalaudio.com/products/fm9-mark-ii-turbo-amp-modeler-multi-fx-floor-unit
[f9-m]: https://www.fractalaudio.com/downloads/manuals/FM9/FM9-Owners-Manual.pdf
[f9-d]: https://www.fractalaudio.com/fm9-downloads/
[f9-e]: https://www.fractalaudio.com/fm9-edit/

Official sources read2026-10-17;manual2022-08,firmware3.x,original/Turbo cover. No file/software/firmware downloads or hardware operations. Remaining:MKIIphysical corroboration,category/concurrency census,display,IRlimits,NAM/captures,looper qualifications,drums,power-operation andqualified condition/stock evidence. One new partial record,not full verification.
