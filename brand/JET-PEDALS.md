# JET Pedals — controllers and loop switchers

[Repository](../README.md) · [Footswitch displays](../FOOTSWITCH-DISPLAYS.md)

<!-- brand-index begins -->
**Model and section index — A–Z, natural numeric order**

- [Unity6 — partial controller discovery](#unity6--partial-controller-discovery)
<!-- brand-index ends -->

## Unity6 — partial controller discovery

Checked **2026-11-06**. Controller/analog-loop switcher, **outside402 active audio processors**. Ownership unverified;not a newly verified synth/pitch/instrument multi-effects engine.

### Manufacturer hardware and display evidence

[Product page](https://jetpedals.com/collections/midi-control/products/unity6): shared main touchscreen anddedicated per-switch scribble strips with selectable colors/on-off indicators. **LCD/OLED,diagonals,resolution,touch on strips andexact strip count unverified**. Text names four preset switches,a rotary/push dial anddedicated Tap switch;complete physical census uninspected.

Mono input/output;three TRS send/return pairs provide six mono loops using insert cables,with bank-specific reordering. Four configurable UniPorts support EXP,TRS MIDI,tap/amp/JHS switching;five-pin MIDI input/output with optionalThru. Wi-Fi browser editor andBluetooth MIDI are separate fromUSB audio. Fullconnector inventory,USB,battery,headphones andunitmass remain unverified.

[Dimensions/power documentation,revision1](https://docs.jetpedals.com/books/unity6/page/dimensions-power-requirements): **7W×5D×3.5H inches**,derived **177.8×127×88.9mm**;**200mA draw**,isolated **9VDC negative-tip** supply. Connector diameter unknown. No measurement ordownload.

### Memory, expression and firmware scope

[Manufacturer features,revision4](https://docs.jetpedals.com/books/unity6/page/description-features):127banks×5presets;32MIDI messages/preset,16onbank activation;up toeight messages perEXP1/2 withprogrammable endpoints. Six analogloops are notsixDSP effects. Factoryfilling andpresetsave limits unverified.

[Firmware history](https://jetpedals.com/pages/unity6-firmware-updates): **2.0.0,2024-11-20** introduces Expression-to-Volume saved **per bank**. This doesnot establish global all-bank assignment oranalog attenuation coverage. Product’s built-in-expression-pedal wording is ambiguous;do not infer an onboard treadle from it. **2.3.0,2025-04-16** adds automatic strip-text sizing;**2.5.0,2025-08-14** adds active-preset strip feedback. Toplisted **3.0.0,2026-07-16** adds fullprogramming/global backup/restore andbank exports;not installedfirmware evidence. No package downloaded orhardware operated.

### UniPort wiring and bank-scoped expression

Checked **2026-11-06**. [Manufacturer UniPorts page, revision10](https://docs.jetpedals.com/books/unity6/page/uniports), specifies a **¼-inch TRS cable** and a pedal that receives on **tip** and returns to Unity6 on **ring**. **EXP1 only uses UniPort1; EXP2 only uses UniPort2**. Resistance, taper, sleeve wiring and toe-switch compatibility are not specified here. Do not infer arbitrary pedal compatibility or a direct analog expression output from the socket.

Other port modes are MIDI Type A, Type B, Tip Active and Ring Active; these are MIDI choices, not the analog EXP pinout. External tap uses TS and normally-open switching; the four ports can use different tap divisions. JHS Red Remote and amp-switch modes also use TS; amp switching requires normally-open compatibility. These are alternative port roles, not simultaneous outputs from one socket.

[Expression Pedals, revision2](https://docs.jetpedals.com/books/unity6/page/expression-pedals): each pedal can send up to **eight simultaneous MIDI messages**, saved **per bank**, with separate minimum/maximum values per message. The example maps a displayed minimum50 to transmitted CC value64, and toe-down to127. These are MIDI values, not dB, mute depth or proof of global analog-volume assignment. Calibration, held-position recall and analog-output/tail coverage remain unverified; no cable or device tested.

### Market and continuation

Exact Shopee Indonesia search recovered no seller/item-qualified Unity6 hardware. Used/new IDR,condition,variant,bundle,stock,warranty,voucher,shipping/tax andcheckout unknown;foreigncurrency listings notconverted. Remains asecondary controller lead withunverified striptechnology/count,not a confirmedindividualLCD audio processor. Continue primary LCDprocessor/Shopee priorities;preserve expression andGT-Pro/general queues.
