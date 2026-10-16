# InstrumentFX agent instructions

## Repository and execution boundary

Work only in **kokizzu/instrumentfx**, default branch **main**. Verify the owner/repository before every write. Do not write instrument-effects research to kokizzu/edrums. Never reset history, force-push, or overwrite unrelated concurrent changes.

**Do not create, add, enable, dispatch, rerun, or otherwise use GitHub Actions workflows. Do not create .github/workflows/ files.** This is an explicit repeated user instruction, not a suggestion. Do not introduce CI, scheduled jobs, workflow badges, or Actions-based conversion/scraping. Check and transform files locally or with ordinary repository file/Git operations. A difficult merge or unavailable local network is not permission to use Actions.

## Required document layout

The user wants root-level **[BRAND].md**, **[CATEGORY].md**, and **ALL-[INSTRUMENT].md** documents, not date/progress/batch Markdown files and not new documents under effects/. Use brand files as canonical technical records and category/instrument files as comparison views with links to the brand sections. README.md and this AGENTS.md are navigation/instructions, not progress reports. Save the machine-readable inventory, exact resume cursor, sources and unresolved tasks in **research-state.json**, not new RESUME/history/batch Markdown documents.

Legacy effects/ files still require a lossless consolidation. Read complete source content before merging. Preserve every source URL, field qualification, historical price date, model/revision distinction, correction and unresolved contradiction. Do not delete an old source until the corresponding content has been verified in its root-level destination. Do not merely rename dated findings or change their extensions and call that a merge. Historical commits already preserve history; do not create more per-progress Markdown snapshots.

During transition, the latest root files and root research-state.json take precedence; consult legacy files that have not yet been consolidated. Do not claim the whole migration is complete while legacy files remain.

## Scope

The root `ALL-GUITAR.md`, `ALL-BASS.md` and `ALL-VOCAL.md` must be actual comparisons, not model-name navigation indexes. Every eligible recorded model in an instrument membership list needs a row in each hardware, processing/memory, I/O-power-software and separate IDR-price table. Include effects-only multi-effects such as Line 6 HX Effects; amp modeling is not required. The bass comparison includes documented bass-capable shared processors, not only bass-branded units; uncertain suitability stays explicitly unclassified. Keep the evidence basis in root research-state.json and never infer bass support from a BASS EQ knob, a sibling model or a capture connector.

Dedicated single-function records belong in root `SINGLE-GUITAR.md`, `SINGLE-BASS.md` and `SINGLE-VOCAL.md`, outside all active multi-effects rows/counts. Shared specialist records can cross-reference one canonical archive rather than duplicate their technical evidence. Preserve full original facts, dates, links and contradictions during moves, and leave redirects for existing legacy anchors. FV01 remains explicitly excluded irrespective of its supporting effects. Do not expand the active research into ordinary single-function pedal catalogues.

For guitars, include **multi-effects processors only**. Effects-only processors can qualify without amp modeling, an expression pedal, or a minimum number of switches. A dedicated pitch shifter, acoustic simulator, vocoder, drive, delay, reverb or synth pedal does not qualify merely because it offers modes or presets. Controllers, tuners, pickups, cases, power supplies and downloadable preset packs are not multi-effects hardware.

**Flamma FV01 is explicitly excluded.** BOSS SY-1, SY-200, AC-3, VO-1 and XS-100 are excluded archival specialist records, not active guitar multi-effects. Preserve genuine bass and vocal multi-effects as separate categories. A guitar-thru, chord-detection input or guitar-reverb side path alone does not qualify a vocal unit as guitar multi-effects. GM-800/GR-55 inclusion depends on their documented independent multi-effects architecture and retains their pickup limitations.

Include all eligible units the owner has ever owned, including former/donated units and handheld processors. Ownership is an attribute, not another technical record. Shopping plans and the rejected MG-400 order do not establish ownership. Do not publish private mailbox links, receipt/order identifiers, payment data, or message contents.

## Research priority and evidence

Start with remaining **Shopee Indonesia** hardware leads, verify each exact model's specifications using **official manufacturer product pages, manuals, firmware notes and software documentation**. Manufacturer-authored copies on mirrors can supplement inaccessible official files only after identity/revision checks; generated mirror FAQs are not evidence. Seller pages establish offers, not authoritative hardware specifications. If the saved queue is exhausted, search Shopee again by brand and series rather than claiming market coverage is complete.

Each model needs built-in/external/toe expression; separate rotary/footswitch/button counts; separate used/new **IDR** evidence; simultaneous blocks and per-category choices; complete ports; factory-filled/user/total memories; synth/acoustic distinctions; unit dimensions/weight; power/current/polarity/battery/USB operation; IR/native-versus-converted NAM/proprietary captures; editor platforms; and published display diagonal, monochrome/color and touchscreen. Preserve looper, drums, scenes, routing, headphones, phantom and firmware restrictions.

Unknown is not No. Do not estimate screen diagonals from photos, borrow sibling specifications, silently mix variants, or infer USB power/audio/MIDI from connector presence. Keep exact revisions and source conflicts visible. Do not call a first pass fully verified when fields remain unknown.

Prices must buy hardware, not an accessory or unresolved lowest-priced variation. Keep seller/item IDs, condition, variant, bundle, stock state, voucher, region, check date and direct/indexed access limitations. A cached or sold-out ask is not live stock or a completed sale. Do not invent used-price discounts or exchange rates.

## Immediate commits and resumability

Research one model, update its root brand document, commit the useful findings **before starting the next model**, and update affected category/instrument views and research-state.json. Verify saved contents and inventory counts. If interrupted, inspect commits and newer brand content before trusting an older cursor. Count each distinct active model once, exclude archives, and preserve unresolved fields. Never create a GitHub workflow to automate any of this.
