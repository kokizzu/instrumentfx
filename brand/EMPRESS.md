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

### ZOIA — audio headroom and modular tracking distinctions

Checked **2026-11-04**, [exact manufacturer product/specifications](https://empresseffects.com/products/zoia),revision unstated. Published input impedance **≥1MΩ**,output **100Ω**;input headroom **+0.5dBu without pad,+5.7dBu at6dB pad,+10.8dBu at12dB pad**;output headroom **+16.2dBu**. These are audio ratings,not EXP resistance orheadphone-drive certification. Conversion **24bit/48kHz**,internal processing32bit;this doesnot establish USB audio.

The manufacturer describes **Pitch Detector→CV note→Oscillator** for audio-following synthesis. MIDI Notes In orgrid Keyboard can instead control oscillators;these are different triggering paths. **Pitch Shifter** transposes incoming audio. Input-note polyphony,tracking quality andlatency remain unverified;oscillator count isnot chord-tracking evidence. VCA accepts expression-module control inside a patch,not a documented all-preset master override.

[Own ZOIA support control table](https://empresseffects.com/blogs/support-zoia) assigns grid indices0–39 plusPageLeft,PageRight,Back,Shift: **44 addressable hand-button positions**,separate fromthree stompswitches andencoder press. This is a text-derived control census,not fresh visual corroboration;Euroburo-only indices44–58 are excluded. MIDI remote bypass usesCC60:0bypass,64toggle,127engage;it doesnot prove pedal attenuation duringbypass.

Partial lead remains outside active counts. Exact Shopee hardware identity,current module census,factory fill,complete ports/import/editor profile andglobal-volume output coverage remain open. No downloads ordevice operation.

### ZOIA — page capacity, copy displacement and save destination

Checked **2026-11-04**, [manufacturer Manual v02,printedpp16–21](https://empresseffects.com/cdn/shop/files/ZOIA_User_Manual_rev02_web.pdf?v=9116714327727882529);21PDF pages contain paired printed pages,not21printedpages. Identity follows theZOIA cover/layout andfinalManualv02 mark. Text review only;current5.41 behavior untested.

- **Up to64 pages perpatch,numbered0–63**,each an8×5 grid. Pages are workspaces within one patch,not64 additional whole-rig presets orfixed simultaneous module capacity. Modules consume variable grid space andDSP.
- Connections may cross pages **within a patch**,butcannot cross patches. Page import preserves connections within/between imported pages;this doesnot create shared live global processing acrosspatches.
- **Copy Patch shifts subsequent patches down and erases patch63**. This is the manual’s documented displacement behavior,not adevice operation orproof ofsufficient free space. Preserve backups before using that workflow.
- Ordinary **Save writes internal memory**;SD-card writing isseparately requested inConfig. Saving a patch doesnot itself refresh its card backup. Initial factory occupancy andglobal configuration/sampler-backup scope remain unresolved.

Theprevious source-retrieval failure ishistorical;this check recovered readable original text without a local download. Completeports,currentmodulecensus,exactShopeeitem andglobalvolumecoverage remain open;partial lead stays outsideactivecounts.

### ZOIA — sampler media and factory-content prerequisites

Checked **2026-11-04**, [manufacturer support hub](https://empresseffects.com/blogs/support-zoia), sections “What are the ZOIA Sampler requirements?” and “Updating Firmware”; article revision dates unstated.

- The sampler article explicitly describes **beta firmware**: FAT32 media; 48kHz/16bit stereo WAV; files at root or one directory below; card/files present at boot, or regenerate the list in Config. It gives a10-minute file limit and64 directories with64 files each, with roughly64 entries displayed. Faster playback and recording/overdub increase DSP use. These are revision-uncertain support restrictions, **not a verified current5.41 census**.
- Preserve the separate **4.00** changelog evidence above: mono/stereo8/16/24/32bit acceptance and conversion. The older stereo16bit-only wording must not silently override that later release evidence. Current filesystem/list limits still need confirmation.
- Firmware5 factory patches **Groovebox and Grand Piano require external sample assets**. Empress says new ZOIA pedals ship those assets onSD; Euroburo is excluded. The new guitar-oriented factory set is ZOIA-specific by default. This doesnot establish assets/card contents included with a particular used offer or backup of those assets by patch export.

No package downloaded, card formatted or device updated. Exact hardware offer, complete ports/editor/import profile andglobal-volume coverage remain open; partial lead remains outside active inventory.
