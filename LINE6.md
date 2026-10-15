# Line 6 multi-effects

Root-level brand comparison. **Checked 2026-10-15.** POD Go Wireless and POD Express Guitar are newly researched here; the standard POD Go profile is consolidated from its existing source-backed record without adding another model to the inventory. Other legacy Line 6 records still require consolidation; no whole-repository migration claim is made. No GitHub Actions workflows are used.

## POD Go and POD Go Wireless

Both are guitar/bass multi-effects with a semi-fixed serial path and built-in expression. **Shared specifications are explicitly supported by Line 6's Wireless FAQ**, which says the ordinary POD Go documentation also covers Wireless unless marked otherwise. This is not an inferred similarity between unrelated hardware. Both records remain partial.

### Hardware, display and expression

| Field | POD Go, standard non-Wireless | POD Go Wireless |
|---|---|---|
| Built-in expression | Yes, with toe switch | Yes, with toe switch |
| External expression / switches | One shared TRS **EXP2 / FS7,8** input; suitable Y cable supports two external momentary switches | Same explicitly documented family connection |
| Knobs / footswitches / buttons | **8 / 8 / 4**: upper/lower encoders, volume, five parameter knobs; up/down,A/B/C/D,Mode,Tap switches; Home/View,Action,two Page buttons. Toe and power switches separate; encoder presses counted once | Same controls; wireless indicators on main screen are not additional physical buttons |
| Display | **4.3-inch color LCD**; explicit touchscreen specification **unverified** | Same display; do not infer touch from color or lack of touch from knob navigation alone |
| Published dimensions | Official Japan **88 H ×230 W ×359 D mm**; horizontal axis labels appear counterintuitive for the illustrated orientation. Official Yamaha Singapore standard-model table gives89 mm height: retain1 mm disagreement | Same Japanese family envelope; do not replace the Wireless mass with the standard mass |
| Weight | **2.35 kg** | **2.5 kg** |
| Size classification | **Large** under either horizontal orientation | **Large**; cable and pedal-travel clearance are additional |
| Built-in instrument wireless | **No** | **Relay receiver plus included G10TII transmitter**, transmitter charging through GUITAR IN and rear storage well. Older G10T is supported with updated firmware; other Relay transmitters are not promised compatible |

Sources: [PG-P], [PG-M], [PG-J], [PG-Y], [PG-W]. The normal GUITAR IN remains usable on Wireless. Published envelope figures are not a millimetre-accurate drilling template.

### Processing, memory and loading — applies to both models

| Required field | Evidence-backed specification / unresolved detail |
|---|---|
| Simultaneous processing | **10 semi-fixed blocks**: amp/preamp, cabinet/IR, preset EQ, wah, volume, FX loop and **four freely selected effects**, DSP-limited. Input gate and output level/pan are additional functions, not unlimited effect slots. Serial only; no independent parallel internal chain. [PG-F,PG-M] |
| Presets | **256 overwriteable locations**, Factory128 and User128, with **four snapshots per preset**. Either setlist can be overwritten; Factory does not mean read-only. Current factory-filled subset is not separately established. [PG-M] |
| Acoustic simulation | **Yes: Acoustic Sim**, an optional EQ-category effect. It is excluded from the fixed Preset EQ choices, so it consumes a selectable effect slot. Acoustic simulation is not merely an acoustic amp. [PG-L,PG-M] |
| Synth | **Yes**, named algorithms in Pitch/Synth. Exact current algorithm-by-algorithm inventory and amp/cab subtotals still require reconciliation with the firmware-matched model list. [PG-L] |
| User IRs | **128 IR library locations**;1024-point processing per the official Yamaha specification; WAV import with POD Go Edit. Cab and IR share one processing position. Complete source-file conversion restrictions remain untranscribed. [PG-Y,PG-F] |
| NAM / captures | Native NAM, converted NAM and user amp-capture import **not established** in the checked documentation. Helix-derived amp models and cabinet IR import prove none of these capabilities. |
| Editor | **POD Go Edit Windows/macOS**, full preset/IR editing and management. Hardware2.50 needs Edit2.50 for its newly added models. iOS USB audio is not a mobile editor; Android/Linux full editors are not established. [PG-P,PG-R,PG-M] |
| USB audio / MIDI | **4-in/4-out,24-bit**, dry recording/reamping and USB MIDI; Windows ASIO driver. Mac class-compliant audio defaults to48 kHz; other rates require the documented driver. Complete supported-rate set is not independently transcribed. [PG-M] |
| Power | Supplied **DC-3h family adapter,9 V,3 A,center-negative**. This is an adapter specification, not measured draw. Internal floorboard battery operation and USB-bus-powered operation are not established. **Wireless transmitter battery is separate from the floorboard's power source.** [PG-J,PG-A,PG-P] |

### POD Go family category-choice evidence

Preserved from the existing standard-model research, which transcribed Line 6's official POD Go model-list page on2026-10-15, not the larger HX/Helix library. Shared firmware applicability to Wireless is independently confirmed by [PG-W,PG-R]. Mono/stereo implementations are not counted twice; separate HX/Legacy entries remain distinct.

| Category | Named entries / qualification |
|---|---:|
| Distortion |55|
| Dynamics |18|
| EQ effects |8; fixed Preset EQ offers7 because Acoustic Sim is excluded|
| Modulation |55|
| Delay |41 named entries **plus one blank-name table row**, unresolved|
| Reverb |23|
| Pitch/Synth |24|
| Filter |15|
| Wah |11|
| Volume/Pan |4|

No definitive grand total is claimed from an incomplete delay/cabinet inventory. Amp/preamp and cabinet subtotals remain unreconciled with the current page. **Firmware2.50 was released2025-01-23**, not October2026; its official notes add11 guitar amps,2 bass amps,11 guitar cabinets,2 bass cabinets and2 effects for **both** hardware variants. The added effects include Regal Bass DI and Teardrop Bass Q. Preserve the firmware context; do not add these again to a webpage count already incorporating them. [PG-L,PG-R]

### Connections and practical features — both models

One6.35 mm mono GUITAR IN; one external EXP/footswitch TRS socket; stereo TRS SEND and RETURN; two balanced/unbalanced6.35 mm MAIN OUTs; separate mono AMP OUT; dedicated6.35 mm stereo headphones; USB-B and DC. RETURN can become an always-on stereo aux input. No microphone/XLR/phantom, physical DIN MIDI or separate3.5 mm aux socket in the complete inventory. [PG-P,PG-M]

AMP OUT can tap the signal before Cab/IR while the main outs retain cabinet processing. This is **not** a second independent effects chain. Four-cable-method use and external stereo effects insertion are documented. [PG-P]

Looper consumes one of the four optional effect slots: **40 seconds mono/20 seconds stereo at full speed;80/40 seconds at half speed**, with one-switch and six-switch implementations documented in the2.50 manual. Yamaha's store comparison mentions Shuffling Looper but the model list/manual used here do not establish it; that remains a source conflict rather than a verified extra algorithm. Tuner,snapshots,trails and USB MIDI are documented; an internal drum machine is not established. Manufacturer describes snapshot changes without audio dropouts or disruption of delay/reverb trails; this is not a measured whole-device latency or blanket preset-switching guarantee. [PG-M,PG-Y,PG-P]

### Wireless-specific operation

Line 6 specifies **up to30 m/100 ft line-of-sight** and about **seven hours transmitter playing time**, both manufacturer ratings rather than independent tests. The floorboard needs its own supply. RF antennas are above the expression-pedal toe area. Wireless reliability depends on RF conditions; do not cover the antenna or assume arbitrary crowded2.4 GHz conditions meet the rated range. [PG-W]

GUITAR IN charges the transmitter; the separate rear well stores it. Leaving the transmitter in the charge port while the processor is off slowly discharges it, so the storage well is the documented storage location. Wireless accepts Guitar,Wireless or Guitar+Wireless input selections; ordinary POD Go presets are compatible and their Guitar input is automatically converted to Guitar+Wireless when imported. USB3/4 is a reamp source; USB1/2 is monitoring that bypasses processing. Cable Tone and Wireless Gain are separate settings, not additional audio-effect blocks. [PG-W]

### Separate IDR evidence

All observations retain their original2026-10-15 review date. Indexed/cached listings do not establish checkout stock, condition or seller authenticity. A sold-out ask is not a completed sale; voucher compensation is not an applied product discount.

| Exact model / condition | Amount | Source and limitation |
|---|---:|---|
| Standard POD Go, retail indexed ask | **Rp7.704.000** | [Nuansa Musik-named store,shop51110469/item9145739709](https://shopee.co.id/Yamaha-Line-6-POD-GO-Multi-Effects-Guitar-Processor-i.51110469.9145739709). Existing research recorded older August–September delivery dates and failed subsequent reopening. Preserved evidence, not a new stock verification in this consolidation. |
| Standard POD Go, explicit SECOND/BEKAS, SOLD OUT | **Rp5.000.000** | [Pomade.borneo,shop7513711/item18366387490](https://shopee.co.id/LINE-6-POD-GO-Floor-Processor-Multi-Effect-%28SECOND-BEKAS%29-i.7513711.18366387490). Historical used ask, not an active offer or proven sale. |
| **POD Go Wireless**, retail indexed ask | **Rp11.130.500** | [melodiasby,shop158144224/item27772459064](https://shopee.co.id/Line6-Pod-Go-Wireless-Multi-Effect-i.158144224.27772459064). Re-found in current search, but June29–July1 cached delivery text is not October stock. Exact condition, transmitter/bundle contents, warranty and shipping remain unverified. |
| POD Go Wireless, condition-verified used | **?** | No suitable current used observation established. Standard-model used price is not transferred to Wireless. |

Do not combine these variants into one used-to-new range. No guessed currency conversion or percentage-of-new used-price estimate is used.

### Official sources and preserved provenance

[PG-P] [Official family product and numbered controls](https://line6.com/podgo/).

[PG-W] [Official Wireless FAQ](https://kb.line6.com/pod-go-wireless-faq), explicit shared-documentation rule and receiver/transmitter differences.

[PG-F] [Official POD Go FAQ](https://kb.line6.com/pod-go-faq); launch prices and launch library totals are not current observations.

[PG-L] [Official model list](https://line6.com/podgo-models/); incomplete row and count qualifications retained above.

[PG-R] [Official2.50 release notes](https://kb.line6.com/pod-go-2-50) and [official manual index](https://line6.com/support/manuals/podgo), covering both variants and matching editor generation.

[PG-J] [Official Japanese product page](https://line6.jp/podgo/), published dimensions and separate2.35/2.5 kg masses.

[PG-A] [Official DC-3h specification](https://line6.jp/effects-pedals/accessories/).

[PG-Y] [Official Yamaha Singapore specification](https://shop.sg.yamaha.com/products/pod-go.html), preserved1 mm height and Shuffling Looper disagreements.

[PG-M] Manufacturer-authored **2.50 Owner's Manual,RevG,2025**, [original manual text mirror](https://manuals.plus/m/ce56ac3123bea01e1af09c67ee23bbacde033cc732eecebac95132e123405944): pp.6–8 controls/ports,13 blocks,15–16 overwriteable setlists,31–33 looper/EQ,45–47 USB. The previous standard-model research could not complete PDF rendering and did not claim visual inspection. The official manual index was rechecked for this consolidation; a fresh successful PDF visual inspection is not claimed. Generated mirror FAQs are not evidence.

The existing standard record originated in commit `4f82a0b2893f2ec4b9bf7a01a45da394acca1164`, source blob `14f1c485763e10810e2f4ee673f41436edc6970f`. Its fields,prices,source URLs,known conflicts and incomplete-verification qualifications are retained here. The old file is not deleted until full migration/link validation. Consolidation does not count standard POD Go twice.

## POD Express Guitar

**New model, checked2026-10-15.** The2024-generation POD Express Guitar is not the older Pocket POD Express, POD Express Bass, or POD Express Black. It is a fixed-chain guitar multi-effects processor; no built-in expression. The current edit application must not be omitted because an older launch document mentioned only updating.

| Required field | Verified value / explicit remaining gap |
|---|---|
| Expression | No built-in pedal; **one TRS VOLUME/FS3,4 socket** accepts a volume expression pedal, two external switches, or a pedal plus one switch with the specified cable. Arbitrary expression control of every effect parameter is not established. [PE-G,PE-M] |
| Physical controls | **6 rotary /2 footswitches /1 button**: AMP push-encoder,four effect knobs,side volume thumbwheel;ON and TAP;ALT button. Encoder press is not a second button. [PE-G] |
| Screen | **No graphical or numeric screen**. Seven multicolor LED segments and switch indicators show state/tuning/parameters; they are not a color LCD. Screen diagonal/color-mode N/A; touchscreen No. [PE-G] |
| Dimensions / mass / size bin | Manufacturer-backed W×D×H and mass **not established in the inspected primary sources**. Do not promote reseller92×130×56mm/350g to a verified specification or estimate from photos. Size bin remains unverified. |
| Simultaneous processing | **Four category-selected effects plus amp and cabinet**, with gate and volume functions. Fixed serial order; not eight freely assignable blocks or a parallel chain. Looper shares the Delay selector rather than adding another independent delay engine. [PE-M] |
| Library | **7 amps,7 cabinets,17 effect choices including the looper**. Effect categories: Distortion4,Modulation4,Delay4,Reverb4,Looper1. Gate/volume are separate utilities, not additional entries in the advertised17. [PE-G,PE-M] |
| Distortion choices | Boost,Overdrive,Distortion,Fuzz. |
| Modulation choices | Chorus,Flanger,Phaser,Tremolo. |
| Delay / reverb choices | Delay: Analog,Digital,Tape,Pong. Reverb: Spring,Hall,Plate,Space. The looper occupies the Delay category when selected. [PE-M] |
| Presets | **21 total overwriteable locations**; factory-labelled sounds can be replaced by user settings. Not21 factory plus21 user. Factory-filled subset is not independently quantified here. [PE-G,PE-M] |
| Synth / acoustic simulation | **No dedicated synth or electric-to-acoustic simulator identified in the complete documented Guitar-model effect library**. Bass/Black variant functions are not transferred to this unit. |
| IR / NAM / captures | Seven factory cabinet models and cabinet bypass are documented. Third-party IR, native/converted NAM or user amp-capture import is **not established** in the documented2.00/edit workflow. Preset import is not IR/capture import. |
| Audio I/O | One6.35mm mono input,1MΩ;two6.35mm main outputs L/MONO,R;dedicated3.5mm stereo headphones. Main outputs are **680Ω impedance-balanced TRS,not true differential balanced**; preserve the manufacturer's distinction. No mic/XLR/phantom,analog aux or FX loop in the complete panel inventory. [PE-IO,PE-G] |
| Data/control | USB-C for recording,reamp and editing;one shared external-control socket as above. No physical DIN/TRS MIDI connection documented; do not infer general MIDI functionality from an operating system's Audio MIDI Setup name. |
| Battery / DC / USB power | **3 AA** or **9V center-negative,2.1mm pin,at least500mA/4.5W supply**; adapter sold separately. **USB-powered operation explicitly unsupported.** Plugging into the instrument input switches battery operation on. Supply rating is not measured draw. [PE-F,PE-M] |
| Battery runtime | Manufacturer typically at least6h alkaline,up to10h under ideal conditions; headphones,DSP and interaction affect this. Rechargeable AA chemistry may work but changes battery indication/runtime; internal recharging is not established. [PE-F] |
| Configuration | **POD Express Edit Windows/macOS/iOS/iPadOS/Android**, full editing and preset management,requires hardware2.00+. Desktop firmware updates through Line6 Central1.02+; Linux full editor not established. [PE-R,PE-M,PE-F] |
| USB audio | **4-in/4-out,24-bit/48kHz**; processed recording1/2,dry3/4,USB3/4 reamp. Windows ASIO driver; macOS/iOS/Android class compliant. Power still comes from batteries/DC,not USB. [PE-M,PE-F] |
| Looper / live features | **30-second stereo looper**,post-processing,one-switch control,undo/redo;selecting it replaces the Delay-category effect. Changing presets,exiting looper mode or power-off clears the loop. Tuner,tap and assignable external switches; internal drums not established. [PE-M] |

### POD Express Guitar — routing and software qualifications

Without headphones,using only L/MONO sums stereo effects to mono. With headphones connected,the manual says L/MONO carries only the left channel for stereo effects; do not promise the same mono-sum behavior in both configurations. Volume expression sits after amp/cab and before post effects. The looper is documented after the processing chain. [PE-M]

The2.00 manual has inconsistent OS-minimum tables: its introduction lists macOS11,Windows10,iOS/iPadOS15 and Android6 for editing/8 for audio,while the later editor section lists older macOS10.14 and iOS12.1. Platforms are established; **current minimum supported OS versions remain unresolved**, not selected arbitrarily from one table. The official FAQ's October2024 shipping firmware2.00 statement is dated evidence,not proof it is the latest firmware in October2026. [PE-M,PE-F]

### POD Express Guitar — IDR evidence

**Rp3.030.000**, [Seven Stereo, Shopee shop16879370/item26763471564](https://shopee.co.id/Line-6-POD-Express-Guitar-INT-P38-1-i.16879370.26763471564), indexed2026-10-15 with **Layanan Tidak Tersedia/service unavailable**. It establishes a hardware asking-price record,not an active checkout offer. Exact condition,bundle,warranty,region,stock and shipping remain unverified. **Used IDR: ?**. No guessed used discount,FX conversion or comparison against an unrelated older Pocket POD Express.

### POD Express official sources

[PE-G] [Official POD Express Guitar product and complete numbered panel](https://line6.com/podexpress/guitar-effects).

[PE-F] [Official Guitar/Bass/Black FAQ](https://kb.line6.com/pod-express-guitar-pod-express-bass-pod-express-black-faq), explicit no-USB-power rule,battery,driver and dated firmware statements.

[PE-IO] [Official input/output specification](https://kb.line6.com/pod-express-input-and-output-specs), including impedance-balanced output distinction.

[PE-R] [Official resources and editor description](https://line6.com/podexpress/resources).

[PE-M] **Line6/Yamaha-authored2.00 Owner's Manual,RevE,2024**, [original complete manual text](https://device.report/m/308188e1724d71b19719491ca6b3176709d7ead87c9a2e25f72e6ce38aee9a57). Used the actual manual's controls,signal-flow,model tables,looper,preset,USB and editor sections,not generated retailer/mirror summaries. Direct PDF retrieval failed; no successful PDF visual inspection is claimed. The official product's numbered panel independently supports controls and screen absence. Conflicting OS-minimum tables remain recorded.

## Other Line 6 records awaiting consolidation

HX Stomp,HX Effects and HX Stomp XL already have research in legacy pages and are not newly discovered models. Merge their complete records and sources before retiring the old files. **Next new research: POD Express Bass; POD Express Black requires separate exact Shopee discovery.** Keep brand/category/instrument documents at repository root and keep GitHub workflows disabled/uncreated.
