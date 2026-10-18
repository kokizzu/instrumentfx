# Eventide multi-effects

## H9 Max

Checked 2026-10-17; partial. Max is distinct from Standard/Core; ownership unverified.

| Field | Evidence / qualification |
|---|---|
| Instrument scope | **Guitar and bass:** own manual p43 offers GUITAR, BASS, SYN.LD and SYN.BAS source modes, optimizing pitch algorithms and filter ranges for that source. Vocal suitability remains unclassified. [M][H9-M] |
| Expression / pedal plus auxiliary switch | Manual explicitly permits **expression plus one ring-contact auxiliary switch** through aY lead onthe sharedEXP socket;with expressioninuse,onlyRNGswitch remainsavailable. This is not threeauxswitches plus expression,anddoesnot independentlyestablish aphysical toe switch. [Own manual pp33–34][H9-M] |
| Live / bypass tails | **DSP** isdefault buffered bypass;**RELAY** hardwires inputs tooutputs andalso engages automatically withoutpower;**DSP+FX** mixes dryinput withthe currenteffect’s decayingtail. This establishes effect-bypass tails,not patch-change spillover. WithKilldry enabled,DSP bypass mutes theeffect instead ofpassingdry. [Own manual pp15–16][H9-M] |
| Expression / input versus output swell | Swell attenuates beforeoraftertheeffect withoutboost;input swell lets existingeffects decay,output swell fadesprocessed output. GlobalSwell overridesper-preset choice anddisables ordinarypedal/HotKnob mappings. Swell isinactive inbypass andaffects onlythewet channel inPre/Post orWet/Dry routing. [Own manual p14][H9-M] |
| Expression | No built-in pedal. External EXP controls multiple parameters;5–25kΩ linear pot, auto-calibration. EXP alternatively supports 3 momentary switches;toe-switch support unknown. Manual calls EXP stereo, product table says mono: retain connector conflict. [M pp25–26][H9-M] |
| Knobs / footswitches / buttons | **1 rotary/2 footswitches/5 buttons**:encoder;left/right;HOTKNOB,X,Y,Z,PRESETS. Encoder press counted once; derived from text, not visual inspection. [M pp7–9][H9-M] |
| Display | **Six-character alphanumeric LED display**, plus LightRing; diagonal, monochrome/color and touch specifications remain unverified. [M p18][H9-M] |
| Processing / choices | **52 algorithms**,from TimeFactor, ModFactor, PitchFactor, Space and H9-specific families. Guide contents reconcile **Space 12 + PitchFactor 10 + TimeFactor 10 + ModFactor 10 + H9-specific 10 =52** [G pp1–2][H9-G]. **One preset operates both channels; two presets cannot run simultaneously**. Fixed combined algorithms are not free block chains. [P][H9-P],[M p10][H9-M] |
| Factory / user memory | **99 onboard slots, 99 factory presets, editable/saveable**;not 99 factory + 99 extra user. App offers 500+ presets, not additional onboard slots. [P][H9-P],[M pp7,18][H9-M] |
| Synth / acoustic | **HotSawz:** 6 saw oscillators follow a mono pitch tracker, low-pass filter. **Synthonizer:** additive voice A/subtractive voice B; input 1 only, input 2 disabled, no tempo mode. Acoustic simulation remains unverified. [G pp31,75][H9-G] |
| Dimensions / mass | Product labels **133H×118W×50Dmm;0.7kg**. Axis labels are unusual for a floor pedal; retained without normalization. [P][H9-P] |
| Audio / control I/O | Two ¼-inch mono inputs, two ¼-inch mono outputs,EXP,mini USB 2.0, MIDI IN and OUT/THRU 5-pin DIN,DC. **600kΩ input, 470Ω output, load ≥10kΩ**. No headphone connector in the published list. USB audio unverified; USB MIDI documented. **USB connected disables DIN MIDI activity, including thru** [M p27][H9-M]. [P][H9-P] |
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

### H9 Max — bass source mode and MIDI transport

Checked 2026-10-17 against [own H9 User Guide][H9-M], printed pp5,27,43,47. The BASS/SYN.BAS modes explicitly optimize pitch algorithms and filter ranges; they establish bass capability, not uniform performance for every algorithm. This supersedes the earlier unclassified bass scope. USB priority excludes concurrent DIN MIDI, including MIDI thru. A Windows “USB Audio Device” driver name does not by itself establish audio streaming. USB audio, bus power and capture/IR import remain unresolved.

The same manual’s DC connector specification says **2.5×5mm**, whereas the product page says **5.5/2.5mm**; retain this outer-diameter discrepancy alongside the existing EXP mono/stereo wording conflict. Do not silently substitute Gen 2 power specifications. No hardware operation or file download.

## H90

Checked 2026-10-17; partial. Separate from original H9 Max and H9 Gen 2. Ownership unverified.

| Field | Evidence / qualifications |
|---|---|
| Instrument scope | Guitar; vocal path requires external MixingLink in the manufacturer example. No direct XLR mic/phantom input. **Bass capability verified:** own Source Type settings include Bass(Tenor) and Sub(Bass), adjusting pitch tracking, filters and tone controls. [Global1.12.5][H90-B] [P][H90-P] |
| Expression | No built-in pedal; two TRS EXP/CTL inputs accept 10–25kΩ pedals, 0–5V CV on tip, or 1–3 normally-open momentary switches. Toe support unverified. [Rear][H90-R] |
| Knobs / footswitches / buttons | **5 rotary /3 physical footswitches /7 buttons**, text-derived: Select, Perform, three Quick Knobs; Programs, Routing, Presets, Parameters, P/A/B. Push encoders counted once. Product’s six programmable footswitch functions are not six physical switches. [Top][H90-T] |
| Display | OLED; diagonal, resolution, monochrome/color and touchscreen unverified. [Top][H90-T] |
| Processing / choices | Current product headline **74=52 H9-derived+22 newer algorithms**; **Manual1.12.5 reconciles74 effects**, excluding Mute/Thru utilities; release1.12.5 introduces the four granular algorithms. Installed firmware unknown. [Guide][H90-G],[Release][H90-F] **Two algorithms per Program**, series/parallel, with spillover. Two mono inserts or one stereo insert; Dual mode can process two stereo instruments. [P][H90-P] |
| Memory / reset scope | **Clear Current State preserves saved Lists,Programs andPresets**,but clears theloaded Program andresets System/Tempo settings. **Factory Reset erases all user Lists,Programs andPresets** andresets System/Tempo;it doesnot downgrade installedsoftware. Neither operation was performed. These are different recovery scopes,not proof of factory-fill counts. [Own1.12.5 Startup](https://cdn.eventideaudio.com/manuals/h90/1.12.5/content/appendix/startup.html) |
| Editor / library load and overwrite | H90 Control Library auto-load selects aProgram immediately whenenabled;withitoff,selection previews anddouble-click/Enter loads. Dragging aProgram to aPlaylist location overwrites thatlocation;locked Factory Programs cannotbeoverwritten. Duplicate filtering/UseCount concern repeatedlist memberships,not additionalunique Programs. [Own1.12.5 Library](https://cdn.eventideaudio.com/manuals/h90/1.12.5/content/h90-control/program-library.html) |
| Factory / user memory | **Up to99 Programs per List**; editable User Lists and read-only Factory Lists, first User List factory-populated. Total list count, total capacity and exact factory fill unresolved. A Preset is one algorithm’s settings; a Program contains two. Only User Lists can be the active Playlist; Factory Lists remain searchable. Library Use Count tracks reuse across lists, so list memberships are not automatically distinct stored sounds. [Global][H90-B],[Library][H90-U] [Terminology][H90-M] |
| Synth / acoustic | **PolySynth:** SIFT polyphonic guitar-to-synth, up to3 synth voices; Playstyle trades pure mono tone against polyphonic tracking. **HotSawz:**6 saw oscillators follow mono pitch tracking. **Synthonizer:**additive A/subtractive B voices with reverb. Acoustic simulation and Synthonizer input/tempo restrictions unverified. [Synth manual1.12.5][H90-Y] [P][H90-P] |
| Dimensions / mass | Product: **170W×136D×68Hmm;0.84kg**, also6.5W×5.25D×2.5Hin. Manual1.11.4: **179W×136D×65Hmm;1.36kg**, also1.85lb. Retain conflicting metric axes/mass and inch/metric mismatch; do not silently convert or choose. [P][H90-P],[Specs][H90-S] |
| Memory / routing-mode compatibility | **Insert and Dual routing use alternate Program/List sets**; a Program/List created in one cannot directly serve the other. H90 Control export/reimport offers conversion after changing modes. This is a compatibility boundary, not evidence of erased lists or doubled physical memory. [Routing manual1.12.5](https://cdn.eventideaudio.com/manuals/h90/1.12.5/content/edit-modes/routing.html) |
| Routing / insert compensation | Each insert has send/return levels,mix,normal/inverted polarity,**0–512 samples latency compensation** andTails. Tails On permits inserted effects to decay on bypass;Off immediately mutes the insert. Compensation is additional to the documented3.8ms insert latency,not latency removal or a measured external-device value. [Own1.12.5 routing](https://cdn.eventideaudio.com/manuals/h90/1.12.5/content/edit-modes/routing.html) |
| I/O / mono summing limits | Auto uses connected jacks:mono uses I/O1,stereo-to-mono sums atoutput1;Path2 usesI/O3 equivalently. A mono insert atchainend sumsoutput tomono;parallel mono insert canretain stereo. **Force Mono sums dry andalgorithm paths**,duplicating them atoutputs1/2 regardless ofstereo cabling. Do not infer independent stereo processing fromtwo connected outputs inthatmode. [Own1.12.5 I/O](https://cdn.eventideaudio.com/manuals/h90/1.12.5/content/system-menu/io.html);[routing](https://cdn.eventideaudio.com/manuals/h90/1.12.5/content/edit-modes/routing.html) |
| Audio / control ports | Four¼TS inputs/four¼TS outputs, each instrument/line configurable; two¼TRS EXP/CTL, MIDI DIN IN/OUT-THRU, USB-C, DC. USB for control/update/MIDI; audio streaming unverified. No headphone socket in complete inventory. [Rear][H90-R] |
| Power / battery / USB | Included **12V1A center-positive,5.5/2.5mm** supply. Manual power table lists **12V600mA or9V800mA** operating requirements, distinct from included adapter rating. Measured draw, battery and USB bus power unverified. [Rear][H90-R],[Specs][H90-S] |
| Processing / conversion and latency | **48kHz;24-bit AD/DA;32-bit float DSP**. Manual:parallel3.8ms/series4.5ms;each insert adds3.8ms plus configured compensation. Not USB audio format evidence. [Specs][H90-S] |
| IR / NAM / capture import | Unverified; preset/list import is not proof of IR or amp capture. |
| Editor / platforms | Current **Eventide Control Mac/PC/iPad**, Bluetooth/USB-C; older manual calls it H90 Control. Desktop **Eventide Control2.2.0 requires H90 firmware1.9.4+**; **Current Eventide Control requirements:Windows10+ Intel,macOS10.14+ Intel/Apple Silicon,iPadOS15+**;Bluetooth explicitly Mac/iPad. Older H90 Control manual1.12.5 lists macOS10.13+,Windows10+,iPadOS15+;retain application distinction. iPad app version pending. [Current app][H90-C],[Older app manual][H90-CM]. [Downloads][H90-D] [P][H90-P],[Rear][H90-R] |
| Looper / drums / live | Tuner and **0–30s configurable spillover** documented. DSP bypass allows tails; relay does not and is unavailable on Dual Path2(I/O3–4). AB Only bypasses A/B while leaving inserts active. [Global1.12.5][H90-B]; **Looper stereo:60s full-quality headline; speed table2x60s/1x120s/½x240s/¼x480s**, slower recording trades fidelity for length. Undo/redo, reverse, MIDI clock, one-button control; Punch/Repl-Punch unavailable in one-button mode. Max length only changes while empty. **Three HotSwitch parameter snapshots, one active at a time**; Perform mode supplies two assignment pages for the three physical footswitches. Drums unverified. [Parameters1.12.5][H90-PA],[Perform1.12.5][H90-PF] [Looper1.12.5][H90-L] [P][H90-P] |

### H90 — separate IDR hardware evidence

| Price class | Evidence / qualifications |
|---|---|
| Verified used | Unknown |
| Verified new | Unknown |
| Condition unverified | **Rp17,240,000**, [Swee Lee Official Shop][H90-O],Kota Jakarta Utara,seller799119783/item26020027851. Search crawl3months; direct indexed page2months,checked2026-10-17. Stale28–29June delivery. Exact hardware title; condition, bundle, warranty, voucher, shipping/tax, authenticity and checkout stock unverified. Historical ask, not completed sale. Store name does not establish new condition. |

No downloads or image inspection. Product checked now; manual sections explicitly version1.11.4, not proof of seller-unit firmware. No sibling specifications borrowed.

[H90-P]: https://www.eventideaudio.com/pedals/h90/
[H90-T]: https://cdn.eventideaudio.com/manuals/h90/1.11.4/content/hardware/top.html
[H90-R]: https://cdn.eventideaudio.com/manuals/h90/1.11.4/content/hardware/rear-side.html
[H90-S]: https://cdn.eventideaudio.com/manuals/h90/1.11.4/content/appendix/specifications.html
[H90-M]: https://cdn.eventideaudio.com/manuals/h90/1.11.4/content/terminology.html
[H90-O]: https://shopee.co.id/Eventide-H90-Harmonizer-Stompbox-Multi-Effects-Pedal-i.799119783.26020027851

### H90 — firmware-qualified effect inventory

Checked2026-10-17 against [manual1.12.5 index][H90-G]. Counts derived from its named entries; **12+5+1+4+13+4+1+16+1+14+3=74**, plus two utilities outside the effect total. Lineage differs from H9’s grouping.

| Field | Choices |
|---|---|
| Processing / Delay12 | Band Delay, Bouquet Delay, Digital Delay, Ducked Delay, Filter Pong, Head Space, Mod Delay, MultiTap, Reverse, Tape Echo, UltraTap, Vintage Delay |
| Processing / Distortion5 | Aggravate, CrushStation, PitchFuzz, Sculpt, WeedWacker |
| Processing / EQ1 | EQ Compressor |
| Processing / Granular4 | Cosmic Web, Glitch, GrainMod, Stutter |
| Processing / Harmonizer13 | Crystals, Diatonic, H910 H949, HarModulator, HarPeggiator, MicroPitch, Octaver, PitchFlex, PolyFlex, Polyphony, Prism Shift, Quadravox, Resonator |
| Processing / Harmonizer+4 | Quadravox+, VocalShift, VocalShiftMIDI, VocalTune |
| Processing / Looper1 | Looper |
| Processing / Modulation16 | Chorus, Even-Vibe, Flanger, Harmadillo, Instant Flanger, Instant Phaser, ModFilter, Phaser, Q-Wah, RingMod, Rotary, Sticky Tape, TremoloPan, Tricerachorus, Undulator, Vibrato |
| Processing / Multi1 | SpaceTime |
| Processing / Reverb14 | Blackhole, DualVerb, DynaVerb, Hall, MangledVerb, ModEchoVerb, Plate, Reverse Reverb, Room, SP2016 Reverb, Spring, Shimmer, TremoloVerb, Wormhole |
| Processing / Synth3 | HotSawz, PolySynth, Synthonizer |
| Processing / Utility2 | Mute, Thru; not added to74 |

[Release1.12.5][H90-F] explicitly introduces four granular algorithms. This establishes their version requirement; it does not prove the seller unit has that update or that1.12.5 is the newest release. No software was installed.

The [looper page][H90-L] retains its60s full-quality headline alongside the speed-dependent table. Do not infer120s at1x has the same fidelity as the headline. One-button control supports record/play/overdub, hold undo/redo and double-press stop; punch modes require dedicated transport controls. Stereo looper limits are not borrowed from H9 Max.

[H90-G]: https://cdn.eventideaudio.com/manuals/h90/1.12.5/content/algorithms/index.html
[H90-F]: https://www.eventideaudio.com/forums/topic/h90-software-latest-h90-release-1-12-5/
[H90-L]: https://cdn.eventideaudio.com/manuals/h90/1.12.5/content/algorithms/looper.html
[H90-D]: https://www.eventideaudio.com/downloads/?product=H90

### H90 — bass, bypass and library limits

Checked2026-10-17 against the [1.12.5 Global chapter][H90-B] and [Program Library chapter][H90-U]. Bass/Sub source modes are explicit capability evidence, not an inference from a low-frequency EQ knob. The source labels also describe sonic range; not every algorithm is equally suitable for every source.

DSP/Relay Program bypass both bypass inserts; AB Only retains inserts. Relay bypass cannot serve Dual Path2, though Path1 supports it and automatically uses relay if no presets occupy that path. Spillover’s adjustable0–30s limit qualifies the earlier general claim.

Only one User Playlist is active. Factory Programs are locked; Use Count records their occurrence across lists.99 Programs per List is not a99-Program total-storage claim. Searches did not establish a reliable published maximum list count or physical storage limit; no unlimited-memory claim adopted. No operation, download or visual inspection.

[H90-B]: https://cdn.eventideaudio.com/manuals/h90/1.12.5/content/system-menu/global.html
[H90-U]: https://cdn.eventideaudio.com/manuals/h90/1.12.5/content/h90-control/program-library.html

### H90 — editor platform qualification

Checked2026-10-17. [Current Eventide Control page][H90-C] explicitly includes H90 and separates its supported systems from the [H90 Control1.12.5 manual][H90-CM]. The current page’s macOS10.14+ requirement is not silently replaced with the older10.13+ minimum. Windows support explicitly says Intel;ARM Windows support is unverified. Bluetooth is listed for Mac/iPad, not established for Windows. Android/Linux editors remain unverified.

Eventide Control imports original H9 preset lists, but its supported-device list names H9 Gen2 rather than original H9 Max. File compatibility does not establish original H9 Max hardware control. No original-H9 software record was changed.

The [H90 FAQ](https://www.eventideaudio.com/faqs/?product=H90) rendered only its heading/navigation. Forum searches surfaced USB-audio requests and a negative reply, but author identity was not exposed in the retrieved thread; no unsupported primary-author attribution or definitive hardware limitation adopted. USB audio/bus power remain unverified. No application or driver downloaded or run.

[H90-C]: https://www.eventideaudio.com/software/eventide-control/
[H90-CM]: https://cdn.eventideaudio.com/manuals/h90/1.12.5/content/h90-control/index.html

### H90 — synth architecture and playing restrictions

Checked2026-10-17 against [own1.12.5 Synth chapter][H90-Y]. Three synth algorithms are alternatives within the documented two-algorithm Program architecture. PolySynth’s three synth voices are not three independent effect blocks or proof of a three-note input-polyphony ceiling. Its per-voice waveforms are saw, square, triangle, narrow pulse and wide pulse; a mapped pitch-wheel parameter spans±1200cents.

HotSawz has mono tracking despite six oscillators. Synthonizer combines additive/subtractive synthesis and reverb; the H90 chapter does not repeat H9’s input1-only/no-tempo limitations, so those restrictions remain unverified for H90. No guitar was connected, and no audio, software or firmware was downloaded or executed. Exact installed firmware remains unknown.

[H90-Y]: https://cdn.eventideaudio.com/manuals/h90/1.12.5/content/algorithms/synth.html

### H90 — performance mappings

Checked2026-10-17 in the own1.12.5 manual. HotSwitches store alternate parameter settings inside a Program; they do not add algorithms, physical switches or Program-memory slots. HotKnob P/A/B macros can control multiple parameters, including via expression mappings with reversible heel/toe ranges. [Parameters][H90-PA]

External aux or MIDI CC mappings remain usable in Select mode. Full latching/momentary/trigger behavior requires normally-open momentary switches, or MIDI CC values≥64 on press and≤63 on release. With Tempo Sync off, A/B taps can independently set algorithm times/rates; enabling sync makes that tap control the Program BPM. [Perform][H90-PF]

No hardware or app operation, downloads or image inspection. Installed firmware remains unknown.

[H90-PA]: https://cdn.eventideaudio.com/manuals/h90/1.12.5/content/edit-modes/parameters.html
[H90-PF]: https://cdn.eventideaudio.com/manuals/h90/1.12.5/content/play-modes/perform.html

### H90 — input headroom and specification-edition check, 2026-10-18

| Field | Manufacturer evidence / qualification |
|---|---|
| I/O / electrical limits | [Own manual1.12.5 specification table](https://cdn.eventideaudio.com/manuals/h90/1.12.5/content/appendix/specifications.html): input impedance **>600kΩ instrument /80kΩ line**, output impedance **220Ω**,recommended load **10kΩ**. Maximum input **+4dBu instrument /+14dBu line**. These are input limits,not maximum output ratings or measured clipping tests. The [product-page table](https://www.eventideaudio.com/pedals/h90/) instead prints **>80kΩ** for line input; retain the inequality distinction. |
| Dimensions / edition conflict persists | Manual1.12.5 repeats **65H×179W×136Dmm;1.36kg and1.85lb**,so the earlier1.11.4 versus product-page discrepancy is not resolved by this edition. Product distinguishes **0.84kg unit /1.36kg package**; that explains where1.36kg appears in its table but doesnot authorize silently relabeling the manual’s net-weight figure. |

The manual’s updated-spec shortlink redirected to the product page,but the returned body was a1.2-year cache with70algorithms/18new. It is not evidence to remove the firmware1.12.5 inventory of74 or claim a rollback. Cache age and document version remain separate.
