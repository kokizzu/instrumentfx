# MELOFTY — multi-effects discovery

[Comparison](../MULTI-EFFECTS.md#separate-displays-for-effect-footswitches) · [Repository](../README.md)

<!-- brand-index begins -->
**Model and section index — A–Z, natural numeric order**

- [AXOM MAX — partial discovery lead](#axom-max--partial-discovery-lead)
<!-- brand-index ends -->

## AXOM MAX — partial discovery lead

### Current evidence summary

Consolidated **2026-11-04** from the revision-qualified findings below; this is not a new hardware or firmware test. **Partial lead outside active counts.** Earlier dated tables remain evidence history, not the current list of wholly unknown fields.

| Field | Current evidence and remaining boundary |
|---|---|
| Displays / controls | Manufacturer V1.7.4: 7-inch color touchscreen, mini readouts, 4 rotaries, 9 footswitches, 4 named panel buttons plus power/lock. Six performance switches in documented modes. Importer explicitly reports nine individual switch displays; manufacturer physical census and LCD/OLED technology remain unresolved. A [retailer OLED claim](#axom-max--retailer-oled-lead-and-specification-conflicts) is separately qualified. Separate pedal readout is not added to nine. |
| Expression | Built-in toe-switched MASTER+EXP1 or EXP1+EXP2; MASTER Pre/Post and 0–100 endpoints. External EXP3, 10–100kΩ TRS; internal EXP2/EXP3 wording conflict retained. External global master assignment and headphone/USB/loop/tail coverage remain unknown. |
| Processing / memory | Two nine-slot chains, CPU-limited; 19 modules, advertised 880+ models, 504 locations and six Subpatch scenes. Default MIDI map separates two factory and two user banks, each126 locations; supplied/blank allocation remains manufacturer-unverified. [Recovered quick-guide19-entry list](#axom-max--recovered-quick-guide-processing-category-census) is documented; per-category algorithm counts andcurrent-firmware census remain pending. [Cross-chain slot occupancy](#axom-max--cross-chain-move-and-module-editing-boundaries) is separate from CPU availability. |
| Connections / power / body | Guitar TS, mic/line combo with switchable48V phantom, two sends/two returns, TS/XLR stereo mains, phones, EXP, MIDI IN/OUT-THRU and USB-C. Phones6.35mm is corroborated in several manuals; German specification3.5mm conflict remains. 9VDC/3A center-negative;381×230×73mm axes unlabeled;3.45kg. USB bus power is not established. |
| Loading / sound engines | Manufacturer documents WAV IR loading, .nam import and proprietary MFIM capture separately from Synth/Inst.Sim. NAM architecture/conversion limits, exact creative algorithms and input-note polyphony remain unresolved. Importer instrument examples and independent capacity claims retain their own evidence grades. |
| Software / live features | [Manufacturer V1.7.4 editor requirements](#axom-max--editor-platforms-versus-usb-audio-drivers) confirm Windows10+/macOS10.11+ for AXOM Controller, separately from USB audio drivers. Bluetooth mobile control; current Apple mobile minimum differs from older manual/flyer. USB8-in/8-out routing is documented, but sample-rate claims conflict. Six scenes, looper-context preset navigation, loop-audio import/export and full-backup workflow are documented; preset navigation and loop retention must not be generalized across modes. |
| USB / documentation conflict | [English and German USB7/8 wording](#axom-max--english-usb-conflict-and-editor-preset-operations) both permit reamp input yet contain an input-node prohibition in the dry-output paragraph. Actual routing remains untested. |
| Routing / output levels | [Manufacturer V1.7.4 global outputs](#axom-max--output-level-linkage-and-eq-destinations): UNBAL, BAL and PHONES have separate menus, global EQ and linkable L/R levels. Numeric range, recall and EXP3 assignment remain unverified. |
| Software / editor continuity | [Editor save prompts and Tail-Spill](#axom-max--editor-save-prompts-and-tail-spill-scope): global setting documented; effect/preset continuity and pedal coverage remain unverified. |
| MIDI / transport and tempo | [V1.7.4 receive/transmit settings](#axom-max--midi-transport-and-clock-roles) document USB MIDI in both directions, clock following versus clock output, and separate channel settings. Bluetooth audio/control does not establish Bluetooth MIDI. |
| Software / network services | [V1.7.4 network and Cloud scope](#axom-max--cloud-object-types-and-update-source-details): Wi-Fi login, five separate sound-file categories and an on-device update checker. These do not establish private/full backups, NAM export or current firmware availability. |
| Indonesia hardware | No qualified exact Shopee offer, live stock or separate new/used IDR established. Seller/accessory/bundle identity must be checked before adding a price. |

Sources, page references, historical claims and unresolved contradictions are retained in the detailed sections below. No current-firmware equivalence or ownership is inferred.

### Initial discovery baseline — 31 October 2026

Checked 2026-10-31. Manufacturer-authored **Axom Max User Manual V1.7.4, 2026-08-31**, 58 pages, recovered through the importer’s exact-model manual link: [original manual](https://shop.warwick.de/media/23/53/74/1790324346/4on4_MEL_AXOM_MAX_Manual_EN.pdf?ts=1790324346). Title/model/version identity checked; no host-generated FAQ used. Manufacturer website currently exposes no readable text.

| Field | Evidence / remaining gap |
|---|---|
| Hardware identity | Audio multi-effects/modeling processor, not merely a MIDI controller. Manual pp4–6 documents instrument input, effects processing and audio outputs. |
| Display layout | **7-inch color touchscreen plus footswitch/pedal mini screens** displaying assigned functions (manual p5). Exact mini-screen count, LCD/OLED technology, dimensions and one-per-switch placement remain unverified; panel screenshot retrieval failed. Nine numbered footswitches do not prove nine mini screens. |
| Expression | Built-in treadle; external EXP3 uses a stereo quarter-inch cable. Therefore outside the no-built-in-treadle shortlist. Global-volume scope/coverage and wiring remain unverified. |
| Software lead | Manufacturer’s [MELOFTY Android app](https://play.google.com/store/apps/details?id=com.melofty.axommax), published by Changsha Melofty Audio Technology, identifies Axom-series Bluetooth tone/hardware control; initially observed update2026-09-27; the later October listing is qualified below. App identity is not proof of every hardware feature. |
| Indonesian hardware | Exact Shopee offer and separate used/new IDR, condition, stock, bundle and warranty unverified; targeted search found no qualified hit. |
| Remaining profile | Controls, algorithm census, memory, complete I/O, power, mass/dimensions, IR/native-versus-converted NAM/capture, editor platforms and live-feature limits require full verification. |

**Partial lead outside active model/brand counts.** No files, apps, firmware or dependencies downloaded; no device operation or successful visual audit claimed.

### AXOM MAX — distributor flyer leads

Checked 2026-10-31: [English three-page flyer](https://shop.warwick.de/media/df/39/ee/1790778142/yf9_Melofty-Flyer_EN_ONLINE.pdf?ts=1790778142), exact Axom Max branding and ©2026 Warwick/W-Music Distribution identity. This is distributor-authored technical evidence, not manufacturer confirmation; original PDF text was readable but screenshot failed.

The flyer lists nine customizable footswitches,504 preset slots,six scenes per preset and two paths with up to nine slots each. None states the mini-screen count. It lists381×230×73mm (axes unlabeled),3.45kg,and included9VDC supply; polarity/current require independent verification. Ports: quarter-inch TS guitar,combo XLR/TRS mic-line,EXP,two sends/two returns,stereo quarter-inch phones,two XLR and two TS main outputs,5-pin MIDI IN/OUT-THRU,USB-C.

Software leads: AXOM Controller Windows10+/macOS10.11+; mobile Bluetooth management Android5+/iOS11+. NAM A2 support is claimed,not verified native `.nam` compatibility. Earlier unknowns remain dated provenance; this partial lead stays outside active counts pending manufacturer reconciliation.

### AXOM MAX — document identity and remaining display check

Checked2026-10-31: [manufacturer filing index](https://fccid.io/2BYCHSFT40) identifies Changsha Melofty Audio Technology and model SFT40. Its [user-manual exhibit9716561](https://fccid.io/2BYCH-SFT40/User-Manual/User-manual-9716561) is a new retrieval lead; [secondary document index](https://device.report/changsha-melofty-audio-technology/SFT40) names **SFT40 quick guide CN/EN V03,2026-06-18**,3 pages,331.93KB. The exhibit and [FCC attachment](https://apps.fcc.gov/eas/GetApplicationAttachment.html?id=9716561) were inaccessible; document-body identity and hardware revision remain unverified. Filing dates do not establish retail launch or installed firmware.

[Thomann’s exact-model search entry](https://www.thomann.pl/melofty_axom_max_audio_processor.htm?type=quickSearch) claims nine switches with individual displays; direct page returned cache miss. This is a **retailer lead**, not manufacturer confirmation of nine LCDs. The manufacturer site again returned zero readable lines. Retain the manufacturer-manual mini-screen evidence and unresolved LCD/OLED/count qualifications above; no active inventory admission. Next: retrieve the identified original quick guide or manufacturer panel documentation.

### AXOM MAX — manufacturer mobile-app requirements

Checked2026-10-31 against Changsha Melofty Audio Technology’s [MELOFTY Apple listing](https://apps.apple.com/us/app/melofty/id6762972347),explicitly titled **Axom Series Control Software**.

| Field | Developer-published scope / qualification |
|---|---|
| Editor / Apple mobile minimum | **iOS15.5+ /iPadOS15.5+**,current listed version**1.9.2**,relative release label“3d ago”. This differs from the distributor flyer’s iOS11+ claim;the older figure remains provenance,not current-version compatibility. |
| Editor / Mac boundary | The mobile app lists **macOS12.4+ with M1 or later**,but explicitly says **Not verified for macOS**. This is not the separate AXOM Controller desktop editor’s minimum or an Intel-Mac compatibility claim. |
| Editor / function scope | Developer describes Bluetooth preset/Subpatch control,global settings and stomp/expression mappings. Generic global-settings support does not prove global-volume assignment or coverage. App version is not hardware firmware. |

A newly surfaced [manual index](https://device.report/manual/21300124) links [an original-file candidate](https://device.report/m/63a022bc23df064392ad6523fb0e69573ed5ae7b06aa019d4e8601c2f649aa85_optim.pdf);the PDF returned cache miss. Its cleaned overview/troubleshooting text is not independently authenticated manufacturer documentation and is not adopted for specifications. Screen count/technology remain unresolved;no qualified Shopee hardware surfaced. No download,installation or active-inventory admission.

### AXOM MAX — manufacturer manual follow-up

Checked2026-10-31: [manufacturer V1.7.4 manual](https://shop.warwick.de/media/23/53/74/1790324346/4on4_MEL_AXOM_MAX_Manual_EN.pdf?ts=1790324346),text readable again;no local download or visual inspection. Earlier gaps are narrowed only as follows.

| Field | Revision-qualified evidence |
|---|---|
| Controls | p5: **4 rotaries,9 footswitches,4 named panel buttons** HOME/SYSTEM/SAVE/EXP;separate power/lock button. Encoder pushes not counted twice. Mini-screen count/technology still unresolved. |
| Expression / power | p57: external **10–100kΩ TRS** pedal;**9VDC,3A,center-negative** supply. Rating is not measured draw. |
| IR / NAM loading | pp51–52,55–56: AXOM Controller imports **.nam** files;WAV IR specifications48kHz/32bit/up to2048samples. Supported NAM architectures,conversion requirements and live import test unresolved;this supersedes the earlier lack of a manufacturer .nam workflow. |
| USB / source conflict | p57: **USB2.0,8-in/8-out,48kHz/24bit**; **own manualp33 also claims24bit,44.1–192kHz**. Thus the rate discrepancy is internal as well as distributor-versus-specification; supported rates remain unresolved. Do not treat32bit processing as USB resolution. |

Still a partial discovery lead outside active counts. New quick-guide link surfaced but web reader rejects its23.3MB size: [importer-linked guide](https://shop.warwick.de/media/96/42/2c/1791505539/7fj5_MEL_Axom_Max_Quick_Guide_EN.pdf?ts=1791505539).

### AXOM MAX — mini-screen labels and master-pedal scope

Checked2026-10-31,[own V1.7.4 manual pp22–24](https://shop.warwick.de/media/23/53/74/1790324346/4on4_MEL_AXOM_MAX_Manual_EN.pdf?ts=1790324346);manufacturer text only.

| Field | Evidence / qualification |
|---|---|
| Display / STOMP labels | Single-module control shows its module name;multi-module control shows **MULTIPLE**. Green/orange status refers to the footswitch icon/LED,not proof of color mini-screen pixels. Latching and momentary control are selectable. Physical screen count and LCD/OLED remain unresolved. |
| Expression / built-in MASTER | **MASTER+EXP1** selects master-volume/parameter roles via toe switch;master position can be **Pre/Post**,with minimum/maximum **0–100**. Alternative **EXP1+EXP2** provides two parameter roles. This documents the built-in treadle,not externalEXP3 master assignment or every-preset coverage. Headphone/tail/loop attenuation remains unknown. |
| Expression / naming conflict | p23 introduces externalEXP3 but then says externalEXP2;rear-panelp6 and controller selectorp24 identify **EXP3(EXT)**. Preserve this internal typo/conflict;do not invent a second external socket. Parameter assignments offer individual minimum/maximum values. |

Built-in treadle keeps this model outside the no-built-in-expression shortlist. No pedal operation or display visual inspection.

### AXOM MAX — USB routing and looper navigation

Checked2026-10-31,[ownV1.7.4 manual pp33–35](https://shop.warwick.de/media/23/53/74/1790324346/4on4_MEL_AXOM_MAX_Manual_EN.pdf?ts=1790324346). Panel screenshot still fails cache access;no visual count inferred.

| Field | Revision-qualified evidence |
|---|---|
| USB / route directions | Computer playback1/2 bypasses the effects chain;3/4,5/6,7/8 can feed chain inputs for reamping. Device-to-computer1/2,3/4,5/6 can carry chain outputs;7/8 carries dry A/B inputs. USB-only output nodes avoid duplicate hardware/software monitoring. This is routing,not proof of192kHz operation or master-pedal attenuation of computer playback. |
| Looper / navigation | Within Looper,holdFS1 to select FS8/9 preset−/+ or Subpatch−/+ navigation. OrdinaryFS8/9 instead control reverse/half-speed. Context-dependent navigation does not establish a permanent preset-down/up pair or uninterrupted loop playback across presets. |

### AXOM MAX — app revision and display lead qualifications

Checked2026-10-31. [Developer Apple history](https://apps.apple.com/us/app/melofty/id6762972347) lists **1.9.0,September29**:Synth/Inst Subpatch model switching and dynamic-response changes;long-press module copy/paste;Delay note range1/64–1/1 plus High/Low Cut;Pitch CPU reduction;MFIM(AMP/ENTIRE) Sharpness. These are developer release claims,not measured performance or confirmation of the required hardware firmware.1.9.2 remains separately listed as fixes.

[Importer exact-product text](https://shop.warwick.de/effektpedale-multieffekt-prozessorenmelofty-axom-max-hybrid-audio-processor) explicitly describes **nine footswitches with their own mini displays**. This strengthens the earlier retailer layout lead but does not resolve manufacturer-confirmed count,LCD/OLED technology,diagonal or color. The earlier unattributed OLED lead is now traceable to [Esse Music’s exact AXOM MAX listing](https://www.essemusic.it/en/shop/1024423-melofty-axom-max-162704), reopened **2026-11-01**: it explicitly advertises nine configurable footswitches with OLED displays. This is retailer wording, not manufacturer-confirmed screen technology or a visual census. Its 3.1 kg and 5 GHz Wi-Fi claims also differ from the existing 3.45 kg and 2.4 GHz evidence; do not import those specifications or treat the catalogue price as an Indonesia hardware offer. The model remains outside confirmed LCD matches and active counts. Browser surfaces were unavailable and original manual retrieval failed;no new visual count. Partial status and existing source qualifications remain.

### AXOM MAX — manufacturer memory and capture workflows

Checked **2026-10-31** against the [manufacturer V1.7.4 manual](https://shop.warwick.de/media/23/53/74/1790324346/4on4_MEL_AXOM_MAX_Manual_EN.pdf?ts=1790324346), printed pp28–30,50,55. Retrieved through the importer’s exact-model manual link; no local download or device operation.

| Field | Manufacturer evidence / qualification |
|---|---|
| Memory / capacity and model count | Specification table gives **504 preset tone slots,19 modules,880+ total effect models**. These are published totals, not a complete category census or880 simultaneous effects. Factory-filled versus empty allocation remains unverified. |
| Memory / DeepSynth quick presets | Browsing auditions a quick preset without changing the working preset. Loading it with the download icon **replaces the active user preset and its module parameters**; subsequent edits can be saved separately. Quick presets are not proven additional user locations. |
| Captures / on-device MFIM | Manual documents capturing overdrive pedals, amp preamps, complete amp rigs and speaker cabinets as digital models, with MELOFTY Cloud sharing. The full-amp example requires a microphone. This establishes a proprietary on-device capture workflow, distinct from cabinet IR import and `.nam` loading; it does not certify NAM export or every NAM architecture. |

The lead remains outside active counts. Mini-screen technology/count confirmation, category inventory, factory allocation and qualified Indonesian hardware evidence remain open.

### AXOM MAX — recovered quick-guide navigation boundaries

Checked2026-10-31. The previously inaccessible three-page quick-guide candidate is now readable through its [PDF reproduction](https://manuals.plus/m/63a022bc23df064392ad6523fb0e69573ed5ae7b06aa019d4e8601c2f649aa85_optim.pdf). Document identity is supported by the matching three-page/331.93KB filing-index metadata and the same named controls, connectors and MASTER/EXP architecture as the saved manufacturer manual. **English extraction has shifted-font encoding errors**; no clean visual inspection, printed revision/date or complete display census is certified. The host’s rewritten summary is excluded.

On English PDFp1, FS2 is labeled bank-up/Bank Select (hold: Looper); FS6 bank-down/Bank Select (hold: Tuner). Pressing both cycles selected footswitch modes. This documents **bank navigation**, distinct from the already-recorded contextual FS8/9 preset−/+ function inside Looper. It does not prove a permanent sequential preset pair or loop retention across presets.

The same connector text specifies8-in/8-out24-bit/48kHz USB-C, corroborating the saved manual’s specification table; it does not resolve the manual’s separate44.1–192kHz claim. Mini-screen count and LCD/OLED technology remain unverified; this partial lead remains outside active counts. No local download or device operation.
### AXOM MAX — CPU, scene linkage and headphone conflict

Checked **2026-10-31** through the importer’s current links;original documents,not generated summaries.

| Field | Manufacturer-document qualification |
|---|---|
| Processing / concurrency | [English V1.7.4,p12](https://shop.warwick.de/media/23/53/74/1790324346/4on4_MEL_AXOM_MAX_Manual_EN.pdf?ts=1790324346): **two nine-slot chains**,repeat loading within a category supported;CPU/resources can gray out unavailable models. Eighteen slots are not a guaranteed eighteen arbitrary simultaneous effects. |
| Memory / scene linkage | Samepp21–22: six SUBPATCH scenes share module types/counts. Bypass/parameters synchronize by default;enable a module’s SUBPATCH control for independent scene values. Saving remembers the active scene for next preset recall. Scenes do not multiply504 user locations. |
| Dimensions / mass | Samep57 independently corroborates **381×230×73mm;3.45kg**,previously a distributor lead. Axes remain unlabeled;do not silently assign them. |
| I/O / headphones conflict | Englishp57 specifies **¼-inch stereo**,matching its panel inventory. [German guide,p62](https://shop.warwick.de/media/33/3e/c1/1790324347/2itz_MEL_AXOM_MAX_Manual_DE.pdf?ts=1790324347) instead prints **3.5mm stereo**. Both list6Ω output impedance,not a required headphone load. Physical jack size awaits corroboration;preserve the contradiction. |

Mini-screen count/technology,complete category census andqualified Indonesian offers remain unresolved. Still partial,outside active counts;no local download ordevice operation.

### AXOM MAX — revision-qualified looper controls

Checked **2026-11-01** in the [German V1.7.4 manual,PDFpp34–35](https://shop.warwick.de/media/33/3e/c1/1790324347/2itz_MEL_AXOM_MAX_Manual_DE.pdf?ts=1790324347),63pages,exact AXOM MAX title andmatching named controls. English endpoint unavailable this check;no translation-based reconciliation ofexisting conflicts.

| Field | Documented operation / boundary |
|---|---|
| Looper / record andstop | FS6 cycles **Record→Play→Overdub**;FS7 short-press stops,long-press erases. German text requires multiple layers and playback stopped for FS2 **Undo/Redo**; [English V1.7.4 instead requires playback running](#axom-max--looper-undo-playback-state-conflict). Current behavior remains unresolved. |
| Looper / automatic start | Enable **Auto Record**,choose a threshold andpressFS6 toarm;recording starts when input reaches that threshold. With Auto Record off,FS6 starts immediately. Numeric threshold range is not established here. |
| Display / evidence boundary | GermanPDFp5 calls the footswitch/pedal readouts **mini displays**;no LCD/OLED classification established. It separately describes the LED light strip. Manufacturer-confirmed screen count andtechnology remain open. |

These actions supplement the preserved contextual FS8/9 navigation. They do not establish preset-change loop continuity,persistent storage orrecording duration. No download,device operation orvisual count;partial status andactive inventory unchanged.

### AXOM MAX — documented loop duration and pedal readout

Checked **2026-11-01**, [German V1.7.4 manual, PDFpp4,54,63](https://shop.warwick.de/media/33/3e/c1/1790324347/2itz_MEL_AXOM_MAX_Manual_DE.pdf?ts=1790324347),63-page exact-model document. English endpoint remained unavailable; the manufacturer website returned no readable text.

| Field | Documented evidence / boundary |
|---|---|
| Looper / published maximum | Overview explicitly specifies a **stereo phrase looper, maximum3,600seconds =60minutes**. This narrows the previous duration gap. Half-speed capacity, overdub storage, power-cycle retention and preset-change continuity remain unverified. |
| Display / pedal status | Troubleshooting identifies **MASTER on the pedal’s mini display** when in volume mode. This corroborates a pedal readout, not nine switch LCDs or additional analog EXP assignment. |
| Display / brightness scope | System settings list SCREEN BRIGHTNESS separately from AMBIENT LIGHT MODE. The text does not certify independent mini-screen brightness, LCD/OLED technology or numeric ranges. |

Partial lead remains outside active counts. No local download, firmware change, device operation or visual count.

### AXOM MAX — audio monitoring and recorded-loop backup

Checked **2026-11-01**, [German V1.7.4 manual,PDFpp4,6,49–50,54–55,58](https://shop.warwick.de/media/33/3e/c1/1790324347/2itz_MEL_AXOM_MAX_Manual_DE.pdf?ts=1790324347). Original text;no device operation orlocal download.

| Field | Documented scope / qualification |
|---|---|
| Audio / wireless and output controls | Bluetooth **audio input** supports backing tracks,separate from app control. UNBAL,BAL andPHONES each have global level/EQ controls,with linked orindependent L/R levels. These controls do not establish external EXP3 global-volume assignment orattenuation of every source. |
| Editor / recorded-loop backup | AXOM Controller documents looper-audio import/export;full backup/restore includes presets,samples,global settings andlooper recordings. This is a documented transfer workflow,not verified automatic power-cycle retention,file-format compatibility orour restore test. |
| Headphones / internal German conflict | PDFp6 explicitly says **6.35mm stereo**,while its specification tablePDFp62 says **3.5mm**. Thus the discrepancy is internal to this German document as well as between language versions. Both statements remain;physical jack size is unresolved. |

Mini-screen count/technology andqualified Indonesian hardware remain unresolved. This partial lead stays outside active counts.


### AXOM MAX — independent firmware1.9 review leads

Checked **2026-11-01** in [Thomas Dill’s original Bonedo hands-on review,2026-10-21](https://www.bonedo.de/artikel/test-melofty-axom-max-konkurrenz-fuer-line-6-neural-kemper-und-co/),which lists tested firmware**1.9.0**. This is independent firsthand reporting,not manufacturer specifications orour device test.

| Field | Review report / remaining qualification |
|---|---|
| Memory / supplied content | Reports **252 supplied presets in two folders**,within504 locations arranged asfour×126. This is a dated review-unit observation,not verified current factory allocation orproof the other252 areblank. Manufacturer factory-fill confirmation remains open. |
| Loading / capacity lead | Reports Loader capacity **100 NAM files(A1/A2) and100 cabinet IRs**. Exact supported architecture sizes,conversion,firmware dependency,slot sharing andfull-capacity behavior remain unverified;do not promote this to unrestricted native NAM certification. |
| Capture / firsthand operation | Author describes capturing his MarshallPlexi/4×12 rig withtwo microphones mixed through aChandlerTG2. This corroborates proprietary capture operation independently;it doesnot establish NAM export orall capture types tested. |

The article lists381W×230D×73Hmm,3.45kg;this is independent corroboration ofaxes,not a manufacturer drawing that resolves earlier unlabeled dimensions. Original manufacturer [shop page](https://www.meloftyaudio.com/shop/axom-max),linked byPremierGuitar,still exposes no readable text. Mini-screen technology/count andqualifiedShopee hardware remain unresolved. **Partial lead outside active counts**;no downloads ordevice operations.

### AXOM MAX — dated mobile update and remaining display boundary

Checked **2026-11-01** against the developer-published [Android listing](https://play.google.com/store/apps/details?id=com.melofty.axommax) and [Apple version history](https://apps.apple.com/us/app/melofty/id6762972347).

- Google Play now gives **2026-10-23** as the update date, superseding the earlier September27 observation for that listing. The retrieved page supplies no app version or minimum Android OS; “Fixed known issues” is not a specific hardware-firmware changelog.
- Apple’s **1.9.0, September29** notes additionally claim a **Simplified Noise Gate**, noise-gate performance changes, improved Wah audio quality, and tuner UI/bass-tuning improvements. These supplement the previously recorded Delay/Pitch/MFIM/Synth changes; they are developer claims, not measured results or proof of the required device firmware.

The current Apple listing still shows1.9.2 with a relative release label; no absolute date inferred. Neither app listing identifies the mini screens as LCD or OLED or confirms their physical count. The maker’s exact AXOM MAX shop page remains inaccessible in this reader. Existing manual, importer and retailer qualifications remain; this is still a partial lead outside active counts. No app, manual or firmware downloaded or run.

### AXOM MAX — translated-manual headphone corroboration

Checked **2026-11-01** in importer-linked original manual translations: [French V1.7.4](https://shop.warwick.de/media/f8/d7/95/1790900166/ghaq_MEL_AXOM_MAX_Manual_FR.pdf?ts=1790900166),59PDFpages, and [Polish V1.7.4](https://shop.warwick.de/media/bc/cc/92/1790900167/4bz8_MEL_AXOM_MAX_Manual_PL.pdf?ts=1790900167),63PDFpages. Exact model/version covers, panel controls and matching connection architecture identify these as AXOM MAX documents; translations are not independent hardware measurements. Page numbers below are one-based PDF pages.

| Field | Evidence / remaining limit |
|---|---|
| Headphones / corroboration | Frenchpp6,58 and Polishpp6,62 each specify **¼-inch/6.35mm stereo** in both panel and specification text. This strengthens the English and German panel wording;the German specification’s3.5mm contradiction remains preserved. Physical socket inspection is still pending. |
| Display / classification boundary | Frenchp5 still calls the switch/pedal readout a **mini screen** without establishing LCD/OLED technology or a physical census. Nine footswitch identities are not a verified nine-screen count. The retailer OLED statement remains attributed separately. |

Neither translation establishes later-firmware equivalence or a global external EXP3 volume assignment. No local document download,software installation ordevice operation;partial lead remains outside active model counts.

### AXOM MAX — six performance switches and hybrid screen roles

Checked **2026-11-02**,[manufacturer V1.7.4 manual,pp9–12,22–23](https://shop.warwick.de/media/23/53/74/1790324346/4on4_MEL_AXOM_MAX_Manual_EN.pdf?ts=1790324346). Original text,not a visual census orcurrent-firmware test.

- **FS3/4/5/7/8/9 are six performance controls**:RIG shows two preset groups;SUBPATCH shows six scenes;STOMP shows six stomp controls. Nine physical footswitches do not mean nine independent stomp assignments inthese documented modes.
- **HYBRID has three pairings**:SUB+PRESET,STOMP+PRESET,STOMP+SUB. SUB/STOMP offers123/456 selection. These pages change assignments,not physical screen count.
- In RIG,FS2/FS6 change paired groups,e.g.01–02→03–04. In SUBPATCH/STOMP,the first press previews the group;another changes it. This is distinct from sequential preset−/+ inside the looper.
- A momentary stomp action operates while pressed andreturns toits prior state onrelease. Latching retains its toggled state. Module names/MULTIPLE labels andLED colors retain the earlier qualifications.

For the collection’s count field,the [identified importer’s current exact-model page](https://shop.warwick.de/en/effect-pedals-multi-effects-processorsmelofty-axom-max-hybrid-audio-processor) explicitly reports **nine footswitches,each with its own mini-display**. Thus nine is an **importer-backed count**,not wholly unknown;primary confirmation ofthe physical census andLCD/OLED technology remains pending. The separate pedal readout mustnot be silently included inthat nine. Prior source statements remain preserved above. Partial profile,outside active counts;no local download ordevice operation.

### AXOM MAX — recovered quick-guide USB evidence

Checked **2026-11-03**:the previously inaccessible [original-file candidate](https://manuals.plus/m/63a022bc23df064392ad6523fb0e69573ed5ae7b06aa019d4e8601c2f649aa85_optim.pdf) nowopens as **three PDF pages**,matching the preserved331.93KB quick-guide index. The body has an English panel/connection sheet,a Chinese sheet andFCC text. Its extracted English glyphs are shifted;adding31 to the affected character codes restores contiguous English words andnumbers. This is text decoding,not executing document code. Host-generated overview/troubleshooting prose is excluded.

| Field | Recovered document text / qualification |
|---|---|
| USB / quick-guide wording | PDFp1 USB-C paragraph decodes as **8-in/8-out,24-bit/48kHz**,recording,reamp andUSB MIDI;also OTG smartphone/tablet recording/playback. This corroborates48kHz documentation,not exclusive sample-rate support orproof ofthe separate192kHz claim. No USB bus-power ormobile-editor support inferred. |
| Display / remaining access limit | Render requests produced no usable panel image. Physical mini-screen count/technology remain unverified bythis document;the importer-backed nine-screen count remains separately qualified. ExactV03 date/firmware attribution isnot established fromthis extraction. |

This narrows the earlier file-access failure without certifying allquick-guide details,currentfirmware orhardware. Partial lead remains outside active counts;no local download,installation ordevice operation.

### AXOM MAX — filing-photo retrieval leads and RF scope

Checked **2026-11-03** in the [SFT40 filing index](https://fccid.io/2BYCH-SFT40),identifying Changsha Melofty Audio Technology. It links original submission exhibits **[external photos9716546](https://fccid.io/2BYCH-SFT40/External-Photos/psi2604038-C01-R05-Appendix-II-external-photos-9716546)** and **[label/location9716543](https://fccid.io/2BYCH-SFT40/Label/Label-and-Label-Location-9716543)**,alongside the already-recorded quick guide. The exhibit bodies returned cache miss;the [FCC external-photo attachment](https://apps.fcc.gov/eas/GetApplicationAttachment.html?id=9716546) was inaccessible. These are exact next retrieval targets,not inspected panel photographs orproof ofretail hardware revision.

The mirrored grant/index lists **2402–2480MHz and2412–2462MHz** for its2026-10-11 authorizations. This supports a documented2.4GHz regulatory scope,not the retailer’s5GHz claim;it doesnot prove that unlisted5GHz hardware orother regional variants are absent. Filing frequencies do not identify LCD/OLED technology.

The maker-hosted [panel-image lead](https://www.meloftyaudio.com/banner-product-1.png) surfaced in image search butwouldnot open;generated image descriptions were excluded as evidence. Browser inventory was empty. **Nine footswitch mini-displays remain importer-backed**,withmanufacturer/visual count andtechnology pending;the separate pedal readout isnot silently added. Partial lead,outside active counts;no local download ordevice operation.

### AXOM MAX — tuner sources and global tempo scope

Checked **2026-11-03** against the [German V1.7.4 manufacturer manual,PDFpp19–20,33–34](https://shop.warwick.de/media/33/3e/c1/1790324347/2itz_MEL_AXOM_MAX_Manual_DE.pdf?ts=1790324347).

| Field | Revision-qualified evidence / boundary |
|---|---|
| Tuner / source and output | Select GUITAR IN,MIC/LINE IN,RETURN1 orRETURN2;choose BYPASS orMUTE. Calibration **430–450Hz,default440Hz**. HoldFS6 opens the tuner;shortFS6 exits. Tuner mute does not establish master-pedal attenuation of headphones,USB,loops or tails. |
| Tempo / preset scope | Touch drag,touchscreen tap,± controls orFS1 tapping set tempo. **Global Off** keeps tempo preset-specific;**On** applies the current value across presets. This is global tempo,not global expression-volume assignment. Numeric BPM limits andpower-cycle retention remain unverified. |

Mini-screen technology/manufacturer count andqualified exact Shopee Indonesia hardware remain open. The model stays a partial lead outside active counts;no installation,local download ordevice operation.

### AXOM MAX — separate send/return routing

Checked **2026-11-03** in the [German V1.7.4 manufacturer manual,PDFpp26–30](https://shop.warwick.de/media/33/3e/c1/1790324347/2itz_MEL_AXOM_MAX_Manual_DE.pdf?ts=1790324347). Exact-model original text;English endpoint was unavailable.

- A combined **FX LOOP** block places send andreturn at one chain location. Separate **FX SEND** and **FX RETURN** blocks permit different positions,including parallel external processing orA/B routing.
- The FX SEND **Dry=0** configuration is serial;**Dry≠0** is parallel. The manual also permits these ports to serve asadditional inputs/outputs when external-loop orfour-cable operation isnot needed.
- Its four-cable example uses a **Mono,Series** loop,with pre-effects before the loop block andpost-effects after it. This is documented configuration,not a tested wiring setup orproof ofarbitrary simultaneous DSP capacity.

This narrows routing details only. Mini-screen technology/manufacturer count andqualifiedShopee hardware remain unresolved;the partial profile stays outside active counts. No local download ordevice operation.

### AXOM MAX — global input controls and microphone power

Checked **2026-11-03** in the [German V1.7.4 manufacturer manual,PDFp49](https://shop.warwick.de/media/33/3e/c1/1790324347/2itz_MEL_AXOM_MAX_Manual_DE.pdf?ts=1790324347). Exact-model original text;no device operation.

The global input page separately selects GUITAR IN or MIC/LINE IN. It documents input-level adjustment and global noise suppression across presets,adjustable guitar-input impedance,and microphone preamp GAIN with switchable **48V phantom power**. Numeric gain/impedance ranges are not established here. Input-level adjustment does not prevent overload distortion from an excessively strong source.

These are input controls,not proof of external EXP3 global-volume assignment orcoverage of headphones,USB,loops andtails. Mini-screen technology/manufacturer count andqualified Indonesian offers remain open;this partial lead stays outside active counts.

### AXOM MAX — MIDI bank allocation and note-direction boundary

Checked **2026-11-03** in the [German V1.7.4 manufacturer manual, PDF pp40–41,44–45,47–49](https://shop.warwick.de/media/33/3e/c1/1790324347/2itz_MEL_AXOM_MAX_Manual_DE.pdf?ts=1790324347). Original text; English endpoint unavailable.

| Field | Revision-qualified evidence / boundary |
|---|---|
| Memory / default MIDI address map | Banks **0=FACTORY 1, 1=FACTORY 2, 2=USER 1, 3=USER 2** each map **PC0–125 to 01A–42C**: 126 locations. The advertised 504 locations are not 504 separately established user slots. Named maps do not certify factory filling, blank allocation or write protection; PC mappings are customizable. |
| MIDI / note direction and forwarding | Command matrix supports **Note receive, not Note send**; PC, CC and Clock are bidirectional. Separate **MIDI THRU** forwards incoming data through OUT. This does not establish guitar-to-MIDI note generation, DeepSynth note-trigger routing or input-note polyphony. |
| MIDI / learned control addresses | CC Learn is **empty by default**; users assign addresses. Bank-selection values 0–3 and EXP1/2/3 targets are functions, not fixed CC numbers or global-volume assignments. |

Mini-display manufacturer count/technology, qualified Shopee hardware and current-firmware equivalence remain unresolved. Partial lead stays outside active counts; no local download, MIDI transmission or device operation.

### AXOM MAX — chain endpoints and MULTI OUT coverage

Checked **2026-11-03** in the [German V1.7.4 manufacturer manual, PDF pp14–16](https://shop.warwick.de/media/33/3e/c1/1790324347/2itz_MEL_AXOM_MAX_Manual_DE.pdf?ts=1790324347). Exact-model original text; current-firmware equivalence untested.

| Field | Documented routing / boundary |
|---|---|
| I/O / chain inputs | Mono choices include Guitar, Mic/Line, Return1, Return2 and individual USB3–8. Paired choices include **GTR+MIC, RETURN1/2, USB3/4, USB5/6, USB7/8**; NONE is also available. Channel-pair processing does not establish synth input polyphony or a second physical guitar socket. |
| I/O / MULTI OUT | Explicitly includes **UNBAL OUT, BAL OUT, PHONES OUT and USB1/2**. Separate destinations include main-output pairs/sides, Phones, Send1/2 and USB pairs1/2,3/4,5/6; NONE and **TO CHAIN B** are distinct options. A destination list is not proof of master/EXP attenuation of every source. |
| Routing / quick-template initialization | **Parallel** initially assigns Guitar→Multi Out to A and NONE→NONE to B. **Series** instead sends A to Chain B, whose external input remains NONE. Selecting a two-chain template does not automatically configure two independently audible instrument paths. |

Manufacturer mini-screen count/technology, external EXP3 global-volume coverage and qualified Indonesian hardware remain unresolved. Partial profile stays outside active counts; no download, setting change or device operation.

### AXOM MAX — MFIM monitoring and capture refinement

Checked **2026-11-03** in the [manufacturer German V1.7.4 manual,PDFpp31–33](https://shop.warwick.de/media/33/3e/c1/1790324347/2itz_MEL_AXOM_MAX_Manual_DE.pdf?ts=1790324347). Original exact-model text;current-firmware equivalence untested.

| Field | Documented workflow / boundary |
|---|---|
| Capture / target monitoring | Before capture,the target can be monitored through UNBAL,BAL orPHONES while adjusting microphone position/preamp gain. Full-amp capture requires microphone/XLR. |
| Capture / comparison | After acquisition,the interface switches between target and captured model,with a corresponding live spectrum display. This is a comparison tool,not measured accuracy orlatency evidence. |
| Capture / refinement | Optional TONE CAPTURE refinement asks the player to cover all six strings,open through high frets,until100% progress. Separate **Gain,Model Volume andten-band EQ** adjustments refine the result. Progress is not a fidelity score;the six-string instruction doesnot prove bass capture is unsupported. |

Saved results remain proprietary MFIM models;no NAM export,arbitrary time-varying effect capture ornew synth capability is established. Mini-screen technology/manufacturer count andqualifiedShopee hardware remain unresolved. Partial lead outside active counts;no capture,download ordevice operation performed.

### AXOM MAX — manufacturer body and electrical ratings

Checked **2026-11-03**, [German manufacturer V1.7.4 manual,PDFpp61–62](https://shop.warwick.de/media/33/3e/c1/1790324347/2itz_MEL_AXOM_MAX_Manual_DE.pdf?ts=1790324347). Exact-model original table; no hardware measurement.

| Field | Published rating / boundary |
|---|---|
| Body / mass | **381×230×73mm**, axes unlabeled; **3.45kg**. Manufacturer corroborates the distributor figures; retailer3.1kg discrepancy remains. |
| Audio / inputs | Guitar andReturns **1MΩ,+10dBu maximum**;Mic/Line **2.4kΩ,+10dBu maximum,60dB mic gain**. Fixed ratings do not establish selectable impedance/gain ranges. |
| Audio / outputs | Unbalanced mains andXLR **600Ω,+18dBu maximum**;Sends **510Ω,+18dBu**;Phones **6Ω,+18dBu**. These are source ratings,not headphone load orpower. The3.5/6.35mm socket conflict remains. |

Partial,outside active counts. Display technology,category census,global external-pedal coverage andqualified Indonesian hardware remain open. No local download ordevice operation.

### AXOM MAX — creative-category evidence and qualified instrument examples

Checked **2026-11-03**. [Manufacturer German V1.7.4 manual, PDFpp19,30](https://shop.warwick.de/media/33/3e/c1/1790324347/2itz_MEL_AXOM_MAX_Manual_DE.pdf?ts=1790324347) explicitly separates **Inst.Sim, Synth, Amp, Cab and Amp & Cab** lists and identifies DeepSynth Quick Presets as instrument/synth sounds. Category separation does not certify exact algorithms, input-note polyphony or tracking quality.

The [identified importer’s exact AXOM MAX page](https://shop.warwick.de/en/effect-pedals-multi-effects-processorsmelofty-axom-max-hybrid-audio-processor), retrieved today, advertises **50+ synth sounds without a MIDI pickup** and **70+ instrument models**, with organ, saxophone, violin, flute and Asian-instrument examples. These are **importer claims and instrument families**, not manufacturer-verified algorithm names or a fresh installed-library census. Its separate vocal-instrument transformation claim likewise does not establish polyphonic voice tracking, simultaneous availability or MIDI-note routing. No electric-to-acoustic algorithm is established by these examples.

MFIM hardware capture, cabinet IRs and NAM import remain distinct from DeepSynth. This is now cross-linked as a partial creative lead, **outside active counts and the separate existing-catalogue index**. No ownership inferred.

Maker page and English manual remained inaccessible; German panel rendering failed and no in-app browser was available. A targeted Shopee Indonesia search yielded no qualified exact hardware offer. Preserve importer-backed nine mini displays, unresolved technology, existing contradictions and independent queues. No local download/device operation.


### AXOM MAX — touchscreen gestures and bank-window behavior

Checked **2026-11-03**, [manufacturer German V1.7.4 manual, PDFp54](https://shop.warwick.de/media/33/3e/c1/1790324347/2itz_MEL_AXOM_MAX_Manual_DE.pdf?ts=1790324347). Original system-settings text; no panel rendering or device test.

- **Gesture** selects Vertical or Rotate touchscreen parameter adjustment. This is a touch interaction setting, not rotary-encoder hardware or mini-display touch support.
- **BANK SWITCH OVER DISPLAY**: Manual leaves the bank-selection window for a held function-switch action to close; Auto closes it after preset selection. This is window dismissal, not automatic timed preset selection or proof of uninterrupted switching.
- **AMBIENT LIGHT MODE** offers Preset Sync, Pulse Breath and Signal Reactive. Lighting behavior does not establish LCD/OLED technology, screen color or independent mini-screen brightness.

Fresh targeted Shopee Indonesia searches yielded no qualified exact hardware offer; absence from search is not market absence. The physical mini-screen census remains importer-backed and manufacturer technology remains unresolved. Partial lead stays outside active counts. No local download or device operation.

### AXOM MAX — recovered English reset scope and display evidence boundary

Checked **2026-11-04**, [manufacturer English manual V1.7.4,2026-08-31,PDFpp5,50–51](https://shop.warwick.de/media/23/53/74/1790324346/4on4_MEL_AXOM_MAX_Manual_EN.pdf?ts=1790324346),58pages,linked by the identified importer. This endpoint now yields original text;earlier access failures remain dated observations. No local download orvisual panel inspection.

- **Factory Reset** offers separately selectable **Preset,Global Setting,Sample** categories,then aconfirmation prompt. The text doesnot enumerate every nestedsetting/sample type,loop inclusion orcross-version restoration. It is areset workflow,not proof that saving a preset backs up all three categories. No reset performed.
- The English panel description still says **footswitch/pedal mini screen** forfunction readout withoutLCD/OLED technology orphysical count. Importer-backed nine remains qualified;its separate pedal readout is not silently counted amongnine. The manufacturer shop remains inaccessible.
- The newly inspected [importer-hosted English flyer,PDFp3](https://shop.warwick.de/media/df/39/ee/1790778142/yf9_Melofty-Flyer_EN_ONLINE.pdf?ts=1790778142),Warwick copyright2026,listsnine configurable footswitches andthe7-inch main touchscreen. It doesnot independently settle mini-screen technology ormanufacturer screen census. Preserve its distributor provenance ratherthan treating its brand logo as manufacturer authorship.

Partial lead remains outsideactivecounts. Currentfirmware,fullcategory census,globalexternalEXPcoverage andqualifiedShopeehardware remainunresolved.

### AXOM MAX — preset color linkage and mini-screen boundary

Checked **2026-11-04**, [manufacturer German V1.7.4 manual,PDFp21](https://shop.warwick.de/media/33/3e/c1/1790324347/2itz_MEL_AXOM_MAX_Manual_DE.pdf?ts=1790324347). Original preset-save instructions; no device or visual panel test.

- Choosing a preset color links **the preset-name color in main-screen editing/stage views, its footswitch LED, and the large color block in bank selection**. It does not establish color rendering on the separate mini displays, their technology or independent brightness.
- **SET LIST/POSITION** selects the save destination. SAVE confirms; close/HOME cancels. This documents preset storage, not a whole-device backup or verified factory-bank write permissions.

Importer-backed nine mini displays remain qualified. Manufacturer physical census, LCD/OLED technology, full algorithm inventory, current firmware and exact Shopee Indonesia hardware remain unresolved; partial lead stays outside active counts. English-manual retrieval failed again today; earlier successful readings remain dated evidence. No local download or device operation.

### AXOM MAX — capture-EQ revision conflict

Checked **2026-11-04**. The [manufacturer German V1.7.4 manual](https://shop.warwick.de/media/33/3e/c1/1790324347/2itz_MEL_AXOM_MAX_Manual_DE.pdf?ts=1790324347), currently rendered as63 PDF pages, explicitly specifies a **10-band EQ** for manual refinement of an MFIM capture on PDFpage33 (zero-based32). Earlier pagination observations remain historical.

[Thomas Dill’s Bonedo review,2026-10-21](https://www.bonedo.de/artikel/test-melofty-axom-max-konkurrenz-fuer-line-6-neural-kemper-und-co/), lists tested firmware1.9.0 and describes a **12-band EQ** after capture. This independent report conflicts with the manufacturer manual; neither a firmware expansion nor a reviewer error is established. Preserve both counts with their provenance. This is capture refinement, not the separate output-global EQ or an additional simultaneous effects block. Exact current firmware behavior remains unresolved; no device test, download or inventory admission.

### AXOM MAX — Cloud object types and update source details

Checked **2026-11-04** in the manufacturer-authored [German V1.7.4 manual, PDF pages 50–53](https://shop.warwick.de/media/33/3e/c1/1790324347/2itz_MEL_AXOM_MAX_Manual_DE.pdf?ts=1790324347). Exact model/version identified; manufacturer site exposes no readable body. This is documentation review, with no account, network or device operation.

The network menu connects to a selected Wi-Fi network using its password. Saved networks offer **Disconnect** and **Delete**. Account access offers username/password registration or quick phone login; the shown phone flow specifies **+86**, without establishing support for Indonesian numbers or a universal regional restriction.

**Tone Cloud** separates **Preset files, Clipping Pedal Samples, Amp Head Samples, Full Amp Samples and Cabinet Samples**. Upload/Download tabs operate these distinct sound objects. This does not establish that a preset embeds every dependency, that Cloud storage is private, or that a complete system backup can be restored from it. Proprietary samples are not documented here as exportable NAM files.

The firmware page displays the installed version and provides **Check Update**. A manual describing this facility does not identify the latest available firmware, guarantee Indonesian service availability or establish current editor compatibility. Full category/algorithm census, mini-screen technology, global external-expression coverage and qualified Shopee hardware remain open. No file downloaded or update requested.

### AXOM MAX — recovered quick-guide processing-category census

Checked **2026-11-04** against the [recovered manufacturer quick-guide PDF,English sheet1](https://manuals.plus/m/63a022bc23df064392ad6523fb0e69573ed5ae7b06aa019d4e8601c2f649aa85_optim.pdf),three pages with the previously reconciled filing/document identity. This is the original PDF body,not the host-generated overview. English glyphs have the already documented encoding shift;adding31 to the affected character codes recovers these labels. No code from the document was executed andno visual panel census is claimed.

The extracted **EFFECT BLOCKS** portion names **19 processing entries**,excluding **NONE**: INST.SIM; SYNTH; OD; DYNAMIC; FILTER; AMP&CAB; AMP; DUAL CAB; MOD; FX; EQ; PITCH; DELAY; SPECIAL DELAY; REVERB; HQ REVERB; LEVEL; FX LOOP; CAB. This reconciles a named-entry list with the preserved19-module headline;it doesnot enumerate models within each category orcertify the current firmware menu. The separate **SAMPLE** label occurs elsewhere in the extraction;its relation to this list is unverified,andit isnot silently counted as a twentieth processing category. No **LOADER** label is established by this portion;that isnot a claim that current firmware lacks one.

Inst.Sim/Synth remain distinct from amp/cab/sample workflows. Physical mini-screen census/technology,exact algorithms andnote handling,qualified Shopee hardware andcurrent-firmware equivalence remain unresolved. German panel rendering andthe maker page were inaccessible again;the earlier successful textual evidence remains. Partial lead stays outside active counts;no local download ordevice operation.

### AXOM MAX — learned MIDI output controls and switch access

Checked **2026-11-04**, [manufacturer German V1.7.4 manual,PDFpp40–43](https://shop.warwick.de/media/33/3e/c1/1790324347/2itz_MEL_AXOM_MAX_Manual_DE.pdf?ts=1790324347). Original text;English endpoint inaccessible thispass.

- Separate learned targets **Unbal Out Level,Phones Out Level,Bal Out Level** accept documented values0–127. Each corresponding **Global EQ** target enables/disables that output EQ;it doesnot edit every EQ band. Addresses are user-learned,not fixed CC numbers;the default learn list is empty.
- **FS1–FS9** targets simulate the corresponding footswitch functions;separate RIG/SUBPATCH/STOMP/HYBRID andsix STOMP targets are documented. This extends remote control access without adding physical switches ormini displays. Numeric0–127 entries do not establish trigger thresholds,latching semantics orMIDI feedback.
- Output MIDI targets are distinct from EXP1/EXP2/EXP3 parameter targets. They do **not** prove direct analog EXP3 global assignment,full-mute endpoints,source/tail/recorded-loop coverage,power-cycle recall orscreen technology. Those questions remain open.

Partial lead remains outside active counts. No qualified exact Shopee hardware surfaced;no device operation,software download orMIDI command transmission occurred. Requested separate-screen research remains first priority.

### AXOM MAX — editor save prompts and Tail-Spill scope

Checked **2026-11-04**, [manufacturer German V1.7.4 manual,PDFp59](https://shop.warwick.de/media/33/3e/c1/1790324347/2itz_MEL_AXOM_MAX_Manual_DE.pdf?ts=1790324347). Original AXOM Controller chapter; current firmware equivalence untested.

- The desktop editor’s global-settings window lists **Tail-Spill** alongside screen brightness, USB audio and reset. The chapter does not define supported effects, duration, preset/scene transitions, bypass behavior or loop continuity. A named global control does not establish seamless switching or external EXP3 attenuation of tails.
- Changing the preset name, color or parameters triggers a save prompt when switching presets in the editor. This is a prompt, not documented automatic saving or hardware-only switching behavior.
- Its pedal-editing instructions name **EXP1/EXP2** with per-parameter minimum/maximum values; the hardware chapter separately identifies **EXP3(EXT)**. The abbreviated editor description does not prove external-pedal editing is unsupported. Global-volume assignment remains unresolved.

No qualified exact Shopee hardware offer surfaced in the targeted search. Partial lead remains outside active counts; no software download, device operation or workflow use.

### AXOM MAX — developer1.9 processing and tuner qualifications

Checked **2026-11-04** in the manufacturer/developer’s [Apple app history](https://apps.apple.com/us/app/melofty/id6762972347), **1.9.0,September29**; the same listing separately displays1.9.2 with a relative date. These are app-store release notes,not independently identified hardware firmware requirements.

- The developer names a **Simplified Noise Gate** addition andclaims improved noise-gate performance. This supplies a named processing lead,not its threshold/range,category placement,extra simultaneous slot ormeasured noise reduction.
- **Wah audio quality** and **tuner UI/bass tuning accuracy** are also listed as improved. No accuracy tolerance,tracking latency oruniversal bass/synth note handling follows from those statements.
- The already-retained **Synth/Inst Subpatch model switching** claim must be kept alongside the olderV1.7.4 scene architecture: shared module types/counts anddefault linked parameters. Neither source alone establishes which installed hardware revision permits which model substitutions.

The [Google Play developer listing](https://play.google.com/store/apps/details?id=com.melofty.axommax) displays **October23,2026** with generic fixes,without an exposed matching version here;do not equate that date with Apple1.9.2 orhardware firmware. Manufacturer site remains unreadable,English manual retrieval failed,andGerman panel rendering yielded no inspectable control census. No qualified exact Shopee Indonesia hardware found. Partial lead remains outside active counts;mini-screen technology,exact category census andexternal global-volume coverage stay unresolved. No download,installation ordevice operation.

### AXOM MAX — output-level linkage and EQ destinations

Checked **2026-11-04**, [manufacturer German V1.7.4 manual, PDFpage50 (zero-based49)](https://shop.warwick.de/media/33/3e/c1/1790324347/2itz_MEL_AXOM_MAX_Manual_DE.pdf?ts=1790324347). Original global-output chapter; current firmware and physical controls untested.

**UNBAL, BAL and PHONES** select separate output-level/EQ menus. Level can be adjusted with the touchscreen fader or volume rotary. Each fader group has a left/right link: lit links their levels; unlit permits independent adjustment. The text doesnot define how linking reconciles previously unequal values. Each output group has its own global-EQ enable control.

These are global output controls, distinct from per-preset LEVEL blocks, learned MIDI targets and external EXP3 assignment. Numeric level limits, full silence, EQ band count, power-cycle recall, USB-send inclusion and Bluetooth/looper/tail attenuation are not established by this chapter. This doesnot resolve mini-screen technology or the separate headphone-jack-size conflict. Partial lead remains outside active counts; no download, setting change or device operation.

### AXOM MAX — USB7/8 direction wording conflict

Checked **2026-11-04**, [manufacturer German V1.7.4 manual,PDFpp36–39](https://shop.warwick.de/media/33/3e/c1/1790324347/2itz_MEL_AXOM_MAX_Manual_DE.pdf?ts=1790324347). The input-channel section explicitly permits computer playback **USB7/8** as chain input;the reamp procedure repeats that selection. The output-channel paragraph instead says USB7/8 cannot be an input node while describing **dry A/B recording to DAW7/8**. Preserve this internal wording conflict rather than interpreting it as a universal USB7/8 input prohibition or silently changing “input” to “output.”

The documented playback andrecording directions remain distinct. AUDIO MIXER controls Bluetooth input level andindividual USB-channel levels;no numeric ranges,global EXP3 assignment orall-source mute coverage is established here. This adds a source qualification,not a device-tested routing guarantee. Existing sample-rate conflict andpartial status outside active counts remain. No local download,connection ordevice operation.

### AXOM MAX — English USB conflict and editor preset operations

Checked **2026-11-04**, alternate distributor-hosted [manufacturer English V1.7.4 manual,2026-08-31](https://cdn.rockboard.de/nos/data/erp/Artikell_PDF/Manual_PDF/Melofty/EN/MEL_AXOM_MAX_Manual_EN.pdf),58pages,printed34–36,54. The original title/version matches the previously identified manual;this newly readable endpoint supplements earlier retrieval failures.

- English input and reamp instructions explicitly permit **USB7/8** feeding a chain. Its dry-output paragraph nevertheless prohibits selecting that pair as an input node while assigning dry A/B to DAW7/8. The already-retained German conflict therefore also exists in English;neither a translation-only error noractual circuit behavior is established. Playback andrecording directions remain distinct.
- Desktop preset-list dragging **inserts** a preset at another position. Right-click offers rename,delete,copy/paste andimport/export. Import accepts a menu command orfile drag onto a preset,then confirmation;the text doesnot establish insertion-versus-overwrite semantics forimport orportable inclusion ofall sample dependencies. No import/reorder performed.

English panel screenshot again failed;no new visual census orLCD/OLED identification. ExactShopeeIndonesia search found no qualified local hardware item,not evidence ofmarket absence. Partial lead remains outside402 active models. Next:other accessible priority-model gaps;retain mini-screen technology,globalEXP3 coverage,currentfirmware andqualifiedoffers as unresolved. No local download ordevice operation.

### AXOM MAX — quick-routing defaults and inactive second chain

Checked **2026-11-04**, [manufacturer English V1.7.4 manual,2026-08-31,printedp13](https://cdn.rockboard.de/nos/data/erp/Artikell_PDF/Manual_PDF/Melofty/EN/MEL_AXOM_MAX_Manual_EN.pdf),original text. These are documented quick-setting endpoints,not a device-tested diagram.

| Quick setting | Documented routing boundary |
|---|---|
| Parallel | No inter-chain connection;A usesGuitar In→Multi Out,whileB input/output arebothNone. The name alone doesnot establish two audible parallel paths. |
| Split→Merge | ConnectsA input toB1 andB9 toA output;B endpoints remainNone. |
| A/B→Y | Both chains selectGuitar In;B9 feedsA output,withB outputNone. |
| Y→A/B | A input feedsB1;both outputstoMulti Out,B inputNone. |
| Series | A outputTo Chain B;B inputNone andoutputMulti Out. |

None is an endpoint setting,not proof the entire chain isalways disconnected:inter-chain links can still feed it. Repeated effects remain CPU-limited;these templates do not addslots orprove EXP3/master attenuation acrossboth paths. Current-firmware equivalence,physical mini-screen count/technology andqualified Shopee hardware remain unresolved. Partial lead remains outside active counts;no download ordevice operation.

### AXOM MAX — cross-chain move and module-editing boundaries

Checked **2026-11-05**, [manufacturer V1.7.4 manual,2026-08-31, printed12,16–18](https://cdn.rockboard.de/nos/data/erp/Artikell_PDF/Manual_PDF/Melofty/EN/MEL_AXOM_MAX_Manual_EN.pdf). Exact title/revision confirmed; original prose only. Panel screenshot retrieval still failed, so no visual screen census is claimed.

Each chain has nine slots. The manual expressly prevents moving a block from the other chain into a chain with **no empty slot**. This is a slot-occupancy restriction in addition to the separately documented CPU/resource restrictions; it does not establish that any eighteen effects will run together or that moving a block automatically swaps another one back.

Block order changes by dragging the icon between positions. Model replacement occurs from the effect-name area in the parameter editor, opening the category/model list; it is distinct from adding another block. Parameter pages use horizontal swipes or page-number selection. These touchscreen operations do not imply touch-sensitive mini displays, additional physical switches or scene-specific topology. Current firmware equivalence and exact algorithm counts remain unverified. No download or device operation.

### AXOM MAX — looper Undo playback-state conflict

Checked **2026-11-05** in the original manufacturer **V1.7.4,2026-08-31** manual editions, hosted by the importer/distribution network.

| Edition | Documented FS2 Undo/Redo condition |
|---|---|
| [English,printedp32](https://cdn.rockboard.de/nos/data/erp/Artikell_PDF/Manual_PDF/Melofty/EN/MEL_AXOM_MAX_Manual_EN.pdf) | At least two recorded layers **and looper playing**. |
| [German,printedp35](https://shop.warwick.de/media/33/3e/c1/1790324347/2itz_MEL_AXOM_MAX_Manual_DE.pdf?ts=1790324347) | Multiple recorded layers **and looper not playing**. |

Both specify a short FS2 press. This is a same-revision language conflict, not evidence that both playback states work or that a firmware change introduced either behavior. Preserve the earlier German finding with this qualification; actual installed behavior and later correction remain unverified. FS7 stop/hold-to-delete and contextual FS8/9 roles are separate. No device operation, download or MIDI transmission. Mini-display technology and qualified Indonesian hardware remain unresolved; this partial lead stays outside active inventory.

### AXOM MAX — retailer OLED lead and specification conflicts

Checked **2026-11-05**: [Esse Music Store, exact AXOM MAX product1024423/template162704](https://www.essemusic.it/en/shop/1024423-melofty-axom-max-162704) explicitly advertises nine customizable footswitches with OLED displays. **Retailer claim only**: no manufacturer display datasheet or revision is supplied. It supplements the importer-backed nine-display lead but does not resolve manufacturer LCD/OLED identification, physical screen census, dimensions, color or touch. The separate pedal readout remains separate.

The same seller body lists **3.1kg,5GHz Wi-Fi,48kHz/32-bit USB**, and **60-minute looper/120 minutes with layering**. These differ from retained manufacturer/importer mass, radio and USB qualifications; the layering wording does not prove120 minutes of independent recording capacity. Its270+/90+/600+ amp/cab/effect figures also differ from the retained400+/210+/130+ importer breakdown. No source revision, hardware variant or firmware change reconciles them. Preserve these as seller discrepancies rather than replacing canonical specifications or adding algorithm totals.

This is an Italian offer, not Shopee Indonesia or IDR evidence. No currency conversion or local stock inferred. Manufacturer site retrieval remained inaccessible; no qualified exact Shopee hardware found. Partial lead remains outside402 active records; primary display confirmation, current library and external global-expression coverage stay open. No downloads or device operation.

### AXOM MAX — assignment removal and parameter indicators

Checked **2026-11-05** in the [manufacturer English V1.7.4 manual,2026-08-31,printed23–24](https://cdn.rockboard.de/nos/data/erp/Artikell_PDF/Manual_PDF/Melofty/EN/MEL_AXOM_MAX_Manual_EN.pdf). Original text; no device operation.

- In STOMP editing, a controlled module’s delete icon removes that module from the switch assignment. DELETE in the expanded switch-selection interface instead clears **all controls assigned to that switch**. Neither instruction says to delete the underlying audio block orreset every switch.
- Expression editing selects **EXP1/EXP2/EXP3(EXT)**. Blue/yellow/purple parameter indicators identify the assigned controller, and a pedal icon marks an assigned module. These are editing-interface indicators,not evidence that the physical mini displays render those colors.
- Deselecting a parameter removes its expression assignment;the expanded DELETE control clears the controls together. The abbreviated text doesnot define that clear operation across other controllers,presets orscenes. Keep its scope unresolved rather than assuming a device-wide reset.

These assignment operations differ from clearing audio samples,factory reset orpedal calibration. They do not establish external global master-volume assignment,all-source mute,mini-display technology orcurrent firmware equivalence. Partial lead remains outside402;the already-recorded app1.9 notes addno new verified hardware revision here.


### AXOM MAX — MIDI transport and clock roles

Checked **2026-11-05**, [manufacturer English V1.7.4 manual,2026-08-31,printed36–37,42–45](https://cdn.rockboard.de/nos/data/erp/Artikell_PDF/Manual_PDF/Melofty/EN/MEL_AXOM_MAX_Manual_EN.pdf). Original prose,not a connection test.

MIDI IN settings separately enable external-clock following and USB MIDI reception; MIDI OUT settings enable clock transmission from the current BPM and USB MIDI sending. These are documented transport/tempo roles,not confirmation of MIDI Start/Stop,Song Position,looper phase alignment orBluetooth MIDI.

Receive andtransmit channels default to1. Receive OMNI accepts commands regardless ofsender channel. The OUT chapter describes OMNI as transmitting on all channels;that wording doesnot establish any ability to override the receiver’s channel configuration. Enabled MIDI THRU forwards incoming MIDI toOUT;forwarding is distinct from generating new note messages.

This extends the retained note-receive-only matrix,not evidence ofguitar-to-MIDI output orDeepSynth MIDI-note triggering. USB audio andmobile Bluetooth editing remain separate functions. Current-firmware equivalence,mini-screen hardware andqualified Indonesian stock remain unresolved. Partial lead remains outside402 active records;no download,MIDI transmission ordevice operation.

### AXOM MAX — editor platforms versus USB audio drivers

Checked **2026-11-05**, [manufacturer English V1.7.4 manual,2026-08-31,printed33,51,55](https://cdn.rockboard.de/nos/data/erp/Artikell_PDF/Manual_PDF/Melofty/EN/MEL_AXOM_MAX_Manual_EN.pdf). Exact title/revision and original chapter text identify this source; no generated mirror summary used.

| Software function | Documented requirement / qualification |
|---|---|
| AXOM Controller desktop editor | **Windows10+;macOS10.11+**. This supplies manufacturer corroboration of the earlier distributor flyer, not verification of current installers, CPU architecture or present-day compatibility. |
| USB audio | Windows requires the dedicated **ASIO driver for low-latency recording/monitoring**; Mac audio is described as driver-free plug-and-play. This is separate from editor installation. Driver version, supported Windows/macOS releases and measured latency remain unknown; the manual’s conflicting sample-rate claims remain. |
| Mobile editor | Manual lists **iOS11+;Android5.0+**. These are historical documented requirements; the newer developer listing’s iOS/iPadOS15.5+ remains the applicable listed minimum for that version. Android current minimum is not independently confirmed. |

No installer, driver, manual or firmware downloaded locally; no connection or device test. Mini-display technology/count confirmation, exact algorithms and qualified Shopee hardware remain unresolved. Partial lead stays outside active counts.

### AXOM MAX — screen lock and power-button timing scope

Checked **2026-11-05**, [manufacturer English User Manual V1.7.4,2026-08-31,printedpp5,57](https://cdn.rockboard.de/nos/data/erp/Artikell_PDF/Manual_PDF/Melofty/EN/MEL_AXOM_MAX_Manual_EN.pdf).

- **Short power-button press after startup locks/unlocks the screen.** This is not documented here as muting audio,bypassing effects,locking expression ordisabling all footswitches. The passage doesnot identify lock coverage forindividual mini displays orparameter changes fromexternal controllers.
- Panel chapter specifies **1.5s long press for power on/off**. The troubleshooting chapter instead instructs **more than2s to power on**. Preserve these as different documented instructions;they do not establish two hardware revisions,a firmware change ormeasured switch thresholds. Startup/shutdown duration andretention ofunsaved edits remain unverified.
- The power/lock button remains separate fromthe four named panel buttons andnine footswitches. It adds no extra display anddoesnot resolve LCD/OLED technology,individual-screen dimensions ormanufacturer physical screen count.

No button pressed,device operated orfile downloaded. Importer-backed nine switch mini displays andthe separate pedal readout retain their existing evidence grades. This partial lead stays outside402 active records;current Shopee Indonesia hardware,algorithm census andglobal external-expression coverage remain open.
