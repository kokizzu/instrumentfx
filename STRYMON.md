# Strymon — expression-volume capability leads

[External expression-volume comparison](EXPRESSION-VOLUME.md)

## Iridium

**Checked 2026-10-18. Capability supplement; scope-admission pending.** Iridium combines amp, cabinet and room processing, but is not a general-purpose multi-effects chain with interchangeable drive/modulation/delay blocks. It is recorded as an adjacent answer to the small-pedal volume question, **not silently added to the active multi-effects inventory**. It is not a Deco, Riverside or another Strymon model.

### External pedal operation

**Documented persistent device-level input mode:** select **Volume PRE** or **Volume POST**, rather than assigning LEVEL within an individual preset's Expression mode. Strymon places this under Power Up Modes / EXP Jack Options and explicitly states the jack assignment survives power cycles. This configuration does not ask the user to edit each preset. [IR-FAQ, IR-M pp.18,39]

To select POST: hold **FAV** while connecting power, release when both LEDs flash, turn **LEVEL** until the **ON LED is red**, then press ON or FAV to store and exit. PRE is amber and is the factory default. Use a compatible **TRS expression pedal**. The actual M-VAVE model's resistance, polarity and taper have not been verified; no hands-on compatibility claim is made. [IR-FAQ]

**PRE** is before amp/cab/room; **POST** is after amp/cab but **before ROOM**, not after every effect. Existing room decay is therefore not covered by a final-output mute guarantee. The manual's mono bypass diagram routes through a buffer, outside the processing chain: do not rely on this volume function when Iridium itself is bypassed. Full heel/toe attenuation limits and every preset-transition case remain untested. [IR-M pp.18,46]

### Hardware and practical limitations

| Field | Verified finding / qualification |
|---|---|
| Built-in treadle / normal input | No built-in expression pedal. Normal mono guitar input supported; instrument/line input modes. [IR-P, IR-M] |
| Chassis | **102 W ×114 D ×44 H mm**, fits 200 ×140 mm before plugs. Mass is not verified here. [IR-M p.35] |
| Headphones | Dedicated **3.5 mm stereo** output; manufacturer states it receives the same signal as main outputs. [IR-M p.12] |
| Preset operation | **FAV and ON**, not onboard preset-down/up. The shared EXP jack must instead use Digital mode for MultiSwitch Plus/MIDI selection, so do not promise a directly connected analog EXP pedal and external MIDI preset access simultaneously through this one jack. [IR-P, IR-M p.18] |
| Processing | Three amp models, nine cab selections and Room ambience; third-party cab IR replacement supported. Not a full alternative to a processor's drive, modulation and delay library. [IR-P] |
| Screen / controls | No graphical screen or touchscreen in the complete panel; six knobs, FAV/ON footswitches, amp/cab and input-mode selectors. Exact switch-count taxonomy remains to reconcile with other brand records. [IR-P] |
| Power | **9 V DC, center-negative, at least 500 mA supply**. Supply requirement is not measured consumption. [IR-M p.35] |
| Other gaps | Model-specific full memory accounting, editor OS/support versions, USB audio/power, complete bypass/EXP interaction, min/max sweep, qualified used price and exact Shopee hardware offer. No features are inferred from other Strymon pedals. |

### Indonesian offer evidence

[Swee Lee Indonesia Iridium page](https://www.sweelee.co.id/en/products/strymon-iridium-amp-and-ir-cab-guitar-effects-pedal) displays **Rp8.170.000, Pre-Order Now**, checked 2026-10-18. This is the product's own ask, **not a Shopee listing or verified immediate stock**. Condition grade, exact adapter bundle and delivery remain to confirm. The same page's recommendation grid separately lists a **w/o adapter** offer at Rp9.050.000; that is a different offer, not an interchangeable lower/higher bound for the same bundle. Used IDR and a matching Shopee Indonesia hardware listing remain unverified.

### Sources and inspection

- [IR-FAQ] [Manufacturer setup instructions for Volume PRE/POST and persistence](https://www.strymon.net/faq/how-to-set-the-exp-jack-to-volume-pedal-mode-on-iridium/).
- [IR-M] [Official Iridium User Manual Rev D](https://www.strymon.net/manuals/Iridium_UserManual_RevD.pdf). PDF pages **18,35,39,46** (1-based printed numbering) were successfully rendered and inspected for mode choices, dimensions, persistent settings and mono bypass routing. The headphone passage on page12 was read as parsed original text.
- [IR-P] [Manufacturer product and full control description](https://www.strymon.net/product/iridium/).

**Verdict:** another small, headphone-equipped pedal with a persistent volume-input mode, but a limited amp/cab/room platform with no onboard preset-up/down workflow. Do not present it as a verified Shopee bargain or an unconditional GP-50 replacement.
