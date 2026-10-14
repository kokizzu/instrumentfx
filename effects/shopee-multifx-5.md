# Shopee multi-effects — recovered Hotone, MOOER and Line 6 batch

[All comparisons](README.md) · [Scope](SCOPE.md) · [Resume](RESUME.md)

**Integrated 2026-10-15; underlying observations dated 2026-10-14.** These six complete first-pass findings were committed individually before an interrupted response. Integration is not a new verification of every specification, current firmware, price or stock. All six remain **partial**. The previous 80 active records plus these six make **86 active records**, before subsequent additions. Six scope exclusions remain archived and are not counted.

The linked model records carry all required field groups, full source references, category-count details, firmware restrictions, connection lists and unresolved evidence. Unknown is not No. These summaries do not replace those qualifications.

## Hardware and displays

K/F/B = rotary controls / main footswitches / separate buttons. Encoder pushes count once; toe/power switches are separate. Dimensions are unit dimensions, not installed cable clearance.

| Model / full record | Built-in / external expression | K/F/B | Published dimensions, mm; weight | Main display |
|---|---|---|---|---|
| [Hotone Ampero MP-100][mp100] | Yes / EXP2 | 5/4/1; toe unverified | W320×D147×H46; 1408 g | 4-inch color, 800×480, touchscreen |
| [Hotone Ampero II MP-350][mp350] | Yes / EXP/CTRL count conflicting | ?/4/? | W330×D157×H61; 1695 g | 5-inch color, 800×480, touchscreen |
| [MOOER GE1000 non-Li][ge1000] | Yes + toe / no dedicated EXP socket in checked inventory | 2/5/17 | L337×W170×H57; 1.9 kg | 5-inch color LCD touchscreen |
| [Hotone Ampero II Stage MP-380][mp380] | No / 2 EXP/CTRL | 5/8/1 | W301×D180×H58; 1895 g | 5-inch color, 800×480, touchscreen |
| [Line 6 HX Stomp XL][xl] | No / shared EXP1/2–FS7/8 | 6/8/4 | Manufacturer chart W316×D120×H68; 1.5 kg; chart-render limitation in finding | 2.4-inch color LCD; explicit touch specification unverified |
| [MOOER GE150 Pro non-Li][ge150pro] | Yes + toe / no dedicated EXP socket in checked inventory | 3/4/6 | L310×W153×H55; 1.1 kg | 2.8-inch color LCD; explicit touch specification unverified |

All six exceed the repository's medium footprint in at least one dimension and therefore classify as **large**, even where a manufacturer markets them as compact. GE1000 Li, GE150 Pro Li, non-XL HX Stomp and the other Ampero models are separate hardware records.

## Processing, storage and loading

| Model | Processing and memory | IR / NAM / captures |
|---|---|---|
| MP-100 | 9 simultaneous modules; 99 factory + 99 user. Earlier manual and current marketing counts differ; explicit acoustic simulator documented | 1024-sample user IRs; firmware 5.2 Sound Clone: 10 stored, one active. Do not infer native NAM from proprietary clone import |
| MP-350 | 12 simultaneous slots, 17 module types, dual routing; 300 locations with 4 scenes per patch; factory/user split unverified | 50 user IRs, 1024/2048 samples; native NAM A2 Lite is firmware-qualified; Tone Catch/Sound Clone separate |
| GE1000 | 14 DSP-limited slots, 11 module categories in checked manual; 255 editable locations; revision-specific category counts retained | 50 IR slots up to 2048 samples; 50 separate MNRS amp slots; native NAM A2 Lite in dated manufacturer roadmap, exact installed build unverified |
| MP-380 | 12 simultaneous slots, dual routing; 300 editable locations with 5 scenes; older and newer category inventories differ | 50 IR slots, 1024/2048 samples; native A2 Lite from specified Stage firmware; proprietary capture separate |
| HX Stomp XL | 8 DSP-limited blocks; 128 editable presets, 4 snapshots each. Manual 3.80 transcription: 274 named effects across 10 categories, plus looper and separate amps/cabs. Acoustic Sim and synth algorithms documented | 128 IR-library locations, 1024/2048 samples; no NAM/capture support established in checked 3.80 evidence |
| GE150 Pro | 9 modules; 200 factory-filled editable locations. Firmware 1.5 list: FX12, drive28, amp55, cab26, NS3, EQ4, MOD25, delay9, reverb8 = 170, including amps/cabs | 20 user cab IRs at 512 samples after 1.5; 20 separate amp slots; documented NAM A2 **conversion**, not native loading |

Effect-library totals, available module categories and simultaneous processing limits are different quantities. Firmware versions and primary-source disagreements remain in each linked finding, not silently resolved here.

## Connections, power and apps

| Model | Connection / software highlights | Documented power |
|---|---|---|
| MP-100 | Mono input, stereo quarter-inch and XLR outs, dedicated phones/aux, MIDI IN, USB-B, EXP2; Windows/macOS editor | 18 V center-negative, 500 mA maximum; USB/battery operation not established |
| MP-350 | Independent instrument/mic paths, 48 V phantom, stereo loop, XLR/quarter-inch outs, DIN MIDI, USB-C; Windows/macOS editor; 8-in/8-out USB audio | 9–18 V center-negative; maximum 1.2 A at 9 V; EXP socket-count conflict remains |
| GE1000 | Mono input, stereo TRS loop, XLR/quarter-inch outs, phones, single selectable DIN MIDI IN/OUT, USB-C; desktop Studio and mobile Cloud functions distinguished | Non-Li 9 V/1 A center-negative supply; no internal Li battery; USB powering unverified |
| MP-380 | Instrument/mic input with phantom, stereo loop, XLR/quarter-inch outs, 3.5 mm TRS MIDI IN/OUT, 2 EXP/CTRL; Windows/macOS/iOS/Android editor; 8-in/8-out USB | 9–18 V center-negative; maximum 1.4 A at 9 V; USB/battery operation unverified |
| HX Stomp XL | Stereo inputs/outs, stereo-send/two-return loop, dedicated phones, DIN MIDI, USB-B; HX Edit Windows/macOS. Manual distinguishes 8 recording and 6 active playback channels | Supplied DC-3-family supply; panel 9 V/3 A, not measured draw; polarity/USB-operation gap retained |
| GE150 Pro | Mono input, stereo outs, separate phones/aux, USB-C; Windows/macOS editor; USB audio is not mobile editing | Non-Li 9 V center-negative, published 300 mA; no internal Li battery; USB powering unverified |

## IDR observations and original commits

These are **2026-10-14 listed/indexed asking prices**, not current checkout verification. Used offers were not established for these six. Exact seller/item links, condition gaps, cached delivery dates and accessories are in the model findings. A listed price does not authenticate a seller or establish a completed sale.

| Model | Used IDR | Retail observation | Original model commit |
|---|---|---|---|
| MP-100 | ? | Rp7.535.000, listing retrieved; detailed condition/stock unconfirmed | `95075d2b802d2c8ef5374426fd8f3d66ad218451` |
| MP-350 | ? | Rp11.900.000, indexed; direct reopening failed | `4bcf30a87ee202f6e387d8680188a6f12944f047` |
| GE1000 | ? | Rp7.520.000, indexed Shopee; separate retailer observation same amount | `671fc47896c8c6544598926e789ad4a0be19c1eb` |
| MP-380 | ? | Rp13.685.000, indexed; direct reopening failed | `fe82a572c99c65f074b2ee5d13e870c7004b51a3` |
| HX Stomp XL | ? | Rp14.900.000, cached indexed ask; not active-stock proof | `b4ba5b5559dcdd33b196153d4557408d71cbb89f` |
| GE150 Pro | ? | Rp2.750.000, **sold out**, historical ask only | `be016fb50f1df0642ef1c06890a19a3ba3574fb7` |

**Continuation:** remaining GE150 Plus/Plus Li/Max/Max Li variants, GE1000 Li, and missing ever-owned models. Preserve the original display/IDR queue; the recovery does not complete those outstanding fields. New model findings must be committed immediately and their next step recorded.

[mp100]: findings/2026-10-14-hotone-ampero-mp100.md
[mp350]: findings/2026-10-14-hotone-ampero-ii-mp350.md
[ge1000]: findings/2026-10-14-mooer-ge1000.md
[mp380]: findings/2026-10-14-hotone-ampero-ii-stage-mp380.md
[xl]: findings/2026-10-14-line6-hx-stomp-xl.md
[ge150pro]: findings/2026-10-14-mooer-ge150-pro.md
