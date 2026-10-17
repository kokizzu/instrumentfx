# Darkglass multi-effects

[All bass](ALL-BASS.md) · [Repository](README.md)

## Anagram

Bass multi-effects platform; checked2026-10-18,partial. Ownership unverified. Guitar cabinet choices do not independently establish guitar/vocal comparison membership. Expression accessory is a separate product,not another processor.

| Field | Finding / qualification | Evidence |
|---|---|---|
| Expression / toe | No treadle in documented layout. External expression shares RETURN;requires signal onTRS ring(**RTS wiring**),sacrificing return use. Toe support unknown. | [Product][ANA-P] |
| Knobs / footswitches / buttons |6 endless push rotaries,3 footswitches;separate button census pending visual audit. Encoder pushes are not extra standalone buttons. | [Product][ANA-P] |
| Display |**7-inch touchscreen**;published color-mode detail unverified. | [Product][ANA-P] |
| Processing / category choices |Hexacore,32-bit48kHz;advertised12 serial/24 parallel blocks,50+effects. Exact category census andDSP/model-complexity restrictions unresolved. | [Product][ANA-P] |
| Factory / user / total memory |KosmOS1.17 PDF:42banks×3=126presets;factory area read-only,copyable toUser. Current1.18 product adds up to126 user areas;capacity perarea/full factory-user total not reconciled. Three scenes/preset in1.17. | [Manual][ANA-M];[1.18 product][ANA-P] |
| Dimensions / weight |W210×length105×H62mm;815g,mass basis unstated. | [Manual specifications][ANA-M] |
| I/O |6.35mm TS instrument;TRS SEND(stereo/mono insert);TRS RETURN(stereo/AUX/EXP);3.5mmTRS phones;2XLR+2unbalanced6.35TS outs;3.5TRS TypeA MIDIin/out;USB-C;DC. | [Manual][ANA-M] |
| Power / USB / battery |Product **9–12V center-negative≥1.7A**,9V adapter included;manual rear layout **9V2A**. Preserve rating/scope difference. USB-C PD **≥18W**;battery operation unverified. | [Product][ANA-P];[manual][ANA-M] |
| IR / NAM / captures |User cabinetIR,NAM,AIDA-X viaSuite desktop assets. NeuralAmp,NeuralPedal,NeuralLoader separate model-loading blocks. Exact native/converted architecture,size/format limits andinstance ceilings pending version-specific audit. | [Manual][ANA-M] |
| Synth / acoustic |KosmOS1.18 adds **Axioma monophonic synth**;license/bundle eligibility unverified. Acoustic simulation unverified. | [Product changelog][ANA-P] |
| Editor / USB |Darkglass Suite forupdates/library/assets;platform/minimumOS previously unknown; see versioned Suite findings below. ManualUSB AudioClass2,48kHzfixed,**3in/9out** asprinted;host/device channel direction mapping pending. USBMIDI. Bluetooth role/version pending. | [Product][ANA-P];[manual][ANA-M] |
| Looper / routing / live |Looper,tuner,parallel split/merge andscenes documented;recording duration,drums,trails restrictions unverified. | [Product][ANA-P];[manual][ANA-M] |

### Source versions and limits

[Official PDF][ANA-M] retrieved as97pages,title2026-10-12,cover **KosmOS1.17**. Read relevant introduction,layout,core concepts,loader andtechnical sections as text;not a complete97-page audit orvisual confirmation. [Current product][ANA-P] lists **KosmOS1.18.0** andAxioma;regional cached pages still1.17. Keep firmware distinctions rather than silently claiming every offer includes newest software/plugins. No firmware,software ormanual files downloaded orrun.

### Separate IDR hardware evidence

| Condition / access | Amount / qualification | Source |
|---|---|---|
| Used |Unknown;no condition-qualified ask. | — |
| New |Unknown;no condition-qualified ask. | — |
| Condition-unverified sold-out/preorder cached ask |**Rp20,350,000**,FireWorX Music Gear,Surabaya,shop72439811/item41315767273. Last-month search cache,**Habis** alongside30-day preorder andstale9–12Oct arrival. Clean exact URL failed toopen. Condition,working state,selected variant,firmware,plugin licenses,adapter/case,bundle,warranty,shipping/tax/voucher andcheckout total unknown. Rp10,000 latecompensation is not discount. | [Exact clean item](https://shopee.co.id/product/72439811/41315767273) |

Not live stock orcompleted sale. Original search URL carried advertising parameters;clean seller/item identity retained. Remaining:full model/category audit,NAM native/conversion constraints,editor platforms,hardware panel,firmware memory reconciliation andqualified used/new prices.

[ANA-P]: https://www.darkglass.com/products/anagram
[ANA-M]: https://api.darkglass.com/static/Anagram-Manual.pdf

### Anagram — versioned block-list census and NAM claims

Checked2026-10-18: [official online manual/block list](https://www.darkglass.com/pages/anagram-manual) now labels itself **v1.18.1**,while earlier indexed copy1.18.0 andPDF1.17 remain distinct. No firmware downloaded;list counts are a text audit,not installed-device verification.

| Field | Current evidence / qualification |
|---|---|
| Processing / category choices | List has **4 preamps,11 amps,22 bass cabinets,6 guitar cabinets,18 artist cabinets,12 drive/distortion,16 EQ/filter/dynamics,11 modulation/pitch,8 delay/reverb,13 utilities**. Sum **121 listed entries**,includingIR variants,loaders/system blocks andpotential licensed content. Not121 unique conventional algorithms orsimultaneous blocks;installed license/library census unresolved. |
| Processing / cabinet-list conflict | Bass-cabinet prose says6 microphones×6positions,butnames **7 microphones**(3condenser+4dynamic). Guitar section names6microphones×3positions. Do not silently collapse names orcalculate a definitive total IR library from the conflicting bass statement. |
| NAM / published concurrent claims | [Current exact product](https://www.darkglass.com/products/anagram) advertises **5 NAM A2 Full or9 A2 Lite**,running side byside,andstandard-size NAM/AIDA-X support. These are manufacturer performance claims,not all-model/mixed-chain benchmarks. Native execution versusconversion,architecture restrictions andactual DSP budget still require precise versioned documentation. |
| Looper / recording independence | Same exact product says loops continue across preset changes. This does not prove spillover forother effects orloop persistence afterpower-off;duration stillunverified. |
| Factory / user memory limits |1.18 changelog's126 user areas isnot yetreconciled with1.17's126preset capacity. Do not multiply them toinvent15,876presets. |

Full named block list remains linked rather than treated as guaranteed free factory content. Further work:memory areas,NAM architecture/limits,Suite platforms,plugin licensing,full manual/panel andqualified offers.

### Anagram — Suite compatibility and firmware limits

Checked 2026-10-18 against the [official Suite page](https://www.darkglass.com/products/darkglass-suite); no installers or firmware downloaded. Earlier versioned evidence above remains historical.

| Field | Evidence / qualification |
|---|---|
| Editor / desktop platforms | Suite **6.11.1** explicitly supports Anagram **1.18.0**. Windows heading says **Windows 10 & 11 (24H2 or later)**; the scope of that parenthesis is ambiguous. macOS **11 Big Sur+**, universal x64/arm64. Legacy Suite **1.3.6** lists other devices only, not Anagram. |
| Editor / mobile and driver separation | Suite mobile lists **iOS 15.6+ / Android 11+**, but product-dependent features mean Anagram mobile editing/asset parity remains unverified. Separate Windows USB audio driver **5.72.0**; driver availability is not editor compatibility. |
| NAM / firmware-dependent concurrency | KosmOS **1.18.1** removes the three-neural-loader-block limit and adds Blend/EQ Position to Tone3000 NAM loader. Removal does not imply unlimited DSP or settle native-versus-converted model architecture. |
| Factory / user memory area conflict | Suite changelog for **1.18.0 says up to127 user areas**; exact product page above says126. Preserve the unresolved conflict, not an assumed factory-area offset. Total preset capacity remains unverified. |

Next: version-specific NAM architecture/file constraints, licensing, full preset-area semantics, hardware panel and qualified used/new offers.
