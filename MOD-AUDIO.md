# MOD Audio — multi-effects discovery

[Repository](README.md) · [Footswitch displays](FOOTSWITCH-DISPLAYS.md)

<!-- brand-index begins -->
**Model and section index — A–Z, natural numeric order**

- [Duo](#duo)
<!-- brand-index ends -->

## Duo

Admitted **2026-11-01** as an **active partial guitar/bass/voice processor**, not fully verified. Original Duo is distinct from Duo X/Dwarf. LCD technology is known, but one dedicated screen above each footswitch remains unverified. No ownership, current-stock or complete-library claim. Earlier outside-inventory statements below are preserved historical checkpoints.

<!-- comparison evidence begins -->

| Field | Evidence / qualification |
|---|---|
| Instrument scope | Own product explicitly names guitar, bass and voice with independent processing; normal instrument input, not special-pickup equipment. Voice support does not certify microphone gain, phantom power or every vocal algorithm. [Manufacturer](https://mod.audio/mod-duo/). |
| Built-in / external / toe expression | No built-in treadle in documented panel. **No direct analog EXP port**, explicitly in own guide. MIDI converters/Control Chain adapters are separate hardware; toe support unknown. [Own guide](https://wiki.mod.audio/wiki/MOD_Duo_User_Guide). |
| Expression / global volume | Requested direct analog path fails. Direct assignment, endpoints and recall N/A for absent port; MIDI/Control Chain global assignment, bypass, headphone, tail and looper coverage unknown. Calibration and saved plugin state do not establish global volume. [Audit](#duo--partial-lcd-discovery). |
| Knobs / footswitches / buttons | **Two push knobs; two footswitches**. Separate-button census/visual corroboration remain unverified. One parameter assignment per footswitch; knobs can cycle several. [Own guide](https://wiki.mod.audio/wiki/MOD_Duo_User_Guide);[OS1.13 control scope](#duo--footswitch-assignments-and-snapshot-scope). |
| Display | **Two LCDs**, technical page2.7in versus user guide2.8in. Color, touch and exact physical screen-to-foot placement unresolved; menus use left main/right submenu. LED colors are separate. [Conflict](#duo--partial-lcd-discovery);[LCD navigation](#duo--os-110-lcd-navigation-and-file-loading-scope). |
| Dimensions / weight | Own product **180W×160D×74.7H mm;1.2kg** versus wiki **160W×186L×75H mm**. Both exceed preferred200W×140D. Revision/measurement basis unknown. [Full source conflict](#duo--manufacturer-product-page-dimensions-and-instrument-scope). |
| Processing / simultaneous limits | Modular LV2/JACK host; plugin-dependent CPU/RAM, no verified fixed block ceiling. Two independent audio channels support split/join/feedback. Optional256-frame buffer trades latency for processing headroom; not guaranteed extra blocks. [Architecture](#duo--processing-architecture-and-resource-limits);[product](https://mod.audio/mod-duo/). |
| Categories / choices | Manufacturer advertises over400 available free plugins spanning effects, amps, instruments and MIDI utilities. This is not a complete current category census, installed inventory or400 simultaneous algorithms. [Own product](https://mod.audio/mod-duo/). |
| Preset memory | Saved pedalboards organized in banks; exact factory/user/total counts unknown. Snapshots store parameters inside boards; save the containing board after edits. Four I/O/MIDI profiles are not four preset slots;4GB/8GB flash disagreement is not preset capacity. [Settings](#device-settings--os-113-scope);[snapshots](#duo--footswitch-assignments-and-snapshot-scope). |
| Synth / acoustic | MIDI-controlled virtual instruments advertised. This does not establish ordinary-pickup oscillator synthesis, polyphonic tracking or electric-to-acoustic simulation; exact compatible engines remain unverified. [Own product](https://mod.audio/mod-duo/). |
| Audio I/O | Two independent TS1MΩ inputs; two balanced-compatible TRS outputs;6.35mm stereo phones. Technical page later calls all audio connectors TRS, conflicting with its explicit TS input list. Full connector dimensions and mic/phantom tolerance unknown. [Own specs](https://wiki.mod.audio/wiki/MOD_Duo_Technical_Specs). |
| Headphones / levels | Phones monitor outputs1/2 or direct inputs, with independent volume. Technical phones+12…−33dB; main0…−127dB in0.5dB steps. These are hand-operated controls, not expression endpoints or proven mute coverage. [Guide](https://wiki.mod.audio/wiki/MOD_Duo_User_Guide);[specs](https://wiki.mod.audio/wiki/MOD_Duo_Technical_Specs). |
| MIDI / USB / control ports | DIN5 MIDI In/Out; TypeA USB2 host,500mA peripheral-output rating; TypeB USB2 device for network editor/update; Control Chain RJ45 is not Ethernet. Bluetooth uses an adapter. USB audio and USB-powered operation remain unverified. [Own specs](https://wiki.mod.audio/wiki/MOD_Duo_Technical_Specs);[guide](https://wiki.mod.audio/wiki/MOD_Duo_User_Guide). |
| Power | **12VDC centre-positive, supplied2A adapter**,5.5×2.1×10mm plug. Guide also prints12W/1.5A; arithmetic/source discrepancy retained, not measured draw. Adapter input100–240VAC50–60Hz. Battery/USB operation unknown. [Power qualification](#duo--partial-lcd-discovery);[product](https://mod.audio/mod-duo/). |
| IR / loading | **User WAV/FLAC IR through Convolution Loader**, explicitly Duo-applicable;48kHz24bit WAV recommended. Duo maximum less than15s for Duo X/Dwarf, exact limit unknown; generic wiki2048-sample claim remains separately qualified. Multichannel files processed stereo. [Exact plugin evidence](#duo--plugin-specific-ir-import-and-tail-behavior). |
| NAM / capture | Original-Duo native NAM, converted NAM, AIDA-X and capture playback remain unverified. File extension acceptance, upstream A1/A2 claims and build flags do not prove installed hardware compatibility. NAM recipe disables RTNeural; separate AIDA package. [Version/build evidence](#duo--manufacturer-nam-build-configuration-and-provenance). |
| Editor / platforms | Built-in browser WebGUI via USB network; guide names Chrome/Safari/Firefox. Exact host minima/current OS compatibility unknown. Standalone playing after setup; browser editing distinct from updater, USB audio or Bluetooth streaming. [Own guide](https://wiki.mod.audio/wiki/MOD_Duo_User_Guide). |
| Firmware / scope | OS1.13 settings and historical1.10/1.13.2 changes documented; current installed firmware/revision equivalence unknown. Developer clock912MHz versus technical1GHz and4GB versus8GB flash retained. [Resource conflict](#duo--processing-architecture-and-resource-limits);[file handling](#duo--neural-model-file-acceptance-versus-playback-compatibility). |
| Looper / drums / live | Manufacturer advertises loopers, but exact compatible plugin duration, drum engine, retention and transition continuity unknown. With Foot Nav enabled,left previous/right next board; LCDs show adjacent names and LED blinks during loading. Chromatic tuner documented. [Guide](https://wiki.mod.audio/wiki/MOD_Duo_User_Guide);[navigation](#duo--os-110-lcd-navigation-and-file-loading-scope). |
| Routing / bypass / tails | Physical input1→output1,input2→output2 bypass, enabled powered-off and disabled after board loads; independent channel bypass. Convolution Loader Trails controls its own bypass decay, not global volume/preset spillover. Headphone/loop bypass coverage unknown. [Device settings](#device-settings--os-113-scope);[plugin](#duo--plugin-specific-ir-import-and-tail-behavior). |
| Used IDR | No exact condition-qualified Shopee Indonesia hardware ask established; unknown is not unavailable. |
| New IDR | No exact condition-qualified Shopee Indonesia hardware ask established. No sibling price, currency conversion, discount or stock inferred. |

<!-- comparison evidence ends -->

### Duo — partial LCD discovery

Checked **2026-11-01**; **partial lead outside active models and brand counts**. Original MOD Duo,not Duo X orDwarf. Manufacturer-hosted wiki documentation is evidence below;community forum specifications are not promoted. No ownership assertion.

| Field | Evidence / qualification |
|---|---|
| Display / conflict | [Own technical specification](https://wiki.mod.audio/wiki/MOD_Duo_Technical_Specs),last edited2025-12-15,lists **two2.7-inch LCDs**. [Own user guide](https://wiki.mod.audio/wiki/MOD_Duo_User_Guide) says **two2.8-inch LCDs**,showing actuator/menu/tuner information. Preserve the disagreement;exact diagonal/color/touch unresolved. One dedicated label display above each footswitch is not yet established by inspected text. No visual inspection. |
| Controls / navigation | User guide explicitly identifies **two push knobs andtwo footswitches**. Separate-button census pending. When bank navigation is enabled,left foot loads previous pedalboard,right loads next. Plugin assignments are another mode. |
| Expression / direct analog | User guide explicitly says **no direct expression-pedal port**. MIDI converters orControlChain adapters are separate hardware;they do not satisfy the requested direct analog path. Global analog-volume assignment/range/recall therefore N/A for that absent path;other controller coverage unverified. |
| Dimensions / footprint | Both pages give **160mm width,186mm length,75mm height**. Retain length axis;either orientation exceeds140mm depth. Mass initially unknown;own product now lists1.2kg withconflictingdimensions;[qualified follow-up](#duo--manufacturer-product-page-dimensions-and-instrument-scope). |
| Audio I/O | Technical page lists two independent **TS,1MΩ inputs**,two balanced-compatibleTRS outputs,and6.35mmTRS headphones. A later generic sentence calls every input/outputTRS;preserve this connector inconsistency rather than override the explicit input list. |
| Headphones / levels | Technical page:phones **+12…−33dB**,outputs **0…−127dB in0.5dB steps**. User guide:phones normally monitoroutputs1/2,withdirect-input monitoring option andindependent volume. These are not expression assignments orverified mute endpoints. |
| USB / MIDI | Technical page:USB2.0 TypeA host,max500mA output;TypeB device;five-pinDIN MIDI in/out. Host-current rating is notunit draw. Guide usesTypeB fornetwork WebGUI/manualupdate,TypeA forUSB-MIDI/Bluetooth adapter;USB audio/power remain unverified. |
| Power / source inconsistency | User guide specifies **12VDC,center-positive,2A supplied adapter**,5.5×2.1×10mm plug. It also says at least **12W,1.5A**;retain both figures without reconciling their arithmetic orinferring measured draw. Peripherals change requirements. Battery/USB operation unknown. |
| Editing / operation | Guide documents built-in browser WebGUI viaUSB network,withChrome/Safari/Firefox examples;Bluetooth requires adapter. Standalone playing after setup doesnot require computer. Exact OS compatibility andcurrent firmware scope pending. |
| Processing / memory / formats | Modular plugin architecture documented;complete category choices,simultaneous DSP limits,factory/user memory,synth/acoustic,IR/nativeNAM/convertedNAM/capture,looper/drums remain unverified. Storage capacity is notpreset capacity. The earlier IR unknown is narrowed bythe [Duo-applicable Convolution Loader](#duo--plugin-specific-ir-import-and-tail-behavior);other format/plugin applicability remains open. |
| Used / new IDR | No exact Shopee hardware offer established by2026-11-01 searches. No exchange rate,used discount orrelated-model price inferred;unknown is notunavailable. |

Technical page also gives24-bit48kHz ADC/DAC;this is notUSB stream-format proof. [Manufacturer-hosted developer page](https://wiki.mod.audio/wiki/Developers) lists4GB flash forDuo,versus8GB ontechnical page;revision basis unresolved. Do notborrow Duo X CV-expression sockets orDwarf features.

### Device settings — OS 1.13 scope

The [Duo device-settings guide](https://wiki.mod.audio/wiki/MOD_Duo_Device_Settings), explicitly for OS 1.13, describes the left LCD as the main menu and the right LCD as its submenu. This establishes menu roles, not a dedicated label above each footswitch.

Four user profiles A–D store input, output and sync/MIDI settings; they are not four pedalboard slots. Saving a pedalboard stores its plugin parameters; reset or reload restores that saved state. Neither feature establishes a global expression-volume assignment. Banks and current-pedalboard settings require disconnection from the computer.

Hardware bypass connects each input directly to its corresponding output, engages while powered off and disengages after the pedalboard loads. Each channel can also be bypassed separately. Headphone, effect-tail and looper coverage through this bypass remains unverified.

### Duo — footswitch assignments and snapshot scope

Checked **2026-11-01** against the manufacturer-hosted [WebGUI guide for OS 1.13](https://wiki.mod.audio/wiki/MOD_Web_GUI_User_Guide), including its explicit **MOD Duo** assignment subsection. Knobs can hold multiple parameter assignments; each footswitch holds only one. This is not evidence of a single switch directly toggling multiple arbitrary plugin parameters. A snapshot-list assignment is a separate documented route to changing several saved settings.

Snapshots store parameter states inside a pedalboard and switch those states without reloading the board. After creating or editing a snapshot, the containing pedalboard must also be saved or the changes are lost. WebGUI snapshot lists cannot be reordered in the documented revision. No numerical snapshot capacity, guaranteed gapless switching, tail/looper continuity or global across-pedalboard assignment is established. Dwarf-specific on-device saving/reordering is not borrowed for Duo.

### Duo — processing architecture and resource limits

Checked **2026-11-01**. The [manufacturer-hosted developer reference](https://wiki.mod.audio/wiki/Developers) describes LV2 plugins hosted through JACK/mod-host, with a dual-core Cortex A7 running at a fixed **912 MHz**. The [own technical page](https://wiki.mod.audio/wiki/MOD_Duo_Technical_Specs) instead lists **dual-core ARM A7 1.0 GHz**, **1 GB RAM and 8 GB flash**; the developer reference separately lists **4 GB flash** as preserved above. Rated-versus-operating clock may explain the numbers, but neither document establishes that reconciliation or a hardware-revision mapping.

The [OS 1.13 WebGUI guide](https://wiki.mod.audio/wiki/MOD_Web_GUI_User_Guide) says individual plugins consume different CPU/RAM resources. Its Advanced Audio Server option allows a **256-frame buffer** for heavier processing at increased latency; this is not a guaranteed effect-count increase. No fixed arbitrary-plugin concurrency, complete installed category census or preset capacity is established. Shared file-manager folders for IRs/models alone do not certify a particular Duo-compatible IR/NAM/capture plugin.

### Duo — manufacturer product-page dimensions and instrument scope

Checked **2026-11-01**, [exact original Duo manufacturer page](https://mod.audio/mod-duo/),not Duo X orDwarf. It gives **180W×160D×74.7H mm;1.2kg**,contrasting with the wiki’s **160W×186L×75H mm**. Neither published footprint meets200W×140D;revision/measurement basis remains unresolved. The mass is a manufacturer claim,not a measurement.

The page explicitly names **guitar,bass andvoice simultaneously with independent channels**,and MIDI-controlled virtual instruments. This establishes advertised instrument scope,not a microphone/phantom specification,polyphonic guitar tracking orautomatic electric-to-acoustic conversion. Its routing description explicitly permits **split,join andfeedback paths** across two independent audio channels.

“Over400 free plugins” describes available effects,amps,instruments andMIDI utilities,not installed contents,400 distinct guitar algorithms orsimultaneous capacity. The supplied adapter’s **100–240VAC,50–60Hz** input range is separate from the already-documented12VDC unit supply anddoes not resolve the guide’s current/wattage discrepancy. No local download ordevice operation. LCD placement anddirect-analog-expression failure remain unchanged.

### Duo — plugin-specific IR import and tail behavior

Checked **2026-11-01**, [MOD/DISTRHO Convolution Loader entry](https://pedalboards.mod.audio/plugins/aHR0cHM6Ly9tb2QuYXVkaW8vcGx1Z2lucy9Db252b2x1dGlvbkxvYWRlcg==),listed **v1:2.0-23**. It explicitly names **MOD Duo**:user IR loading is supported,with a lower maximum than the **15seconds for Duo X/Dwarf**;the original Duo’s numerical maximum is not published there. Files may be **WAV orFLAC**,with48kHz/24-bit WAV recommended for loading speed,not stated as the only accepted format. Multichannel files are processed in stereo.

Its **Trails** setting preserves reverb decay on plugin bypass when enabled;disabling it cuts the tail. Dry/Wet each span−60…0dB;High Pass0…500Hz. These are plugin parameters,not a global expression-volume range,whole-device bypass orpreset-change spillover guarantee.

[Wiki File handling](https://wiki.mod.audio/wiki/File_handling),last editedDecember1,2025,also retains a **2048-sample IR-file limit**,while listing larger-reverb IR plugins. Preserve that generic-page versus plugin-specific scope conflict;do not impose2048samples on every loader. Its AIDA/NAM folder listing still does not verify original-Duo model architecture compatibility.

### Duo — OS 1.10 LCD navigation and file-loading scope

[Manufacturer OS1.10 announcement](https://mod.audio/mod-mod-os-update/),shown withApril7,2021/February27,2023 date labels,explicitly includes Duo. It introduces user cabinet-IR loading andaudio/MIDI file players. **Momentary footswitch mode** andlist-parameter LED-color cycling are documented;LED colors do not establish color LCDs.

Duo-specific changes add pedalboard/snapshot names to display headers. Foot-navigation readouts show **previous/next pedalboard names**,withLED blinking until loading finishes. This resolves a practical readout detail,not exact physical LCD-to-foot placement orzero-latency switching. The new LV2 State extension enables plugins to implement persistent data,but does not guarantee every looper saves recordings afterpower-off. No files,plugins orfirmware downloaded;no device operation.

### Duo — neural-model file acceptance versus playback compatibility

Checked **2026-11-01**. [Manufacturer-hosted release history](https://wiki.mod.audio/wiki/Releases),**1.13.2,June28,2023**,adds acceptance of **.aidax/.nam extensions**. This establishes a file-handling change,not supported model architectures,CPU feasibility ornative-versus-converted playback on original Duo.

The [MOD-hosted Neural Amp Modeler plugin entry](https://pedalboards.moddevices.com/plugins/aHR0cDovL2dpdGh1Yi5jb20vbWlrZW9saXBoYW50L25ldXJhbC1hbXAtbW9kZWxlci1sdjI=) lists **v1:2.3-19**,NAM andRTNeural Keras/AIDA-X models. The [upstream developer README](https://github.com/mikeoliphant/neural-amp-modeler-lv2) now describes **NAM A1/A2 plusRTNeural JSON**,atom:Path host support andmatching host/model sample rates;even-multiple oversampling is the stated exception. The README is a current upstream scope,not certification of that listed store build orDuo-specific operation.

MOD’s [AIDA-X page](https://mod.audio/aida-x/) explicitly advertises **Dwarf andcomputers**;its [neural-modeling page](https://mod.audio/neural-modelling/) likewise names **Dwarf** forAIDA-X/NAM. Omission does not prove original Duo incompatibility. **Original-Duo native NAM,converted NAM,AIDA-X andcapture playback remain unverified**;Dwarf marketing,shared resource folders andblank Duo cells in a community CPU table are insufficient. At that checkpoint the manufacturer build-recipe page exposed metadata butnot readable source;the follow-up below resolves source access without claiming a build result. No clone,download,training,plugin installation ordevice operation.

### Duo — manufacturer NAM build configuration and provenance

Checked **2026-11-01** by reading the [manufacturer’s build recipe](https://raw.githubusercontent.com/mod-audio/mod-plugin-builder/master/plugins/package/neural-amp-modeler-lv2/neural-amp-modeler-lv2.mk) remotely;no code executed. It pins the MOD fork to **9574e74a8eddcd54a5c65c5748e3ff226c7c4f55**. This resolves the earlier unreadable-source access gap only.

| Evidence | Build-time scope / qualification |
|---|---|
| NAM versus RTNeural | **BUILD_NAMCORE=ON;BUILD_RTNEURAL=OFF;BUILD_STATIC_RTNEURAL=OFF**. The store’s generic RTNeural/AIDA-X description andupstream JSON support therefore cannot certify those backends in this configured build. AIDA-X has a separate package. |
| Architectures / defaults | **NAM_ENABLE_A2_FAST=ON**,internal static WaveNet/LSTM enabled;**DEFAULT_QUALITY_SCALE=0.49**. These are configuration requests,not a tested model-architecture matrix,measured quality orDuo performance result. |
| Bypass | **SMART_BYPASS_ENABLED=OFF**. Do not infer upstream optional silence-triggered processing bypass for this configuration,orwhole-device relay/volume behavior. |

The [separate manufacturer AIDA-X recipe](https://raw.githubusercontent.com/mod-audio/mod-plugin-builder/master/plugins/package/aidadsp-lv2/aidadsp-lv2.mk) pins **f86e21dcb3b481246f0406c5f003f1a0c7d93d37**,bundle **rt-neural-generic.lv2**,withRTNEURAL_EIGEN enabled. This is distinct from enabling RTNeural in the NAM package. Neither recipe establishes successful original-Duo compilation,store-binary provenance,installed firmware orusable CPU headroom.

The [MOD Live-USB project](https://github.com/mod-audio/mod-live-usb) targets a PC-hosted MOD environment. Its plugin list andmodduo-new naming are not by themselves original-Duo hardware playback proof. Original-Duo native/converted NAM andAIDA-X playback remain unknown. No clone,download,build,workflow use ordevice test.

Next:establish LCD-to-actuator placement fromprimary text orinspectable originalpanel,verify complete profile andexact hardware offers before active admission. No files,software,firmware,plugins ordependencies downloaded;no device operation.
