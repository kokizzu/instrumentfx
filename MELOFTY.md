# MELOFTY — multi-effects discovery

[Comparison](MULTI-EFFECTS.md#separate-displays-for-effect-footswitches) · [Repository](README.md)

## AXOM MAX — partial discovery lead

Checked 2026-10-31. Manufacturer-authored **Axom Max User Manual V1.7.4, 2026-08-31**, 58 pages, recovered through the importer’s exact-model manual link: [original manual](https://shop.warwick.de/media/23/53/74/1790324346/4on4_MEL_AXOM_MAX_Manual_EN.pdf?ts=1790324346). Title/model/version identity checked; no host-generated FAQ used. Manufacturer website currently exposes no readable text.

| Field | Evidence / remaining gap |
|---|---|
| Hardware identity | Audio multi-effects/modeling processor, not merely a MIDI controller. Manual pp4–6 documents instrument input, effects processing and audio outputs. |
| Display layout | **7-inch color touchscreen plus footswitch/pedal mini screens** displaying assigned functions (manual p5). Exact mini-screen count, LCD/OLED technology, dimensions and one-per-switch placement remain unverified; panel screenshot retrieval failed. Nine numbered footswitches do not prove nine mini screens. |
| Expression | Built-in treadle; external EXP3 uses a stereo quarter-inch cable. Therefore outside the no-built-in-treadle shortlist. Global-volume scope/coverage and wiring remain unverified. |
| Software lead | Manufacturer’s [MELOFTY Android app](https://play.google.com/store/apps/details?id=com.melofty.axommax), published by Changsha Melofty Audio Technology, identifies Axom-series Bluetooth tone/hardware control; updated2026-09-27. App identity is not proof of every hardware feature. |
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
| USB / source conflict | p57: **USB2.0,8-in/8-out,48kHz/24bit**. Distributor192kHz claim remains separately qualified;do not treat32bit converter processing as USB resolution. |

Still a partial discovery lead outside active counts. New quick-guide link surfaced but web reader rejects its23.3MB size: [importer-linked guide](https://shop.warwick.de/media/96/42/2c/1791505539/7fj5_MEL_Axom_Max_Quick_Guide_EN.pdf?ts=1791505539).

### AXOM MAX — mini-screen labels and master-pedal scope

Checked2026-10-31,[own V1.7.4 manual pp22–24](https://shop.warwick.de/media/23/53/74/1790324346/4on4_MEL_AXOM_MAX_Manual_EN.pdf?ts=1790324346);manufacturer text only.

| Field | Evidence / qualification |
|---|---|
| Display / STOMP labels | Single-module control shows its module name;multi-module control shows **MULTIPLE**. Green/orange status refers to the footswitch icon/LED,not proof of color mini-screen pixels. Latching and momentary control are selectable. Physical screen count and LCD/OLED remain unresolved. |
| Expression / built-in MASTER | **MASTER+EXP1** selects master-volume/parameter roles via toe switch;master position can be **Pre/Post**,with minimum/maximum **0–100**. Alternative **EXP1+EXP2** provides two parameter roles. This documents the built-in treadle,not externalEXP3 master assignment or every-preset coverage. Headphone/tail/loop attenuation remains unknown. |
| Expression / naming conflict | p23 introduces externalEXP3 but then says externalEXP2;rear-panelp6 and controller selectorp24 identify **EXP3(EXT)**. Preserve this internal typo/conflict;do not invent a second external socket. Parameter assignments offer individual minimum/maximum values. |

Built-in treadle keeps this model outside the no-built-in-expression shortlist. No pedal operation or display visual inspection.
