# Empress Effects — multi-effects discovery

[Repository](../README.md) · [External-expression audit](../EXPRESSION-VOLUME.md)

<!-- brand-index begins -->
**Model and section index — A–Z, natural numeric order**

- [ZOIA — control-port sharing and patch backup scope](#zoia--control-port-sharing-and-patch-backup-scope)
- [ZOIA — current firmware and sampler revision boundaries](#zoia--current-firmware-and-sampler-revision-boundaries)
- [ZOIA — partial no-treadle discovery](#zoia--partial-no-treadle-discovery)
<!-- brand-index ends -->

## ZOIA — control-port sharing and patch backup scope

Checked 2026-11-03 against [manufacturer Rev02 manual, printed pp24,26,28–30](https://empresseffects.com/cdn/shop/files/ZOIA_User_Manual_rev02_web.pdf?v=9116714327727882529); text only, no hardware test.

- CPort connects **one selected device at a time**. EXP, CV, MIDI and external switch are alternative configurations, not four simultaneous sockets.
- Dedicated⅛-inch MIDI uses **Type A** adapters and does not accept CV. In CPort MIDI mode, tip receives and ring transmits; a TS cable prevents transmission. With the dedicated MIDI ports in use, CPort MIDI can send but cannot receive. These MIDI pin roles are separate from analog EXP wiring.
- External switch mode accepts normally-open/closed, momentary/latching operation; tip-to-sleeve closure is the switching connection. It still needs a patch stompswitch module/target.
- SD patch imports create backups of the currently loaded patches, with up to256 backup folders. Exporting into an existing folder overwrites same-named patches. Patch import names require a three-digit prefix and.bin extension. This does not prove backup of global configuration or sampler audio.

Global analog-volume assignment, position/endpoints and bypass/headphone/tail/loop coverage remain unresolved. Partial lead stays outside active counts.

## ZOIA — current firmware and sampler revision boundaries

Checked2026-11-03. [Manufacturer firmware page](https://empresseffects.com/pages/firmware-updates) advertises **5.41**; [manufacturer changelog](https://empresseffects.com/cdn/shop/files/zoia_changelog_79fc7e0a-a748-4381-a0df-0f0866ff01d6.txt?v=9624477519191733807) dates it June16,2026. This is a published release, not a claim about installed firmware; no binary downloaded or run.

- 5.41 revises factory patch1 on ZOIA (patch37 on Euroburo); model-specific positions must not be interchanged.
- 5.40 adds MIDI pitch-bend OUT and aftertouch OUT modules. The product-page module list may lag; no complete current census inferred.
- **5.32 retains bypass state when changing patches in Bank mode**, fixing earlier toggling. The Rev02 manual describes pressing the selected switch again to bypass. Keep these version-qualified; neither proves that expression volume survives bypass or acts globally.
- 4.00 sampler supports mono/stereo WAV at8/16/24/32bit, with48kHz required for playback and built-in conversion of individual files. WAV sample import is not IR/NAM/capture support.
- Sequencer patches saved on4.20+ do not load correctly on earlier firmware. Preserve original backups for backward compatibility. Current preset-volume override and output/tail/looper coverage remain unverified.

## ZOIA — partial no-treadle discovery

Checked 2026-11-03. Genuine modular multi-effects/synth hardware; normal guitar/bass input is manufacturer-documented. **Partial lead outside active model/brand counts**, with no ownership inferred. Shared OLED is not an established individual-footdisplay match.

| Field | Exact-model evidence and qualification |
|---|---|
| Processing/memory | Product header 90+ modules; older details say 80+; 20+ prebuilt effects, 64 onboard patches. These are library/storage figures, not simultaneous-block counts. Current category census/factory-filled count unknown. |
| Footprint/power | Manufacturer L5.7×W3.75in = 144.78×95.25mm; enclosure H44.45mm, controls H66.675mm; 1.5lb (~0.680kg). 9VDC center-negative, 2.1mm, 300mA required; supply excluded. Nominal L as depth exceeds140mm; rotated rectangle fits200×140mm, but practical orientation/cable clearance remains unverified. |
| Display | OLED main screen; diagonal, color/touch and separate footswitch displays unverified. |

Source: [manufacturer product/specifications](https://empresseffects.com/products/zoia). No fixed DSP ceiling, current firmware census, USB capability, editor OS, native/imported IR/NAM/capture support or acoustic-simulation conclusion established by this pass.

**Expression and navigation:** [Rev02 manual](https://empresseffects.com/cdn/shop/files/ZOIA_User_Manual_rev02_web.pdf?v=9116714327727882529), printed pp4–5,10–11,23,28–29: CPort selects EXP globally, but the expression-input module and target connections belong to saved patches. VCA routing permits pedal volume within a patch; an all-preset volume override without patch editing remains **unknown**. Position recall, attenuation minimum/maximum, bypass and tail/looper/output coverage remain unknown. Global CPort mode is not global target assignment.

Scroll mode advances preview with SCROLL; SELECT+SCROLL previews downward; SELECT loads. Bank mode offers three patch switches and paired bank± commands. These are not an immediate dedicated preset± pair. One rotary encoder/three stompswitches documented; complete physical button census pending. No dedicated headphone jack established by the published layout; shared manual references to Euroburo Headphone do not establish ZOIA pedal headphones.

**Actual EXP wiring:** [manufacturer compatibility article](https://empresseffects.com/blogs/support-zoia/what-expression-pedals-can-i-use) specifies TRS tip=signal, ring=3.3V, sleeve=ground. Known-compatible examples include Roland EV-5, BOSS EV-30 and M-Audio EX-P with suitable polarity. Resistance/taper requirements unverified. [Wrong-polarity warning](https://empresseffects.com/blogs/support-zoia/my-expression-pedal-only-controls-effect-in-the-first-10-of-its-travel-whats-going-on): ring-signal pedals compress response into roughly the first10% of travel. This is wiring behavior, not a volume-endpoint specification.

**Shopee Indonesia discovery only:** [category index](https://shopee.co.id/search?keyword=modular+synthesizer), checked2026-11-03, search cache four days old: “Empress Zoia Modular Synth Pedal Multi Effects & Synthesizer Guitar Pedal”, Rp16,278,000, Jakarta Barat. Exact seller/item ID, condition, variant, bundle, stock, voucher and warranty unresolved. This is neither a qualified new/used price nor verified available hardware. No accessory/software price substituted.

Remaining: exact Shopee hardware page; current firmware/module index; complete I/O/control census and memory split; output/headphone/bypass/tail/looper scope; import/editor support. Preserve the independent GP-200JR → Prime → GE300 queue and LCD-first priority.
