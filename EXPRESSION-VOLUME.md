# External expression as volume — no built-in treadle

[All guitar models](ALL-GUITAR.md) · [Bass](ALL-BASS.md) · [Multi-effects](MULTI-EFFECTS.md) · [Research state](research-state.json)

**Checked 2026-10-18. Research is ongoing, not an exhaustive market certification.** This comparison answers: can a separate analog expression pedal control normal-pickup instrument volume on every preset without configuring each preset? The preferred chassis limit is **200 W ×140 D mm**, excluding cable clearance. Headphones and onboard preset-down/up are tracked separately rather than silently assumed.

The instrument index reports **120 existing catalogue models**; the older README/JSON reported117 before this audit. Those totals are inventory counts, **not120 freshly inspected expression manuals**. This page contains **10 model-level capability records**, including three separately named POD Express variants, plus unresolved and size-screened leads. New partial discoveries are not silently included in the old catalogue totals. Iridium is an adjacent amp/cab/room candidate pending scope admission.

## What counts as global

| Status | Meaning |
|---|---|
| **GLOBAL** | Manufacturer documents a device/system input mode or mapping that does not require a volume assignment/block to be configured separately in each preset. |
| **PER PATCH** | A volume effect or controller assignment must be configured inside each patch. |
| **CONDITIONAL** | Pedal controls volume only when some other effect is disabled or a patch-specific condition is satisfied. |
| **UNVERIFIED** | Evidence has not established the assignment scope. This must not be converted into No. |

Global **calibration**, global **pedal-position recall**, global **EQ**, a physical **master knob**, and generic **MIDI support** prove none of the GLOBAL assignment requirement by themselves. Global assignment also does not guarantee final-output muting, pedal action during bypass, headphone coverage, or a compatible taper with an arbitrary expression pedal.

## Sourced capability matrix

All ten named models below have no built-in treadle. Dimensions are manufacturer-backed where numerical values are given; unknown values are intentionally not filled from unsourced marketplace descriptions.

| Model | Analog EXP volume scope | Signal target / caveat | Chassis fit | Headphones | Detailed evidence |
|---|---|---|---|---|---|
| **Line 6 POD Express Black** — new lead | **GLOBAL** Volume Jack → Volume/FS4 | Volume after amp/cab, before post effects. Not a final-output mute. | Numeric manufacturer dimensions still unverified in inspected sources | Yes,3.5 mm | [LINE6](LINE6.md#pod-express-black), official product and joint2.00 manual explicitly include Black |
| Line 6 POD Express Guitar — already discussed | **GLOBAL** same explicit family mode | After amp/cab, before post effects | Numeric manufacturer dimensions still unverified | Yes,3.5 mm | [LINE6 audit](LINE6.md#external-expression-volume-audit) |
| Line 6 POD Express Bass — already discussed | **GLOBAL** same explicit family mode | After amp/cab, before modulation/delay; not a promise to mute recorded loops | Numeric manufacturer dimensions still unverified | Yes,3.5 mm | [LINE6 audit](LINE6.md#external-expression-volume-audit) |
| **Eventide H90** — new lead | **GLOBAL** Pedal Control → P Out Gain | Program output gain; exact full-mute range and dual-routing coverage unresolved. Relay bypass does not pass through the DSP gain control. | **170 W ×136 D mm — fits** | **No dedicated jack** | [EVENTIDE H90](EVENTIDE.md#h90), manufacturer Global Mapping Chart and I/O settings |
| **Eventide H9 Max** — new lead | **GLOBAL** Output Swell / OSW | Zero-to-full attenuation, not boost above the preset level. Wet/Dry, Pre/Post and bypass coverage require further verification. | Official133 ×118 ×50 mm; axis labels unusual, all dimensions fit the limit | **No dedicated jack** | [EVENTIDE H9 Max](EVENTIDE.md#h9-max), corrected manufacturer-hosted support discussion and indexed manual |
| Neural DSP Nano Cortex | **UNVERIFIED global**; EXP and LEVEL target documented | Confirm whether target is final main-output level and whether headphones follow it. Global calibration is not global mapping. | **144 ×103 mm — fits** | Yes; expression coverage **unverified** | [NEURAL-DSP](NEURAL-DSP.md), NanOS2.2.0 official HTML manual |
| DigiTech RP55 | **CONDITIONAL**, not always-volume | Volume only with both Wah and Whammy disabled; otherwise pedal function changes | **165.1 W ×143.51 D mm — fails depth by3.51 mm** | Shared TRS output explicitly supports headphones | [DIGITECH](DIGITECH.md), rendered official manual pp.20,22 |
| Zoom B2 FOUR | **PER PATCH** | Pedal effect selected within each patch. Global master knob is a separate function. | **249 W ×146 D mm — fails both limits** | Yes,3.5 mm | [ZOOM B2 FOUR](ZOOM.md#b2-four--external-expression-volume-audit), official HTML manual |
| IK Multimedia TONEX Pedal | **UNVERIFIED global** | Generic expression parameter control does not prove all-preset volume mapping | **176 ×142 mm — fails depth by2 mm** | Yes; expression coverage unverified | [IK-MULTIMEDIA](IK-MULTIMEDIA.md), official product specifications; needed manual not retrieved |
| **Strymon Iridium** — adjacent new lead | **GLOBAL device mode** Volume PRE/POST | POST is after amp/cab but before ROOM. Do not rely on it in buffered bypass. | **102 W ×114 D mm — fits** | Yes,3.5 mm; same processed signal as main outs | [STRYMON](STRYMON.md), rendered official RevD manual and manufacturer setup FAQ |

### Preset workflow and platform differences

POD Express Black/Guitar/Bass have a documented Preset Mode: hold ON and TAP together, then use the two switches for down/up. Black has a distinct high-gain-oriented library; its shared global setup does not imply identical effects to Guitar or Bass.

Iridium provides Favorite and bypass, **not onboard preset-down/up**. Its EXP socket is shared with Digital/MIDI remote control; do not promise a directly connected analog expression pedal and an external preset controller at once through the same jack. It is an amp/cab/room platform, not a general-purpose multi-effects chain. Its active-inventory scope remains pending, so it is not used to inflate the existing catalogue count.

H9 Max and H90 satisfy the global-control research question but lack headphone amplifiers. They are not headphone-equipped all-in-one substitutes. H9 Max, H90 and H9 Gen2 are separate products; do not transfer settings or wiring between them by name similarity.

## Indonesian hardware offers — do not confuse channels or bundles

| Exact model | Observed asking price | Evidence and limitation |
|---|---:|---|
| POD Express Guitar | **Rp3.099.000**, indexed2026-10-18 | [Seven Stereo Shopee hardware page](https://shopee.co.id/Line-6-POD-Express-Guitar-INT-P38-1-i.16879370.26763471564). The older Rp3.030.000 observation is preserved in LINE6.md. Not verified checkout stock; **not a Black price**. |
| H9 Max | **Rp11.344.000** | [Melodia Indonesia](https://www.melodiamusik.com/product/eventide-h9-max-harmonizer/). Retail page displays regional availability; not warehouse confirmation and **not Shopee**. Condition/bundle and used offer unresolved. |
| Iridium, specific original product page | **Rp8.170.000, Pre-Order Now** | [Swee Lee Indonesia](https://www.sweelee.co.id/en/products/strymon-iridium-amp-and-ir-cab-guitar-effects-pedal). Not Shopee or immediate-stock confirmation. A separate w/o-adapter product appears at another price; do not merge bundle variants. |
| POD Express Black, H90 | **Unverified** | No exact usable current Shopee Indonesia hardware offer established. Unrelated H90 cameras, overseas retailers, plug-ins and other POD variants are not replacements. |
| Nano Cortex, RP55, B2 FOUR, TONEX Pedal | **Not refreshed in this capability pass** | Preserve previous prices where present; a technical near-miss does not justify manufacturing a new/used market range. |

**No newly discovered candidate has every requested buying criterion verified simultaneously**: exact fit, global volume, controller compatibility, desired preset workflow, and matching current Shopee stock. The price table is evidence of specific offers, not a ranked list of purchase-ready matches. No currency conversion, used-price percentage, automatic voucher or completed-sale inference is used.

## Other compact or no-treadle leads

### Relevant but not cleared by this audit

| Model / family | Current research disposition |
|---|---|
| **Hotone Ampero Mini MP-50** | Official product establishes134 ×120 ×49 mm, external EXP/CTRL and headphones. A current-firmware **global volume assignment is not established** by the retrieved material. A failed large-manual download is not evidence of No. Revisit its exact current manual/settings before recommending. [Official product](https://www.hotone.com/products/multi-effects/Ampero%20Mini) |
| **BOSS GT-1000CORE** | Already discussed, not a new discovery. Preserve the full existing [BOSS record](effects/guitar-boss.md); a normalized capability field with exact current manual references remains to add. |
| **Line 6 HX Stomp / HX Effects / HX Stomp XL** | Existing models, not newly found. Global EXP Position must not be called global volume insertion. Fresh firmware-matched output-controller/assignment review remains open; see [LINE6](LINE6.md#hx-family-distinction). |
| **Valeton GP-50** | Existing discussion established no documented global EXP assignment in the inspected firmware. This audit does not upgrade that to a permanent No for future firmware. It remains a purchase plan, not confirmed ownership. |
| **VING Flybro FB-100** | Already-owned comparison reference, not a purchase candidate. Prior claim about Global VOL still needs exact manual/firmware persistence confirmation; do not upgrade a promising menu label to a tested guarantee. |
| **Zoom G2 FOUR, G3/G3X legacy; DigiTech other RP models** | Separate model-specific manual work remains. Do not copy B2 FOUR dimensions or RP55 wiring/behavior to them. |
| **Eventide H9 Gen2; other newly found no-treadle families** | Research leads only until exact primary manuals, size and Indonesian hardware offers are obtained. H9 Max/H90 findings are not inherited automatically. |

### Size exclusions inherited from existing repository research

These are a **repository-based screen**, not newly certified expression-volume mappings. Full source URLs and unresolved qualifiers remain in the linked brand records.

| Model | Existing recorded chassis information | Disposition |
|---|---|---|
| NUX MG-200 |240 ×155 mm |Too wide and deep; external pedal capability does not make it compact. [NUX](NUX.md) |
| NUX TRIDENT NME-5 |312 ×164 mm |Too wide and deep. [NUX](NUX.md) |
| NUX Cerberus NME-3 |320 mm width; depth-source conflict retained in record |Width already fails, irrespective of unresolved depth. [NUX](NUX.md) |
| M-VAVE TANK-PRO |260 ×100 mm |Width fails even though external EXP is documented. [M-VAVE](M-VAVE.md) |
| Hotone Ampero II Stomp MP-300 |185 ×145 mm |Depth fails by5 mm. [Existing full record](effects/findings/2026-10-15-hotone-ampero-ii-stomp-mp300.md) |

Built-in-treadle models remain outside this sub-comparison even if they also accept an external pedal. Owned/donated devices are not reintroduced as new purchases. Models with only USB/MIDI control need a controller/host and do not satisfy the direct analog-EXP requirement merely because a MIDI CC can change volume. GM-800's system-wide synth volume does not solve ordinary pickup audio routing.

## Controller wiring and acceptance test

The multipurpose socket's TRS label does not make all controllers interchangeable. POD Express illustrates **TS for a single expression pedal**, with a specified splitter for expression plus a switch. RP55 explicitly **does not support TRS expression pedals**. H9's connector table says mono; H90 and Iridium have their own specifications. Check the particular M-VAVE model, resistance, polarity, wiring and sweep rather than guessing from a quarter-inch connector.

Before treating a model as a complete match, test at low monitoring volume: pedal heel/middle/toe in at least three different presets; switch presets without moving the pedal; confirm heel-down range; repeat with the device bypassed; check headphones separately; test any room/delay/looper tails; power-cycle and confirm assignment persistence. No physical test is claimed in this research.

## Evidence and remaining coverage

Detailed manufacturer links, firmware/manual versions, failed-download limits and source-specific qualifications are stored in **LINE6.md, EVENTIDE.md, NEURAL-DSP.md, DIGITECH.md, ZOOM.md, IK-MULTIMEDIA.md and STRYMON.md**. This capability work does not delete or fully consolidate legacy technical records.

Remaining work is explicit in research-state.json: normalize the existing non-treadle inventory; resolve current-firmware global assignments for Mini/Nano/GP-50 and any other eligible compact lead; verify the actual controller; re-search exact Shopee hardware offers; keep price channels/conditions separate; and reconcile older inventory/navigation counts. **Do not mark the audit complete or infer a negative answer for an uninspected model.** The separate general research cursor GP-200JR → HeadRush Prime → GE300 is preserved.
