# Neural DSP multi-effects

<!-- brand-index begins -->
**Model and section index — A–Z, natural numeric order**

- [Incoming capability evidence, 2026-10-18](#incoming-capability-evidence-2026-10-18)
- [Nano Cortex](#nano-cortex)
- [Quad Cortex](#quad-cortex)
<!-- brand-index ends -->

## Incoming capability evidence, 2026-10-18

Preserved from origin/main87c7d38. References to older inventory counts or incomplete consolidation describe that branch checkpoint; current root profiles and ledger take precedence. Technical conflicts remain qualified.


[Expression-volume comparison](EXPRESSION-VOLUME.md) · [Guitar inventory](ALL-GUITAR.md)

### Nano Cortex — incoming capability supplement

**Expression-volume capability supplement, checked 2026-10-18 against the official NanOS 2.2.0 HTML manual.** Nano Cortex already exists in the catalogue: this is not a new inventory item. Its earlier full technical record remains in [advanced modelers](effects/advanced-modelers.md); no legacy content is deleted or represented as fully consolidated.

| Capability field | Verified finding / explicit uncertainty |
|---|---|
| Built-in expression | No treadle; the complete Overview shows external control rather than a built-in pedal. |
| External analog EXP | Yes, shared EXP/MIDI input. In app Settings, select EXPRESSION PEDAL; use a compatible TRS controller and calibrate heel/toe. The manual explicitly distinguishes a TRS expression output from audio wah/volume outputs, which are not supported. |
| Volume-related target | Expression Parameter Range section lists GAIN, BASS, MID, TREBLE, AMOUNT and **LEVEL**. The Global Controls section separately identifies the LEVEL knob as main-output master volume; the headphone level has a separate rear control. These statements establish a documented level-control lead, not an all-output/all-preset guarantee. |
| Assignment scope | **UNVERIFIED global assignment.** The inspected Expression Pedal Configuration section explains assignments and calibration persistence but does not explicitly establish a single level assignment applying to every preset without individual setup. Do not turn global calibration or the section title Global Controls into proof of global mapping. |
| Headphone behavior | Dedicated HP output is documented. Whether expression-mapped LEVEL controls HP level as well as main outputs is **unverified**; separate HP OUT knob is documented. |
| Size / weight | **144 × 103 × 62 mm; 620 g**. Chassis fits 200 × 140 mm; connected plugs add clearance. |
| Normal guitar pickup | Yes, normal instrument INPUT; no divided pickup required. |
| Preset switching | Manual describes 2-Preset and 4-Preset operation. Do not automatically describe its default two-switch behavior as unrestricted preset-down/up. |
| Power relevant to compact use | **9–12 V DC, center-negative, at least 600 mA**, or **USB-C 5 V / 1.5 A**. These are manufacturer supply requirements, not measured consumption. |
| Research verdict | **Not a confirmed buy for global pedal volume.** Direct EXP and a level target are documented, but cross-preset assignment persistence, exact target behavior and headphone coverage require model/firmware-specific confirmation. |

### Sources

[Official Nano Cortex User Manual 2.2.0](https://neuraldsp.com/manual/nano-cortex): Overview; Connecting your Gear; Global Controls; Performance Mode; Expression Pedal Configuration; Device Settings; Hardware Specifications. This is an accessible manufacturer HTML manual, not an inferred feature from forum complaints or a retailer.

### Remaining tasks

Verify on NanOS 2.2.0 whether LEVEL in the expression target list refers to final main-output gain, establish assignment storage scope explicitly, test changing at least three presets with the pedal held at heel/middle/toe, and separately verify HP behavior. No hands-on test is claimed. Refresh exact Shopee hardware offers, separate used/new IDR, condition and stock. Existing broader specification/price gaps in the legacy record remain unresolved.

### Nano Cortex — lock and bypass distinctions

Checked2026-10-19 against [official NanOS2.2.0 manual](https://neuraldsp.com/manual/nano-cortex), Parameter Lock and Expression Pedal Configuration. **Parameter Lock disables physical rotary operation temporarily**; it does not document locking an expression assignment across presets. Calibration persists until recalibration; assignment persistence remains unspecified in these sections.

Expression **slot bypass** is a separate assignment: SWITCH uses toe switching, STOP bypasses after stillness, HEEL-TOE bypasses at heel with delay up to2000ms. These describe Capture/IR/effect-slot states, **not whether expression LEVEL attenuates audio when slots are bypassed**. LEVEL range is adjustable/reversible0–100%; no final-output mute, headphone coverage orcross-preset guarantee follows from that normalized range. Prior official target-list discrepancy remains unresolved. No downloads orhardware test.

### Nano Cortex — trails and physical LEVEL boundary

Checked2026-10-19 in [ownNanOS2.2.0 manual](https://neuraldsp.com/manual/nano-cortex),Device Settings/Global Controls/Expression Pedal Configuration. **Trails enables delay/reverb decay ondevice bypass,but hasnoeffect in4-Preset Mode**. This isnotproof expressionLEVEL attenuates tails orpersists acrosspresets. PhysicalLEVEL islabelled masterforOUTPUT1L/2R;HP OUT separatelycontrols headphones. Latching behavior described forphysicalLEVEL inCaptureVolume/InputGate context isnotexpressionheld-position recall. TRS expression output required;audioWah/Volume outputs unsupported. Linear/logarithmic curves accepted aftercalibration;optionalrange/polaritycontrols supported. Resistance/pinout compatibility foractualM-VAVE controller remainsunverified. Globalassignment,headphoneattenuation andbypassLEVELcoverage remainunknown;no hardwaretest ordownloads.

### Nano Cortex — three distinct volume references

Checked 2026-10-19. [Official device list](https://neuraldsp.com/nano-cortex-device-list) lists **Volume** as a utility added in NanOS2.0.0, available in **any pre-effects slot**. It consumes a selectable slot; it is not documented as a fixed final-output volume block. Its presence does not establish global insertion or assignment across presets. Do not conflate this utility with LEVEL or Neural Capture Volume.

The [NanOS2.2.0 manual](https://neuraldsp.com/manual/nano-cortex), Capture Volume & Input Gate and Capture Library Workflow, gives **Capture Volume −24dB to+12dB, default0dB**, located at the capture’s output. The physical LEVEL knob edits that parameter only in the stated mode; app capture-volume controls refer to the active capture slot. These decibel endpoints are not the normalized expression0–100% range and do not promise heel-down silence. Existing LEVEL target-list conflict, global assignment, headphone/bypass/tail coverage and held-pedal recall remain unresolved. No software or hardware operation.

## Nano Cortex

Complete original model fields consolidated and partially refreshed **2026-10-17**. Standard Nano Cortex; no Quad Cortex specifications substituted.

### Preserved historical evidence

Checked **2026-10-14**. **Partial records**: `?` means unverified, not No. Native NAM, architecture-limited NAM, converted NAM, proprietary captures and cabinet IRs are different capabilities. An effects-only unit is not necessarily an amp modeler.

K/F/B = rotary controls / footswitches / separate buttons. Push-encoders are counted once. Nano Cortex's rotary footswitches are explicitly called out rather than hidden in the knob count. Dimensions are **W×D×H, mm**. Prices are separate **USD** new and used observations; missing used prices have not been invented.

USB audio input/output counts use the manufacturer's interface convention. A capture microphone connector does not establish a dedicated live vocal-effects path. Do not connect an amplifier's speaker output directly to an instrument/capture input; the appropriate load/interface is required.

- [Nano Cortex current product page](https://neuraldsp.com/nano-cortex); manual sections Hardware Specifications, Effects, Capture Mode, Presets Library, USB Channels and Expression Pedal Configuration.

- **External expression** (No built-in expression pedal): **One shared EXP/MIDI input**
- **K/F/B** (No built-in expression pedal): **7 knobs +2 rotary footswitch encoders /2 FS /5 buttons**; 2 analog switches additional
- **W×D×H; weight** (No built-in expression pedal): **144×103×62**, 620 g
- **Size class** (No built-in expression pedal): Compact
- **Used USD** (No built-in expression pedal): ?
- **New USD observation** (No built-in expression pedal): ?
- **Simultaneous processing / available choices** (Processing, presets, IR and capture formats): **5 FX slots + Neural Capture + IR**, plus input-gate functionality; **50+ effects/utilities** with NanOS 2; per-category counts pending
- **Preset storage** (Processing, presets, IR and capture formats): **64 presets**, four directly assigned hardware quick-access positions; **25 factory +256 user captures** are separate storage
- **Synth / acoustic functions** (Processing, presets, IR and capture formats): Specific synth/acoustic algorithms ?
- **Third-party IR** (Processing, presets, IR and capture formats): **256 user IRs**, 10 factory IRs; five hardware quick-access IR slots
- **NAM / proprietary capture** (Processing, presets, IR and capture formats): **Proprietary Neural Capture**, including onboard capture; NAM compatibility not established
- **Audio/control ports** (Connections, power, software and live use): ¼″ instrument in; XLR/¼″ combo capture in; 2×¼″ balanced out; 3.5 mm phones; shared ¼″ TRS EXP/MIDI Type A; USB-C; DC; remaining capture-routing connector detail pending
- **Power; battery/USB-powered?** (Connections, power, software and live use): **9–12 V centre-negative ≥600 mA OR USB-C 5 V/1.5 A**; no internal battery established
- **Configuration apps and USB functions** (Connections, power, software and live use): **Cortex Cloud iOS/Android** via Bluetooth; desktop full editor not established; USB audio **4-in/3-out**, fixed 48 kHz; Windows driver /macOS class-compliant
- **Other important differences** (Connections, power, software and live use): Onboard capture; **no phantom power for condenser capture mic**; ordinary USB-A power is insufficient for full operation

Retained original source URLs: https://neuraldsp.com/manual/nano-cortex, https://neuraldsp.com/nano-cortex

The [complete original comparison](MULTI-EFFECTS.md)<!-- historical-link:neural-dsp-001 --> remains available; no source or incoming link removed.

### Current comparison fields

| Field | Evidence and qualification |
|---|---|
| Expression | No built-in pedal; one external EXP/MIDI Type A socket, mutually exclusive modes. Toe behavior unverified. [M] |
| K/F/B | 7 knobs **plus2 rotary footswitch encoders /2 footswitches /5 digital buttons**; two analog switches additional. [M] |
| W×D×H; weight | **144×103×62mm;620g**. [M] |
| Size class | Compact. |
| Blocks / category choices | **Five effects slots**, two pre/three post, plus capture/IR and separate input gate. Slots have placement restrictions; not54 simultaneous effects. [M,D] |
| Preset storage | **64 presets**, four hardware assignments. [M] Capture storage separate: **25 factory plus up to256 additional**; cloud library is not internal memory. [P] |
| Synth / acoustic functions | Transpose documented; exact synth/acoustic simulation algorithms unverified. [D] |
| Third-party IR | **256 user IRs**. Product specifies **10 cabinet models ×30 mic/position variations =300 factory IRs**; older source/manual calls these10 factory IRs. Retain terminology difference; five quick-access slots are not total library capacity. [P,M] |
| NAM / proprietary capture | **Proprietary Neural Capture**, onboard V1 creation; NanOS2.2.0 adds **V2 playback**. That release explicitly restricts V2 creation to Quad Cortex and describes Nano creation as future development; not an available Nano feature. Native/converted NAM compatibility unverified. [R] |
| Audio/control ports | ¼-inch instrument in; XLR/¼-inch combo capture in; two balanced ¼-inch outs; 3.5mm phones; shared TRS EXP/MIDI Type A; USB-C; DC. **Output2R doubles as capture send**,1L monitors; no separate capture-out jack. [M] |
| Power / battery / USB | **9–12V DC≥600mA,center-negative,2.1/5.5mm**, or **USB-C5V/1.5A**. USB-A supports data but insufficient operating power. Internal battery unverified; external USB battery-pack support is not an internal battery. [M,P] |
| Configuration apps and USB functions | **Cortex Cloud iOS/Android**, Bluetooth editing/update workflow. Desktop full editor unverified. **USB4-in/3-out,24-bit/48kHz**; Windows driver, macOS class-compliant. [M] |
| Display | LED interface; published graphical-screen diagonal, color technology and touch specifications unverified. |
| Other relevant features | Tuner. Capture mic connector does not prove live vocal processing. Preserved no-phantom assertion is not independently reverified here. [M] NanOS2.2 adds Tremolo, optional mono summing, offline app mode, five cloud backups and capture auditioning. [R] Looper, drums, scenes and parallel routing remain unverified. |
| Used IDR | ? — no dependable condition-qualified used offer established. |
| New / retail IDR | **Rp11.900.000,Habis**: [Seven Stereo Music & Audio Store exact hardware](https://shopee.co.id/Neural-DSP-Nano-Cortex-Digital-Effects-Processor-i.16879370.51902266280),shop16879370/item51902266280,Kota Bandung; indexed reopening checked2026-10-17. Historical retail ask, not checkout-confirmed stock or completed sale. Condition grade, warranty region, accessory bundle, shipping/tax and voucher eligibility unverified. |

### Category counts and firmware qualifications

[D] [Official device list](https://neuraldsp.com/nano-cortex-device-list), checked2026-10-17: counting named rows gives **54 effects/utilities including the fixed input gate**, or53 slot-selectable entries. Mono/stereo compressor variants count separately. Capture/cabinet rows are excluded from that sum. Category counts: **9 guitar drives,2 bass drives,6 delays,6 reverbs,8 compressors (4 mono/4 stereo),1 pitch,8 modulation,2 filters,3 EQ,4 wah,5 utilities**. Utilities include the fixed input gate. Placement: drives/wah/filter and mono compression any pre; stereo compression any post; pitch pre1; modulation/doubler post1; delay post2; reverb post3; EQ any pre/post. Other utility entries occupy pre slots. Factory capture rows comprise20 guitar amps,4 bass amps and1 bass drive; cabinet list contains8 guitar and2 bass types. These counts are derived from the published rows, not an additional manufacturer headline or simultaneous-block count.

[P] [Official product page](https://neuraldsp.com/nano-cortex), checked2026-10-17, explicitly supports **guitar and bass**. This is the basis for shared bass membership, corroborated by the model-specific bass library; not a sibling-model inference. The page's50+ headline and NanOS2.0 effects list predate the Tremolo row added in2.2. No new unique model is created by adding bass membership.

[M] [Official HTML manual for NanOS2.2.0](https://neuraldsp.com/manual/nano-cortex), checked2026-10-17. Model-specific hardware, power, routing, control and USB sections reviewed; no downloaded manual or executable was used. The complete original15 fields, uncertainty and historical dates remain above. Capture a speaker-level amplifier only through the appropriate load/interface, as the original source warns.

[R] [NanOS2.2.0 release,2025-11-26](https://neuraldsp.com/nano-cortex-updates/nanos-2-2-0-is-now-available): V2 player versus creation distinction applies to that documented release. Its669 downloadable V2 captures across41 device types are cloud content, not factory on-device capacity. [NanOS2.2.1 hotfix,2025-12-10](https://neuraldsp.com/nano-cortex-updates/nanos-2-2-1-is-now-available) fixes a boot failure with an expression or MIDI pedal connected. This later hotfix supersedes any claim that2.2.0 alone is the newest checked release; no complete future-release audit is claimed.

### Remaining verification

External toe-switch behavior, precise live-vocal/capture-mic limitations, internal battery, published graphical-screen attributes, native/converted NAM, synth/acoustic algorithms and looper/drum/scene support remain open. Source absence is not proof of absence. Price condition, regional warranty, accessories, discounts and current availability require direct seller/checkout confirmation. All model records remain partial.

### Nano Cortex — global expression-volume audit, 2026-10-19

[Manual 2.2.0](https://neuraldsp.com/manual/nano-cortex) lists LEVEL as an expression target, 0–100% adjustable/reversible range, persistent calibration and a shared TRS EXP/MIDI socket. **Across-preset assignment scope is not established.** LEVEL controls main outputs; headphones have a separate knob. Onboard switches recall assigned A/B pairs, not documented general previous/next browsing. Expression attenuation during bypass, headphones, tails or looper use remains unknown.

[Official setup article](https://neuraldsp.com/getting-started/using-midi-on-nano-cortex) lists GAIN/BASS/MID/TREBLE/AMOUNT but omits LEVEL. Preserve this documentation conflict; do not substitute Capture Volume or calibration for global output assignment. See [audit comparison](EXPRESSION-VOLUME.md). Existing dimensions, offers and revision qualifications remain above; no download or hardware test.

### Nano Cortex — toe switches and control boundaries, rechecked 2026-10-22

[Official NanOS 2.2.0 manual](https://neuraldsp.com/manual/nano-cortex), Expression Pedal Configuration and Incoming MIDI CC List:

| Field | Evidence / qualification |
|---|---|
| External expression / toe switches | **Latching and momentary supported; momentary requires Latching Emulation.** Slot bypass offers toe-switch, stationary-pedal and heel/toe modes; delay reaches 2000 ms. This resolves the earlier toe-support gap for documented compatible pedals. |
| External expression / MIDI distinction | **CC1 conveys pedal position**, 0 heel/127 toe; it is not an independent globally assigned volume controller. Analog EXP and TRS MIDI remain alternative socket modes. |
| External expression / unresolved volume scope | LEVEL still appears in the manual target list but not the setup article. Preset-wide assignment, headphone attenuation and bypass/tail coverage remain unverified. Knob Parameter Lock only prevents accidental rotary adjustment; it is not volume-assignment persistence. |

Manual and [setup article](https://neuraldsp.com/getting-started/using-midi-on-nano-cortex) rechecked; preserve their disagreement and the separate capture-volume/main-output/headphone paths. No hardware operation or local downloads.

## Quad Cortex

Partial record checked **2026-10-17**. Full Quad Cortex,distinct from Nano Cortex andQuad Cortex mini. Product page advertises CorOS4.1.0;current web manual identifies4.1.1. Seller firmware unverified.

| Required field | Evidence / qualification |
|---|---|
| Built-in / external / toe expression | **Two external expression inputs** [qc-p]. Manual4.1.1 supports TRS sweep pedals anddualTRS sweep/toe outputs;latching toe supported,momentary requires Latch Emulation. Wah/volume audio outputs unsupported. Global calibration persists;expression-assigned values excluded fromScene data. Built-in pedal unverified [qc-m]. |
| Knobs / footswitches / buttons | **12 rotary /11 footswitches /1 power button**,derived:11 combined stomp/rotary actuators plusMaster Volume;A–H,BankUp, BankDown,Tempo. Hardware table confirms one capacitive power button;power separate from footswitches;encoder presses counted once [qc-p] [qc-m]. |
| Display | **7-inch multitouch** [qc-m];published color specification not yet checked. |
| Dimensions / weight | **290×195×69 mm;1.95kg**,manufacturer dimensions;axis labels not explicit in retrieved prose [qc-p]. |
| Simultaneous blocks / category choices | Manufacturer demonstrates four amp models plus stereo reverbs andother effects;not a universal maximum. Headline90+amps,100+effects,1000+IRs;exact category census unresolved [qc-p]. Manual4.1.1: **4rows×8slots=32 grid slots**,subject to CPU availability;not32arbitrary simultaneous algorithms. Bypassing blocks does not reduce CPU;GlobalEQ/InputGate automatically disable when resources exceeded. Maximum2side-chain devices per row pair [qc-m]. |
| Processing / inspected category choices | Official current device-list named rows: **GuitarAmps83,BassAmps13,GuitarCabinets62,BassCabinets8,GuitarOverdrive24,BassOverdrive5,Delay12,Reverb18,Compressor15;Pitch10,Modulation23,Morph6,Filter4,EQ6,IRLoader8,Wah7,Looper1,Synth1,Utility12**. Counts include separately named mono/stereo/Lite/side-chain variants;not simultaneous limits orunique underlying algorithms. Counts are source-table entries,including amp channels/modes,not distinct physical amps,cabIR files orfactoryRig occupancy. Capture andlicenced-plugin totals still unaudited. Separate Plugin devices table explicitly requires corresponding licences;not included in these standard counts. Current list includes4.1.0 additions;not seller firmware proof [qc-d]. |
| Preset / factory / user memory | Manual4.1.1: **256 full presets per setlist**;Factory/MyPresets setlists cannot be deleted. Setlist maximum,combined capacity andfactory occupancy unresolved. SceneA–H recall anddesktop shortcuts1–8 document **eight Scene selections** [qc-m]. Separate libraries: **2048 user captures alongside factory captures,and2048IRs**,each up to30folders/four nesting levels;folder links do not duplicate storage. Compatible virtual devices,GlobalEQ andI/O settings each support **32 user parameter presets**,not32full signal chains [qc-m]. |
| Synth / acoustic | Manual4.1.1 explicitly includes **SYNTH waveform-generation devices**. [qc-m]. Official device list has **one standard Synth entry:Mono Synth**,free enhanced Overlord-derived engine,addedCorOS3.3.0. Separate Pitch category includes Subharmonic Synth;category placement is retained. Electric-to-acoustic simulation unresolved [qc-d]. |
| Audio I/O | Two TS/TRS/XLR combo inputs with mic preamps/phantom;dual FX loops;two balancedTRS andtwo balancedXLR outs;headphones;capture out. [qc-p]. Manual4.1.1:returns2×¼-inchTRS,1Mohm;sends2×¼-inchTRS ground-cancelling,560ohm,+9.5dBu;phones¼-inchTRS,300mW(load unspecified). InputXLR9.4kohm/TS10kohm–10Mohm,+60dBmaxgain. MainXLR560ohm,+9.5dBu. **Connector discrepancy:** headingTRS OUT3/4 butconnector printsTS-F;balanced+15.5/unbalanced+9.5dBu,560ohm. Retained,not silently corrected. Capture-out format unresolved [qc-m]. |
| Control / USB | MIDI in,out/thru;dualEXP;USB audio/MIDI/updates. [qc-p]. Manual4.1.1 confirms **8in/8out USB audio**;**USB Audio Class2.0,fixed48kHz**;MIDI5-pinDINin/out. USB power andcomplete socket census unresolved [qc-m]. |
| Power / battery / USB operation | **12V DC,≥3A,centre-negative**,supplied adapter;not measured consumption. Battery/USB operation andbarrel dimensions unresolved [qc-m]. |
| IR / NAM / captures | Proprietary Neural Capture:V1 runs offline ondevice;V2 uses Cortex Cloud processing. User IR transfer via cloud documented [qc-p]. Manual4.1.1:compatible **WAV uploads resized to1024samples,approximately21ms** through CortexCloud,regardless oforiginal length. CortexControl supports WAV drag/drop intoIR library. Accepted sample-rate/bit-depth limits andnative/converted NAM unresolved [qc-m]. |
| IR / captures — V2 workflow | Manual4.1.1: V2 creation requires CortexControl login,connected hardware andcloud training;Windows needs latestpublic audio driver,microphone permission may be requested. Captures autosave privately tocloud. **40sessions/user/day**,typically10min each;not guaranteed timing. Compressor captures withaggressive threshold/long release may differ fromhardware [qc-m]. |
| Processing / plugin licences | Manual4.1.1: compatible paidplugin devices require perpetual licences verified viaNeuralDSP/linked iLok account;14-daytrials do notqualify. One-time online validation allows offlineuse afterward;changing account canchange availability. Limit3QuadCortex plus3mini devices peraccount;fourthQuadCortex bypasses lockedplugin blocks. A usedhardware offer doesnot establish licence ownership/transfer [qc-m]. |
| Editor platforms / drivers | Cortex Control desktop editor documented;Cortex Mobile iOS/Android cloud discovery distinct from fulldevice editor. [qc-p]. Manual4.1.1 Cortex Control requires USB-connected hardware,no standalone processing;**macOS13+**,Intel i5fourth-gen+/AppleM1+;**Windows10+**,i5fourth-gen+,latest QuadCortexASIO driver. Both8GBRAM,100MBstorage. Host minima are editor requirements,not firmware installation proof [qc-m]. |
| Practical features | Preset,Scene,Stomp,Hybrid modes andmetronome documented [qc-m]. **Looper X** is a Grid block with optionalglobal I/O routing;A–H action mapping andMIDI CC control. Record/overdub,punch-in,duplicate/re-loop,one-shot,half-speed,reverse,undo/redo. Toggle/momentary record/overdub/punch modes. Quantize totempo/externalMIDI clock;clock disables threshold autostart. Pre-roll1/2/4bars;fixed recording length1–32bars. Numericseconds maximum,export/power-off persistence,drums andswitching tails unresolved;bars are not a fixed-time specification [qc-m]. |
| Bass capability | Manufacturer explicitly identifies guitar andbass algorithms;not equal low-end performance certification [qc-p]. |

### Quad Cortex — separate IDR hardware offers

| Condition / access | Amount | Exact evidence / qualifications |
|---|---:|---|
| Condition-unverified indexed ask | **Rp38.500.000** | [Gelora Musik Serpong,seller306155985/item42028931563](https://shopee.co.id/Digital-Effects-Modeler-Gitar-Neural-DSP-Quad-Cortex-Quad-Core-i.306155985.42028931563),Kab.Tangerang. Direct indexed body checked2026-10-17,month-oldcrawl;August26–28delivery stale. Condition,stock,variation,bundle,adapter,warranty,authenticity,installedOS,shipping/tax/voucher/final total unknown. Rp10k late compensation notdiscount. Not live checkout orsale. |
| Condition unknown;Habis | **Rp30.899.999** historical clean-URL snapshot;**Rp30.999.999** later tracking-URL snapshot | [HAWILA MUSIK INDONESIA,seller130137603/item5704605568](https://shopee.co.id/Neural-DSP-Quad-Cortex-Quad-Core-Guitar-Digital-Effects-Modeler-Original-i.130137603.5704605568),KotaSurabaya. Search evidence checked2026-10-17:two-month versusone-monthcrawl,July23–25 versusSeptember9–11delivery,bothHabis. Snapshot difference does not prove current price movement. New/used,working state,bundle,variation,warranty andcheckout availability unresolved;no completed-sale claim. |
| Verified new IDR | ? | Not established. |
| Verified used IDR | ? | Not established. |

[qc-d]: https://neuraldsp.com/device-list
[qc-p]: https://neuraldsp.com/quad-cortex
[qc-m]: https://neuraldsp.com/manual/quad-cortex

No download orvisual inspection claimed;current web documentation does not prove seller firmware orlive stock.
