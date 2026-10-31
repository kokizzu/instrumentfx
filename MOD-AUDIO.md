# MOD Audio — multi-effects discovery

[Repository](README.md) · [Footswitch displays](FOOTSWITCH-DISPLAYS.md)

<!-- brand-index begins -->
**Model and section index — A–Z, natural numeric order**

- [Duo — partial LCD discovery](#duo--partial-lcd-discovery)
<!-- brand-index ends -->

## Duo — partial LCD discovery

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

Next:establish LCD-to-actuator placement fromprimary text orinspectable originalpanel,verify complete profile andexact hardware offers before active admission. No files,software,firmware,plugins ordependencies downloaded;no device operation.
