# Line 6 multi-effects

Root-level brand comparison. **Checked 2026-10-15.** POD Go Wireless and POD Express Guitar/Bass are newly researched here; the standard POD Go profile is consolidated from its existing source-backed record without adding another model to the inventory. Other legacy Line 6 records still require consolidation; no whole-repository migration claim is made. No GitHub Actions workflows are used.

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

## POD Express Bass

**New bass-specific model, checked2026-10-15.** A separate hardware/sound-library record, not a color option for POD Express Guitar. The official Bass product and joint2.00 manual explicitly document the following common hardware and different processing path. This record is partial; current dimensional evidence and precise OS minima remain unresolved.

| Required field | Verified specification / limitation |
|---|---|
| Expression | **No built-in pedal**;one shared TRS VOLUME/FS3,4 port for volume expression,two switches or expression plus one switch. Arbitrary effect-parameter expression is not established. [PE-B,PE-M] |
| Controls | **6 rotary /2 footswitches /1 button**: amp encoder,four category knobs,side volume;ON,TAP;ALT. Encoder press is not counted again. [PE-B] |
| Display | **No graphical/numeric screen;no touchscreen**. Seven multicolor LED ring segments and switch LEDs are indicators,not a color graphical display. Diagonal and screen color classification N/A. |
| Dimensions / mass | **Unverified from primary sources**. The inconsistent350g/400g and rounded reseller measurements are not substituted for manufacturer specifications; mechanical size bin remains unknown. |
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
| Editor | **POD Express Edit Windows/macOS/iOS/iPadOS/Android**,hardware2.00+;desktop Central updater separately. The joint manual's contradictory OS-minimum tables are retained in the Guitar entry; no arbitrary minimum or Linux-editor claim. [PE-R,PE-M] |
| USB audio | **4-in/4-out,24-bit/48kHz**,processed1/2,dry3/4,reampUSB3/4;Windows ASIO,other supported platforms class compliant. USB recording still requires AA/DC power. [PE-M,PE-F] |
| Live / practice | **30s stereo looper**,one-switch,post-effects,undo/redo;clears on preset change,exiting looper or power-off. Tuner,tap,external-switch assignments. Internal drums not established. [PE-M] |

The family manual's headphone/main-output caveat also applies: L/MONO sums to mono when used alone without headphones,but with headphones connected it carries the left channel of stereo effects. Neither two main sockets nor stereo USB creates two independent processing chains.

### POD Express Bass — IDR evidence and sources

**Retail indexed ask: Rp3.099.000**, [Seven Stereo Music & Audio Store, Shopee shop16879370/item29813481193](https://shopee.co.id/Line-6-POD-Express-Bass-INT-P38-2-i.16879370.29813481193). Re-found2026-10-15; the indexed body retains **August13–15 delivery text**, and direct reopening failed. Not verified current stock,new-condition certification or a completed sale. Accessories,regional warranty and shipping remain unknown. **Used IDR: ?**. No conversion or assumed secondhand percentage.

[PE-B] [Official POD Express Bass page with numbered controls/ports](https://line6.com/podexpress/bass-effects). The Bass-specific effect table and signal path are in [PE-M] above, especially printed pp.26–27. [PE-F] explicitly names Bass for the battery,USB-power and driver rules. Sources shared across models are explicit manufacturer family documentation,not sibling-model inference.

## HX Effects

**Guitar/bass effects-only multi-effects**, not a single-function pedal. No amp modeling is required for inclusion. Consolidated from the complete `effects/advanced-modelers.md` record (technical snapshot 2026-10-14), with model-specific manufacturer rechecks **2026-10-16**. This is the existing inventory entry, not a new model.

| Required field | Evidence / qualification |
|---|---|
| Built-in / external / toe expression | No built-in pedal or toe switch; **two external pedal sockets shared with amp-control outputs**. Each can instead control two amp-switch functions; selecting amp control consumes that expression connection. [HXE-P, HXE-F] |
| Knobs / footswitches / buttons | **4 / 8 / 6** from the official numbered control inventory: Big Knob plus three parameter knobs; six assignable footswitches plus MODE and TAP; SAVE, MENU, ACTION, HOME and two PAGE buttons. Encoder presses counted once; rear power toggle separate. Earlier ?/8/? count is superseded. [HXE-P] |
| Display | **Six customizable LCD scribble strips**; no large central display. Published diagonals, monochrome/color and touchscreen specifications unverified. Capacitive-touch footswitches and colored LED rings do **not** establish a touchscreen or color LCDs. [HXE-P] |
| Body / size | Official FAQ **10.8 W ×7.9 D ×2.8 H inches; 4.75 lb**, approximately **274×201×71 mm; 2.15 kg**. Rounded conversions, not precision measurements. **Large**, because rounded depth exceeds the 200 mm medium limit. [HXE-F] |
| Blocks / category choices | **Nine simultaneous blocks, DSP-limited**, reorderable with parallel Path B. No amp or factory cabinet-model blocks. Legacy FAQ's 117 HX +77 Legacy effects is a **launch-era** count, not the present library. Distortion/dynamics/EQ/modulation/delay/reverb/pitch-synth/filter/wah/volume/IR/loop utilities are documented; complete firmware-current subtotals remain unverified. [HXE-F, HXE-M] |
| Memory | **128 overwriteable presets**, four snapshots each; factory-filled subset not separately established. [HXE-F, HXE-M pp.16,31] |
| Synth / acoustic | **Synth yes**: 3 OSC Synth and Legacy synth models explicitly listed. Acoustic-body IR loading supported; this is distinct from a verified dedicated electric-to-acoustic simulator algorithm. [HXE-M p.22; HXE-F] |
| IR / NAM / captures | **128 user IR locations**, one 2048-sample block or two 1024-sample blocks per preset. IRs consume processing blocks and sum their input to mono. Native NAM, converted NAM and user amp-capture import not established. [HXE-M pp.24–25] |
| I/O | Two 6.35 mm instrument/line inputs; two **unbalanced TS** main outputs; two TS sends and two TS returns (two mono loops or one stereo loop); two PEDAL/EXT AMP sockets; MIDI DIN IN and OUT/THRU; USB-B; DC. No dedicated headphone output in the complete rear-panel inventory. [HXE-P] |
| Power / battery / USB | Included **DC-3G**, **2.5 mm pin**, FAQ requires **at least 2 A clean DC**. Voltage/polarity and battery/USB-powered operation not independently established here; do not copy another HX supply specification. Supply requirement is not measured current draw. [HXE-F] |
| Editing / USB | **HX Edit Windows/macOS** full editor, preset/IR librarian; current official page and manual supersede the launch FAQ's librarian-only wording. HX Edit 2.60+ with matching hardware firmware added full editing. **USB MIDI, explicitly no USB audio interface**. iOS USB remote MIDI control is not an iOS full editor; Android/Linux editing unverified. [HXE-P, HXE-F, HXE-E] |
| Practical features | Analog relay or DSP bypass with trails, snapshots, parallel routing, four/seven-cable integration, MIDI/amp control and Pedal Edit. Looper occupies one of nine blocks. Current looper duration/modes and drums remain unverified here. [HXE-F] |

### HX Effects — IDR and source provenance

**Used IDR: ?; new IDR: ?**. Exact Shopee Indonesia hardware searches on 2026-10-16 did not establish an item with a qualified ask. Do not invent stock, region, bundle, seller, voucher or a converted USD price. The legacy record likewise had no used/new price; the FAQ's **$599.99 US MAP** is launch-price provenance, not a current Indonesian offer.

- [HXE-P: official HX Effects page and complete numbered front/rear controls](https://line6.com/hx-effects/).
- [HXE-F: official HX Effects FAQ](https://kb.line6.com/hx-effects-faq), retaining its launch-era library/software/price limits. It explicitly identifies guitar **and bass** use.
- [HXE-M: manufacturer HX Effects 3.0 Owner's Manual, Rev C](https://line6.com/data/6/0a020a411710a6112a67116f0b/application/pdf/HX%20Effects%203.0%20Owner%27s%20Manual%20-%20Rev%20C%20-%20English%20.pdf). Original manual text inspected for model list, IRs and memory. Web screenshots failed; no successful new PDF visual inspection claimed. Official product's numbered panel independently supports the control/port count.
- [HXE-E: manufacturer HX Edit Pilot's Guide Rev E](https://line6.com/data/6/0a020a3f182a45b4f6d41c90dc/application/pdf/HX%20Edit%20Pilot), full editing from 2.60; [current HX Edit software listing](https://line6.com/software/index.html?hardware=All&name=HX+Edit&os=All&submit_form=set).

All earlier HX Effects facts, rounded-dimension provenance, nine-block/128-preset/four-snapshot distinctions, amp-control sharing, IR/acoustic qualifications, source URLs and launch-FAQ correction are preserved. Legacy source retained because it also contains five other model records. Remaining: current category totals, exact display specifications, supply voltage/polarity, explicit battery/USB-power statements, looper limits and qualified IDR offers.

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
