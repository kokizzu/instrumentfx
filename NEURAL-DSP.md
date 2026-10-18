# Neural DSP multi-effects

[Expression-volume comparison](EXPRESSION-VOLUME.md) · [Guitar inventory](ALL-GUITAR.md)

## Nano Cortex

**Expression-volume capability supplement, checked 2026-10-18 against the official NanOS 2.2.0 HTML manual.** Nano Cortex already exists in the catalogue: this is not a new inventory item. Its earlier full technical record remains in [advanced modelers](effects/advanced-modelers.md); no legacy content is deleted or represented as fully consolidated.

| Capability field | Verified finding / explicit uncertainty |
|---|---|
| Built-in expression | No treadle; the complete Overview shows external control rather than a built-in pedal. |
| External analog EXP | Yes, shared EXP/MIDI input. In app Settings, select EXPRESSION PEDAL; use a compatible TRS controller and calibrate heel/toe. The manual explicitly distinguishes a TRS expression output from audio wah/volume outputs, which are not supported. |
| Volume-related target | Expression Parameter Range section lists GAIN, BASS, MID, TREBLE, AMOUNT and **LEVEL**. The Global Controls section separately identifies the LEVEL knob as main-output master volume; the headphone level has a separate rear control. These statements establish a documented level-control lead, not an all-output/all-preset guarantee. |
| Assignment scope | **UNVERIFIED global assignment.** The inspected Expression Pedal Configuration section explains assignments and calibration persistence but does not explicitly establish a single level assignment applying to every preset without individual setup. Do not turn global calibration or the section title Global Controls into proof of global mapping. |
| Headphone behavior | Dedicated HP output is documented. Whether expression-mapped LEVEL controls HP level as well as main outputs is **unverified**; separate HP OUT knob is documented. |
| Size / weight | **144 × 103 × 62 mm; 620 g**. Chassis fits 200 × 140 mm; connected plugs add clearance. |
| Normal guitar pickup | Yes, normal instrument INPUT; no divided pickup required. |
| Preset switching | Manual describes 2-Preset and 4-Preset operation. Do not automatically describe its default two-switch behavior as unrestricted preset-down/up. |
| Power relevant to compact use | **9–12 V DC, center-negative, at least 600 mA**, or **USB-C 5 V / 1.5 A**. These are manufacturer supply requirements, not measured consumption. |
| Research verdict | **Not a confirmed buy for global pedal volume.** Direct EXP and a level target are documented, but cross-preset assignment persistence, exact target behavior and headphone coverage require model/firmware-specific confirmation. |

### Sources

[Official Nano Cortex User Manual 2.2.0](https://neuraldsp.com/manual/nano-cortex): Overview; Connecting your Gear; Global Controls; Performance Mode; Expression Pedal Configuration; Device Settings; Hardware Specifications. This is an accessible manufacturer HTML manual, not an inferred feature from forum complaints or a retailer.

### Remaining tasks

Verify on NanOS 2.2.0 whether LEVEL in the expression target list refers to final main-output gain, establish assignment storage scope explicitly, test changing at least three presets with the pedal held at heel/middle/toe, and separately verify HP behavior. No hands-on test is claimed. Refresh exact Shopee hardware offers, separate used/new IDR, condition and stock. Existing broader specification/price gaps in the legacy record remain unresolved.
