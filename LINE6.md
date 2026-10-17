# Line 6 multi-effects

Root-level brand comparison. **Checked 2026-10-15.** POD Go Wireless and POD Express Guitar/Bass are newly researched here; the standard POD Go profile is consolidated from its existing source-backed record without adding another model to the inventory. All eight recorded Line 6 models now have root records; specification checks and market discovery remain incomplete. No GitHub Actions workflows are used.

## POD Go and POD Go Wireless

Both are guitar/bass multi-effects with a semi-fixed serial path and built-in expression. **Shared specifications are explicitly supported by Line 6's Wireless FAQ**, which says the ordinary POD Go documentation also covers Wireless unless marked otherwise. This is not an inferred similarity between unrelated hardware. Both records remain partial.

<!-- comparison evidence begins -->
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
| User IRs | **128 IR library locations**;1024-point processing per Yamaha specification;WAV import throughPOD Go Edit. Cab/IR share one position. [Official FAQ](https://kb.line6.com/pod-go-faq),rechecked2026-10-17,explicitly converts allIRs to **16-bit/48kHz/mono**. Accepted source-rate/bit-depth ceilings remain incompletely transcribed;conversion target is not native arbitrary-format playback. [PG-Y,PG-F] |
| NAM / captures | Native NAM, converted NAM and user amp-capture import **not established** in the checked documentation. Helix-derived amp models and cabinet IR import prove none of these capabilities. |
| Editor | **POD Go Edit Windows/macOS**, full preset/IR editing and management. Hardware2.50 needs Edit2.50 for its newly added models. iOS USB audio is not a mobile editor; Android/Linux full editors are not established. [PG-P,PG-R,PG-M] |
| USB audio / MIDI | **4-in/4-out,24-bit**,dry recording/reamping andUSB MIDI. **USB3/4** can feed reamping;**USB1/2** monitors computer audio bypassing processing and is not an input-block source. This shared routing remains distinct fromWireless receiver selection; Windows ASIO driver. Mac class-compliant audio defaults to48 kHz; other rates require the documented driver. Complete supported-rate set is not independently transcribed. CurrentFAQ says Windows ARM/Snapdragon drivers have **not been tested**;this is not a tested incompatibility or support guarantee. [PG-M,PG-F] |
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

One6.35 mm mono GUITAR IN; one external EXP/footswitch TRS socket; stereo TRS SEND and RETURN; two balanced/unbalanced6.35 mm MAIN OUTs; separate mono AMP OUT; dedicated6.35mm stereo headphones (**63Ω output impedance**,currentFAQ);USB-B andDC. RETURN can become an always-on stereo aux input. No microphone/XLR/phantom, physical DIN MIDI or separate3.5 mm aux socket in the complete inventory. [PG-P,PG-M]

AMP OUT can tap the signal before Cab/IR while the main outs retain cabinet processing. This is **not** a second independent effects chain. Four-cable-method use and external stereo effects insertion are documented. [PG-P]

Looper consumes one of the four optional effect slots: **40 seconds mono/20 seconds stereo at full speed;80/40 seconds at half speed**, with one-switch and six-switch implementations documented in the2.50 manual. Yamaha's store comparison mentions Shuffling Looper but the model list/manual used here do not establish it; that remains a source conflict rather than a verified extra algorithm. Tuner,snapshots,trails and USB MIDI are documented; an internal drum machine is not established. Manufacturer describes snapshot changes without audio dropouts or disruption of delay/reverb trails; this is not a measured whole-device latency or blanket preset-switching guarantee. [PG-M,PG-Y,PG-P]

### Wireless-specific operation

Line 6 specifies **up to30 m/100 ft line-of-sight** and about **seven hours transmitter playing time**, both manufacturer ratings rather than independent tests. The floorboard needs its own supply. RF antennas are above the expression-pedal toe area. Wireless reliability depends on RF conditions; do not cover the antenna or assume arbitrary crowded2.4 GHz conditions meet the rated range. [PG-W]

GUITAR IN charges the transmitter; the separate rear well stores it. Leaving the transmitter in the charge port while the processor is off slowly discharges it, so the storage well is the documented storage location. Wireless accepts Guitar,Wireless or Guitar+Wireless input selections; ordinary POD Go presets are compatible and their Guitar input is automatically converted to Guitar+Wireless when imported. USB3/4 is a reamp source; USB1/2 is monitoring that bypasses processing. Cable Tone and Wireless Gain are separate settings, not additional audio-effect blocks. [PG-W]

The [WirelessFAQ](https://kb.line6.com/pod-go-wireless-faq),rechecked2026-10-17,recommends resyncing in each new room: insert the transmitter intoGUITAR IN,wait **10–15seconds**,then reconnect to the guitar. Keep at least **3m** from2.4GHz Wi-Fi routers. Up to **four systems** are described with sequential scanning while earlier transmitters stay awake;after **four minutes** without audio the transmitter sleeps. These are conditional manufacturer instructions,not a venue reliability guarantee or floorboard battery rating. [PG-W]

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

<!-- comparison evidence ends -->

### Standard POD Go — complete original finding

The2026-10-17 standard-model FAQ follow-up resolves the IR conversion target and adds headphone impedance/WindowsARM testing limits. Shared hardware/software applicability follows the already documented WirelessFAQ rule;it does not transfer the standard2.35kg mass or used/new offers toWireless. No newWireless listing or transmitter check is implied. Original source-input limits and revision gaps remain. No PDF,editor,driver or dependency downloaded or run.

The entire2026-10-15 standard,non-Wireless finding follows,including original dates,allcategory-count conflicts,price andinspection qualifications. Older unknown conversion details remain historical;current qualification above has priority. No source deleted.

<!-- LINE6-PODGO-STANDARD source begins -->

Reviewed **2026-10-15**. Guitar/bass multi-effects; **large**, built-in expression. Distinct from POD Go Wireless and POD Express. Partial record; undocumented capabilities and dated listing limitations remain explicit.

### Required comparison

| Field | Evidence-backed result |
|---|---|
| Expression | Built-in expression with toe switch, plus one shared TRS **EXP2 / FS7,8** input. A Y cable supports two external momentary switches; this is not two expression sockets [P,M] |
| Knobs / footswitches / buttons | **8 / 8 / 4**: upper/lower encoders, volume and five parameter knobs; up/down, A/B/C/D, Mode and Tap; Home/View, Action and two Page buttons. Toe/power switches separate; encoder presses counted once [P,M] |
| Dimensions / weight | Official Japan page publishes **88 H × 230 W × 359 D mm; 2.35 kg**. The horizontal labels appear counterintuitive for the illustrated orientation; retain the published envelope rather than invent a drilling template. Large under either orientation. Official Yamaha store gives 89 mm height, so preserve the 1 mm source disagreement. Wireless mass is different [J,Y] |
| Display | **4.3-inch color LCD**. Explicit touchscreen specification **unverified**; knob navigation is not by itself proof of absence [P] |
| Blocks / routing | **10 semifixed blocks**: amp/preamp, cab/IR, preset EQ, wah, volume, FX loop and **four freely selected effects**, DSP-limited. Input gate and output utility settings are additional functions, not unlimited extra effect slots. Serial path only; no dual parallel chain [F,M] |
| Presets | **256 overwriteable locations**, arranged as Factory128 and User128, with **four snapshots per preset**. Manual explicitly permits overwriting either setlist. Factory-labelled locations are not read-only; current factory-filled subset is not separately counted [M] |
| Acoustic / synth | **Yes / yes**: Acoustic Sim in the optional EQ-effect category; Pitch/Synth includes named synth algorithms. Acoustic Sim is excluded from the dedicated fixed Preset EQ block, so it consumes an optional effect slot [L,M] |
| IR import | **128 user IR library locations**, 1024-point processing in official Yamaha specification; WAV import through POD Go Edit. A cabinet block and IR share the same processing position. Detailed source-file conversion restrictions not fully transcribed [Y,F] |
| NAM / captures | Native NAM, converted NAM and user amp-capture import **not established**. Helix-derived amp modeling and cabinet IR loading are not NAM support |
| Power | Supplied **DC-3h family adapter**, 9 V, 3 A, center-negative. This is the adapter specification, not measured device draw. Battery/USB-powered operation not established in checked material [J,A] |
| Configuration | **POD Go Edit Windows/macOS**, full editor/IR/preset management. Firmware2.50 requires Edit2.50 to expose its new models. iOS USB audio is not an iOS editor; Android/Linux full editors not established [P,R,M] |
| Audio interface | **USB 4-in/4-out, 24-bit**, dry recording/reamp, USB MIDI; Windows ASIO driver. Mac class-compliant operation defaults to48 kHz; other rates require the documented Line6 driver. Exact supported-rate set not fully transcribed [M] |

### Category-choice inventory

Counts below are transcribed from the **official POD Go model-list webpage** as retrieved, not copied from HX Stomp or the broader Helix library. Mono/stereo implementations are not counted twice; different HX versus Legacy entries remain separate.

| Category | Named entries / qualification |
|---|---:|
| Distortion |55|
| Dynamics |18|
| EQ effects |8; fixed Preset EQ offers7 because Acoustic Sim is excluded|
| Modulation |55|
| Delay |41 named entries plus one blank-name table row; unresolved rather than fabricated|
| Reverb |23|
| Pitch/Synth |24|
| Filter |15|
| Wah |11|
| Volume/Pan |4|

Amp/preamp and cabinet subtotals have not been fully reconciled with the current webpage and firmware2.50 additions. No definitive grand total is claimed from the incomplete delay/cabinet tables. Source [L]; the 2.50 release notes [R] add11 guitar amps,2 bass amps,11 guitar cabs,2 bass cabs and2 effects. Their firmware date is **2025-01-23**, not a newly released October2026 update.

### Connections and live/practice features

One 6.35 mm mono guitar input; one shared external EXP/footswitch socket; stereo TRS send and return; two balanced/unbalanced 6.35 mm main outputs; separate mono AMP OUT; dedicated 6.35 mm stereo headphones; USB-B and DC. Return can operate as a stereo aux input. No XLR microphone/phantom, physical DIN MIDI or separate 3.5 mm aux socket in the complete inventory [P,M].

AMP OUT may be tapped before Cab/IR while the main outputs retain cabinet processing. This is not a second independent internal signal chain. Standard POD Go has **no built-in Relay receiver**; the Wireless variant does [P,M].

Looper uses one of the four optional effects: **40 seconds mono /20 seconds stereo at full speed; 80/40 seconds at half speed**. The 2.50 manual documents one-switch and six-switch mono/stereo implementations. An official store comparison table also mentions Shuffling Looper, which the model list/manual do not establish; it remains a source discrepancy, not an added verified algorithm. Tuner, snapshots, trails and USB MIDI are documented; no internal drum machine is established [M,Y].

### Separate IDR observations

| Condition | Amount | Exact evidence / limitation |
|---|---:|---|
| Retail indexed ask; detailed condition/stock unconfirmed | **Rp7.704.000** | [Nuansa Musik Official Shop, Shopee shop51110469/item9145739709](https://shopee.co.id/Yamaha-Line-6-POD-GO-Multi-Effects-Guitar-Processor-i.51110469.9145739709). Search evidence contained older August–September delivery dates; subsequent direct reopening failed |
| Explicit SECOND / BEKAS, sold out | **Rp5.000.000** | [Pomade.borneo, shop7513711/item18366387490](https://shopee.co.id/LINE-6-POD-GO-Floor-Processor-Multi-Effect-%28SECOND-BEKAS%29-i.7513711.18366387490). Historical used asking price, not an active offer or verified completed sale; direct reopening failed |

Not a current used-to-new market range. Seller names, badges or familiar branding do not independently authenticate a seller. Exact accessories, warranty, regional variant, shipping and checkout stock remain unverified. No currency conversion or guessed used discount.

### Sources and inspection limits

[P] [Official product and numbered interactive control descriptions](https://line6.com/podgo/).
[F] [Official POD Go FAQ](https://kb.line6.com/pod-go-faq). Launch prices and launch-era effect counts are not used as current offers/library totals.
[L] [Official model list](https://line6.com/podgo-models/).
[R] [Official firmware2.50 release notes](https://kb.line6.com/pod-go-2-50) and [official manual index](https://line6.com/support/manuals/podgo), identifying the2.50 manual/editor generation.
[J] [Official Line6 Japan product](https://line6.jp/podgo/), model-specific weight and published dimensions.
[A] [Official DC-3h accessory specification](https://line6.jp/effects-pedals/accessories/).
[Y] [Official Yamaha Singapore product specification](https://shop.sg.yamaha.com/products/pod-go.html), IR/USB/looper chart; its height and Shuffling Looper disagreements are retained above.
[M] Manufacturer-authored **2.50 Owner's Manual, RevG,2025**, [actual manual text mirror](https://manuals.plus/m/ce56ac3123bea01e1af09c67ee23bbacde033cc732eecebac95132e123405944): printed pp.6–8 controls/ports,13 blocks,15–16 preset storage/overwrite,31–33 looper/EQ,45–47 USB. Download/PDF rendering could not be completed; no successful PDF image inspection is claimed. The original manual text is used, not generated Q&A.

Remaining: current amp/cabinet subtotals, blank delay entry, explicit touchscreen/USB-power specifications, complete IR input-format rules and independently verified active offers. **Next Shopee-first target: Zoom G11**, subject to exact hardware-listing discovery.
<!-- LINE6-PODGO-STANDARD source ends -->

### POD Go Wireless — complete original finding

The2026-10-17 FAQ recheck adds transmitter synchronization/coexistence/sleep qualifications. Wireless-only operating prose is selected only forWireless in the instrument views;common USB3/4 reamp andUSB1/2 monitoring behavior remains in shared specifications. Standard2.35kg andWireless2.5kg masses andtheir distinct price evidence remain isolated. The entire2026-10-15 original follows with all wording,dates,URLs,condition/bundle limits andmanual-access qualifications retained. No fresh seller/bundle/stock authentication or device test implied. No file/dependency downloaded or source deleted.

<!-- LINE6-PODGO-WIRELESS source begins -->

Reviewed **2026-10-15**. Guitar/bass multi-effects, **large**, built-in expression and Relay wireless receiver. Separate hardware record from standard POD Go. Line6 explicitly states that the shared manual's ordinary POD Go specifications apply to both except the labelled wireless differences; this is not an inferred sibling-model substitution.

### Required comparison

| Field | Evidence-backed result |
|---|---|
| Expression / controls | Built-in expression/toe switch; one shared TRS external EXP2/FS7,8 socket. **8 rotary /8 footswitches /4 buttons**, with encoder pushes, toe and power switches counted separately [P,M] |
| Dimensions / weight | Official Japan specification **88 H ×230 W ×359 D mm; 2.5 kg Wireless**, versus2.35 kg standard. Published horizontal labels retained; envelope is large either way. Transmitter/bundle inclusion in the weight is not explicitly resolved [J] |
| Screen | **4.3-inch color LCD**; explicit touch-panel specification unverified. Adds RF quality and transmitter-charge indicators, not another display [P,W] |
| Blocks | **10 semifixed blocks**: amp/preamp, cab/IR, EQ, wah, volume, FX loop, plus **four selectable effects**, DSP-limited. Input/output utilities are separate; serial internal path, not two parallel chains [M] |
| Library/category choices | Shared current POD Go model library: drive55, dynamics18, EQ8, modulation55, reverb23, pitch/synth24, filter15, wah11, volume/pan4. Delay table has41 named entries plus one blank row; amp/cab current subtotals remain unresolved. Full source/count qualifications in [standard record](effects/findings/2026-10-15-line6-pod-go.md) and official list [L] |
| Presets | **256 overwriteable locations**, Factory128 + User128 labels; **four snapshots per preset**. Both setlists can be overwritten. Current factory-filled subset is not extra memory [M] |
| Synth / acoustic | **Yes / yes**: named synth algorithms and Acoustic Sim. Acoustic Sim uses an optional EQ effect slot, not the fixed Preset EQ slot [M,L] |
| IR | **128 imported IR library locations**, 1024-point processing, WAV via POD Go Edit. Cabinet and IR share one processing block; full input-conversion limits remain unverified [P,Y] |
| NAM / captures | Native/converted NAM and user amp-capture import **not established**; IRs and Helix-derived amp models are different capabilities |
| Power | Floor unit uses supplied **DC-3h, 9 V/3 A center-negative** adapter. **The rechargeable battery is in the transmitter**, not proof of battery-powered floorboard operation. Floorboard USB-powered operation unverified [J,A,W] |
| Editor | **POD Go Edit Windows/macOS**, full preset/IR/parameter editing; firmware2.50 requires Edit2.50. Editor also updates compatible G10T/G10TII transmitter firmware. Mobile USB audio is not a mobile editor [R,M] |
| Audio / live | **USB4-in/4-out,24-bit**, dry capture/reamp, USB MIDI. Looper uses an optional effect slot:40s mono/20s stereo full speed,80/40s half speed. Four snapshots, tuner, trails; no internal drum machine established [M] |

### Wireless-specific features and I/O

Built-in Relay receiver; manufacturer bundle includes **G10TII transmitter**, charged in GUITAR IN and stored in a separate rear recess. Earlier G10T is supported with current firmware; other Relay transmitter models are not certified by the FAQ. Manufacturer rates G10TII playing time at **seven hours**, and line-of-sight range at **30 metres**. These are published ratings, not measured performance in the user's venue [W,M].

Input source may select wired guitar, wireless, both or USB reamp. A wired cable input remains available. Cable Tone offers Off/3m/9m simulation; this is tonal filtering, not the radio range. The transmitter's rechargeable battery must not be listed as a built-in battery for the floor processor [W].

Audio ports: one6.35mm guitar input/charging jack; stereo TRS send and return/aux; two balanced/unbalanced6.35mm main outputs; separate mono AMP OUT with optional pre-Cab/IR tap; dedicated6.35mm stereo phones; shared external EXP/FS; USB-B; DC. No XLR microphone/phantom or physical MIDI DIN ports. The transmitter storage recess is not an audio input [M,P].

### IDR evidence

**Retail ask Rp11.130.500**, [melodiasby, Shopee shop158144224/item27772459064](https://shopee.co.id/Line6-Pod-Go-Wireless-Multi-Effect-i.158144224.27772459064). Direct page reopened but retains **29 June–1 July delivery text** and a JavaScript-limited body. Detailed condition, included transmitter/accessories, warranty, region and current checkout stock are not established. **Used IDR unknown**; no condition-verified offer obtained. This is not a completed sale or a guaranteed active market price.

### Primary sources

[P] [Official shared product/control descriptions](https://line6.com/podgo/).
[W] [Official Wireless-specific FAQ](https://kb.line6.com/pod-go-wireless-faq), explicitly defining common and differing hardware/features.
[J] [Official Japan specification and bundle](https://line6.jp/podgo/).
[A] [Official DC-3h specification](https://line6.jp/effects-pedals/accessories/).
[L] [Official POD Go model list](https://line6.com/podgo-models/).
[R] [Official2.50 release notes](https://kb.line6.com/pod-go-2-50), recommended for standard and Wireless; dated2025-01-23.
[Y] [Official Yamaha POD Go family specification](https://shop.sg.yamaha.com/products/pod-go.html), IR processing specification; contradictory looper summary is not adopted over the manual.
[M] Manufacturer **2.50 RevG manual**, [actual text mirror](https://manuals.plus/m/ce56ac3123bea01e1af09c67ee23bbacde033cc732eecebac95132e123405944), expressly covering both variants. PDF download/image rendering was not available; no successful visual PDF inspection is claimed.

Remaining: complete current amp/cab counts, blank delay-table row, explicit touch/USB-power specifications and current condition-specific bundle prices. **Next: POD Express Guitar**, followed by the separately listed Bass variant.
<!-- LINE6-PODGO-WIRELESS source ends -->

### Preserved seventh Shopee expansion: POD Go

Historical2026-10-15 source wording for this exact variant. Shared rows apply only where explicitly labelled;current firmware-qualified evidence retains precedence.

- **External control** (Built-in expression): One shared EXP2/FS7,8 socket
- **K/F/B** (Built-in expression): 8/8/4
- **Body and weight** (Built-in expression): Official Japan **88 H×230 W×359 D mm;2.35 kg;large**
- **Displays** (Built-in expression): **4.3-inch color LCD**; touch ?
- **Processing and available choices** (Blocks, categories and presets): **10 semifixed blocks**, including four selectable effects; serial, DSP-limited. Complete qualified category counts below
- **Preset storage** (Blocks, categories and presets): **256 overwriteable locations**,Factory128/User128 labels;4 snapshots each. Both setlists editable
- **Synth / acoustic simulation** (Blocks, categories and presets): **Synth and Acoustic Sim yes**; Acoustic Sim consumes an optional slot, not fixed Preset EQ
- **IR / capture support** (IR, NAM, power and software): **128 imported IR locations**,1024-point;factory cabinets share the IR block;NAM/capture import not established
- **Power** (IR, NAM, power and software): **9 V3 A center-negative DC-3h** supply;unit USB/battery ?
- **Configuration / USB audio** (IR, NAM, power and software): POD Go Edit Win/Mac2.50;USB4×4,24-bit,dry/reamp;mobile audio is not mobile editing
- **Audio/control connections** (Connections and practical differences): Mono input;stereoTRS loop/return-aux;balanced main pair;monoAMP OUT;quarter-inch phones;USB-B;sharedEXP
- **Looper / additional functions** (Connections and practical differences): Full-speed40 s mono/20 s stereo,half-speed80/40;loop uses optional slot;no drums. Wireless adds receiver and charging/storage functions
- **Used evidence** (Separate IDR evidence): **Rp5.000.000,SECOND/BEKAS,SOLD OUT**
- **Retail evidence / qualification** (Separate IDR evidence): **Rp7.704.000**,Nuansa Musik,indexed olderAug–Sep delivery text

[Original shared source](effects/shopee-multifx-7.md),retained pending complete navigation/provenance audits.

### Preserved seventh Shopee expansion: POD Go Wireless

Historical2026-10-15 source wording for this exact variant. Shared rows apply only where explicitly labelled;current firmware-qualified evidence retains precedence.

- **External control** (Built-in expression): Same documented shared socket
- **K/F/B** (Built-in expression): 8/8/4
- **Body and weight** (Built-in expression): Same published body; **2.5 kg**, not standard model's mass
- **Displays** (Built-in expression): **4.3-inch color LCD**; touch ?
- **Processing and available choices** (Blocks, categories and presets): **10 semifixed blocks**, including four selectable effects; serial, DSP-limited. Complete qualified category counts below
- **Preset storage** (Blocks, categories and presets): **256 overwriteable locations**,Factory128/User128 labels;4 snapshots each. Both setlists editable
- **Synth / acoustic simulation** (Blocks, categories and presets): **Synth and Acoustic Sim yes**; Acoustic Sim consumes an optional slot, not fixed Preset EQ
- **IR / capture support** (IR, NAM, power and software): **128 imported IR locations**,1024-point;factory cabinets share the IR block;NAM/capture import not established
- **Power** (IR, NAM, power and software): **9 V3 A center-negative DC-3h** supply;unit USB/battery ?
- **Configuration / USB audio** (IR, NAM, power and software): POD Go Edit Win/Mac2.50;USB4×4,24-bit,dry/reamp;mobile audio is not mobile editing
- **Audio/control connections** (Connections and practical differences): Mono input;stereoTRS loop/return-aux;balanced main pair;monoAMP OUT;quarter-inch phones;USB-B;sharedEXP
- **Looper / additional functions** (Connections and practical differences): Full-speed40 s mono/20 s stereo,half-speed80/40;loop uses optional slot;no drums. Wireless adds receiver and charging/storage functions
- **Retail evidence / qualification** (Separate IDR evidence): **Rp11.130.500**,melodiasby,reopened withJune–July dates;included transmitter not checkout-verified
- **Commit** (Individual findings commits): `ac3be6737643e81a13b5d1c3d1f6d18e8e104426`

[Original shared source](effects/shopee-multifx-7.md),retained pending complete navigation/provenance audits.

## POD Express Guitar

**New model, checked2026-10-15.** The2024-generation POD Express Guitar is not the older Pocket POD Express, POD Express Bass, or POD Express Black. It is a fixed-chain guitar multi-effects processor; no built-in expression. The current edit application must not be omitted because an older launch document mentioned only updating.

<!-- comparison evidence begins -->
| Required field | Verified value / explicit remaining gap |
|---|---|
| Expression | No built-in pedal; **one TRS VOLUME/FS3,4 socket** accepts a volume expression pedal, two external switches, or a pedal plus one switch with the specified cable. Arbitrary expression control of every effect parameter is not established. [PE-G,PE-M] |
| Physical controls | **6 rotary /2 footswitches /1 button**: AMP push-encoder,four effect knobs,side volume thumbwheel;ON and TAP;ALT button. Encoder press is not a second button. [PE-G] |
| Screen | **No graphical or numeric screen**. Seven multicolor LED segments and switch indicators show state/tuning/parameters; they are not a color LCD. Screen diagonal/color-mode N/A; touchscreen No. [PE-G] |
| Dimensions / mass / size bin | **92 W ×130 D ×56 H mm;350 g**, compact. Yamaha manufacturer announcement2024-03-06 explicitly names Guitar/Bass; reopened2026-10-17. Battery inclusion in mass remains unverified. [Yamaha primary announcement](https://www.yamaha.com/ja/news_release/2024/24030601/) |
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
| Configuration | **POD Express Edit Windows/macOS/iOS/iPadOS/Android**, full editing and preset management,requires hardware2.00+. Current Line6 App Store1.10 listing,checked2026-10-17,requires **iOS/iPadOS14+**; this mobile package is not the separate desktop editor. Desktop firmware updates through Line6 Central1.02+; Linux full editor not established. [PE-R,PE-M,PE-F], [App Store](https://apps.apple.com/gb/app/pod-express-edit/id6504572519) |
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

<!-- comparison evidence ends -->

### POD Express Guitar — correction and preserved original finding

On2026-10-17 the migration audit found omitted source URLs and a root dimensions regression. The earlier root statement was: Manufacturer-backed W×D×H and mass **not established in the inspected primary sources**. Do not promote reseller92×130×56mm/350g to a verified specification or estimate from photos. Size bin remains unverified. Yamaha’s original announcement now directly verifies the figures. The original2026-10-15 finding below retains all facts,URLs,price dates and OS/manual qualifications. Its App Store minimum14+ was independently rechecked; conflicting old manual OS tables remain historical evidence. The original factory-filled seven-preset statement is retained as a dated manual finding,not a fresh inspection of a device. No source deleted.

<!-- LINE6-PE-GUITAR source begins -->

Reviewed **2026-10-15**. Compact guitar multi-effects; no built-in expression. Separate from POD Express Bass and Black. Specifications use Line6/Yamaha sources, not retailer feature flags.

### Required comparison

| Field | Result and evidence |
|---|---|
| Expression / controls | External volume expression or up to two footswitch functions through one shared 6.35 mm TRS socket; no built-in pedal. **6 rotary /2 footswitches /1 ALT button**: five front rotary controls plus side volume thumbwheel; encoder press counted once [P] |
| Dimensions / weight | **92 W ×130 D ×56 H mm;350 g**, compact. Battery inclusion in stated weight is not explicit [Y] |
| Display | **No screen**; seven multicolor LED segments and status LEDs, not a graphical or numeric screen. Screen diagonal/color N/A; touchscreen No [P] |
| Architecture | Up to **8 fixed stages**, serial: gate, drive, amp, cab, volume, modulation, delay/looper, reverb. Four effect categories are not freely assignable or duplicable; selecting the looper replaces delay [L,M] |
| Choices | **7 amps,7 cabs; drive4,modulation4,delay4,reverb4,plus one looper =17 advertised effects**. Gate/volume utility stages are not additional selectable amp models. No synth/acoustic-simulator algorithm is identified in this Guitar model's inspected library [P,M] |
| Presets | **21 fully overwriteable locations;7 factory-filled** according to RevE manual. Not7 factory plus21 user slots [P,M] |
| IR / NAM | Factory cabinets selectable independently from amps. **Third-party IR, native/converted NAM and user amp-capture loading not established**; preset import is not model/IR import [M] |
| Audio I/O | One6.35 mm mono input; two6.35 mm main outputs; separate3.5 mm stereo headphones; shared external EXP/FS; USB-C and DC. No analog aux input, FX loop, microphone/phantom or physical MIDI port in full inventory [P] |
| Output type | Official KB specifies **impedance-balanced TRS outputs**, not fully differential balanced outputs. A TRS socket is not a second stereo headphone output [K] |
| Power | **Three AA batteries or9 V center-negative adapter, at least500 mA/4.5 W**, 2.1 mm center pin. **Cannot run on USB power**, explicitly documented. Adapter rating is not measured current draw [M,F] |
| Apps | **POD Express Edit Windows/macOS/iOS/Android**, editing, backup and presets; firmware2.00+ required. Current App Store requires **iOS/iPadOS14+**, superseding the manual's older12.1 minimum. Desktop firmware updates require Mac/Windows; mobile editing is not mobile firmware updating [M,A,G] |
| USB audio | **4-in/4-out,24-bit/48 kHz**, dry recording, reamp and playback. Windows ASIO; Mac/iOS/Android class support. Device-specific USB-host compatibility still matters [F,L,M] |
| Practice/live | **30-second stereo looper**, undo/redo, tap tempo, chromatic tuner, preset preselection and programmable switches. No internal drum machine established [L,M] |

### Separate IDR evidence

**Retail ask Rp3.030.000**, [Seven Stereo, Shopee shop16879370/item26763471564](https://shopee.co.id/Line-6-POD-Express-Guitar-INT-P38-1-i.16879370.26763471564). The page reopened with **service unavailable**; it is not verified current stock. **Used IDR unknown**. Condition, selected accessories, warranty, regional variant and delivery cost are not independently verified; no completed-sale or active-range claim.

### Primary sources and qualifications

[P] [Official Guitar product and numbered controls/ports](https://line6.com/podexpress/guitar-effects).
[Y] [Yamaha manufacturer announcement,2024-03-06](https://www.yamaha.com/ja/news_release/2024/24030601/), exact body dimensions and weight for Guitar/Bass.
[L] [Yamaha Music London specification](https://www.yamahamusiclondon.com/POD-Express-Guitar/pidGPODEXPRESSGT), eight fixed blocks and interface/looper specification. Yamaha Singapore's much larger dimension/weight table is not used as a unit-size measurement; its scope is unclear against the manufacturer announcement.
[F] [Official family FAQ](https://kb.line6.com/pod-express-guitar-pod-express-bass-pod-express-black-faq), explicit USB-power exclusion, audio support and battery-runtime qualifications.
[K] [Official input/output electrical specification](https://kb.line6.com/pod-express-input-and-output-specs).
[A] [Line6 developer App Store listing](https://apps.apple.com/gb/app/pod-express-edit/id6504572519).
[G] [Yamaha Guitar Group developer Google Play listing](https://play.google.com/store/apps/details?id=com.line6.podexpressedit&hl=en).
[M] Manufacturer **2.00 RevE manual**, [original text mirror](https://manualzz.com/doc/81729734/line-6-pod-express---black-owner-s-manual), covering the named Guitar/Black/Bass variants; printed pp.8,16,39 for power, memory and software. The older [RevC PDF](https://manuals.plus/m/8df05a2926e246f18ea670acc356bb3549d114f2273679b94fff0b4498713194.pdf) parsed successfully but attempted screenshots failed. Its seven-block prose disagrees with its eight-stage diagram and Yamaha's eight-block specification; explicit signal stages are retained rather than silently combining categories. No successful PDF visual inspection is claimed.

Remaining: weight battery inclusion, any later undocumented loading capability and current condition-specific price evidence. **Next: POD Express Bass**, whose effect categories differ from Guitar.
<!-- LINE6-PE-GUITAR source ends -->

### Preserved seventh Shopee expansion shared comparison

Historical2026-10-15 source wording. Current firmware-qualified findings retain precedence. Offers,old classifications and unknowns preserve their original context;this is not a new stock/specification verification.

- **External expression** (No built-in expression): One shared EXP/FS socket
- **K/F/B** (No built-in expression): 6/2/1
- **Body and weight** (No built-in expression): **92 W×130 D×56 H mm;350 g;compact**
- **Display** (No built-in expression): No screen; seven LED segments; screen diagonal N/A; no touchscreen
- **Processing and available choices** (Blocks, categories and presets): Eight fixed stages:gate,drive,amp,cab,volume,MOD,delay/looper,reverb.7 amps,7 cabs;4 each drive/MOD/delay/reverb plus looper =17 effects
- **Preset storage** (Blocks, categories and presets): **21 editable**,7 factory-filled
- **Synth / acoustic simulation** (Blocks, categories and presets): Neither identified in inspected Guitar library
- **IR / capture support** (IR, NAM, power and software): Factory cabinets,**no third-party IR/NAM import established**
- **Power** (IR, NAM, power and software): **3 AA or9 V center-negative ≥500 mA/4.5 W;USB power explicitly No**
- **Configuration / USB audio** (IR, NAM, power and software): Full Edit Win/Mac/iOS/Android,FW2.00+;currentiOS14+,desktop needed for firmware update;USB4×4,24-bit48 kHz
- **Audio/control connections** (Connections and practical differences): Mono quarter-inch input;two **impedance-balanced** TRS outputs;3.5 phones;sharedEXP/FS;USB-C;DC;no analogaux/loop/mic
- **Looper / additional functions** (Connections and practical differences): 30 s stereo loop;Guitar loop replaces delay;Bass loop replaces MOD/delay. No drum generator
- **Retail evidence / qualification** (Separate IDR evidence): **Rp3.030.000**,Seven Stereo,**service unavailable**
- **Commit** (Individual findings commits): `e8db0979b6ad77793934c92aabf119e54054a33c`

[Original shared source](effects/shopee-multifx-7.md),retained pending complete navigation/provenance audits.

## POD Express Bass

**New bass-specific model, checked2026-10-15.** A separate hardware/sound-library record, not a color option for POD Express Guitar. The official Bass product and joint2.00 manual explicitly document the following common hardware and different processing path. This record remains partial. Dimensions were repaired from the joint manufacturer announcement on2026-10-17; platform-specific OS minima need separate evidence.

<!-- comparison evidence begins -->
| Required field | Verified specification / limitation |
|---|---|
| Expression | **No built-in pedal**;one shared TRS VOLUME/FS3,4 port for volume expression,two switches or expression plus one switch. Arbitrary effect-parameter expression is not established. [PE-B,PE-M] |
| Controls | **6 rotary /2 footswitches /1 button**: amp encoder,four category knobs,side volume;ON,TAP;ALT. Encoder press is not counted again. [PE-B] |
| Display | **No graphical/numeric screen;no touchscreen**. Seven multicolor LED ring segments and switch LEDs are indicators,not a color graphical display. Diagonal and screen color classification N/A. |
| Dimensions / mass | **92 W ×130 D ×56 H mm;350g**,compact. [Yamaha announcement2024-03-06](https://www.yamaha.com/ja/news_release/2024/24030601/) explicitly names both Guitar and Bass; reopened2026-10-17 during the Guitar repair. Battery inclusion in the published mass remains unresolved; retailer400g is not silently substituted. |
| Processing | Fixed serial path: **gate → compressor → synth → distortion → amp → cab → volume → modulation/delay**. Four effect categories plus amp/cab and utilities,not freely assignable slots. The30-second stereo looper shares the final MOD/DELAY selector and is placed post-processing when active. [PE-M] |
| Library | **7 bass amps,7 bass cabinets,17 effect choices including looper**. Amp names: Round,Grit,Vintage,Punch,Modern,Studio,Deep. Gate/volume do not add to the advertised17. [PE-B,PE-M] |
| Compression choices | **4**: Optical,LA,Deluxe,Limiter. |
| Synth-category choices | **4**: Octave,Growl,String,Mutant. This category includes octave and envelope-filter behavior as well as synthesizer algorithms; not four interchangeable polyphonic synth engines. String is based on the Roland GR700 model,Octave on BOSS OC-2,Mutant on Mu-Tron III; manufacturer comparison names describe modeled sounds,not required external hardware. [PE-M] |
| Distortion choices | **4**: Boost,Overdrive,Distortion,Fuzz; Bass-specific models,not copied from Guitar's similarly labelled selection. |
| Modulation/delay choices | **3 modulation** choices Chorus,Flanger,Phaser;**1 Digital delay**;**1 Looper**. These share a single category position: do not claim simultaneous chorus plus delay or copy Guitar's separate reverb category. **No dedicated reverb is present in the documented Bass-model library.** [PE-M] |
| Presets | **21 overwriteable total locations**,not21 factory plus21 user. Factory-filled subset not separately quantified. [PE-B] |
| Acoustic / synth | **Synth category yes**,with the algorithm qualifications above. No electric-to-acoustic simulator identified in the documented Bass library. |
| IR / NAM / captures | Seven factory cabinets selectable/bypassable;third-party IR,native/converted NAM or user capture import **not established** in the2.00/editor documentation. Preset management is not model/IR import. |
| Ports | One6.35mm mono1MΩ input;two6.35mm impedance-balanced680Ω TRS main outs L/MONO,R;3.5mm stereo phones;USB-C;external-control TRS;DC. Not true differential-balanced outputs. No mic/XLR/phantom,analog aux,FX loop or physical MIDI port in the documented inventory. [PE-B,PE-IO] |
| Power | **3 AA or9V center-negative,2.1mm,≥500mA/4.5W supply;NO USB bus power.** Supply rating is not measured draw. Battery operation powers on with an instrument cable. Manufacturer alkaline runtime typically6h and up to10h ideal;depends on use. No internal AA charger documented. [PE-M,PE-F] |
| Editor | **POD Express Edit Windows/macOS/iOS/iPadOS/Android**,hardware2.00+;desktop Central updater separately. Current Line6 [App Store1.10](https://apps.apple.com/gb/app/pod-express-edit/id6504572519),checked2026-10-17,requires **iOS/iPadOS14+**; this is the mobile package,not the separate desktop editor. Conflicting old manual minima remain historical; no Linux editor established. [PE-R,PE-M] |
| USB audio | **4-in/4-out,24-bit/48kHz**,processed1/2,dry3/4,reampUSB3/4;Windows ASIO,other supported platforms class compliant. USB recording still requires AA/DC power. [PE-M,PE-F] |
| Live / practice | **30s stereo looper**,one-switch,post-effects,undo/redo;clears on preset change,exiting looper or power-off. Tuner,tap,external-switch assignments. Internal drums not established. [PE-M] |

The family manual's headphone/main-output caveat also applies: L/MONO sums to mono when used alone without headphones,but with headphones connected it carries the left channel of stereo effects. Neither two main sockets nor stereo USB creates two independent processing chains.

### POD Express Bass — IDR evidence and sources

**Retail indexed ask: Rp3.099.000**, [Seven Stereo Music & Audio Store, Shopee shop16879370/item29813481193](https://shopee.co.id/Line-6-POD-Express-Bass-INT-P38-2-i.16879370.29813481193). Re-found2026-10-15; the indexed body retains **August13–15 delivery text**, and direct reopening failed. Not verified current stock,new-condition certification or a completed sale. Accessories,regional warranty and shipping remain unknown. **Used IDR: ?**. No conversion or assumed secondhand percentage.

[PE-B] [Official POD Express Bass page with numbered controls/ports](https://line6.com/podexpress/bass-effects). The Bass-specific effect table and signal path are in [PE-M] above, especially printed pp.26–27. [PE-F] explicitly names Bass for the battery,USB-power and driver rules. Sources shared across models are explicit manufacturer family documentation,not sibling-model inference.

**Additional historical retail IDR ask Rp3.200.000**, [Dial Musik,shop338305078/item29164837310](https://shopee.co.id/Line-6-Pod-Ekspress-Bass-Efek-Bass-Line-6-Pod-Original-i.338305078.29164837310),observed2026-10-15 as **sold out** in the preserved original finding. No2026-10-17 offer refresh claimed. Condition grade,new status,bundle,warranty region,shipping,total and stock unverified. Not a current market upper/lower bound or completed sale.

<!-- comparison evidence ends -->

### POD Express Bass — migration correction and complete original finding

The root previously said: **Unverified from primary sources**. The inconsistent350g/400g and rounded reseller measurements are not substituted for manufacturer specifications; mechanical size bin remains unknown. That uncertainty was a consolidation regression: the original finding cited Yamaha directly. The primary announcement explicitly documents Bass as well as Guitar. Current field corrected; battery-inclusion uncertainty remains. The legacy seven-factory-filled statement and all price/access/OS/manual qualifications are retained below without presenting an old observation as a new device inspection. No original source deleted.

<!-- LINE6-PE-BASS source begins -->

Reviewed **2026-10-15**. Compact bass multi-effects, separate from Guitar and Black. The manufacturer shared manual expressly documents this model; common hardware is not borrowed without that evidence.

### Required comparison

| Field | Verified result / explicit limitation |
|---|---|
| Expression / controls | No built-in pedal; one shared6.35 mm TRS input for volume expression, one expression plus footswitch, or two footswitches. **6 rotary /2 footswitches /1 ALT button**, including side volume thumbwheel [P,M] |
| Size / weight | **92 W ×130 D ×56 H mm;350 g**, compact. Published mass does not explicitly identify battery inclusion [Y] |
| Display | No screen: seven multicolor LED segments plus indicators. Diagonal/color screen fields N/A; touchscreen No [P] |
| Signal chain | **8 fixed serial stages**: gate, compressor, synth, distortion, amp, cab, volume, and modulation/delay/looper. Four simultaneous effect categories plus amp/cab/utilities; not freely assignable slots [M] |
| Library | **7 bass amps,7 cabinets; compressor4,synth-category4,drive4,modulation3,delay1,looper1 =17 effects**. The synth category mixes octave/filter and true synth-style choices; not four independent synthesizers [P,M] |
| Synth / acoustic | **Synth yes:** Growl and String are among the documented bass synth choices. Acoustic simulator not identified in the inspected library. Guitar version's reverb section is not present here [M] |
| Presets | **21 overwriteable locations;7 factory-filled**. No separate21-slot user bank beyond those locations [P,M] |
| IR / NAM | Seven factory cabinets, separately selectable/bypassable. Third-party IR import and native/converted NAM or amp-capture loading **not established**; preset-file management does not imply sample loading [M] |
| I/O | One6.35 mm mono input;2×6.35 mm main outs;dedicated3.5 mm stereo phones;shared external EXP/FS;USB-C;DC. No analog aux,FX loop,mic/phantom or physical MIDI socket [P] |
| Output electrical type | **Impedance-balanced TRS**, not fully differential balanced outputs, per the official family electrical specification [K] |
| Power | **3 AA or9 V center-negative supply,minimum500 mA/4.5 W,2.1 mm center pin. USB power explicitly unsupported.** Adapter specification is not measured draw [M,F] |
| Configuration | **POD Express Edit Windows/macOS/iOS/Android**, full parameter/preset/backup editing, requiring device firmware2.00+. Current iOS/iPadOS minimum14 supersedes old manual12.1. Firmware updates use the desktop app/Line6 Central; Linux editor not established [M,A,G] |
| USB audio | **4-in/4-out,24-bit/48 kHz**, dry capture/reamp and stereo playback; Windows ASIO and Mac/iOS/Android class support [M,F] |
| Practice/live | **30-second stereo looper**, undo/redo,tuner,tap,preset preselection. **Modulation,delay and looper are alternatives in one block**, so do not imply simultaneous chorus+delay+looper. No internal drum machine established [M] |

### Bass model choices

Amp labels: Round,Grit,Vintage,Punch,Modern,Studio,Deep. Compressor: Optical,LA,Deluxe,Limiter. Synth category: Octave,Growl,String,Mutant. Drive: Boost,Overdrive,Distortion,Fuzz. Last block: Chorus,Flanger,Phaser,Digital Delay or Looper. These are the Bass-specific choices, not a reused Guitar effect table [M].

### IDR listing evidence

**Retail indexed ask Rp3.099.000**, [Seven Stereo, Shopee shop16879370/item29813481193](https://shopee.co.id/Line-6-POD-Express-Bass-INT-P38-2-i.16879370.29813481193); cached13–15 August delivery text, direct reopening failed. Separate **Rp3.200.000 sold-out** offer: [Dial Musik shop338305078/item29164837310](https://shopee.co.id/Line-6-Pod-Ekspress-Bass-Efek-Bass-Line-6-Pod-Original-i.338305078.29164837310). **Used IDR unknown.** No checkout stock, seller authentication, warranty, condition grade or completed-sale assertion; the sold-out ask is not a current upper/lower market bound.

### Primary sources

[P] [Line6 Bass product and numbered hardware features](https://line6.com/podexpress/bass-effects).
[Y] [Yamaha manufacturer announcement](https://www.yamaha.com/ja/news_release/2024/24030601/), body dimensions/weight.
[F] [Official shared FAQ](https://kb.line6.com/pod-express-guitar-pod-express-bass-pod-express-black-faq).
[K] [Official I/O electrical specifications](https://kb.line6.com/pod-express-input-and-output-specs).
[A] [Line6 developer App Store listing](https://apps.apple.com/gb/app/pod-express-edit/id6504572519).
[G] [Yamaha Guitar Group Google Play listing](https://play.google.com/store/apps/details?id=com.line6.podexpressedit&hl=en).
[M] Manufacturer **2.00 RevE manual**, [actual manual text](https://manualzz.com/doc/81729734/line-6-pod-express---black-owner-s-manual), named Bass signal path/library, power, memory and editor. Older RevC PDF was also parsed; attempted screenshots failed, so no visual PDF verification is claimed. Its obsolete seven-block sentence is superseded by the explicitly enumerated eight-stage chain and current manual.

Remaining: battery inclusion in mass, later undocumented loading capabilities and active condition-specific offers. **Next Shopee-first model: Hotone Ampero One MP-80.** POD Express Black still needs an exact Indonesian hardware listing before Shopee-priority promotion.
<!-- LINE6-PE-BASS source ends -->

### Preserved seventh Shopee expansion shared comparison

Historical2026-10-15 source wording. Current firmware-qualified findings retain precedence. Offers,old classifications and unknowns preserve their original context;this is not a new stock/specification verification.

- **External expression** (No built-in expression): One shared EXP/FS socket
- **K/F/B** (No built-in expression): 6/2/1
- **Body and weight** (No built-in expression): **92×130×56 mm;350 g;compact**
- **Display** (No built-in expression): No screen; LED segments, not a color LCD; no touchscreen
- **Processing and available choices** (Blocks, categories and presets): Eight fixed stages:gate,COMP,synth,drive,amp,cab,volume,MOD/delay/looper.7 amps,7 cabs;COMP4,synth-category4,drive4,MOD3,delay1,looper1 =17
- **Preset storage** (Blocks, categories and presets): **21 editable**,7 factory-filled
- **Synth / acoustic simulation** (Blocks, categories and presets): **Synth yes**,including Growl/String;acoustic simulator not identified
- **IR / capture support** (IR, NAM, power and software): Factory cabinets,**no third-party IR/NAM import established**
- **Power** (IR, NAM, power and software): **3 AA or9 V center-negative ≥500 mA/4.5 W;USB power explicitly No**
- **Configuration / USB audio** (IR, NAM, power and software): Full Edit Win/Mac/iOS/Android,FW2.00+;currentiOS14+,desktop needed for firmware update;USB4×4,24-bit48 kHz
- **Audio/control connections** (Connections and practical differences): Mono quarter-inch input;two **impedance-balanced** TRS outputs;3.5 phones;sharedEXP/FS;USB-C;DC;no analogaux/loop/mic
- **Looper / additional functions** (Connections and practical differences): 30 s stereo loop;Guitar loop replaces delay;Bass loop replaces MOD/delay. No drum generator
- **Retail evidence / qualification** (Separate IDR evidence): **Rp3.099.000**,Seven Stereo,August cache;separateRp3.200.000sold-out ask
- **Commit** (Individual findings commits): `233e29942df322892b9a841f75a54ed7e760479e`

[Original shared source](effects/shopee-multifx-7.md),retained pending complete navigation/provenance audits.

## HX Effects

<!-- comparison evidence begins -->
**Guitar/bass effects-only multi-effects**, not a single-function pedal. No amp modeling is required for inclusion. Consolidated from the complete `effects/advanced-modelers.md` record (technical snapshot 2026-10-14), with model-specific manufacturer rechecks **2026-10-16**. This is the existing inventory entry, not a new model.

| Required field | Evidence / qualification |
|---|---|
| Built-in / external / toe expression | No built-in pedal or toe switch; **two external pedal sockets shared with amp-control outputs**. Each can instead control two amp-switch functions; selecting amp control consumes that expression connection. [HXE-P, HXE-F] |
| Knobs / footswitches / buttons | **4 / 8 / 6** from the official numbered control inventory: Big Knob plus three parameter knobs; six assignable footswitches plus MODE and TAP; SAVE, MENU, ACTION, HOME and two PAGE buttons. Encoder presses counted once; rear power toggle separate. Earlier ?/8/? count is superseded. [HXE-P] |
| Display | **Six customizable LCD scribble strips**; no large central display. Published diagonals, monochrome/color and touchscreen specifications unverified. Capacitive-touch footswitches and colored LED rings do **not** establish a touchscreen or color LCDs. [HXE-P] |
| Body / size | Official FAQ **10.8 W ×7.9 D ×2.8 H inches; 4.75 lb**, approximately **274×201×71 mm; 2.15 kg**. Rounded conversions, not precision measurements. **Large**, because rounded depth exceeds the 200 mm medium limit. [HXE-F] |
| Blocks / category choices | **Nine simultaneous blocks, DSP-limited**, reorderable with parallel Path B. No amp or factory cabinet-model blocks. Legacy FAQ's 117 HX +77 Legacy effects is a **launch-era** count, not the present library. Distortion/dynamics/EQ/modulation/delay/reverb/pitch-synth/filter/wah/volume/IR/loop utilities are documented; **3.80 manual table count: 274 named models = 167 HX + 107 Legacy**: distortion 61 (44+17), dynamics 19 (12+7), EQ 8 (8+0), modulation 56 (30+26), delay 45 (28+17), reverb 25 (13+12), pitch/synth 29 (12+17), filter 15 (4+11), wah 11 (11+0), volume/pan 5 (5+0). Parentheses are HX+Legacy; each named row counts once, without duplicating mono/stereo versions. Excludes IR, sends/returns, loopers, routing and Favorites. Manual-derived inventory, not a firmware-independent manufacturer headline or simultaneous capacity. [HXE-F, HXE-M; HXE-D pp.19–24] |
| Memory | **128 overwriteable presets in one setlist, four presets per bank**, four snapshots each. **128 Favorites and 128 user IRs are separate libraries**, not additional preset slots. Factory-filled subset not separately established. [HXE-F, HXE-M pp.16,31; HXE-E370 p.5] |
| Synth / acoustic | **Synth yes**: 3 OSC Synth and Legacy synth models explicitly listed. **Acoustic Sim**,mono/stereo,in the3.80 EQ library now establishes a dedicated acoustic-simulation algorithm;this supersedes the earlier unverified status. Acoustic-body IR loading is a separate capability. Firmware/library revision remains device-specific. [HXE-M p.22; HXE-F; HXE-D p.20] |
| IR / NAM / captures | **128 user IR locations**, one 2048-sample block or two 1024-sample blocks per preset. Earlier 3.0 single-IR limits above remain historical. **Dual IR was introduced in 3.50**, not 3.80: two 1024-point IRs in one stereo block, with independent pan/polarity and up to 50 ms relative delay. The 3.50 notes explicitly include HX Effects, but do not clearly resolve the total-per-preset conflict below. [HXE-R350] **Unresolved internal manual conflict:** pp.25–26 specify one 2048 or two 1024 Single IRs per preset and one Dual IR per preset; p.39 instead allows two 2048 Singles, four 1024 Singles, or two Duals across paths. Do not treat the larger limits as verified device capacity. Native NAM, converted NAM and user amp-capture import not established. [HXE-M pp.24–25; HXE-D pp.25–26,39] |
| I/O | Two 6.35 mm instrument/line **unbalanced TS** main inputs (1 MΩ); two **impedance-balanced TRS** main outputs and two impedance-balanced TRS sends; two unbalanced TS returns (1 MΩ instrument / 10 kΩ line; two mono loops or one stereo loop). Outputs drive audio on the tip only: impedance balancing is not differential balanced audio. This supersedes the earlier unbalanced-TS output/send classification. [HXE-I] Two PEDAL/EXT AMP sockets; MIDI DIN IN and OUT/THRU; USB-B; DC. No dedicated headphone output in the complete rear-panel inventory. [HXE-P] |
| Power / battery / USB | Included **DC-3G**, **2.5 mm pin**, FAQ requires **at least 2 A clean DC**. Voltage/polarity and battery/USB-powered operation not independently established here; do not copy another HX supply specification. Supply requirement is not measured current draw. Current general FAQ confirms DC-3G supports worldwide mains standards with the appropriate regional plug adapter; it does not mean direct mains input to HX Effects. The compatibility chart is image-only and was not visually inspected. [HXE-F; HXE-POWER] |
| Editing / USB | **HX Edit Windows/macOS** full editor, preset/IR librarian; current official page and manual supersede the launch FAQ's librarian-only wording. HX Edit 2.60+ with matching hardware firmware added full editing. **USB MIDI, explicitly no USB audio interface**. iOS USB remote MIDI control is not an iOS full editor; Android/Linux editing unverified. [HXE-P, HXE-F, HXE-E] |
| Practical features | Analog relay or DSP bypass with trails,snapshots,parallel routing,four/seven-cable integration,MIDI/amp control andPedal Edit. **One looper block maximum per preset**,using one of9 blocks:6 Switch,1 Switch orShuffling,inmono/stereo. **6/1Switch full-speed60s mono/30s stereo;half-speed120s mono/60s stereo**. Shuffling60s mono/30s stereo,nohalf-speed entry. Preset changes retain playback only with the **same looper model AND mono/stereo type**. Six-switch controls include overdub,last-overdub undo,play-once,reverse andspeed. From **3.50**, Snapshot Control can be disabled per parameter assigned to EXP, footswitch or MIDI, so snapshots need not overwrite that physical controller assignment. **Firmware3.10:** tuner Trails keeps delay/reverb tails and looper running. Shuffling Looper replaces its earlier Octaves probability with Pitch plus Interval1/2 (−1 to+1octave). Reload/change the model to expose new parameters in existing presets; saved defaults need resaving. Command Center Instant commands gain up to1000ms Wait Time. CC69 snapshot changes received during preset loads are buffered until loading completes. Drum machine remains unverified. [HXE-F; HXE-D pp.27–28; HXE-R350; HXE-R310] |

### HX Effects — IDR and source provenance

Earlier2026-10-16/17 searches did not establish an exact Indonesian ask; that search limitation is superseded by the exact indexed item below. Foreign-region offers remain excluded from IDR evidence. The FAQ's **$599.99 US MAP** remains launch-price provenance, not a current Indonesian offer.

| Price class | Amount | Offer and limits |
|---|---:|---|
| Condition-unverified sold-out indexed ask | Rp7.900.000 | [Soundstationstore,seller250276993/item5129480739](https://shopee.co.id/LINE-6-HELIX-HX-EFFECTS-i.250276993.5129480739);Kota Tangerang Selatan. Checked2026-10-17;four-month indexed body says **Habis** and **Layanan Tidak Tersedia**. Exact direct open failed cache access. Used/new condition,bundle,variant,voucher,warranty andauthenticity unverified. Historical ask,not current stock or completed sale |
| Verified used IDR | ? | Not established;do not infer used from sold-out status |
| Verified new IDR | ? | Not established;store identity does not establish new condition |


- [HXE-E370: official HX Edit 3.70 Pilot’s Guide, Rev X](https://line6.com/data/6/0a00050b25c26643a8409a0e2/application/pdf/HX%20Edit%20Pilots%20Guide%203.70%20-%20English%20.pdf), indexed feature table p.5 checked 2026-10-17. Device-specific memory cells support one setlist, four presets per bank, 128 presets, and separate 128-entry IR/Favorites libraries. Merged model/limit cells broadly include amp/cab language and exclude 6 Switch Looper from HX Effects, conflicting with its own manual; those cells do not independently settle IR totals or override device-specific capabilities. Full 3.50 guide open exceeded the web reader’s size limit; no file downloaded.
- [HXE-R350: official Helix/HX 3.50 release notes](https://kb.line6.com/helix-3-50-release-notes), checked 2026-10-17. HX Effects is explicitly included under Dual IR and Snapshot Control; the new factory cab engine applies to other listed hardware, with HX Effects marked IRs only. These notes do not establish additional amp/cab modeling for HX Effects or settle the 3.80 manual’s contradictory IR totals.
- [HXE-I: official HX Effects input/output electrical specifications](https://kb.line6.com/helix-floor-rack-lt-hx-effects-input-and-output-specs), checked 2026-10-17. The HX Effects subsection explicitly identifies main outputs and sends as impedance-balanced TRS, main inputs as 1 MΩ TS, and returns as 1 MΩ instrument / 10 kΩ line. Earlier connector classification above is corrected; this does not assign Helix-only auxiliary inputs to HX Effects.
- [HXE-R310: official Helix/HX3.10/3.11 notes](https://kb.line6.com/helix-3-10-3-11-release-notes), checked2026-10-17. Each adopted feature explicitly lists HX Effects. These are historical firmware-qualified behaviors, not installed-version confirmation; HX Stomp-only3.11 fixes are not assigned to HX Effects.
- [HXE-POWER: current official supply/battery FAQ](https://kb.line6.com/power-supply-battery-specs-and-faq), checked2026-10-17. Worldwide DC-3G input guidance and supply-rating/current-draw distinction only; chart cells,voltage,polarity andreplacement equivalence were not verified. Older community quotations are not adopted.
- [HXE-P: official HX Effects page and complete numbered front/rear controls](https://line6.com/hx-effects/).
- [HXE-F: official HX Effects FAQ](https://kb.line6.com/hx-effects-faq), retaining its launch-era library/software/price limits. It explicitly identifies guitar **and bass** use.
- [HXE-M: manufacturer HX Effects 3.0 Owner's Manual, Rev C](https://line6.com/data/6/0a020a411710a6112a67116f0b/application/pdf/HX%20Effects%203.0%20Owner%27s%20Manual%20-%20Rev%20C%20-%20English%20.pdf). Original manual text inspected for model list, IRs and memory. Web screenshots failed; no successful new PDF visual inspection claimed. Official product's numbered panel independently supports the control/port count.
- [HXE-E: manufacturer HX Edit Pilot's Guide Rev E](https://line6.com/data/6/0a020a3f182a45b4f6d41c90dc/application/pdf/HX%20Edit%20Pilot), full editing from 2.60; [current HX Edit software listing](https://line6.com/software/index.html?hardware=All&name=HX+Edit&os=All&submit_form=set).

- [HXE-D: official HX Effects3.80 Owner’s Manual,RevD](https://line6.com/data/6/0a00051afdbe673ccc8bdcf2d/application/pdf/HX%20Effects%203.80%20Owner%27s%20Manual%20-%20English%20.pdf),indexed manufacturer text checked2026-10-17:EQ table p.20;looper types/durations andpreset-continuity restrictions pp.27–28. No manual/software/firmware files downloaded to the workspace. This documents revision3.80,not proof of installed firmware.

All earlier HX Effects facts, rounded-dimension provenance, nine-block/128-preset/four-snapshot distinctions, amp-control sharing, IR/acoustic qualifications, source URLs and launch-FAQ correction are preserved. The shared legacy page now redirects with pinned originals. Remaining:confirmation against installed/newer firmware beyond the 3.80 manual inventory,exact display specifications,supply voltage/polarity,explicit battery/USB-power statements,complete Shuffling/control details andqualified Indonesian offers. Earlier acoustic-simulation andlooper unknowns are superseded only by the revision-qualified evidence above.
<!-- comparison evidence ends -->

### Preserved original shared-source HX Effects fields

Historical snapshot **2026-10-14**,retained2026-10-17. Earlier unknown controls,ports and synth details below are superseded where the current2026-10-16 record above supplies verified evidence. Preserving these rows does not reverse those corrections or add another model.

| Original field | Original value |
|---|---|
| External expression | **2**, shared with amp-control outputs |
| K/F/B | ?/8/?; six assignable stomp switches plus Mode and Tap |
| W×D×H; weight | Approx. **274×201×71**, 2.15 kg, converted from official FAQ |
| Size class | Large by the 200 mm medium-depth limit |
| Used USD | ? |
| New USD observation | ? |
| Simultaneous processing / available choices | **9 blocks, DSP-limited**; no amp-model or factory cab-model blocks; current category counts pending |
| Preset storage | **128 editable presets**, **4 snapshots each** |
| Synth / acoustic functions | Acoustic-body IR use documented; individual synth algorithms ? |
| Third-party IR | Yes, including acoustic-body IRs |
| NAM / proprietary capture | NAM not established |
| Audio/control ports | Stereo instrument/line routing; **2 mono FX loops or1 stereo**; 2 EXP/amp-control ports; MIDI/USB; exact complete connector inventory and headphone provision pending |
| Power; battery/USB-powered? | Supplied **DC-3G**; FAQ requires at least **2 A clean DC**, 2.5 mm pin; USB/battery power not established |
| Configuration apps and USB functions | **HX Edit Windows/macOS**; **USB MIDI, not USB audio** |
| Other important differences | Effects-only; analog/DSP bypass; snapshots and parallel path; looper consumes one of nine blocks |

### Original shared qualifications

These paragraphs retain the original shared scope;references to other devices do not assign their features to HX Effects.

Checked **2026-10-14**. **Partial records**: `?` means unverified, not No. Native NAM, architecture-limited NAM, converted NAM, proprietary captures and cabinet IRs are different capabilities. An effects-only unit is not necessarily an amp modeler.

K/F/B = rotary controls / footswitches / separate buttons. Push-encoders are counted once. Nano Cortex's rotary footswitches are explicitly called out rather than hidden in the knob count. Dimensions are **W×D×H, mm**. Prices are separate **USD** new and used observations; missing used prices have not been invented.

The rounded Line 6 FAQ dimensions are not precision measurements. They establish the category but should not be used as a millimetre-perfect drilling template. Manufacturer FAQ launch prices are **not** presented as current offers.

**HX Stomp's old FAQ says six blocks**, but the official firmware-3.0 release notes increased the limit to **eight**. Similarly, HX Effects' launch FAQ predates full HX Edit support and later model additions. This comparison uses the release notes/current software listing rather than treating the old FAQ's launch-era software limitations and prices as current.

USB audio input/output counts use the manufacturer's interface convention. A capture microphone connector does not establish a dedicated live vocal-effects path. Do not connect an amplifier's speaker output directly to an instrument/capture input; the appropriate load/interface is required.

Original model sources: [Source 1](https://line6.com/hx-effects/) · [Source 2](https://kb.line6.com/hx-effects-faq) · [Source 3](https://line6.com/software/index.html?hardware=All&name=HX+Edit&os=All&submit_form=set)

## Other Line 6 records awaiting consolidation

HX Stomp and HX Stomp XL already have research in legacy pages and are not newly discovered models. HX Effects is now root-canonical above. Merge the complete remaining records and sources before retiring the old files. POD Express Black is a distinct sound library but **an exact Indonesian Shopee hardware listing was not established in this pass**; Thai marketplace results must not be labelled Indonesian evidence. Ampero One is already recorded; do not restart that stale cursor. Keep brand/category/instrument documents at repository root and do not create or run GitHub workflows.

## Helix LT

Guitar/bass multi-effects; checked **2026-10-16**. First pass, not fully verified. The LT-specific manufacturer chart explicitly lists bass amps and bass inputs; this is not inferred from Helix Floor.

| Field | Evidence and limits |
|---|---|
| Expression | Built-in treadle; toe switch. One external EXP2 socket shares amp control. [Chart][HLT-C]; [product][HLT-P] |
| K/F/B | 12 footswitches, plus separate toe; rotary/button totals await direct panel inspection. Indexed manual diagrams are insufficient for a final count. |
| Display | 6.2-inch 800×480 color LCD; touchscreen unverified. Capacitive footswitches do not establish screen touch. No scribble strips. [KB][HLT-K] |
| Dimensions / weight | KB:20.87×11.93×3.66 inches,12.5 lb. Chart:20.86×11.87×3.61 inches,12.0 lb. Both published figures retained; reconciliation unresolved. [KB][HLT-K], [chart][HLT-C] |
| Simultaneous processing / categories | Up to32 DSP-limited blocks; four stereo paths. Chart's **2017** library:50 guitar amps,12 bass amps,37 cabs,16 mics,104 effects; not current firmware totals. Full current category subtotals unresolved. [Chart][HLT-C] |
| Factory / user / total memory | 1,024 locations,8×128; all overwriteable per indexed RevD manual. Factory-filled subset unresolved. [Chart][HLT-C]; [manual][HLT-M] |
| Synth / acoustic | Exact current LT algorithms and acoustic-simulation distinctions require firmware/model-list review; unknown. |
| IR / NAM / captures | Chart:128 mono IR slots,1024/2048 points; simultaneous four1024 or two2048,DSP permitting. Native NAM,converted NAM,proprietary captures unverified. [Chart][HLT-C] |
| Audio / control I/O | Variable-impedance guitar,Variax; paired quarter-inch/XLR outputs; headphones; two sends/two returns; DIN MIDI in/out-thru; shared L6 LINK/AES-EBU output; USB. No mic input,AUX,EXP3,dedicated S/PDIF. EXP2 shares tip/ring amp-control outputs. Connector-level routing review pending. [Chart][HLT-C]; [KB][HLT-K] |
| Power / battery / USB power | Internal AC,IEC inlet. Voltage,current,frequency,battery/USB operation unresolved; DC polarity inapplicable to IEC mains. [Chart][HLT-C] |
| Editor / USB / platforms | HX Edit explicitly supports LT on Windows and macOS; downloads distinguish editor versions3.82 Windows/3.81 Mac. Driver/updater OS requirements need separate review. Chart:8×8 USB audio,USB MIDI,class compliant,iOS audio; iOS editing not established. [Software][HLT-S]; [chart][HLT-C] |
| Looper / scenes / routing | Chart:half-speed120s mono/60s stereo; eight snapshot switches; parallel routing; per-block trails. Full-speed/current looper,drums and snapshot restrictions require manual review. [Chart][HLT-C] |

### Separate IDR offers

| Condition / evidence | IDR ask and qualification |
|---|---|
| Used | Unknown; no condition-verified used offer established. |
| Retail-style hardware offer | **Rp20.040.000**, Seven Stereo Music & Audio Store,Bandung,item1167670551/shop16879370. [Exact hardware][HLT-O]. Reopened2026-10-16 via cached web extraction with **5–7Sep** delivery text; current stock,checkout,new condition,bundle,warranty region,shipping/tax unconfirmed. Late-delivery voucher up toRp10.000 is compensation,not a price discount. |

Remaining:direct complete manual/control inspection,current firmware/category counts,synth/acoustic details,power ratings,IR formats/capture limits,driver/updater requirements,factory subset and condition-verified used/live retail offers. No software,dependencies or project payloads were downloaded or executed for this record.

[HLT-K]: https://kb.line6.com/helix-lt-comparison
[HLT-C]: https://kb.line6.com/__attachments/a_a2761f537d297d89a096c84ee7708fb1fda432484a7b5e3886f8b9d36269c408/Comparison_HELIX_LT.pdf?cb=29d5d8b9fb12df962b8061a40302f54d
[HLT-P]: https://origin.line6.com/helix/helix-lt.html
[HLT-M]: https://line6.com/data/6/0a020a3f18374611d5dffd3a45/application/pdf/Helix%20LT%203.0%20Owner%27s%20Manual%20-%20Rev%20D%20-%20English%20.pdf
[HLT-S]: https://line6.com/software/index.html?hardware=All&name=HX+Edit&os=All&submit_form=set
[HLT-O]: https://shopee.co.id/Line-6-Helix-LT-Streamlined-HX-Guitar-Processor-i.16879370.1167670551

## HX Stomp XL

Consolidated 2026-10-16. The complete original observation below retains its technical date, prices, sources, contradictions and unknowns. This is a document consolidation, not a fresh stock or firmware verification. Historical next-model notes are provenance; use research-state.json for current work.

<!-- LINE6-HX-STOMP-XL source begins -->

Reviewed 2026-10-14. Guitar/bass multi-effects, **large**, no built-in expression. Separate from the existing three-switch HX Stomp. **Partial record**; firmware-specific evidence and unresolved fields are explicit.

### Required comparison

| Field | Evidence-backed result |
|---|---|
| Expression | No built-in pedal; one shared TRS EXP1/2–FS7/8 socket accepts up to two expression/footswitch functions with a suitable Y cable. Compatible external toe-switch control documented [M] |
| Controls K/F/B | **6 / 8 / 4**. Upper/lower encoders, three parameter knobs, rear recessed volume; six stomp switches plus Mode and Tap; View, Action and two Page buttons. Encoder presses and rear power switch are not counted as extra front buttons [M] |
| Dimensions / weight | Manufacturer 2021 chart: **316 W ×120 D ×68 H mm,1.5 kg**; large. Chart PDF text was read but screenshot rendering failed; exact millimetre fit should be checked on the unit. FAQ rounds width to12.5 inches [C,F] |
| Screen | **2.4-inch color LCD**. Explicit touchscreen specification remains **?**; capacitive-touch footswitches do not establish a touch display [P,M] |
| Processing | **8 blocks maximum, DSP-limited**, including amp/cab/IR/looper; parallel A/B path possible. Eight lightweight effects and eight demanding polyphonic effects are not equivalent DSP loads [M] |
| Memory | **128 editable presets,32 banks×4;4 snapshots each**. Factory-filled subset unverified. Snapshots do not add independent preset slots [F,M] |
| Synth / acoustic | **Yes / Yes**: 3 Osc Synth and other Pitch/Synth models; **Acoustic Sim** in EQ category. Ordinary instrument input, no divided pickup required [M] |
| IR | **128 library locations**,1024/2048-sample mono IRs; supported WAV import through HX Edit. DSP limits constrain simultaneous single/dual IR and cab blocks. Exact import conversion restrictions require the HX Edit guide [M,C] |
| NAM / capture | Native NAM, converted NAM and user amp-capture loading **not established** in the checked3.80 documentation. Helix amp modeling and IR import are not NAM support |
| Audio I/O | Two¼-inch instrument/line inputs; two¼-inch balanced TRS/unbalanced TS main outs; one¼-inch stereo TRS send; two¼-inch returns that can become aux inputs; dedicated¼-inch stereo headphones. No XLR mic/phantom or3.5mm aux socket [M] |
| MIDI / USB | Five-pin DIN MIDI IN/OUT-THRU,USB-B for audio/MIDI/editor; shared external-controller socket as above [M] |
| Power | Supplied DC-3 family adapter; panel specifies **9V DC/3A**. This is a supply specification, not measured consumption. Polarity not independently resolved from the parsed panel; USB bus/battery operation not established for XL in this pass. Use the supplied adapter [M,F] |
| Apps | **HX Edit Windows/macOS**, full editing/IR/preset management. iPad/iPhone USB audio/MIDI via appropriate adapter is documented, not a mobile editor. Linux full editor not established [M,P] |
| USB audio | **8 recording channels into the computer,6 active playback channels to hardware**,24-bit/up to96kHz; reamp. Host output7/8 are reserved in the3.80 manual. State direction rather than misreporting eight active playback channels [M,C] |
| Live/practice | Three looper algorithms; full-speed60s mono/30s stereo,half-speed120s mono/60s stereo where supported. Looper occupies a block. Analog or DSP bypass/trails,Command Center,Pedal Edit. No onboard drum-machine claim established [M,C] |

### Effect choices by category — manual3.80

Counts below are a transcription of **model names** in the manufacturer3.80 appendix, including Legacy models but not double-counting mono/stereo implementations:

| Category | Named choices |
|---|---:|
| Distortion |61|
| Dynamics |19|
| EQ |8|
| Modulation |56|
| Delay |45|
| Reverb |25|
| Pitch/Synth |29|
| Filter |15|
| Wah |11|
| Volume/Pan |5|

**274 named effects across these ten categories**, calculated from the appendix, plus three looper algorithms and separate amp/cab/utility choices. The amp/preamp table lists94 guitar and17 bass amp models, with a separate Studio Tube Pre mic-preamp entry; preamp versions are offered separately and are not counted again as new modeled amplifiers. Cabinet/microphone subtotals have not been completely transcribed. The 2021 chart's older231-effect figure is not substituted for the3.80 appendix.

This is a documented firmware3.80 inventory, not a claim that an arbitrary installed unit is updated or that all274 can run together. Official3.80 release notes distinguish hardware firmware from HX Edit3.82 and list6 new amps,4 cabs and1 wah. Later unknown firmware is not assumed compatible.

### IDR evidence

**Retail/indexed ask: Rp14.900.000**, [Seven Stereo, Shopee shop16879370/item22454857163](https://shopee.co.id/Line-6-HX-Stomp-XL-Guitar-Multi-effects-Floor-Processor-i.16879370.22454857163). Retrieved search evidence retains July delivery text, so this is not live checkout verification. The older savedRp14.899.000 is historical discovery, not a current lower bound. **Used IDR: ?**; no condition-verified offer located.

Detailed condition, accessories, warranty, region, final shipping and stock remain unverified. A seller name and late-delivery voucher are not authentication or an applied product discount. No foreign-price conversion or guessed used-price percentage.

### Sources and access limits

[P] [Line6 product page](https://line6.com/hx-stomp-xl/).
[F] [Manufacturer XL FAQ](https://kb.line6.com/hx-stomp-xl-faq).
[M] Manufacturer **3.80 Owner's Manual,40-00-0500 RevD,2024**, actual manual text mirrored at [ManualsPlus](https://manuals.plus/m/7e506bff9341be7f9712b0e10533b9bdee5aaf9de1a0a08688b58130ea5d5e35) and [Manualzz](https://manualzz.com/doc/81729727/line-6-hx-stomp-xl-owner-s-manual). Controls pp.6–8; algorithms pp.26–38; USB section distinguishes reserved playback channels. Generated mirror introductions/FAQs are not evidence.
[C] [Line6-authored2021 processor comparison chart,retailer-hosted PDF](https://tmw.com.sg/wp-content/uploads/2021/11/Line-6-Processor-Comparison-Chart.pdf). Parsed table text was accessible; screenshot attempts failed. Its older model counts and obvious typos in other product columns are not silently copied as current facts.
[R] [Official3.80 release notes](https://line6.com/support/page/kb/effects-controllers/helix/helixhx-380-release-notes-r1079/) and [official software index](https://line6.com/software/index.html?hardware=All&os=All&submit_form=set).

Next: non-Li MOOER GE150 Pro and remaining exact marketplace variants, while preserving the owned-device and original display/IDR queues. Remaining XL gaps include explicit touch/power-operation evidence, current used offers, full cabinet count and factory-filled memory.
<!-- LINE6-HX-STOMP-XL source ends -->

### HX Stomp XL — supporting comparison provenance

The complete supporting comparison was read before merging. Its model-specific values are retained below, including historical shorthand. These do not override fuller qualifications above. Original files and incoming links remain available.

- **Built-in / external expression** (Hardware and displays): No / shared EXP1/2–FS7/8
- **K/F/B** (Hardware and displays): 6/8/4
- **Published dimensions, mm; weight** (Hardware and displays): Manufacturer chart W316×D120×H68; 1.5 kg; chart-render limitation in finding
- **Main display** (Hardware and displays): 2.4-inch color LCD; explicit touch specification unverified
- **Processing and memory** (Processing, storage and loading): 8 DSP-limited blocks; 128 editable presets, 4 snapshots each. Manual 3.80 transcription: 274 named effects across 10 categories, plus looper and separate amps/cabs. Acoustic Sim and synth algorithms documented
- **IR / NAM / captures** (Processing, storage and loading): 128 IR-library locations, 1024/2048 samples; no NAM/capture support established in checked 3.80 evidence
- **Connection / software highlights** (Connections, power and apps): Stereo inputs/outs, stereo-send/two-return loop, dedicated phones, DIN MIDI, USB-B; HX Edit Windows/macOS. Manual distinguishes 8 recording and 6 active playback channels
- **Documented power** (Connections, power and apps): Supplied DC-3-family supply; panel 9 V/3 A, not measured draw; polarity/USB-operation gap retained
- **Used IDR** (IDR observations and original commits): ?
- **Retail observation** (IDR observations and original commits): Rp14.900.000, cached indexed ask; not active-stock proof
- **Original model commit** (IDR observations and original commits): `b4ba5b5559dcdd33b196153d4557408d71cbb89f`

Sources: [effects/findings/2026-10-14-line6-hx-stomp-xl.md](effects/findings/2026-10-14-line6-hx-stomp-xl.md), [effects/shopee-multifx-5.md](effects/shopee-multifx-5.md). No legacy file was deleted.

## HX Stomp

Consolidated2026-10-17. Complete legacy model rows, dated qualifications and URLs are retained below. Display, controls, expression and qualified Shopee offers were additionally checked; indexed manual/guide facts are labelled with access limitations. This existing guitar/bass model adds no inventory count. Verification remains partial.

### HX Stomp historical source evidence

Checked **2026-10-14**. **Partial records**: `?` means unverified, not No. Native NAM, architecture-limited NAM, converted NAM, proprietary captures and cabinet IRs are different capabilities. An effects-only unit is not necessarily an amp modeler.

K/F/B = rotary controls / footswitches / separate buttons. Push-encoders are counted once. Nano Cortex's rotary footswitches are explicitly called out rather than hidden in the knob count. Dimensions are **W×D×H, mm**. Prices are separate **USD** new and used observations; missing used prices have not been invented.

The rounded Line 6 FAQ dimensions are not precision measurements. They establish the category but should not be used as a millimetre-perfect drilling template. Manufacturer FAQ launch prices are **not** presented as current offers.

**HX Stomp's old FAQ says six blocks**, but the official firmware-3.0 release notes increased the limit to **eight**. Similarly, HX Effects' launch FAQ predates full HX Edit support and later model additions. This comparison uses the release notes/current software listing rather than treating the old FAQ's launch-era software limitations and prices as current.

USB audio input/output counts use the manufacturer's interface convention. A capture microphone connector does not establish a dedicated live vocal-effects path. Do not connect an amplifier's speaker output directly to an instrument/capture input; the appropriate load/interface is required.

- **External expression** (No built-in expression pedal): Shared EXP1/2, FS4/5; two controllers with appropriate Y cable
- **K/F/B** (No built-in expression pedal): 6/3/4 [panel]
- **W×D×H; weight** (No built-in expression pedal): Approx. **178×127×64**, 794 g, converted from official FAQ's rounded inches/pounds
- **Size class** (No built-in expression pedal): Compact
- **Used USD** (No built-in expression pedal): ?
- **New USD observation** (No built-in expression pedal): $555, Thomann [P1]
- **Simultaneous processing / available choices** (Processing, presets, IR and capture formats): **8 blocks, DSP-limited**, since firmware 3.0; amp/cab/effects share the budget; current category counts not yet transcribed
- **Preset storage** (Processing, presets, IR and capture formats): **126 editable presets**; factory-filled subset ?
- **Synth / acoustic functions** (Processing, presets, IR and capture formats): Individual synth/acoustic algorithms not yet verified
- **Third-party IR** (Processing, presets, IR and capture formats): Yes; slot/sample limits pending
- **NAM / proprietary capture** (Processing, presets, IR and capture formats): NAM not established; ordinary Helix amp models are not NAM captures
- **Audio/control ports** (Connections, power, software and live use): 2×¼″ in/out; balanced main outputs; stereo TRS send +2 returns; ¼″ headphones; shared EXP/FS; DIN MIDI IN/OUT-THRU; USB-B; DC
- **Power; battery/USB-powered?** (Connections, power, software and live use): Manufacturer specifies **DC-3G supply**, special 2.5 mm pin; **no batteries**; USB-powered operation not established
- **Configuration apps and USB functions** (Connections, power, software and live use): **HX Edit Windows/macOS**; multichannel USB audio/reamp; iOS USB audio via appropriate adapter, not an iOS editor
- **Other important differences** (Connections, power, software and live use): Analog or DSP bypass/trails; flexible parallel routing; looper occupies a block

Original source URLs: https://line6.com/hx-stomp/, https://kb.line6.com/hx-stomp-faq, https://line6.com/support/page/kb/effects-controllers/helix/helix-30-release-notes-r934/, https://line6.com/software/index.html?hardware=All&name=HX+Edit&os=All&submit_form=set, https://www.thomannmusic.com/zoom_b6.htm

The P1 **USD555** observation was checked2026-10-14 at an international store, excluding destination tax/shipping; no IDR conversion or present stock claim is made. [Complete legacy source](effects/advanced-modelers.md) remains available; no source or incoming link was deleted.

### HX Stomp comparison fields

| Field | Dated evidence / qualification |
|---|---|
| Expression | No built-in pedal/toe. Shared EXP1/2–FS4/5 accepts two external expression pedals, two switches, one of each, or compatible Mission pedal/toe-switch combination with appropriate cable/settings. These share one TRS socket, not independent ports. [HS-F](https://kb.line6.com/hx-stomp-faq). |
| K/F/B | **6/3/4**: upper/lower/volume plus three parameter rotaries; three capacitive footswitches; HOME/VIEW,ACTION and two PAGE buttons. Encoder presses counted once; power toggle separate. [HS-P](https://line6.com/hx-stomp/). |
| W×D×H; weight | Approx. **178×127×64**, 794 g, converted from official FAQ's rounded inches/pounds |
| Size class | Compact |
| Used USD | ? |
| Simultaneous processing / available choices | **8 blocks, DSP-limited**, since firmware 3.0; amp/cab/effects share the budget; current category counts not yet transcribed |
| Preset storage | **126 editable presets**, three snapshots each. [HX Edit3.80 guide, indexed device-specific table](https://line6.com/data/6/0a00051aff0e673cd37585ccd/application/pdf/HX%20Edit%20Pilots%20Guide%203.80%20-%20English%20.pdf); full reopening failed. Factory-filled subset remains unverified; do not borrow XL128/four figures. |
| Synth / acoustic functions | Individual synth/acoustic algorithms not yet verified |
| Third-party IR | **128 custom/third-party IR locations**, Single IR1024/2048 samples; one2048 or two1024 blocks per preset, subject to combined cab/IR and DSP restrictions. [Original3.80 manual, indexed evidence](https://line6.com/data/6/0a00051afdda673cccdb61c9c/application/pdf/HX%20Stomp%203.80%20Owner%27s%20Manual%20-%20English%20.pdf). Full reopen exceeded tool size limit; format/conversion details remain unverified. |
| NAM / proprietary capture | NAM not established; ordinary Helix amp models are not NAM captures |
| Audio/control ports | 2×¼″ in/out; balanced main outputs; stereo TRS send +2 returns; ¼″ headphones; shared EXP/FS; DIN MIDI IN/OUT-THRU; USB-B; DC |
| Power; battery/USB-powered? | FAQ officially supports **DC-3G**, legacy source records special2.5mm pin and **no batteries**. Product-panel text calls supplied adapter **DC-3**; name discrepancy retained. Voltage/polarity/current and USB-powered operation not independently verified. [HS-F](https://kb.line6.com/hx-stomp-faq),[HS-P](https://line6.com/hx-stomp/). |
| Configuration apps and USB functions | **HX Edit Windows/macOS**; multichannel USB audio/reamp; iOS USB audio via appropriate adapter, not an iOS editor |
| Other relevant features | Analog or DSP bypass/trails; flexible parallel routing; looper occupies a block |
| Display | **2.4-inch color LCD**, explicitly published. Touchscreen and numerical pixels unverified; capacitive footswitches do not establish a touch display. [HS-P](https://line6.com/hx-stomp/) |
| Used IDR | **Rp8.900.000**, explicitly Second/Bekas/Preloved, **Habis**; sellerotnielsusanto,shop91725285/item26545060709,Kota Surabaya. Indexed reopening checked2026-10-17; stale25–27September delivery. Historical ask, not an available offer or completed sale. Condition grade/accessories,warranty region,delivered charges and voucher eligibility unconfirmed. [Exact used listing](https://shopee.co.id/Line-6-HX-Stomp-%28Second-Bekas-Preloved%29-Digital-Multi-Effects-Electric-Guitar-Bass-Keyboard-Efek-Gitar-Elektrik-Akustik-i.91725285.26545060709) |
| New / retail IDR | **Rp11.229.000**, ROCKPIZZ MUSIC,shop440477624/item23519849983,Kota Denpasar,black HX Stomp. Indexed reopening checked2026-10-17,stale18August delivery. Retail hardware title; detailed condition,stock,accessories,warranty region,delivery/tax and voucher eligibility unconfirmed. Not HX Stomp XL. [Exact retail listing](https://shopee.co.id/LINE-6-HX-STOMP-MULTI-EFFECTS-GUITAR-PEDAL-BLACK-i.440477624.23519849983) |

### HX Stomp evidence limits

The product page/FAQ still contain six-block wording. Retain the firmware3.0 eight-block correction above; do not revert based on launch copy or equate advertised available-model totals with simultaneous capacity. Firmware-current category counts, exact synth/acoustic algorithms, IR import conversion, NAM/capture support, screen touch/pixels, detailed USB channel/driver/updater requirements and looper/drum limits remain open. No sibling XL specifications are substituted. Published2.4-inch display and numbered control descriptions are model-specific evidence; no screen size was measured from a photo. The3.80 manual/guide details above came from indexed original-document excerpts; full-file reading or visual inspection is not claimed.

## POD HD500

Original guitar multi-effects;distinct fromHD500X. Checked2026-10-17;partial. Exactsellerunit identity remainsunconfirmed;ownership pending. Bass support is documented in the original v2.10 guide.

<!-- comparison evidence begins -->

| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression | **Built-in pedal+toe switch;external PEDAL2**. Without external, toe togglesEXP1/2;with external,built-inEXP1/externalEXP2. Toe can toggleamp/FX blocks. | [Guide3•7–13][HD5-M] |
| K/F/B | **13 rotary controls:12 top (PRESETS,four multifunction,Drive,four tone,Volume,Master)+rear Mic Level;12 footswitches (FS1–8,Bank↑/↓,Tap,Looper),plus expression toe**. Four dedicated buttons (Save,View,Move,Enter),four-way navigation pad andPRESETS push;counted separately. Text-derived inventory;panel-image verification pending. | [Pilot RevC,controls1–14,22][HD5-QC] |
| Display | **LCD**;diagonal,color,touch unverified. | [Pilot control1][HD5-QC] |
| Dimensions / mass | FAQ: **21.50W×10.29D×2.91H inches**;masspending. Large footprint. | [OfficialFAQ][HD5-F] |
| Processing / category choices | **Eight FX blocks**,any one caninstead hosthardwareFXloop. **Up to two amp blocks** whenplaced inparallelA/B;singleamp canusePre/Post/A. Mixer fixedafterA/B. DSPlimits constraincombinations. FamilyFAQ lists dynamics8,distortion15,modulation22,filter17,pitch3,EQ5,delay19,reverb12,wah8,volume/pan. Family80/90/100+ wording isnotfirmware-currentHD500 total;revisionaudit pending. Do nottransferHD500X DSPcapacity. | [Guide3•1–4,3•14][HD5-M];[FAQ][HD5-F] |
| Bass capability | **Yes: Flip Top bass amp (Ampeg B-15NF Portaflex), matching 1×15 cabinet and eight bass-cab microphone models**. Guide explicitly recommends this processing to bass players; no optional pack is needed to establish this documented v2.10 capability. Firmware2.62 supports optional purchasedMetal,Vintage andBass packs;Bass examples includeSVT/GK800RB. These are notincluded-base-library claims. | [Guide6•4,6•6,6•13,6•15][HD5-M] |
| Factory / user memory | **8 setlists×64=512 presetlocations**. All locations writable;initialfactoryfill pending. | [Guide4•1][HD5-M] |
| Synth / acoustic | **Synth yes**:v2.10 filter-model table listsOctisynth,Synth O Matic,Attack Synth,Synth String andGrowler. Dedicated acoustic-simulation algorithm unverified. Variax Acoustic control isnot onboardacousticsimulation proof. | [Guide7•5][HD5-M] |
| I/O | Rear diagram includesguitar,mic,AUX,CD/MP3,phones,balanced/unbalanced outputs,FXloop,PEDAL2,MIDI,S/PDIFout,USB,Variax,L6LINK,DC. FAQ confirms **XLRmic has no phantom power**;externalphantomsupply/preamp neededforcondenser. Pilot specifies **two ¼-inch unbalanced outs,two balanced XLR outs,mono unbalanced ¼-inch AUX,one TRS stereo FXsend andtwo FXreturns L/Mono+R;MIDI In+Out/Thru**. Remaining socket sizes/types pending. | [Guide1•4][HD5-M];[FAQ][HD5-F];[Pilot15–28][HD5-QC] |
| Power / battery / USB | FAQ **DC-3g9V DC3A,2.5mm,center-negative**;guide rearlabel2.5Aminimum. Supplyrating≠measureddraw. Battery/USBpower unknown. | [FAQ][HD5-F];[Guide1•4][HD5-M] |
| IR / NAM / capture | UserIR,native/convertedNAM,captureimports unverified. | Unresolved |
| Editor / software | **POD HD500 Edit Windows/Mac editor/librarian**;USB audio driver chapter. Driver routesprocessedrecordsend tocomputer andmixeslocalmonitor withcomputerplayback atanalogouts. **USB audio muted whenL6LINK connectsDT25/DT50**. Guide recommendsdirectUSB2,not hub. FAQ specifiesUSBrecord sends1–2 and44.1/48/88.2/96kHz,16/24bit support. BothMac/Windows driver sections expose **one stereo1–2 MainOut recordsend**,notmultitrackisolatedstems. Updatearticlepairs **flash2.62 withEdit2.26** topreventinvalidpresetdata/high-volumeevents;Englishheading differsfromolder2.02/2.00translations. Playbackchannels/currentOS pending. | [Guide1•5,9•1–2][HD5-M];[FAQ][HD5-F];[Updatearticle][HD5-U] |
| Global EQ / firmware | **Free v2.62 Global EQ:three parametric bands plus low/high cut**,appliesacrosspresets/setlists;**not available atL6LINK output**. Release notes also specifyUSBfirmware1.04. | [Release notes][HD5-R] |
| Looper / drums / live | **Mono24s normal/48s half-speed**,overdub,undo,reverse. Switchingrecordedspeed changespitch byoctave andplaybackspeed by2×. Storage,drums,scenes/trails pending. | [Guide8•1,8•6][HD5-M] |

### Separate IDR hardware offers

| Condition | Evidence | Source |
|---|---|---|
| Used | Unknown;conditionandunitidentity unconfirmed. | — |
| New | Unknown;conditionandunitidentity unconfirmed. | — |

<!-- comparison evidence ends -->

### Identity-unverified seller lead

[HopeMusic HD500](https://shopee.co.id/Efek-Line6-HD500-i.703817770.29524092321),shop703817770/item29524092321:Rp3,499,000,22%display,month-oldstorefront;itemcachemiss. Displaymodel242513456401 notvalidatedvariant. Condition,stock,region,bundle/adapter,workingstate andvoucher/checkout terms unknown. Checked2026-10-17;notqualifiedused/newprice. SellerHD500title doesnot prove exactunitversusHD500X.

Officialguide v2.10RevA©2012 explicitly coversoriginalHD500;manufactureridentity established independently ofsellerunit. No software/firmwaredownloaded.

[HD5-M]: https://l6c-acdn2.line6.net/data/6/0a06434dc1a55085c5d6532bf/application/pdf/POD%20HD500%20Advanced%20Guide%20v2.10%20%28%20Rev%20A%20%29.pdf
[HD5-F]: https://kb.line6.com/pod-hd500x-hd500-pod-hd-pod-hd-pro-faq

### Output and access qualifications

FAQ global output modes:Studio/Direct,Combo/Stack Front,Combo/Stack PowerAmp. They affectunbalanced/XLR/headphone andUSBrecord sends. Frontmodes targetampinputs;PowerAmpmodes targetreturns withAMP/LINEsetLINE. OfficialQuickStartRevB linkfailedcachemiss;physicalcontrolcount remainspending.

[HD5-Q]: https://l6c.scdn.line6.net/data/l/0a06434dc35d4ca4b2d228923/application/pdf/POD%20HD500%20Quick%20Start%20Guide%20%28Rev%20B%29%20-%20English.pdf

### Stereo signal-path restrictions

Guide2•7 and3•6:inputs1/2 feedA/B separately whenPre isempty;anactive monoamp/FX inPre combines inputs. MonoFX laterinthechain collapse upstreamstereo. EQ/wah/volume andselectedothers preservestereo. Stereo hardwareconnections alone donotguarantee stereoprocessing. [Advancedguide][HD5-M]

QuickStartmirrorattempts atmanuals.plus andGrahamEnglishWiki failed;no physicalcount inferred fromunseenimages.

### Pilot handbook access and controls

Manufacturer-authored mirror identifiesoriginalPOD HD500 Pilot’s Handbook,**40-00-0281 RevC**,notHD500X;readabletranscript checked2026-10-17. Powercontrol29 says unplug toturnoff. CD/MP3feedsphones andbothanalogoutputpairs. No filedownload orvisualpanelverification. OfficialRevB remainedinaccessible;revisiondifference retained.

[HD5-QC]: https://manualzilla.com/doc/5804481/hd500-quick-start-guide

### Firmware and editor qualifications

[Official v2.62 release notes][HD5-R] distinguishfreefirmwareGlobalEQ fromoptionalpurchasedamp/cabpacks. [Update article][HD5-U] Englishsection pairsflash2.62/Edit2.26;itsFrench/Germansections retainolder2.02/2.00labels,andEnglishrestorationparagraphmentionsEdit2.00. Versionconflict retained. Articlewarnsolderasynchronoussync couldcorruptpresets andcauseintermittenthighvolume;invalidpresets resettoNew Tone (Reset). Manufacturerprocedure requiresbackup,editorbeforeflash,globalreset andpedalrecalibration. Documentationonly;noinstaller/firmwaredownloadedorrun.

[HD5-R]: https://kb.line6.com/pod-hd500-hd-desktop-hd-pro-v2-62-release-notes
[HD5-U]: https://kb.line6.com/pod-hd500x-hd500-hd400-hd300-hd-hd-pro-firmware-v2-62-and-pod-hd-hd500-hd400-hd300-hd-pro-edit-v2-26-update-instructions

## M5

Effects-only multi-category processor; one selected model plus gate,not a chain processor. Eligible under multi-category scope; distinct from dedicated single-purpose pedals and M9/M13. Checked2026-10-17;partial. Ownership and vocal suitability unverified. Bass suitability documented for Bass Octaver;not every model is certified equally suitable.

| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression | External EX-1/passive10kΩ linear mono¼-inch;multiple parameters,heel/toe values per preset. Built-in/toe switch unverified. | [Handbook PDF pp4,7–8][M5-M] |
| K/F/B | **6 rotary /2 footswitches /separate buttons unverified**;text-derived model selector+five parameter knobs,OnOff+Tap;selector push additional. | [Handbook PDF pp4–6][M5-M] |
| Display | Category-colored LCD;diagonal,touch unverified. | [Handbook PDF p4][M5-M];[FXParameters §4•1][M5-F] |
| Processing / category choices | One selected model plus separate gate;five categories:delay,modulation,distortion,filter,reverb. **109 selectable models in2011guide:19delay+22modulation+30DIST-category+26filter+12reverb**. Delay includes15families plus4separate DryThru variants. DIST includes17drive/octave entries,volume,6compressors,selectable gate and5EQs;the separate setup gate is not an extra selectable model. Filter=16FM4-style+8wah+PitchGlide+SmartHarmony. Internal settings do not add models. Manufacturer100+ claim retained;counts tied to cited guide,not a claim about unverified firmware revisions. | [Handbook PDF pp4,7][M5-M];[Manufacturer resource indexed excerpt][M5-R];[FXParameters §§1•1,2•1,3•1–9,4•1,5•1][M5-F] |
| Factory / user memory | **24 factory-filled writable presets**,not24+24. Manual/autosave modes;LOAD waits confirmation,INSTANT switches immediately. | [Handbook PDF pp5–6][M5-M] |
| Synth / acoustic | Synth options include Octisynth,Synth-O-Matic,AttackSynth,SynthString andGrowler. VoiceBox/VTron imitate vowel/talkbox behavior without establishing a microphone vocoder path. Dedicated acoustic simulator not established by this guide. | [FXParameters §§4•4–10][M5-F] |
| Dimensions / mass | Unknown;not borrowed from M9/M13. | Unresolved |
| I/O | Stereo Lmono/R inputs andoutputs,expression,DC,MIDI IN/OUT;connector sizing andother ports pending. SysEx preset backup/restore,MIDIclock,PC0–23,CC expression/tap/bypass/tuner. | [Handbook PDF pp4,6,8][M5-M] |
| Power / battery / USB | **9VDC,500mA included supply rating**,not measured draw. Polarity,currentdraw,battery/USB operation unknown. | [Handbook PDF p4][M5-M] |
| IR / NAM / capture | UserIR,native/convertedNAM,capture import unverified. | Unresolved |
| Editor / software | Line6Monkey firmware updater via external MIDI interface;editor/platform/current compatibility pending. | [Handbook PDF p7][M5-M] |
| Looper / drums / live | True/DSP bypass;DSP retains disengaged delay/reverb tails. Tuner selectablemute/bypass. Looper,drums,scenes pending. | [Handbook PDF pp5–6][M5-M] |

### Separate IDR hardware offers

| Condition | Evidence and limits | Source |
|---|---|---|
| Used | Unknown;no condition-verified offer. | — |
| New | Unknown;no condition-verified offer. | — |
| Condition-unverified cached offer | **Rp2,921,000**;Gelora Musik Serpong,Kab.Tangerang;shop306155985/item6072223176. Checked2026-10-17;direct web open/search returned2month cachedpage with15–16August delivery. Sale condition,working state,revision,adapter/bundle,warranty,variant,shipping/tax unknown. No Habis in excerpt is not stock confirmation. Late-arrivalRp10,000 compensation is not price discount. | [Exact hardware item][M5-O] |

### Source-access provenance

RevB Handbook accessed as webPDF text,10pages; citations use PDF page numbers. Former productURL https://line6.com/effects-pedals/m5/ redirects to current /pedals/; no HX One specifications transferred. Original M5 resource search excerpt available,subsequent direct fetch failed. No downloads or physical inspection.

[M5-M]: https://line6.com/data/6/0a06434d12155507f39d011ad3/application/pdf/M5%20Pilot%27s%20Guide%20-%20English%20%28%20Rev%20B%20%29.pdf
[M5-R]: https://origin2.line6.com/effects-pedals/resources/
[M5-O]: https://shopee.co.id/Stombox-Modeller-Pedal-Line-6-M5-i.306155985.6072223176

[M5-F]: https://line6.com/data/6/0a060b316ac34f0593fabe278/application/pdf/M13/M9/M5

## M9

Effects-only guitar/shared-bass multi-effects; distinct from M5/M13. Checked2026-10-17;partial. Ownership/vocal suitability unknown.

| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression | Two external EX-1/passive10kΩ linear mono¼-inch inputs. Built-in/toe switch unverified. FX assignments per scene;looper assignment global. | [Pilot PDF p4][M9-M];[Advanced §§2•2–3][M9-A] |
| K/F/B | **6 rotary /7 main footswitches /separate buttons unresolved**;model+5parameter knobs,6A/B memories+Tap,text-derived. Encoder push additional. | [Advanced §1•1][M9-A];[Pilot PDF pp4–5][M9-M] |
| Display | Category-colored LCD;diagonal,touch unknown. | [Pilot PDF pp4–5][M9-M] |
| Processing / category choices | **3 simultaneous FX**,one of A/B per FXunit;additional setup gate. Firmware2.01 FAQ:109=30DIST/comp/EQ/volume+22mod+26filter/pitch+19delay+12reverb. | [Pilot PDF pp4,8][M9-M];[FAQ][M9-Q] |
| Factory / user memory | **24 scenes=4folders×6** with2.01;each stores6FX memories,3active. Factory examples;manual/autosave available. Not24user+24preset. | [FAQ][M9-Q];[Pilot PDF pp5–7][M9-M] |
| Synth / acoustic | Shared guide explicitly covers M9:Octisynth,Synth-O-Matic,AttackSynth,SynthString,Growler;BassOctaver expressly suitable for bass. Acoustic simulator unverified. | [FXParameters §§3•6,4•8–10][M9-F] |
| Dimensions / mass | FAQ:**10.5L×7W×3H inches;2.3lb**. Axes/weight retained exactly as manufacturer claim;physical corroboration pending. | [FAQ][M9-Q] |
| I/O | Unbalanced instrument-level¼-inch mono L/R input/output pairs,2¼-inchEXP,MIDI IN/OUT,power. SysEx scenes;MIDI PC0–23 selects scenes,CCs toggle loaded A/B effects;individual model selection/assignment via MIDI not implemented. Looper levels are expression-only,not MIDI CC. Other ports unverified. | [FAQ][M9-Q];[Pilot PDF p4][M9-M];[Advanced §§A•1–4][M9-A] |
| Power / battery / USB | FAQ specifies **PX-2 only,9V2000mA,2.5mm,center-positive wording;no batteries**. M9 FAQ omits AC/DC type,but Line6 identifies the same named PX-2 as an AC supply: **9VAC2000mA supply specification** supported by combining named-adapter sources. DC polarity is inapplicable to AC;FAQ center-positive wording retained as conflict,not DC compatibility. Actual draw/USB operation unknown. | [FAQ][M9-Q];[Line6 PX-2 identification][M9-P] |
| IR / NAM / capture | UserIR,native/convertedNAM,capture import unverified. | Unresolved |
| Editor / software | Line6Monkey updater;MIDI scene backup/restore. Editor/platform/current compatibility unknown. | [Pilot PDF p8][M9-M] |
| Looper / drums / live | **Mono28s/56s halfspeed** perPilot andAdvanced§5•1 vs **30s/60s** FAQ:unresolved conflict. Overdub,undo/redo,reverse. Loops cannot be archived;only current session retained. MIDI looper control leaves sixFX switches available. PRE/POST selectable;Pilot before/after label conflicts with its playback-effect explanation,andAdvanced§5•3 repeats PRE=noFX/POST=FX wording. Hardware behavior unresolved;do not silently reverse labels. Stereo collapses at mono effect. Chain1→2→3 orreverse;DSP bypass trails. Tuner bypasses FX+loop,selectablemute. Drums unknown. | [Pilot PDF pp6–8][M9-M];[Advanced §§5•1–3,A•1–4][M9-A];[FAQ][M9-Q] |

### Separate IDR hardware offers

| Condition | Evidence and limits | Source |
|---|---|---|
| Used | Unknown;no qualified exact-item observation. | — |
| New | Unknown;no qualified exact-item observation. | — |
| Unqualified shop-index lead | **Rp3,388,000**,Namin Music;3month searchcache checked2026-10-17. Index label ProdukBaru does not confirm actual sale condition. Exact item/shopIDs,region,stock,revision,bundle/adapter,warranty,voucher,shipping/tax unknown;directshopopen failed. Not an exact hardware offer or current retail range. | [Shop index][M9-O] |

### Source-access provenance

Own RevC Pilot(8PDFpages),v2.0 Advanced guide RevA and model-specific FAQ used;no M5 power/memory borrowed. Guide citations use printed chapter notation except Pilot PDF positions. No downloads. Forum power anecdotes were encountered but not adopted as specifications.

[M9-M]: https://line6.com/data/6/0a06434d12161507f39faccc35/application/pdf/M9%20Pilot%27s%20Guide%20-%20English%20%28%20Rev%20C%20%29.pdf
[M9-A]: https://line6.com/data/6/0a060b316ac34f0593fca717b/application/pdf/M9%20Advanced%20Guide%20-%20English%20%28%20Rev%20A%20%29.pdf
[M9-Q]: https://kb.line6.com/m9-stompbox-modeler-faq
[M9-F]: https://line6.com/data/6/0a060b316ac34f0593fabe278/application/pdf/M13/M9/M5
[M9-O]: https://shopee.co.id/namin_music

[M9-P]: https://kb.line6.com/line-6-four-button-stompbox-pedal-faqs

## Pocket POD

Handheld multi-effects;distinct from Pocket POD Express. Checked2026-10-17;partial. Ownership,vocal suitability unknown. Bass use documented for Tube Preamp.

| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression | Built-in/external/toe unverified. No standardMIDI/Line6 footcontroller compatibility perFAQ. | [FAQ][PP-Q] |
| K/F/B | **4 rotary /0 listed footswitches /3 physical button assemblies**,text-derived:Drive,Effects,Delay,ChanVol;Save,Tap,4-wayNav. Directional contacts distinguished from assemblies. | [Reference §§1•1–3][PP-M] |
| Display | LCD confirmed by official product page;diagonal,color,touch unknown. | [Reference §1•2][PP-M];[Product indexed text][PP-R] |
| Processing / category choices | **32amp,16cabinet choices**;manual advertises15effectmodels plus separate reverb/gate. Reference§4•5 lists **8single selections+7delay-combinations+Bypass=16positions**;15processing selections when bypass excluded. Productpage advertises16effectmodels;count basis differs,not16independent algorithms. Singles:compressor,tremolo,chorus1/2,flanger1/2,rotary,delay. Combinations:delay with comp,tremolo,chorus1/2,flanger1/2,swell. Reverb spring/room selected byamp;gate separate. Explicit simultaneousceiling pending. | [Reference §§1•1,3•1,4•1–5][PP-M];[Product indexed text][PP-R] |
| Factory / user memory | **300+ total,124factory-filled user=31×4**;Band/Style read-only,remainder exactcount unknown. | [Reference §2•1][PP-M] |
| Synth / acoustic | Dedicated synth/acoustic simulation unverified. TubePreamp explicitly usable as bassDI. | [Reference §3•2][PP-M] |
| Dimensions / mass | **5in long×3½in wide×2in deep;6oz**,manufacturer wording. Battery inclusion unspecified;axes not silently relabeled. | [Product indexed text][PP-R] |
| I/O | Mono¼-inchguitar input/ampout,stereo⅛-inchAUX/phones-direct,DC,miniUSB. USBMIDI,class-compliant;manufacturer explicitly says no direct USB recording. | [Reference §§1•3–4][PP-M];[Pilot p9][PP-P];[Product indexed text][PP-R] |
| Power / battery / USB | DC-1 **9.6VDC200mA center-negative supply rating**,notdraw;four nonrechargeable alkalineAAA,4–6h conditional. USB neither powers nor charges;USB/input connection turnsuniton. Currentproduct lists9VDC/DC1g versus older9.6VDC/DC1 supply specification;distinct adapter references retained,not a measured voltage range. | [Reference §§1•4–6][PP-M];[Product indexed text][PP-R] |
| IR / NAM / capture | UserIR,native/convertedNAM,capture unverified. FAQ denies purchasablemodelpacks. | [FAQ][PP-Q] |
| Editor / software | Vyzex editor/librarian Mac/Windows;FAQ says no longer supported. Monkey updater separate. CurrentOS compatibility unknown. | [Pilot p10][PP-P];[FAQ][PP-Q] |
| Looper / drums / live | Cabinet-tuning modes A/B/C/D/Direct;unplug input when unused. Tuner436–445Hz. Looper,drums,scenes,trails unverified. | [Pilot pp4,6,8][PP-P] |

### Separate IDR hardware offers

| Condition | Evidence and limits | Source |
|---|---|---|
| Used | Unknown;no condition-verified offer. | — |
| New | Unknown;no condition-verified offer. | — |
| Condition-unverified cached offer | **Rp2,112,000**;Awlind Music Official,KotaBandung;shop78230612/item2863842140. Checked2026-10-17;lastmonth searchcache,16–18Sepdelivery. Directwebopen failed. Salecondition,workingstate,revision,adapter/bundle,warranty,variant,shipping/tax unknown. No Habis in excerpt does not confirm stock. LatearrivalRp10,000 compensation not discount. | [Exact indexed item][PP-O] |

### Source-access provenance

ReferenceRevA2007 andPilotRevB2022 accessed aswebPDFtext. OldReference says USBcableincluded;2022Pilot says notincluded:bundle depends ondate,not guaranteed by seller title. No Express specifications transferred. No downloads.

[PP-M]: https://line6.com/data/l/0a06007212036468013d917d3a/application/pdf/Pocket_POD_Reference_Manual.pdf
[PP-P]: https://line6.com/data/6/0a00050b264e6643ac1a367bb/application/pdf/Pocket%20POD%20Pilot%27s%20Guide%20-%20English%20.pdf
[PP-Q]: https://kb.line6.com/pocket-pod-faq
[PP-O]: https://shopee.co.id/ALAT-MUSIK-Line-6-Pocket-POD-i.78230612.2863842140

[PP-R]: https://line6.com/pocket-pod/?locale=en_US

## HX One

Effects-only multi-category guitar/bass processor;distinct from HX Effects/HX Stomp. One selected model,not a multi-block chain. Checked2026-10-17;partial. Ownership/vocal suitability unknown.

| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression | External TS expression,TRS dualswitch,or expression+switch;no built-in pedal established. Toe switch unverified. | [Product][HX1-P] |
| K/F/B | **4 rotary /2 main footswitches /3 buttons**;Effect+3parameter,On+TapFlux,HomeSave+2Page,text-derived;rotary pushes additional. | [Product controls][HX1-P] |
| Display | **128×32pixel OLED**. Yamaha Singapore table prints **“1.7/43 (OLED)”** without units or diagonal label;retain raw claim,not verified inches/mm diagonal. Color/touch unknown. | [FAQ][HX1-Q];[Yamaha Singapore][HX1-SG] |
| Processing / category choices | **1selectedeffect+inputgate**. Product250+;launchFAQ260+ tiedto3.60/anticipated3.70. RevF firmware3.83 tables: **61distortion+24Dynamics-table entries(including5volume/pan utilities)+8EQ+56modulation+45delay+25reverb+29pitch/synth+26wah/filter+2looper families=276listed models**. Counting mono/stereo looper variants separately gives278entries;ordinarymono/stereo processing is not double-counted. Table-derived count,not a substituted manufacturer headline. Separateinputgate excluded. Flux ramps parameter states,not an extra simultaneousmodel. | [FAQ][HX1-Q];[Manual pp1,13–20][HX1-M] |
| Factory / user memory | **128factory-filled writable presets**,not128+128;user modeldefaults separate. | [FAQ][HX1-Q];[Manual p11][HX1-M] |
| Synth / acoustic | AcousticSim inEQ;3OSC Synth plusLegacy synths. 3NoteGenerator/4OSCGenerator generate without instrument input and load disabled. PolyPitch/Wham/Capo/12String designatedmono. | [Manual pp14,17–18][HX1-M] |
| Dimensions / mass | **125W×96D×62H mm;450g**. Manufacturer Japanese launch release dated2023-10-25;mass inclusion basis unstated. | [Yamaha Japan][HX1-J] |
| I/O | Unbalanced¼-inchTS L/R inputs/outputs,EXP/FS3/4,DC,USB-C,MIDIIN+OUT/THRU. Instrument/line settings. Insert mode repurposes rightI/O as mono send/return,sacrificing stereo;position per preset. USBMIDI;USBaudio unverified. RevF:HX stereo models process discrete L/R except designated mono/polyphonic models;Legacy models are mono-in/stereo-out. Lmono-only output folds to mono. | [Manual pp6–8][HX1-M];[Product][HX1-P] |
| Power / battery / USB | **9VDC center-negative2.1mm,500mA included adapter**;FAQ drawjustunder400mA,distinct fromsupplyrating. Battery/USBpower unverified. | [Product][HX1-P];[FAQ][HX1-Q] |
| IR / NAM / capture | UserIR,native/convertedNAM,capture import unverified;effectsmodeling not capture import. | Unresolved |
| Editor / software | HXOneLibrarian macOS/Windows forpresets/backups;Line6Central updater separate. **Not HXEdit compatible**. Presets are incompatible with otherHelix/HXhardware,HXEdit andHelixNative;names up to16characters. ExactcurrentOS/editorparameters pending. Historical3.70release notes identify separate macOS/Windows Librarian packages12407/12408;both links redirect tologin on2026-10-17. Do not substitute firmware-package OS metadata for librarian requirements. | [Manual pp4,11][HX1-M];[FAQ][HX1-Q];[3.70release notes][HX1-S] |
| Looper / drums / live | Simple/Shuffling mono60s/stereo30s;Simple halfspeed viaMIDI doublesrecordtime. Insert forcesmono. Presetchange stops/discardsloop;poweroff discards. True/DSPbypass,adjustableinputimpedance,Flux andtuner. Insert mode requires DSPbypass to maintain send/return signal. Tuner425–455Hz,factory440;outputMute/Dry/Effect,factoryMute;preceding pitch/modulation effects impair tuning. Last edits/bypass restore afterpowercycle only after≥3ssettling;perpresetbypass recall documented from3.81. Drums unknown. | [Manual pp10,12–13,19,27,29][HX1-M];[Product][HX1-P] |

### Separate IDR hardware offers

| Condition | Evidence and limits | Source |
|---|---|---|
| Used | Unknown;no condition-verified offer. | — |
| New | Unknown;no condition-verified offer. | — |
| Condition-unverified cached offer | **Rp5,099,000** directURLcached3weeks,23–24Sepdelivery;older2monthsearchcache **Rp5,040,000**,6–8Augdelivery. SameSevenStereoMusic&AudioStore,KotaBandung;shop16879370/item26668651924. Checked2026-10-17. Neither provescurrentstock;noHabislabel is not availability. Salecondition,workingstate,firmware,adapter/bundle,warranty,variant,shipping/tax unknown. LatearrivalRp10,000 compensation not discount. | [Exact item][HX1-O] |

### Source-access provenance

OwnRevF manual2025 forfirmware3.83,manufacturer product andlaunchFAQ readaswebtext. FAQlaunch wording retainsoldercounts/features;do not use it to deny latermanual additions. No downloads,firmware installs orphysical inspection.

[HX1-P]: https://line6.com/hx-one/
[HX1-Q]: https://kb.line6.com/hx-one-faq
[HX1-M]: https://line6.com/data/6/0a0004220039697155cf001b7/application/pdf/HX%20One%20Owner%27s%20Manual%20-%20English%20.pdf
[HX1-O]: https://shopee.co.id/Line-6-HX-One-Guitar-Multi-effects-Floor-Processor-i.16879370.26668651924

[HX1-S]: https://line6.com/software/index.html?hardware=All&locale=en_US&os=All&software=HXEdit&submit_form=set

### Historical firmware qualifications

Official3.70notes list lost3.60userdefaults afterupdate,TrueBypasstuner failure andInsertPost stereofolding issues;3.71notes repeat those knownissues. These are historical version qualifications,not claims that3.83 remains affected. RevF covers3.83. Package links https://line6.com/software/readeula.html?rid=12407 and https://line6.com/software/readeula.html?rid=12408 were read only;no login,download,installation orupdate performed.

### Regional manufacturer specification qualifications

Yamaha Singapore table lists268effectmodels without firmware date,distinct from launch250+/260+ and the RevF3.83 table audit;not silently substituted. Its bundle includesDC1G,while table saysDC-1;regional bundle does not establish the Indonesian seller’s adapter. Table’s “Stereo L/R, Return L/R” input wording does not establish extra physical return sockets:ownmanual documents repurposed rightI/O in Insert mode. Checked2026-10-17 as webtext;no downloads.

[HX1-J]: https://www.yamaha.com/ja/news_release/2023/23102501/
[HX1-SG]: https://shop.sg.yamaha.com/hx-one-set.html

## Helix Floor

<!-- comparison evidence begins -->
Checked **2026-10-17**. Original Helix Floor; distinct from LT,Rack and Stadium. Guitar, bass and live microphone processing explicitly documented. Platinum is the same hardware with a different finish per manufacturer timeline;count once.

| Required field | Finding |
|---|---|
| Built-in / external / toe expression | Built-in pedal; toe toggles EXP1/2;two external EXP2/3 inputs. CV/expression output and amp-switch output separate. [Cheat sheet][HF-S], [Floor product][HF-P] |
| Knobs / footswitches / buttons | **10 rotaries including rotary joystick /12 footswitches /8 separate front buttons**:Preset,Volume,Phones,6parameter knobs,joystick;Save,Menu,Home,Amp,Bypass,Action,2Page buttons. Push encoders counted once; toe, rear power/ground lift additional. Text-derived; product’s thirteen-strip wording conflicts with FS1–12 cheat sheet. [Cheat sheet][HF-S], [Floor product][HF-P] |
| Display | **6.2-inch,800×480 color LCD**;touchscreen **?**. Capacitive foot controls do not prove screen touch. Separate scribble strips;exact count/diagonal pending given the product wording conflict. [Comparison KB][HF-K], [Floor product][HF-P] |
| Dimensions / weight | KB **22.05 W×11.85 D×3.58 H inches;14.7lb**;older manufacturer FAQ **22.05×11.85×3.6 inches;14.6lb**. Preserve rounding/mass difference; basis unspecified. [Comparison KB][HF-K], [FAQ][HF-Q] |
| Simultaneous blocks | Indexed manufacturer chart **up to32,DSP-permitting**;four stereo paths. Four-amp/IR concurrency claims are DSP-qualified; heavy chains may reach the limit earlier. [Chart][HF-C], [FAQ][HF-Q], [Floor product][HF-P] |
| Category choices | Indexed chart 96amps/268effects,firmware basis unstated; older KB 62amps/37cabs/16mics/104FX is historical. Current 3.80 category-by-category audit **?**. Do not presentolder totals as the current installed library. [Chart][HF-C], [Comparison KB][HF-K] |
| Factory / user presets | **1,024 locations** (8×32×4);factory-filled subset **?**;up to 8 snapshots per preset. Snapshots are variations,not additional preset slots. [Chart][HF-C], [Floor product][HF-P] |
| Synth / acoustic simulation | Own cheat sheet documents the Pitch/Synth category;exact synthesis/acoustic simulator algorithms and restrictions **?**,not borrowed from LT. [Cheat sheet][HF-S] |
| IR / NAM / capture | User IRs supported;older manufacturer FAQ **128 slots, 1024/2048 points, up to 4 simultaneous DSP-permitting**. Native NAM, converted NAM, proprietary capture loading **?**;Stadium Proxy not inferred. [FAQ][HF-Q] |
| Audio/control I/O | Guitar/active-instrument AUX;XLR mic with 48 V;4 send/return pairs;stereo XLR and¼″TS mains;stereo phones;VDI;EXP2/3;ExtAmpTRS;CV/EXPout;DIN MIDI in/out-thru;RCA S/PDIF in/out;AES/EBU/L6 LINK out;USB;groundedAC. Exact remaining jack types/USB connector pending manual. [Cheat sheet][HF-S], [Floor product][HF-P] |
| Power / battery / USB | Grounded AC in confirmed;voltage/frequency/current **?**. DC polarity N/A. Battery/USB-powered operation **?**;USB interface does not prove bus power. [Cheat sheet][HF-S] |
| Editor / USB audio | **HX Edit** editor distinct from Helix Native plugin/updater;Mac/Windows documented; exact current OS versions **?**. **8-in/8-out,24-bit/up to 96 kHz**,DI/reamp/MIDI;iPad with camera adapter. [Cheat sheet][HF-S], [Floor product][HF-P], [Software][HF-D] |
| Looper / snapshots / routing | One looper per preset. Manufacturer KB gives **60 s mono/30 s stereo at full speed**, doubled at half speed. Across presets, KB requires matching mono/stereo type, path and footswitch assignment; indexed Floor manual additionally specifies matching 6 Switch/1 Switch/Shuffle model. Shuffle has no half-speed extension. Retention and drums **?**. [Looper KB][HF-L], [Indexed Floor manual][HF-M0] 8snapshots;true preset spillover uses only 2 paths per current product. Mic processing supports vocal membership; intelligent vocal harmony is unverified. [FAQ][HF-Q], [Floor product][HF-P] |

### Helix Floor — separate IDR offers

| Class | Amount | Exact offer and qualifications |
|---|---:|---|
| Indexed hardware ask;condition unverified | **Rp30.609.000** | [W Musik Official Shop,shop37016589/item24212177775][HF-O1],JakartaUtara;retrieved 2026-10-17,cache last month. Earlier 4-month index **Rp28.999.000**,June 3 delivery, retained as an older observation. Condition,variant,bundle,warranty, checkout stock **?**;mall badge does not establish condition. Late-delivery voucher not deducted. |
| Historical hardware ask;condition unverified;**sold out** | **Rp19.850.000** | [SMOSYU MUSIC,shop397175630/item27006529188][HF-O2],Bekasi;retrieved 2026-10-17,cache last month,**Habis**. Condition/accessories/warrantyunknown;not a verified used price. |
| Verified used offer | **?** | Not established |
| Verified new offer | **?** | Sale condition not verified |
<!-- comparison evidence ends -->

### Helix Floor provenance and gaps

Own 3.80 manual URL returned **content too large,14,601,036bytes**;manual was not read or downloaded. Accessible original Rev A cheat sheet, Floor product page, manufacturer KB and older FAQ provide partial evidence. Indexed comparison PDF contains 96/268/32 claims; direct PDF failed, so indexed table evidence is explicit. Current 3.80 firmware index identifies November 19, 2024; this does not date all webpage figures. No LT specification fills missing Floor fields.

Manufacturer [timeline][HF-T] explicitly says Platinum is identical except finish. Its separate cached **Rp25.000.000** sold-out [MR.GUITAR INDONESIA,shop605621869/item47400474099][HF-O3],Depok,2-month index with August 12 delivery, is variant provenance, not another model or an authenticated new price. Full condition, bundle and warranty remain unknown.

Next:read accessible own manual text, verify complete power/ports, loop limits, factory-filled memory, firmware 3.80 category choices and current editor OS support. Preserve every historical price and variant distinction.

[HF-P]: https://line6.com/helix/helix-guitar-processor.html
[HF-S]: https://line6.com/data/6/0a0643391bb055fca90096a38/application/pdf/Helix%20Cheat%20Sheet%20-%20English%20(%20Rev%20A%20).pdf
[HF-K]: https://kb.line6.com/helix-lt-comparison
[HF-Q]: https://line6.com/support/topic/14264-helix-faq/
[HF-C]: https://line6.com/documents/processor_comparison_chart/Line_6_Processor_Comparison_Chart.pdf
[HF-T]: https://line6.com/timeline/
[HF-D]: https://line6.com/software/index.html?hardware=Helix&locale=en_US&name=Flash+Memory&os=All&submit_form=set
[HF-M]: https://line6.com/data/6/0a00051afda2673ccc1cc8e68/application/pdf/Helix%203.80%20Owner%27s%20Manual%20-%20English%20.pdf
[HF-O1]: https://shopee.co.id/Yamaha-LINE-6-HELIX-Floor-Yamaha-LINE-6-HELIX-LINE-6-HELIX-Floor-i.37016589.24212177775
[HF-O2]: https://shopee.co.id/Line-6-Helix-Floor-i.397175630.27006529188
[HF-O3]: https://shopee.co.id/Line-6-Helix-Floor-Platinum-Limitide-Edition-Helix-Effect-Guitar-Bass-i.605621869.47400474099

### Helix Floor looper audit — 2026-10-17

The original Floor manual at a separate 3.0-named URL was also too large for direct reading (14,238,658 bytes). Search-indexed manufacturer text establishes three looper models and matching-model restrictions; its filename says 3.0 while the indexed title says Rev F, so revision identity remains qualified. This is not a full manual review. The accessible manufacturer KB supplies loop times and older cross-preset conditions. Neither source establishes saved audio export or power-cycle retention.

[HF-L]: https://kb.line6.com/the-helix-looper
[HF-M0]: https://line6.com/data/6/0a00050b287e6643b71cda93a/application/pdf/Helix%203.0%20Owner%27s%20Manual%20-%20English%20.pdf

## Helix Stadium XL Floor

<!-- comparison evidence begins -->
Checked **2026-10-17** against selected pages of the live **Rev E / firmware1.4** online manual. Distinct from original Helix Floor and smaller Stadium Floor. Guitar, bass and live mic paths documented; partial verification.

| Required field | Finding |
|---|---|
| Built-in / external / toe expression | Built-in pedal with assignable toe switch, default EXP1/2 toggle. Up to4 external pedals through CONTROL A/B and C/D; these connections also serve switches, triggers or amp control, so maxima are alternatives rather than additional dedicated sockets. [Top panel][SX-T], [Rear panel][SX-R] |
| Knobs / footswitches / buttons | **11 /12 /13** from text inventory:8 parameter rotaries,Volume,Upper,Lower;3 output buttons,3 transport,Home,Song,Amp,Save,XY,2 Page. Encoder presses counted once;toe and rear power additional. [Top panel][SX-T] |
| Display | **8-inch color touchscreen**;12 OLED scribble strips on XL. Strip diagonal/color specification **?** [Display][SX-D], [Product][SX-P] |
| Dimensions / weight | **498 W × 257 D × 92 H mm; 5.25 kg**. Manufacturer also lists 19.4 W × 10.1 D × 3.6 H inches and 11.5 lb; rounded mixed units retained as published. [Support tips][SX-K] |
| Simultaneous blocks | Manual describes **46 processing positions in Super Serial template**; exact DSP/model limits remain separate. Do not assume46 heavy amps. Agoura amp models and HX-compatible effects; official list row counts: distortion **65**, delay **45**, reverb **25**, modulation **57**, dynamics **19**, EQ **5**, pitch/synth **29**, filter **15**, wah **11**, volume/pan **5**, looper **3**. These include Legacy rows and count each named mono/stereo entry once, not simultaneous blocks. Amp-table audit: **142 distinct name/subcategory entries** after removing one repeated Cali 2C+ row: guitar 24 Agoura + 66 Guitar + 28 Legacy; bass 6 Agoura + 11 Bass + 6 Legacy; 1 mic preamp. Same names across Agoura/Legacy remain separate. **46 cabinets: 38 guitar + 8 bass**; **12 mic choices per cab family**. These are derived table counts, not expanded channel options. [Model list][SX-ML], [Presets][SX-M], [Blocks][SX-B] |
| Factory / user memory | **512 initially empty user locations**, separate protected factory folder; factory-filled count/combined total **?**. Up to122 setlists with1–128 aliases each;aliases do not add independent preset storage. [Presets][SX-M] |
| Synth / acoustic simulation | **Acoustic Sim** appears under EQ. Pitch/Synth includes **3 OSC Synth**, legacy synth algorithms and **3 Note / 4 OSC Generators**; generators can sound without an instrument and default off. Native NAM is not established by these synth entries. [Model list][SX-ML] |
| IR / NAM / capture | **2,048 user IRs**, WAV import; processed as 2,048-sample, 48 kHz, 32-bit float mono. Each Cab block holds one or two cabs/IRs; one sums input to mono, two preserve stereo input/output. [Cab IRs][SX-I]. **Proxy** amp, amp+cab, preamp and distortion clones, introduced in firmware 1.3. Library **2,048 clones**; up to **4 per preset, 2 per main path**, subject to DSP. All clone blocks are mono and sum preceding stereo. Creation requires Internet access and a signed-in Line 6 account; native/converted NAM **?**. [Clones][SX-C], [Presets][SX-M] |
| Audio/control I/O | Two instrument inputs;XLR mic,+48V;4¼″ send/return loops;stereoXLR and¼″ mains;stereo phones;two sharedCONTROL jacks;DIN MIDI in/out-thru;RCA S/PDIF in/out;Nexus expansion;microSD;USB-A Ethernet adapter option;USB-C audio/editor;grounded IEC. Exact remaining connector wiring/sizes **?**. Sends impedance-balanced,returns unbalanced. [Rear panel][SX-R] |
| Power / battery / USB | Internal supply,grounded IEC;voltage/frequency/draw **?**,DC barrel polarity N/A. Battery/USB-powered operation **?** [Rear panel][SX-R], [Product][SX-P] |
| Editor platforms | **Helix Stadium application1.4**,macOS14+ orWindows11 64-bit;Wi-Fi/USB editing. Requires devicefirmware≥1.1;Showcase requires≥1.2 app/firmware. Drivers/updaters andStadiumNativeplugin are separate. Linux/mobile full editor **?**. Support tips still say USB editing is unavailable; the version 1.4 application manual explicitly supports it. [Application][SX-A], [Support tips][SX-K] |
| USB audio | **8-in/8-out,24-bit**. WindowsASIO supports44.1/48/88/96kHz (manual writes88,not88.2);macOS driverless native48kHz. Apple/Android class-compliant audio doesnot establish mobileeditor support. USB-C only;DI/reamp andMIDI. [USB audio][SX-U] |
| Looper / routing / live features | One Deluxe,1Switch orShuffle per preset. Deluxe/1Switch **120s mono/60s stereo fullspeed**,double at halfspeed;Shuffle60/30s,no halfspeed. Acrosspresets requires same model,mono/stereo andpath. Audio cleared atpoweroff. **8 snapshots per preset** recall bypass (except Looper), assigned parameters, commands and optional tempo, without rearranging blocks or replacing amp/effect models. Showcase automation/playback distinct from drum machine; drums **?**. [Snapshots][SX-S], [Loopers][SX-L] |
| Storage / practical restrictions | Rear manual says microSD soldseparately andrequired forShowcase/backups;QuickStart says cardpre-inserted andproduct says32GBremovable. Retain bundle/document conflict;actualIndonesianoffer inclusion **?**. [Rear panel][SX-R], [Quick Start][SX-Q], [Product][SX-P] |

### Stadium XL — separate IDR evidence

| Class | Amount | Exact hardware offer and qualifications |
|---|---:|---|
| Indexed hardware ask; sale condition unverified | **Rp41.220.000** | [ROCKPIZZ MUSIC,shop440477624/item53707848703][SX-O],Denpasar. ExactURL retrieved2026-10-17;cache3months old,delivery18July (olderlead said6July). Condition,variant,bundle,microSD,warranty andcheckoutstock **?**. Relative delivery andlate-deliveryvoucher up toRp10.000 do not prove live stock or reduce this ask. |
| Verified used offer | **?** | Not established |
| Verified new offer | **?** | Sale condition unverified |
<!-- comparison evidence ends -->

### Stadium XL provenance and next checks

Online manual landing identifies **Rev E,v1.4.0**,while navigation retains earlierrevision labels. These are dated documentation observations,not proof that listedhardware runs1.4. Only citedsections were read;no whole-manual review claimed. No downloads orsoftware execution. Remaining: power label, further routing restrictions, DSP limits and condition-qualified offers. OriginalFloor andStadiumFloor values do not fill XL gaps.

[SX-P]: https://line6.com/helix-stadium/?locale=en_UK
[SX-T]: https://manuals.line6.com/en/helix-stadium/live/top-panel-and-footswitches
[SX-R]: https://manuals.line6.com/en/helix-stadium/live/rear-panel
[SX-D]: https://manuals.line6.com/en/helix-stadium/live/display
[SX-M]: https://manuals.line6.com/en/helix-stadium/live/presets
[SX-B]: https://manuals.line6.com/en/helix-stadium/live/the-blocks
[SX-A]: https://manuals.line6.com/en/helix-stadium/live/helix-stadium-edit-application
[SX-U]: https://manuals.line6.com/en/helix-stadium/live/usb-audio
[SX-L]: https://manuals.line6.com/en/helix-stadium/live/looper-block
[SX-Q]: https://manuals.line6.com/en/helix-stadium/live/quick-start
[SX-O]: https://shopee.co.id/LINE-6-HELIX-STADIUM-XL-FLOOR-LINE-6-HELIX-STADIUM-XL-FLOOR-i.440477624.53707848703

### Proxy cloning and support qualifications

Clones capture the device at its chosen settings. The manual recommends excluding compression, modulation and time effects from capture. Direct amp capture needs a load box; preamp capture needs a suitable preamp output or FX send. Monitoring cab processing is excluded from direct amp/preamp capture. The desktop app manages clones but does not create them and is locked during capture. [Clones][SX-C]

The support tips page says empty user presets do not send automatic MIDI program changes until saved and named. It also says L6 LINK awaits Expand D10 release; this is a dated support statement, not independently verified present availability. Its USB-editing restriction conflicts with the explicitly versioned 1.4 application chapter. [Support tips][SX-K], [Application][SX-A]

[SX-K]: https://kb.line6.com/helix-stadium-tips-and-tricks
[SX-C]: https://manuals.line6.com/en/helix-stadium/live/clones

### Cab IR and snapshot restrictions

IR file selection can be stored per snapshot when the Cab IR browser’s Snapshot Control option is enabled (off by default). This does not establish snapshot replacement of amp/effect models. Deleting an IR used by a preset leaves its tab UNRESOLVED. Large IR imports can lengthen the next startup while indexing. Older pre-3.50 Helix/HX Hybrid Cabs are converted on import and can sound different. [Cab IRs][SX-I]

Snapshot edits are retained during snapshot changes by default; enabling Discard Edits restores saved values instead. Save before changing snapshots to retain such edits. Delay, reverb and FX-loop Trails must be enabled for the documented snapshot spillover. Snapshot bypass changes can alter how a shared stomp assignment toggles multiple blocks. [Snapshots][SX-S]

[SX-I]: https://manuals.line6.com/en/helix-stadium/live/cab-blocks
[SX-S]: https://manuals.line6.com/en/helix-stadium/live/snapshots

### Model inventory counting basis

The official current list includes models introduced through version 1.4. Counts above are derived from named rows within each effect table, including Legacy entries, without doubling rows marked Mono, Stereo. They are not a manufacturer headline total, a count of simultaneously available blocks or confirmation of an offer’s installed firmware. The amp table repeats Cali 2C+, so its raw row total must not be treated as unique amp count. Polyphonic pitch models are marked as DSP-intensive. [Model list][SX-ML]

[SX-ML]: https://line6.com/helix-stadium-models/

The amp table contains 143 rows before removing the identical Cali 2C+ entry. Channel/input options within a row are not expanded; Brit SL100 groups several years. This counting method preserves generation distinctions rather than claiming 142 unique names. [Model list][SX-ML]

## POD HD500X

<!-- comparison evidence begins -->
Checked **2026-10-17**; distinct from original HD500. Selected sections of own Advanced Guide Rev A (firmware 1.01+) and Pilot’s Guide Rev C; partial verification.

| Required field | Finding |
|---|---|
| Built-in / external / toe expression | Built-in EXP1/2 with toe switch; one external Pedal 2 permits simultaneous EXP1/2. [Pilot][H5X-P] |
| Knobs / footswitches / buttons | **12 front rotaries / 12 footswitches / 8 front button directions**: Presets, four multifunction, Drive, four tone, Volume, Master; FS1–8, Bank up/down, Tap, Looper; Save, View, Move, Enter, four navigation directions. Encoder press counted once; toe, rear Mic Level rotary and slide switches additional. [Pilot][H5X-P] |
| Display | LCD; published diagonal, color and touch specification **?** [Pilot][H5X-P] |
| Dimensions / weight | **?** — old manufacturer dimensions URL redirects; sibling dimensions not substituted |
| Simultaneous blocks | **8 FX slots + up to 2 amps**, subject to dynamic DSP; FX Loop consumes an FX slot. Pre/post and parallel A/B routing. [Advanced][H5X-A] |
| Categories / choices | Family FAQ lists dynamics8, distortion15, modulation22, filter17, pitch3, EQ5, delay19, reverb12, wah8, Volume/Pan; firmware2.62 lists22 full guitar amps +22 preamps. Family/firmware wording retained; installed HD500X inventory and later packs require reconciliation. [FAQ][H5X-F] |
| Factory / user memory | **512 writable locations**, 8 setlists ×64; factory-filled count **?**. [Advanced][H5X-A], [Pilot][H5X-P] |
| Synth / acoustic simulation | Synth O Matic, Attack Synth and Synth String documented; acoustic simulation **?**. Bass Flip Top amp/cab explicitly recommended. [Advanced][H5X-A] |
| IR / NAM / capture | Native NAM, converted NAM, user IR import and capture **?**; factory cab modeling does not prove import |
| Audio/control I/O | Guitar and mono AUX; CD/MP3; Mic with rear level; stereo quarter-inch unbalanced and XLR balanced outs; phones; stereo TRS send and L/R returns; Pedal2; Variax guitar/bass interface; S/PDIF out; MIDI in/out-thru; USB; L6 LINK. Remaining connector sizes and phantom **?**. [Pilot][H5X-P] |
| Power / battery / USB | Rear drawing **9V DC, 2.5A minimum**; actual draw, polarity/barrel, battery and USB-powered operation **?**. [Advanced][H5X-A] |
| Editor platforms | **POD HD500X Edit**, Mac/Windows USB editor/librarian; current OS versions **?**. USB driver and Monkey updater separate. [Advanced][H5X-A] |
| USB audio | Processed stereo record send, playback/monitor mix,24-bit; native48kHz with44.1/88.2/96 conversion. **USB audio muted during DT25/DT50 L6 LINK connection**. [Advanced][H5X-A] |
| Looper / routing / live features | Mono **24s full /48s half speed**, PRE/POST, overdub/undo/reverse. Trails do not spill across presets. Mic-source Vintage Pre documented; harmony features not inferred. Drums and loop retention **?**. [Advanced][H5X-A], [Pilot][H5X-P] |

### HD500X — separate IDR evidence

| Class | Amount | Exact hardware offer and qualifications |
|---|---:|---|
| Used-title hardware ask | **Rp6.200.000** | [alvienz37,56303985/2253537586][H5X-O1],Cilegon; title explicitly second. Opened2026-10-17,cache last month,delivery8–11September versus initial3month search4–6July. Physical condition,completeness,warranty and live stock **?**; voucher not deducted. |
| Sold-out hardware ask; sale condition unverified | **Rp4.100.000** | [Aliska_Musik,267406637/21071872133][H5X-O2],Jakarta Pusat; **Habis**,cache last month,delivery26August; bundle/warranty **?**. Not live stock. |
| Sold-out hardware ask; sale condition unverified | **Rp4.250.000** | [Ayx Music,58780289/18911697683][H5X-O3],Lamongan; **Habis**,search cache3months. Title mulus +HC suggests cosmetic condition/hardcase,not verified inclusion or sale condition. |
| Verified new offer | **?** | Not established |
<!-- comparison evidence ends -->

### HD500X provenance and next checks

No full-manual or installed-firmware audit claimed. FAQ power, dimensions and phantom statements explicitly name older HD500/Bean; they do not fill X gaps. A reused Shopee URL naming Zoom707II now indexes HD500X and failed exact opening; excluded from prices. Mixed HD300/400/500/500X listing and case-only listing likewise excluded; exact URLs and observations retained in research-state.json. No downloads or software execution. Remaining: physical/power details, firmware-specific category totals, current editor OS, IR/NAM/capture evidence, display, loop persistence and offers.

[H5X-A]: https://l6c-acdn2.line6.net/data/6/0a06434c6fb051e03e8ab63dc/application/pdf/POD%20HD500X%20Advanced%20Guide%20%28%20Rev%20A%20%29.pdf
[H5X-P]: https://line6.com/data/6/0a06434cb30151dddd9ae9314/application/pdf/POD%20HD500X%20Quick%20Start%20Guide%20-%20English%20%28%20Rev%20C%20%29.pdf
[H5X-F]: https://kb.line6.com/pod-hd500x-hd500-pod-hd-pod-hd-pro-faq
[H5X-O1]: https://shopee.co.id/effect-gitar-LINE-6-POD-HD500X-second-i.56303985.2253537586
[H5X-O2]: https://shopee.co.id/Line-6-pod-hd500x-i.267406637.21071872133
[H5X-O3]: https://shopee.co.id/pod-Hd500X-mulus-HC-line6-pod-hd-i.58780289.18911697683

## AMPLIFi FX100

<!-- comparison evidence begins -->
Checked **2026-10-17**. Guitar floor processor, distinct from AMPLIFi speaker amps and Flamma FX100. Own Rev D guide and manufacturer support; partial verification.

| Required field | Finding |
|---|---|
| Built-in / external / toe expression | Built-in pedal, toe toggles Volume/Wah; external expression socket not listed in own rear-panel inventory, further controller options **?**. [Guide][AF-M] |
| Knobs / footswitches / buttons | **7 / 4 / 2**: six tone rotaries + Master; A–D footswitches; Bluetooth and Tap buttons. Master press counted once; toe and rear power rocker additional. [Guide][AF-M] |
| Display | Numeric bank/tuner indicator and LED rings; diagonal, color/touch specifications **?**. [Guide][AF-M] |
| Dimensions / weight | FAQ **17¾ W × 9¼ D × 3 H inches; 7 lb 6 oz** (translated FAQ 3.3 kg). Rev D instead prints **641 × 330 × 153 mm, 3.40 kg**, axes unstated. Material dimensions conflict retained; do not silently treat as unit/packaging conversion. [FAQ][AF-F], [Guide][AF-M] |
| Simultaneous blocks | **8 simultaneous effects** advertised; 70+ amps, 100+ effects, 20+ cabs. The model descriptions list **8 wah choices**; other per-category counts and whether amp/cab count toward 8 **?**. [FAQ][AF-F] |
| Factory / user memory | **100 onboard locations**, 25 banks × 4, saveable; factory-filled count **?**. Cloud/library capacity separate. [FAQ][AF-F], [Guide][AF-M] |
| Synth / acoustic simulation | Manufacturer model descriptions include **Seismik Synth** (8 wave choices), **Double Bass** (two pitch-tracking oscillators), Synth Analog, Synth Harmony, Synth Lead and Synth String. Acoustic simulation **?**. Tube Instrument Preamp explicitly supports bass/piezo; piezo/Variax-acoustic voicing is not proof of electric-to-acoustic simulation. [Model descriptions][AF-C] |
| IR / NAM / capture | User IR, native/converted NAM and capture **?**; factory cab models alone do not prove import |
| Audio/control I/O | Quarter-inch guitar, stereo phones, L/R main outs and mono Amp Out; USB; 9V DC input and power rocker. FAQ calls main outs balanced. [Guide][AF-M], [FAQ][AF-F] |
| Power / battery / USB | **Line 6 9V DC supply** specified; polarity, barrel, current/draw, battery and USB power **?**. [Guide][AF-M] |
| Editor platforms | **AMPLIFi Remote iOS/Android** Bluetooth editor. Old requirements differ: FAQ iOS 7+, Rev D iOS 9+/Android 4.2+. No ongoing development; manufacturer reports Android 11/12/13 malfunction. From 2023-11-01 new Android users above 4.4 cannot see it in Play Store; official legacy APK is provided as-is, modern compatibility unguaranteed. Support expired 2023-12-01. Current iOS compatibility and desktop editor **?**; desktop Bluetooth audio/updaters are separate. [Guide][AF-M], [FAQ][AF-F], [Development][AF-D], [Availability][AF-A] |
| USB audio | Later guide confirms stereo in/out. Firmware 2.10 added recording: Mac/iPad class-compliant 24-bit/48 kHz; Windows ASIO 16/24-bit 44.1/48/88.2/96 kHz with conversion. Historical Windows 7/8 and OS X 10.7+ support is not current-OS verification. Old FX100 FAQ says USB unused; superseded by later guide/release evidence. [Guide][AF-M], [Firmware][AF-U] |
| Looper / routing / live features | **Amp Out excludes Bluetooth and removes guitar from Main Outs when connected**. Hardware preset saving disabled while Remote app connected. The app’s Advanced Routing directs music to another playback device while retaining tone control; this is not evidence of parallel guitar DSP paths. Tap/tuner; looper, drums, scenes **?**. [Guide][AF-M], [Routing][AF-R] |
| Practical restrictions | Firmware 2.50.2 requires Remote ≥2.13; updater/Windows driver separate. Bluetooth 2.1/SBC; app sync is distinct from pairing. Manufacturing ended 2021-12-01; old inventory does not imply current support. [Firmware][AF-U], [FAQ][AF-F], [End of life][AF-E] |

### AMPLIFi FX100 — separate IDR evidence

| Class | Amount | Exact hardware offer and qualifications |
|---|---:|---|
| Indexed hardware ask; sale condition unverified | **Rp2.999.000** | [Tempo Music,18437660/186076637][AF-O],Jakarta Barat. Exact page opened 2026-10-17; cache 2 months, delivery 19–22 August, seller activity 4 years versus initial 5-month search/activity 3 years/service unavailable. Title names FX100 but category amplifier/mixer; actual unit, bundle, warranty and checkout stock unverified. Late delivery voucher not deducted. |
| Verified used offer | **?** | Sale condition unverified |
| Verified new offer | **?** | Sale condition unverified |
<!-- comparison evidence ends -->

### FX100 provenance and remaining checks

The FX100-specific FAQ incorrectly describes a five-speaker design in a streaming answer; that belongs to speaker-equipped products and does not establish FX100 speakers. Preserve its older USB claim as historical, not current functionality. Own guide is Rev D/2016; selected support pages were read without downloading software or files. The alternative CDN guide URL failed; the official English URL rendered as 8-page PDF text. No visual measurement or hardware test. Remaining: reconciled dimensions, full model category inventory, draw/polarity, external control, display and app compatibility, IR/NAM/capture and sale-condition-qualified offers.

[AF-M]: https://line6.com/data/6/0a020a4132f0612713c723f4f/application/pdf/AMPLIFi%20FX100%20Pilot%27s%20Guide%20-%20English%20.pdf?locale=en_UK
[AF-F]: https://kb.line6.com/amplifi-fx100-faq
[AF-C]: https://kb.line6.com/full-list-of-amplifi-firehawk-series-amps-effects-and-cabs
[AF-D]: https://kb.line6.com/amplifi-development
[AF-A]: https://kb.line6.com/amplifi-and-firehawk-android-app-availability
[AF-U]: https://kb.line6.com/amplifi-firmware-update-release-notes
[AF-E]: https://kb.line6.com/amplifi-series-end-of-life
[AF-O]: https://shopee.co.id/YAMAHA-LINE6-LINE-6-Ampli-Gitar-Amplifi-FX100-AmplifiFX100-i.18437660.186076637

[AF-R]: https://kb.line6.com/amplifi-remote-advanced-routing-feature

## POD X3 Live

Checked **2026-10-17**; partial. Floor processor, distinct from desktop X3, rack X3 Pro and XT Live. Model-specific [product documentation][X3L-P] establishes guitar, bass and vocal modeling; all three instrument comparisons include this single canonical record.

<!-- comparison evidence begins -->

| Required field | Finding / qualification |
|---|---|
| Built-in / external / toe expression | Integrated pedal with toe switch; Pedal 2 supports EX-1 expression, with volume/tweak assignments. [Manual][X3L-M], pp3•12,6•5–6 |
| Rotary / footswitches / buttons | **14 / 12 / 8** from text inventory: 13 top rotaries plus mic trim; 12 floor switches; Home, Inputs, On/Off, Outputs and four navigation directions. Select encoder push, toe switch, power/ground/pad/level toggles additional. Visual corroboration pending. [Manual][X3L-M], pp3•8–15 |
| Display | Backlit LCD documented; diagonal, color mode, resolution and touch unverified. [Product][X3L-P] |
| Dimensions / weight | **21.5 in length × 10 in width/depth × 4.75 in height; 8.40 lb**. Preserve manufacturer axes; metric W×D×H and accessory inclusion unverified. [Specifications FAQ][X3L-S] |
| Simultaneous processing | Two independent Tone paths. [Manual][X3L-M], p4•4. Manufacturer history advertises up to **2 amps / 18 effects**; this is not 98 simultaneous effects or proof of arbitrary block allocation. [History][X3L-H] |
| Categories / model choices | Product: **78 guitar amps,24 guitar cabs,28 bass amps,22 bass cabs,6 vocal preamps,98 effects**, four microphone choices. [Product][X3L-P]. KB list: **8 wah,33 stomp,24 modulation,14 delay,14 reverb** entries; delay numbering repeats6. These subtotal93, so reconciliation with98 and firmware additions remains incomplete. No Amp/No Cabinet entries excluded from advertised amp/cab counts. [Model list][X3L-L] |
| Factory / user / total presets | **128 writable User locations**; listed other folders total250, giving378 displayed locations by arithmetic. Manual says over350; factory-filled User count unverified. Each preset stores both Tones. [Manual][X3L-M], p4•7 |
| Synth / acoustic simulation | Synth algorithms listed: Seismik Synth,Rez Synth,Synth Analog,FX,Harmony,Lead,String. Acoustic-named amp choices include Piezacoustic2/Variax Acoustic; dedicated acoustic-simulator behavior remains unverified. [Model list][X3L-L] |
| IR / NAM / capture | Factory cabinet/mic modeling established; user IR import, native NAM, converted NAM and proprietary capture loading each unverified. |
| Audio / control I/O | Quarter-inch guitar, auxiliary input, L/R Live outputs, stereo phones, mono send/stereo return, Pedal2; XLR mic/trim and L/R Direct outputs; eighth-inch stereo CD/MP3 input; Variax digital; MIDI In/Out-Thru; S/PDIF out; USB2. [Product][X3L-P]; [Manual][X3L-M], pp3•12–15. Live outputs unbalanced, Direct XLR balanced; do not borrow desktop balanced TRS outputs. |
| Power / battery / USB | **PX-2 supplied adapter** named in Live section. [Manual][X3L-M], p3•15. Exact voltage/current, AC/DC, polarity/barrel, measured draw, battery and USB power operation unverified in this pass; no sibling or seller-adapter rating substituted. |
| Editor / platforms / drivers | **GearBox** is the hardware editor; Monkey handles firmware/bundle utilities. POD Farm is a plug-in for X3, not its standalone hardware editor. Historical Windows/Mac GearBox documentation. Manufacturer lists **POD X3 audio drivers, editors, updaters, Control Panel and License Manager as not receiving Apple Silicon support**. Monkey is discontinued for newer OS releases, including Windows 11, Catalina and Monterey; its firmware-installation route requires an older supported OS. Exact supported Windows/Intel Mac versions and mobile editing remain unverified. These notices do not prove every legacy setup fails or that current activation works. [Silicon notice][X3L-SIL]; [Monkey notice][X3L-MON]. [GearBox FAQ][X3L-G]; [POD Farm FAQ][X3L-F]; [GearBox3.6 guide][X3L-GM] |
| USB audio | Eight device-to-computer channels: stereo main, stereo Tone1,Tone2, two raw input sums. Windows ASIO/Mac Core Audio documented; return-channel count, current drivers and rates unverified. [Manual][X3L-M], pp8•2–3 |
| Live / vocal functions | Tap/tuner; separate amp/direct routing. **No phantom power** per model-specific FAQ. [Applications][X3L-A]. Hardware looper, drums, scenes, persistence and spillover unverified; FX loop is not a phrase looper. |
| Used IDR | **?** Exact sold-out ask below lacks sale-condition evidence. |
| New IDR | **?** No exact condition-verified new offer established. |

<!-- comparison evidence ends -->

### Exact Shopee evidence

Checked **2026-10-17**: [GIDEON MUSIC, shop726736590/item25319569969](https://shopee.co.id/Efek-Gitar-Line-6-POD-X3-Live-i.726736590.25319569969), Kota Medan, **Rp1,850,000; indexed Habis**. Three-month cached exact title; July10–13 delivery stale; direct retrieval failed. Sale/working condition, selected variation, adapter/bundle, warranty, shipping/tax, current stock and final total unknown. Not a used/new market range or completed sale; late Rp10,000 compensation is not deducted.

Blitza Music shop recommendation at Rp2,000,000 is unresolved as an exact item; Hope Music mixed X3 Live/XT Live/Floor POD ask is not assigned to X3 Live. Gigbag and potentiometer prices are rejected. Exact discovery provenance and subsequent XT Live/HD400 leads remain in research-state.json.

### Document identity and remaining work

Primary family Advanced Guide **Rev E,40-00-0120**,100 PDF pages; only Live-specific panels and expressly shared family functions used. Desktop/rack differences stay separate. Selected technical sections read, not a complete manual audit. Current product is discontinued. Category figures reflect the cited list/product, not verified installed firmware. Manufacturer v2.0 update notes identify additional effects; full version reconciliation remains open. No files, dependencies, firmware or editor downloaded or executed.

Remaining: physical panel image count; exact power label; all category/fixed-block totals and firmware; factory-filled User memory; synth/acoustic details; IR/NAM/capture; current editor/driver platforms, USB rates/return channels; screen specification; looper/live restrictions and qualified prices.

[X3L-P]: https://line6.com/legacy/podx3live?locale=en_US
[X3L-M]: https://line6.com/data/l/0a060072a53c4aae7fe287ecf/application/pdf/POD_X3_Advanced_Guide.pdf
[X3L-S]: https://kb.line6.com/pod-x3-series-specifications-and-general-faqs
[X3L-L]: https://kb.line6.com/pod-x3-series-models-list
[X3L-H]: https://origin2.line6.com/timeline/
[X3L-A]: https://kb.line6.com/pod-x3-live-applications-f-a-q
[X3L-G]: https://kb.line6.com/getting-started-with-gearbox-amp-effect-modeling-software
[X3L-F]: https://kb.line6.com/pod-farm-1-faq
[X3L-GM]: https://line6.com/data/6/0a060b316ac34f0593cdec813/application/pdf/GearBox%203.6%20User%20Manual%20-%20English%20%28%20Rev%20F%20%29.pdf
[X3L-FW]: https://line6.com/support/page/kb/legacy-products/pod/pod-x3/pod-x3-product-family-firmware-version-20-update-instructions-and-general-information-r273/

[X3L-SIL]: https://kb.line6.com/macos-11-big-sur-silicon-m1-chip-compatibility
[X3L-MON]: https://kb.line6.com/line-6-monkey-discontinued

## POD XT Live

Checked **2026-10-17**; partial. Manufacturer styles the name PODxt Live. Guitar floor processor, distinct from Bass PODxt Live, desktop PODxt, rack PODxt Pro and POD X3 Live. Included in guitar and **conditional bass** comparisons: the optional authorized Bass Expansion pack is documented for this hardware; its presence in a particular used unit is unknown. No vocal membership established.

<!-- comparison evidence begins -->

| Required field | Finding / qualification |
|---|---|
| Built-in / external / toe expression | Integrated wah/volume/tweak pedal and toe switch; external EX-1 Pedal2 for volume/tweak. [Manual v3][XTL-M], pp2•3,2•9,4•9 |
| Rotary / footswitches / buttons | **9 / 11 / 7** from text inventory:8 top rotaries plus rear Output Level; Bank2,A–D4,Amp/Stomp/Mod/Delay4,Tap1; Save/Edit/System3 and4 soft buttons. Power,pad,amp/line toggles and toe switch additional. Image corroboration pending. [Manual v3][XTL-M], chapter2 |
| Display | Backlit LCD plus bank/channel display; diagonal,color mode,touch and resolution unverified. [Product][XTL-P]; [Manual v3][XTL-M], p2•4 |
| Dimensions / weight | **? / ?** Manufacturer dimensions page offers downloadable spreadsheets rather than inline unit values; files not downloaded under the task constraint. X3 Live and gigbag dimensions not substituted. [Dimensions index][XTL-D] |
| Simultaneous processing / routing | Named processing includes amp/cab,comp,gate,EQ,stomp,mod,delay,reverb,wah,volume; category names are not freely allocatable slots. Maximum simultaneous audio effects remains unverified; no X3 dual-tone claim. [Manual v3][XTL-M], chapters4–6 |
| Categories / choices | Product advertises **42 amps,24 cabinets,4 microphones,95 effects**. Optional licenses and installed firmware change available choices; complete category reconciliation remains open. [Product][XTL-P]. FX Junkie is included in the Live model set according to manufacturer FAQ. [Model Pack FAQ][XTL-FX] |
| Bass capability / license condition | **Optional Bass Expansion:28 bass amps,22 bass cabinets**; manufacturer shop cache explicitly lists PODxt Live as compatible. License and models installed in a seller unit unverified. Reopened shop redirects to homepage, so current sale/activation availability unverified; historical USD software ask is not hardware IDR evidence. [Expansion listing][XTL-B]; [Pack guide][XTL-BM], chapter5 |
| Factory / user / total presets | **128 writable Channel Memories**,32×4. RevB quick start describes banks1–16 factory/17–32 free; RevC controls describe1–20 factory/21–32 free. RevC also says36 banks and elsewhere16 during save. Preserve conflict; exact factory-filled slots/installed revision unverified. [RevB][XTL-OLD], p1•1; [v3][XTL-M], pp2•3–8 |
| Synth / acoustic simulation | Synth algorithms in included FX Junkie model set; exact pack/category audit pending. Acoustic-named Piezacoustic2/Variax Acoustic choices documented; dedicated acoustic-simulator behavior unverified. [Product][XTL-P]; [Model Pack FAQ][XTL-FX] |
| IR / NAM / capture | Factory cab/mic modeling documented; user IR,native NAM,converted NAM and proprietary capture loading each unverified. |
| Audio / control I/O | Quarter-inch mono instrument input and unbalanced L/Mono,R outputs; phones; auxiliary input; Variax digital; MIDI In/Out; USB; Pedal2; power input. Aux signal excluded from USB recording. Aux/phones exact connector sizes and USB rates/channel count remain unverified. [Manual v3][XTL-M], pp2•1–3 |
| Power / battery / USB | **Included PX-2** specified by own manual; manufacturer separately identifies named PX-2 as AC supply. Exact voltage/current,barrel,measured draw,battery/USB operation unverified in this pass. DC polarity not assigned to an AC supply. [Manual v3][XTL-M], p2•1; [PX-2 identity][XTL-PWR] |
| Editor / platforms / drivers | Product documents historical **Line6 Edit on Mac/PC** and GuitarPort. Later **GearBox** is the XT hardware editor; Monkey handles firmware/bundle utilities. POD Farm plug-in is not standalone XT editing. Manufacturer lists **POD XT audio drivers,editors,updaters,Control Panel and License Manager as not receiving Apple Silicon support**. Monkey is discontinued for newer OS releases,including Windows11,Catalina and Monterey; manufacturer says firmware installation requires an older supported OS. This does not establish failure on every Intel Mac or prove a working license-activation route. Other current OS/mobile support remains unverified. [Silicon notice][XTL-S]; [Monkey notice][XTL-MON] [Product][XTL-P]; [GearBox][XTL-G]; [POD Farm][XTL-F] |
| Live / practical features | Tap/tuner,Manual Mode,amp/line destinations; headphone insertion overrides destination with Studio mode. Looper,drums,scenes,persistence and spillover unverified. [RevB][XTL-OLD], pp1•1,2•2–3. Manufacturer FAQ acknowledges obsolete output-mode terminology in manual. [FAQ][XTL-Q] |
| Used IDR | **?** Saved sold-out hardware ask lacks sale-condition evidence. |
| New IDR | **?** No condition-verified new hardware offer established. |

<!-- comparison evidence ends -->

### Exact Shopee hardware evidence

Checked **2026-10-17**: [Ayx Music,shop58780289/item21810633258](https://shopee.co.id/line6-Pod-Xt-live-pod-xt-not-x3-i.58780289.21810633258), Kabupaten Lamongan: **Rp2,500,000; indexed Habis**. Exact title names XT Live and expressly says not X3. Three-month search cache,July19–21 delivery stale; direct retrieval failed. Sale/working condition,actual model-pack authorization,selected variation,adapter/bundle,warranty,shipping/tax,current stock and final total unknown. Not a completed sale or qualified used/new range; late-delivery Rp10,000 compensation not deducted.

The separate Rp1,900,000 preorder candidate has an XT Live title but a Zoom G3X URL slug; it remains unassigned. Hope Music's mixed X3/XT/Floor POD ask is not assigned to this variant. Adapter and potentiometer offers are rejected as processor prices. Discovery details remain in research-state.json.

### Primary-document revisions and gaps

Own **v3 RevC** manual,146 PDF pages, follows the exact link on manufacturer legacy page. Older **RevB** manual,144 pages,retained for differing wording. Selected sections read; no claim of a complete manual/algorithm audit. The v3 pedal-assignment page mentions an FBV Shortboard even though this floor unit has its own Pedal2; own connector/control text establishes external expression,while that wording remains a copy/revision issue. Discontinued product. No software,dependencies,firmware or files downloaded or executed.

The Bass Expansion source is the manufacturer's eight-month shop cache,corroborated by its Model Packs RevD guide and published compatibility email. Current shop reopening redirects to the homepage. This establishes documented optional hardware capability,not a working present-day purchase/activation route or a licensed seller bundle. Base guitar and separately sold Bass PODxt Live must not be conflated.

Remaining: power label/dimensions/weight,control image,precise simultaneous effects and category totals,current licenses/firmware,factory memory fill,synth/acoustic details,IR/NAM/capture,current editor/audio support,display and qualified prices.

[XTL-P]: https://cdn.line6.com/legacy/podxtlive
[XTL-M]: https://l6c-acdn2.line6.net/data/6/0a060b316ac34f0593d2ca219/application/pdf/PODxt%20Live%20Manual%20-%20Version%203%20%28%20Rev%20C%20%29.pdf
[XTL-OLD]: https://line6.com/data/6/0a060b316ac34f0593d168408/application/pdf/PODxt%20Live%20-%20English%20.pdf
[XTL-B]: https://shop-us.line6.com/standard-model-packs/bass-expansion-pack/
[XTL-BM]: https://l6c-acdn2.line6.net/data/6/0a0643391683555d3aa9aab48b/application/pdf/Model%20Packs%20Pilot%27s%20Guide%20%28%20Rev%20D%20%29.pdf
[XTL-BC]: https://line6.com/media/email/marketing/goldFAQ/mailer.html
[XTL-FX]: https://kb.line6.com/gearbox-model-pack-faq
[XTL-Q]: https://kb.line6.com/podxt-series-faqs
[XTL-PWR]: https://kb.line6.com/line-6-four-button-stompbox-pedal-faqs
[XTL-G]: https://kb.line6.com/getting-started-with-gearbox-amp-effect-modeling-software
[XTL-F]: https://kb.line6.com/pod-farm-1-faq

[XTL-S]: https://kb.line6.com/macos-11-big-sur-silicon-m1-chip-compatibility
[XTL-MON]: https://kb.line6.com/line-6-monkey-discontinued
[XTL-D]: https://kb.line6.com/line-6-product-weights-and-dimensions

## POD HD400

Checked **2026-10-17**; partial. Discontinued floor multi-effects, distinct from HD300, HD500 and HD500X. Guitar and bass membership: its own Flash 2.0 guide documents the Flip Top bass amp/cab. No vocal membership established.

<!-- comparison evidence begins -->

| Required field | Finding / qualification |
|---|---|
| Built-in / external / toe expression | Built-in toe-switched expression; external Pedal2, including EX-1. Wah/volume/Pitch Glide assignments. [Guide][HD4-M], pp2•4,6•8 |
| Rotary / footswitches / buttons | **12 / 9 / 6**, derived from handbook inventory:11 top rotaries plus rear Master; A–D,Mode,Loop,Tap,Bank up/down; FX Only,Save,four navigation directions. Encoder push,toe,rear toggles additional. Image corroboration pending. [Handbook][HD4-Q] |
| Display | Main LCD and bank display; diagonal,color,touch,resolution unverified. [Handbook][HD4-Q] |
| Dimensions / weight | **? / ?** Primary unit measurements pending; no case or sibling dimensions substituted. |
| Simultaneous processing / routing | FX1/2/3 plus separate reverb,gate,wah,volume and amp/cab; pre/post routing. Total simultaneous maximum unverified. Global FX Only bypasses amp/cab/mic. [Guide][HD4-M], chapters2,4–6 |
| Categories / choices | Derived Flash2.0 table counts: **48 FX1** (21 Gain,17 Various,10 under Pitch), **18 FX2** (9 Mod,5 Filter,4 Trem), **19 FX3** (10 Delay,5 Tape,4 Sweep), **9 reverb,8 wah**. Names group heterogeneous algorithms; do not add into a simultaneous-block count. Amp table:16 knob-accessed plus14 edit-only entries = **30**, including Flip Top; **17 cabinets** excluding None;8 guitar/5 bass mic choices. Revision-qualified, not installed-firmware proof. [Guide][HD4-M], pp5•4,5•8–11,6•1–18 |
| Historical count conflict | Manufacturer FAQ advertises16 amps and90 HD400 effects; older FAQ totals are not substituted for Flash2.0 tables. Full library reconciliation open. [FAQ][HD4-F] |
| Factory / user / total presets | **128 overwriteable slots**,32×4; handbook says minimum128 factory presets. Factory and user are not additive capacities. [Guide][HD4-M], chapter3; [Handbook][HD4-Q] |
| Synth / acoustic simulation | Attack Synth,Synth String,Growler,Synth-O-Matic documented. Dedicated acoustic simulator unverified. [Guide][HD4-M], p6•3 |
| IR / NAM / capture | Factory cab modeling established; user IR,native NAM,converted NAM and proprietary capture loading individually unverified. |
| Audio / control I/O | Guitar in; CD/MP3 in; unbalanced quarter-inch L/Mono,R; balanced XLR L,R with ground lift; phones; stereo send/return pairs; Pedal2; USB; L6 LINK; power. L6 LINK is proprietary audio/control, not microphone input. [Handbook][HD4-Q] |
| USB / audio restrictions | Stereo record/playback,24-bit,native48k with rate conversion. **Active L6 LINK mutes USB audio.** MIDI SysEx backup documented; general CC support unverified. [Guide][HD4-M], chapters8,B |
| Power / battery / USB | Rear label **9 V DC,2.5 A minimum**; supply capacity is not measured draw. Unplug to turn off. Polarity,barrel,battery and USB-powered operation unverified. [Handbook][HD4-Q] |
| Editor / platforms / drivers | **POD HD400 Edit v2.0**, historical Windows/Mac editor/librarian; Monkey updater separate. Current Windows/Intel Mac versions unverified. Manufacturer lists **HD300/400 as not receiving Apple Silicon support**. [Edit guide][HD4-E]; [Compatibility][HD4-C] |
| Looper / practical features | **24-second mono looper**,overdubs,pre/post. Stereo effects loop,Line/Stomp levels; empty enabled loop can mute signal. Drums,scenes,spillover unverified. [Guide][HD4-M], chapters2,7 |
| Output modes | Live/Studio/Dual; Dual sends live to unbalanced and studio to balanced outputs, not two independent amp chains. [Handbook][HD4-Q] |
| Used IDR | **?** Saved sold-out hardware ask lacks sale-condition evidence. |
| New IDR | **?** No condition-qualified new offer established. |

<!-- comparison evidence ends -->

### Exact Shopee evidence

Checked **2026-10-17**: [SadewaMusikAudio,shop171167271/item21985664004](https://shopee.co.id/LINE-6-POD-HD-400-EFEK-DIGITAL-HD400-EFX-MULTIEFEK-KOLEGA-XT-X3-LIVE-HD500-300-HD300-i.171167271.21985664004), Kabupaten Bantul: **Rp2,200,000; indexed Habis**. Two-week index; October2–3 delivery stale; direct retrieval cache miss. Sale/working condition,selected variant,adapter/bundle,warranty,current stock,shipping/tax,voucher and final total unknown. Late-delivery compensation is not a discount. Related XT/X3/HD500/HD300 title keywords are not variants or additional offers. Not a completed sale or qualified used/new range.

### Source identity and remaining verification

Manufacturer legacy page links its own HD400 handbook,Edit guide and shared HD300/400 Advanced Guide. The Advanced Guide is RevA,©2012,for Flash2.0 or later and explicitly applies to both models except marked differences. Derived table counts include HD400-only starred entries; do not assign them to HD300. The handbook mirror reproduces manufacturer document40-00-0242 RevC; original CDN retrieval failed. Mirror-generated FAQ content is not evidence. Selected text sections inspected; no complete manual or visual-panel audit claimed. No files,software,firmware or dependencies downloaded or executed.

Remaining: verify body/polarity/barrel/draw,control image,screen,maximum simultaneous effects,firmware/count reconciliation,precise connector sizes,USB/MIDI/editor compatibility,IR/NAM/capture,drums/scenes and condition-qualified prices. Vintage Pre is an algorithm,not proof of a mic input or vocal membership.

[HD4-P]: https://line6.com/legacy/podhd400
[HD4-M]: https://line6.com/data/6/0a06434df9be5005ac8bcc52f/application/pdf/POD%20HD300%20Advanced%20Guide%20%28%20Rev%20A%20%29.pdf
[HD4-Q]: https://www.manualshelf.com/manual/line-6/pod-hd400/quick-start-manual-english.html
[HD4-QO]: https://line6.com/data/6/0a060b316ac34f05938560c41/application/pdf/POD%20HD400%20Quick%20Start%20Guide%20-%20English%20%28%20Rev%20C%20%29.pdf
[HD4-E]: https://l6c-acdn2.line6.net/data/6/0a06434dfd3f5005ada360213/application/pdf/POD%20HD400%20Edit%20Pilot%27s%20Guide%20%28%20Rev%20A%20%29.pdf
[HD4-F]: https://kb.line6.com/pod-hd300-400-500-amp-model-and-fx-list
[HD4-C]: https://kb.line6.com/macos-11-big-sur-silicon-m1-chip-compatibility

## POD HD300

Checked2026-10-17;partial;ownership unverified. Own RevC handbook;HD400-only features not borrowed.

<!-- comparison evidence begins -->

| Field | Finding / qualification |
|---|---|
| Expression | Built-in wah/volume/FX1 Pitch Glide;toe switches modes. No Pedal2 socket:shared guide explicitly reserves external Pedal2 for HD400. [Manual][HD300-M] |
| K/F/B | **12 rotary/6 main footswitches/2 separate buttons**,plus4-way Nav disc,Presets encoder push and pedal toe switch. Rotary:Amp,Drive,Bass,Mid,Treble,ChVol,Reverb,FX1/2/3,Presets,rearMaster. Foot:A/B/C/D,Mode,Tap. Buttons:Save,FXOnly. Nav directions are not4separate button caps. [Manual][HD300-M] |
| Display | Main LCD plus segmented bank/preset display;diagonal/color/touch unverified. [Manual][HD300-M] |
| Processing / categories | FX1 gain/various/pitch;FX2 modulation/filter/tremolo;FX3 delay/tape/sweep;9reverbs. Exact algorithms/full ceiling pending. FXOnly globally disables amp modeling. [Manual][HD300-M] |
| Processing / FX1 inventory Flash2.0+ | **37 alternatives**,counted after excluding HD400-only starred entries:18GAIN,10VARIOUS,9PITCH-table entries. GAIN:Screamer,Tube Drive,Classic/Heavy Distortion,Color Drive,Overdrive,Line6 Drive/Distortion,Boost Comp,Red/Blue/Vetta Comp,Fuzz Pi,Octave/Jet/Sub Octave/Facial/Jumbo Fuzz. VARIOUS:Spring,Parametric EQ,4-Band Shift EQ,Tron Down/Up,Q Filter,Ring Modulator,Dimension,Frequency Shifter,Rotary Drum. PITCH-table:Smart Harmony,Pitch Glide,Synth String,Growler,Synth-O-Matic,Bass Octaver,V Tron,Vintage Pre,Hard Gate. Last2addedFlash2.0;table placement does not make them pitch algorithms. [Advanced guide][HD300-A] |
| Processing / FX2 inventory | **18 alternatives**:9MOD(Analog Chorus/Flanger,U-Vibe,Phaser,Dual/Barberpole/Panned/Script Phase,Pitch Vibrato),5FILTER(Seeker,Throbber,Spin Cycle,Obi-Wah,Voice Box),4TREMOLO(Opto,Bias,Pattern,Panner). These are selections within one slot,not18 simultaneous effects. [Advanced guide][HD300-A] |
| Synth / bass revision qualification | Flash2.0+ shared guide includes Flip Top bass amp and115FlipTop bass cab for HD300;positive bass basis. Synth String,Growler,Synth-O-Matic included;Attack Synth explicitly HD400-only. Installed firmware unverified. Acoustic simulator remains unverified. [Advanced guide][HD300-A] |
| Processing / FX3 inventory | **18 alternatives** in Flash2.0+ guide6-14,excluding HD400-only Multi-Head Delay:10DELAY(Digital,Digital w/Mod,Analog Echo,Analog w/Mod,Echo Platter,Echo Platter Studio,Low Res,Stereo,Ping Pong,Dynamic);4TAPE(Tape Echo,Tape Echo Studio,Tube Echo,Tube Echo Studio);4SWEEP(Auto Volume Echo,Sweep Echo,Sweep Echo Studio,Reverse Delay). One selection per FX3 slot. [Advanced guide][HD300-A] |
| Processing / reverb count conflict | Advanced guide6-16 lists **8 HD300 choices**:Plate,Room,Chamber,Hall,Echo,Tile,Cave,Octo;Ducking is starred HD400-only. Own RevC handbook says9reverbmodels. Preserve this source/revision conflict;do not silently assign Ducking to HD300. [Advanced guide][HD300-A] [Handbook][HD300-M] |
| Expression / wah inventory | **6 HD300 choices**,guide6-18:Vetta,Fassel,Chrome,Weeper,Conductor,Colorful. Throaty and Chrome Custom are HD400-only. Wah Edit menu selects model;onboard pedal operates it. [Advanced guide][HD300-A] |
| Live / FX3 tempo storage | TapCtl is global,not preset-stored. When disabled,delay milliseconds are preset-stored;enabled follows tapped tempo with0.1BPM editing(or1BPM while pushing encoder). Numeric delay limits remain unverified. [Advanced guide][HD300-A] |
| Processing / amp table versus summary | Flash2.0+ guide5-8/5-9 contains **30 named amp entries**,counted as16knob-accessible+14Edit-only,despite summary prose saying16. Edit-only:Blackface Double Vibrato,Tweed B-Man Bright,Blackface Lux Vibrato,Brit J-45 Normal,Brit P-75 Normal,Line6 Elektrik,Plexi Lead Normal/Bright,Solo Clean/Crunch/OD,Line6 Doom/Epic,Flip Top. Full/preamp variants are selectable,not simultaneous amps. [Advanced guide][HD300-A] |
| Processing / cab count conflict | Guide5-3 says16cabs;5-10/5-11 lists **17 named cabinets plus None**,including115FlipTop basscab. Preserve summary/table discrepancy. None disables cab/mic modeling;cab choice saved per preset. No userIR import established. [Advanced guide][HD300-A] |
| Processing / microphone choices | Guitar cabs offer8:57On/OffAxis,409Dyn,421Dyn,4038Ribbon,121Ribbon,67Cond,87Cond. FlipTop offers its own8:57OnAxis,421Dyn,12Dyn,112Dyn,20Dyn,7Dyn,40Dyn,47Cond. These are cabinet-dependent choices,not16simultaneous microphones. [Advanced guide][HD300-A] |
| Processing / base amp names | 16knob-accessible entries:Blackface Double Normal,Hiway100,Super O,Gibtone185,Tweed B-Man Normal,Blackface Lux Normal,Divide9/15,PhD Motorway,Class A-15,Class A-30TB,Brit J-45 Bright,Brit P-75 Bright,Brit J-800,Bomber Uber,Treadplate,Angel F-Ball. Additional14Edit-only entries listed above. [Advanced guide][HD300-A] |
| Processing / cabinet names | 17named choices:212Blackface Double,412Hiway,6×9Super O,112Field Coil,410Tweed59,112BF Lux,112Celest12-H,212PhD Ported,112Blue Bell,212Silver Bell,412Greenback25,412Blackback30,412Brit T-75,412Uber,412Tread V-30,412XXL V-30,115FlipTop;plusNone. This is the table inventory,not a resolution of the conflicting16cab prose. [Advanced guide][HD300-A] |
| I/O / Live and Dual clarification | LIVE retains specially voiced Live cab processing without mic simulation. HD300 DUAL sends LIVE left and Studio mic/cab sound right on both balanced/unbalanced pairs;HD400 instead separates by connector family. Earlier “direct” wording must not imply raw bypass. [Advanced guide][HD300-A] |
| Live / tuner and tempo | Tuner mutes output;any footswitch exits. System Tap Tempo is saved per preset,while FX2/FX3 TapCtl sync-enable remains global. These are separate settings. [Advanced guide][HD300-A] |
| Expression / volume routing and noise tools | Volume may sit pre/post amp,with pedal assignments saved per preset. Gate menu provides Noise Gate and Noise Reduction,also saved per preset;not extra freely assignable FX1 selections. [Advanced guide][HD300-A] |
| Processing / dual-tone limit | Official knowledge base restricts dual-tone configurations to HD500/500X,HD Desktop,HD Pro/ProX;HD300 lacks this capability. DUAL output mode on HD300 is a Live/Studio output split,not two independent amp tones. [Official dual-tone FAQ][HD300-D] |
| Editor / preset incompatibility | Official FAQ states XT/X3 tones do not work with HD architecture. HD500/500X tones also do not translate to HD300/400 because routing differs. Model-specific editor/preset files must not be treated as universally interchangeable. IR/NAM/capture remains separately unverified. [Official tone FAQ][HD300-T] |
| Preset memory | 32banks×ABCD=128locations,preloaded and overwritable. Rear Master unsaved. Additional factory library unverified. [Manual][HD300-M] |
| Synth / acoustic | Synth and firmware-qualified bass evidence below;acoustic simulation unverified. |
| I/O | GuitarIn,CD/MP3,¼inch unbalanced outs,XLR balanced outs,phones,L6LINK,USB,power. Remaining socket sizes/channel details pending. [Manual][HD300-M] |
| I/O / routing | Studio cab/mic simulation;Live guitar-amp use;Dual left direct/right studio-simulated. XLR groundlift;unbalanced AMP/LINE switch. L6LINK carries audio/control. [Manual][HD300-M] |
| I/O / advanced USB restrictions | Flash2.0+ shared guide applies to HD300 unless explicitly excepted. **24-bit;native48kHz**,converted44.1/88.2/96kHz. Stereo1–2 MainOut recording send is processed;computer playback mixes with direct monitoring to analog outputs. **All USB audio mutes while L6LINK is active**. Dry USB recording not established. [Advanced guide][HD300-A] |
| Editor / historical audio driver | Line6 USB driver required by reviewed2012guide;MacCoreAudio,WindowsASIO/DirectSound. Driver5.7.0 drops MacOSX10.4;earlier5.1.2 supported it. Historical compatibility is not currentOS support. Editor/updater remain separate from driver. [Advanced guide][HD300-A] |
| Looper / hold-Tap distinction | 24s **mono** looper. In Looper mode holdTap clears audio and stops playback/recording;it does not open tuner. Switch to Preset/PedalOnOff first for holdTap tuner. [Advanced guide][HD300-A] |
| I/O / model distinction | External FX loop is explicitly **HD400 only** in shared guide;do not assign one to HD300. [Advanced guide][HD300-A] |
| Power / battery / USB | Supplied Line6 power supply;unplug turns off. Voltage/current/polarity/battery/USBpower unverified. [Manual][HD300-M] |
| Dimensions / mass | Unverified. |
| IR / NAM / capture | Import/capture support unverified. |
| Editor / platforms | POD HD300 Edit Windows/Mac;presets/bundles. USB recording documented;audio driver/minimumOS pending. Monkey updater separate. [Manual][HD300-M] |
| Looper / live | 24s;pre/post recording,overdub,playonce. Preset/Looper/PedalOnOff modes;holdTap tuner. Drums/scenes unverified. [Manual][HD300-M] |

### Separate IDR hardware offers

| Condition | Evidence | Source |
|---|---|---|
| Unverified | **Rp1.500.000**,mendemkaset,shop504301607/item29822606720,Kab.Tulungagung;Habis,two months indexed crawl. | [Item][HD300-O1] |
| Unverified mixed variations | **Rp3.699.000 unallocated**,Hope Music,shop703817770/item24703618953,Kota Bandung;4HD300/400/500/500X variations,four months indexed crawl. Not an HD300-specific price. | [Item][HD300-O2] |

<!-- comparison evidence ends -->

Historical indexed asks checked2026-10-17,not livecheckout. Conditions,stock,bundles,variants,warranty,authenticity,shipping,tax,vouchers unresolved. No qualified used/new allocation. No files downloaded or images visually inspected.

[HD300-M]: https://line6.com/data/6/0a060b316ac34f05937e126fa/application/pdf/POD%20HD300%20Quick%20Start%20Guide%20-%20English%20%28%20Rev%20C%20%29.pdf
[HD300-O1]: https://shopee.co.id/Line6-POD-HD300-Digital-Multy-Effect-Guitar-i.504301607.29822606720
[HD300-O2]: https://shopee.co.id/Efek-Gitar-Line6-POD-HD300-HD400-HD500-HD500X-i.703817770.24703618953

[HD300-A]: https://l6c-acdn.line6.net/data/6/0a06434dfde45005adfca27d6/application/pdf/POD%20HD400%20Advanced%20Guide%20%28%20Rev%20A%20%29.pdf

[HD300-D]: https://kb.line6.com/do-all-pod-hd-modelers-sport-dual-tone-functionality
[HD300-T]: https://kb.line6.com/are-pod-hd-tones-compatible-with-older-pods

## Floor POD Plus

Guitar multi-effects;checked2026-10-17;partial. [Own Spanish manual][FPP-M],40-00-0116RevB,©2009,36pages,sections1,2,3,4. Not original FloorPOD. Bass/vocal suitability andownership unverified.

| Field | Evidence / gaps |
|---|---|
| Expression | Built-in volume/wah,toe switches wah;external socket unlisted. |
| Controls | Text-derived **14rotary/7foot/2separatebuttons**;AMP encoder push additional,rearAmp/Direct separate. Rotary:AMP,Effects,Delay-select,Drive,Bass,Mid,Treble,ChannelVolume,Compressor,Gate,EffectTweak,Delay-level,Reverb,OutputLevel. Foot:Bank±,A–D,Tap;buttonsSave/Manual. Visual verification pending. |
| Display | Channel/note display;diagonal,color,touch unverified. |
| Processing / choices | **32amps;16cab selections includingNoCab;16FX;6delays;2reverbs**. Compressor,gate,wah;aggregate simultaneous count pending. |
| Factory / user memory | **124 factory-filled,editable channels,31×4**;same locations,not124+124. |
| Synth / acoustic | Unverified;A.I.R. speaker/mic/room simulation is not acoustic-guitar conversion. |
| Dimensions / mass | Unverified. |
| I/O | Guitarinput,AUX,L/Mono+Routs,quarter-inchphones,MIDIIn/Out,power;connector sizes otherwise pending. NoUSB listed. |
| Power / batteries | [Own FAQ][FPP-F] specifies **PX-2**;voltage,current,polarity,battery unresolved. USBpower unsupported by port inventory. |
| IR / NAM / captures | User loading unverified. |
| Editor / platforms | FAQ: **Vyzex FloorPODPlus viaMIDI**;OS support pending. |
| Looper / drums / live | Looper/drums/scenes unverified. Tapdelay,holdtuner;A–D can switch amp,solo,FX,delay. |

### Floor POD Plus — separate IDR evidence

| Condition | Amount / qualifications | Offer |
|---|---|---|
| Used exact-model price | Unknown | — |
| New | Unknown | — |
| Mixed seller-labelled second/bekas listing | **Rp2,000,000–2,500,000 unallocated**,four variations acrossAX3000G/AX1500G/FloorPODPlus;**Habis**. studio_musik_gema,Kab.Blitar;shop102019323/item25663831731;two-month searchcache2026-10-17. | [Shopee][FPP-S] |

Not an exact FloorPODPlus ask. Seller normal/bonus-bag claims unverified;selectedvariant,workingstate,adapter,bundle,warranty,voucher,shipping/tax/liveStock unknown. Stale11–14August delivery. No download or visualinspection.

[FPP-M]: https://line6.com/data/6/0a060b316ac34f0593b6b6f51/application/pdf/Floor%20POD%20Plus%20user%20manual%20-%20Spanish%20%28%20Rev%20B%20%29.pdf
[FPP-F]: https://kb.line6.com/floor-pod-floor-pod-plus-faq
[FPP-S]: https://shopee.co.id/efek-gitar-second-korg-ax3000g-ax1500g-pod-floor-plus.-bonus-tas-effect-guitar-ax-3000g-1500g-3000-1500-bekas-normal-bukan-zoom-nux-mg-valeton-line-6-moer-i.102019323.25663831731

### Floor POD Plus — memory and effect restrictions

Checked2026-10-17;[SpanishRevB][FPP-M],sections3•1–3•6,4•1–4•3.

| Field | Verified behavior / qualification |
|---|---|
| Processing / FX16 | Tremolo,Chorus1/2,Flange1/2,Rotary,Phaser,U-Vibe,Obi-Wah,Tron-Up,OctaveFuzz,SubOctave,CometTrails,RingModulator,OttoPhase,Swell. These are alternatives in one FX selection,not16 simultaneous blocks. |
| Processing / delay-reverb | Delay choices:Tape,Multi-Tap,Digital,Reverse,SweepEcho,Analog. Reverb is Spring orRoom,automatically assigned by amp model;not established as freely selectable independently. Compressor offers five active ratios(1.4:1,2:1,3:1,6:1,infinity:1),plusoff. |
| Factory / user memory | All124 channels editable;Save,choosebank1–31/channelA–D,confirm. Turning a knob or waiting5s cancels saving. Custom default settings for currentamp/FX/delay can also be saved;these do not add channel slots. |
| Preset / live | HoldSave2s entersCompare;indicators compare knob position with stored value. Manual mode uses physical knob positions;exiting recalls the last channel. |

### Floor POD Plus — supply identity and editor boundaries

Checked2026-10-17.

| Field | Evidence / qualification |
|---|---|
| Power / adapter | [Own-model FAQ][FPP-F] requires PX-2. [Line6's PX-2 specification in its JM4 FAQ](https://kb.line6.com/jm4-faq) identifies that named adapter as **9VAC,2000mA,2.5mm diameter**. This establishes compatible supply identity/rating,not FloorPODPlus measured current draw or any JM4 battery/connector/function claim. DC centre polarity does not describe an AC output. Regional mains rating and FloorPODPlus battery support remain unverified. |
| Editor / software identity | [Official editor guide](https://line6.com/customtone/help/editors.html) assigns separate Vyzex versions to PocketPOD andFloorPODPlus. Its Windows/Mac Java instructions concern Line6Edit,not Vyzex;do not transfer those requirements. Exact Vyzex OS/version compatibility remains unverified;community reports are not manufacturer support guarantees. |
| Documentation | [Own English Pilot's Guide](https://line6.com/data/l/0a060072caf7499051779818f/application/pdf/Floor_POD_Plus_user_manual.pdf) located/read as36-page official PDF;available for subsequent cross-checks. SpanishRevB remains the explicitly identified source for earlier facts. |
