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
| Categories / choices | **32 amps, 23 cabinets, 16 stereo effect choices**. Product calls amp groups Clean/Acoustic/Guitar; manual divides 32 as 16 bass + 8 guitar + 4 keyboard + 4 acoustic and documents 4 drive models. Taxonomies retained. [Product][BV-P], [Manual][BV-M] |
| Factory / user memory | **125 editable/storable presets, 25 × 5**; factory/user partition not established. [Manual][BV-M] |
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
| Verified used offer | **?** | Sale condition unverified |
| Verified new offer | **?** | Sale condition unverified |
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
| Factory / user memory | **125 rewritable presets,25×5**; factory/user partition **?**. [Manual][BV-M] |
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
| Blocks / category choices | **32 amps, 15 cabinets, 16 effect selections**; clean/blues/metal/rock amp groups. These are choices, not simultaneous block counts. [Product][V2-P] Manual describes five preset ingredients, fixed effect combinations and independent **nine-type reverb**; freely assignable DSP-slot ceiling **?**. [Manual][V2-M] |
| Memory | **125 rewritable presets, 25×5**; factory subset **?**. [Product][V2-P] |
| Synth / acoustic | Dedicated synthesis and acoustic-simulation algorithms **?**; cabinet models do not prove either. |
| IR / NAM / captures | User IR, native NAM, converted NAM and proprietary capture import **?**. |
| I/O | Quarter-inch guitar, stereo AUX, L/R balanced line outputs, stereo phones, FS112V socket; DIN MIDI IN and OUT/THRU; AC IN. [Manual][V2-M] USB/audio-interface capability **?**. |
| Power / battery / USB | **13 W**, external supply. Unit-side voltage, current, connector pinout, polarity, battery and USB power **?**. [Manual][V2-M] Manufacturer warns replacement supplies are country-specific. [Product][V2-P] |
| Editing / platforms | Manufacturer names historical third-party **iVAMP and V-amplio Pro for Mac OS X**; current compatibility **?**. MIDI parameter/preset transfer documented; MIDI THRU suppresses the unit’s own outgoing messages. Driver/updater/USB-audio support **?**. [Product][V2-P] |
| Practical features | Tuner, noise gate, tap tempo; five configurations **S1/S2/L1/L2/L3**. S2 splits effect-free/effected outputs; L2 omits cabinets; L3 splits stage-amp/mixer feeds. Headphones select S1. [Product][V2-P] Preamp bypass supports effects-only use. Looper, drums, scenes and spillover **?**. [Manual][V2-M] |

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

Manual identity: manufacturer English **v1.2, September 2002**, Rev C filename, 26 PDF pages. Relevant sections: controls pp.7–10; preset architecture p.13; effects pp.18–20; specifications p.25. A separate shared V-AMPIRE/V-AMP PRO/V-AMP 2 Rev B manual at https://images.thomann.de/pics/atg/atgdata/document/manual/164913_manual_eng.pdf was retrieved but has badly corrupted text; its sibling columns were not used to fill this record. Spanish v1.2 direct retrieval returned 502. Remaining: full routing/effect inventory, power label, contemporary software availability, factory-memory partition and qualified offers.
