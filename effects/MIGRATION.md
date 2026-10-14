# Repository correction audit — 2026-10-14

**Working repository: `kokizzu/instrumentfx`.** The user clarified that `kokizzu/edrums` was a formatting reference, not the destination for instrument-effects research.

## Completed transfer

All **13 original effects files** are now present under `effects/` in instrumentfx. The **eight comparison pages, 51 partial model records, methodology and coverage backlog** were preserved byte-for-byte, verified using matching Git blob SHAs. The comparison index, resume instructions and progress JSON were deliberately updated to point to instrumentfx; their model inventory, next-batch cursor and pending research requirements were retained.

Each comparison category has its own commit. A root README and AGENTS.md additionally identify the correct repository and require separate commits/checkpoints for completed research parts.

Verified target snapshot before this audit: `c21d79d6bd5422ca511df45349ae97f5364197ea`.

Source snapshot: `kokizzu/edrums@bcc8d39507b445a3b708c4bb9706d1fb45db925d`.

## Matching source and destination blobs

| File under effects/ | Matching Git blob SHA |
|---|---|
| guitar-compact.md | 843998022f85297d63fc4285df0d583c6c159d1d |
| guitar-boss.md | fe18d0eb11fa64fbd3766ad60c0537925f919eea |
| guitar-nux.md | 01c12be78d929e4ced06d13bbf3a2d4fa59e7cc7 |
| guitar-floorboards.md | 4394e367d3744ee519829bac4bc98cb60e40e89f |
| bass.md | aeccc111f415aa882b97e8b5bb82099ef9f36d5d |
| vocal.md | ed1089a3cacd5f58d609cbe8f8b3493a05581223 |
| specialist.md | 836245f7e1bc66b872afb43f330b46337cdb776c |
| advanced-modelers.md | f4ecc7b15636ab477803031d34bf280afa9b98dc |
| METHODOLOGY.md | f8f425e4c7e133b58365a9938661d1e792392ec7 |
| COVERAGE.md | 885aa55914406833245ad516fb947774a8576817 |

## Old-repository cleanup: blocked, not completed

An attempted deletion of only the 13 misplaced `effects/` files from edrums was blocked by the tool's safety checks. No cleanup commit or branch update was made. **The old copies remain in edrums.** Do not claim they were removed, retry through a different mechanism to bypass the block, or make further effects-research commits there. Any future cleanup needs an appropriately authorised operation.

The edrums root README and `gotro-projects.md` were not changed during this correction. Their inspected blob SHAs were `3f3c626c47db0c08a90935ffa1847139bb9e3fca` and `1a8158501505114aea77b5b210f820aa7099f258` respectively.

## Research remains resumable, not finished

Continue from [RESUME.md](RESUME.md) and [research-state.json](research-state.json) in **instrumentfx**. The next model is still Valeton GP-100 on the compact page. Screen-size/color/touchscreen backfill and IDR price migration are still pending; this repository transfer did not complete them.
