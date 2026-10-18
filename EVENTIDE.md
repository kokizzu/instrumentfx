# Eventide multi-effects

[Expression-volume comparison](EXPRESSION-VOLUME.md) · [Guitar inventory](ALL-GUITAR.md)

## H90

**Capability-focused partial profile, checked 2026-10-18.** New research lead for normal-pickup guitar/bass processing without a built-in expression treadle. This is not an H9, H9 Max or H9 Gen 2 record. Full inventory admission/count reconciliation is pending; this supplement does not claim every required field is verified.

| Field | Verified finding / qualification |
|---|---|
| Built-in expression | No built-in treadle; external controllers connect separately. [H90-P, H90-IO] |
| External expression | Two 6.35 mm TRS EXP/CTL inputs; select expression rather than switch and calibrate in System > I/O. Do not assume a particular M-VAVE pedal's polarity or resistance is compatible without checking. [H90-P, H90-IO] |
| Volume target | **P Out Gain**, the Program output gain, is explicitly present in the Global Mapping Chart. P In Gain is a separate pre-processing option. A/B Out Gain affects only one algorithm, and P Mix is not master volume. [H90-MAP] |
| Assignment scope | **Documented GLOBAL**: Global Pedal Control applies regardless of which Program is loaded. No per-Program volume block is required to establish this mapping. [H90-G, H90-MAP] |
| Setup | Set EXP/CTL 1 or 2 to expression and calibrate in System > I/O; then System > Global > Pedal Control, choose P Out Gain and the connected expression source. Verify desired heel/toe gain range at low monitoring volume. [H90-IO, H90-G, H90-MAP] |
| Volume limitations | Numerical gain range, full heel-down mute, and behavior during every Program-transition case remain to be checked. **Relay bypass directly connects input to output**, so do not promise DSP gain control in relay bypass. Prefer checking DSP bypass behavior for this application. In Dual Routing, confirm which signal path is affected rather than assuming one mapping controls both instruments. [H90-G] |
| Normal pickup input | Yes, instrument/line-level operation; four 6.35 mm TS inputs and four outputs. No divided pickup is required. [H90-P] |
| Dimensions / mass | Manufacturer metric specification **170 W × 136 D × 68 H mm; 0.84 kg**. Fits the 200 × 140 mm chassis filter; connected plugs require extra clearance. Published imperial dimensions are rounded and not used to override the metric specification. [H90-P] |
| Headphones | **No dedicated headphone output** in the complete connector specification. Main outputs' recommended load is 10 kΩ; do not represent them as a verified headphone amplifier. [H90-P] |
| Processing | **Two algorithms simultaneously**, serial/parallel, two mono or one stereo insert, or two independent stereo paths. Current product page advertises 74 algorithms; this is not 74 simultaneous blocks. Complete per-category counts remain unverified. [H90-P] |
| Controls / screen | Manufacturer describes five push knobs, seven LED buttons and an OLED screen. Physical footswitch count versus six assignable performance functions, published screen diagonal, color/monochrome and touch specifications still need a complete hardware pass. [H90-P] |
| Other I/O | MIDI DIN In and Out/Thru; USB-C for control, updates and MIDI. USB connector alone is not evidence of USB audio or bus-powered operation. [H90-P] |
| Power | **12 V DC, 1 A supply, center-positive, 5.5/2.5 mm connector**. This is not a typical 9 V center-negative pedal supply. Battery operation and measured consumption are not established here. [H90-P] |
| Software | Eventide Control for Mac, PC and iPad; product page documents USB/Bluetooth connection. Checked download page lists Eventide Control 2.2.0 and H90 firmware requirement 1.9.4+. This is not a claim about any user's installed firmware. [H90-P, H90-D] |
| Remaining full-profile fields | Factory/user/total memory, complete effect-category inventory, screen details, IR/NAM/capture loading, acoustic simulation, full looper specifications, and separate condition-verified used/new IDR offers. Synth and vocal algorithm names appear on the official page, but a complete category assessment is not yet made. |

### H90 — Indonesian availability

**Shopee hardware price and live stock: unverified.** Searches on 2026-10-18 returned unrelated EZVIZ H90 cameras and non-Indonesian retailers; those are not pedal offers and are excluded. Do not convert the manufacturer's foreign price into a guessed IDR quote. No new/used market range is asserted.

### H90 — sources

- [H90-P] [Official product, features and complete connector/metric specifications](https://www.eventideaudio.com/pedals/h90/).
- [H90-G] [Official H90 manual 1.9.7, System > Global: Pedal Control and bypass behavior](https://cdn.eventideaudio.com/manuals/h90/1.9.7/content/system-menu/global.html).
- [H90-MAP] [Official Global Mapping Chart: P Out Gain and assignment across Programs](https://cdn.eventideaudio.com/manuals/h90/1.9.7/content/appendix/global.html).
- [H90-IO] [Official I/O settings: expression mode and calibration](https://cdn.eventideaudio.com/manuals/h90/1.9.7/content/system-menu/io.html).
- [H90-D] [Official downloads and version requirements](https://www.eventideaudio.com/downloads/?product=H90).

These HTML manual pages were read directly; no PDF rendering or hands-on test is claimed. The global mapping is confirmed, but this is **not yet a verified Shopee purchasing recommendation**, especially when a headphone jack is required.

## H9 Max

**Capability-focused partial profile, checked 2026-10-18.** A separate effects processor, not H90 or H9 Gen 2. Legacy H9 variants are not automatically counted as additional researched models. This lead remains outside the older inventory totals pending reconciliation.

| Field | Finding / qualification |
|---|---|
| Built-in / external expression | No built-in treadle. External EXP/AUX control input documented. The official connector table calls EXP a **1/4-inch mono phone jack**, whereas H90 explicitly specifies TRS. Do not promise an arbitrary M-VAVE TRS pedal works unchanged. Resistance, wiring, calibration and any required cable remain to be checked against the actual controller. [H9-P] |
| Volume function / scope | **GLOBAL Output Swell (OSW)** is documented as the all-preset alternative to per-preset swell. Input Swell (ISW) is a different pre-processing option. Set the global OSW mode rather than individually enabling output swell in every preset. [H9-M, H9-S] |
| Range / position | The manufacturer's support discussion states swell attenuates from zero to full level; it does not provide gain above the preset's level. The expression value is current rather than saved with each preset. This is not the same as dynamically boosting the preset Output Level parameter. [H9-S] |
| Routing / bypass limits | Check normal mono/stereo operation first. Do not assume whole-signal volume in Pre/Post or Wet/Dry routing, or control during relay bypass. Exact routing-dependent output-swell coverage and bypass behavior remain unresolved in this capability pass. |
| Standard guitar input | Instrument-level input, 600 kΩ; no divided pickup required. Two 1/4-inch mono inputs and two mono outputs. [H9-P] |
| Size / mass | Official product dimensions are **133 × 118 × 50 mm; 0.7 kg**. The page labels them H/W/D rather than normal pedalboard W/D/H; retain that axis-label ambiguity rather than silently rewriting it. Every published dimension is under 140 mm, so the chassis fits the 200 × 140 mm filter in the usual placement. Cable clearance is extra. [H9-P] |
| Headphones | **No dedicated headphone jack** in the complete port specification. Recommended output load is 10 kΩ or greater; not a verified headphone amplifier. [H9-P] |
| Controls / memory / library | One-knob interface and two footswitches; exact separate button count/display specifications not yet audited. Official page lists 52 algorithms and 99 onboard presets, with 500+ available through H9 Control. Do not count downloaded presets as additional onboard memory, or algorithms as simultaneous processing blocks. Complete concurrency/category/overwrite details remain to verify. [H9-P] |
| USB / MIDI / editor | Mini USB, MIDI DIN In/Out-Thru, H9 Control for Android/iOS/Mac/PC with Bluetooth/USB control. USB audio or USB power is not established by those connectors. [H9-P] |
| Power | **9 V DC, 500 mA, center-positive, 5.5/2.5 mm** per manufacturer. This differs from a common center-negative 9 V supply and from H90's 12 V requirement. Battery operation unverified. [H9-P] |
| Other required fields | Published display diagonal/color/touch, full physical control count, category inventory/concurrency, factory/user memory split, IR/NAM/capture loading, acoustic simulation, looper details and qualified used IDR remain unresolved. This is not a fully verified catalogue profile. |

### H9 Max — local price observation

**Melodia Musik retail asking price Rp11.344.000**, checked 2026-10-18, rather than the struck-through Rp14.180.000. The product page displays available for Jakarta and Yogyakarta, unavailable for Bali, BSD, Surabaya and Roland Store Jakarta. These are the website's displayed stock statements, **not warehouse/checkout confirmation**. Condition grade, bundle, shipping and final stock were not independently verified. [H9-ID]

This is **an Indonesian retailer offer, not a Shopee listing**. A matching current Shopee hardware offer and an explicitly used offer remain unverified. Do not use eBay/Reverb foreign asks, unrelated H9 products or an invented conversion to fill those fields.

### H9 Max — sources and evidence strength

- [H9-P] [Official H9 Max product and complete connector/power/dimension specification](https://www.eventideaudio.com/pedals/h9-max/).
- [H9-M] [Manufacturer H9 User Guide download](https://www.eventideaudio.com/downloads/h9-user-guide/): indexed manufacturer text describes expression input/output swell globally or per preset. Direct file opening returned unsupported binary/internal errors; a complete rendered manual inspection is **not claimed**.
- [H9-S] [Eventide-hosted support discussion, including the corrected Input/Output Swell answer and GLOBAL ISW/OSW reference](https://www.eventideaudio.com/forums/topic/h9-output-level-control-with-expression-pedal/). The old initial not-yet-available answer is superseded within the discussion; the correction specifies global enable and zero-to-full attenuation. This accessible support text supplements, rather than masquerades as, a successfully rendered manual.
- [H9-ID] [Melodia Musik H9 Max hardware offer](https://www.melodiamusik.com/product/eventide-h9-max-harmonizer/).

**Verdict:** a source-supported global-volume capability candidate, but not a headphone-equipped all-in-one replacement, not a verified M-VAVE wiring match, and not yet a verified Shopee purchase. H9 Gen 2 requires its own manual and offer checks; do not transfer these settings by name similarity.
