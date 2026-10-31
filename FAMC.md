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

## Liquid Foot JR+ — pending controller lead

Checked **2026-11-01**. Distinct from the original Liquid-Foot Jr., Mini, 12+ and Pro+. Controller only; outside active audio-processor counts and confirmed individual-LCD matches.

The [manufacturer LF+ series guide reproduction](https://manualzz.com/doc/23278544/famc-liquid-foot---series-12--12---jr---pro--midi-control...) explicitly names JR+ and gives it different page-menu button combinations from 12/12+/Pro+. However, the guide’s explicit LCD-above-each-button example identifies **12+**; the host’s JR+ manual title is not an exact JR+ screen census. Do not transfer the 12+ display count, dimensions or power requirements.

An [exact JR+ used-hardware listing](https://reverb.com/item/86977433-famc-liquid-foot-jr-midi-foot-controller-liquid-foot-jr), Charlies Gear Depot, Irvine, US, is marked **sold / Used–Excellent**. It describes eight buttons and LCD labels above each button, with **2×8 characters**, and says this text was copied from FAMC’s website. That attribution has not been independently authenticated: the manufacturer homepage was inaccessible. Its phrase “seven color LCD” is not treated as a count of seven screens or proof of full-color pixels. A [separate exact JR+ seller](https://reverb.com/item/15764729-famc-liquid-foot-jr-midi-controller) instead calls the button screens LED; retain the LCD/LED terminology conflict as seller-level evidence. No foreign asking price converted to IDR.

Targeted Shopee Indonesia search found no qualified exact hardware offer; new/used IDR, stock, bundle, warranty and delivered total remain unknown. Remaining: primary exact-model display count/technology/diagonal, full controls/ports, body/mass, power, expression wiring and current editor support. No local download, device operation or visual screen count.

## Liquid Foot Pro+ — pending controller lead

Checked **2026-10-31**;distinct from original Liquid Foot Pro and12+. [Manufacturer LF+ manual reproduction](https://manualzz.com/doc/27981410/famc-pro--user-manual),printedpp5,18,85,explicitly names Pro+ anddescribes shared interface/display functions. Undated document;host’s Pro+ title alone does not certify model-specific physical specifications. Its interface description onprintedp18 still numbers only1–12;that is not a full Pro+ hardware census.

[Exact Pro+ used-hardware seller](https://www.amusicstoreonmainstreet.com/shop/Electronics/Effects-PedalsProcessors/p/Used-FAMC-Liquid-Foot-Series-Pro-MIDI-Foot-Contoller.htm) claims **24 switches with individual multicolored LCDs**,plus main LCD. Treat count,placement andtechnology as **seller leads**,not manufacturer verification. Its supply/editor claims are likewise unadopted. No foreign price converted to IDR.

Manufacturer product endpoint was inaccessible;targeted Shopee Indonesia searches found no qualified exact offer. This does not establish market absence. Remaining:primary exact-model screen census,dimensions/weight,power,complete ports,current editor/firmware andcondition-qualified IDR hardware offers. Controller only;outside active processor/brand counts andconfirmed-LCD table. No local download ordevice test.

### Liquid Foot Pro+ — shared-guide capacity and page-count conflict

Checked **2026-11-01** in the [manufacturer-authored LF+ series guide reproduction](https://manualzz.com/doc/27981410/famc-pro--user-manual), printed pp5–7,18. FAMC website references, LF+ family naming and the explicit Pro+ interface subsection corroborate identity. This is an undated shared guide, not an exact Pro+ hardware specification sheet or current firmware test.

| Field | Historical guide evidence / qualification |
|---|---|
| Memory / page conflict | Introduction p5 says **50 pages**; feature summary p7 says **60 pages**. Preserve both; no firmware or model mapping is established. |
| Controls / logical versus physical buttons | Page definitions address up to **60 button positions**, each with **two functions (120 function positions)**. The guide expressly says the controller itself does not have60 switches: MIDI, expanders and other LF+ units extend access. This is not a physical Pro+ switch/LCD count. |
| Memory / controller libraries | Summary p7 lists **384 presets,254 songs,128 setlists (up to60 songs each),180 IA slots,254 stored SysEx messages (16bytes each, linkable)**. Songs group up to24 presets. These are MIDI-controller structures, not audio presets, simultaneous effects, factory occupancy or a verified current capacity. |

Exact Pro+ LCD census and physical specifications remain unresolved. The manufacturer homepage was inaccessible again; seller/secondary tables are not promoted to manufacturer evidence. No local download, software installation or device operation.
