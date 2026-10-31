# RJM Music — display controllers

[Display collection](FOOTSWITCH-DISPLAYS.md) · [Repository](README.md)

## Mastermind GT/10

Checked 2026-10-31 against the [exact GT/10 manufacturer page](https://rjmmusic.com/products/mastermind-gt-10-midi-foot-controller). Controller only, outside active audio counts.

| Field | Evidence / qualification |
|---|---|
| Displays / memory | **Ten individual LCDs, one above each switch**, plus separate main LCD. **768 presets,16 button pages**; pages are not extra screens. Diagonal, resolution and touch remain unverified. |
| Power | **12VDC/800mA, center-positive, 2.1mm ID/5.5mm OD** published requirement; MIDI phantom powering also documented. Not GT/22’s1.6A requirement; measured draw unknown. |
| Ports / expression | Four TRS EXP inputs, linear/log, current page says wiper-to-tip but manual4.1 says wiper-to-ring (see below); two TRS momentary-switch inputs supporting four switches;7-pin MIDI IN/OUT;USB-A storage/USB-B computer. Page mentions phantom power through XLR but omits XLR from its GT/10 connector list: unresolved wording,not a confirmed XLR socket. |
| Body / software | Published **19.4W×8.1D×3.25H inches,6lb/2.7kg**; corroborated by manual4.1 below; current revision equivalence unverified. PC/Mac editor; minimum OS unknown. |
| Remaining | Complete revision/profile and exact Shopee used/new IDR,condition,stock,bundle and warranty unverified. |

No download, installation or hardware operation.

### GT/10 — MIDI limits and mislabeled manual link

Checked 2026-10-31. The [exact GT/10 page](https://rjmmusic.com/products/mastermind-gt-10-midi-foot-controller) specifies **16 connected devices**: one preset-button tap can send a program change to all 16; an IA button can send **up to 20 messages**, combining CC, PC and Note. These are MIDI-control limits, not simultaneous audio effects. It also lists **two auxiliary 9VDC outlets**; the product page omits their available current and polarity; manual4.1 qualifications appear below. USB-thumb-drive settings backup/restore and onboard editing are documented; USB audio or bus powering is not established.

The [manufacturer GT comparison page](https://rjmmusic.com/pages/mastermind-gt-10-16-22) labels its product-manual link “Mastermind GT Manual”, but that link currently resolves to [PBC6X Manual-4.2.pdf](https://docs.rjmmusic.com/download-content/PBC6X/PBC6X%20Manual-4.2.pdf), whose internal text identifies Mastermind PBC, version4.2, dated2019-04-07. **This is a mismatched model document and is not used for GT/10 specifications.** The older GT4.1 link is retained above; it was inaccessible on this pass. Current GT/10 manual corroboration, the XLR wording conflict, display dimensions and exact Shopee Indonesia offers remain unresolved. No file downloaded or hardware operated.

### GT/10 — recovered manufacturer manual, revision4.1

The [manufacturer GT manual](https://docs.rjmmusic.com/download-content/MMGT/Mastermind%20GT%20Manual-4.1.pdf), version4.1 dated2018-09-11, explicitly includes GT/10. Printedpp2,4,59,72 establish:

- Ten footswitches plus **two setup soft buttons**; button LCDs have **RGB backlighting**, which does not establish full-color pixel graphics. Brightness/contrast adjustment is documented; numeric ranges remain unknown.
- GT/10 dimensions and mass corroborate the existing product figures. Its **700mA** rating differs from the current page’s **800mA**; generic rear-panel text separately requests a supply rated at least2A. These are revision-qualified statements, not measured draw.
- Auxiliary outputs: **9VDC, center-negative,100mA total shared**, not100mA each.
- XLR connectors are explicitly **GT/22-only** in this revision, conflicting with the current GT/10 phantom-power wording. No current hardware inspection resolves that discrepancy.

This restores historical manual corroboration; it does not certify current firmware/hardware equivalence or resolve display diagonal, touch, exact Indonesian offers or global audio-volume coverage. Earlier inaccessible and mislabeled links remain preserved.

### GT/10 — expression wiring conflict and MIDI scope

[Manual4.1](https://docs.rjmmusic.com/download-content/MMGT/Mastermind%20GT%20Manual-4.1.pdf), printedpp39–40,68–69, describes **TRS wiper-to-ring**, conflicting with the current product page’s **wiper-to-tip**. It describes swapping tip/ring for Roland/BOSS-type pedals. Revision or documentation error remains unresolved; neither wiring is certified for current hardware here.

The controller converts pedal position to MIDI CC. Global settings select destination, CC and heel/toe values; presets can override them. A second CC destination is available. **SndOnPrst** sends current CC values on preset changes; this is distinct from target assignment. Calibration is also separate. These controller functions do not establish the receiving processor’s all-preset volume, headphone, bypass, tail or looper coverage, or make this a direct analog audio-volume processor.

Exact GT/10 Shopee Indonesia searches on2026-10-31 returned no indexed hardware item; used/new IDR, seller, stock and bundle remain unknown. No wiring or hardware test performed.

### GT/10 — editor versions and macOS requirements

Checked **2026-10-31**. Manufacturer [version history](https://docs.rjmmusic.com/books/other-mastermind-information/page/mastermind-version-history-log) covers Mastermind GT;this updates the GT/10 software gap without transferring PBC/LT-only releases.

| Field | Manufacturer documentation / qualification |
|---|---|
| Editor /5.5 compatibility | **5.5.0+ requires macOS12 Monterey orlater**,following a development-environment change that enables universal Mac binaries. This supersedes older Mac minimums for that release family;no local Intel/Apple-silicon test performed. |
| Editor / model-specific version | History says **5.5.1 fixes only PBC/LT editor UI**;GT editor andGT/LT/PBC firmware should remain **5.5.0**. No release date is supplied in that section;installed versions unknown. |
| Editor / historical requirements | [Online editor manual](https://docs.rjmmusic.com/books/mastermind-editor-manual) explicitly reflects **5.2.x**. Its [requirements](https://docs.rjmmusic.com/books/mastermind-editor-manual/page/system-requirements) list Windows7+32/64-bit ormacOS10.13+64-bit,2GBRAM andUSB-B connection. Do not certify current5.5 Windows architectures from that older manual. |

[Downloads guidance](https://rjmmusic.com/pages/downloads) requires firmware/editor first-two-version-digits to match;patch digits may differ. Generic iPad-app wording is only for supported products anddoesnot establish GT/10 iPad editing. No download,installation ordevice operation.

## Mastermind GT/16

Checked 2026-10-31 against the [exact manufacturer page](https://rjmmusic.com/products/mastermind-gt-16-midi-foot-controller). Controller only, outside active audio counts.

| Field | Evidence / qualification |
|---|---|
| Displays | **16 individual LCDs, one above each switch**, plus main LCD. Diagonal, resolution and touch unknown. |
| Power / body | **12VDC/1.2A, center-positive, 2.1mm ID/5.5mm OD**; MIDI-output phantom powering. **19.4W×11.1D×3.25H inches /49.3×28.2×8.3cm;8lb/3.6kg**. Ratings, not measured draw. |
| Connections | Four TRS EXP inputs, linear/log, high/low impedance; two TRS momentary-switch sockets supporting four switches;7-pin MIDI IN/OUT;USB-A storage/USB-B computer;two9VDC auxiliary outputs. Exact EXP wiper wiring unverified. |
| Memory / software | Product384 presets versus [Manual4.1](https://newsite.rjmmusic.com/download-content/MMGT/Mastermind%20GT%20Manual-4.1.pdf)768: revision conflict retained.16 button pages;Mac/PC editor, minimum OS unknown. |
| Remaining | Complete current profile and exact Shopee Indonesia condition, stock, bundle and used/new IDR evidence pending. No sibling specifications substituted. |

### GT/16 — revision-qualified LCD controls and power

Checked2026-10-31 against [manufacturer Manual4.1,2018-09-11](https://docs.rjmmusic.com/download-content/MMGT/Mastermind%20GT%20Manual-4.1.pdf), printedpp1–7,72. It explicitly covers GT/16:

- **16 footswitches plus two setup soft buttons**. Individual graphic LCDs have RGB backlights; full-color pixel rendering, diagonal, resolution and touch remain unverified.
- Default five-preset banks: Bank± previews labels; a preset press confirms the change. This is configurable bank navigation, not an immutable sequential preset± pair. IA Mode can expose15 IA switches.
- GT/16 body/mass corroborate the product figures. Manual **12VDC/1.0A** differs from current **1.2A**; generic supply guidance separately requests at least2A. No measured draw or hardware-revision explanation.
- Two accessory outputs share **100mA total**,9VDC center-negative. Manual XLR sockets are GT/22-only; no GT/16 XLR inferred.
- USB-B presents a MIDI interface; this does not establish audio or bus power. Historical768-preset versus product384 conflict remains.

The [exact GT/16 product page](https://rjmmusic.com/products/mastermind-gt-16-midi-foot-controller) additionally specifies16 connected devices, one-tap PC transmission to all16 and IA sequences of up to20 CC/PC/Note messages. These are MIDI limits, not audio-effect capacity. Page says sold out; that is manufacturer-store status, not Indonesian availability. Exact Shopee GT16/GT/16 searches returned no indexed hardware item on this pass. Used/new IDR, seller, condition, bundle and local stock remain unverified. No download or hardware test.

## Mastermind GT/22

Checked 2026-10-31 against the [exact manufacturer page](https://rjmmusic.com/products/mastermind-gt-22-midi-foot-controller). MIDI controller, outside active audio processor/brand counts. GT/10 and GT/16 specifications are not substituted.

| Field | Evidence / qualification |
|---|---|
| Displays | **22 LCDs, one above every footswitch**, plus separate main LCD. Diagonals, resolution and touch remain unknown. |
| Power / body | **12VDC, 1.6A, center-positive, 2.1mm ID/5.5mm OD**; phantom power via MIDI also documented. **19.4W×14.1D×3.25H inches /49.3×35.8×8.3cm; 10lb/4.5kg**. No USB-power inference. |
| Connections / editor | Four TRS EXP inputs, two TRS external-switch sockets supporting four momentary switches, 7-pin DIN MIDI IN/OUT, 6-pin XLR MIDI, USB-A storage and USB-B computer. Mac/PC editor; minimum OS pending. |
| Memory conflict | Product lists384 presets; [manufacturer Manual4.1](https://newsite.rjmmusic.com/download-content/MMGT/Mastermind%20GT%20Manual-4.1.pdf) introduction says768. Keep revision conflict; neither is a count of screens. |
| Remaining | Full current firmware/profile and exact Shopee Indonesia used/new hardware prices, condition, stock and bundles pending. |

No download, purchase, software installation or device test.

### GT/22 — historical controls and XLR power boundaries

[Manufacturer Manual4.1](https://docs.rjmmusic.com/download-content/MMGT/Mastermind%20GT%20Manual-4.1.pdf), dated2018-09-11, explicitly covers GT/22 (printedpp1–7,72–73):

- **22 footswitches plus two setup soft buttons**; individual LCDs have RGB backlighting, not verified full-color pixel graphics. IA Mode can expose21 IA switches. Default six-preset banks preview before preset confirmation; this is configurable navigation.
- Body/mass corroborate the product figures. Manual **12VDC/1.5A** differs from current **1.6A**; generic supply guidance requests at least2A. Revision explanation and measured draw remain unknown.
- Male6-pin XLR MIDI OUT and female6-pin XLR Remote IN are parallel to DIN; manual says use only one connector set at a time. Phantom input uses DIN OUT pins6/7 or XLR OUT pins1/2. Manual prohibits simultaneous phantom and adapter power.
- Two accessory outputs share **100mA total**,9VDC center-negative. These outputs differ from the center-positive main input.

The [exact product page](https://rjmmusic.com/products/mastermind-gt-22-midi-foot-controller) specifies16 connected devices and up to20 CC/PC/Note messages per IA button. These MIDI limits do not imply audio processing. Historical768 versus current-page384 presets remains unresolved. Exact Shopee GT22/GT/22 queries returned no indexed hardware item on2026-10-31; no IDR, condition, stock or bundle claim added. Display dimensions/touch, current firmware equivalence and processor-side volume coverage remain unverified. No download or hardware test.
