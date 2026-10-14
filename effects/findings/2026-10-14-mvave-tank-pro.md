# M-VAVE TANK-PRO — Shopee-first research

[Comparison home](../README.md) · [Marketplace index](../shopee-indonesia.md) · [Resume](../RESUME.md)

Checked **2026-10-14**. **Partial technical record**, not a live-stock or fully verified claim. This is TANK-PRO, not TANK-G, TANK-B, MK-300 or an assumed-equivalent rebadge. Next priority: **M-VAVE ANN Blackbox**. This note is saved immediately as one model's research, before starting the next model.

## Hardware and display

| Field | Finding | Evidence |
|---|---|---|
| Instruments | Guitar/multi-instrument; bass EQ and bass amp entries also documented | M1, EN18 and effects appendix |
| Built-in expression | **No**; external expression supported | M1 complete front/rear panels EN02–03 |
| External expression / toe | **1 × 6.35 mm TRS EXP**, assignable P1/P2; no built-in toe switch | M1 EN03–05; an external-pedal Toe setting is not a physical built-in toe switch |
| Knobs / footswitches / buttons | **5 / 4 / 12**; PARA push-encoder counted once; power and ground-lift switches separate | M1 EN02–03 panel inspection: PARA, three assignable knobs, MASTER; A–D; HOME/SAVE plus ten module buttons |
| Dimensions W×D×H | **260×100×52 mm**; medium, not ≤200×140 compact | M1 EN19 labels horizontal side L; orientation normalized using panel diagrams; plug clearance additional |
| Weight | **Approximately 815 g** in manual; indexed official product specification says approximately 800 g | M1 EN19 versus M2; conflict retained, not independently weighed |
| Display | **One 2.4-inch LCD, color** | M1 EN19 diagonal; EN17 specifies seven interface theme colors |
| Touchscreen / resolution | **? / ?** | No explicit specification established; knob navigation alone is not proof of no touch |

## Processing and storage

| Field | Finding |
|---|---|
| Simultaneous processing | **Up to 10**, reorderable; 300+ advertised models. Manual warns about excessive DSP load, including global EQ with demanding effects. |
| Category choices | WAH **14**; FX1 **20**; FX2 **20**; DS **30**; AMP **90**; CAB **90**; EQ **8**; MOD **20**; DLY **27**; REV **18**. FX1/FX2 reuse the same library; these are not all unique algorithms. Counts include amps/cabs and alternative category assignments. |
| Presets | **120 editable locations = 30 banks ×4**. Banks1–15 contain 60 factory sounds; banks16–30 contain 60 effects-off starting setups. Not 120+60 presets. |
| Synth / acoustic simulation | **? / ?**. Pitch, octave and ring modulation do not establish a full synthesizer; an acoustic simulator was not established. |
| IR import | CAB accepts **mono WAV, 44.1 kHz/24-bit, 1024 or2048 samples**. Ninety cabinet entries are documented; an additional separate 90-user bank is not established. |
| Captures and NAM | DS/AMP import **AM4DATA** in the effect table, described more generally as amX Data in specifications. Official SINCO ANN changelog documents **NAM→AM4DATA conversion**. This supports a converted-model workflow, not an unrestricted native `.nam` or NAM A2 claim. Exact architecture/firmware restrictions remain unresolved. |
| Looper / rhythms | **150.8 seconds mono/stereo**, pre/post placement, overdub and last-layer undo/redo, retained after power-off; **100** rhythms. |

Evidence: M1 EN07, EN08–10, EN12–19 and M3 conversion changelog. DSP limits, preset locations, onboard cabinets and import formats are separate concepts.

## I/O, power and applications

| Field | Finding |
|---|---|
| Audio input | **1 × 6.35 mm TS instrument input** |
| Audio outputs | **2 × 6.35 mm TS unbalanced L/mono and R; 2 × XLR balanced L/R with ground lift; 1 × 3.5 mm TRS stereo headphone output** |
| Other connections | **6.35 mm TRS EXP; 3.5 mm TRS MIDI IN; USB-C USB2**. TRS MIDI wiring convention not established. No AUX, microphone input or FX loop appears in the complete rear-panel inventory. |
| USB | Audio, MIDI, data and charging; loopback and reamp, dry recording/wet monitoring documented. Exact USB channel count **?**. |
| Battery | **3000 mAh, 3.7 V, 11.1 Wh**, DTP105050; approximately7h manufacturer rating, not a measured result |
| Power | USB charging **5 V/1 A rated**; safety introduction recommends a **5 V/2 A adapter**. Approximately400mA working current is separately stated. **Simultaneous use and charging supported**. No9V barrel inlet is shown; do not copy a reseller's9V specification. Operation with battery removed is unverified. |
| Editors | **Windows, macOS, iOS, Android** documented in the model-specific manual; mobile app **M-EFCS**, built-in Bluetooth. Linux support **?**. Generic download-page supported-device lists omit some newer models; model-specific manual explicitly explains TANK-PRO connection. |
| Live features | Assignable individual switch presses; fixed switch combinations; tuner mute/bypass; right-output dry or no-cab options; Bluetooth accompaniment. Switching latency/gapless operation **?**. |

Evidence: M1 EN01–05, EN08–19, EN20 mobile connection; M3 software downloads. Touchscreen, Bluetooth, USB audio and USB power are not inferred from each other.

## Indonesian price evidence

| Condition | IDR observation | Exact listing and limitations |
|---|---:|---|
| Retail listing; explicit new-condition confirmation pending | **Rp1.900.000** | [Seven Stereo Music & Audio Store, item44814342587](https://shopee.co.id/M-Vave-Tank-Pro-Mvave-Tank-Pro-Multi-Effect-Processor-i.16879370.44814342587). Silver/Black and another variation shown; selected variant not independently resolved. Cached delivery text is6–7September, older than this review. **Not verified current stock**, seller authorization or delivered cost. |
| Used | **?** | No dependable used offer established. Do not estimate from retail. |

Earlier discovery [item55016320305](https://shopee.co.id/product/1408254222/55016320305) remains historical index evidence; it was not successfully reopened in this pass. Neither item establishes a completed sale. No foreign-currency conversion used.

## Primary sources and verification trail

- **M1: [Manufacturer-authored TANK-PRO manual and effect appendix](https://manualf.oss-cn-hongkong.aliyuncs.com/manual/Combined-Effect-Pedals/TANK-PRO.pdf)**. Original branded70-page bilingual document; Chinese specification section gives revision2026-06-12. Front/rear panels and EN18/19 tables visually checked. This original document replaces reliance on an unverified reformatted importer PDF.
- **M2: [Official TANK-PRO page](https://www.cuvave.com/product?id=tank-pro)**. Dynamic page exposes limited body text; approximately800g is indexed official evidence, explicitly distinguished from the manual's815g.
- **M3: [Official software/firmware downloads](https://www.cuvave.com/download)**. TANK-PRO V36 dated2026-09-24 listed; release-note retrieval failed, so later native NAM support is not inferred. SINCO ANN1.0.9 changelog explicitly adds NAM→AM4DATA conversion. No firmware was installed or independently tested.

**Remaining work:** explicit touch/resolution; weight conflict; current firmware NAM architectures and separate import capacities; synth/acoustic algorithms; live used/new offers and selected variations; USB channel count, MIDI TRS wiring, switching latency and Linux support. Preserve this evidence and continue with ANN Blackbox rather than restarting TANK-PRO.
