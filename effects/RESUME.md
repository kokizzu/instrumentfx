# Resume this effects-comparison project

**Checkpoint: 2026-10-14. Ready to resume; research is not complete.**

**Canonical repository: `kokizzu/instrumentfx`, branch `main`, directory `effects/`.** The separate `kokizzu/edrums` repository is only a formatting reference. The user has removed the misplaced copies there; cleanup and preservation are verified in [MIGRATION.md](MIGRATION.md). Do not write instrument-effects research to edrums.

Read this file, [research-state.json](research-state.json), [METHODOLOGY.md](METHODOLOGY.md), [COVERAGE.md](COVERAGE.md), and the current comparison page before editing. Use repository contents, not chat memory. Verify owner/repository and current file SHAs before every write. Never reset, force-push, or overwrite unrelated work.

## Required scope and fields

Research guitar, bass, vocal and specialist/dedicated effects, not only multi-effects. Organise by instrument/function, physical size and built-in versus external expression. The current catalogue is not exhaustive.

Every model needs:

1. Built-in expression, external expression support and toe switch.
2. Separate rotary-control, footswitch and button counts; explain concentric controls and exclude duplicate push-encoder counts.
3. **Separate used/new IDR prices**, with seller, market, condition, availability, date and source. Preserve foreign evidence separately; do not invent a conversion rate or a used percentage.
4. Simultaneous effect blocks, DSP restrictions, available categories and choices per category.
5. Complete I/O, including headphones, microphone/phantom power, loops and control connections where applicable.
6. Factory, editable/user and total preset storage without double counting.
7. Synth and electric-to-acoustic simulation, distinguished from acoustic amp models and body IRs.
8. Width × depth × height and weight, including pedal-travel/plug-clearance qualifications.
9. Battery, voltage, polarity, device draw versus adapter rating, and USB operation versus charging/data.
10. IR, native NAM architectures, converted NAM workflows and proprietary captures as separate capabilities.
11. Configuration/editor platforms separately from drivers, updaters, librarians and USB-audio compatibility.
12. **Manufacturer-specified display diagonal**, with multiple screens recorded individually; never estimate from a photograph.
13. **Monochrome/color**, independently of LCD/OLED/TFT technology.
14. **Touchscreen yes/no/unverified**, supported independently of screen color or marketing language.

Retain additional useful fields already present: looper, rhythms, USB audio/reamp, MIDI, scenes, parallel routing, bypass/trails, DI/phantom power, special pickups/cables, firmware and conflicts.

**Commit each completed model/finding separately**, then integrate its comparison changes and update the checkpoint. Save partial evidence rather than withholding it until an entire brand is complete. The dated findings notes themselves should identify their scope, unknowns and next step.

## Saved inventory

**51 distinct partial models across eight pages; zero fully verified records.** Cross-references and new findings notes do not add models. Firmware updates are not automatically new hardware.

| Page | Models | Display/IDR review status |
|---|---:|---|
| [Compact guitar](guitar-compact.md) | 8 | First pass saved; IDR columns migrated; unresolved fields retained |
| [BOSS guitar](guitar-boss.md) | 7 | **Next: start at GT-1000CORE** |
| [NUX](guitar-nux.md) | 6 | Pending |
| [Larger Valeton/Sonicake](guitar-floorboards.md) | 3 | Pending |
| [Bass](bass.md) | 7 | Pending |
| [Vocal](vocal.md) | 8 | Pending |
| [Specialist](specialist.md) | 6 | Pending |
| [Advanced modelers](advanced-modelers.md) | 6 | Pending |

Transfer baseline in instrumentfx: `c82aa042ecf97647c9f877e0ceabf314880012d7`. Latest integrated compact research: **`c77420e66f01a1bad5d5e032d3f9e5ae70e515f5`**. These are recovery references, not reset instructions. The eight separate model findings commits are recorded in `completed_review_batches` in the JSON ledger.

## What the completed compact pass actually established

All eight existing compact records now have display rows and primary **IDR** comparison columns. Five diagonals are manufacturer-supported: GP-150/GP-180 at 2.4 inches; GP-50/Smart Box/Pocket Master at 1.77 inches. Color display evidence is recorded for all eight. **GP-100, GP-5 and Matribox diagonals remain unverified, and explicit touch specifications remain unverified for all eight.** Knob navigation or drag-and-drop wording is not treated as touch hardware proof.

Seven models have identified local retail amounts, but several are sold out, ambiguous in stock status, or lack detailed condition confirmation. GP-100 has a separately labelled sold-out used asking price. Matribox's indexed **CN-language/preorder** offer is kept outside the English/global price range. **None of this establishes complete active used-to-new market ranges.** All old USD evidence is preserved in a separate provenance section; no FX rate was chosen.

Specific technical corrections are integrated: GP-100 control count and pre/post looper modes; GP-50 separate button count; GP-5 documented USB/output/OS limitations with the FAQ date; Smart Box's explicit iOS/Android apps; Pocket Master's two USB-C roles. Existing unrelated specifications, sources and uncertainties are retained, not blanket re-certified.

The eight notes are linked from [the compact page](guitar-compact.md) and enumerated with commit SHAs in [the ledger](research-state.json).

## Exact next task: BOSS GT-1000CORE

Start with **`effects/guitar-boss.md`**, beginning with **BOSS GT-1000CORE**. Then review GX-10, GT-1, GX-1, ME-90, GX-100 and GT-1000.

For each model:

- Read the existing full row/context and its source links. Verify exact model and firmware; do not transfer sibling-model features.
- Establish screen presence/count, diagonal, monochrome/color and explicit touch support from primary sources. Distinguish segmented displays, status LEDs and auxiliary screens. Preserve `?` where evidence is insufficient.
- Find dated Indonesian used/new offers. Mark sold-out asks as historical, index-only evidence as indexed, and conflicting availability as unconfirmed. Do not blend regional variants or treat a listing as a completed sale.
- Where only foreign offers exist, either leave IDR unknown or use a **verified dated rate** with an explicit **FX estimate** label and original quote. Never relabel USD numbers as rupiah.
- Commit each model's useful findings separately, preserving provenance. Integrate changes into the comparison, verify saved content, then update this checkpoint and the JSON cursor. Advancing a reviewed model does not certify all its fields complete; list unresolved fields.

After the BOSS page, continue in this order: **NUX → larger Valeton/Sonicake → bass → vocal → specialist → advanced modelers**. Return to unresolved compact fields when better evidence is found. Then expand the backlog, prioritising M-VAVE/CUVAVE, Mooer, Hotone and TC-Helicon alongside remaining mainstream families. This is a work queue, not a recommendation ranking.

## Guardrails and unresolved conflicts

Compact means width ≤200 mm **and** depth ≤140 mm, without rotation. Medium means ≤300×200 mm but not compact; large exceeds medium; unknown means unverified width/depth. Cable clearance and pedal travel are additional.

Keep original observation dates when only some fields are rechecked. A product landing page does not complete every required field. The other seven pages still have legacy USD comparison columns; the overall IDR/display migration is **not complete**.

Preserve conflicts: TONEX ONE memory count, MG-50Li factory/user/model counts, Matribox II Pro MIDI output, GP-100 rhythm/effect totals, firmware-specific NAM architecture limits, regional-language variants and conflicting seller stock markers. See the ledger and findings for details.

## Continue without this chat

> Continue the guitar, bass and vocal effects comparison in kokizzu/instrumentfx. Read effects/RESUME.md and effects/research-state.json. Resume at BOSS GT-1000CORE, verify display specifications and IDR prices, preserve existing research, commit each model's findings separately, and update the checkpoint. Keep unresolved compact fields recorded. Do not write effects research to edrums.

No background worker or recurring research automation is configured.
