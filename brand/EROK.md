# EROK — multi-effects

[All guitar](../all-guitar.md) · [Repository](../README.md)

<!-- brand-index begins -->
**Model and section index — A–Z, natural numeric order**

- [MP-10](#mp-10)
- [MP-20](#mp-20)
- [Pocket Sonic](#pocket-sonic)
<!-- brand-index ends -->

## MP-10

<!-- firmware-pitch:EROK::MP-10 begins -->
### Firmware and pitch audit — EROK MP-10

| Field | Sourced finding |
|---|---|
| Firmware / first hardware release | Not verified. No dated first hardware launch established. June 2026 PDF creation/index dates and earliest located VER 014 notes are not hardware release dates. [launch 1](https://erokmusic.com/product/multi-effects/MP-10) |
| Firmware / latest verification | 016 — Latest verified. Official current catalogue selects MP-10_016.fwsc; explicit VER 016 changelog dates release November 17. Download metadata says November 18, treated as file metadata, not release date. Fixes UI, CAB saving/model upload and busy-state issues; normal upgrade retains presets/models/IR. VER 016 AI Ms Gate presets require older backups for downgrade. [firmware 1](https://erokmusic.com/js/firmware-notes/en.json) [firmware 2](https://erokmusic.com/js/data-core.min.js?v=13&rev=61ae222d06935186) [firmware 3](https://erokmusic.com/js/data-download-meta.js?v=10&rev=78d5cd5bb107c29f) |
| Firmware / release date | 2026-11-17 (day precision) |
| Firmware / release-to-update duration | Not calculable from verified dates; observed release span, not continuous support or promised future updates. |
| Firmware / audit date | 2026-11-21; [firmware recap](../FIRMWARE-UPDATES.md). |
| Pitch / note handling | Pitch present; polyphony unverified. VER 015 (2026-10-16) adds WHAMMY to EXT: MBody, Oct1, Oct2 and Bend control. Exact interval ranges and input polyphony unverified. Original manual also documents Shimmer wet pitch from unison to +2 octaves; this is not dry-signal transpose. [pitch 1](https://erokmusic.com/js/firmware-notes/en.json) [pitch 2](https://erokmusic.com/download/manuals/MP-10.pdf) |
| Pitch / preset recall | 120 writable locations; first 54 factory-filled, not 54 extra protected slots. Banks contain three presets. VER 016 retains saved resources on normal upgrade; newer AI Ms Gate presets have downgrade incompatibility. |
| Pitch / DSP resources | Original manual: seven reorderable modules FX/AMP/MOD/DLY/REV/CAB/EXT, advertised 7+1 via gate combined with boost/compression. WHAMMY occupies EXT; Shimmer is a REV choice. Pitch CPU %, current-firmware worst-case ceiling and combined WHAMMY/Shimmer operation unmeasured. |
| Pitch / qualifications | External TRS expression and calibration documented. Older manual EXT list is volume/four wah choices; WHAMMY availability requires the later VER 015+ notes, not sibling-model inference. MBody/Oct1/Oct2 labels alone do not prove polyphonic input tracking. |
| Pitch / comparison | [Polyphony, presets and DSP recap](../PITCH-SHIFTING.md). |

Sources checked:

- [EROK MP-10 exact product route](https://erokmusic.com/product/multi-effects/MP-10) — Exact MP-10 identity; no dated hardware launch. (Direct dynamic shell; public catalogue data recovered separately).
- [EROK official firmware notes — MP-10](https://erokmusic.com/js/firmware-notes/en.json) — VER 016 November 17, 2026; VER 015 October 16 adds WHAMMY MBody/Oct1/Oct2/Bend to EXT; resource retention and downgrade limits. (Direct public JSON as inert text, SHA256 df303b3d88967b04115e91708ad3bdcbe6023bc9278580caf5b0b2dd873d5cae).
- [EROK current product/download catalogue](https://erokmusic.com/js/data-core.min.js?v=13&rev=61ae222d06935186) — Exact MP-10 manual/gallery paths and current firmware 016 selection with November 17 date. (Direct manufacturer JS read as inert text, SHA256 61ae222d069351869f49a8e0c904c0a3429d834cc810039c226d1894f9a94341).
- [EROK download file metadata](https://erokmusic.com/js/data-download-meta.js?v=10&rev=78d5cd5bb107c29f) — MP-10_016 file date November 18 differs from explicit release notes; not adopted as release date. (Direct manufacturer JS as inert text, SHA256 78d5cd5bb107c29fd0035ed016786b0e56e670e65fc54278c1a091def219a5cd).
- [EROK MP-10 original manual](https://erokmusic.com/download/manuals/MP-10.pdf) — 120 locations, first 54 factory-filled; seven reorderable modules and 7+1 gate combination; Shimmer unison to +2 octaves; EXT volume/wah and TRS expression. Predates documented WHAMMY addition. (Direct manufacturer 14-page raster PDF; visually read printed EN01/02/05/08/09/11/12; SHA256 255db4da4d0ff61915b62eda1cf63055838b01929bd78b4aceae9ce7440eedbe).

<!-- firmware-pitch:EROK::MP-10 ends -->

<!-- model-images:EROK::MP-10 begins -->
<details>
<summary>Product pictures — top and rear ports</summary>

**MP-10 near-top manufacturer product image with active display**

[![MP-10 near-top manufacturer product image with active display](https://erokmusic.com/img/products/MP-10-1.webp?v=936e3222fbe0ba88)](https://erokmusic.com/img/products/MP-10-1.webp?v=936e3222fbe0ba88)

[Image source](https://erokmusic.com/product/multi-effects/MP-10). Exact EROK MP-10 branding and 01A screen visible. Slight perspective; powered-on state versus composited display is not independently authenticated.

**MP-10 angled rear connection view**

[![MP-10 angled rear connection view](https://erokmusic.com/img/products/MP-10-3.webp?v=1ff46eaae9d4d721)](https://erokmusic.com/img/products/MP-10-3.webp?v=1ff46eaae9d4d721)

[Image source](https://erokmusic.com/product/multi-effects/MP-10). Exact manufacturer gallery image shows rear audio/USB/phones/expression connections and side XLR. Perspective and small port labels limit readability; no model-family connector equivalence inferred.

</details>
<!-- model-images:EROK::MP-10 ends -->


<!-- comparison evidence begins -->
Checked2026-10-18; partial. Manufacturer identifies a portable guitar multi-effects unit with drums and recording. [Manufacturer](https://erokmusic.com/index.html). Bass/vocal suitability and ownership remain unverified. Seller Tank Pro wording does not establish identity with M-VAVE TANK-PRO.

| Field | Evidence / qualification |
|---|---|
| Expression | Built-in, external and toe behavior unverified. |
| Knobs / footswitches / buttons | Separate counts unverified; no panel visual audit. |
| Display | Diagonal, technology, color and touch unverified. |
| Dimensions / mass | Unit dimensions, axis order and weight unverified. |
| Processing / choices | Guitar multi-effects identity established; simultaneous ceiling, category choices and routing unverified. |
| Factory / user memory | Writable, protected, total and factory-filled split unverified. |
| Synth / acoustic | Dedicated synthesis, acoustic simulation and bass library unverified. |
| I/O | Recording advertised; full connectors, audio/MIDI channel formats and dry/reamp routing unverified. |
| Power / battery / USB | Voltage, current, polarity, battery and USB operation unverified. Seller eight-hour title is not primary verification. |
| IR / NAM / capture | Import formats, native/converted NAM and proprietary capture unverified; no sibling transfer. |
| Editor / software | Applications, editing scope, desktop/mobile OS, drivers and updaters unverified. |
| Looper / drums / live | Manufacturer advertises drums; counts, looper duration/retention, synchronization, scenes and trails unverified. |
| Documentation | [Manufacturer downloads](https://erokmusic.com/download) indexes MP-10 Manual PDF7.0MB,2026-06-22; original contents/URL unrecovered. Date does not establish document or firmware revision. Exact product route returned an internal access error. |

### Separate IDR hardware evidence

| Field | Evidence / qualification |
|---|---|
| IDR verified used | Unknown. |
| IDR verified new | Unknown. |
| IDR condition-unverified hardware ask | **Rp1.399.999**, crossedRp1.699.999/18%; EROK MUSIC,shop1736925571/item45705646832. [Exact MP-10 item](https://shopee.co.id/EROK-MP-10-Multi-Efek-Gitar-Bass-Loop-Mesin-Drum-Baterai-8-Jam-%E2%80%93-Portable-Tank-Pro-Oleh-M-vave-Technology-i.1736925571.45705646832). Direct JS-limited two-month cache and week-old search cache agree on the ask,checked2026-10-18. Search also displayed Rp1.329.999 for00:00 October10,an expired teaser,not adopted. Direct delivery August15–17 conflicts with indexed October10–12; neither proves stock. Condition,new/used,working state,selected variant,region,adapter/bundle,warranty,authenticity,voucher,shipping/tax andcheckout total unverified. Late-delivery compensation is not a purchase discount. Seller affiliation and Tank Pro equivalence unverified. |

No files/dependencies downloaded or software/devices operated. MP-9/MP-20/M-VAVE specifications are not borrowed.

<!-- comparison evidence ends -->

### MP-10 — warranty eligibility and expression evidence boundary

Checked2026-10-28. The [manufacturer warranty](https://erokmusic.com/) states one-year worldwide coverage for the original buyer of a new unit through an authorized dealer/official channel, with purchase proof; rights are non-transferable. It excludes unauthorized channels and second-hand platforms. This is a general policy, **not confirmation that shop1736925571 or item45705646832 qualifies**. Authorization, item condition and warranty eligibility remain unverified; the earlier cached ask is unchanged.

The [MP-10 product route](https://erokmusic.com/product/multi-effects/MP-10) now returns a dynamic shell rather than the earlier access error, but exposes no model-specific panel/manual contents. No available browser surface could recover its preview. Built-in treadle, analog EXP, global assignment, position/range, bypass/phones/tail/recorded-loop coverage, chassis fit and preset down/up all remain **unknown**, not No. The indexed manual listing is not a connector inventory. No model equivalence, downloads or device operation are inferred.

## MP-20

<!-- firmware-pitch:EROK::MP-20 begins -->
### Firmware and pitch audit — EROK MP-20

| Field | Sourced finding |
|---|---|
| Firmware / first hardware release | Not verified. No dated first retail release established. Manual filename/creation date, regulatory dates and earliest located V78 March 2026 notes are not hardware release dates. [launch 1](https://erokmusic.com/product/multi-effects/MP-20) [launch 2](https://erokmusic.com/download/manuals/MP-20.pdf) |
| Firmware / latest verification | 86 — Latest verified. Official catalogue selects MP-20_086.fwsc and V86 changelog explicitly dates October 19. File metadata dated October 27 is not release date. Adds global BPM/MIDI Clock; fixes WHAMMY Oct2 ceasing near Bend 80, Pattern Mono freezes and save failures. Back up via M-EFCS; downgrade erases user presets. [firmware 1](https://erokmusic.com/js/firmware-notes/en.json) [firmware 2](https://erokmusic.com/js/data-core.min.js?v=13&rev=61ae222d06935186) |
| Firmware / release date | 2026-10-19 (day precision) |
| Firmware / release-to-update duration | Not calculable from verified dates; observed release span, not continuous support or promised future updates. |
| Firmware / audit date | 2026-11-21; [firmware recap](../FIRMWARE-UPDATES.md). |
| Pitch / note handling | Pitch present; polyphony unverified. Manual-linked effect reference lists FX Pitch (high/low/dry levels), semitone Pitch shifter (Semi), and Octave. V81 (2026-08-20) adds Gojira WHAMMY; V86 fixes Oct2/Bend. Interval limits, WHAMMY module assignment and input polyphony unverified. DLY Ice Stereo shifts echoes; REV Shimmer wet pitch spans unison to +2 octaves. [pitch 1](https://erokmusic.com/download/manuals/MP-20.pdf) [pitch 2](https://manualf.oss-cn-hongkong.aliyuncs.com/manual/Combined-Effect-Pedals/PD39-Effects-Description.pdf) [pitch 3](https://erokmusic.com/js/firmware-notes/en.json) |
| Pitch / preset recall | 150 editable slots: 1–66 guitar-filled, 67–75 bass-filled, 76–150 initially effect-free. Not 150 plus separate factory slots. V78 adds snapshot mode within a preset; firmware downgrade after V81+ erases presets per notes. |
| Pitch / DSP resources | Ten reorderable modules FX/NS/DS/AMP/CAB/EQ/MOD/DLY/REV/VOL. FX Pitch/Pitch shifter/Octave share the FX choice; wet-pitch effects use DLY or REV. Onboard CPU meter warns above 90%; global EQ can overload heavy chains. No per-pitch CPU %, measured configuration, or proven simultaneous pitch combination found. |
| Pitch / qualifications | The manual itself links the PD39 effects reference via printed p12 QR, decoded and retrieved; applicability is established by that direct link, not inferred from MK-20 regulatory kinship. Stereo echo/reverb and separate pitch voices do not prove polyphonic input tracking. |
| Pitch / comparison | [Polyphony, presets and DSP recap](../PITCH-SHIFTING.md). |

Sources checked:

- [EROK MP-20 exact product route](https://erokmusic.com/product/multi-effects/MP-20) — Exact model identity; no dated hardware launch. (Manufacturer dynamic product route; public catalogue recovered separately).
- [EROK official MP-20 firmware notes](https://erokmusic.com/js/firmware-notes/en.json) — V86 October 19, 2026; WHAMMY Oct2 fix, V81 August 20 addition, V78 snapshots; downgrade data loss. (Direct inert JSON; SHA256 df303b3d88967b04115e91708ad3bdcbe6023bc9278580caf5b0b2dd873d5cae).
- [EROK current product/download catalogue](https://erokmusic.com/js/data-core.min.js?v=13&rev=61ae222d06935186) — Current MP-20 firmware86/date October19 and exact manual/gallery paths. (Direct inert JS; SHA256 61ae222d069351869f49a8e0c904c0a3429d834cc810039c226d1894f9a94341).
- [EROK MP-20 owner manual](https://erokmusic.com/download/manuals/MP-20.pdf) — 150 editable slots and initial fill; ten reorderable modules; CPU warning above90%, EQ overload; p12 QR links exact PD39 effects reference. (Direct 28-page manufacturer PDF; printed pp2/5/8/9/12; SHA256 da6460e6b7b2bf1e59eaba4b131d314a9d456ef02bc86912eebfa255e39cabdf).
- [MP-20 manual-linked PD39 Effects Description](https://manualf.oss-cn-hongkong.aliyuncs.com/manual/Combined-Effect-Pedals/PD39-Effects-Description.pdf) — Printed English p3 FX Pitch/Pitch shifter/Octave; Chinese pp34–35 Ice Stereo and Shimmer wet pitch; no input-polyphony or per-pitch DSP percentage. (Direct original 85-page PDF via manual QR; SHA256 65e8524534cc069166b79b6d98d2d7c2b4874ec85f1cae146dc927ec7cbc8977).
- [EROK file metadata](https://erokmusic.com/js/data-download-meta.js?v=10&rev=78d5cd5bb107c29f) — MP-20_086 file date October27 is not substituted for explicit October19 release. (Previously recovered direct inert JS; metadata differs from changelog).

<!-- firmware-pitch:EROK::MP-20 ends -->

<!-- model-images:EROK::MP-20 begins -->
<details>
<summary>Product pictures — top and rear ports</summary>

**MP-20 top-down manufacturer image with active display and light rings**

[![MP-20 top-down manufacturer image with active display and light rings](https://erokmusic.com/img/products/MP-20-1.webp?v=1d0e068e17648151)](https://erokmusic.com/img/products/MP-20-1.webp?v=1d0e068e17648151)

[Image source](https://erokmusic.com/product/multi-effects/MP-20). Official exact-model gallery. Display and teal footswitch rings appear active, but promotional compositing versus a photographed powered-on unit is not independently established. Screen CPU 80 is illustration, not a measured pitch cost.

**MP-20 straight-on rear connection panel**

[![MP-20 straight-on rear connection panel](https://erokmusic.com/img/products/MP-20-4.webp?v=c5bb39fd9e3a94b7)](https://erokmusic.com/img/products/MP-20-4.webp?v=c5bb39fd9e3a94b7)

[Image source](https://erokmusic.com/product/multi-effects/MP-20). Manufacturer gallery clearly labels MP-20, INPUT, MIDI, phones, L(MONO)/R OUTPUT, USB and power. This exact model view is separate from MK-20 regulatory photographs.

</details>
<!-- model-images:EROK::MP-20 ends -->


Checked2026-10-18; partial. Exact manufacturer MP-20 description and two exact Shopee titles establish guitar multi-effects identity. Bass/vocal membership and ownership remain unverified. A regulatory report now documents a limited MK-20/MP-20 hardware-family declaration, qualified below. Firmware/feature equivalence and MP-9 identity remain unverified; specifications are not transferred.

| Field | Evidence / qualification |
|---|---|
| Expression | Built-in, external and toe expression unverified. |
| Knobs / footswitches / buttons | Separate physical counts unverified; no panel visual audit. |
| Display | Technology, diagonal, color and touch unverified in readable primary text. Seller 2.4-inch LCD wording is not manufacturer verification. |
| Dimensions / mass | Unit dimensions, axis order and mass unverified. |
| Processing / choices | Manufacturer advertises **320+ effects and amp modeling**. Exact library/category counts, installed firmware, simultaneous ceiling and routing restrictions unverified. The headline is not a block count. [EMP] |
| Factory / user memory | Factory-filled, user, total and initial blank split unverified. |
| Synth / acoustic | Dedicated synthesis, electric-to-acoustic simulation and bass-specific library unverified. Seller instrument labels alone do not establish comparison membership. |
| I/O | Manufacturer identifies an **audio interface**; complete connectors, channel count, sample format, MIDI, phones and routing unverified. [EMP] |
| Power / battery / USB | Voltage, current, polarity, battery capacity/runtime, USB power and adapter/bundle unverified. Seller 8-hour title is not a primary power specification. |
| IR / NAM / capture | IR import, native NAM, converted NAM and proprietary capture unverified. Seller ANN wording does not establish NAM or its model architecture. |
| Editor / software | **Bluetooth control** advertised; exact application, editing scope, platforms, current OS, drivers/updaters and USB audio compatibility unverified. [EMP] |
| Looper / drums / live | **Looper and drum machine** advertised; duration, overdub/retention, synchronization, rhythm counts, scenes and trails unverified. [EMP] |

### Separate IDR hardware evidence

| Field | Evidence / qualification |
|---|---|
| IDR verified used | Unknown. |
| IDR verified new | Unknown. |
| IDR condition-unverified offer1 | **Rp1.850.000**, crossed Rp2.222.222/17% display; EROK MUSIC, shop1736925571/item40078512026. Direct JS-limited body and search both returned a month-old cache, checked2026-10-18. Region, condition, new/used, working state, selected variant, stock, adapter/bundle, warranty/import region, authenticity, voucher, shipping/tax and checkout total unverified. Stale 12–13 September delivery; late-arrival compensation is not a purchase discount. Seller name not independent authorization. [Exact item][EMS1] |
| IDR condition-unverified offer2 | **Rp1.850.000**, crossed Rp2.222.222/17%; M-VAVE Outlets, Kab.Tangerang, shop1659915296/item51311588226. Month-old search cache, checked2026-10-18; indexed variant display_model_id371006973353, but selected variant/bundle unverified. Condition, working state, stock, warranty, authenticity, shipping/tax, voucher andcheckout total unknown. Stale September delivery; cached ask not current stock or completed sale. [Exact indexed variant][EMS2] |

Manufacturer indexed home-page content is readable through search, but direct reopening currently exposes a dynamic shell. Its [downloads index][EMD] lists **MP-20 Manual PDF, 8.4 MB, 2026-06-22**; no original contents/direct PDF URL recovered. Listing date is not verified firmware/manual revision. No images visually audited, files/dependencies downloaded or software/device operated. MP-9’s manufacturer NAM/IR/USB claims are not assigned to MP-20.

[EMP]: https://erokmusic.com/index.html
[EMD]: https://erokmusic.com/download
[EMS1]: https://shopee.co.id/Prosesor-Efek-Multi-Gitar-EROK-MP-20-Pemodelan-ANN-320-Efek-LCD-2-4-Looper-Mesin-Drum-Baterai-8-Jam-untuk-Gitar-Elektrik-Bass-Akustik-i.1736925571.40078512026
[EMS2]: https://shopee.co.id/EROK-MP-20-Guitar-Multi-Effects-Processor-ANN-Modeling-320-Effects-2.4-LCD-Looper-Drum-Machine-8H-Battery-for-Electric-Bass-Acoustic-Guitars-i.1659915296.51311588226?extraParams=%7B%22display_model_id%22%3A371006973353%2C%22model_selection_logic%22%3A3%7D

### Regulatory family evidence and manual applicability

Checked2026-10-18. Original **Shenzhen Global Test Service report GTS20251010019-2-09**,issued2026-01-04,for Sinco/FCC ID **2ARCP-MK-20**,lists EROK among trademarks andMP-20/PD39 alongside testedMK-20. Printed p5 records the model declaration that PCB,structure andinternals match,with model name/color differences. This is regulatory-family evidence,not a retail-unit inspection orproof of identical firmware,algorithms,editor support ordisplay. [Original report reproduction](https://device.report/m/1159cb7090ae42be8e6d851424ddc20b6359f11203995bef73882c18188f9bab).

The associated [manufacturer-submitted user-manual exhibit9030673](https://fccid.io/2ARCP-MK-20/User-Manual/User-Manual-9030673) is indexed as27pages,submitted2026-01-28. The directlanding returned403;only indexed metadata is established. The separate Model Difference exhibit9030686 was identified,butits originalbody remains unread. Before applying MK-20 manual details toMP-20,match the original document/panel andrecord firmware/revision limits. No MK-20 technical specifications are imported bythis discovery. No files downloaded ordevices operated.

The original five-page **MK-20 external-photograph exhibit9030670**, dated2026-01-15 in the mirror index, is now browser-readable as an [original PDF](https://device.report/m/68b7c27e86a39899dd5f01e379ad324d3aee5425f1713460f6115b66555dcf53.pdf). Its extracted text identifies FCC2ARCP-MK-20 and figures1–10; it does not establish an MP-20 retail panel match. No control counts or connector labels are inferred from the text extraction. The model-difference letter and original manual PDF still returned cache misses through their actual index links. The cleaned HTML manual is a recovery lead, not a substitute for original-document/revision verification.

## Pocket Sonic

<!-- firmware-pitch:EROK::Pocket Sonic begins -->
### Firmware and pitch audit — EROK Pocket Sonic

| Field | Sourced finding |
|---|---|
| Firmware / first hardware release | Not verified. No dated first hardware release established. Earliest located VER007 December 30, 2025, regulatory dates and March 2026 manual metadata are not launch dates. [launch 1](https://erokmusic.com/product/multi-effects/POCKET-SONIC) [launch 2](https://erokmusic.com/download/manuals/POCKET-SONIC.pdf) |
| Firmware / latest verification | 105 — Latest verified. Current official catalogue selects PocketSonic_105.fwsc; explicit changelog dates VER105 October14. Adds Speaker Mode, native NAM A2, six MW FX choices, stereo DLY/MOD, DLY/REV tails and Input Gain; improves gate and Output Limit. Do not substitute download-file metadata for release date. [firmware 1](https://erokmusic.com/js/firmware-notes/en.json) [firmware 2](https://erokmusic.com/js/data-core.min.js?v=13&rev=61ae222d06935186) |
| Firmware / release date | 2026-10-14 (day precision) |
| Firmware / release-to-update duration | Not calculable from verified dates; observed release span, not continuous support or promised future updates. |
| Firmware / audit date | 2026-11-21; [firmware recap](../FIRMWARE-UPDATES.md). |
| Pitch / note handling | Pitch present; polyphony unverified. Manual Shimmer shifts reverb wet sound from unison to +2 octaves; Analog delay has wet detune Pitch control, cents unspecified. Vibrato is pitch modulation. Dedicated dry transpose, octave/harmony or WHAMMY not established in checked exact-model manual/changelog; input polyphony unverified. [pitch 1](https://erokmusic.com/download/manuals/POCKET-SONIC.pdf) [pitch 2](https://erokmusic.com/js/firmware-notes/en.json) [pitch 3](https://erokmusic.com/js/data-core.min.js?v=13&rev=61ae222d06935186) |
| Pitch / preset recall | Manual:80 writable locations, first40 factory-filled (40+40 table); current catalogue says36 presets. Firmware VER009 simplified presets to one group without a capacity figure. Current VER105 allocation unresolved; do not combine counts or add protected factory memory. |
| Pitch / DSP resources | Six reorderable modules FX/AMP/MOD/DLY/REV/CAB; manual advertises6+1 with gate combined into boost/compression. Shimmer uses the REV choice and Analog detune uses DLY. No per-pitch CPU percentage, measured configuration or verified combined wet-pitch ceiling. |
| Pitch / qualifications | Firmware changes alter library/routing: VER009 removed Speaker Mode/EQ; VER105 adds Speaker Mode again. Changelog does not establish restoration of EQ or the older preset layout. Stereo effects and bass models do not prove polyphonic pitch tracking. |
| Pitch / comparison | [Polyphony, presets and DSP recap](../PITCH-SHIFTING.md). |

Sources checked:

- [EROK exact Pocket Sonic product route](https://erokmusic.com/product/multi-effects/POCKET-SONIC) — Exact model identity; no dated hardware launch. (Manufacturer catalogue route, dynamic page).
- [EROK official Pocket Sonic firmware notes](https://erokmusic.com/js/firmware-notes/en.json) — VER105 October14,2026 features; older VER009 preset simplification; earliest located VER007 December30,2025 not launch proof. (Direct inert JSON; SHA256 df303b3d88967b04115e91708ad3bdcbe6023bc9278580caf5b0b2dd873d5cae).
- [EROK current product/download catalogue](https://erokmusic.com/js/data-core.min.js?v=13&rev=61ae222d06935186) — Current105 firmware/date; exact manual/gallery;36-preset headline conflicts with80-slot manual. (Direct inert manufacturer JS; SHA256 61ae222d069351869f49a8e0c904c0a3429d834cc810039c226d1894f9a94341).
- [EROK Pocket Sonic original manual](https://erokmusic.com/download/manuals/POCKET-SONIC.pdf) — 80 locations/40filled; six reorderable6+1 modules; Shimmer unison to+2octaves; Analog wet detune; no polyphony or CPU cost stated. (Direct16-page raster PDF; visually read printedpp1/5/7–9/12–14; SHA256 73fd7ebec56f475f94be66a732cfa1848d006d0f132a094af89b35b566dac204).

<!-- firmware-pitch:EROK::Pocket Sonic ends -->

Checked2026-10-18;partial. Manufacturer explicitly identifies a miniature **guitar multi-effects processor with headphone practice**. Exact Indonesian hardware title establishes a separate Pocket Sonic offer. Bass/vocal suitability andownership remain unverified. The regulatory hardware-family declaration below links Pocket Sonic with POCKET AMP;retail revision,firmware andfeature equivalence remain unverified. [Manufacturer](https://erokmusic.com/index.html).

| Field | Evidence / qualification |
|---|---|
| Expression | Built-in,external andtoe support unverified. |
| Knobs / footswitches / buttons | Separate counts unverified;no panel visual audit. |
| Display | Technology,diagonal,color andtouch unverified. |
| Dimensions / mass | Dimensions,axis order andweight unverified. |
| Processing / choices | Manufacturer multi-effects identity established;exact category/library counts,simultaneous ceiling androuting unverified. Seller60+/20amp/20IR claims are not primary verification. |
| Factory / user memory | Writable,protected,total andfactory-fill split unverified. |
| Synth / acoustic | Dedicated synthesis,acoustic conversion andbass-specific processing unverified. |
| I/O | Manufacturer describes headphone practice;connector sizes,complete ports,audio/MIDI channels androuting unverified. |
| Power / battery / USB | Voltage,current,polarity,battery capacity/runtime andUSB power unverified. Seller rechargeable wording is not a primary power specification. |
| IR / NAM / capture | IR import,native/converted NAM andproprietary capture unverified. Seller tone-cloning title does not establish a capture format. |
| Editor / software | Application,platforms,OS,driver/updater andmobile recording support unverified. |
| Looper / drums / live | Looper,drums,scenes,trails andpractical routing unverified. |
| Documentation | Official downloads index lists **Pocket Sonic Manual PDF19.7MB,2026-06-22**;original contents/URL unrecovered. Date is an index label,not verified firmware revision. [Downloads](https://erokmusic.com/download) |

### Separate IDR hardware evidence

| Field | Evidence / qualification |
|---|---|
| IDR verified used | Unknown. |
| IDR verified new | Unknown. |
| IDR condition-unverified offer | **Rp790.000**,crossedRp888.888/11%;M-VAVE Outlets,Kab.Tangerang,shop1659915296/item54211588203. Checked2026-10-18,three-day indexed cache;direct base item cache miss. Indexed variant341006932698 not verified. Condition,working state,current stock,revision,bundle/charger,warranty/import region,authenticity,voucher,shipping/tax andcheckout total unknown. October16–18 delivery is cached,not live stock;late-arrival compensation is not an immediate discount. [Exact indexed item](https://shopee.co.id/EROK-Pocket-Sonic-Mini-Multi-Effects-Pedal-60-Built-in-Effects-20-Amp-Modeling-with-Tone-Cloning-20-IR-Cabinets-OTG-Recording-Rechargeable-with-Clip-On-Design-i.1659915296.54211588203?extraParams=%7B%22display_model_id%22%3A341006932698%2C%22model_selection_logic%22%3A3%7D) |

No files/dependencies downloaded orsoftware/devices operated. No sibling specifications transferred.

### Pocket Sonic — regulatory hardware-family boundary

Checked2026-10-18 against original **GTSL2025110472F02**,issued2025-12-30,printed pp1,5,for Sinco/FCC **2ARCP-POCKETAMP**,read via [original report text reproduction](https://device.report/m/27368ee6f8b6b150b2426ccb840f90c7816bdf8895ca48525e94d94e315eda79). EROK appears among the listed trademarks.

| Field | Evidence / qualification |
|---|---|
| Processing / hardware-family applicability | Applicant declares **POCKET AMP,SK17,Pocket Sonic,PIXIE1** share PCB layout,interior andelectrical circuits,with name/color differences. This is regulatory-family evidence,not proof that the offered retail unit has identical effect libraries,editor support orfirmware. No cross-flashing recommended orperformed. |
| Power / regulatory sample | Tested model is **POCKET AMP**,engineering sample **GTSL2025110472-1**,hardware **V08E1**,software **V05**. Report lists **5.0VDC adapter or3.7VDC lithium battery** for that sample. It does not verify Pocket Sonic retail connector,current,capacity,runtime orUSB-power behavior;those remain unresolved. |

This qualifies the previous identity uncertainty without merging records ortransferring Pocket Amp manual specifications. Original Pocket Sonic manual remains unread. No downloads ordevice/software operation.

### Pocket Sonic — expression audit identity hold

Checked **2026-10-28**. [Own manufacturer catalogue](https://erokmusic.com/) confirms Pocket Sonic guitar multi-effects andheadphone practice. [Manual index](https://erokmusic.com/index.html) lists Pocket Sonic PDF19.7MB,2026-06-22;the current[download route](https://erokmusic.com/download) returns only site controls without the file URL. No manual contents newly inspected.

**No-treadle eligibility,analog EXP presence,global volume,footprint,headphone connector andonboard preset down/up remain unverified.** Keep this existing active model in the pending-screen inventory,not among confirmed no-treadle matches. Regulatory hardware-family evidence above is not retail firmware/feature equivalence;do not inherit Pocket Amp connectors,dimensions orassignment behavior. Volume position,min/max,recall,bypass/headphone/tail/loop coverage all remain unknown. Exact manual recovery is the next technical action;older offer andsource qualifications remain intact. No downloads ordevice operation.
