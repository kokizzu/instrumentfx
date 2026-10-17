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
| Blocks / category choices | **Nine simultaneous blocks, DSP-limited**, reorderable with parallel Path B. No amp or factory cabinet-model blocks. Legacy FAQ's 117 HX +77 Legacy effects is a **launch-era** count, not the present library. Distortion/dynamics/EQ/modulation/delay/reverb/pitch-synth/filter/wah/volume/IR/loop utilities are documented; complete firmware-current subtotals remain unverified. [HXE-F, HXE-M] |
| Memory | **128 overwriteable presets**, four snapshots each; factory-filled subset not separately established. [HXE-F, HXE-M pp.16,31] |
| Synth / acoustic | **Synth yes**: 3 OSC Synth and Legacy synth models explicitly listed. **Acoustic Sim**,mono/stereo,in the3.80 EQ library now establishes a dedicated acoustic-simulation algorithm;this supersedes the earlier unverified status. Acoustic-body IR loading is a separate capability. Firmware/library revision remains device-specific. [HXE-M p.22; HXE-F; HXE-D p.20] |
| IR / NAM / captures | **128 user IR locations**, one 2048-sample block or two 1024-sample blocks per preset. IRs consume processing blocks and sum their input to mono. Native NAM, converted NAM and user amp-capture import not established. [HXE-M pp.24–25] |
| I/O | Two 6.35 mm instrument/line inputs; two **unbalanced TS** main outputs; two TS sends and two TS returns (two mono loops or one stereo loop); two PEDAL/EXT AMP sockets; MIDI DIN IN and OUT/THRU; USB-B; DC. No dedicated headphone output in the complete rear-panel inventory. [HXE-P] |
| Power / battery / USB | Included **DC-3G**, **2.5 mm pin**, FAQ requires **at least 2 A clean DC**. Voltage/polarity and battery/USB-powered operation not independently established here; do not copy another HX supply specification. Supply requirement is not measured current draw. [HXE-F] |
| Editing / USB | **HX Edit Windows/macOS** full editor, preset/IR librarian; current official page and manual supersede the launch FAQ's librarian-only wording. HX Edit 2.60+ with matching hardware firmware added full editing. **USB MIDI, explicitly no USB audio interface**. iOS USB remote MIDI control is not an iOS full editor; Android/Linux editing unverified. [HXE-P, HXE-F, HXE-E] |
| Practical features | Analog relay or DSP bypass with trails,snapshots,parallel routing,four/seven-cable integration,MIDI/amp control andPedal Edit. **One looper block maximum per preset**,using one of9 blocks:6 Switch,1 Switch orShuffling,inmono/stereo. **6/1Switch full-speed60s mono/30s stereo;half-speed120s mono/60s stereo**. Shuffling60s mono/30s stereo,nohalf-speed entry. Preset changes retain playback only with the **same looper model AND mono/stereo type**. Six-switch controls include overdub,last-overdub undo,play-once,reverse andspeed. Drum machine remains unverified. [HXE-F; HXE-D pp.27–28] |

### HX Effects — IDR and source provenance

**Used IDR: ?; new IDR: ?**. Exact Shopee Indonesia hardware searches on2026-10-16 and2026-10-17 did not establish an Indonesian item with a qualified ask. Later searches returned foreign-region offers,which are not IDR evidence. Do not invent stock, region, bundle, seller, voucher or a converted USD price. The legacy record likewise had no used/new price; the FAQ's **$599.99 US MAP** is launch-price provenance, not a current Indonesian offer.

- [HXE-P: official HX Effects page and complete numbered front/rear controls](https://line6.com/hx-effects/).
- [HXE-F: official HX Effects FAQ](https://kb.line6.com/hx-effects-faq), retaining its launch-era library/software/price limits. It explicitly identifies guitar **and bass** use.
- [HXE-M: manufacturer HX Effects 3.0 Owner's Manual, Rev C](https://line6.com/data/6/0a020a411710a6112a67116f0b/application/pdf/HX%20Effects%203.0%20Owner%27s%20Manual%20-%20Rev%20C%20-%20English%20.pdf). Original manual text inspected for model list, IRs and memory. Web screenshots failed; no successful new PDF visual inspection claimed. Official product's numbered panel independently supports the control/port count.
- [HXE-E: manufacturer HX Edit Pilot's Guide Rev E](https://line6.com/data/6/0a020a3f182a45b4f6d41c90dc/application/pdf/HX%20Edit%20Pilot), full editing from 2.60; [current HX Edit software listing](https://line6.com/software/index.html?hardware=All&name=HX+Edit&os=All&submit_form=set).

- [HXE-D: official HX Effects3.80 Owner’s Manual,RevD](https://line6.com/data/6/0a00051afdbe673ccc8bdcf2d/application/pdf/HX%20Effects%203.80%20Owner%27s%20Manual%20-%20English%20.pdf),indexed manufacturer text checked2026-10-17:EQ table p.20;looper types/durations andpreset-continuity restrictions pp.27–28. No manual/software/firmware files downloaded to the workspace. This documents revision3.80,not proof of installed firmware.

All earlier HX Effects facts, rounded-dimension provenance, nine-block/128-preset/four-snapshot distinctions, amp-control sharing, IR/acoustic qualifications, source URLs and launch-FAQ correction are preserved. The shared legacy page now redirects with pinned originals. Remaining:firmware-current category subtotals,exact display specifications,supply voltage/polarity,explicit battery/USB-power statements,complete Shuffling/control details andqualified Indonesian offers. Earlier acoustic-simulation andlooper unknowns are superseded only by the revision-qualified evidence above.
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
