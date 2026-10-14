# HeadRush Core — Shopee-first research

Checked **2026-10-14**. **Partial record**, not independently tested. Guitar/bass/vocal multi-effects; **large**, no built-in expression. This is Core, not Prime, Flex Prime, MX5 or Gigboard. Next queued model: **Flamma FV01**.

## IDR listing evidence

| Condition | Asking price | Evidence |
|---|---:|---|
| Retail listing; detailed condition/stock not established | **Rp15.120.000** | [ROCKPIZZ MUSIC, Shopee item 44463652142, shop 440477624](https://shopee.co.id/HEADRUSH-CORE-GUITAR-MULTI-EFFECT-AMP-MODELER-VOCAL-PROCESSOR-i.440477624.44463652142) |
| Used | **?** | No independently verified used offer in this pass |

The fetched listing identifies actual Core hardware and the displayed price, but its JavaScript-limited body does not establish accessories, warranty, selected variant or checkout stock. Delivery/voucher text is not a discount applied to this price. This is one asking-price observation, not a used-to-new market range or completed sale.

## Hardware and required fields

| Field | Finding | Evidence |
|---|---|---|
| Expression | **No built-in pedal**; external 6.35 mm TRS EXP and separate TS TOE input | [FAQ][faq] |
| Controls | **5 footswitches**; current specification lists **3 front rotary controls** (main, headphones, navigation encoder). Complete rotary/button inventory including rear controls **?**; encoder press not double-counted | [Product technical specifications][product] |
| Display | **One 7-inch full-color touchscreen**; no Prime-style auxiliary OLED strips | [Product][product], [FAQ][faq] |
| W × D × H | **408.4 × 234.6 × 67.0 mm**; **3.80 kg** | [Product][product] |
| Power | **12 V DC, 3 A, center-positive adapter input** in current technical specifications; FAQ instead says IEC, an unresolved documentation error/conflict. Battery/USB-powered operation **not established** | [Product][product], [FAQ][faq] |
| Presets | FAQ states **50 supplied factory rigs**; current firmware factory total and maximum user storage **?** | [FAQ][faq] |
| Processing | **14 rig blocks**, subject to routing/DSP/model limits; guitar/vocal paths supported. These are not 14 physical footswitches | [FAQ][faq] |
| Synth | **Yes**: Hybrid Synth, Electric Piano and DB-33 Organ; website Synth heading also includes Ambi-Verb | [Product model list][product], [firmware history][fw] |
| Acoustic simulation | **Yes**, Acoustic Sim; separate Acoustic Pre is not the same effect | [Product model list][product] |
| IR loading | **Yes**, third-party WAV/AIFF; FAQ specifies up to 192 kHz/32-bit files and two IRs per block. Storage/sample-length limit **?** | [FAQ][faq] |
| NAM | **Native**, architecture-qualified; details below | [5.2 release notes][fw], [Cloud formats][cloud] |
| Other captures | Onboard amp/pedal cloning; proprietary HeadRush/ReValver clones and SuperClones, separate from NAM | [Product][product] |
| Editor | Wi-Fi **browser editor: Windows/macOS/iOS/Android** documented; Linux not established. Windows/macOS firmware updaters and USB file transfer are separate functions | [Release notes, printed p.7][fw] |
| USB audio | **6-in/4-out**, 24-bit 44.1/48/96 kHz; recording/reamping; Windows driver, macOS driverless | [FAQ][faq] |
| Live features | Scenes, trails; looper **50 layers, 5 minutes/layer, 20 minutes total per loop**; drum machine | [FAQ][faq], [Product][product] |

## Connections

Manufacturer evidence lists: 6.35 mm TS guitar input; XLR/6.35 mm combo mic input with switchable **48 V phantom**; stereo pairs of XLR and 6.35 mm main outputs; 3.5 mm headphones and aux; stereo TRS FX send/return; EXP and separate TOE; TRS amplifier-control output; DIN MIDI IN/OUT; USB-A storage/MIDI and USB-B computer; Wi-Fi and Bluetooth audio. [Product][product], [FAQ][faq].

The published port bullets incorrectly call SEND an input and RETURN an output. They are retained here with their functional directions corrected, rather than copying the reversal. FAQ also conflicts with the product's DC power description. Obtain the matching Core manual/rear-label confirmation before treating the port/power list as a fully reconciled hardware specification.

## Firmware and category-count evidence

**Firmware 5.2.0, October 2026** is identified on printed p.1 of the official release notes, visually checked. Its p.3 specifies **two A2 Full captures or four A2 Lite captures across two NAM blocks**, running natively. Version 5.1 introduced A1 Standard/Lite/Feather/Nano and A2 support; do not generalize the new A2 concurrency limits to every A1 architecture. The cloud page independently lists supported formats. [Release notes][fw], [Cloud][cloud].

The website's category headings advertise: HeadRush amps53; ReValver amps44; HeadRush cabs15/mics10; ReValver cabs67/mics31; vocal7; drive16; distortion/fuzz11; EQ9; compressor6; delay14; reverb7; chorus7; phaser/flanger10; vibrato/tremolo/rotary6; wah/filter8; synth4; rhythmic2; pitch7; volume/dynamics5; utility3. **These are website-heading figures, not a verified firmware-5.2 installed total.** [Model list][product].

Conflicts prevent summing a definitive grand total: the drive list has **18 entries under a 16 heading**; pitch shows **8 entries under a 7 heading**, including duplicate/truncated names; later detailed EQ heading differs; 5.1 added an amp and Graphic Bass EQ not reflected consistently in the page. Per-category firmware reconciliation remains pending. The seven named vocal choices include correction, de-essing, distortion, doubling, harmony, stutter and vocoder. Do not count microphone routing utilities as seven extra independent blocks.

## Resume gaps

Confirm complete physical controls, actual power-label/manual consistency, current factory/user storage, installed category totals and used offers. The download index links a 5.2 user guide, but it could not be fetched in this pass; **the guide was not read**. The accessible 5.2 release notes and current Core page were used instead. No arbitrary sibling-model values fill these gaps.

[product]: https://www.headrushfx.com/products/core/index.html
[faq]: https://support.headrushfx.com/en/support/solutions/articles/69000844379-headrush-core-frequently-asked-questions
[fw]: https://cdn.inmusicbrands.com/Software/SGEE/52/READ%20ME%20-%20HeadRush%20Core%20Firmware%20Update%20Instructions%20v5.2.0.pdf
[cloud]: https://www.headrushfx.com/cloud/index.html
