# Repository correction audit — 2026-10-14

**Working repository: `kokizzu/instrumentfx`.** `kokizzu/edrums` was a formatting reference, not the effects-research destination.

## Completed transfer

All **13 original effects files** were copied into `instrumentfx/effects/`. The **eight comparison pages containing 51 partial model records, methodology and coverage backlog** matched the source byte-for-byte at transfer. The comparison index, resume instructions and progress JSON were deliberately updated to identify instrumentfx while retaining the model inventory, pending requirements and cursor.

Each comparison category has its own transfer commit. Root README and AGENTS.md identify the correct repository and require incremental research commits/checkpoints.

Verified transfer snapshot: `c21d79d6bd5422ca511df45349ae97f5364197ea`.

Original source snapshot: `kokizzu/edrums@bcc8d39507b445a3b708c4bb9706d1fb45db925d`.

All 13 original files were rechecked as present in instrumentfx at `b6ca1b7696b9d1021d0080c250b4a70f8a5c14fd`, before the resumed research edits. Later legitimate research updates will change individual hashes; the table below records the **transfer baseline**, not a requirement to freeze the research files.

## Matching source and destination blobs at transfer

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

## Old-repository cleanup: completed by the user and verified

The assistant's earlier deletion attempt was blocked by tool safety checks. No cleanup commit or branch update was made by that attempt, and no alternate mechanism was used to bypass it.

**The user subsequently removed the misplaced files.** A fresh recursive tree read of `kokizzu/edrums/main` at **`80052b611be72cb5d9259dc7456f0f8cd238355e`** showed exactly two files and no `effects/` directory:

| Remaining file | Unchanged blob SHA |
|---|---|
| README.md | 3f3c626c47db0c08a90935ffa1847139bb9e3fca |
| gotro-projects.md | 1a8158501505114aea77b5b210f820aa7099f258 |

Both match their inspected pre-cleanup versions. The old effects files are absent from the current branch tree; this does not claim that their historical commits were erased. No further cleanup is needed. All effects research writes remain restricted to **instrumentfx**.

Verification evidence: [edrums cleanup tree](https://api.github.com/repos/kokizzu/edrums/git/trees/80052b611be72cb5d9259dc7456f0f8cd238355e?recursive=1) and [instrumentfx preserved snapshot](https://api.github.com/repos/kokizzu/instrumentfx/git/trees/b6ca1b7696b9d1021d0080c250b4a70f8a5c14fd?recursive=1).

## Research continuation after transfer

The first display/IDR review for the eight compact models was subsequently committed as eight separate findings, then integrated in **`c77420e66f01a1bad5d5e032d3f9e5ae70e515f5`**. Inventory remains **51 partial models**; no additional models were counted for these notes.

See [RESUME.md](RESUME.md) and [research-state.json](research-state.json) for current progress and unresolved fields. The next review starts with **BOSS GT-1000CORE**. The compact page now has IDR comparison columns and display rows, but unknown diagonals/touch specifications and incomplete local-price evidence remain; the other seven comparison pages still need that review.
