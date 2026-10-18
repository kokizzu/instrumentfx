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
