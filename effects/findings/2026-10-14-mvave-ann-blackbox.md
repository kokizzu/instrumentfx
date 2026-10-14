# M-VAVE ANN Blackbox — Shopee-first research

[Home](../README.md) · [Marketplace](../shopee-indonesia.md) · [Resume](../RESUME.md)

Checked **2026-10-14**. **Partial record** for **ANNBLACK BOX**, not a blanket specification for every older product titled Blackbox. Next discovery checks: **Boin Audio BG300 and Scorpion KMF-10**, then JOYO GemBox variants. Findings are committed individually.

## Comparison

| Required field | Finding | Source |
|---|---|---|
| Instruments | Guitar and bass; manual's original amp/cab banks contain15 guitar and5 bass entries | M1 EN01/14 |
| Built-in / external expression | **No / no dedicated socket** in complete panels; MIDI-controller expansion exists but is not an included expression pedal or verified continuous-expression mapping | M1 EN03–07,15 |
| Knobs / footswitches / buttons | **2 / 2 / 7**, including MASTER/PARA, two footswitches, HOME plus six module buttons. PARA push action is not counted again; rear power slide separate | M1 panels |
| Dimensions / size | **113×109×41 mm, source L×W×H**; precise W/D orientation unresolved. **Compact in either orientation**; no rotation is needed to pass200×140 | M1 EN14 |
| Weight | **410 g** | M1 EN14; do not copy613g from a mismatched legacy HTML table |
| Screen | **One color graphical screen**; diagonal, technology, resolution and explicit touchscreen specification **?** | M1 EN04 describes white/blue on-screen Bluetooth icon; no diagonal inferred from enclosure |
| Blocks / categories | **6 reorderable modules**, FX/AMP/MOD/DLY/REV/CAB. Manufacturer calls processing **6+1** because FX can combine gate with boost or compressor, not seven freely assignable blocks | M1 EN01/07/14 |
| Choices | FX3 configurations: gate, gate+boost, gate+compressor; AMP20 with3-band EQ; MOD7; DLY5; REV6; CAB20. Advertised60+ total includes amps/cabs | M1 EN01/07/14 |
| Presets | **80 editable total**,40 factory-filled; original P36–40 are bass patches. A firmware preset pack can change factory contents; not80+40 | M1 EN05; M3 |
| Synth / acoustic sim | **? / ?**; swell/shimmer does not establish a synth or electric-to-acoustic algorithm | No matching primary claim established |
| IR | Third-party **mono WAV,44.1kHz/24-bit,1024 samples**,20 cabinet locations. Do not add another20-user bank without evidence | M1 EN14 |
| NAM / captures | AMP import uses **AM2/AM3/AMx** in this manual. Official SINCO ANN offers NAM conversion to proprietary formats; **unrestricted native NAM and exact accepted architectures on this hardware remain unverified** | M1 EN01; M2 |
| Audio ports | **1×6.35mm TS input,1×6.35mm TS mono output,1×3.5mm stereo headphone output** | M1 rear panel and EN14 |
| Other ports | **USB-C** for audio/data/power and supported MIDI-controller connection. No XLR, AUX, FX loop, DIN or TRS MIDI socket shown | M1 EN03/14/15 |
| Power / battery | **2000mAh,3.7V** rechargeable; USB **5V≥300mA** power input; approximately200mA working current. Manual states approximately408mA charging limit and10+h runtime; these are not independent measurements | M1 EN14 |
| USB-powered? | **Yes**, manual explicitly lists battery **or USB5V**. No9V barrel input shown | M1 EN03/14 |
| Editors | **M-EFCS Windows/macOS/iOS/Android**; phone editing via Bluetooth. Linux **?** | M1 cover/EN14–15; M2 |
| USB audio | **44.1kHz/24-bit**, selectable loopback; phone OTG recording. Channel count/reamp **?** | M1 EN14–15 |
| MIDI / live | Wired/wireless controller expansion, including documented Chocolate Plus functions; module stomp control, preset up/down, tap tempo, tuner mute/bypass and delay hold | M1 EN07/15 |
| Looper / drums / trails | Built-in looper, drum machine and documented gapless/spillover specification **not established**; USB loopback is not a looper | M1 scope; no unsupported negative assertion |

## IDR evidence

**Retail listing: Rp1.089.000**, [Vi Music Store, Shopee item41328082291](https://shopee.co.id/M-Vave-MVAVE-Ann-BlackBox-Black-box-Amp-Modeler-Effects-Processor-Multi-Effect-Guitar-i.31581393.41328082291), with black/blue/milk-color variations. **Used: ?**. The page was retrievable on the check date; condition declaration, selected variant, seller authorization and checkout stock were not independently confirmed. Its location-dependent delivery banner is not a shipping promise. No completed-sale or market-range claim.

## Primary evidence and source-quality notes

- **M1: [Manufacturer-authored ANNBLACK BOX manual, mirrored PDF](https://device.report/m/38851327ce24db6d2907bb20d70f3b9d20279ab5e4355cd2752a6407b3d74a3d_optim.pdf)**. Inspected cover and English printed pages1,3,4,5,7,14,15 as page images because extracted text was absent. Mirror metadata incorrectly uses on-screen example P14/097 as a model name; the actual cover says ANNBLACK BOX. Optimization causes duplicated character artifacts, so only clearly legible values were used. The source's current revision/date is not established.
- **M2: [Official software/firmware downloads](https://www.cuvave.com/download)**, M-EFCS and SINCO ANN conversion resources. **[Official product identity](https://www.cuvave.com/product?id=annblack-box)** is dynamic and exposed little text; it does not independently resolve unknown specifications.
- **M3: [Manufacturer ANNBLACKBOX preset introduction](https://community.m-vave.com/bbs/api/software?file=ANNBLACKBOX_en.pdf)**. A downloadable sound pack is not extra hardware memory.

**Rejected conflation:** a third-party legacy BLACKBOX HTML specification table lists310×65×40mm,613g and XLR output, incompatible with the ANN manual/panel. Those values were not adopted. Do not use AI-generated Q&A on manual mirrors to establish firmware formats.

**Unresolved:** exact display diagonal/touch/technology, W/D labels, current NAM conversion/architecture restrictions and factory content, live used/new offers, firmware-specific effects additions, USB channel count, continuous MIDI-expression mapping and Linux support.
