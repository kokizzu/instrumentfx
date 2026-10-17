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
| Dimensions / weight | **236 W × 180 D × 63 H mm; approximately 1.2 kg**. [Manual][BV-M] |
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
