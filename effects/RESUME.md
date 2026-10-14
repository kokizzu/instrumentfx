# Resume InstrumentFX research

**Checkpoint: 2026-10-14. Ready to resume; research is not complete.**

**Canonical repository: `kokizzu/instrumentfx`, branch `main`, directory `effects/`.** Never write instrument-effects research to `kokizzu/edrums`. That repository was only a formatting reference; the user removed the misplaced copies, and transfer/cleanup were verified in [MIGRATION.md](MIGRATION.md). No cleanup is pending.

Read this file, [research-state.json](research-state.json), [METHODOLOGY.md](METHODOLOGY.md), [COVERAGE.md](COVERAGE.md), and the relevant current comparison page. Use current repository content and blob SHAs, not chat memory. Preserve unrelated work. Never reset or force-push to an old checkpoint.

## Latest priority: Shopee Indonesia multi-effects

The user asked to continue, **especially all multi-effects listed on Shopee Indonesia**. This now takes priority over the earlier BOSS-first display/IDR queue, without discarding it. Retain guitar, bass and vocal scope; specialist effects remain in the broader project.

Start with [shopee-indonesia.md](shopee-indonesia.md). It separates newly researched models, listing evidence for existing records, still-unresearched hardware, and excluded preset downloads/accessories. It is **not an exhaustive seller inventory or current-stock guarantee**.

## Required record fields

1. Built-in expression, external support and toe switch.
2. Separate rotary/footswitch/button counts; explain concentric controls; do not double-count push-encoders.
3. **Used and new/retail IDR prices separately**, exact seller/item/date/condition/stock/variant/bundle/voucher evidence. Preserve foreign quotes; no guessed exchange rate or used-price percentage.
4. Maximum simultaneous blocks, DSP limits, available categories and choices per category.
5. Complete I/O, headphones, microphones/phantom, loops and controller connections.
6. Total/editable/factory-filled/dedicated user or factory storage without double counting.
7. Synth and electric-to-acoustic simulation, distinguished from acoustic amp and body-IR models.
8. Width × depth × height and weight; separate packaging, pedal-travel and plug clearance.
9. Battery, voltage, polarity, actual draw versus adapter rating; USB operation versus charging/data.
10. IR, native NAM architectures, NAM conversion and proprietary captures as separate capabilities.
11. Editor platforms separately from updater, librarian, audio driver and mobile USB audio.
12. **Manufacturer-published screen diagonal**, including separate screens; never estimate from photos.
13. **Monochrome/color**, independent of LCD/OLED/TFT technology and colored indicator LEDs.
14. **Touch yes/no/unverified**, with independent support; color or knob navigation alone is insufficient.

Retain looper, rhythms, USB audio/reamp, MIDI, scenes, parallel routing, bypass/trails, DI/phantom power, special pickups/cables, firmware and source conflicts. Unknown is `?`/`null`, not false/zero.

**Commit each model's useful findings separately**, then integrate its comparison changes and update the ledger/checkpoint. Partial evidence is worth saving; a page link alone does not make a record complete.

## Saved inventory and progress

**67 distinct partial models across nine comparison pages; zero fully verified.** The original 51 are preserved. Sixteen new Shopee-first models were individually committed and integrated in **`77a5027eae1bbb4c9079d64d46f7cd16a36c0b03`**. Shopee discovery index commit: **`78deb9e43962dbaa40039b688a986a282c52d6cf`**. Individual findings commits are in `completed_review_batches` in the ledger.

| Comparison | Records | Status |
|---|---:|---|
| [Compact guitar](guitar-compact.md) | 8 | Earlier display/IDR first pass saved; unknowns retained |
| [BOSS guitar](guitar-boss.md) | 7 | Original display/IDR queue deferred, not completed |
| [NUX](guitar-nux.md) | 6 | Original display/IDR review pending |
| [Larger Valeton/Sonicake](guitar-floorboards.md) | 3 | Original display/IDR review pending |
| [Bass](bass.md) | 7 | Original display/IDR review pending |
| [Vocal](vocal.md) | 8 | Original display/IDR review pending |
| [Specialist](specialist.md) | 6 | Original display/IDR review pending |
| [Advanced](advanced-modelers.md) | 6 | Original display/IDR review pending |
| [Shopee-first expansion](shopee-multifx.md) | **16** | IDR, display and technical first-pass records saved |

New models: **TANK-G, TANK-B, TANK MINI, MK-20, MK-300; Ampero Mini; GE100 original, GE150 original, GE150 Pro Li, GE200 original; G1 FOUR, G1X FOUR, G2 FOUR, G2X FOUR; FX100, FX200.** Notes and discovery rows are not additional models.

Recovery references: original instrumentfx transfer baseline `c82aa042ecf97647c9f877e0ceabf314880012d7`; earlier compact integration `c77420e66f01a1bad5d5e032d3f9e5ae70e515f5`. **Do not reset to these references.**

## Exact next task: M-VAVE TANK-PRO

1. Read its exact Shopee item in section C of [the index](shopee-indonesia.md). The indexed Rp1.900.000 ask is not verified stock, condition or delivered cost.
2. Obtain manufacturer-authored TANK-PRO documentation, matching revision/firmware. A shell-only product page or unverified reformatted/AI-looking PDF is not sufficient technical evidence. Do not copy TANK-G dimensions, controls or loading formats.
3. Fill all required fields with evidence or explicit unknowns, especially expression, screen/touch, exact processing architecture, app platforms, battery/USB behavior and NAM native-versus-converted support.
4. Commit a scoped findings note; integrate a new model record only once useful technical evidence is saved. Update counts, comparison/navigation and the cursor; verify read-back before claiming it is saved.

Then prioritize **ANN Blackbox → Boin Audio BG300 → Scorpion KMF-10 → JOYO GemBox I/II/III**. Include **TC-Helicon VoiceLive Play/Play Acoustic, HeadRush Core and Flamma FV01** so vocals are not indefinitely displaced by guitar models. Continue Donner Arena 2000, remaining MOOER GE variants, Hotone, Zoom and other discovered families. Queue order is not a product ranking.

The earlier task remains at **BOSS GT-1000CORE**, then GX-10, GT-1, GX-1, ME-90, GX-100, GT-1000; after that **NUX → larger Valeton/Sonicake → bass → vocal → specialist → advanced**. It is preserved in `deferred_cursor`. New Shopee evidence for existing NUX/GP-50/GX-100/HX Stomp/Matribox records is saved in the marketplace index, not yet fully integrated into their older pages.

## Important unresolved findings

**Latest batch:** MK-20's spec-table external EXP socket conflicts with its complete rear panel. FX200 advertises160 types but numbered categories total161; its W/D labels also need resolution. MK-300 and FX100 prices disagree between snippets and bodies. Zoom G2-family storefront/voucher amounts differ. Most used prices, live stock, several screen diagonals/touch specs and current firmware category totals remain unknown.

**NAM correction:** GE150 Pro Li's current Pro V2.1.4 notes document **converted NAM A2** via the converter, not unrestricted native NAM; this does not establish original GE150 support. Pro versus Pro Li power ratings also differ. Preserve architecture/region/revision restrictions on M-VAVE and other products.

**Earlier compact pass:** all eight have display rows and IDR columns; GP-150/180 diagonals2.4 inches, GP-50/Smart Box/Pocket Master1.77 inches. GP-100, GP-5 and Matribox diagonals remain unknown, as do explicit touch specs. GP-100 used and GP-50 retail observations were sold out; other stock markers conflict. Matribox CN-language preorder is separate from English/global offers. Existing GP-100/GP-50 controls, GP-100 pre/post looper corrections, GP-5 limitations, Smart Box mobile apps and Pocket Master USB roles remain preserved.

**Other original conflicts:** TONEX ONE memory counts, MG-50Li factory/user/model totals, Matribox II Pro MIDI-out and GP-100 rhythm/effect totals. Do not hide conflicts to fill a table.

## Marketplace and measurement guardrails

A listing price may refer to a downloadable preset, carrying case, power supply, controller or mixed variant. Verify the actual hardware item before accepting its price. A sold-out ask is not a sold-price statistic; an Official seller name is not authentication. Preserve historical/stock/voucher/bundle/selected-variant context. Do not combine unlike observations into one apparent active range. A missing offer does not mean a product is unavailable in Indonesia.

Compact is width≤200 AND depth≤140 mm, without rotation; medium≤300×200 but not compact; large otherwise; unknown if either dimension is unverified. Never use shipping dimensions. Keep original observation dates when only selected fields are checked.

Seven original pages still have USD comparison columns. The overall IDR/display migration and all-Shopee research are **not complete**. No unattended worker or scheduled research is configured.

## Copyable continuation request

> Continue the effects comparison in kokizzu/instrumentfx, prioritizing multi-effects listed on Shopee Indonesia. Read effects/RESUME.md, effects/research-state.json and effects/shopee-indonesia.md. Resume at M-VAVE TANK-PRO, preserve the 67 partial records, verify primary specifications and used/new IDR listing evidence, commit each model finding separately, integrate it and update the checkpoint. Keep the deferred BOSS review and unresolved fields. Do not write effects work to edrums.
