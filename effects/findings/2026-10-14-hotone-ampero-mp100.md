# Hotone Ampero MP-100 — guitar/bass multi-effects

Checked 2026-10-14. **Partial record; large footprint; built-in expression.** Exact original MP-100, not Ampero One, Mini or Ampero II. Useful findings are committed before starting the next model. [Scope](../SCOPE.md) · [Resume](../RESUME.md).

## Hardware and processing

| Required field | Established value / explicit remaining uncertainty |
|---|---|
| Expression | Built-in pedal plus one 6.35 mm TRS EXP2 input. Toe-switch implementation not verified |
| Controls, K/F/B | **5 rotary / 4 footswitches / 1 separate front button**: volume, MENU/VALUE, three quick-access knobs, four footswitches, device-lock button. Push-encoder counted once; rear switches separate. Manufacturer panel enumeration [M] and three-knob description [P] |
| Dimensions and weight | **320 W × 147 D × 46 H mm; 1408 g**. Large by this repository's size bins; cables/pedal travel additional [P] |
| Display | **4-inch, 800×480, color touchscreen**; one main display [P] |
| Processing | **9 simultaneous modules**. FX1/FX2/FX3 have shared libraries; amp/cab/EQ/gate/delay/reverb stages are not nine arbitrary duplicate engines [P,M] |
| Effects and category choices | Product page: **240+**, including 64 amps, 60 cabinets, 100+ pedal models and 50+ original effects. These overlapping marketing counts are not summed. V3.0 manual documents **71 shared FX1/2/3 choices**, including dynamic 9 and frequency 18; remaining category subtotals and current V5.2 total need a matched effect list [P,M] |
| Presets | **99 factory + 99 user =198**. Factory patches can be adjusted but not overwritten in their factory banks; save to a user location [P,M] |
| Acoustic simulator | **Yes**: AC Sim with Standard/Jumbo/Enhanced/Piezo modes in V3.0 list. Acoustic Refiner is a separate acoustic-input effect; product also describes acoustic-body IRs [P,M] |
| Synth | Exact current synthesizer algorithms unverified; do not treat pitch/modulation alone as a synth |
| IR | Third-party **24-bit/44.1 kHz mono WAV, 1024 samples**; user-slot capacity not established in the checked specification [P] |
| Captures / NAM | **Firmware 5.2 adds Sound Clone import: 10 stored clone files, one usable at a time, in FX1/FX2/AMP.** Proprietary workflow established; native-versus-converted NAM, accepted NAM architectures and capture-file limits require further documentation. Do not label IR support as NAM support [F] |

## Connections, power and software

| Field | Specification |
|---|---|
| Audio input | One 6.35 mm TS instrument input with electric/acoustic/line selector; 3.5 mm stereo aux. Input impedances 1 MΩ /4.7 MΩ /10 kΩ respectively [P] |
| Audio output | Two 6.35 mm TS unbalanced L/R outputs, two balanced XLR L/R outputs with ground lift, dedicated 3.5 mm stereo headphones [P] |
| Other ports | 6.35 mm TRS EXP2, five-pin DIN MIDI IN, USB 2.0 Type-B, DC. No microphone/phantom input, MIDI OUT or external FX loop in complete published connector list [P] |
| Power | **18 V DC center-negative, 500 mA maximum consumption**. Battery and USB-powered operation not established; USB audio does not establish bus power [P] |
| Configuration | **Ampero Editor Windows/macOS** for editing, managing effects/IRs and updating. Firmware **5.2 requires Editor1.5.0** per release notes. No mobile/Linux editor claim established [P,F] |
| Recording | USB Audio2.0 and USB recording documented; 24-bit/44.1 kHz processing. Exact interface channel count not independently verified in these sources [P] |
| Practice / live | **100-second mono /50-second stereo looper; 100 drum patterns**, tuner, assignable switches; rearrangeable chain documented in V3.0. No unmeasured latency or switching-gap claim [P,M] |

## IDR evidence — price is not checkout stock

| Condition | Amount | Source / qualification |
|---|---:|---|
| Retail hardware listing, detailed condition unconfirmed | **Rp7.535.000** | [Swee Lee Official Shop, Shopee shop799119783/item28319916328](https://shopee.co.id/Hotone-MP-100-Ampero-Multieffects-Pedal-i.799119783.28319916328). Reopened; cached/JavaScript-limited listing, not authenticated stock or final delivered price |
| Separate retail hardware listing | **Rp7.535.000** | [Gelora Musik Serpong, shop306155985/item22933054510](https://shopee.co.id/Multi-Efek-Pedal-Hotone-MP-100-Ampero-i.306155985.22933054510), indexed with older delivery text; not a second-hand lower bound |
| Used | **?** | No condition-verified used price obtained |

Seller branding and original-product claims are not independent authentication. Late-delivery vouchers are not purchase discounts. Accessories, regional firmware, final taxes/shipping and live stock require seller/checkout verification. No foreign exchange estimate or percentage-of-new used price used.

## Sources and revision limits

[P] [Manufacturer product/specification page](https://www.hotone.com/products/multi-effects/ampero).

[M] Hotone-authored **V3.0** manual mirrored on ManualsLib: [panel and memory definitions, p.4](https://www.manualslib.com/manual/1596650/Hotone-Ampero.html?page=4); [effect list, p.23](https://www.manualslib.com/manual/1596650/Hotone-Ampero.html?page=23). The manufacturer's numbered panel text was read; no PDF screenshot inspection is claimed. V3.0 counts are not current-firmware tests.

[F] [Hotone Japan, 2026-03-09 release notes](https://www.hotone.jp/announcements/ampero-sound-clone-release) and [global firmware index](https://www.hotone.com/support/2?pid=1&tid=1), both naming V5.2/Editor1.5.0. Pink/limited V5.2A is not silently substituted for the ordinary hardware firmware. The manual-download page returned a server-error shell; another mirrored V4.1 PDF could not be fetched.

Remaining: firmware-matched complete algorithm breakdown, synth choices, IR capacity, toe implementation, bus-power confirmation, current used offers and exact NAM workflow. **Next marketplace model: Hotone Ampero II MP-350.**
