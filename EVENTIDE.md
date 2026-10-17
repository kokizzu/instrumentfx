# Eventide multi-effects

## H9 Max

Checked 2026-10-17; partial. Max is distinct from Standard/Core; ownership unverified.

| Field | Evidence / qualification |
|---|---|
| Instrument scope | Guitar setups in own manual; bass/vocal suitability unclassified pending explicit evidence. |
| Expression | No built-in pedal. External EXP controls multiple parameters;5–25kΩ linear pot, auto-calibration. EXP alternatively supports 3 momentary switches;toe-switch support unknown. Manual calls EXP stereo, product table says mono: retain connector conflict. [M pp25–26][H9-M] |
| Knobs / footswitches / buttons | **1 rotary/2 footswitches/5 buttons**:encoder;left/right;HOTKNOB,X,Y,Z,PRESETS. Encoder press counted once; derived from text, not visual inspection. [M pp7–9][H9-M] |
| Display | Six-character display plus LightRing;diagonal,color/touch unverified. [M p18][H9-M] |
| Processing / choices | **52 algorithms**,from TimeFactor, ModFactor, PitchFactor, Space and H9-specific families. Guide contents reconcile **Space 12 + PitchFactor 10 + TimeFactor 10 + ModFactor 10 + H9-specific 10 =52** [G pp1–2][H9-G]. **One preset operates both channels; two presets cannot run simultaneously**. Fixed combined algorithms are not free block chains. [P][H9-P],[M p10][H9-M] |
| Factory / user memory | **99 onboard slots, 99 factory presets, editable/saveable**;not 99 factory + 99 extra user. App offers 500+ presets, not additional onboard slots. [P][H9-P],[M pp7,18][H9-M] |
| Synth / acoustic | **HotSawz:** 6 saw oscillators follow a mono pitch tracker, low-pass filter. **Synthonizer:** additive voice A/subtractive voice B; input 1 only, input 2 disabled, no tempo mode. Acoustic simulation remains unverified. [G pp31,75][H9-G] |
| Dimensions / mass | Product labels **133H×118W×50Dmm;0.7kg**. Axis labels are unusual for a floor pedal; retained without normalization. [P][H9-P] |
| Audio / control I/O | Two ¼-inch mono inputs, two ¼-inch mono outputs,EXP,mini USB 2.0, MIDI IN and OUT/THRU 5-pin DIN,DC. **600kΩ input, 470Ω output, load ≥10kΩ**. No headphone connector in the published list. USB audio unverified;USB MIDI documented. [P][H9-P] |
| Power / battery / USB | **9V DC 500mA, center-positive, 5.5/2.5mm**,supply included; published power specification, not measured current. Battery/USB operation unverified. [P][H9-P] |
| IR / NAM / captures | User IR, native/converted NAM and captures unverified. |
| Editor / platforms | **H9 Control iOS/Android/Mac/PC**,editing, setlists, preset management via Bluetooth or USB; Official listing: **Windows 4.0.1, macOS 4.1.6, iOS 4.0.5**; Android ≤12 uses 4.0.1, Google Play 4.1.2 added Android 13+ support and lists 4.2.0. Full OS matrix pending. In-app algorithm store removed in 4.0.1. [Downloads][H9-D] [P][H9-P] |
| Looper / drums / live | Tap tempo, MIDI sync, tuner, analog bypass. **Looper: 12s mono at full quality, 24s at half-speed, 48s at quarter-speed with reduced quality**. Stereo inputs are summed; both outputs carry the same loop. Reverse and MIDI clock sync supported. Tuner requires an empty loop; loading a Looper preset starts empty. Drums/scenes/tails limits remain unverified. [Looper supplement pp1,3–5][H9-L] [P][H9-P] |

### Separate IDR hardware evidence

| Condition / source | Amount / limits |
|---|---|
| Verified used | Unknown |
| Verified new | Unknown |
| Condition unverified / Melodia Musik Roland Store JKT, Kota Jakarta Selatan | **Rp10,635,000**,25% off crossedRp14,180,000;exact seller30194339/item18057992258. [Shopee][H9-O] search and direct indexed text, two-month crawl, checked 2026-10-17. Relative Hari Ini delivery is not live checkout stock. Bundle, condition, variant, warranty, voucher, shipping/tax and authenticity unverified. Not a completed-sale price. |

[P] is manufacturer product text. [M] original H9 User Guide identifies H9/H9MAX despite the PDF search title SPACE; 53 PDF pages with printed page numbers offset. No file downloads or image inspection. Early manual in-app algorithm-store language is not current purchase availability.

[H9-P]: https://www.eventideaudio.com/pedals/h9-max/
[H9-M]: https://cdn.eventideaudio.com/uploads/2020/07/H9-Manual.pdf
[H9-O]: https://shopee.co.id/Eventide-H9-Max-Harmonizer-Multi-Effect-Pedal-i.30194339.18057992258

### H9 Max — software and looper verification

Checked 2026-10-17. [Official downloads][H9-D] lists separate updater and H9 Control versions; no software was downloaded or operated. Older store instructions on that page are historical and are superseded by the explicit store-removal notes.

The [H9/TimeFactor looper supplement][H9-L] explicitly separates their footswitch operations. The saved durations and mono routing apply to H9; TimeFactor’s third switch is not assigned to H9. H9 right-switch double-tap while stopped clears the loop; holding it changes Preset/Looper mode. This does not establish simultaneous looping plus a second algorithm.

The linked V12 algorithm guide redirects to an inaccessible PDF. Search results labeled **H9 Harmonizer Gen 2** or H90/H9000 were not used to enlarge this original H9 Max library. Per-family enumeration and synth details remain pending.

[H9-D]: https://www.eventideaudio.com/downloads/?product=H9
[H9-L]: https://cdn.eventideaudio.com/uploads/2021/09/Looper.pdf

### H9 Max — algorithm family reconciliation

Checked 2026-10-17 against the manufacturer-authored guide body on [Scribd][H9-G]. The upload title reports V12; the body identifies H9, its six-character display and H9 Control. Its contents end with TriceraChorus, matching Eventide’s V12 release note. An embedded revision stamp was not independently located; no complete parameter-by-parameter audit or visual inspection claimed. Generated page title and summaries are not evidence.

| Field | Documented algorithms |
|---|---|
| Processing / Space 12 | Hall, Room, Plate, Spring, DualVerb, Reverse Reverb, ModEchoVerb, BlackHole, MangledVerb, TremoloVerb, DynaVerb, Shimmer |
| Processing / PitchFactor 10 | Diatonic, Quadravox, HarModulator, MicroPitch, H910/H949, PitchFlex, Octaver, Crystals, HarPeggiator, Synthonizer |
| Processing / TimeFactor 10 | Digital Delay, Vintage Delay, Tape Echo, Mod Delay, Ducked Delay, Band Delay, Filter Pong Delay, MultiTap, Reverse, Looper |
| Processing / ModFactor 10 | Chorus, Phaser, Q-Wah, Flanger, ModFilter, Rotary, TremoloPan, Vibrato, Undulator, RingMod |
| Processing / H9-specific 10 | UltraTap, Resonator, EQ Compressor, CrushStation, SpaceTime, Sculpt, PitchFuzz, HotSawz, Harmadillo, TriceraChorus |

These are lineage groups, not five simultaneous blocks. Earlier full-guide access gap is narrowed by this readable original-body copy; the official PDF remains inaccessible. Actual installed algorithms/firmware are unverified. The older guide found at [Zikinf](https://www.zikinf.com/manuels/eventide-h9-algorithm-guide-en-46958.pdf) says over40 and no Looper; retain that as older documentation, superseded here by the 52-entry contents and official H9 looper supplement. No file downloaded.

[H9-G]: https://www.scribd.com/document/754982282/Eventide-H9-Multi-FX-Algorithm-Guide-v12
