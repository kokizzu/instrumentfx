# Positive Grid — multi-effects discovery

[Repository](README.md) · [Expression-volume comparison](EXPRESSION-VOLUME.md)

<!-- brand-index begins -->
**Model and section index — A–Z, natural numeric order**

- [Spark PEDAL — partial no-treadle discovery](#spark-pedal--partial-no-treadle-discovery)
<!-- brand-index ends -->

## Spark PEDAL — partial no-treadle discovery

Checked **2026-11-01**; manufacturer-backed partial lead **outside active model/brand counts**, not fully verified. This is the audio processor, distinct from Spark Control, Control X and Spark amplifiers. No ownership assertion. The individual-LCD research queue retains priority; no individual LCD is established here.

| Field | Exact-model evidence / qualification |
|---|---|
| Instrument / expression | Electric, acoustic and bass input; no built-in treadle listed. Direct **¼-inch TRS EXP** for volume/wah. Resistance, taper, wiper wiring and external toe-switch compatibility remain unknown. [Panel][PG-PANEL] |
| Global volume / calibration | **Device Card → EXP Pedal Settings → Volume** assigns output volume; Wah LFO is another target. Calibration separately learns heel/toe range. This documents a device-menu target, not proven all-preset persistence, absence of preset overrides or saved/startup pedal position. Bluetooth Tone Control connection is required to access these settings. [Device Card][PG-DC] |
| Range / output coverage | Numeric attenuation endpoints, adjustable minimum/maximum, response curve, disconnect fallback, bypass, headphone, USB/Bluetooth backing-audio, tails and recorded-loop coverage remain unverified. Global EQ's documented output coverage must not be transferred to EXP Volume. |
| Controls | **5 rotary controls / 3 footswitches / 2 rear buttons** (Power, Pair); center-knob press counted once. Textual inventory, not visual census. [Product][PG-P];[Panel][PG-PANEL] |
| Displays | Multicolor LED indicators/ring are listed. LCD/OLED, diagonal, touch and individual switch-screen layout are not established. LED count is not a screen count. [Product][PG-P] |
| Chassis / mass | **L175 × W104 × H47.2 mm excluding knobs/switches; H54.8 including them; 0.56 kg**. The 175×104 rectangle fits the preferred 200×140 rectangle in one orientation; preserve published L/W axes. Cable clearance unmeasured. [Product][PG-P] |
| Power / battery | **USB DC5V/1A; 3000mAh rechargeable lithium-ion; up to7h play, about4.5h charge**. Published claims, not measurements. USB-C charging and USB audio can run together. Barrel polarity N/A for listed USB supply; other power methods unverified. [Product][PG-P];[USB][PG-USB] |
| Memory / factory / scenes | **6 custom preset locations, two banks of3**. Factory-filled subset, initially empty slots, scenes and full backup contents unknown. ToneCloud's100,000+ tones are community library content, not onboard capacity. [Canada product][PG-CA];[Navigation][PG-NAV] |
| Processing / categories | Product advertises **33 amps /43 effects**. [Linked app guide](#spark-pedal--fixed-chain-firmware-and-midi-boundaries) specifies seven fixed positions:one amp plus six effect slots. This establishes chain structure,not arbitrary duplicate blocks or a tested DSP ceiling. Four FX knobs each have four labeled choices; these are selectors, not16 simultaneous blocks. App can substitute additional effects at those positions. [Product][PG-P];[Modes][PG-MODES] |
| Shared-library conflict | Own PEDAL guide links the shared app list:36 amps minus3 LIVE/EDGE-exclusive preamps =33. Its51 effects minus7 starred LIVE/EDGE-exclusive effects =**44**, conflicting with43 on the product page. Residual category counts below are not a certified PEDAL inventory. [Own guide][PG-G];[App list][PG-LIST] |
| Synth / acoustic | Acoustic-guitar input and acoustic amp choices do not prove electric-to-acoustic conversion. Dedicated synth/tracking, native NAM, converted NAM, proprietary capture and user-IR import remain unknown. |
| Audio/control ports | ¼-inch instrument in; two¼-inch L/Mono,R line outs; **⅛-inch stereo headphones**;¼-inch TRS EXP; USB-C; two⅛-inch TRS MIDI in/out; Power/Pair. Two included MIDI-to-DIN adapters; TypeA/B wiring unverified. Input impedance, line balancing and headphone load/rating unknown. [Product][PG-P];[Panel][PG-PANEL] |
| USB / platforms | Manufacturer specifies **44.1kHz/24-bit,1In×2Out**, Mac/Windows audio; Windows driver required. Default recording is wet; dry recording requires bypassing amp and pedals. Mobile USB audio is not officially supported, rather than proven impossible. Desktop audio support is not a desktop editor claim. [USB][PG-USB] |
| Editor / wireless | Spark App **iOS15+ /Android8.1+**. Bluetooth5.0 supports app control and audio; Wi-Fi2.4GHz supports OTA firmware. Full desktop/Linux editor and installed firmware unknown; no Spark Control X profile behavior transferred. [Product][PG-P] |
| Firmware / listing | **2.10.1.175, September 9, 2026**, in the exact PEDAL release notes. Initial2.8.1.101 is also dated September9; article update October19 is not a separate release date. Installed firmware remains unknown. [Release notes][PG-FW] |
| Onboard preset down/up | Three switches select bank slots; hold saves. **FS2+3 toggles Red/Green banks; FS1+2 changes Preset/Looper mode**. This does not document a sequential preset−/+ pair. [Navigation][PG-NAV] |
| Looper / continuity | **60s per layer**, overdub/undo/clear. Manufacturer FAQ permits toggling preselected Red/Green presets while looping, but says leaving Looper Mode for other direct preset selection stops playback. Power-cycle retention, export, tails and EXP attenuation remain unknown. [Canada FAQ][PG-CA] |
| Used / new IDR hardware | No exact qualified Shopee Indonesia offer recovered. Condition, seller/item, bundle, stock, warranty and delivered IDR unknown; no related-model price or currency conversion used. |

### Shared-list residual census — not a verified PEDAL library

The October28,2026 [manufacturer app list][PG-LIST], reached from the [PEDAL guide][PG-G], explicitly restricts starred entries to specified LIVE/EDGE channels. Counting non-starred rows gives:

| List | Residual named rows |
|---|---|
| Amps | Clean5;Glassy4;Crunch5;High Gain5;Metal6;Acoustic4;Bass4 = **33** |
| Effects | Gate1;Comp6;Drive10;MOD/EQ12;Delay6;Reverb9 = **44** |

Keep the pedal's43-effect claim and this44-row residual separate. Do not arbitrarily remove Auto Wah or another row to force agreement, add the separately listed discontinued Hendrix purchase pack, or treat app availability as installed hardware content. The exact current PEDAL category census remains open.

No local downloads, software installation, device operation, checkout or visual inspection. Primary HTML documentation establishes the facts above; a mirrored quick-guide PDF exposed no extractable text, so its rewritten summary was not used. Next: resolve all-preset EXP scope/range/coverage, library discrepancy and exact Indonesian offers after LCD-first tasks yield new evidence.

### Spark PEDAL — fixed chain, firmware and MIDI boundaries

Checked **2026-11-01** against the manufacturer articles linked below. Shared app instructions are reached from the exact PEDAL app guide; do not transfer Spark Control X profiles.

| Field | Documented behavior / remaining limit | Evidence |
|---|---|---|
| Processing / fixed signal chain | **Gate → Comp/Wah → Drive → Amp → Mod/EQ → Delay → Reverb**. Seven positions include the amp; shared Comp/Wah and Mod/EQ categories are not extra parallel slots. CPU limits and arbitrary combinations were not tested. | [App instructions, updated October26,2026][PG-CHAIN];[PEDAL app guide][PG-APPGUIDE] |
| MIDI / preset addresses | Published **channel1, PC0–2 = Red1–3; PC3–5 = Green1–3**. Six addresses correspond to the existing six hardware memories, not additional slots or a sequential onboard−/+ pair. Channel configurability remains unverified. | [Own MIDI table, updated October28,2026][PG-MIDI] |
| MIDI / effects and tuner | CC0–6 address Gate,Comp/Wah,Drive,Amp,Mod/EQ,Delay,Reverb in that order;CC7 selects tuner. **0–63 off /64–127 on**,channel1. These are digital commands, not analog EXP wiring or a universal all-audio mute. | [Own MIDI table][PG-MIDI] |
| MIDI / volume and tap | **CC20:0 minimum,127 maximum** output volume;no dB endpoints supplied. CC8 counts each value change as a tap. Do not substitute a nonzero-trigger rule, analog pedal range or preset-recall guarantee. | [Own MIDI table][PG-MIDI] |
| Firmware / revision scope | **2.10.1.175** claims faster app/preset control, LED-ring/Bluetooth improvements and minor looper,wah,stereo-output fixes. Both it and initial2.8.1.101 are dated September9,2026. These notes do not specify global EXP recall, output coverage or fixes for every unit. | [Exact PEDAL release history, article updated October19,2026][PG-FW] |

No MIDI sent, presets changed, firmware downloaded or hardware tested. Analog Volume target scope, endpoint/recall/coverage and the43/44-effect discrepancy remain unresolved. Partial discovery status and active counts are unchanged.

### Spark PEDAL — app backups and looper applicability conflict

Checked **2026-11-01**. The [exact PEDAL app guide][PG-APPGUIDE],updated September18,2026,links both articles below. Their own scope and revision take precedence over assuming every linked instruction applies unchanged.

| Field | Evidence / qualification |
|---|---|
| Memory / app-library backup | [Backup article,updated October18,2026][PG-BACKUP]: **Tone Vault holds up to ten whole app-preset-library snapshots**,introduced in **Spark app4.6.0**. Restoring replaces the current library. Ten snapshots are not ten onboard presets,scenes or complete device images. The article does not establish backup of global EXP settings,firmware or recorded loops. |
| Editor / backup transition | Same article says **Dropbox backup support is being retired in2027**,recommending Tone Vault. It gives no exact retirement day. The older PEDAL index still describes Dropbox;preserve that dated wording rather than presenting it as the only current method. No account connected or backup performed. |
| Looper / model-scope conflict | PEDAL index labels its link “Simple Looper and Groove Looper on Spark PEDAL”,but the [linked article,updated October1,2026][PG-LOOPER],explicitly lists **Spark2 and Spark EDGE only**. Its power-cycle loop persistence and Groove drum instructions are therefore **not verified PEDAL capabilities**. Keep the separate own-model60-second looper evidence;PEDAL retention,Groove availability and expression attenuation of loops remain unknown. |

This narrows the app-backup field and records a manufacturer cross-reference conflict;it does not resolve full-system backup or global volume. Partial status and active counts remain unchanged. No local download or device operation.

[PG-P]: https://www.positivegrid.com/pages/spark-pedal
[PG-CA]: https://www.positivegrid.com/ca/pages/spark-pedal
[PG-G]: https://help.positivegrid.com/hc/en-us/articles/43231630507789-Spark-PEDAL-User-Guide
[PG-PANEL]: https://help.positivegrid.com/hc/en-us/articles/45070676594189-Panel-Overview
[PG-DC]: https://help.positivegrid.com/hc/en-us/articles/47758018318349-Device-Card-Settings
[PG-NAV]: https://help.positivegrid.com/hc/en-us/articles/47610328480013-Preset-Control-and-Looper-Control
[PG-MODES]: https://help.positivegrid.com/hc/en-us/articles/47610320664077-FX-Mode-and-AMP-Mode
[PG-LIST]: https://help.positivegrid.com/hc/en-us/articles/8140276955917-Amp-Effect-List
[PG-USB]: https://help.positivegrid.com/hc/en-us/articles/43231631097613-USB-Recording

[PG-APPGUIDE]: https://help.positivegrid.com/hc/en-us/articles/47499454651789
[PG-CHAIN]: https://help.positivegrid.com/hc/en-us/articles/8141176035725-Adjusting-Effects-and-Presets
[PG-MIDI]: https://help.positivegrid.com/hc/en-us/articles/47499545258509-MIDI-Control-Commands-Setup
[PG-FW]: https://help.positivegrid.com/hc/en-us/articles/43231598990861-Spark-PEDAL-Firmware-Release-Notes

[PG-BACKUP]: https://help.positivegrid.com/hc/en-us/articles/8141122585869-Backup-Restore-Presets-in-the-Spark-app
[PG-LOOPER]: https://help.positivegrid.com/hc/en-us/articles/47557771640461
