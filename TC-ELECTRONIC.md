# TC Electronic multi-effects

[Repository](README.md) · [Guitar](ALL-GUITAR.md) · [Vocal](ALL-VOCAL.md)

<!-- brand-index begins -->
**Model and section index — A–Z, natural numeric order**

- [M100](#m100)
- [M350](#m350)
- [M-One XL](#m-one-xl)
- [NOVA System](#nova-system)
- [PLETHORA X3](#plethora-x3)
- [PLETHORA X5](#plethora-x5)
<!-- brand-index ends -->

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


### M100 — current-guide MIDI control mappings

Checked 2026-10-18 from original manufacturer-indexed [QSG English MIDI Communication Guide,p70][M100-M]. The Chinese section p90 corroborates the mapping. Current-guide applicability to older M100 hardware remains unresolved; no MIDI messages or firmware were sent.

| Field | Revision-qualified behavior |
|---|---|
| Editor / MIDI channel setup | Hold BYPASS while turning EFFECT SELECTOR; selected effect number becomes the channel. Guide explicitly says no visual or audible confirmation. This is setup, not proof of a patch editor or persistent user-preset storage. |
| I/O / MIDI CC map | **CC102** bypass0/1; **CC103** effect0–15; **CC104** effect parameter0–127; **CC106** mix0dry–127wet. These map controls, not extra effect blocks or memories. |
| Live / MIDI tap and select | **CC105** is mode-dependent:tap values1–127 each supply one tap;select uses0Off/1On. Do not interpret the tap value as a BPM number or assume MIDI-clock sync. |

<!-- comparison evidence ends -->

Working state, authenticity, hardware revision, bundle, adapter, warranty, shipping/tax and voucher eligibility unresolved. Direct QSG open failed; indexed official text readable. No filesystem download or visual inspection claimed.

[M100-P]: https://www.tcelectronic.com/en/products/0828-AAH
[M100-M]: https://mediadl.musictribe.com/media/PLM/data/docs/P0CAH/QSG_TE_0828-AAH_M100_WW.pdf
[M100-O]: https://shopee.co.id/TC-Electronic-M100-Stereo-Multi-Effects-Processor-i.19576516.6955147985

### M100 — direct-expression capability screening

Checked 2026-10-28 against [manufacturer-indexed current QSG][M100-M], pp24–25. **FOOTSW is a quarter-inch TS bypass-switch input**, not a documented continuous expression input. Complete listed connections contain **no analog EXP or dedicated headphones**; MIDI DIN remains revision-qualified as above. **191W×99Dmm fits** the preferred rectangle, but not the direct analog-pedal requirement. No onboard preset down/up footswitches; EFFECTS is a hand selector.

Direct analog position/range/recall are inapplicable to the documented inventory. OUTPUT level differs from wet/dry MIX; current-guide CC106 is mix, not proof of global output-volume assignment. Bypass leaves the sound unaffected per the guide, but tail/looper attenuation remains unverified. Keep input-impedance/source conflict and older-hardware applicability open; no assumed passive-pickup match. Historical preorder/condition qualifications remain. No download or device test.

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


### M350 — preset confirmation and MIDI addressing

Checked 2026-10-18 from original text in the [manufacturer Rev1.1/SW1.00 manual, printed pp21–22](https://cdn.mediavalet.com/aunsw/musictribe/oexFf_5Xrkic0GfCn2XAEw/j6PZVTEe-UynlIA4ETJYOA/Original/tc_electronic_m350_manual_english.pdf). No device operation or download.

| Field | Evidence / qualification |
|---|---|
| Memory / recall and store | In Preset On mode, arrows select locations1–99; blinking digits indicate selection before recall. LOAD recalls; an empty location causes no action. Holding LOAD about2.5seconds stores into the selected user location. Selection is not automatic recall or proof of seamless transitions. |
| Live / panel versus stored state | Preset Off processes according to front-control positions. Returning to Preset On keeps that panel-derived sound until LOAD recalls the blinking stored preset. The mode name does not mean audio bypass; physical knob positions can differ from recalled settings. |
| I/O / MIDI channel and SysEx ID | Receive channel1–16, O for all channels, or OF to ignore incoming MIDI; factory/reset default ischannel1. SysEx ID follows the selected MIDI channel. LOAD confirms the menu choice. These addressing options do not establish editor operating-system support. |


### M350 — historical editor scope and algorithm limits

Checked 2026-10-18 through manufacturer-hosted original indexed text;no local download or software operation.

| Field | Evidence / qualification |
|---|---|
| Editor / dated feature provenance | [TC Summer2007 catalogue,p11](https://service-tcgroup.tcelectronic.com/media/Touring_Install_DE.pdf) describes a bundled VST editor with parameter/preset automation and realtime control;the [English cutsheet](https://service-tcgroup.tcelectronic.com/media/M350_Cutsheet_web.pdf) also lists AU. This dates the capability claim;recent indexing/upload labels are not new editor releases. Installer availability,OS versions,plugin bitness and current host compatibility remain unverified. |
| Looper / delay timing limits | Cutsheet advertises **5seconds of delay**. [Rev1.1 manual,printedp24](https://cdn.mediavalet.com/aunsw/musictribe/oexFf_5Xrkic0GfCn2XAEw/j6PZVTEe-UynlIA4ETJYOA/Original/tc_electronic_m350_manual_english.pdf) gives TIMING **0.5–2×** the tapped interval and power-up tempo120BPM;range depends on algorithm,with Slapback shorter. Do not assign5seconds to every delay type or confuse this with phrase-loop recording. |
| Processing / compressor controls | Manual pp25–26:TIMING becomes drive/threshold;FEEDBACK/DEPTH sets ratio. Attack is fixed and automatic makeup gain compensates level reduction. No adjustable attack time or numerical ratio range is established here. |


### M350 — routing-dependent mix and input-gain ranges

Checked 2026-10-18 from the [manufacturer Rev1.1/SW1.00 manual,printed pp16–17](https://cdn.mediavalet.com/aunsw/musictribe/oexFf_5Xrkic0GfCn2XAEw/j6PZVTEe-UynlIA4ETJYOA/Original/tc_electronic_m350_manual_english.pdf),original text only. The diagram screenshot attempt failed;no visual control count or hardware operation claimed.

| Field | Evidence / qualification |
|---|---|
| Routing / effect mix restrictions | In Serial routing,compressor/de-esser mix is fixed100%;chorus/flanger/phaser/tremolo mix is fixed50%. MIX adjusts delay/reverb,with BALANCE adjusting their relative contribution. In Dual S/R,MIX controls overall wet/dry for both engines. These routing-dependent rules do not establish arbitrary independent wet/dry control for every algorithm. |
| I/O / input-gain control | INPUT controls both L/R channels:analog gain spans **−10 to+14dB**,digital **−18 to+6dB**,each0dB at center. These are gain ranges,not maximum input levels or dBu nominal sensitivities;the electrical ratings remain separately documented. Unequal source levels require adjustment upstream rather than separate L/R gain knobs. |



### M350 — MIDI controller map and clock direction

Checked 2026-10-19 from the [Rev1.1/SW1.00 manufacturer manual, printed pp30–31](https://cdn.mediavalet.com/aunsw/musictribe/oexFf_5Xrkic0GfCn2XAEw/j6PZVTEe-UynlIA4ETJYOA/Original/tc_electronic_m350_manual_english.pdf). The [alternate manufacturer-hosted English index](https://mediadl.musictribe.com/download/software/tcelectronic/tc_electronic_m350_manual_english.pdf) separates Color CC20 from the following page number. Screenshot retrieval failed; this is original text evidence, with no device operation.

| Field | Evidence / qualification |
|---|---|
| I/O / MIDI general controls | **Input level CC12; Mix CC13; Effect Balance CC14; Digital Input CC15; Bypass CC81**. The chart describes single-byte controllers scaled to each parameter range; this does not supply switch-value polarity or numerical parameter endpoints. |
| Live / MIDI delay-effects controls | **Type CC50; engine Off CC82; Timing CC16; Tap CC80; Feedback CC17**. These control existing engine parameters, not extra simultaneous blocks. The CC number alone does not establish a BPM-valued payload. |
| Live / MIDI reverb controls | **Type CC51; engine Off CC83; PreDelay CC18; Decay CC19; Color CC20**. These are MIDI mappings, not proof of analog expression-pedal support or editor OS compatibility. |
| I/O / MIDI clock and message scope | April2006 implementation chart lists CC, Program Change and SysEx transmission/reception. **Clock received, not transmitted**; MIDI TimeClock sets delay tempo. Note messages, velocity, aftertouch and pitch bend are not implemented in either direction; this is a MIDI-message scope statement, not a verdict on audio algorithms. |

### M350 — additional indexed preorder hardware ask

| Field | Dated asking evidence / limitations |
|---|---|
| Price / condition-unverified IDR | **Rp6.898.094**, CHdada, Kota Jakarta Pusat; seller1003926059/item20383192872. Checked2026-10-19: two-month indexed exact-item body shows **Pre-Order, dispatched within15days**, with stale13–21August arrival. [Seller-labelled TC-M350 processor](https://shopee.co.id/%E2%9C%85-TC-M350-vocal-reverb-effect-dual-engine-digital-effect-processor-%EF%BC%8Cprofessional-stage-performance-effect-karaoke-i.1003926059.20383192872). Direct page returned cache miss. Condition, selected variant, original-brand authenticity, working state, bundle, warranty, voucher, shipping/tax and checkout stock remain unverified. Rp10.000 late-delivery compensation is not a purchase discount. Historical asking evidence, not current availability or a completed sale; it establishes neither verified new nor used price. |

### M350 — direct-expression capability screening

Checked 2026-10-28 against the [own Rev1.1/SW1.00 manufacturer manual](https://cdn.mediavalet.com/aunsw/musictribe/oexFf_5Xrkic0GfCn2XAEw/j6PZVTEe-UynlIA4ETJYOA/Original/tc_electronic_m350_manual_english.pdf), rear panel p8 and front overview pp6–7. **No continuous analog EXP input**: quarter-inch TRS pedal socket explicitly uses **momentary bypass on tip, tap on ring**. Complete connector inventory has **no dedicated headphones**. **483W×105.6Dmm** exceeds width preference; guitar needs upstream preamp. No onboard preset footswitch pair: arrows select presets, LOAD recalls, all hand controls.

Direct-expression position/range/recall are inapplicable to the documented input. Global tap tempo and bypass are not global volume assignment. Preserve Serial dry-pass versus Dual Input mute, and routing-dependent MIX rules; MIDI input-level/mix controls do not prove analog expression or tail/looper attenuation. Historical preorder/variant offers remain qualified. No download, hardware operation or model admission.

## M-One XL

Checked 2026-10-17; partial. [Original English manual, mirrored][M1XL-M], Rev4, product E60500152: SW2.07 XL versus1.43 Standard. Manufacturer download inaccessible; mirror adds watermarks. Text-only review.

| Field | Evidence / gaps |
|---|---|
| Expression | No integrated treadle. Quarter-inch pedal input explicitly accepts **momentary switches only**: bypass1,2,both or tap; continuous expression is unsupported through this jack. Built-in toe switch absent with treadle;external toe-switch accessory compatibility unverified. [Own manual p12](https://www.liveline.be/wa_files/tc_electronic_m-one_xl_manual_english.pdf). |
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

### M-One XL — manufacturer-hosted electrical specifications

Checked2026-10-18 from indexed manufacturer Spanish manual,p40,explicit **M-One XL** table. English file retrieval failed;this is not a full manual orvisual inspection.

| Field | Exact-model evidence |
|---|---|
| I/O / digital format | RCA S/PDIF **24-bit**,EIAJ CP-340/IEC958;**44.1/48kHz**. Output HPF/TPDF dither choices24/20/16/8-bit. Published digitalprocessing delay **0.1ms at48kHz**,not total analog round-trip latency. [Own XL table](https://mediadl.musictribe.com/download/software/tcelectronic/tc_electronic_m-one_xl_manual_spanish.pdf). |
| I/O / analog limits | XLR input **21kΩ balanced/13kΩ unbalanced**,maximum+24dBu. Output **40Ω**,maximum+20dBu balanced;range choicesbalanced20/14/8/2dBu,unbalanced14/8/2dBu. [Own XL table](https://mediadl.musictribe.com/download/software/tcelectronic/tc_electronic_m-one_xl_manual_spanish.pdf). |
| Conversion / format | A/D andD/A **24-bit,128× oversampling**. A/Ddelay0.65/0.70ms andD/Adelay0.63/0.68ms at48/44.1kHz respectively;these are stage specifications,not measured fullunit latency. [Own XL table](https://mediadl.musictribe.com/download/software/tcelectronic/tc_electronic_m-one_xl_manual_spanish.pdf). |

### M-One XL — clock selection and bypass tails

Checked2026-10-18 in manufacturer-authored Rev4 mirror,pp11–12;cover/declaration andE60500152 imprint identify XL SW2.07. Watermarks retained;no hardware test.

| Field | Exact operating distinction |
|---|---|
| I/O / source and clock | Analog source initially selects internal44.1kHz;clock options areinternal44.1,internal48 orDigital,including withanalog input. Digital source locks toS/PDIF;outputs mute during lock andunmute when acquired. Internal clock with digitalaudio requires synchronization;slip samples trigger **Rate Mismatch**. XL-only **ANLGLEFT** uses leftXLR input. Input selection isglobal,not anextra input pair. [Own manual p11](https://www.liveline.be/wa_files/tc_electronic_m-one_xl_manual_english.pdf). |
| Live / bypass modes | **0%Mix** passes input tooutput; **FXInput** cuts engineinput while lettingexisting effects decay andretaining dry; **FXOutput** cuts effectoutput immediately while retaining dry. These are enginebypass modes,not proof ofrelay true bypass orpreset-change spillover. [Own manual p12](https://www.liveline.be/wa_files/tc_electronic_m-one_xl_manual_english.pdf). |
| Routing / lock | Routing Lock makes currentrouting global andignores routing stored inrecalled presets. It doesnot create additionalengines orscenes. [Own manual p12](https://www.liveline.be/wa_files/tc_electronic_m-one_xl_manual_english.pdf). |

### M-One XL — recall, store and tempo controls

| Field | Own Rev4 manual distinction |
|---|---|
| Memory / preview versus recall | CONTROL wheel previews presets with flashing number/ENTER; **ENTER orRECALL** activates, **EXIT** returns tocurrently loadedpreset. Factory locations cannot be overwritten. STORE suggests firstfree userlocation unless editing auserpreset,when it suggests thatsame location;ENTER confirms saving. Empty-slot behavior doesnot establish original userbankfill. [Manual pp16–17](https://www.liveline.be/wa_files/tc_electronic_m-one_xl_manual_english.pdf). |
| Live / tap and MIDI sync | Global TAP can targetEngine1,Engine2 orboth; subdivision canignore taps oruse straight/dotted/triplet values. MIDI Sync locks tempo toincoming MIDIclock;it is distinct fromS/PDIF audio-clock synchronization. [Manual p17](https://www.liveline.be/wa_files/tc_electronic_m-one_xl_manual_english.pdf). |

Checked2026-10-18;no presetwrite orhardwareoperation performed.

### M-One XL — delay and pitch limits

Checked2026-10-18 in original Rev4 manufacturer manual mirror,printedpp27–31.

| Field | Algorithm-specific scope |
|---|---|
| Processing / delay times | **One Tap0–4000ms;Two Tap0–4000ms per tap**,with rightchannel offset0–200ms. Each tap has feedback,level andpan controls. **XL-only PingPong0–1800ms**,so the4s range must not be assigned toall delays. These are repeat buffers,not verified overdub-loop storage. [Manual pp27–28](https://www.liveline.be/wa_files/tc_electronic_m-one_xl_manual_english.pdf). |
| Processing / pitch voices | Pitch Shift adds **two fixed voices**,each **−1200…+1200cents**,independent level/pan and0–100ms delay. Detune instead gives eachvoice **−50…+50cents**. Fixed transposition doesnot establish scale-aware harmony,polyphonic tracking orsound-generating synthesis. [Manual p31](https://www.liveline.be/wa_files/tc_electronic_m-one_xl_manual_english.pdf). |
| Processing / modulation structure | Classic Chorus andFlanger use two voices;4Voice versions combine twoClassic blocks internally. Both rates span **0.05–19.2Hz**. Internal voices do not increase the processor’s twoengine limit. [Manual pp29–30](https://www.liveline.be/wa_files/tc_electronic_m-one_xl_manual_english.pdf). |

### M-One XL — direct-expression capability screening

Checked 2026-10-28 against [manufacturer-authored Rev4 manual mirror][M1XL-M], exact XL rear inventory p8 and Pedal Setup p12. **No continuous analog EXP**: pedal jack accepts momentary switches only for engine1/2/both bypass or tap. **No dedicated headphone socket** in the complete XL inventory. No onboard preset down/up footswitches; CONTROL plus confirmation are hand-operated. Existing **483W×195Dmm** fails preference; metric/inch depth conflict remains. No direct passive-pickup suitability inferred from XLR.

Direct analog position/endpoints/recall are inapplicable. Routing Lock is global routing, not global volume assignment. Retain **FXInput** letting effects decay versus **FXOutput** cutting effects immediately, both retaining dry; these are not complete-output expression attenuation. Existing 0%Mix bypass remains separate. MIDI global-volume scope, looper coverage and current offer condition remain unverified. Original mirrored manufacturer identity/revision verified; no visual or hardware test, local download or sibling transfer.

## NOVA System

Checked 2026-10-18. Guitar multi-effects, distinct from NOVA Drive/Modulator and G-System. Manufacturer manual revision1.2,SW1.10,E60508712: identity verified from original text on mirror. Official PDF endpoints failed;generated mirror summary/FAQ excluded. Bass/vocal suitability unresolved.

<!-- comparison evidence begins -->
| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression | External Pedal In accepts expression orG-Switch;calibration required. Built-in/toe audit pending. | [Manual][NOVA-M] pp9,16–17 |
| K/F/B | **4 / 8 / 15**, derived from manual text: four A–D encoders; eight footswitches; seven effect-edit buttons + four variation keys + Factory Default, Store, Levels and Menu. Encoder rotation counts once; power/toe separate. Diagram/photo corroboration pending. | [Manual][NOVA-M] pp6–9,24 |
| Display | 24×2 characters;English manual says LCD,Spanish1.0 says LED (conflict below). Diagonal/color/touch unresolved. | [Manual][NOVA-M] p46 |
| Dimensions / weight | Printed284×89×267mm,axis order unlabelled;1.85kg. Inch-to-mm depth correspondence appears inconsistent;not silently corrected. | [Manual][NOVA-M] p46 |
| Processing / choices | Analog overdrive/distortion plus six digital blocks:compression,EQ+gate,modulation,pitch,delay,reverb. Section-level category census below;exact simultaneous ceiling remains unverified. | [Manual][NOVA-M] p5 |
| Factory / user memory | 30factory+60user presets;initial user fill unresolved. | [Manual][NOVA-M] p5 |
| Synth / acoustic | Dedicated synth/acoustic simulation unverified;pitch effects alone do not establish synthesis. | Pending |
| I/O | Drive In,Line In,two balancedTRS outputs,MIDI In/Out/Thru5-pinDIN,Pedal In,mains. Line In bypasses analog preamp/drive. Other-port audit pending. | [Manual][NOVA-M] pp9,46 |
| Conversion | AD/DA24-bit128×oversampling;listed converter delay0.63ms at48kHz. Complete operating-rate specification pending. | [Manual][NOVA-M] p46 |
| Power / battery / USB | 100–240VAC50–60Hz auto-select,<15W. DC-barrel polarity N/A to documented mains supply. Battery/USB operation unverified. | [Manual][NOVA-M] p46 |
| IR / NAM / capture | UserIR,native/convertedNAM andproprietary capture import unverified. | Pending |
| Editor / software | Editor/platform/OS support unverified;MIDI connector doesnot prove USB audio/editor compatibility. | Pending |
| Looper / drums / routing | Looper,drums,scenes andfull routing/spillover audit pending. | Pending |
| IDR used | Unknown;no qualified exacthardware offer. | Shopee search2026-10-18 |
| IDR new | Unknown;no exactShopee hit. Seller/item,condition,stock,region,bundle,warranty,voucher andcheckout total unresolved;not proof ofunavailability. | Shopee search2026-10-18 |

### NOVA System — routing, speaker filter and preset transitions

Checked 2026-10-18 against original manufacturer manual revision 1.2, SW1.10, pp12–19; mirrored original text, excluding generated FAQ.

| Field | Evidence / qualification |
|---|---|
| Routing / three architectures | **Serial:** successive blocks feed one another. **Semi Parallel:** delay/reverb run independently. **Parallel:** modulation/delay/reverb receive the same signal independently. These are fixed routing alternatives, not arbitrary free block ordering. [Manual][NOVA-M] pp12–13 |
| Cabinet / EQ restriction | **SpeakerSim is a high-frequency speaker-simulation filter; enabling it disables EQ.** Manufacturer recommends it for direct recording/mixer connections and off into a guitar amplifier. This does not establish cabinet IR loading or an amp-model library. [Manual][NOVA-M] pp18–19 |
| Live / delay versus reverb tails | FX Mute **Soft** preserves delay repeats across different delay presets;reverb can continue but adopts the new preset's settings. **Hard** mutes both. This is not proof of wholly gapless preset changes. [Manual][NOVA-M] p18 |
| Expression / volume position | **Pre** places volume after drive,before effects,allowing tails while lowering input to effects;**Post** controls the complete effected signal. [Manual][NOVA-M] p14 |
| Expression / recall and curve | Master **Preset** recalls stored parameter value;**Pedal** uses physical position at preset change. Min/Mid/Max each0–100% define response;one Pedal In selects Expression orG-Switch,not both concurrently. [Manual][NOVA-M] pp16–17 |

### NOVA System — category census and pitch-range conflict

Checked 2026-10-18 against original manual revision 1.2, SW1.10, printed pp3,26–45. Counts below derive from named sections, not an installed-firmware test or manufacturer total.

| Field | Evidence / qualification |
|---|---|
| Category choices / section census | Drive2;compression3;EQ1;noise gate1;modulation6;pitch5;delay6;reverb4. **28 section-level entries**,excluding boost,tuner,speaker filter androuting utilities. EQ/gate are separate entries here but grouped in the manual's six-digital-block headline. This count does not establish28 simultaneous processors. [Manual][NOVA-M] |
| Category choices / delay and reverb | Delays:Clean,Analog,Tape,PingPong,Dynamic,Dual. Reverbs:Spring,Hall,Room,Plate. **Spillover is behavior,not a seventh delay algorithm.** Internal delay taps andreverb shapes do not add choices. [Manual][NOVA-M] pp41–45 |
| Processing / time limits | Common delay range0–1800ms;Dual has two independently adjustable taps. Reverb decay0.1–20s,pre-delay0–100ms. These parameters are not phrase-looper duration. [Manual][NOVA-M] pp41–45 |
| Synth / pitch-range disagreement | Pitch Shifter introduction says±1octave;Voice1 range±1200cents butits explanation says±2octaves;Voice2 lists±2400cents. Preserve this unresolved internal disagreement. Separate intelligent harmony has two voices withkey/scale selection;not evidence ofpolyphonic synthesis. [Manual][NOVA-M] pp39–40 |

### NOVA System — MIDI backup and control scope

Checked 2026-10-18 against original manual revision1.2/SW1.10,printed pp21–23. [Manual][NOVA-M]. No MIDI/software operation performed.

| Field | Evidence / qualification |
|---|---|
| Memory / two distinct MIDI dumps | **Dump System sends global settings and excludes presets. Dump Bank sends the entire user bank.** Both are MIDI data dumps to a sequencer;the manual recommends astandard MPU401 interface. A system dump alone is not a complete preset backup,despite the manual's complete-system wording. This does not establish a desktop editor orsupported current OS. |
| MIDI / receive and program mapping | Receive channelOff,1–16 orOmni. Program-change input/output independently enabled;mapping translates incoming changes to presets andalso affects outgoing program changes onrecall. ChannelOff ignores incoming MIDI. |
| MIDI / clock and controller assignments | Incoming clock can supply global tempo. Each listed control function acceptsOff orCC0–127 assignments:effect bypass,boost,tap andthe expression-mapped parameter. This is aCC-number assignment range,not a documented on/off value threshold oraccess toevery editable parameter. |
| MIDI / identification | SysEx deviceID0–126 orALL distinguishes units;it isnot a MIDI channel number. |

### NOVA System — control census and variation memories

Checked 2026-10-18 against original manual revision1.2/SW1.10,pp7–9,24. Text-derived inventory;no photo inspection ordevice operation.

| Field | Evidence / qualification |
|---|---|
| Physical controls / count method | **K4/F8/B15.** Manual p24 explicitly identifies seven effect-edit switches;these are distinct from the eight performance footswitches described onp8. Four variation keys andfour additional named front-panel buttons complete B15. Dual functions andlong-press actions do not add switches. Built-in expression/toe hardware still requires diagram corroboration. [Manual][NOVA-M] |
| Memory / variation scope | Each selected effect type stores **four favorite settings** through the variation keys. Recalling one changes that effect in the current preset;the preset itself still needs saving. These are reusable effect settings,not four additional complete-preset banks orsimultaneous effects. [Manual][NOVA-M] p7 |
| Memory / factory-default scope | Front-panel Factory Default recalls defaults for the **currently selected effect algorithm**. It isdistinct from Utility Clear System anddoes not establish a whole-unit reset from one button press. [Manual][NOVA-M] pp7,19 |

### NOVA System — direct manufacturer Spanish specification check

Checked 2026-10-18. [Manufacturer Spanish manual][NOVA-SP],revision1.0/SW1.00 (p3),distinct from English1.2/SW1.10. Exact NOVA System cover andmodel declaration verified;English PDF still502. Text inspection only.

| Field | Evidence / qualification |
|---|---|
| Display / language-revision conflict | Spanish p46 calls the24×2-character display **LED**;English p46 says **LCD**. Preserve the disagreement;no new color,touch ordiagonal specification established. |
| Dimensions / repeated unit disagreement | Spanish p46 repeats **284×89×267mm** alongside **11.2×3.5×10.25in**. The final pair is not an exact conversion;this corroborates the printed discrepancy without resolving axis order orreplacing267mm with a calculated value. |
| I/O / analog specifications | Line impedance **21kΩ balanced/13kΩ unbalanced**;outputs **40Ω**. Maximum balanced/unbalanced output **+20/+14dBu into1200Ω**;selectable output ranges **20/14/8/2dBu**. Output dynamic range **>104dB,20Hz–20kHz**. These are operating/electrical limits,not device current draw oradditional processing choices. Spanish p46. |

### NOVA System — firmware 1.2 qualifications

Checked 2026-10-18 against [manufacturer 1.2 release/install notes][NOVA-FW12],indexed original text;direct PDF returned502. Changes explicitly compare with1.13. This firmware1.2 isdistinct from owner-manual revision1.2 describingSW1.10. No installer downloaded orupdate performed.

| Field | Evidence / qualification |
|---|---|
| Memory / restore defect fixed | Firmware1.2 fixes inability torestore saved **system anduser-bank MIDI dumps** (TT471). Documented dump creation in the older manual therefore doesnot prove reliable restore onearlier firmware. Installed version andactual backup/restore operation remain untested. |
| MIDI / clock and tap restriction | Fixes delay/modulation MIDI-tempo sync (TT604). **Tap tempo isdisabled while synced toMIDI clock**;tempo-dependent displayed parameters now update with MIDI tempo. System-dump reception **ignores SysEx ID**,so the general identification setting isnot a filter forthat transfer. |
| Expression / preset recall defect | Fixes physical pedal position not being read atpreset change in **Master:Pedal** mode (TT465). Earlier manual describes intended operation;correct behavior should not be assumed forunverified older firmware. |
| Processing / other fixes | Notes also fix intelligent-harmony scale changes not applying immediately,incorrect Factory Default behavior forsome subtypes,dynamic-delay L/R level mismatch andtuner exit requiring twopresses. These fixes qualify earlier feature descriptions without establishing new algorithms orhigher concurrency. |

### NOVA System — expression-volume capability audit

Checked2026-10-19; partial, original revision1.2/SW1.10 manual body on mirror, not generated FAQ.

| Field | Evidence / qualification |
|---|---|
| Expression / default versus global scope | Volume is the default pedal target. Pedal menu mixes global and preset parameters, distinguished by display **p**; extracted text does not identify the mapping’s marker. **Across-preset assignment remains unverified**; Master:Pedal only establishes position recall. [Manual][NOVA-M] pp14,16–17 |
| Expression / range and wiring | Volume−100–0dB; response Min/Mid/Max0–100%. TS orTRS depends on controller; one cable, not universal pinout compatibility. [Manual][NOVA-M] |
| Live / onboard navigation | MOD/PITCH select banks after hold; three switches select presets. This is bank navigation plus slot selection, not dedicated previous/next-preset switches. [Manual][NOVA-M] p19 |
| Expression / remaining | Built-in-treadle absence still needs panel corroboration; no dedicated headphones in recorded connector inventory. Bypass/looper coverage unknown. Existing Pre/Post, firmware1.2 recall fix and dimension conflict retained. No qualified new Shopee offer found; no download or operation. |
<!-- comparison evidence ends -->

[NOVA-M]: https://manualzz.com/doc/7256177/tc-electronic-nova-system-guitar-and-bass-owner-s-manual

Official original endpoints retained forprovenance: https://service-tcgroup.tcelectronic.com/media/Nova_Sys_US.pdf (502); https://mediadl.musictribe.com/download/software/tcelectronic/tc_electronic_nova_system_manual_english.pdf (inaccessible). No package/file downloaded ordevice/software operated.

[NOVA-SP]: https://service-tcgroup.tcelectronic.com/media/Nova_Sys_SP.pdf

[NOVA-FW12]: https://service-tcgroup.tcelectronic.com/media/novasystem-1_2-installation-guide.pdf

## PLETHORA X3

Checked 2026-10-17; partial. Guitar multi-effects; bass/vocal suitability and ownership unverified.

<!-- comparison evidence begins -->

| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression | No built-in treadle; **three pressure-sensitive MASH footswitches** provide assignable expression. External EXP socket absent from complete specification connector list; toe separate unresolved. | [Product][PX3-P]; [QSG p23][PX3-M] |
| K/F/B | **5 rotary /3 footswitches /0 separate buttons** from complete textual control inventory:Effect,TonePrint,three parameter knobs;three MASH. Play/Edit and Board selector switches separate;push encoders counted once. Earlier button uncertainty resolved by inventory,not visual inspection. | [QSG controls/specifications][PX3-M];[original V0.0 copy pp18–19,63][PX3-QM] |
| Display | **Three LCD slot displays**, corresponding to the three effect footswitches. PLAY shows each slot’s active effect; EDIT uses them for pedal/TonePrint lists and parameter settings. Diagonal/color/touch unresolved. Own V0.0 guide, printed18–19, reopened2026-10-29; text evidence, not visual inspection. | [Manufacturer-authored guide][PX3-QM] |
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
| Editor / desktop versus mobile functions | Exact X3 V0.0 guide explicitly offers the **desktop TonePrint App with full library and TonePrint Editor**, connected by USB. Its mobile app likewise provides library/editor access via Apple/Google stores. Desktop OS versions, architecture and current compatibility remain unknown; this is not merely a firmware updater. | [Own guide copy, printed p21][PX3-QM] |
| Expression / multi-parameter mappings | The guide permits **up to three parameters per knob or MASH control** through TonePrint Editor. Its generic EXP wording does not add a physical EXP socket absent from the X3 connector list; MIDI expression remains separately documented. Mapped parameters are not extra simultaneous audio blocks. | [Own guide copy, printed p21][PX3-QM] |
| Editor / dated Apple OS minimum | Developer listing explicitly names **Plethora X3** Bluetooth editing and requires **iOS16.0 /iPadOS16.0 or later**. Listed TonePrint version **4.6.18**, released **2025-04-01**, adds Infinite support subject to pedal firmware. Checked2026-10-18 in US/Indonesia storefronts; this is the listed app requirement, not an older-version or every-device guarantee. | [TC/MUSIC Tribe App Store listing](https://apps.apple.com/id/app/toneprint/id432767616);[US listing](https://apps.apple.com/us/app/toneprint/id432767616) |
| Editor / application identity | Android TonePrint is **com.tcelectronic.toneprint**; its listing shows update2025-03-26. The separate **TC app,com.tcelectronic.tcapp**, explicitly excludes TonePrint-generation products and must not replace TonePrint in this record. Android minimum OS and desktop compatibility remain unverified. | [Developer TonePrint listing](https://play.google.com/store/apps/details?hl=en&id=com.tcelectronic.toneprint);[Separate TC listing](https://play.google.com/store/apps/details?hl=en&id=com.tcelectronic.tcapp) |
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

### PLETHORA X3 — factory content and Board operations, 2026-10-18

[Own V0.0 quick guide, printed pp18–21][PX3-QM]; manufacturer-authored text, no software or device operation.

| Field | Documented scope / qualification |
|---|---|
| Memory / initial TonePrint content | The guide explicitly says **a selection of TonePrints is pre-installed**. It gives no filled-slot count and does not say all75 slots per effect or127 Board locations are factory-filled. TonePrint assignments include parameter values and knob/MASH mappings; they are not extra simultaneous effects. |
| Memory / Board management | In EDIT, BOARD UP opens **CREATE/DUPLICATE**; BOARD DOWN presents **DELETE/CLEAR** for the current Board. This confirms management functions, without assigning an undocumented difference between Delete and Clear or adding memory capacity. |
| I/O / mono connection | For mono operation use only each pair’s **MONO input and MONO output**; both TS jacks provide stereo connections when used together. This does not establish a dedicated headphone output or balanced TRS operation. |


### PLETHORA X3 — restored primary documents and current listing, 2026-10-31

| Field | Evidence / qualification |
|---|---|
| Editor / current desktop listing | [Current exact-model page](https://www.tcelectronic.com/en/products/0709-AIS) lists **TonePrint4.7.2 for Windows/macOS**. Listed availability does not establish OS minima or tested compatibility. Its firmware list heads **1.4.3**,with1.3.11 previous;preserve the separate manufacturer1.5.6 release notes above. Omission does not prove withdrawal,unsupported hardware or a downgrade recommendation. |
| Display / original primary source restored | The page now links [manufacturer-hosted X3 guide](https://cdn-media.empowertribe.com/a7147f29903640918cc9bc9fc6e097dc/QSG_TE_0709-AIS_PLETHORA-X3_WW.pdf),**V0.0,©2022,35PDFpages**;printed18–19 independently confirms the existing LCD slot/PLAY/EDIT description. This is the same original revision,not proof of a newer V1.0 guide. Old mirror and failed endpoints retained. |
| Expression / exact MIDI range | [Newly linked official X5/X3 table](https://cdn-media.empowertribe.com/c4ab468ba07f481080559bfc432c679c/PX5_3_MIDI_CC_table.pdf) prints **CC100:0–125→0–100%**,unlike adjacent0–127 mappings. Preserve this unusual range;126/127 behavior unverified. CC94/95 trigger Board down/up at64–127,0–63 inactive. MIDI expression still does not establish direct analog EXP or global master-volume assignment. |

No local files downloaded,software installed or hardware tested.

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

### PLETHORA X3 — direct-expression audit, 2026-10-19

**Direct analog external EXP:No**,complete model-specific connector inventory. [Manufacturer-authored V0.0 QSG copy][PX3-QM],printed pp18–19,63,listsTS audio pairs,MIDI DIN,USB andDC,butnoEXP orheadphone socket. ThreeMASH pressure switches areonboard expression,notanalogexternalinputs. Earlier genericEXP editor wording doesnot addmissinghardware. This fails the requested direct path,irrespective ofMIDI capabilities.

**176.53 W×116.75 Dmm** fits preference. Master-volume position,min/max,bypass/tail/looper coverage throughMIDI remain unverified;not inferred fromTrueBypass specification. OnboardBOARD selector isseparate fromfoot-operated boarddown/up,whose currentmapping remains unverified. PriorCC100GlobalExpression evidence isMIDI-only,not necessarily globalmastervolume. OfficialMIDI table failedretrieval thispass;older sourcequalification retained.

[Official V1.0 QSG][PX3-M] returned502;readthe matchingX3 V0.0 manufacturerbody,notgeneratedFAQ. Newerguide differences remain unverified. [ExactNEOMUSIC shop158235298/item28021818540][PX3-O1] returnedcachemiss2026-10-19. PreserveRp6.180.000 andseparateGeloraRp7.508.100 historicalasks;currentstock,condition,bundle,warranty,shipping andusedoffers unknown. No localdownload orhardwaretest.

## PLETHORA X5

Checked 2026-10-17; partial. Guitar/bass shared processor; ownership and vocal suitability unverified.

<!-- comparison evidence begins -->

| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression | No built-in treadle; **five MASH pressure switches**, each maps up to three parameters. External TRS EXP input; toe behavior unresolved. | [Product][PX5-P]; [QSG pp14–15][PX5-M] |
| K/F/B | **5 rotary / 5 footswitches / 0 separate buttons in the textual control inventory**. EFFECT/TONEPRINT push encoders and three parameter knobs. Specifications explicitly classify PLAY/EDIT and BOARD as selector switches, despite the controls prose calling PLAY/EDIT a knob. Encoder presses counted once; visual corroboration pending. | [QSG pp14–15,33][PX5-M] |
| Display | **Five corresponding LCD slot displays**, one per effect footswitch (slots1–5). PLAY shows loaded/active effects; EDIT shows effect, TonePrint and knob settings. Diagonal/color/touch unresolved. Indexed manufacturer QSG text checked2026-10-29; direct PDF returned500, no visual inspection. | [QSG pp14–15][PX5-M]; [manufacturer-hosted guide](https://cdn.mediavalet.com/aunsw/musictribe/sSjbS7aFnE6cqRC8D2gfUg/HooGpCuT9kurBB7T-lgWaQ/Original/QSG_TE_0709-AIK_PLETHORA-X5_WW.pdf) |
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
| Expression / volume audit2026-10-19 | Japanese distributor ELECTORI’s Rev1.3 manual explicitly covers **firmware1.3.11**: EXP ASSIGNMENT/VOLUME is **Board-level**, unlike global EXP calibration. Volume can precede slot1, follow slot5, sit between slots, or follow the insert before SEND/after RETURN. OFF disables volume; modifier and volume are mutually exclusive. Later global override, volume min/max and position recall remain unverified. | [Distributor manual pp5–7](https://www.electori.co.jp/tc-electronic/assets/pdf/PLETHORA_X5_MANUAL_JP_REV_1_3.pdf) |
| Expression / wiring and coverage qualification | Distributor p3 says **TS** EXP, conflicting with own QSG’s **TRS**; controller pinout remains unresolved. Its complete connector list has no dedicated headphones. Bypass, tail and looper attenuation guarantees remain unknown. No local download or device test. | [Distributor manual pp3,5–7](https://www.electori.co.jp/tc-electronic/assets/pdf/PLETHORA_X5_MANUAL_JP_REV_1_3.pdf);[QSG][PX5-M] |
| Expression / Hot Knob scope | The three Hot Knob assignments are **Board-level settings**,controlling multiple pedal parameters in Play mode;not three additional audio blocks. | [Own X5 release notes1.2.18][PX5-F] |
| Memory / automatic storage | Product documents automatic settings storage as edits occur. This does not establish a factory-filled Board count or persistent audio-loop storage. | [Product][PX5-P] |
| Live / buffered no-trails | Firmware1.3.6 adds **Buffered / No Trails**, retaining buffering while cutting delay/reverb tails when disengaged. Distinguish it from buffered trailing behavior and the later1.3.11 feedback change. | [Official release notes][PX5-F] |
| Expression / MIDI mapping | **CC100 Global Expression** maps0–125 to0–100%; Hot Knobs CC107–109. MASH for slots1–5:CC70/75/80/85/90; expression modifiers CC71/76/81/86/91. Physical EXP and MIDI expression are separate control paths. | [Official X5/X3 MIDI table][PX5-C] |
| Live / MIDI looper mapping | CC110 Record,111 Play,112 Clear,113 Pause. Values0–24/25–50/51–76/77–102/103–127 target slots1–5 respectively. Slots4–5 explicitly X5-only. CC92 tap,93 tuner,94/95 Board down/up. | [Official X5/X3 MIDI table][PX5-C] |
| Preset memory | **127 custom Boards;75 TonePrint slots per pedal**. Factory-filled subset unresolved; Board count is not simultaneous block count. | [Product][PX5-P] |
| Synth / acoustic | Dedicated synth/acoustic conversion unresolved. | Unresolved |
| I/O | Stereo quarter-inch TS inputs/outputs; TS Send/Return insert; TRS EXP; MIDI In/Thru; **Mini-B USB** for computer TonePrint/update; DC input. USB audio/power unresolved. | [QSG pp14–15][PX5-M] |
| Power / battery / USB | **9V DC,>600mA included supply**,5.5/2.1mm centre-negative. Actual draw,battery/USB operation unresolved. | [QSG controls/specifications][PX5-M] |
| Dimensions / mass | Guide prints **298.5×116×53mm under H×W×D**,1.4kg. Axis-label inconsistency preserved; no silent normalization or size-bin assignment. | [QSG specifications][PX5-M] |
| IR / NAM / capture | **Nine global proprietary cabinet simulations**, including bass use. User IR/native or converted NAM/capture support unresolved. | [Product][PX5-P] |
| Editor / dated mobile compatibility | Developer listings explicitly name **Plethora X5** Bluetooth editing. Apple lists **TonePrint4.6.18,2025-04-01**, requiring **iOS16.0/iPadOS16.0+**; Google Play lists Android TonePrint,updated2025-03-26. Checked2026-10-18; minimum Android OS,desktop OS/architecture and every-device operation remain unverified. This narrows the older platform uncertainty without treating historical firmware notes as current OS requirements. | [Developer Apple listing](https://apps.apple.com/us/app/toneprint/id432767616);[Developer Android listing](https://play.google.com/store/apps/details?hl=en&id=com.tcelectronic.toneprint) |
| Editor / distinct TC application | The separate **TC app,com.tcelectronic.tcapp**, expressly excludes TonePrint-generation products. It is not a replacement editor for this X5 record; TonePrint’s Android package is **com.tcelectronic.toneprint**. No app installed or hardware connection tested. | [Developer TC listing](https://play.google.com/store/apps/details?hl=en&id=com.tcelectronic.tcapp) |
| Editor / platforms | Own X5 release notes, **1.1.55 dated 2020-11-09**, explicitly list TonePrint desktop editor for **Mac and PC**, and mobile app for **iOS and Android**. Historical platform evidence only: desktop/Android OS versions and processor architecture remain unverified; dated mobile-store evidence appears above. Bluetooth/USB app connectivity does not establish USB audio or power. | [Official release notes, version1.1.55 section][PX5-F]; [QSG pp14–15][PX5-M] |
| Live / looper | RAM looper: **40s stereo/80s mono**, up to five instances per Board. Multiple instances do not imply five times shared memory capacity. Drums/scenes unresolved. | [Product][PX5-P] |
| Live / routing | Insert allows external drive or four-cable setup; Quick Swap reorders effects. | [Product][PX5-P] |
| Bass capability | Own product explicitly offers bass-oriented cabinet simulation; shared bass inclusion does not certify every effect equally on bass. | [Product][PX5-P] |

### Separate IDR hardware offers

| Condition | Evidence | Source |
|---|---|---|
| Used | No qualified offer. | — |
| New | No condition-confirmed offer. | — |
| Unverified condition | **Rp9.105.200**,NEO MUSIC,shop158235298/item27271818642,Kota Sukabumi. Checked2026-10-17; three-month indexed crawl,July2 delivery text. Historical ask, not current stock/checkout. | [Item][PX5-O] |

### PLETHORA X5 — readable V3.0 guide, 2026-10-31

[Manufacturer-authored mirrored guide](https://device.report/m/2fae0bfbda2091158a57d1b22482ef6f5af083e6db2ff7851088282e301026b9), exact X5 title, V3.0, Music Tribe©2021, printed pp14–15,33. Read extracted original text, not generated FAQs; no download or visual inspection.

- LCDs correspond to effect switches1–5; separate status LEDs are not additional screens. EDIT selects/edits a slot; PLAY switches its effect. Screen diagonal/color/touch remain unverified.
- Specifications identify **Mini-B USB** and **True Bypass**. This does not establish bus power, USB audio, trailing behavior or power-failure bypass.
- EFFECT/TONEPRINT encoder presses assign the selected item in EDIT; both have no PLAY function in this revision. Do not infer unchanged behavior in later firmware.

Exact NEO MUSIC item27271818642 returned cache miss on this pass; preserve the historical Rp9.105.200 ask without claiming current stock or condition.


### PLETHORA X5 — restored original guide and persistence scope, 2026-10-31

| Field | Evidence / qualification |
|---|---|
| Editor / current exact-model listing | [Current manufacturer X5 page](https://www.tcelectronic.com/en/products/0709-AIK) lists **TonePrint4.7.2 for Windows/macOS**. OS minima and tested compatibility remain unknown. Its retrieved Files section has no firmware heading;this does not prove firmware withdrawal or supersede the preserved1.5.6 history. X3’s firmware listing is not transferred. |
| Memory / stored TonePrint persistence | Same page explicitly says **Store To Product retains TonePrints after power-off**. This establishes saved TonePrint persistence,not persistent recorded loops,held EXP position or global all-Board volume assignment. |
| Display / direct original guide | The page links a readable [manufacturer-hosted X5 QSG](https://cdn-media.empowertribe.com/069d07f7d9a3476e87a799ebe17a7483/QSG_TE_0709-AIK_PLETHORA%20X5_WW.pdf),**V3.0,©2021,25PDFpages**. It corroborates the already recorded five slot LCDs and TRS EXP,without resolving screen diagonal/color/touch or the distributor TS conflict. Printedp33 still labels298.5×116×53mm as H×W×D;axis ambiguity remains. Old endpoints and mirrored evidence are retained. |

Text-only review;no local download,installation or hardware operation.

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
