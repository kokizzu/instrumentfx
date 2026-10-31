# FAMC

[Footswitch displays](FOOTSWITCH-DISPLAYS.md) · [Repository](README.md)

## Liquid Foot 12+ — controller

Partial controller lead,checked **2026-10-31**. [Manufacturer-authored LF+ series guide reproduction](https://manualzz.com/doc/23278544/famc-liquid-foot---series-12--12---jr---pro--midi-control...),original text pp5,8,18,76,78–80. It names FAMCmusic.com and expressly distinguishes **12+** from LED-only **12**. Undated guide;firmware1.68 appears as an example,not verified current firmware. Manufacturer homepage was inaccessible. Generated FAQs and seller descriptions were not used.

| Field | Archived evidence / qualification |
|---|---|
| Display / layout | **LCD above each button** on12+ (p76);p18 numbers buttons1–12,supporting twelve switch displays. Separate main LCD. Diagonal,pixel resolution,touch and pixel-color depth unknown;colored backgrounds do not establish full-color graphics. |
| Display / controls | Main and button-LCD contrast controls are separate. Button readouts can devote line2 to a second function;an option clears inactive IA labels. Adjustment endpoints unverified. |
| Expression / wiring | Four external ports;TRS,5–25kΩ potentiometer;**tip=wiper,ring=toe end,sleeve=heel end**. This converts pedal movement into MIDI control;it does not supply analog audio-volume processing. |

Not an audio multi-effects processor;excluded from active model/brand counts. Dimensions,weight,dedicated supply requirements,complete controls/current editor support andqualified Shopee hardware offers remain unresolved. No files downloaded ordevice operated.

### Liquid Foot12+ — MIDI power and pedal recall

Same archived manufacturer guide,printed pp9,41:

- MIDI OUT accepts5/7-pin connections;optional THRU repeats MIDI IN. Pins6/7 receive phantom power:guide specifies9–12V AC/DC,at least800mA per connected LF+. This does not establish dedicated DC-jack polarity oradapter specifications. Do not power other devices from this port.
- MIDI IN can instead enter through the combined OUT connection;the separate MIDI IN must then remain disconnected.
- Expansion A/B uses CAT-5 cable with proprietary signals;it is not Ethernet and is incompatible with original LF PRO.
- **EXP PDL Resend defaults No** and is a per-preset option to retransmit current continuous-controller pedal values. It does not establish automatic host volume assignment across presets.

No powered connection orhardware test performed;current firmware behavior remains unverified.

## Liquid Foot Pro+ — pending controller lead

Checked **2026-10-31**;distinct from original Liquid Foot Pro and12+. [Manufacturer LF+ manual reproduction](https://manualzz.com/doc/27981410/famc-pro--user-manual),printedpp5,18,85,explicitly names Pro+ anddescribes shared interface/display functions. Undated document;host’s Pro+ title alone does not certify model-specific physical specifications. Its18-page interface description still numbers only1–12;that is not a full Pro+ hardware census.

[Exact Pro+ used-hardware seller](https://www.amusicstoreonmainstreet.com/shop/Electronics/Effects-PedalsProcessors/p/Used-FAMC-Liquid-Foot-Series-Pro-MIDI-Foot-Contoller.htm) claims **24 switches with individual multicolored LCDs**,plus main LCD. Treat count,placement andtechnology as **seller leads**,not manufacturer verification. Its supply/editor claims are likewise unadopted. No foreign price converted to IDR.

Manufacturer product endpoint was inaccessible;targeted Shopee Indonesia searches found no qualified exact offer. This does not establish market absence. Remaining:primary exact-model screen census,dimensions/weight,power,complete ports,current editor/firmware andcondition-qualified IDR hardware offers. Controller only;outside active processor/brand counts andconfirmed-LCD table. No local download ordevice test.
