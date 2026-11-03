# HeadRush multi-effects

<!-- brand-index begins -->
**Model and section index — A–Z, natural numeric order**

- [Core](#core)
- [Flex Prime](#flex-prime)
- [Gigboard](#gigboard)
- [MX5](#mx5)
- [Pedalboard](#pedalboard)
- [Prime](#prime)
- [VX5](#vx5)
<!-- brand-index ends -->

## Core

**Technical and original price observations:2026-10-14.** Guitar/bass/vocal multi-effects; **large**, no built-in expression. This is Core, not Prime, Flex Prime, MX5 or Gigboard. Partial record, not independently tested. The complete earlier Core finding is consolidated here; its stale next-model instruction is superseded by the root ledger and current exclusions.

<!-- comparison evidence begins -->
### Core hardware and required fields

| Field | Finding | Evidence |
|---|---|---|
| Expression | **No built-in pedal**; external6.35 mm TRS EXP and separate TS TOE input | [Core FAQ][core-faq] |
| Controls | **5 footswitches**; current specification lists **3 front rotary controls**: main,headphones,navigation encoder. Complete rotary/button inventory including rear controls **?**; encoder press not double-counted | [Core product][core-product] |
| Display | **One7-inch full-color touchscreen**; no Prime-style auxiliary OLED strips | [Core product][core-product], [Core FAQ][core-faq] |
| W×D×H / mass | **408.4×234.6×67.0 mm;3.80 kg**; installed cable clearance additional | [Core product][core-product] |
| Power | **12 V DC,3 A,center-positive adapter input** in technical specifications; FAQ instead says IEC, unresolved documentation conflict. Battery/USB-powered operation **not established** | [Core product][core-product], [Core FAQ][core-faq] |
| Presets | FAQ states **50 supplied factory rigs**; current firmware factory total and maximum user storage **?** | [Core FAQ][core-faq] |
| Processing | **14 rig blocks**, subject to routing/DSP/model limits; guitar/vocal paths supported. Not14 physical footswitches | [Core FAQ][core-faq] |
| Synth | **Yes**: Hybrid Synth,Electric Piano,DB-33 Organ; website Synth heading also includes Ambi-Verb | [Core model list][core-product], [firmware][core-fw] |
| Acoustic simulation | **Yes: Acoustic Sim**; separate Acoustic Pre is not the same effect | [Core model list][core-product] |
| IR loading | **Yes**, third-party WAV/AIFF; FAQ specifies up to192 kHz/32-bit files and two IRs per block. Storage/sample-length limit **?** | [Core FAQ][core-faq] |
| NAM | **Native,architecture-qualified**; see firmware section below | [Release notes][core-fw], [Cloud formats][core-cloud] |
| Other captures | Onboard amp/pedal cloning; proprietary HeadRush/ReValver clones and SuperClones, separate from NAM | [Core product][core-product] |
| Editor | Wi-Fi **browser editor Windows/macOS/iOS/Android**; Linux not established. Windows/macOS firmware updaters and USB file transfer are separate functions | [Release notes,p.7][core-fw] |
| USB audio | **6-in/4-out**,24-bit44.1/48/96 kHz; recording/reamping; Windows driver,macOS driverless | [Core FAQ][core-faq] |
| Live features | Scenes,trails; looper **50 layers,5 minutes/layer,20 minutes total per loop**; drum machine | [Core FAQ][core-faq], [Core product][core-product] |

| Required field | Model-specific qualification |
|---|---|
| Mic routing / live | [Core FAQ][core-faq],rechecked2026-10-17: guitar-centric Straight/Middle Split/Immediate Split paths do not permit the normal vocal-FX chain. **Mic Dry Out** instead has gate,compression,high-pass and simpleEQ adjustments; retaining14 guitar blocks is not14 additional vocal blocks. |
| Capture loading limitations | Current [Core FAQ][core-faq] excludes time-based flanger,chorus and delay cloning; certain gated fuzzes cannot be cloned,and some high-impedance vintage fuzzes need a reamp box. These are onboard cloner limits,not a statement that Core cannot play delay effects or native NAM. |
| MIDI control / data | FAQ documents Program Change,Control Change andClock via DIN andUSB-A,including block/switch control and tempo synchronization. USB-B is not inferred to expose every USB-A MIDI function. [Core FAQ][core-faq] |

### Core connections

Manufacturer evidence lists6.35 mm TS guitar input; XLR/6.35 mm combo mic input with switchable **48 V phantom**; stereo pairs of XLR and6.35 mm main outputs;3.5 mm headphones and aux; stereo TRS FX send/return; EXP and separate TOE; TRS amplifier-control output; DIN MIDI IN/OUT; USB-A storage/MIDI and USB-B computer; Wi-Fi and Bluetooth audio. [Core product][core-product], [Core FAQ][core-faq].

The published port bullets incorrectly call SEND an input and RETURN an output. Functional directions are corrected here rather than copying the reversal. Obtain the matching Core manual/rear-label confirmation before treating the port/power list as fully reconciled. The IEC/DC conflict is not silently resolved by borrowing another HeadRush model.

### Core firmware and category-count evidence

**Firmware5.2.0,October2026** appears on printedp.1 of the official release notes, visually checked in the original research. Its p.3 specifies **two A2 Full captures or four A2 Lite captures across two NAM blocks**, running natively. Version5.1 introduced A1 Standard/Lite/Feather/Nano and A2 support; do not generalize A2 concurrency limits to every A1 architecture. [Release notes][core-fw], [Cloud][core-cloud].

The website headings advertise HeadRush amps53; ReValver amps44; HeadRush cabs15/mics10; ReValver cabs67/mics31; vocal7; drive16; distortion/fuzz11; EQ9; compressor6; delay14; reverb7; chorus7; phaser/flanger10; vibrato/tremolo/rotary6; wah/filter8; synth4; rhythmic2; pitch7; volume/dynamics5; utility3. **These are website-heading figures,not a verified firmware5.2 installed total.** [Model list][core-product].

Conflicts prevent a definitive sum: drive lists **18 entries under16**; pitch shows **8 entries under7**, with duplicate/truncated names; later EQ heading differs;5.1 added an amp and Graphic Bass EQ not consistently reflected. Reconciliation remains pending. The seven named vocal choices include correction,de-essing,distortion,doubling,harmony,stutter,vocoder; they are not seven extra independent microphone-routing blocks.

### Core IDR evidence and original source limitations

| Class | Amount | Evidence |
|---|---:|---|
| Retail hardware listing; detailed condition/stock not established | **Rp15.120.000** | [ROCKPIZZ MUSIC,shop440477624/item44463652142](https://shopee.co.id/HEADRUSH-CORE-GUITAR-MULTI-EFFECT-AMP-MODELER-VOCAL-PROCESSOR-i.440477624.44463652142) |
| Condition-verified used offer | **?** | No independently verified used offer in the original pass |

Original fetched listing identifies actual hardware and displayed price, but JavaScript-limited body does not establish accessories,warranty,selected variant or checkout stock. Delivery/voucher text is not an applied discount. One ask is not a market range or completed sale. This amount was not refreshed merely by consolidating the record.

Original gaps: full controls,power-label/manual consistency,current factory/user capacity,installed category totals and used offers. The download index linked a5.2 user guide but it **could not be fetched and was not read**. Accessible release notes/product/FAQ supplied the evidence. No new visual/manual verification is claimed by this merge.

[core-product]: https://www.headrushfx.com/products/core/index.html
[core-faq]: https://support.headrushfx.com/en/support/solutions/articles/69000844379-headrush-core-frequently-asked-questions
[core-fw]: https://cdn.inmusicbrands.com/Software/SGEE/52/READ%20ME%20-%20HeadRush%20Core%20Firmware%20Update%20Instructions%20v5.2.0.pdf
[core-cloud]: https://www.headrushfx.com/cloud/index.html

<!-- comparison evidence ends -->

### Core — complete dated original finding

The2026-10-17 FAQ follow-up adds the mic-path,cloner andMIDI qualifications above. The full2026-10-14 finding below retains its original observations and access limits under a reversible whole-body check. Its stale next-model instruction is historical only;FV01 remains excluded. The matching5.2 guide is still not claimed read,physical control totals andpower contradiction remain open,and no owner/device/stock verification is implied. No source removed.

<!-- HEADRUSH-CORE source begins -->

Checked **2026-10-14**. **Partial record**, not independently tested. Guitar/bass/vocal multi-effects; **large**, no built-in expression. This is Core, not Prime, Flex Prime, MX5 or Gigboard. Next queued model: **Flamma FV01**.

### IDR listing evidence

| Condition | Asking price | Evidence |
|---|---:|---|
| Retail listing; detailed condition/stock not established | **Rp15.120.000** | [ROCKPIZZ MUSIC, Shopee item 44463652142, shop 440477624](https://shopee.co.id/HEADRUSH-CORE-GUITAR-MULTI-EFFECT-AMP-MODELER-VOCAL-PROCESSOR-i.440477624.44463652142) |
| Used | **?** | No independently verified used offer in this pass |

The fetched listing identifies actual Core hardware and the displayed price, but its JavaScript-limited body does not establish accessories, warranty, selected variant or checkout stock. Delivery/voucher text is not a discount applied to this price. This is one asking-price observation, not a used-to-new market range or completed sale.

### Hardware and required fields

| Field | Finding | Evidence |
|---|---|---|
| Expression | **No built-in pedal**; external 6.35 mm TRS EXP and separate TS TOE input | [FAQ][HEADRUSH-CORE-faq] |
| Controls | **5 footswitches**; current specification lists **3 front rotary controls** (main, headphones, navigation encoder). Complete rotary/button inventory including rear controls **?**; encoder press not double-counted | [Product technical specifications][HEADRUSH-CORE-product] |
| Display | **One 7-inch full-color touchscreen**; no Prime-style auxiliary OLED strips | [Product][HEADRUSH-CORE-product], [FAQ][HEADRUSH-CORE-faq] |
| W × D × H | **408.4 × 234.6 × 67.0 mm**; **3.80 kg** | [Product][HEADRUSH-CORE-product] |
| Power | **12 V DC, 3 A, center-positive adapter input** in current technical specifications; FAQ instead says IEC, an unresolved documentation error/conflict. Battery/USB-powered operation **not established** | [Product][HEADRUSH-CORE-product], [FAQ][HEADRUSH-CORE-faq] |
| Presets | FAQ states **50 supplied factory rigs**; current firmware factory total and maximum user storage **?** | [FAQ][HEADRUSH-CORE-faq] |
| Processing | **14 rig blocks**, subject to routing/DSP/model limits; guitar/vocal paths supported. These are not 14 physical footswitches | [FAQ][HEADRUSH-CORE-faq] |
| Synth | **Yes**: Hybrid Synth, Electric Piano and DB-33 Organ; website Synth heading also includes Ambi-Verb | [Product model list][HEADRUSH-CORE-product], [firmware history][HEADRUSH-CORE-fw] |
| Acoustic simulation | **Yes**, Acoustic Sim; separate Acoustic Pre is not the same effect | [Product model list][HEADRUSH-CORE-product] |
| IR loading | **Yes**, third-party WAV/AIFF; FAQ specifies up to 192 kHz/32-bit files and two IRs per block. Storage/sample-length limit **?** | [FAQ][HEADRUSH-CORE-faq] |
| NAM | **Native**, architecture-qualified; details below | [5.2 release notes][HEADRUSH-CORE-fw], [Cloud formats][HEADRUSH-CORE-cloud] |
| Other captures | Onboard amp/pedal cloning; proprietary HeadRush/ReValver clones and SuperClones, separate from NAM | [Product][HEADRUSH-CORE-product] |
| Editor | Wi-Fi **browser editor: Windows/macOS/iOS/Android** documented; Linux not established. Windows/macOS firmware updaters and USB file transfer are separate functions | [Release notes, printed p.7][HEADRUSH-CORE-fw] |
| USB audio | **6-in/4-out**, 24-bit 44.1/48/96 kHz; recording/reamping; Windows driver, macOS driverless | [FAQ][HEADRUSH-CORE-faq] |
| Live features | Scenes, trails; looper **50 layers, 5 minutes/layer, 20 minutes total per loop**; drum machine | [FAQ][HEADRUSH-CORE-faq], [Product][HEADRUSH-CORE-product] |

### Connections

Manufacturer evidence lists: 6.35 mm TS guitar input; XLR/6.35 mm combo mic input with switchable **48 V phantom**; stereo pairs of XLR and 6.35 mm main outputs; 3.5 mm headphones and aux; stereo TRS FX send/return; EXP and separate TOE; TRS amplifier-control output; DIN MIDI IN/OUT; USB-A storage/MIDI and USB-B computer; Wi-Fi and Bluetooth audio. [Product][HEADRUSH-CORE-product], [FAQ][HEADRUSH-CORE-faq].

The published port bullets incorrectly call SEND an input and RETURN an output. They are retained here with their functional directions corrected, rather than copying the reversal. FAQ also conflicts with the product's DC power description. Obtain the matching Core manual/rear-label confirmation before treating the port/power list as a fully reconciled hardware specification.

### Firmware and category-count evidence

**Firmware 5.2.0, October 2026** is identified on printed p.1 of the official release notes, visually checked. Its p.3 specifies **two A2 Full captures or four A2 Lite captures across two NAM blocks**, running natively. Version 5.1 introduced A1 Standard/Lite/Feather/Nano and A2 support; do not generalize the new A2 concurrency limits to every A1 architecture. The cloud page independently lists supported formats. [Release notes][HEADRUSH-CORE-fw], [Cloud][HEADRUSH-CORE-cloud].

The website's category headings advertise: HeadRush amps53; ReValver amps44; HeadRush cabs15/mics10; ReValver cabs67/mics31; vocal7; drive16; distortion/fuzz11; EQ9; compressor6; delay14; reverb7; chorus7; phaser/flanger10; vibrato/tremolo/rotary6; wah/filter8; synth4; rhythmic2; pitch7; volume/dynamics5; utility3. **These are website-heading figures, not a verified firmware-5.2 installed total.** [Model list][HEADRUSH-CORE-product].

Conflicts prevent summing a definitive grand total: the drive list has **18 entries under a 16 heading**; pitch shows **8 entries under a 7 heading**, including duplicate/truncated names; later detailed EQ heading differs; 5.1 added an amp and Graphic Bass EQ not reflected consistently in the page. Per-category firmware reconciliation remains pending. The seven named vocal choices include correction, de-essing, distortion, doubling, harmony, stutter and vocoder. Do not count microphone routing utilities as seven extra independent blocks.

### Resume gaps

Confirm complete physical controls, actual power-label/manual consistency, current factory/user storage, installed category totals and used offers. The download index links a 5.2 user guide, but it could not be fetched in this pass; **the guide was not read**. The accessible 5.2 release notes and current Core page were used instead. No arbitrary sibling-model values fill these gaps.

[HEADRUSH-CORE-product]: https://www.headrushfx.com/products/core/index.html
[HEADRUSH-CORE-faq]: https://support.headrushfx.com/en/support/solutions/articles/69000844379-headrush-core-frequently-asked-questions
[HEADRUSH-CORE-fw]: https://cdn.inmusicbrands.com/Software/SGEE/52/READ%20ME%20-%20HeadRush%20Core%20Firmware%20Update%20Instructions%20v5.2.0.pdf
[HEADRUSH-CORE-cloud]: https://www.headrushfx.com/cloud/index.html
<!-- HEADRUSH-CORE source ends -->

### Preserved third Shopee expansion shared comparison

Historical2026-10-14 source wording. Current firmware-qualified findings retain precedence. Offers,old classifications and unknowns preserve their original context;this is not a new stock/specification verification.

- **Instrument / size class** (No built-in expression): Guitar/bass/vocal / **large**
- **External expression** (No built-in expression): TRS EXP plus separate TOE input
- **K/F/B** (No built-in expression): **3 front rotary documented /5/?**; complete rotary inventory including rear controls ?
- **W×D×H, mm; weight** (No built-in expression): **408.4×234.6×67**; **3.80 kg**
- **Screen diagonal** (2. Screens): **7 inches**
- **Monochrome / color** (2. Screens): **Color**
- **Evidence limitation** (2. Screens): Core-specific manufacturer specification; not Prime's auxiliary OLED layout
- **New / retail IDR evidence** (3. Separate IDR price evidence): **Rp15.120.000**, ROCKPIZZ MUSIC
- **Availability and condition qualification** (3. Separate IDR price evidence): Actual hardware listing; detailed condition, accessories and checkout stock unverified
- **Blocks / categories / choices** (4. Processing, presets and model loading): **14 rig blocks**, routing/DSP-limited; guitar/vocal paths. Website category totals conflict with their own lists and later firmware; see finding, do not sum a definitive grand total
- **Preset storage** (4. Processing, presets and model loading): FAQ **50 factory rigs**; current factory/user capacity ?
- **Synth / acoustic simulator** (4. Processing, presets and model loading): **Synth yes**: Hybrid Synth, Electric Piano, DB-33; **Acoustic Sim yes**
- **IR / NAM / captures** (4. Processing, presets and model loading): Third-party WAV/AIFF IRs; **native NAM**, architecture-qualified; proprietary HeadRush/ReValver clones and SuperClones separate
- **Audio/control connections** (5. Connections, power, software and live use): Guitar input; combo XLR/¼″ mic with **48 V**; stereo XLR and ¼″ outputs; 3.5 mm phones/aux; stereo TRS loop; EXP/TOE/amp-control; DIN MIDI I/O; USB-A/B; Wi-Fi/Bluetooth audio
- **Power / battery / USB operation** (5. Connections, power, software and live use): Current specs **12 V/3 A center-positive**, but FAQ says IEC: **conflict unresolved**. Battery/USB power not established
- **Configuration and recording** (5. Connections, power, software and live use): Wi-Fi browser editor **Windows/macOS/iOS/Android**; USB **6-in/4-out**, 24-bit 44.1/48/96 kHz; reamp
- **Additional features** (5. Connections, power, software and live use): Scenes, trails, drums; looper **50 layers, 5 min/layer, 20 min total**
- **Individually saved findings commit** (6. Evidence gaps and immediate commits): `369f2c15423a1c83340a5c39cdd16c01dfe27d82`

[Original shared source](../research-state.json)<!-- historical-link:headrush-001 -->,retained pending complete navigation/provenance audits.

### Core — expression-volume audit, 2026-10-19

**Per-rig documented assignment;5.2 override unverified.** Indexed [official5.0 guide](https://cdn.inmusicbrands.com/Software/SGEE/5/HeadRush%20Core%20-%20User%20Guide%20-%20v5.0.0.pdf), sections4.6/4.5.4, says Hardware Assign belongs to the rig. **Hybrid FS1 previous/FS5 next** is explicit. [Current5.2 guide](https://cdn.inmusicbrands.com/Software/SGEE/52/HeadRush%20Core%20-%20User%20Guide%20-%20v5.2.0.pdf) failed web retrieval at12.47MB;not read ordownloaded locally. No5.2 across-rig guarantee inferred.

[Manufacturer volume/wah instructions](https://support.headrushfx.com/en/support/solutions/articles/69000856609-headrush-switching-between-volume-and-wah) explicitly includeCore: insert blocks,assignClassicA/B,save. Selectingwah deactivatesvolume. [Own4.0 global EXP chapter](https://cdn.inmusicbrands.com/HeadRush/FW/4/Finalized%20User%20Guides/HeadRush%20Core%20-%20User%20Guide%20-%20v4.0.0.pdf),indexedsection4.20.7,configures toe type/polarity,not globalvolume target. Placement,min/max,held-position recall,bypass,headphone,tail/recorded-loop coverage remain unverified.

[Exact Core product](https://www.headrushfx.com/products/core/) rechecked:408.4×234.6mm exceeds preference;TRS EXP,separateTS TOE,3.5mm phones. [ROCKPIZZ shop440477624/item44463652142](https://shopee.co.id/HEADRUSH-CORE-GUITAR-MULTI-EFFECT-AMP-MODELER-VOCAL-PROCESSOR-i.440477624.44463652142) rechecked2026-10-19:cached **Rp15.120.000**,17–20October delivery text. Condition,bundle,adapter,warranty,shipping,currentcheckoutstock andused offer unresolved. Voucher compensation not deducted. No hardware test ordependency/software download.

## Flex Prime

<!-- comparison evidence begins -->
**Technical observations retained from2026-10-14; new Shopee price evidence checked2026-10-15.** Guitar/bass multi-effects; **medium**, built-in expression. This consolidates all Flex Prime fields,qualifications and references from the mixed-brand advanced comparison, without importing the other brands' specifications.

| Required field | Existing source-backed result / unresolved value |
|---|---|
| Expression and physical controls | Built-in expression with toe switch; separate TRS external EXP. **Knobs ? /3 main footswitches /buttons ?**; unknown counts not filled from MX5 despite similar dimensions |
| Display | **4-inch touchscreen**; explicit resolution and color specification were not separately recorded in the original pass and remain unverified here |
| Size/mass | **295 W×150 D×70 H mm;1.57 kg**; medium, with plug/pedal clearance additional |
| Processing | **14 DSP blocks,5 routing types**. Product page advertises600+ amps/cabs/mics/effects,100+ effects,100+ amps,80+ cabs,360+ cab IRs. Overlapping totals are not summed |
| Presets | Older FAQ says **40 factory rigs**; current factory count and total user capacity ? |
| Synth / acoustic | Guitar/bass processing documented; exact synth/electric-to-acoustic algorithms remain unverified in the original record |
| IR | Third-party **WAV/AIFF**,two IRs can share one block; exact slot/sample capacity not established |
| NAM | **Native**,current firmware: A2 Full/Lite and supported legacy formats. Two A2 Full captures simultaneously or four A2 Lite captures within two NAM blocks; architecture/DSP restrictions retained |
| Proprietary captures | HeadRush/ReValver clones and SuperClones separate from NAM. Creating captures uses the documented external software/interface workflow, not an inferred onboard capture microphone path |
| Power | **12 V/3 A center-positive adapter**; battery/USB-powered operation not established |
| Software | Wi-Fi **browser Remote Editor Windows/macOS/iOS/Android**; Linux full editor unverified |
| USB audio | **4-in/4-out**,up to24-bit/96 kHz; manufacturer's interface direction convention retained |
| Live/practice | Scenes,gapless switching/spillover claims; **five-minute loop layer,20-minute total loop audio**. No independently measured latency claim |

Ports:6.35 mm guitar input; two6.35 mm main outs;3.5 mm aux/headphones; stereo TRS FX send/return; external EXP;3.5 mm MIDI IN/OUT;USB-B. **No dedicated vocal input**: Prime/Core presets do not automatically preserve vocal processing when transferred to Flex Prime. Do not infer microphone/phantom capability from another model's capture connector.

The checked downloads included **firmware5.2**, and the current manufacturer page explicitly documented **native NAM/TONE3000 access**. It is not accurate to restrict this model to proprietary clones. This is retained dated documentation, not proof an installed unit runs5.2.

### Flex Prime — IDR offers added2026-10-15

The earlier comparison had no dependable used or new price. These later indexed asks add evidence without changing technical verification dates.

| Class | Amount | Exact offer / limitations |
|---|---:|---|
| Retail indexed hardware ask | **Rp10.215.000** | [ROCKPIZZ MUSIC,shop440477624/item29440266570](https://shopee.co.id/HEADRUSH-FLEX-PRIME-GUITAR-AMP-AND-MULTI-EFFECT-MODELING-PROCESSOR-i.440477624.29440266570). Indexed delivery16–19October; checkout/condition not verified |
| Separate retail indexed ask | **Rp9.080.000** | [HOLY MUSIC,shop945642322/item45761740882](https://shopee.co.id/HEADRUSH-FLEX-PRIME-%E2%80%93-Ultra-Compact-Multi-Effects-Premium-Amp-Modeler-Touchscreen-Pedalboard-Original-i.945642322.45761740882). Relative delivery wording is not live-stock proof |
| Retail historical ask, **sold out** | **Rp9.605.000** | [melodiasby,shop158144224/item27922230934](https://shopee.co.id/Headrush-Flex-Prime-Multi-Effect-Processor-i.158144224.27922230934), cached29–30August delivery |
| Condition-verified used offer | **?** | Not established; no automatic used-price discount applied |

Do not call these an authenticated active range. Exact condition,variant,bundle,region,warranty,shipping and stock remain unverified. A seller name is not authentication. An amplifier speaker output requires a suitable load/interface, not direct connection to a signal input.

### Flex Prime sources and preserved provenance

[Official product](https://www.headrushfx.com/products/flex-prime/index.html); [model-specific FAQ](https://support.headrushfx.com/en/support/solutions/articles/69000862403-headrush-flex-prime-frequently-asked-questions); [firmware downloads](https://www.headrushfx.com/downloads.html); [NAM format details](https://www.headrushfx.com/cloud/index.html).

All Flex Prime technical statements above were consolidated from `effects/advanced-modelers.md` at source blob `f4ecc7b15636ab477803031d34bf280afa9b98dc`. Core was consolidated from its complete original finding at blob `dcff2b12eb7dc4196c93fdba5d8ca274d99d57f2`, together with its existing comparison context. Every model-specific source URL and unresolved qualification is retained. The old mixed-brand documents remain until their other brands and incoming links are checked; **the whole repository migration is not complete**. Neither consolidation nor new price observations add Core/Flex Prime again to the model count.
<!-- comparison evidence ends -->

### Preserved original shared-source Flex Prime fields

Historical technical snapshot **2026-10-14**,retained2026-10-17. These exact rows preserve original wording and uncertainties. Later2026-10-15 IDR offers above retain their separate date;the original missing USD asks below do not erase them. Firmware5.2 references remain dated evidence,not proof of an installed version.

| Original field | Original value |
|---|---|
| External expression | Yes, separate TRS EXP |
| K/F/B | ?/3/? + expression toe switch |
| W×D×H; weight | **295×150×70**, 1.57 kg |
| Size class | Medium |
| Used USD | ? |
| New USD | ? |
| Simultaneous processing / available choices | **14 DSP blocks**, 5 routing types; current page advertises 600+ amps/cabs/mics/effects, 100+ effects, 100+ amps, 80+ cabs and 360+ cab IRs |
| Preset storage | Older FAQ states **40 factory rigs**; current factory count and total user capacity ? |
| Synth / acoustic functions | Guitar/bass processing; exact synth/acoustic algorithms ? |
| Third-party IR | **Yes**, WAV/AIFF; two IRs can share a block |
| NAM / proprietary capture | **Native NAM**, current firmware: A2 Full/Lite and supported legacy models; also proprietary HeadRush/ReValver clones and SuperClones |
| Audio/control ports | ¼″ guitar in; 2×¼″ main out; 3.5 mm aux/phones; stereo TRS FX send/return; external EXP; 3.5 mm MIDI IN/OUT; USB-B |
| Power; battery/USB-powered? | **12 V/3 A centre-POSITIVE** adapter; USB/battery operation not established |
| Configuration apps and USB functions | Wi-Fi **browser Remote Editor Windows/macOS/iOS/Android**; USB audio **4-in/4-out**, up to 24-bit/96 kHz |
| Other important differences | 4″ touchscreen; scenes, gapless switching/spillover; 5-min loop layer, 20-min total loop audio; capture creation needs the documented external software/interface workflow |

### Original shared qualifications

Other model names retain shared context;their features are not assigned to Flex Prime.

Checked **2026-10-14**. **Partial records**: `?` means unverified, not No. Native NAM, architecture-limited NAM, converted NAM, proprietary captures and cabinet IRs are different capabilities. An effects-only unit is not necessarily an amp modeler.

K/F/B = rotary controls / footswitches / separate buttons. Push-encoders are counted once. Nano Cortex's rotary footswitches are explicitly called out rather than hidden in the knob count. Dimensions are **W×D×H, mm**. Prices are separate **USD** new and used observations; missing used prices have not been invented.

**Flex Prime is not restricted to proprietary clones.** Its current manufacturer page explicitly documents **native NAM and TONE3000 access**. It specifies two A2 Full captures simultaneously, or four A2 Lite captures within two NAM blocks. The checked downloads include firmware **5.2**; architecture and DSP restrictions still apply. Its missing vocal input means Prime/Core presets do not automatically preserve vocal processing on Flex Prime.

USB audio input/output counts use the manufacturer's interface convention. A capture microphone connector does not establish a dedicated live vocal-effects path. Do not connect an amplifier's speaker output directly to an instrument/capture input; the appropriate load/interface is required.

Original model sources: [Source 1](https://www.headrushfx.com/products/flex-prime/index.html) · [Source 2](https://support.headrushfx.com/en/support/solutions/articles/69000862403-headrush-flex-prime-frequently-asked-questions) · [Source 3](https://www.headrushfx.com/downloads.html) · [Source 4](https://www.headrushfx.com/cloud/index.html)

## Gigboard

<!-- comparison evidence begins -->
Checked **2026-10-17**. Distinct guitar/bass multi-effects model; partial verification. [Product][GB-P] explicitly includes bass instruments. No software or dependencies downloaded.

| Required field | Finding |
|---|---|
| Built-in / external / toe expression | No built-in pedal; one external ¼″ TRS sweep input plus separate ¼″ TS toe-switch input. Product's two-input shorthand does not mean two independent expression pedals. [Comparison][GB-C], [Manual][GB-M] |
| Knobs / footswitches / buttons | **2 /4 /0 separate front buttons**, text-derived from manual inventory: master volume and push encoder; encoder press counted once. Rear power button additional. [Manual][GB-M] |
| Display | Color touchscreen: advertised **7 inches** [Product][GB-P], [Comparison][GB-C]; manual specifies **6.9-inch/176 mm diagonal**, LED backlight. Retain both published values. [Manual][GB-M] |
| Dimensions / weight | **329.2 W×225.6 D×67.1 H mm;3.24 kg**; mass basis unspecified. [Comparison][GB-C], [Manual][GB-M] |
| Simultaneous processing | **11 slots**, with dual amp/cab exceptions; three signal-path layouts. Exact DSP/model concurrency ceiling beyond slot count ? [Manual][GB-M] |
| Category choices | Website headings: amps **52**, cabs **15**, mics **10**; distortion **17**, dynamics/EQ **11**, modulation **22**, reverb/delay **13**, expression **11**. Website headline says more than74 FX; older comparison says **50 amps/67 FX**. These are website snapshots. Adding five missing2.6 entries gives derived53amps/78FX (18distortion/12dynamics/23modulation/14reverb-delay/11expression), not a verified installed total. See full-record audit. [2.6 notes][GB-F26] [Product][GB-P], [Comparison][GB-C] |
| Factory / user memory | Manufacturer support explicitly confirms **270 factory default rigs**, about4 MB of files; this is not total storage capacity. Rigs editable, saveable and transferable; total user capacity **?** [Factory-rig explanation][GB-R] [Manual][GB-M], [Comparison][GB-C] |
| Synth / acoustic simulator | Acoustic Sim documented in product's 2.3 feature description. Independent synth engine **?**; pitch/filter effects alone do not establish one. Polyphonic pitch supported. [Product][GB-P], [Comparison][GB-C] |
| IR / NAM / captures | User **WAV IR** import; product specifies **1024/2048 samples**, 300 included IRs. Firmware **2.6 adds two IRs per block**. [2.6 notes,p.2][GB-F26] “Virtually unlimited” is marketing, not verified storage capacity. Native/converted NAM and proprietary capture loading **?**; Prime/Core capabilities not assigned here. [Product][GB-P], [Comparison][GB-C] |
| Audio/control I/O | ¼″ TS instrument in; 3.5 mm stereo AUX; two balanced ¼″ TRS main outs, amp/line selectable; ¼″ stereo phones; mono ¼″ FX send/return; external TRS EXP and TS toe; TRS amp-switch out; DIN MIDI in/out-thru; USB-B; power. No XLR mains. Manual rear text gives send-output/return-input, but appendix reverses directions; functional directions retained. [Manual][GB-M], [Comparison][GB-C] |
| Power / battery / USB | **19 V DC,3.42 A,center-positive adapter input** in manual power specification. Same appendix incorrectly lists IEC; comparison confirms19VDC. Match actual unit/adapter label before use. Draw,battery and USB-powered operation **?** [Manual][GB-M], [Comparison][GB-C] |
| Editor / USB audio | USB file transfer needs no extra software; full desktop/mobile editor platforms **?**. **4-in/4-out,24-bit/up to96kHz** recording/reamping. Product links Mac/Windows2.7 updaters and Windows1.0.0 audio driver: 2.7 updater minimum is **Windows8/macOS10.15 with USB2.0**; these are not proof of an editor or current OS compatibility. [2.7 notes,p.1][GB-F27] [Product][GB-P], [Comparison][GB-C] |
| Looper / live features | **5-minute loop,50 layers,20 minutes total audio**; save/load. WAV/MP3 loop import,WAV export. Gapless switching/tails advertised; manual says tails unavailable with FX loop or USB audio. Scenes supported; **2.5 adds two scenes per switch**. Song View remains Pedalboard-only in2.3.1 notes, despite product mode text. Drums **?** [2.7 cumulative notes,pp.2–3][GB-F27] [Product][GB-P], [Comparison][GB-C], [Manual][GB-M] |

### Gigboard — separate IDR offer

| Class | Amount | Exact hardware offer and qualifications |
|---|---:|---|
| Indexed hardware ask; sale condition unverified | **Rp17.875.000** | [Legato Music Center,shop158413015/item4243270944][GB-O],Kota Jakarta Pusat. Direct crawler body obtained2026-10-17,cache dated last month. Condition,selected variant,bundle,adapter,warranty and checkout stock **?**. Relative same-day delivery is not current-stock evidence; late-delivery voucher up toRp10.000 is not deducted. |
| Verified used offer | **?** | Not established |
| Verified new offer | **?** | Indexed ask above has no verified sale condition |

<!-- comparison evidence ends -->

### Gigboard source and revision limits

Manual filename/footer identify2.1.2; cover/index metadata are not assumed to establish current installed firmware. Read via web text, not a local download or visual inspection. Appendix connector errors are preserved rather than silently reconciled. Current product links2.7 firmware, while category headlines and comparison totals have no aligned firmware date. Remaining work: verify installed category totals, actual power-label confirmation, user capacity, IR limits, full editor/OS support and condition-qualified offers.

[GB-P]: https://www.headrushfx.com/products/gigboard/
[GB-M]: https://cdn.inmusicbrands.com/HeadRush/gigboard/v2_1_2-0520/Gigboard-User-Guide-v2_1_2.pdf
[GB-C]: https://www.headrushfx.com/compare-boards.html
[GB-O]: https://shopee.co.id/HeadRush-Gigboard-i.158413015.4243270944

### Gigboard firmware audit — 2026-10-17

Own release notes identify **2.7,August2024**. Version2.6 adds Trace Elliot ELF,B2 Drive,Dim Chorus,Acoustic Pre and Party Verb; all five are absent from the product’s enumerated lists. Version2.7 adds Glorious Drive,White Bass Wah and Ten Freq EQ, already represented there (EQ is named10 FREQ EQ on the website). The page therefore mixes revisions. [2.7 notes,p.2][GB-F27]

Adding the five explicitly missing2.6 entries to the website lists yields a **derived reconciliation**, not a manufacturer-published installed total: **53 amps;18 distortion,12 dynamics/EQ,23 modulation,14 reverb/delay,11 expression =78 FX choices**. Cabs15/mics10 remain separate. This arithmetic does not establish simultaneous processing, nor account for unlisted utilities. Preserve the older52/74 website and50/67 comparison snapshots. [Product][GB-P], [2.6 notes,p.2][GB-F26]

Cumulative2.7 notes,p.4 revise looper feedback: it affects recording/overdub, not playback; below100% one evolving layer is replaced, and Insert is unavailable when that is the top layer. The factory-rig support article explicitly names Gigboard; its270-rig statement is not borrowed from Prime/Core’s50-rig bank. [Firmware notes][GB-F27], [Factory-rig explanation][GB-R]

[GB-F27]: https://cdn.inmusicbrands.com/HeadRush/FW/Aug24_Firmware_Updates/Gigboard%20v2.7/Official%20PDF%20Update%20Guide%20and%20Release%20Notes/READ%20ME%20-%20HeadRush%20Gigboard%20Firmware%20Update%20v2.7.pdf
[GB-F26]: https://cdn.inmusicbrands.com/HeadRush/FW/26/READ%20ME%20-%20HeadRush%20Gigboard%20Firmware%20Update%20v2.6.pdf
[GB-R]: https://support.headrushfx.com/en/support/solutions/articles/69000848879-headrush-prime-and-core-where-are-all-the-preset-rigs-

### Gigboard — expression-volume audit, 2026-10-19

**Per-rig assignment;no global volume-target override established.** [Own2.1.2 guide][GB-M], printed pp13,20,23: Hardware Assign belongs to the rig. Classic A/B changes bypass the inactive pedal target;Advanced leaves its parameters active at maximum. A/B state is recalled with the rig;this isnot held-position recall. Target ranges are percentages;signal placement depends on the rig. Headphone,bypass,tail/recorded-loop attenuation remain unresolved. **Hybrid mode:FS3 previous,FS4 next rig**,separate frombank browsing. Existing329.2×225.6mm chassis fails preference;dedicated6.35mm phones. Later2.7 behavior not independently tested.

[Manufacturer expression support](https://support.headrushfx.com/en/support/solutions/articles/69000822750-headrush-fx-how-to-setup-and-troubleshoot-an-external-expression-pedal) describes automatic assignment **after adding Volume to a rig**,not universal insertion. TRS sweep;separate toe switch selects A/B onGigboard. Volume minimum andlinear/log response editable;global polarity isnot globaltarget scope. Actual M-VAVE wiring remains unverified.

Exact [Legato shop158413015/item4243270944][GB-O] rechecked2026-10-19 returns cached **Rp17.875.000** andrelativeToday delivery text. No current checkout/stock,condition,bundle,adapter,warranty orused-offer confirmation. Late-delivery voucher not deducted. No local download orhardware test.

## MX5

Guitar/bass multi-effects; **medium** footprint; first-pass record with outstanding fields.

| Required field | Finding | Source |
|---|---|---|
| Expression | Built-in pedal with toe switch; one external 6.35 mm TRS EXP input | [M], [P] |
| Controls: knobs / footswitches / buttons | **2 / 3 / 0 front buttons**; rear power button and expression toe switch separate. Encoder press counted once | [M] |
| Display | **4-inch full-color touchscreen**; pixel resolution ? | [M], [P] |
| Dimensions and weight | **295 W ×150 D ×70 H mm;1.57 kg**. Pedal-up height and cable clearance additional | [M], [F] |
| Simultaneous processing | **11 slots**, DSP-dependent; serial and two split-path layouts. Not Core/Flex Prime's architecture | [M] |
| Factory and user memory | **270 supplied rigs**; editable/save-new rigs supported. Total storage/user-capacity ceiling ?; do not report270 factory plus270 user | [F], [M] |
| Acoustic simulation / synth | **Acoustic Sim: Yes**. No dedicated synthesizer identified in the published MX5 list; pitch/filter effects are not a verified synth engine | [P] |
| IR loading | WAV/AIFF supported; up to192 kHz/32-bit source files.1024/2048-sample processing; thousands of files described, exact storage ceiling ? | [F], [M] |
| NAM / proprietary amp captures | Neither established for MX5 by the checked2.7 documentation. Do not transfer Prime/Core clone or NAM support | [U], [D] |
| Power | **12 V DC,3 A,center-positive**, supplied adapter. Supply specification, not measured draw. Battery/USB-powered operation not documented | [M], [F] |
| Configuration applications | Onboard touch editing; Windows/macOS USB file management and firmware updater. Official desktop/mobile full editor not established | [M], [D] |
| USB audio | **4-in/4-out**, up to24-bit/96 kHz, dry/wet and reamp; Windows driver, no Mac driver required | [F] |

### MX5 category choices

The current product-page list includes the three effects added in firmware **2.7**, released **2024-08-08**. Counts are listed algorithms, not simultaneous engines: **52 amps;15 cabinets;10 microphone models; Distortion17; Dynamics/EQ11; Modulation22; Reverb/Delay13; Expression11**. The five effect groups sum to **74**; cabinets, microphones, IR files and the FX-loop utility are separate. [P], [U]

### MX5 connections and stage operation

One6.35 mm mono guitar input; stereo TRS send and return; two balanced6.35 mm main outputs; separate3.5 mm headphones and aux; separate3.5 mm MIDI IN/OUT via supplied DIN adapters; external EXP; USB-B; DC. No XLR/microphone/phantom connection in the published inventory. [M]

Scenes, setlists and hands-free editing are documented. Looper: up to **50 layers,five minutes per layer,20 minutes combined**, one loop at a time. [F] **Spillover caveat:** the manual says between-rig tails do not work while using FX Loop or USB Audio; do not repeat the unqualified marketing promise. [M,p.10] Firmware2.7 is the version exposed by the retrieved download index, not proof an owner's unit has been updated. [D]

### MX5 prices — IDR

| Price class | Amount | Exact offer and limitation |
|---|---:|---|
| Retail hardware ask; detailed condition unconfirmed | **Rp8.330.000** | [Imagination Music Store,shop19576516/item18053588344](https://shopee.co.id/Headrush-MX5-Amp-Modeling-Guitar-Effect-Processor-i.19576516.18053588344). Page reopened; checkout stock, accessories and warranty unverified |
| Historical ask; condition not specified, **sold out** | **Rp5.500.000** | [marchick,shop66490222/item29235617750](https://shopee.co.id/Headrush-mx5-i.66490222.29235617750). Cached September delivery text; not assigned to used/new and not a completed-sale value |
| Historical ask; condition not specified, **sold out** | **Rp7.000.000** | [Pedal Monk,shop808382190/item23034025252](https://shopee.co.id/Headrush-MX5-i.808382190.23034025252) |
| Condition-verified used offer | **?** | No suitable verified offer in this pass |

Do not combine unclassified or sold-out asks into an active used-to-new range. Delivery compensation is not a product discount. Seller authenticity, shipping and selected bundle are not verified.

### MX5 sources and remaining gaps

[M] [Official User Guide v1.5](https://cdn.inmusicbrands.com/HeadRush/mx5/MX5_User_Guide_v1.5.pdf): controls pp.5–6,tails p.10,routing p.11,slots p.14,IR p.18,specifications p.37. **Routing and specifications screenshots were successfully inspected**; the front-panel screenshot failed, so its numbered text and specification table supply the control evidence.
[P] [Official MX5 product and complete category list](https://www.headrushfx.com/products/mx5/index.html).
[F] [Official MX5 FAQ](https://support.headrushfx.com/en/support/solutions/articles/69000801165-headrush-mx5-frequently-asked-questions). Its reference to eleven footswitch slots is an editorial error: eleven processing slots, three physical switches.
[U] [Official2.7 release announcement](https://support.headrushfx.com/en/support/solutions/articles/69000858121-headrush-pedalboard-gigboard-and-mx5-what-s-new-in-firmware-v2-7-).
[D] [Official downloads](https://www.headrushfx.com/downloads.html).

Outstanding: exact preset/storage ceiling,pixel resolution,explicit battery/USB-power documentation,any newer model-specific editor/capture support and condition-verified used pricing. A complete field schema does not make unknown values verified.

## Pedalboard

<!-- comparison evidence begins -->
Checked **2026-10-17**. Original HeadRush Pedalboard, distinct from Prime and Gigboard. Bass inclusion rests on its own documented Ampeg SVT/B15 bass models, not a BASS EQ label. Partial record.

| Required field | Finding |
|---|---|
| Built-in / external / toe expression | Built-in pedal with toe switch; external ¼″ TRS sweep. External pedal controls B while internal controls A. Advanced mode assigns up to4 parameters per A/B; Classic switches one parameter each. [FAQ][PB-Q] |
| Knobs / footswitches / buttons | **7 /12 /0 separate front buttons**: master,phones,aux,data encoder,3 parameter encoders. Encoder push counted once; rear power and ground-lift buttons,amp/line andrack/stomp selectors additional. [Manual,pp.4–6,40][PB-M] |
| Display | Main **6.9-inch/176 mm color touchscreen** in manual versus advertised7-inch. Twelve **1.2-inch/30 mm monochrome OLED** strips, one per footswitch. Exact-model manufacturer page independently confirms twelve individual OLED assignments2026-10-31; strip touch support **?** [Manual,p.40][PB-M], [Comparison][PB-C] |
| Dimensions / weight | Manual **609.6 W×304.8 D×79.2 H mm,pedal fully forward;7.50 kg**. Comparison instead **599.4×284.4×73.7 mm;7.12 kg**. FAQ rounds height79 mm and agrees7.5kg. Revision/mass-basis discrepancy unresolved. [Manual,p.40][PB-M], [Comparison][PB-C], [FAQ][PB-Q] |
| Simultaneous processing | **11 rig slots**, dual amp/cab exceptions; Three signal layouts:series,two split/rejoin arrangements. Tails unavailable with FX loop or USB audio in2.1.2. DSP ceiling model-dependent, exact maximum independent effects **?** [Manual,pp.9–10][PB-M] [Manual,p.14][PB-M] |
| Category choices | Own website headings: **52 amps,15 cabs,10 mics;17 distortion,11 dynamics/EQ,22 modulation,13 reverb/delay,11 expression**. Comparison older50amps/67FX. Own2.7 notes include2.6 additions absent from website lists; installed current totals remain unresolved. [Product][PB-P], [Comparison][PB-C], [Firmware,p.2][PB-F] |
| Categories / website versus release-note union | Recounted2026-11-03:[own exact-model page][PB-P] lists **52 amps,15 cabs,10 mics** and **74 effects=17 distortion+11 dynamics/EQ+22 modulation+13 reverb/delay+11 expression**. Own2.7 cumulative notes,p2,document five2.6 additions absent fromthose lists:**17 TRACE ELLIOT ELF;B2 DRIVE;DIM CHORUS;ACOUSTIC PRE;PARTY VERB**. Union gives **53 amps and78 effects**,with category choices18/12/23/14/11;not a verified installed census,concurrency orunique-DSP-engine count. [Own release notes][PB-F] |
| Synth / pitch / special distinctions | The listed **SMART HARM,DETUNE,OCTAVES/OCTAVES UP,DROP TUNE,WHAM,HARM,CHORD WHAM** establish named pitch choices,not blanket polyphonic tracking. **RING MOD,8-BIT CRUSH,HOLD,RESO DELAY,FEEDBACK,TIME WARP** are special-processing choices. Acoustic Sim differs from2.6 Acoustic Pre. No dedicated oscillator synth isestablished bythese sources;Prime’s Hybrid Synth isnot transferred. [Own product][PB-P];[own history][PB-F] |
| Factory / user memory | **270 factory presets**; total user storage and factory-filled versus writable capacity **?**. File backup Mac/PC. [FAQ][PB-Q] |
| Synth / acoustic simulation | Acoustic Sim listed; independent synth engine **?**. Bass amps include66 Flip Bass/69 Blue Line Bass; these are models, not ownership proof. [Product][PB-P] |
| IR / NAM / captures | WAV/AIFF imports,up to192kHz/32-bit source files; storage capacity **?**. Firmware2.6 adds **two IRs in one block**. Native/converted NAM and proprietary capture loading **?**, not inferred from Prime/Core. [FAQ][PB-Q], [Firmware,p.2][PB-F] |
| Audio/control I/O | ¼″ TS instrument in;3.5mm stereo AUX;external¼″TRS EXP;two XLR outs with ground lift;two¼″TRS mains;¼″stereo phones;two¼″sends/two returns;DIN MIDI in/out-thru;USB-B;IEC. No amp-control out per comparison. FAQ/appendix reverse send/return directions; manual rear-panel text correctly identifies sends as outputs and returns as inputs. [Manual,pp.5–6][PB-M], [Comparison][PB-C] |
| Power / battery / USB | **100–240 V AC,50/60Hz,1.2 A IEC input rating**, not measured consumption; DC barrel polarity N/A. Battery/USB-powered operation **?** [Manual,p.40][PB-M] |
| Editor / Windows11 hardware qualification | [Manufacturer Windows11 matrix](https://support.headrushfx.com/en/support/solutions/articles/69000804015-headrush-windows-11-compatibility),checked2026-11-03: **Pedalboard Supported,audio driver1.0.6**. Test scope:file transfer,USB recording,firmware update;exact firmware/build unstated. **WindowsARM andInsider/Preview builds unsupported**. This is not certification ofa full editor,third-party firmware bridge orevery DAW. |
| Editor / macOS26 hardware qualification | [Manufacturer Tahoe matrix](https://support.headrushfx.com/en/support/solutions/articles/69000872801-headrush-macos-26-tahoe-compatibility),checked2026-11-03: **Pedalboard supported onIntel andAppleSilicon;Firmware Updater2.7.0**. Tests use Intel/base-level AppleSilicon forUSB file transfer,recording andupdates. This narrows the earlier current-OS uncertainty,not a full-editor orall-chip/build guarantee. Updater anddevice firmware labels remain distinct. |
| Display / editable OLED assignment labels | [Own cumulative2.7 notes,August2024,p7][PB-F],section“Since Firmware Version1.0.2”,documents custom OLED text through Hardware Assign for **eight assignable Stomp switches**. Twelve physical OLEDs remain;these are not eight extra screens orproof every switch has the same assignment options. The notes’ **800×400 screen-lock image recommendation** is not a published physical LCD pixel specification. Checked2026-11-03;no update ordevice test. |
| Editor / dated updater requirement | **Firmware2.7 notes,August2024:Windows8 or macOS10.15,host USB2.0**. Updater minimum only; not proof of full-editor availability or current driver/OS compatibility. [Firmware,p.1][PB-F] |
| Editor / USB audio | **4-in/4-out,up to24-bit96kHz**,record/reamp;Windows driver,Mac driverless per FAQ. Full editor/mobile/Linux support **?**;current Windows11/Tahoe hardware support is separately qualified above. Live USB mode feeds computer and hardware outs; DAW/Reamp modes disable hardware outs. USB file transfer is separate from editing; Mac/Windows updaters are not editors. [Manual,p.33][PB-M] [FAQ][PB-Q], [Comparison][PB-C] |
| Looper / scenes / routing | Comparison **5-minute loop,50 layers,20-minute total audio**; FAQ instead **100 layers/20 minutes**, unresolved revision difference. Own manual2.1.2 pp.29–30 confirms **50 layers/20 minutes**, matching comparison rather than FAQ. PRE/POST looper placement,half/double speed andlength,reverse,mute,save/load,WAV/MP3 import supported. Playback continues after leaving looper; rigs can change between layers. Unsaved-loop power-cycle retention **?**. Scenes,setlists,Song Mode,hands-free editing;drums **?** [Comparison][PB-C], [FAQ][PB-Q], [Manual,contents][PB-M] |

### Pedalboard — separate IDR offer

| Class | Amount | Exact hardware offer and qualifications |
|---|---:|---|
| Historical indexed ask; sale condition unverified; **sold out** | **Rp26.840.000** | [Legato Music Center,shop158413015/item7543266305][PB-O],Kota Jakarta Pusat. Retrieved2026-10-17;cache4weeks old,delivery19September. **Habis**;no live-stock claim. Condition,selected variant,bundle,IEC cable,warranty **?**. Late-delivery voucher up toRp10.000 not deducted. |
| Verified used offer | **?** | Not established |
| Verified new offer | **?** | Historical ask has no verified sale condition |
<!-- comparison evidence ends -->

### Pedalboard — OLED firmware behavior, 2026-10-31

[Own cumulative2.7 notes][PB-F],August2024,printedpp2–3: the2.3.1 section changes OLED burn-in protection from30 to60 minutes and fixes blank footswitch displays on entering Looper. The2.7 section fixes occasional incorrect LED colors for rigs with dual-state scenes. Screen protection, OLED content and switch-LED color are distinct. Historical firmware behavior; seller-installed versions and present device behavior unverified. No firmware download, installation or hardware test.

### Pedalboard source limits

Own User Guide2.1.2 read via web text,not downloaded. Conflicting dimensions,layer limits and category snapshots are retained. Own2.7 release notes were checked for the current additions and dualIR feature;selected cumulative looper changes were checked;not every historical fix was transcribed. No sibling manual fills missing fields. Next: installed category verification,unsaved-loop persistence,user storage,exact power consumption,current software support and condition-qualified offers.

[PB-P]: https://www.headrushfx.com/products/pedalboard/
[PB-Q]: https://support.headrushfx.com/en/support/solutions/articles/69000801171-headrush-pedalboard-frequently-asked-questions
[PB-M]: https://cdn.inmusicbrands.com/HeadRush/pedalboard/v2_1_2-0520/Pedalboard-User-Guide-v2_1_2.pdf
[PB-C]: https://www.headrushfx.com/compare-boards.html
[PB-F]: https://cdn.inmusicbrands.com/HeadRush/FW/Aug24_Firmware_Updates/Pedalboard%20v2.7/Official%20PDF%20Update%20Guide%20and%20Release%20Notes/READ%20ME%20-%20HeadRush%20Pedalboard%20Firmware%20Update%20v2.7.pdf
[PB-O]: https://shopee.co.id/Headrush-Pedalboard-i.158413015.7543266305

### Pedalboard looper and routing audit — 2026-10-17

Manual2.1.2 pp.29–30 supersedes the unqualified FAQ100-layer assertion for that documented revision: **50 layers,20 minutes aggregate**. The FAQ is retained as a conflict,not erased. Insert replaces the topmost layer segment;loop-length halving is reversible. Global Rig Input can use rightFXreturn,which disables stereo return;XLR,¼″ andphones independently select rig/alternate taps (p.32). These routing options do not add microphone input or vocal eligibility. [Manual][PB-M]

Own2.7 cumulative notes,p.4: feedback affects recording/overdub rather than playback;below100%,one evolving layer replaces itself;peeling it restores underlying levels,and Insert is disabled if it is topmost. Ownnotes,p.2 document two scenes per switch from2.5 andtap-tempo calculation overthree presses from2.6. These are firmware-qualified changes,not new hardware controls. [Firmware][PB-F]

## Prime

**Guitar/bass/vocal multi-effects; checked 2026-10-16.** New distinct model, not Core, Flex Prime or the older Pedalboard. Firmware-specific findings below use the manufacturer's **5.2.0** manual and October 2026 release notes; no device firmware was installed or tested.

| Required field | Model-specific finding / qualification |
|---|---|
| Expression | Built-in with toe switch; one external 6.35 mm TRS EXP plus separate TS toe-switch input. Banks of assignments and multiple-parameter control documented. [PR-M pp.7–9] |
| Expression / assignment modes | [Prime FAQ](https://support.headrushfx.com/en/support/solutions/articles/69000834532-headrush-prime-frequently-asked-questions), checked 2026-11-03: Classic mode assigns one parameter per A/B bank and bypasses the previous target on toe change. Advanced mode assigns up to four per bank; switching leaves previous parameters active at maximum. External EXP controls C/D; without a toe switch only C is accessible. Momentary/latching toe type is configurable. These bank behaviors do not establish global volume assignment or numeric endpoints. |
| Expression / 5.2 Auto-Engage and recall | Saved [own5.2 guide,printedpp37–38](https://cdn.inmusicbrands.com/Software/SGEE/52/HeadRush%20Prime%20-%20User%20Guide%20-%20v5.2.0.pdf), read **2026-11-03**: **Auto-Engage supports two parameters per A/B/C/D bank**, with Off Position **Toe Up,Toe Down orStop** and **Off Delay0–5000ms**. Reaching that position bypasses the assigned target(s) after the delay; toe switching selects the other bank and bypasses the previous targets, as in Classic. Classic-assigned parameters are locked against editing elsewhere; Advanced/Auto-Engage parameters remain editable. Saving recalls the internal **A/B bank state**, not proven held-pedal position. Assignment range uses percentages of the target’s own range, not a universal dB/mute range. These rig-level settings do not establish global volume or headphone/tail/loop coverage. No device operation. |
| Rotary / footswitch / button counts | **8 / 12 / 0 front-panel buttons**: seven top rotaries (main, phones, aux, navigation and three parameters), plus rear mic-gain rotary. Appendix's seven-knob list omits that rear gain control; scope is explicit. Power switch separate, encoder presses counted once. Rendered top panel inspected. [PR-M pp.6–8,85] |
| Footswitch / scene operation | [Prime FAQ](https://support.headrushfx.com/en/support/solutions/articles/69000834532-headrush-prime-frequently-asked-questions): Hardware Assign changes switch placement independently of block routing. Rig/Stomp/Hybrid views separate preset, block and mixed control. **One or two scenes per switch** can recall assigned block states. Dual-purpose switches that hold for hands-free editing perform the block toggle on release; this explains an action-timing delay, not measured audio preset-switch latency. Checked 2026-11-03; no device test. **5.2 guide p66 qualification:** Global Footswitch Functions selects On Press/On Release;some functions move to hold in On Press mode. The FAQ wording is not an unconditional current-mode restriction. [Exact follow-up](#prime--selectable-switch-timing-and-practice-tool-oled-labels). |
| Footswitch / custom labels and scene recall | Original [Prime5.2 guide](https://cdn.inmusicbrands.com/Software/SGEE/52/HeadRush%20Prime%20-%20User%20Guide%20-%20v5.2.0.pdf),printedpp34–35: **eight middle switches** have rig-level assignments;their displayed text is editable separately from block names. Scenes select **On/Off/No Change**,can load block presets andchoose doubling/split-path A/B/No Change. Two states per switch can have different LED colors;LED color is not OLED color. No label-character ceiling orseamless preset-reload guarantee is published here. |
| Footswitch / hands-free editing | Same original guide,p40: hold an assigned block switch **over one second**;top six switches select six parameters per page,expression changes the value,andlower-right −/+ fine-tunes. Lower-middle switches page through parameters,or audition previous/next IR when editing an IR;lower-row second-from-left saves the rig andlower-left exits. This is parameter editing,not global expression-volume assignment. Checked2026-11-03 fromsaved guide;no device operation. |
| Memory / unsaved-change indication | Original [5.2 guide,p20](https://cdn.inmusicbrands.com/Software/SGEE/52/HeadRush%20Prime%20-%20User%20Guide%20-%20v5.2.0.pdf),checked2026-11-03: block insertion/deletion/movement,preset replacement andHardware Assign changes trigger the rig-name asterisk. **Block bypass,parameter-knob edits andexpression movement do not trigger it**,although these changes can be saved. Absence ofthe marker isnot proof the working rig matches its saved state. Confirmation onrig departure is documented when the marker is present andcan be disabled;no automatic-save guarantee inferred. |
| Processing / stereo and mono scope | Same guide,p19: stereo effects,split paths or2X amp/cab/IR configurations establish stereo. Later mono models apply independently toeach channel rather than summing. **L/Mono-only output orRig Width0% produces mono**;100% retains full width. Width affects stereo signals only. These are documented routing rules,not measurements orproof that every NAM model preserves stereo;existing NAM-quality qualifications remain. |
| Controls / automatic switch assignment | Saved [manufacturer5.2 guide,p66](https://cdn.inmusicbrands.com/Software/SGEE/52/HeadRush%20Prime%20-%20User%20Guide%20-%20v5.2.0.pdf), checked2026-11-03: **Auto Assign Footswitches On** assigns a newly loaded model to the next available switch; Off leaves assignment to Hardware Assign. This is a global loading preference, not proof every loaded block has a visible switch or that assignments are shared across rigs. Hybrid Mode separately chooses rigs above/stomps below or the reverse. No device setting changed. |
| Processing / automatic amp-cab pairing | Same p66: **Add Cab with Amp On** selects an associated cab/microphone when loading a new amp or changing its amp Preset; Off keeps cab/microphone independent of amp selection. Manual cab/mic edits remain possible afterward. This coupling is not another signal-chain slot, a fixed mandatory pairing or a rule that every amp parameter edit replaces the cabinet. Actual installed-version behavior untested. |
| Display | **7-inch full-color multi-touch** main display, plus **12 OLED scribble strips, one per footswitch**, independently reaffirmed by exact Prime manufacturer page2026-10-31. Numerical pixel resolution and auxiliary diagonals/color/touch remain unverified; RGB switch LEDs are separate. [PR-P, PR-F, PR-M] |
| Dimensions / weight | **652.3 W ×307.8 D ×82.3 H mm, pedal fully forward; 7.50 kg**. Large. Original centimetre dimensions converted exactly, not measured on a unit. [PR-F, PR-M p.85] |
| Blocks / routing | **14 available blocks**, DSP-limited. Dual-guitar paths retain separate inputs; guitar/vocal paths offer **7 vocal/7 guitar, 4 vocal/10 guitar, or 2 vocal/12 guitar slots** in guide5.2.0 p17. Other guitar-only split routings exist. The earlier seven-per-input summary was incomplete for guitar/vocal mode; see correction below. Repeated block types allowed subject to CPU. A dry-mic output path is not fourteen additional vocal FX. [PR-M pp.14–17; PR-S] |
| Blocks / Dry Mic Out boundary | [Prime-specific FAQ](https://support.headrushfx.com/en/support/solutions/articles/69000834532-headrush-prime-frequently-asked-questions),checked **2026-11-03**: Straight Path,Middle Split andImmediate Split can retain **Mic Dry Out** alongside the guitar chain. Its fixed controls include **noise gate,compression,high-pass filter andsimple EQ**,but arbitrary vocal effects cannot be inserted inthis mic path. Thus “dry” doesnot necessarily mean wholly unprocessed;it isnot another14-slot vocal chain. FAQ firmware unstated;current5.2 equivalence andindependent simultaneous-resource limits untested. |
| Looper / destructive edits andlayer scope | Same [Prime FAQ](https://support.headrushfx.com/en/support/solutions/articles/69000834532-headrush-prime-frequently-asked-questions): **Peel** removes the most recently recorded layer,repeated presses working backward. **Insert punches into a chosen section andoverwrites all previous layers there**,rather than adding a normal overdub. Only **one loop at a time** is documented;50 layers are not50 independently playing loops. Undo/recovery afterInsert,power-cycle retention andcurrent5.2 equivalence remain unverified. No device recording orfile operation performed. |
| Categories / visible reference census | [Current product-list recount](#prime--visible-reference-list-reconciliation) finds **125 effect rows /124 distinct names**, plus separate amp/cab/mic libraries. ReValver amps **47 names versus44 header**;overdrive **18 versus16**;pitch **8 rows/7 names** because Octaves repeats. This reconciles displayed rows, not installed5.2 content, independent DSP algorithms or concurrency. Earlier header counts remain preserved. |
| Memory | FAQ states **50 preloaded factory rigs**; firmware-current installed content and numerical total rig/user storage ceiling unverified. Rigs, block presets, scenes, setlists, loops and captures are distinct objects. MIDI program numbers 1–128 are not proof of only 128 stored rigs. [PR-F, PR-M] |
| Synth / acoustic | Current Prime list explicitly includes **Hybrid Synth, Electric Piano and DB-33 Organ**; Ambi-Verb is also classified under Synth. **Acoustic Sim** and Acoustic Pre are separate EQ-category entries. Do not equate the acoustic preamp or an IR with the simulator. [PR-P] |
| Synth / arpeggiator availability | [Own cumulative5.2 release history,pp9,11](https://cdn.inmusicbrands.com/Software/SGEE/52/READ%20ME%20-%20HeadRush%20Prime%20Firmware%20Update%20Instructions%20v5.2.0.pdf): **3.2.0** adds Hybrid Synth,Electric Piano,DB-33 Organ;Ambi Verb moves intoSynth because its reverb is synthesized. **4.0.0** adds arpeggiator controls to those three instrument/synth blocks. Four category entries do not establish four tracking engines;input-note polyphony remains unverified. |
| Pitch / Drop Tune revisions | [Same history,p4](https://cdn.inmusicbrands.com/Software/SGEE/52/READ%20ME%20-%20HeadRush%20Prime%20Firmware%20Update%20Instructions%20v5.2.0.pdf): **5.0.1** fixes clean-rig artifacts and adds **Legacy** (pre5.0 algorithm) / **Refined** (5.0 algorithm) modes. Manufacturer tracking-speed/quality improvements are claims,not measured latency,chord handling orSynth polyphony. |
| Processing / cross-input effect categories | [Prime-specific manufacturer support](https://support.headrushfx.com/en/support/solutions/articles/69000859800-headrush-prime-can-i-use-guitar-fx-on-vocal-rigs-), checked **2026-11-03**: guitar-effect categories can be used on vocal paths, and vocal effects on guitar paths; Vocal Doubler is an explicit guitar example. Category labels therefore do not restrict each effect to its namesake input. Watch the OUT meter and rear mic-gain setting because guitar effects may add gain even without obvious distortion. Article firmware is unspecified; this does not certify every algorithm’s tracking suitability, latency or DSP concurrency. |
| Vocal | Antares Auto-Tune, De-Esser, Vocal Distortion, Doubler, Harmony, Stutter and Vocoder are separately listed; mic path and routing qualifications above apply. [PR-P, PR-S] |
| IR / captures | Third-party IR loading, 1024/2048-sample processing; FAQ accepts **WAV/AIFF up to 192 kHz/32-bit** and two IRs in a block. Processing length differs from accepted source-file rate/depth. Dedicated IR-loader browser; shared rigs can require external assets and relinking/saving (see support scope below). Exact conversion rules/slot ceiling unresolved. Proprietary onboard **Amp Cloner**, HeadRush/ReValver clones and SuperClones are separate from NAM; SuperClone assembly is a desktop software workflow. [PR-F, PR-M, PR-R] |
| Capture / target restrictions | [Exact Prime manufacturer FAQ](https://support.headrushfx.com/en/support/solutions/articles/69000834532-headrush-prime-frequently-asked-questions),checked2026-11-03: onboard cloner cannot capture time-based flanger/chorus/delay;certain gated fuzzes also cannot be cloned. Some older fuzzes designed for high-impedance guitar output need a **reamp box**. These are capture-target restrictions,not absence of playable modulation/delay effects or a universal NAM-import prohibition. |
| Native / converted NAM | **Native NAM A1/A2**, not a conversion-only claim. 5.1 documented one A1 Standard/Lite/Feather/Nano or A2 Full/Lite per rig; **5.2 allows two A2 Full, or four A2 Lite across two NAM blocks**, including doubling modes. Do not apply the newer A2 limits to every A1 architecture. [PR-R] |
| NAM / stereo and tails restrictions | Own5.2 guide pp24–25: A2 automatically Lite when more than2 captures are loaded or stereo FX precede2 separate NAM blocks; Mode unavailable for A1. Any NAM block disables rig-change reverb/delay tails. Switch Doubling is the documented alternative for capture changes within a rig; not universal spillover. [Detailed qualifications](#prime--nam-stereo-quality-tail-and-level-boundaries). |
| Audio/control I/O | TS guitar in; balanced XLR/6.35 mm combo mic in with **48 V**; stereo TRS FX send/return; two TRS mains plus two XLR mains; 3.5 mm aux and headphones; EXP, toe, external amp-control TRS; DIN MIDI IN/OUT-THRU; USB-A storage/class-compliant MIDI host; USB-B computer; IEC mains; Wi-Fi and Bluetooth audio. **Send is output, return is input**; FAQ/spec table reverse those direction labels, while operating descriptions are clear. [PR-F, PR-M pp.8–9] |
| Routing / global buses and EQ | Saved own5.2 guide,pp65,68: Advanced routing assigns sources to **three global buses**;hardware options are OUT1,OUT2,SPLIT1/2,OUT1+2,OUT3. XLR,quarter-inch andphones destinations are separately configurable. XLR/quarter-inch each have **four-band parametric Global EQ**;headphone EQ coverage unverified. This is not global EXP volume. [Guide](https://cdn.inmusicbrands.com/Software/SGEE/52/HeadRush%20Prime%20-%20User%20Guide%20-%20v5.2.0.pdf). |
| I/O / AUX volume bypass | Saved [own Prime5.2 guide,printedp7](https://cdn.inmusicbrands.com/Software/SGEE/52/HeadRush%20Prime%20-%20User%20Guide%20-%20v5.2.0.pdf),checked2026-11-03: AUX audio goes directly tooutputs without modeling/effects andcannot enter the looper. It is **unaffected by Main Volume andPhones Volume knobs**;use Aux Volume. This documented exception isnot proof ofexpression attenuation oridentical Bluetooth behavior. |
| Expression / drum-page override | Same **p74**: enabling **“Intensity” on Drum Mach. Page** makes expression ignore rig assignments andcontrol drum Intensity while that page isshown. This page-dependent override isnot global guitar-volume assignment;return-to-rig held-position behavior remains unverified. |
| Expression / zero-volume tuner trigger | Same **p74**: **Engage Tuner when Vol is at0%** requires an expression pedal assigned to a **Volume block**;toe-up0% then activates the tuner. This is a block-dependent trigger,not an automatic all-rig volume destination orproof that AUX,USB,tail andloop audio are muted. |
| I/O / external amp control restriction | Same **pp5,9**: external amp-footswitch TRS output requires an amplifier **short-to-sleeve** switching input. It is a control connection,not an audio output oranother expression input;other electrical switching protocols are not established. |
| Power / battery / USB | **100–240 V AC, 50/60 Hz, 1.2 A rated input**, IEC. DC voltage/polarity N/A. Internal coin cell disclosed for disposal is **not a rechargeable operating battery**; battery/USB bus-powered operation not established. [PR-M p.85] |
| Editors | Full **HeadRush Remote browser editor over Wi-Fi**: Windows, macOS, iOS and Android browsers named in release notes; seven-inch-or-larger screen recommended. This differs from desktop Windows/macOS updater and Windows audio driver; Linux full-editor support unverified. [PR-R, PR-M] |
| Editor / Windows hardware-driver qualification | [Manufacturer Windows11 compatibility table](https://support.headrushfx.com/en/support/solutions/articles/69000804015/),checked2026-11-03,explicitly lists **Prime Supported,Windows Audio Driver1.0.2**. Tested USB scope:file transfers,audio recording andfirmware updates;exact hardware firmware/build unstated. **WindowsARM unsupported**;x86/x64 software emulation doesnot provide driver support. Insider/Preview builds are not officially supported. This is not Remote browser-editor certification orproof ofevery DAW/build. |
| Editor / Tahoe hardware qualification | [Manufacturer macOS26 Tahoe table](https://support.headrushfx.com/en/support/solutions/articles/69000872801-headrush-macos-26-tahoe-compatibility),checked2026-11-03,lists **Prime supported onIntel andAppleSilicon**,with **Firmware Updater5.0.1**. Testing describes Intel/base-level AppleSilicon andUSB transfers,recording,updates;no exhaustive chip/build list. This qualifies the older generic Mac plug-and-play claim,butdoesnot certify the newer5.2 updater,all browser-editor functions orReValver/AmpCloner versions byassociation. No software downloaded,installed orrun. |
| USB / exact recording channels | Saved [own5.2 guide,printedp59](https://cdn.inmusicbrands.com/Software/SGEE/52/HeadRush%20Prime%20-%20User%20Guide%20-%20v5.2.0.pdf),checked2026-11-03: computer inputs **1/2=XLR processed L/R,3/4=quarter-inch processed L/R,5=dry guitar mono,6=dry combo-mic mono**. These are six recording channels,not six independently processed rig paths. |
| USB / playback andreamp routes | Same pp59–60: computer outputs **1/2 feed main outputs andphones directly;3 returns through the rig forreamping;4 isunused inthis scenario**. Reamp example records processed1/2 ormono1. Do not infer playback4 isuniversally unavailable orUSB1/2 pass through aVolume block. |
| USB / monitoring andlevel scope | Same p73: **Live** sends tocomputer andhardware outputs; **DAW/Reamp disable hardware outputs** forDAW monitoring. Incoming **USB In Level −60 to+12dB** isseparate from EXP assignment. Sample-rate changes require USB Audio Off,rate selection,On andDAW restart. These settings do not establish global pedal coverage ofUSB/headphones/tails/loops. No hardware orsoftware operated. |
| USB audio | **Six recording channels to computer, four playback channels to device**, 24-bit, **44.1/48/96 kHz**, with dry guitar/mic and reamp. This model-specific 5.2 description is not copied from Core/Flex Prime. Windows driver separate; Mac plug-and-play stated by manufacturer. [PR-M p.59; PR-P] |
| Looper / external-clock and dual-input boundaries | [Prime-specific manufacturer support](https://support.headrushfx.com/en/support/solutions/articles/69000835150-headrush-prime-looper-setup-and-troubleshooting),checked2026-11-03: receive clock over DIN orUSB-A;enable Receive MIDI Clock,looper MIDI Beat Clock andGlobal Tempo Sync. External-clock mode **disables local count-in**;Record blinks while waiting for the clock source tostart,while Record can still stop recording. Dual inputs record into **one shared loop layer**,so speed/reverse affect both together;output-block mixing andseparate-output settings affect routing/looper position. This is not independent two-track editing orglobal EXP attenuation. Support article has nofirmware version;current5.2 equivalence untested. |
| Memory / effect-library save versus rig save | [Manufacturer Prime-named saving guidance](https://support.inmusicstore.com/en/support/solutions/articles/69000881954-headrush-prime-core-and-flex-prime-why-aren-t-my-fx-changes-being-saved-),checked2026-11-03:Save inside the effect editor stores a reusable **FX preset**,not the whole rig. **Main-screen Rig Save** stores effect/amp/cab settings,routing andfootswitch assignments together. Saving only the FX library can therefore leave rig changes absent after switching rigs. This doesnot prove edits propagate toother rigs,global controller assignments orrecorded-loop backup. Article doesnot specify firmware;no save/recall tested. |
| Looper / drums / stage | Loop up to **five minutes; twenty minutes total overdubbed audio, fifty layers**. Scenes, setlists, spillover, practice tool, MIDI sync and capture/storage workflows. Firmware 5.0 adds **16 kits,134 styles/15 genres** with fills/accents; USB audio/loop playback are not unlimited extra rig blocks. [PR-M p.49; PR-R] |

### Prime — selectable switch timing and Practice Tool OLED labels

Checked **2026-11-03** in complete printed pp52,66–67 of the already-saved [original User Guide5.2.0](https://cdn.inmusicbrands.com/Software/SGEE/52/HeadRush%20Prime%20-%20User%20Guide%20-%20v5.2.0.pdf). No new download,screen rendering ordevice operation.

| Field | Exact revision-qualified result |
|---|---|
| Footswitch action timing | Global **Footswitch Functions** chooses **On Release or On Press**. In On Press,some switch functions move to hold operation. This qualifies the older FAQ’s release-trigger explanation above;it is not a measured preset-audio switching delay orproof all hold functions remain identical. |
| Footswitch / assignable utility | **FS6 press** selects Looper,Practice Tool,Tuner orDrum Machine;the separate Hold for View setting chooses FS6 orFS7 for changing footswitch mode. Press assignment andhold-mode selection are distinct,not additional physical switches. |
| Practice Tool / individual OLED contents | The guide explicitly maps all12screens in this mode:top row **Speed−,Speed+,Volume−,Volume+,Track≪,Track≫**;bottom **Loop In,Rwd,Play,Fwd,Loop Out,Exit**. These are mode-specific actions,not12 simultaneous effect blocks orpublished OLED resolution/diagonal. Track pitch can change without speed andspeed without pitch. |
| Display settings / scope | **LCD Brightness1–5** is explicitly the **main display** setting. It does not establish OLED-strip brightness range,individual screen touch capability orphysical color specifications. |
| Storage / scope | Remaining Storage meters available internal space andsupports file backup/removal. It doesnot publish a guaranteed rig-count ceiling;an illustrated meter is not a certified retail storage specification. |

Older FAQ observations andcurrent unknowns remain preserved. The12OLED layout is established independently ofthis functional-label follow-up;separate auxiliary diagonals,pixels andcondition-qualified current Shopee stock remain open.

### Prime — category-count qualifications

The current product list prints these category headers: HeadRush amps **53**, ReValver amps **44**, ReValver cabinet microphones **31**; vocal **7**, overdrive **16**, distortion/fuzz **11**, EQ **9**, compressor **6**, delay **14**, reverb **7**, chorus **7**, phaser/flanger **10**, vib/trem/rotary **6**, wah/filter **8**, synth **4**, rhythmic **2**, pitch **7**, volume/dynamics **5**, utility **3**. These are **published header counts, not a reconciled installed-library census**. Overdrive visibly lists **18 names beneath its 16 header**; pitch lists eight rows with **Octaves duplicated**. Firmware 5.1 adds Graphic Bass EQ, but the displayed EQ list needs reconciliation. Do not silently sum these into a definitive current total. Cabinet/mic/IR combinations are separate from independent effects. [PR-P, PR-R]



**Detailed-card reconciliation, checked 2026-11-03:** the same [manufacturer page](https://www.headrushfx.com/products/prime/index.html) has **eight distinct pitch cards**: Up Tune, Chord Wham, Drop Tune, Harm, Octaves, **Octaves Up**, Smart Harm and Wham. Thus the compact list’s repeated Octaves does not establish that the two cards are identical; its seven-count header remains inconsistent. The detailed **DYNAMICS/EQ (10)** heading contains only **nine named cards**, matching the compact EQ(9) list; Graphic Bass EQ is absent from those visible cards. Overdrive has eighteen distinct detailed cards as well as eighteen compact names beneath its sixteen header. These reconcile page representations only, not installed firmware content or a certified total. The saved 5.2 guide does not supply these missing category-name tables. Older header observations above are retained.

### Prime — routing and amp-list revision correction, checked 2026-11-03

The saved original guide5.2.0, printed pp15–17, specifies the three vocal/guitar allocations above. The older summary “seven per input” applies to the 7/7 option, not every dual-input arrangement. Firmware3.2.0 introduced 4/10 and2/12, as preserved in [current cumulative release notes, printed p11](https://cdn.inmusicbrands.com/Software/SGEE/52/READ%20ME%20-%20HeadRush%20Prime%20Firmware%20Update%20Instructions%20v5.2.0.pdf). Fourteen slots remain DSP-limited; this is not fourteen extra vocal effects or an additional input connector. No diagram or device was newly inspected.

The [manufacturer product compact list](https://www.headrushfx.com/products/prime/index.html) contains **53 HeadRush amp names and47 ReValver amp names**, although the latter header says44. The three25 ON-1 channels are already included in47; firmware5.0 added them, so do not add them a second time. Firmware5.1 separately documents **90 ACM900**, absent from the compact list, plus Graphic Bass EQ absent from its EQ list. Therefore47 is a counted website list, not a certified current installed total; deriving48 assumes complete retention and no other changes. Cabinet/mic compact lists separately contain **15/10 HeadRush and67/31 ReValver** entries. They are model/parameter selections, not multiplied into an effects count. Header44 and prior observations remain historical evidence.

### Prime — separate used / retail IDR evidence

Observed **2026-10-16** through public page text; stock, condition and contents are not independently authenticated.

| Class | IDR ask | Exact offer / qualification |
|---|---:|---|
| Explicit SECOND/BEKAS, **sold out** | **Rp15.400.000** | [BANGBONGMUSICBEKASI,1149776042/54402465704](https://shopee.co.id/Headrush-Prime-Guitar-Multi-Effect-Amp-Modelling-Processor-Second-Bekas-i.1149776042.54402465704), Bekasi. **Habis**; historical ask, not available used stock or a completed sale. Grade/accessories/warranty unknown |
| Retail, **with voucher** | **Rp22.789.000** | [HOLY MUSIC,945642322/52161712736](https://shopee.co.id/HEADRUSH-PRIME-%E2%80%93-Next-Generation-Guitar-FX-Amp-Modeler-and-Vocal-Processor-Touchscreen-Pedalboard-Original-i.945642322.52161712736), Jakarta Utara. **Dengan Voucher**, eligibility and checkout unknown; cached relative delivery is not current stock. New condition, bundle, region/warranty and shipping unconfirmed |
| Condition-unverified retail listing, checked2026-10-31 | **Rp21.500.000** | [ROCKPIZZ MUSIC,440477624/27890256567](https://shopee.co.id/HEADRUSH-PRIME-GUITAR-EFFECT-AMP-MODELLING-PROCESSOR-i.440477624.27890256567), Kota Denpasar. Exact Prime hardware title,not Flex Prime. Search and direct reopening agree but both use two-month-old cached text. No Habis in excerpt is not stock confirmation. Condition,variant,bundle,accessories,warranty region,shipping/tax and checkout unknown. Late-delivery compensation is not a product discount. |
| Condition-unverified exact hardware, checked **2026-11-02** | **Rp21.399.999** | [GITARO STORE INDONESIA,shop1643318004/item25497455618](https://shopee.co.id/Efek-Headrush-Prime-Guitar-Multi-Effect-Amp-Modelling-Processor-Head-Rush-Prime-i.1643318004.25497455618),Kota Jakarta Barat. Exact Prime processor title,not Flex Prime or an accessory. Search and opened page agree;both are **three-month-old snapshots**. No Habis marker exposed does not prove stock. Condition,working state,selected variation,bundle,accessories,warranty,shipping/tax and checkout total remain unknown. Relative “Besok” delivery is stale;up-to-Rp10.000 late-delivery compensation is not deducted. |
| Separate sold-out hardware ask, checked2026-11-03 | **Rp18.910.000** | [SMOSYU MUSIC,shop397175630/item55362368361](https://shopee.co.id/Headrush-prime-i.397175630.55362368361),KotaBekasi. Search and direct page agree on **Habis** and ask in three-month-old snapshots;August4–6 delivery is stale. Title says Headrush Prime,not Flex Prime;no image inspection claimed. Condition,working state,variant,bundle,accessories,firmware,warranty,shipping/tax andcheckout unknown. Not an available condition-qualified price orcompleted sale. Late-delivery compensation up toRp10.000 is not deducted. |

These are separate qualified asks, not an authenticated used-to-new market range. Late-delivery compensation is not an additional product discount.

### Prime — global output buses and EQ boundaries

Checked **2026-11-03** in the already-saved [manufacturer Prime5.2 guide](https://cdn.inmusicbrands.com/Software/SGEE/52/HeadRush%20Prime%20-%20User%20Guide%20-%20v5.2.0.pdf),printedpp65,68. No new local download;the current web reader rejects the11.7MB file.

Advanced routing globally assigns Guitar,Alt Guitar,Guitar(2),Mic Dry,Drum Machine andPractice Tool to buses1–3. The advanced paragraph omits **Vocals**,although the basic routing list includes it;do not silently resolve that omission. Each hardware destination selects OUT1,OUT2,OUT1+2 orOUT3 in stereo,or SPLIT1/2 withbus1 left/bus2 right in mono. These are internal buses,not additional physical outputs orrig-block slots.

Global EQ separately targets XLR andquarter-inch pairs,with four parametric bands,on/off andlevel;outer bands select shelf/cut. It applies across rigs without rewriting their saved EQ. This doesnot establish headphone/USB EQ coverage,expression-pedal targeting orpower-cycle retention. No settings changed orhardware behavior tested.

### Prime — official sources and unresolved work

- [PR-P: Prime product, NAM statement, category lists and software links](https://www.headrushfx.com/products/prime/index.html).
- [PR-F: model-specific manufacturer FAQ](https://support.headrushfx.com/en/support/solutions/articles/69000834532-headrush-prime-frequently-asked-questions).
- [PR-M: original User Guide 5.2.0](https://cdn.inmusicbrands.com/Software/SGEE/52/HeadRush%20Prime%20-%20User%20Guide%20-%20v5.2.0.pdf). Locally extracted; top-panel printed p.6 rendered and inspected; mic-gain/ports/technical data read in their complete sections. Not all PDF illustrations were visually inspected.
- [PR-R: original 5.2.0 firmware notes, October 2026](https://cdn.inmusicbrands.com/Software/SGEE/52/READ%20ME%20-%20HeadRush%20Prime%20Firmware%20Update%20Instructions%20v5.2.0.pdf), including preceding version changes; [current manufacturer download index](https://www.headrushfx.com/downloads).
- [PR-S: manufacturer input/path allocation explanation](https://support.headrushfx.com/en/support/solutions/articles/69000834956-headrush-prime-what-are-the-new-signal-paths-for-rigs-).

Remaining: reconciled category inventory, factory/user rig capacity, IR file restrictions and capacity, main pixel/auxiliary screen specifications, explicit portable-power statement and condition/stock-qualified offers. This is a partial model record with preserved source conflicts.

Canonical root-level brand document for **MX5, Core and Flex Prime**. Unknown values are `?`, not No. MX5 and the additional Flex Prime price evidence were checked **2026-10-15**. Core and Flex Prime technical observations below retain their original **2026-10-14** dates and unresolved conflicts; consolidation is not a fresh certification of every specification. Prime remains a separate research lead, not a completed model.

### Prime — cabinet versus convolution IR limits, 2026-10-28

Read complete printed pp26–27,58 from the previously saved [original User Guide5.2.0](https://cdn.inmusicbrands.com/Software/SGEE/52/HeadRush%20Prime%20-%20User%20Guide%20-%20v5.2.0.pdf); no new download, visual inspection or device operation.

| Field | Exact scope / qualification |
|---|---|
| IR / cabinet library | Guide lists **300+ onboard cabinet IR files**. Cabinet IR blocks process2048 samples or truncate to1024 for lower DSP use. This is included content, not user-slot capacity or a guarantee of unlimited simultaneous IRs. |
| IR / convolution reverb | Separate **C-Verb** uses acoustic-space IRs: **50+ included**, typical.WAV/.AIF/.OPUS files; **one C-Verb instance per rig**, maximum loaded IR length **10seconds**. Only the first two channels of multichannel IRs are used; CPU demand depends on IR length. These limits are not cabinet-block limits or a complete accepted-file specification. |
| Memory / transfer restrictions | USB transfer ignores unsupported files and does not transfer folders or.zip/archive folders; supported files transfer directly. This does not determine the rig/user-storage ceiling. |

[Used item1149776042/54402465704](https://shopee.co.id/Headrush-Prime-Guitar-Multi-Effect-Amp-Modelling-Processor-Second-Bekas-i.1149776042.54402465704) reopened2026-10-28 as month-old cached text:explicitSecond/Bekas,**Rp15.400.000,Habis**,sellerBANGBONGMUSICBEKASI,Kab.Bekasi. Relative delivery and late-delivery voucher do not establish current stock or reduce the hardware ask. Accessories,grade,warranty and checkout remain unverified.

### Prime — IR browser and external-file dependencies

Checked2026-11-03 against manufacturer support text; no files downloaded or device operations performed.

- [Prime-specific IR loading guide](https://support.headrushfx.com/en/support/solutions/articles/69000836037-headrush-prime-loading-impulse-responses-for-your-rig): choose the Cabinet/IR model and1024/2048 processing quality,then **Load** opens a dedicated browser. It can navigate drives/Dropbox;the ordinary file browser cannot assign an IR to the rig. This guide is dated April7,2023 in the support-folder index;it is not proof every5.2 menu is unchanged.
- [Manufacturer missing-IR guidance](https://support.headrushfx.com/en/support/solutions/articles/69000849643-headrush-fx-faq-why-are-there-red-on-my-ir-s): a red question mark can mean the referenced IR is absent;the loader does not substitute a default. Obtain the required file where permitted,place it in Impulse Responses/User,reselect it in the block andsave the rig to retain the new location. Thus sharing a rig is not proof its external IR asset is included. This article is family-level guidance linked to Prime support,not a tested all-version guarantee.
- [Prime-named C-Verb support](https://support.headrushfx.com/en/support/solutions/articles/69000878423-prime-core-and-flex-prime-c-verb-reverb-file-missing-or-corrupt): an unassigned/removed reverb IR can produce the missing/corrupt-file message;select a valid file from Reverbs/Headrush/Spaces. Cabinet IR andC-Verb assets remain distinct.

These sources establish loading/dependency behavior,not resampling algorithms,user-file/rig ceilings orportable power. Existing accepted-format and10-second C-Verb limits retain their own sources/revisions. Exact currently stocked Shopee offers andauxiliary-screen specifications remain open.

### Prime — legacy-rig compatibility is directional

Checked2026-11-03 against [manufacturer backup compatibility guidance](https://support.headrushfx.com/en/support/solutions/articles/69000834915-headrush-prime-will-my-rig-backups-work-with-the-prime-). Prime accepts Pedalboard/Gigboard/MX5 rigs,setlists,IRs andblock presets,but importing Gigboard/MX5 rigs can remap footswitch assignments,usually toward the bottom three/four switches. **A rig created or edited andsaved on Prime cannot return to those older models,even without Prime-specific features**;unchanged older files retain their return compatibility. Preserve original files independently before editing;this is not a verified lossless round trip orfull-device backup. No transfer ordevice operation was performed.

[Separate factory-rig explanation](https://support.headrushfx.com/en/support/solutions/articles/69000848879-headrush-prime-and-core-where-are-all-the-preset-rigs-) explicitly distinguishes Prime/Core’s50 supplied rigs from the older models’270-file bank. The older bank’s approximately4MB file size does not establish Prime storage capacity orcurrent5.2 factory fill. Existing50-rig observation andnumerical-capacity unknown remain unchanged.
### Prime — MIDI switch edges and controller-table qualifications

Checked **2026-11-03** in the already-saved [manufacturer User Guide5.2.0,printedpp76–77](https://cdn.inmusicbrands.com/Software/SGEE/52/HeadRush%20Prime%20-%20User%20Guide%20-%20v5.2.0.pdf). Original complete table/explanatory text,not a device test ornew download.

| Field | Revision-specific evidence |
|---|---|
| MIDI / footswitch emulation | **CC49–60** correspond tophysical switches1–12. Send **127 press,then0 release**;press without release activates the assigned hold function. These are MIDI event values,not audio gain endpoints oradditional switches. Global OnPress/OnRelease settings remain separately qualified above. |
| MIDI / continuous targets | **CC1 internal EXP,CC2 external EXP;CC61/62/63 top/middle/bottom parameter knobs**,values0–127. CC14/15 switch internalA/B andexternalC/D. Emulating EXP isnot proof ofglobal output-volume assignment oranalog pinout compatibility. |
| MIDI / navigation | **CC16=Rig Up(previous),17=Rig Down(next);18=Bank Up(previous),19=Bank Down(next)**. Preserve the manual's direction labels;these are not memory-capacity limits. |
| MIDI / documented table defect | **CC104 Practice Tool Stop appears twice**. Treat it as a repeated row,not asecondstop command orproof ofan omitted mapping. |
| MIDI / controller transport | External MIDI gear uses **DIN input orUSB-A**;USB-A gear must beclass-compliant andrequire nodriver. This doesnot certify every MIDI controller,USB-B host behavior orM-VAVE analog wiring. |

Most other listed actions trigger onany0–127 value;the guide explicitly distinguishes the continuous targets andswitch press/release exceptions. No MIDI messages sent. Current OLED physical specifications,installed-library census,rig-storage ceiling andcondition-qualified hardware stock remain unresolved.


### Prime — NAM stereo quality, tail and level boundaries

Checked **2026-11-03** in the already-saved [original Prime User Guide5.2.0](https://cdn.inmusicbrands.com/Software/SGEE/52/HeadRush%20Prime%20-%20User%20Guide%20-%20v5.2.0.pdf), complete printedpp24–25. No new download ordevice operation.

| Field | Exact-revision limitation / qualification |
|---|---|
| NAM / quality versus routing | A2 **Mode Full/Lite** automatically becomes **Lite** andcannot be changed if more than two captures are loaded, **or a stereo effect precedes two separate NAM blocks**. A1 also disables this selector;the A2 Full/Lite quality choice is not an A1 architecture conversion. Existing two-Full/four-Lite maxima remain subject to these routing andDSP limits. |
| Practical / NAM tail limitation | **Reverb/Delay Tails unavailable for rig switching whenever any NAM block is present.** The guide suggests Switch Doubling for tails while switching captures inside the rig. This is not guaranteed tails between arbitrary NAM rigs,not a promise every effect spills over,andnot proof that an analog volume pedal attenuates the surviving tails. |
| NAM / level controls | Input andOutput each span **−20 to+20dB**. Input changes drive/dynamics;Output changes level. These are NAM-block controls,not universal global-volume endpoints. **Calibrate Input** uses capture metadata andis disabled without it. |
| NAM / output modes | **Raw** retains model-dependent output;**Calibrated** uses stored metadata ifavailable;**Normalize** automatically adjusts toward a target peak. No numerical target orstandardized loudness guarantee supplied. Capture calibration/normalization is separate from expression-pedal calibration andglobal assignment. |

This narrows practical NAM applicability without changing the12OLED hardware layout,native-versus-converted classification orhistorical factory library. Actual installed firmware,complete current category census,rig storage ceiling andqualified current Shopee hardware stock remain unresolved.
### Prime — visible reference list reconciliation

Checked **2026-11-03** against the [exact Prime manufacturer page](https://www.headrushfx.com/products/prime/index.html), first compact FX Overview list only; repeated illustrated cards are not counted again.

| Reference group | Printed header | Named rows | Distinct names within group |
|---|---:|---:|---:|
| HEADRUSH AMP MODELS | 53 | 53 | 53 |
| REVALVER AMP MODELS | 44 | 47 | 47 |
| HEADRUSH CAB MODELS | 15 | 15 | 15 |
| HEADRUSH CAB MICS | 10 | 10 | 10 |
| REVALVER CABS | 67 | 67 | 67 |
| REVALVER CAB MICS | 31 | 31 | 31 |
| VOCAL FX | 7 | 7 | 7 |
| OVERDRIVE | 16 | 18 | 18 |
| DISTORTION/FUZZ | 11 | 11 | 11 |
| EQ | 9 | 9 | 9 |
| COMPRESSOR | 6 | 6 | 6 |
| DELAY | 14 | 14 | 14 |
| REVERB | 7 | 7 | 7 |
| CHORUS | 7 | 7 | 7 |
| PHASER/FLANGER | 10 | 10 | 10 |
| VIB/TREM/ROTARY | 6 | 6 | 6 |
| WAH/FILTER | 8 | 8 | 8 |
| SYNTH | 4 | 4 | 4 |
| RHYTHMIC | 2 | 2 | 2 |
| PITCH | 7 | 8 | 7 |
| VOLUME/DYNAMICS | 5 | 5 | 5 |
| UTILITY | 3 | 3 | 3 |

ReValver’s47 includes **25 ON-1 Clean/Crunch/Lead**; its header still says44. Pitch repeats **Octaves**;deduplicating that name yields7, not proof that two same-named algorithms exist. The16 effect groups total **125 rows /124 distinct names**, excluding amps,cabs,mics,IRs and downloaded captures. These are dated website counts,not an installed-library certification or unique-algorithm total.

IR listing separately shows15 HeadRush families×20files=300 and15 Choptones files;families are not individual files. EQ shows9 names includingBASS EQ,GRAPHIC EQ,10 Freq EQ;their exact mapping tofirmware5.1 Graphic Bass EQ remains unresolved. The600+ marketing figure has a broader,unreconciled scope. No download ordevice test.


### Prime — versioned looper overwrite and continuity limits

Checked **2026-11-03** in the previously saved [manufacturer User Guide5.2.0,printedpp49–51](https://cdn.inmusicbrands.com/Software/SGEE/52/HeadRush%20Prime%20-%20User%20Guide%20-%20v5.2.0.pdf). Complete looper section read;no new download ordevice operation.

- **Insert conflict:** guidep49 says the selected section ofthe **top-most,last-added layer** is overwritten. The [Prime FAQ](https://support.headrushfx.com/en/support/solutions/articles/69000834532-headrush-prime-frequently-asked-questions) instead says allprevious layers. Preserve both;actual installed-version behavior isuntested.
- **Peel recovery:** holdPeel torestore thelast removed layer **before any further overdub**. This doesnot establish undo ofInsert.
- **Continuity:** guidep50 explicitly permits rig changes whileusing thelooper andcontinued playback after exiting its screen. This isnot a guarantee ofuninterrupted audio under every rig/DSP condition orpower-cycle retention.
- **Saved/imported loops:** SaveLoop andLoadLoop aredocumented;USBTransfer accepts.WAV/.MP3 placed in`/LOOPS/`. Export encoding,layer-preserving roundtrip andautomatic persistence remain unverified.

The FAQ-only destructive-edit row above retains its provenance;this revision-specific qualification narrows its applicability. Screen specifications,global EXP coverage,current stock andstorage ceilings remain open.

### Prime — offline backing tracks and duration scope

Checked **2026-11-03** against manufacturer support articles explicitly covering Prime/Core: [USB backing-track import](https://support.headrushfx.com/en/support/solutions/articles/69000860431-headrush-prime-and-core-how-to-play-backing-tracks-from-a-usb-flash-drive) and [track-duration qualification](https://support.headrushfx.com/en/support/solutions/articles/69000860432-headrush-prime-and-core-is-there-a-limit-to-how-long-a-backing-track-may-be-). These pages specify no firmware revision; this entry applies their Prime evidence without certifying installed firmware.

| Required field | Manufacturer evidence / limitation |
|---|---|
| Practice / offline import | **WAV or MP3** on USB flash storage → Browse → Storage → select file → **IMPORT,As Track**. Wait for the success indicator,then double-tap to load the player. Internet is unnecessary for this USB workflow;Dropbox streaming is a separate path. No arbitrary codec,filesystem ordrive-capacity compatibility inferred. |
| Practice / playback continuity | The support procedure permits returning to rig settings while the backing track continues playing. This establishes background playback during editing,not measured gapless playback for every preset change orautomatic power-cycle retention. |
| Memory / backing-track duration | Manufacturer states **no specific duration limit**,with available storage and length-dependent loading as practical constraints. USB tracks require import time;Dropbox requires a suitable connection. This is not infinite storage,nor a change to looper length/layer limits. |

Backing-track volume is distinct from the guitar rig Volume block. Direct analog EXP attenuation of this source,headphones,USB,tails andrecorded loops remains unverified. No files imported,software installed ordevice operated;current rig-storage ceiling andcondition-qualified Shopee stock remain unresolved.

### Prime — recorded-loop retiming and calibration-display scope

Checked **2026-11-03** against the Prime-named manufacturer support articles below. Neither specifies hardware firmware;these findings do not certify installed5.2 behavior.

| Field | Manufacturer evidence / limitation |
|---|---|
| Looper / recorded-loop tempo changes | [Core/Prime support](https://support.headrushfx.com/en/support/solutions/articles/69000864188-core-and-prime-can-i-change-the-tempo-of-my-recorded-loop-) documents enabling **Global Tempo Sync**,then **Quantise Changes**,to make Global Tempo retime the recorded loop. Tempo can use the main dial,an assigned onboard tap switch or**MIDI CC64**. The article doesnot establish pitch preservation,stretch-quality limits,quantization interval orindependent layer tempos. MIDI control isnot a passive analog footswitch connection. Core is named bythe source;only Prime’s record isupdated here. |
| Expression / calibration prompts on an individual display | [Prime calibration procedure](https://support.headrushfx.com/en/support/solutions/articles/69000851456-headrush-prime-how-to-calibrate-the-expression-pedal) enters calibration byholding**FS4+FS11 during startup**. Prompts appear above**FS6**;**FS12** learns toe-up,toe-down andmiddle positions,then saves. This is built-in-pedal calibration,not global volume assignment,automatic external-pedal calibration orproof of all-output attenuation. It supplies a documented use ofthe switch display,not its physical specifications. |

No calibration,recording,MIDI transmission,download ordevice operation performed. Existing OLED dimensions,rig-capacity,IR andcurrent-stock gaps remain open.

## VX5

<!-- comparison evidence begins -->
Checked **2026-10-17**. Vocal multi-effects: independently switchable AutoTune,harmony andFX. Guitar chord detection/thru does not qualify it for guitar multi-effects. Partial record.

| Required field | Finding |
|---|---|
| Built-in / external / toe expression | No built-in pedal or EXP/toe socket in complete hardware inventory. USB MIDI controls modes/presets;continuous expression assignment **?** [Manual,pp.6–10,18][VX-M] |
| Knobs / footswitches / buttons | **5 /2 /5**:4 front rotaries plus rear mic gain;Preset,Key,AutoTune,Harmony,FX buttons. Encoder press counted once;rear power,phantom andground-lift switches additional. Appendix lists only4 front knobs;rear description supplies fifth. [Manual,pp.6–10,22][VX-M] |
| Display | **1.8-inch/45.7mm full-color LCD**;touch **?** [Manual,p.22][VX-M] |
| Dimensions / weight | Manual **167 W×152 D×71 H mm;1.1kg**. Product instead **6.3 D×5.6 W×1.9 H inches;2.6lb**. Unresolved hardware/revision/measurement difference;mass basis unstated. [Manual,p.22][VX-M], [Product][VX-P] |
| Simultaneous blocks / routing | Fixed FX order **compressor→Flavor→chorus→reverb→delay**, alongside AutoTune/harmony. Not freely movable blocks. Product says arbitrary sequencing,conflicting with FAQ's explicit fixed order. [FAQ][VX-Q], [Product][VX-P] |
| Category choices | Manual1.3: **4 compressor,7 Flavor,5 chorus,5 reverb,7 delay** choices;delay1–4000ms. Harmony: **7 instrument-following range choices**,or **11 fixed interval/combination choices** with Source Off;these are choices,not11 simultaneous voices. Key menu has12 pitchclasses,10 scales,5 vocalranges. Support says **compressor requires firmware≥1.3.1**;linked update PDF saysconfirm1.2.2 butalso describes compressor addition:version conflict retained. [Manual,pp.14–16][VX-M], [Compressor support][VX-C] |
| Factory / user memory | **250 total**,99 factory-filled and151 blank;editable saves overwrite selectedslots. Last selectedpreset retained afterpowercycle. [Product][VX-P], [FAQ][VX-Q], [Manual,pp.6,12][VX-M] |
| Synth / acoustic simulation | Vocal pitchcorrection,harmony andvoice coloration;independent synth/acoustic simulator **?**. Guitar input is unprocessedthru,not modeledguitarFX. [FAQ][VX-Q] |
| Audio/control I/O | XLR mic,+48V;XLR main,groundlift;¼″guitar in/thru;phones;USB-B;DC. Rear/manual text specifies3.5mm phones,appendix says¼″;product agrees3.5mm. Guitar rear text saysTS,technical table permitsTRS/TS. No DIN MIDI/FXloop listed. [Manual,pp.9–10,21–22][VX-M], [Product][VX-P] |
| Power / battery / USB | **9V DC,1A,center-negative,2.1mm barrel** adapter rating;actualdraw,battery andUSB-powered operation **?** [Manual,p.22][VX-M] |
| Editor / USB audio | Stereo24bit48kHz USB audio;computer receives post-micFX stereo;computer playback mixes into mainout afterprocessing. UpdatePDF callsWindows11/macOS audio class-compliant;Windows10 networkingdriver concerns updater,not audio. FAQ namescomputer,iPhone,iPad/tablet. [Update PDF,p.2][VX-U] Browser viaUSB is documented for **firmware updates**,not full editor;manual namesWindows11/macOS13–15. Windows networkingdriver distinct fromaudiodriver. Full editor/Linux/Android support **?** [FAQ][VX-Q], [Manual,pp.10,17][VX-M], [Compressor support][VX-C] |
| Looper / scenes / practical limits | A/B switches individualeffects withinpreset;Talk bypasses vocalFX. Harmony followskey/scale orinstrumentchords. Looper,drums,scenes anduninterruptedpresetswitching **?** [FAQ][VX-Q] |
| IR / NAM / captures | No documentedloader in checkeduserguide;IR,nativeNAM,convertedNAM,proprietarycaptures **?**. Prime/Core features not assigned. [Manual][VX-M] |

### VX5 — separate IDR offers

| Class | Amount | Exact hardware offer and qualifications |
|---|---:|---|
| Historical indexed hardware ask;condition unverified;**sold out** | **Rp4.400.000** | [Seven Stereo Music & Audio Store,shop16879370/item40920257841][VX-O1],Bandung. Direct crawler obtained2026-10-17,cachelastweek;delivery6–8October supersedes earlierJulycache. Habis;condition,variant,bundle,adapter,warranty andcheckoutstock **?**. Late-deliveryvoucher up toRp10.000 not deducted. |
| Separate historical indexed ask;condition unverified;**sold out** | **Rp4.631.200** | [GALERI MUSIK SIMFONI_PIM,shop1030145984/item43570585814][VX-O2],JakartaSelatan;earlier3monthindex,exactURLreopened2026-10-17. Condition,variant,bundle,warranty **?**;not a verifiednew/usedrange. |
| Verified used offer | **?** | Not established |
| Verified new offer | **?** | Neither ask has verifiedsalecondition |
<!-- comparison evidence ends -->

### VX5 provenance and remaining work

OwnUserGuide1.3 read viawebtext;no localdownload. Productstill links1.2.2 updater whilebanner/supportdocument1.3.1;compressor availability remainsfirmwarequalified. Conflictingdimensions,mass,connector sizes andchain-order language retained. Next:reconcile updatePDFversion labeling against1.3.1 support,exactsimultaneouslimit,currentofficialeditor/OS support andcondition-qualifiedoffers. Do not reclassify asguitar justbecauseGuitarThru exists.

[VX-P]: https://www.headrushfx.com/products/vx5-autotune/index.html
[VX-Q]: https://support.headrushfx.com/en/support/solutions/articles/69000870979-headrush-autotune-vx5-frequently-asked-questions
[VX-M]: https://cdn.inmusicbrands.com/HeadRush/vx5/AutoTune%20VX5%20-%20User%20Guide%20-%20v1.3.pdf
[VX-C]: https://support.headrushfx.com/en/support/solutions/articles/69000880616-vx5-the-compressor-is-missing-from-the-fx-menu
[VX-O1]: https://shopee.co.id/Headrush-VX5-Vocal-Effects-Pedal-with-Antares-AutoTune-i.16879370.40920257841
[VX-O2]: https://shopee.co.id/HEADRUSH-VX5-VX-5-Vocal-Processing-Pedal-with-AutoTune-by-ANTARES-i.1030145984.43570585814

### VX5 update-document audit — 2026-10-17

The linkedthree-page updateinstructions say to confirm **1.2.2** onboot (p.1),yet p.3 adds compressor and simultaneousFX. Manufacturer support separately dates compressor to **1.3.1**. The PDF also uses an unrelatedinternalmodelcode for compressor;do not treat thatcode as a VX5variant. Its contents supportserialmultiFX,but do notresolvewhich firmwareintroducedeachfeature. [Update PDF][VX-U], [Compressor support][VX-C]

Preset retention is saved afterfive seconds orpower-button shutdown. MIDI isreceived onallchannels:CC32 selects128/122-preset banks,ProgramChange selectswithinbank;CC16 controlsA/B,CC17 Talk. Neither thismapping norbrowserupdater proves a full editor. [Update PDF,p.2][VX-U], [Manual,p.18][VX-M]

[VX-U]: https://cdn.inmusicbrands.com/HeadRush/vx5/VX5-Day1Firmware_v3.pdf

### VX5 — guitar-thru exclusion and published latency examples

Checked **2026-10-28** in the [manufacturer FAQ][VX-Q]. Guitar input passes through without added gain,coloration orsignal changes;it supplies harmony guidance,not guitar multi-effects. Retain vocal-only membership,outside normal-guitar expression-volume table. Published connector inventory includes no analog EXP;dedicated3.5mm TRS phones can also monitor stereo output. USB preset/mode automation does not establish continuous expression volume.

FAQ latency examples are **6ms Empty/preset250,10ms Hard Tune/preset1,31ms Stress Test/preset99**. These are manufacturer examples,not measurements here oruniversal bounds;measurement conditions andfirmware are unstated. Talk mode bypasses vocal FX;it does not prove guitar-volume control. Manual167W×152Dmm fails preferred depth;product dimensional conflict remains open. Direct-pedal position/range/recall are inapplicable to documented inventory;headphone/bypass/tail/recorded-loop pedal attenuation andexact onboard preset down/up remain unverified.
