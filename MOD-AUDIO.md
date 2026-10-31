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
| Dimensions / footprint | Both pages give **160mm width,186mm length,75mm height**. Retain length axis;either orientation exceeds140mm depth. Mass unknown. |
| Audio I/O | Technical page lists two independent **TS,1MΩ inputs**,two balanced-compatibleTRS outputs,and6.35mmTRS headphones. A later generic sentence calls every input/outputTRS;preserve this connector inconsistency rather than override the explicit input list. |
| Headphones / levels | Technical page:phones **+12…−33dB**,outputs **0…−127dB in0.5dB steps**. User guide:phones normally monitoroutputs1/2,withdirect-input monitoring option andindependent volume. These are not expression assignments orverified mute endpoints. |
| USB / MIDI | Technical page:USB2.0 TypeA host,max500mA output;TypeB device;five-pinDIN MIDI in/out. Host-current rating is notunit draw. Guide usesTypeB fornetwork WebGUI/manualupdate,TypeA forUSB-MIDI/Bluetooth adapter;USB audio/power remain unverified. |
| Power / source inconsistency | User guide specifies **12VDC,center-positive,2A supplied adapter**,5.5×2.1×10mm plug. It also says at least **12W,1.5A**;retain both figures without reconciling their arithmetic orinferring measured draw. Peripherals change requirements. Battery/USB operation unknown. |
| Editing / operation | Guide documents built-in browser WebGUI viaUSB network,withChrome/Safari/Firefox examples;Bluetooth requires adapter. Standalone playing after setup doesnot require computer. Exact OS compatibility andcurrent firmware scope pending. |
| Processing / memory / formats | Modular plugin architecture documented;complete category choices,simultaneous DSP limits,factory/user memory,synth/acoustic,IR/nativeNAM/convertedNAM/capture,looper/drums remain unverified. Storage capacity is notpreset capacity. |
| Used / new IDR | No exact Shopee hardware offer established by2026-11-01 searches. No exchange rate,used discount orrelated-model price inferred;unknown is notunavailable. |

Technical page also gives24-bit48kHz ADC/DAC;this is notUSB stream-format proof. [Manufacturer-hosted developer page](https://wiki.mod.audio/wiki/Developers) lists4GB flash forDuo,versus8GB ontechnical page;revision basis unresolved. Do notborrow Duo X CV-expression sockets orDwarf features.

### Device settings — OS 1.13 scope

The [Duo device-settings guide](https://wiki.mod.audio/wiki/MOD_Duo_Device_Settings), explicitly for OS 1.13, describes the left LCD as the main menu and the right LCD as its submenu. This establishes menu roles, not a dedicated label above each footswitch.

Four user profiles A–D store input, output and sync/MIDI settings; they are not four pedalboard slots. Saving a pedalboard stores its plugin parameters; reset or reload restores that saved state. Neither feature establishes a global expression-volume assignment. Banks and current-pedalboard settings require disconnection from the computer.

Hardware bypass connects each input directly to its corresponding output, engages while powered off and disengages after the pedalboard loads. Each channel can also be bypassed separately. Headphone, effect-tail and looper coverage through this bypass remains unverified.

### Duo — footswitch assignments and snapshot scope

Checked **2026-11-01** against the manufacturer-hosted [WebGUI guide for OS 1.13](https://wiki.mod.audio/wiki/MOD_Web_GUI_User_Guide), including its explicit **MOD Duo** assignment subsection. Knobs can hold multiple parameter assignments; each footswitch holds only one. This is not evidence of a single switch directly toggling multiple arbitrary plugin parameters. A snapshot-list assignment is a separate documented route to changing several saved settings.

Snapshots store parameter states inside a pedalboard and switch those states without reloading the board. After creating or editing a snapshot, the containing pedalboard must also be saved or the changes are lost. WebGUI snapshot lists cannot be reordered in the documented revision. No numerical snapshot capacity, guaranteed gapless switching, tail/looper continuity or global across-pedalboard assignment is established. Dwarf-specific on-device saving/reordering is not borrowed for Duo.

Next:establish LCD-to-actuator placement fromprimary text orinspectable originalpanel,verify complete profile andexact hardware offers before active admission. No files,software,firmware,plugins ordependencies downloaded;no device operation.
