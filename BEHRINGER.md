# Behringer multi-effects

[All guitar](ALL-GUITAR.md) · [All bass](ALL-BASS.md) · [Repository](README.md)

## Bass V-AMP

<!-- comparison evidence begins -->
Checked **2026-10-17**. Desktop model; rack PRO remains separate. Manufacturer product page and manufacturer-authored manual v1.2 / December 2005 (Rev C filename), hosted by Thomann. Partial verification.

| Required field | Finding |
|---|---|
| Built-in / external / toe expression | No integrated pedal listed; MIDI expression/wah via FCB1010-type controller. Toe function depends on controller, **?**. [Product][BV-P] |
| Knobs / footswitches / buttons | Inventory: **10 top rotaries + side AUX Level / 0 integrated footswitches / 9 buttons** (A–E, Tuner, Tap, bank arrows). FS112V external two-switch control for presets/tuner. [Manual][BV-M] |
| Display | **2-digit 7-segment LED**; diagonal **?**. Touch/color specification **?** [Manual][BV-M] |
| Dimensions / weight | **236 W × 180 D × 63 H mm; approximately 1.2 kg** in 2005 manual; manufacturer Spanish manual instead **approximately 2 kg**, same dimensions. Weight conflict retained. [Manual][BV-M], [Spanish manual][BV-S] |
| Simultaneous blocks | Selectable effect/combinations; independent compressor/denoiser and extra MIDI wah. Manual describes five preset ingredients: amp, cab, pre-effect, post-effect/combination and compressor. Exact algorithm ceiling **?**; **16 effect groups** is not 16 simultaneous. [Manual][BV-M] |
| Categories / choices | **32 amps, 23 cabinets;16 advertised effect groups versus15 entries in the post-effect table** (unresolved;details below). Product calls amp groups Clean/Acoustic/Guitar; manual divides 32 as 16 bass + 8 guitar + 4 keyboard + 4 acoustic and documents 4 drive models. Taxonomies retained. [Product][BV-P], [Manual][BV-M] |
| Factory / user memory | **125 factory-programmed, editable/storable locations, 25 × 5**; factory originals restorable to the same locations, not a separate additional user bank. [Manual][BV-M] |
| Synth / acoustic simulation | Three-voice synth with 9 variants; MIDI synth separate. ULTRABASS adds lower octave. Acoustic voicing includes piezo/magnetic processing; electric-to-acoustic simulation **?**. [Manual][BV-M], [Product][BV-P] |
| IR / NAM / capture | User IR import, native NAM, converted NAM, capture **?**; factory cabinet simulations alone do not establish import |
| Audio/control I/O | Quarter-inch instrument, AUX, L/R line, phones, footswitch; 5-pin MIDI in/out-thru; AC input. Body calls LINE OUT balanced, technical table TS/unbalanced; AUX described stereo but specification says balanced TRS. Preserve conflicts. PRO-only digital/XLR/insert ports not assigned here. [Manual][BV-M] |
| Power / battery / USB | **External supply, 13 W**; adapter mains regional 120 V/60 Hz, 240 V/50 Hz, 230 V/50 Hz, 220 V/50 Hz or 100 V/50–60 Hz. Unit-side AC voltage/current/pinout **?**; DC polarity not assumed. Battery/USB power **?**. [Manual][BV-M] |
| Editor platforms | MIDI parameter/SysEx documented; supported editor applications/OS **?**. USB audio **?**; no USB listed. [Manual][BV-M] |
| Looper / routing / live features | Delay/loop sampler **15.36 s requires MIDI control**; without MIDI, maximum delay **1,023 ms**. Six manual modes **S1–S3/L1–L3**; S3 sends processed left/unprocessed right, omitted from product’s five-mode discussion. Product: headphones select S1; S2 splits no-FX left/FX right; L1 mixer, L2 amp returns, L3 amp+PA. Drums **?**. [Manual][BV-M], [Product][BV-P] |

### Bass V-AMP — separate IDR evidence

| Class | Amount | Exact hardware offer and qualifications |
|---|---:|---|
| Sold-out indexed hardware ask; sale condition unverified | **Rp1.000.000** | [gitar second,61848168/3979207338][BV-O],Kabupaten Polewali Mandar. Checked 2026-10-17 ; search cache 3 months, delivery 21–25 July, **Habis**. Exact open failed cache miss. Seller name is not condition proof; working condition, adapter, footswitch, bag, bundle, warranty **?**. Late delivery voucher not deducted. |
| Condition unverified;stock unconfirmed | **Rp1.925.000** | [melodiasby,shop158144224/item26580662622](https://shopee.co.id/Behringer-V-Amp-Bass-Effect-Amp-Modelling-i.158144224.26580662622),KotaSurabaya. Checked2026-10-17,direct page retrieval with2weekcrawl;search cache3months. No Habis label in retrieved text does not prove stock. Condition,working status,adapter/footswitch/bag,bundle,warranty,shipping/tax and checkout availability unverified. Late-delivery compensation voucher not deducted;delivery4–5October is cached,not a current promise. |
| Verified used offer | **?** | Sale condition unverified |
| Verified new offer | **?** | Sale condition unverified |
### Bass V-AMP — memory and restoration,2026-10-17

| Field | Verified behavior / qualification |
|---|---|
| Factory / user memory | [Manufacturer manual v1.2,December2005,p10][BV-M] describes restoring the original factory preset for each location and restoring all factory presets. The125 editable locations therefore hold factory-programmed sounds;do not add a second125-slot user bank. |
| Memory / save | Hold the destination preset button about2seconds to overwrite it;bank selection allows saving elsewhere. Selecting another preset discards unsaved edits. |
| Memory / restoration | Holding both arrows until Pr recalls the location’s original sound;save it to retain the restoration. D+E during startup,then both arrows after CL,restores all factory sounds and overwrites user saves. Manual points to MIDI SysEx backup in8.4.1;this does not establish an editor application. |

### Bass V-AMP — effect inventory and count discrepancy,2026-10-17

| Field | Verified inventory / limit |
|---|---|
| Processing / post-effect choices | [Manufacturer manual v1.2,December2005,table6.1,p14][BV-M] enumerates **15**:VCF+Flanger,Delay+Chorus,StereoDelay,Delay/Loop,Reverb,Ambience,VoiceBox,Ultrabass,RotaryCab,Phaser,Flanger,Chorus,StereoChorus,Synth,MIDISynth. The text advertises16groups;the missing sixteenth remains unresolved. Do not silently reconcile it with bypass or a pre-effect. |
| Processing / pre-effects | Table6.2,p13 lists MIDIWah,P-Funk’n,AutoWah. MIDIWah excludes the other two;these choices are separate from the post-effect table. Compressor anddenoiser operate independently of the multi-effects section. Exact aggregate ceiling remains unverified. |
| Synth / MIDI distinction | P15 distinguishes instrument-driven three-voice Synth,nine variants,from MIDISynth for external note control. MIDISynth has its own MIDI-accessible reverb;not proof of freely assignable extra reverb on every patch. |

### Bass V-AMP — latency and MIDI backup,2026-10-17

| Field | Verified behavior / qualification |
|---|---|
| Processing / latency | [Manufacturer manual v1.2,December2005,p18][BV-M] specifies approximately **5ms LineIn→LineOut**,31.250kHz internal sample rate and24-bit converters. This is the published path value,not a new measurement or USB-audio specification. |
| MIDI / backup | Section8.4.1,p16 supports whole-memory dumps to a MIDI sequencer and a selected-preset transfer through a temporary buffer. Receiving a full dump with MIDI editing enabled overwrites all presets;save a received single preset to retain it. OUT transmits preset/parameter changes;THRU forwards incoming data without originating its own. Application names andsupported editor OS remain unverified. |

<!-- comparison evidence ends -->

### Provenance and remaining checks

The Music Tribe English manual URL returned 502; another returned 404. The Thomann-hosted manufacturer manual identifies both models, version 1.2 / December 2005, and separate desktop/rack columns. Only selected sections were checked; no complete manual or installed firmware audit. The product’s included accessories describe the original retail bundle, not this seller’s completeness. Shared guitar membership follows explicit manufacturer use, not sibling specifications. Remaining: unit-side adapter rating/pinout, connector conflicts, exact simultaneous count, remaining routing details, editor support and qualified offers.

[BV-P]: https://www.behringer.com/en/products/0709-AAC
[BV-M]: https://images.thomann.de/pics/atg/atgdata/document/manual/163587_manual_engl.pdf
[BV-O]: https://shopee.co.id/behringer-bass-v-amp-multieffect-i.61848168.3979207338

### Desktop routing and control qualifications

The manual’s five preset ingredients describe saved processing stages, not five freely assignable effect slots. MIDI wah cannot operate alongside Auto Wah or P-Funk’n. Post-effect crossover can leave low frequencies unaffected; input sensitivity adjustment in Configuration applies to every preset. Same-channel output-to-AUX connections can feed back. The last preset is recalled at startup; unsaved edits are lost when selecting another preset. MIDI controllers55–60 provide record,play,stop,speed,reverse and play-once sampler controls. [Manual][BV-M]

[BV-S]: https://mediadl.musictribe.com/media/sys_master/h9c/h88/8850172641310.pdf

## Bass V-AMP PRO

<!-- comparison evidence begins -->
Checked **2026-10-17**. Separate rack model; selected manufacturer manual sections, including its PRO-only columns. Partial verification.

| Required field | Finding |
|---|---|
| Built-in / external / toe expression | No integrated pedal; MIDI controller expression/wah. Toe behavior **?**, controller-dependent. [Manual][BV-M] |
| Knobs / footswitches / buttons | **10 rotaries /0 integrated footswitches /10 front buttons**: shared nine A–E/Tuner/Tap/arrows plus LINE IN; power and rear ground-lift switches additional. [Manual][BV-M] |
| Display | **2-digit 7-segment LED**, digital-format/sample-rate indicators; diagonal **?**. Touch/color specification **?**. [Manual][BV-M], [Specifications][BP-S] |
| Dimensions / weight | **482.6 W ×135 D ×89 H mm**. Older v1.2 manual **approximately2.6kg**; Spanish manufacturer manual **approximately2.76kg**. Revision conflict retained. [Manual][BV-M], [Specifications][BP-S] |
| Simultaneous blocks | Five preset ingredients: amp,cab,pre-effect,post-effect/combination,compressor. Denoiser independent. Exact algorithm ceiling **?**. [Manual][BV-M] |
| Categories / choices | **32 amps** (16bass/8guitar/4keyboard/4acoustic), **23 cabs,16 effect groups,4 drive choices**; group count is not simultaneous count. [Manual][BV-M] |
| Factory / user memory | **125 factory-programmed,rewritable locations,25×5**;factory originals can be recalled into the same locations,not an additional125-slot user bank. [Manual][BV-M] |
| Synth / acoustic simulation | Three-voice synth,9variants; MIDI synth. Acoustic amp/voicing not independent electric-to-acoustic proof. [Manual][BV-M] |
| IR / NAM / capture | User IR,native NAM,converted NAM,capture **?**; factory digital/analog cab simulation alone does not establish import |
| Audio/control I/O | Quarter-inch TS instrument;pre-DSP send/return;stereo post-DSP sends/returns;L/R TS analog outs;balanced XLR DI with ground lift;quarter-inch TRS phones;RCA and XLR digital outs;BNC wordclock;5-pin MIDI in/out-thru;IEC mains. [Specifications][BP-S] |
| Power / battery / USB | **15W,IEC**. Regional mains120V60Hz,230V50Hz,100V50–60Hz,220V50Hz;general export120/230V50–60Hz. Not automatic universal-voltage proof. DC polarity N/A; draw in amps,battery/USB power **?**. [Specifications][BP-S] |
| Digital / USB audio | **24-bit conversion,31.250kHz internal DSP**;digital outputs44.1/48/96kHz internal clock or32–96kHz external wordclock via conversion. USB audio **?**,no USB listed. [Specifications][BP-S] |
| Editor platforms | Manufacturer lists third-party **iVAMP,Mac OS X** for Bass V-AMP PRO; present availability/current OS support **?**. MIDI/SysEx distinct from USB audio. [Software mention][BP-E] |
| Looper / routing / live features | **15.36s sampler requires MIDI**;without MIDI1023ms delay. Six modes;S3processedleft/directright. LINE IN selects pre-DSP return for reamping. Headphones selectS1/cab automatically,configurable afterward. Drums/loop retention **?**. [Manual][BV-M] |

### Bass V-AMP PRO — separate IDR evidence

| Class | Amount | Exact hardware offer and qualifications |
|---|---:|---|
| Sold-out used-title indexed ask | **Rp500.000** | [cahyoadi56,53553463/28809251521][BP-O],Probolinggo. Title explicitly Second;**Habis**,search cache2months,delivery12–14August,checked2026-10-17. Exact page open failed cache miss. Working condition,faults,completeness,bundle and warranty **?**; not a working-unit valuation. Voucher not deducted. |
| Verified new offer | **?** | Not established |

### Bass V-AMP PRO — memory restoration

| Field | Verified behavior / qualification |
|---|---|
| Memory / save and recovery | Shared manufacturer manual explicitly names **both BASS V-AMP and BASS V-AMP PRO** in chapter4,printed pp9–10. Hold a destination preset key about2seconds to save,overwriting that location;unsaved edits disappear on preset change. Single-location factory recovery recalls its original sound,which must then be saved. Full factory restoration overwrites user presets;MIDI SysEx backup is referenced in8.4.1. Last-used preset returns at power-up. This documents common model scope,not an inference from desktop-only instructions. [Manual v1.2,December2005][BV-M] |

<!-- comparison evidence ends -->

### PRO provenance and practical qualifications

The Thomann manufacturer manual identifies version1.2/December2005 (Rev C filename). Manufacturer-hosted Spanish manual has English specification tables and a different mass; revision/date not established. Newer quick-start search evidence also lists2.76kg but direct retrieval returned502. No whole-manual or visual hardware inspection claimed. Do not import desktop AUX or external adapter details. Wordclock connector is described as lacking an internal75Ω terminating resistor. Pre-DSP send provides a dry recording feed; LINE IN chooses return processing. POST DSP send matches digital output signal; analog outputs follow it when returns are unused. [Manual][BV-M]

The 2005 MIDI appendix marks velocity,aftertouch andpitch-bend reception N; Spanish appendix marks Y. Keep this documentation conflict; installed synth MIDI behavior untested. Remaining: source revision reconciliation,full algorithm/controller audit,physical button inventory confirmation,current editor support and qualified hardware offers. [Manual][BV-M], [Specifications][BP-S]

[BP-S]: https://mediadl.musictribe.com/media/sys_master/h9c/h88/8850172641310.pdf
[BP-E]: https://www.behringer.com/en/products/0709-AAD
[BP-O]: https://shopee.co.id/behringer-bass-v-amp-pro-%28-Second-%29-i.53553463.28809251521

## V-AMP 2

<!-- comparison evidence begins -->
Checked **2026-10-17**, partial. Guitar desktop multi-effects; distinct from original V-AMP, V-AMP 3 and Bass V-AMP models.

| Required field | Finding |
|---|---|
| Built-in / external / toe expression | No integrated pedal in the manual inventory. MIDI wah control; external toe behavior **?**. [Product][V2-P] |
| Knobs / footswitches / buttons | **11 / 0 / 9**: ten top rotary controls plus side AUX LEVEL; A–E, TAP, TUNER, two bank buttons. External FS112V is separate. [Manual][V2-M] |
| Display | Two-digit numeric LED; diagonal, color specification and touch **?**. [Manual][V2-M] |
| Dimensions / weight | **236 W ×180 D ×63 H mm; approximately 1.2 kg**. [Manual][V2-M] |
| Blocks / category choices | **32 amps, 15 cabinets, 16 effect selections**; clean/blues/metal/rock amp groups. These are choices, not simultaneous block counts. [Product][V2-P] Manual describes five preset ingredients, fixed effect combinations and independent **nine-type reverb**; freely assignable DSP-slot ceiling **?**. Counting table 5.1 gives **3 delay-only, 5 modulation-only, 1 compressor-only, 1 auto-wah and 6 combination selections** (16 total); these overlap algorithm families, not independent slots. [Manual][V2-M] |
| Memory | **125 rewritable presets, 25×5**; factory subset **?**. Unsaved edits are discarded on preset change; factory recovery overwrites edits. [Manual][V2-M] [Product][V2-P] |
| Synth / acoustic | Dedicated synthesis and acoustic-simulation algorithms **?**; cabinet models do not prove either. |
| IR / NAM / captures | User IR, native NAM, converted NAM and proprietary capture import **?**. |
| I/O | Quarter-inch guitar, stereo AUX, L/R balanced line outputs, stereo phones, FS112V socket; DIN MIDI IN and OUT/THRU; AC IN. [Manual][V2-M] USB/audio-interface capability **?**. |
| Power / battery / USB | **13 W**, external supply. Unit-side voltage, current, connector pinout, polarity, battery and USB power **?**. [Manual][V2-M] Manufacturer warns replacement supplies are country-specific. [Product][V2-P] |
| Editing / platforms | Manufacturer names historical third-party **iVAMP and V-amplio Pro for Mac OS X**; current compatibility **?**. MIDI parameter/preset transfer documented; MIDI THRU suppresses the unit’s own outgoing messages. Manual also names the **V-AMP design PC editor**, requiring MIDI THRU disabled; current OS support **?**. Driver/updater/USB-audio support **?**. [Manual][V2-M] [Product][V2-P] |
| Practical features | Tuner, noise gate, tap tempo; five configurations **S1/S2/L1/L2/L3**. S2 splits the nominally dry left and wet right outputs; **left can retain compressor/auto-wah**, so it is not an unprocessed DI; L2 omits cabinets; L3 splits stage-amp/mixer feeds. Headphones select S1. [Product][V2-P] **L3 left has global monitoring EQ and no cabinet; right has cabinet and no monitoring EQ.** Headphones also auto-select a default cabinet if absent, with manual bypass available. [Manual][V2-M] Preamp bypass supports effects-only use. Looper, drums, scenes and spillover **?**. [Manual][V2-M] |

### V-AMP 2 — IDR observations

**New IDR: ?**. Neither cached ask certifies live stock, working condition or checkout availability.

| Condition / ask | Exact hardware evidence and limitations |
|---|---|
| **Used-title ask Rp1,200,000** | [Item 61848168/7587372301][V2-O2], title explicitly Second. Recovered from gitar second shop recommendation; seller ownership of the recommendation remains unconfirmed. Search crawl last month versus opened shop crawl five months. Both show the ask and one sold indicator, which is not a verified transaction price. Exact item open failed. Region, working condition, adapter, bag, footswitch, warranty and stock **?**; display_model_id 29387076168 remains unresolved. |
| **Condition unknown Rp1,100,000** | [sitiadiran, item 59084647/2820560961][V2-O1], Kabupaten Jember. Indexed last week, delivery 8–11 October; exact open failed. Bundle, warranty, condition and stock **?**. Late-delivery voucher up to Rp10,000 not deducted. |

Sources checked 2026-10-17. Manufacturer manual text inspected in the web viewer; no local manual, software, firmware or dependency downloads. Complete manual audit remains unfinished. Vocal-track preamp use in the manual does not establish an independently documented live microphone path; bass membership remains unverified.
<!-- comparison evidence ends -->

[V2-P]: https://www.behringer.com/en/products/0709-AAD
[V2-M]: https://cdn.mediavalet.com/aunsw/musictribe/qpnCBAUO90iaytgcpSr3Ng/BO7R0l3qqE6jsWGytbBfrQ/Original/8849825169438.pdf
[V2-O1]: https://shopee.co.id/Behringer-V-amp-2-i.59084647.2820560961
[V2-O2]: https://shopee.co.id/Efek-Gitar-Electric-Behringer-VAmp2-original-Second-Effect-Guitar-Vamp-2-V-AMP2-V-AMP-2-i.61848168.7587372301

Manual identity: manufacturer English **v1.2, September 2002**, Rev C filename, 26 PDF pages. Relevant sections: controls pp.7–10; preset architecture p.13; effects pp.18–20; specifications p.25. A separate shared V-AMPIRE/V-AMP PRO/V-AMP 2 Rev B manual at https://images.thomann.de/pics/atg/atgdata/document/manual/164913_manual_eng.pdf was retrieved but has badly corrupted text; its sibling columns were not used to fill this record. Spanish v1.2 direct retrieval returned 502. Follow-up 2026-10-17: corrected the earlier “effect-free” shorthand for S2 using table 2.1. Fixed combination counts are derived from table 5.1, not an assertion of 16 simultaneous effects. Manual p.9 says FS112V selects presets within a bank, while p.11 describes bank switching; this wording conflict remains unresolved. Remaining: power label, contemporary software availability, complete factory-memory partition, MIDI-only routing refinements and qualified offers.

## FX2000

VIRTUALIZER3D rack multi-effects;manufacturer explicitly names guitar,bass andvocals. Checked2026-10-17;partial. Use suitable amp/mixer routing;XLR connectors alone do not establish a microphone preamp.

| Field | Evidence / qualification |
|---|---|
| Instrument scope |Guitar,bass,vocal andkeyboard documented [FX-P];amp/mixer send-return levels must be set appropriately [FX-Q] |
| Expression |Built-in pedal/toe absent from rack control description;external expression mapping unverified |
| Knobs / footswitches / buttons |**6rotary derived**:4EDIT,MIX/BYPASS,JOG.0built-in footswitches. **6separate front buttons**:PRESET,EFFECT,EDIT,STORE,COMPARE,SETUP,numbered11–16 inoriginal manual. MIX push additional,not separate button;power andrear operating-level switches separate. Text-derived inventory;no visual panel check [FX-M pp.6–7,16] |
| Display |4-digit14-segment alphanumeric LED display;diagonal,color andtouch specifications unverified [FX-Q p.28] |
| Processing / categories |71algorithms,including combination algorithms;not71simultaneous effects. Own guide enumerates12reverbs+3delays+15modulation+8dynamics+6psychoacoustic+4filter/EQ+7distortion/amp+5special+11combination=71choices [FX-Q p.26]. Dual-engine combinations61–71 support serial1,serial2 orparallel;not a freely assembled chain of71blocks [FX-M pp.12,17] |
| Preset memory |100internal+100user=200;quick-guide factory chart fills both banks. Writable user locations;fixed-bank editing/persistence details pending [FX-Q] |
| Synth / acoustic |Vocoder,Resonator andRingModulator documented;not proof of a general instrument synth or dedicated acoustic simulator. RSM acoustic-environment modeling is not acoustic-guitar simulation [FX-P] |
| IR / NAM / captures |User IR,native/converted NAM andmeasured capture import unverified |
| Audio / control ports |2audio inputs and2outputs,each offered asbalanced6.35mm TRS andXLR sockets (8analog sockets,total2in/2out channels);3MIDI DIN:IN,OUT,THRU;IEC mains. Numbered rear inventory19–24 contains no USB,headphone,phantom orEXP socket;XLR does not establish mic preamp [FX-M p.7] |
| Analog levels / conversion |80kohm balanced input,80ohm balanced output;selectable−10dBV/+4dBu nominal. Maximum+1dBV/+15dBu respectively forboth input/output.24bit SigmaDelta,64/128× oversampling,**46.875kHz** sampling [FX-Q p.28] |
| Power / battery / USB |IEC mains;regional120V60Hz,230V50Hz,100V50/60Hz,and120/230V50/60Hz export versions.15W maximum;not universally autoranging. Battery/USB operation unverified;DC polarity not applicable to listed mains connection [FX-Q] |
| Dimensions / weight |**Source conflict:** QSG W483×D217×H44.5mm,netapprox1.9kg,shipping3.2kg [FX-Q p.28];fullmanual W482.6×D204.4×H44mm,netapprox2kg,shipping3kg [FX-M p.25]. Both approximate manufacturer specifications;revision/case difference unresolved. Shipping mass is not unit mass |
| Editor / software |MIDI SysEx backup documented;full editor andplatforms unresolved. No USB editor/audio inferred [FX-P] |
| Looper / drums / live |Sampler up to5s;not a verified full looper. Combination algorithms include Chorus/Reverb,Pitch/Delay andothers. Sampler contents clear on effect change [FX-M p.12]. Preset loading takes about1s withbrief signal suppression;not seamless switching. EXTN mixer mode100%wet;INTN amp-loop mode uses MIX. SysEx transfer disables audio [FX-M pp.16–17]. Drums,scenes andspillover unverified [FX-P] |

### FX2000 — separate IDR evidence

| Price class | Amount | Offer and limits |
|---|---:|---|
| Condition-unverified sold-out ask |Rp3.300.000 |[Pro Sound Hub295455465/6248529259](https://shopee.co.id/Behringer-FX2000-FX-2000-FX-2000-Effects-Processor-3D-Efek-Vocal-i.295455465.6248529259);Bekasi;four-month indexed,June17 delivery;Habis. Condition,bundle,voucher,warranty unverified |
| Condition-unverified indexed ask |Rp3.310.000 |[Evolusishop307891948/27592214711](https://shopee.co.id/Behringer-FX2000-3D-Virtualiser-FX-2000-3D-Efek-Vocal-Original-i.307891948.27592214711);Kab.Ponorogo;three-month indexed,July15–17 delivery. Condition,stock,bundle,voucher,warranty unverified |
| Verified used IDR |? |Not established |
| Verified new IDR |? |Not established |

### FX2000 — sources and remaining work

- [FX-P: exact manufacturer product](https://www.behringer.com/en/products/0828-AAG),indexed primary text.
- [FX-Q: manufacturer multilingual quick-start guide](https://mediadl.musictribe.com/media/PLM/data/docs/P0A3P/QSG_BE_0828-AAG_FX2000_WW.pdf),17PDF pages;control/connection text,preset chart andspecifications inspected. No new visual verification claimed.
- [FX-M: Full manufacturer manual](https://mediadl.musictribe.com/media/PLM/data/docs/P0A3P/FX2000_P0A3P_M_EN.pdf),direct opening failed;subsequent manufacturer-indexed text successfully inspected2026-10-17,pp.12,16–17,25 forcombination architecture,sampler,preset activation,routing andconflicting dimensions/mass. Full PDF body/visual panel remains uninspected.

No files downloaded. Remaining:fullmanual visual/revision check,display diagonal,software/routing andqualified offers.

## V-AMP 3

Checked2026-10-17. Partial guitar/bass multi-effects record,distinct from V-AMP2. [Manufacturer manual](https://mediadl.musictribe.com/media/sys_master/h56/hb7/8849514528798.pdf),18pages,©2013;web text only,no download orvisual diagram audit.

| Field | Evidence / gaps |
|---|---|
| Expression | No integrated pedal;MIDI wah/volume control. External analog EXP/toe unknown. |
| Controls | Derived **11 rotary /0 integrated footswitches /9 buttons**:10top+sideAUX;A–E,BankUp/Down,TAP,TUNER. |
| Display | Two-digit seven-segmentLED;diagonal/color/touch unknown. |
| Processing / choices | **32amps,15cabinets,9reverbs**. Five preset ingredients:amp,cab,preFX,postFX,reverb;not five arbitrary effects. **16 effect-selector positions**, including fixed combinations; independent reverb. See exact inventory below. |
| Presets | **125 editable presets,25×5**;not125factory+125user. |
| Synth / acoustic | Acoustic/bass preset banks documented;dedicated synthesis/acoustic conversion unknown. |
| Dimensions / weight | Manual: **79H×267W×180D mm;0.8kg**. Preliminary ©2012 brochure: **78H×180W×270D mm;approx0.8kg**. Published axes conflict;do not silently transpose. |
| I/O | ¼instrument,AUX,stereophones;L/Rline;DIN MIDI IN/OUT-THRU;¼TRSfootswitch;AC IN. Manual calls line outputs “TS,balanced”;preliminary ©2012 brochure says **TRS,balanced**. Panel text accepts balanced/unbalanced cables;actual connector verification unresolved. |
| Power | External supply;**13W**. Adapter output voltage/current/connector,polarity,battery unknown. Regional mains ratings are not processor input ratings. |
| USB / software | USB audio uses separate **UCA222**;not onboard USB. UCA PC/Mac support is not aV-AMP editor. Full editorOS unknown. |
| IR / NAM / capture | Native/convertedNAM,userIR,capture import unknown. |
| Looper / drums / routing | Looper/drums/scenes unknown. Five output configurations;headphones forceS1. |

### V-AMP 3 — separate IDR offers

| Condition / seller | IDR evidence | Exact item |
|---|---|---|
| Used | Unknown | — |
| New | Verified new-condition price unknown | — |
| Condition unverified / melodiasby,Kota Surabaya | **Rp2.046.000**. Opened body crawl1month;index2months. Current stock,variant,bundle/UCA222/footswitch/adapter,warranty,voucher,shipping/tax unknown. Stale September delivery window andlate-arrival voucher do not prove stock orhardware discount. | [158144224/26680659166](https://shopee.co.id/Behringer-V-Amp-3-Guitar-Multi-Effect-Processor-i.158144224.26680659166) |

Own product-information PDF8849735680030 failed web access;no facts adopted. Remaining work includes firmware/library-specific effect counts,power ratings,display specifications andcondition-qualified offers.
### V-AMP 3 — effect-selector inventory and control conflict

Checked 2026-10-17 against the [manufacturer manual](https://mediadl.musictribe.com/media/sys_master/h56/hb7/8849514528798.pdf), pp4–5,12–13.

| Selector grouping | Positions |
|---|---|
| Delay | Echo, Delay, Ping Pong |
| Modulation + delay | Phaser/Delay; Flanger/Delay 1 and 2; Chorus/Delay 1 and 2 |
| Other combinations | Chorus/Compressor |
| Dynamics/filter | Compressor, Auto Wah |
| Modulation | Phaser, Chorus, Flanger, Tremolo, Rotary |

These **16 positions** are choices, not 16 simultaneous blocks. MIDI-controlled wah is additional. Reverb has **9 choices**: Tiny/Small/Medium/Large/Ultra Room, Small/Medium Spring, Short/Long Ambience. Cabinet bypass is additional to15 cabinet models; amp selection loads a matched cabinet that can be changed.

The numbered control descriptions swap EFFECTS and EFFECTS SELECT roles compared with Basic Operation. Retain this labeling contradiction; it does not change the rotary count. Effect-table MIDI values also differ between some standalone/combined modulation entries; do not silently normalize them into one algorithm identity.

Adapter output ratings remain unverified after manufacturer-domain searches; no sibling-model power specification adopted.
### V-AMP 3 — preliminary brochure conflicts

Checked 2026-10-17. [Manufacturer-authored brochure on a mirror](https://usermanual.wiki/Behringer/BehringerVirtualAmplificationVAmp3Brochure752616.1343504435.pdf), five pages, exact V-AMP 3 title and ©2012 MUSIC Group identification. Page5 explicitly labels specifications **preliminary/conceptual**; this is qualified manufacturer evidence, not a current product page or measured unit. Web text read; no file download or diagram inspection.

Page5 gives **78H×180W×270D mm**, versus the ©2013 manual’s79H×267W×180D; retain axes and dimensions separately. Its **balanced TRS** output specification conflicts with the manual’s “TS,balanced,” while supporting the latter’s balanced-cable description. This corroboration does not prove the actual hardware connector.

The brochure reverb table ends at8 and combines Medium/Large Room inone entry; the manual enumerates9 separately. Treat this as a document/table conflict,not proof of different installed firmware. Both identify0.8kg approximately; the brochure’s1.76lb andmanual’s1.6lb equivalents disagree.

The brochure corroborates a separate bundled UCA222 interface andpreamp bypass. Historical inclusion does not verify the Indonesian seller’sbundle. No adapter output ratings resolved.
