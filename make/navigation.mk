# Existing navigation command API; preserve target names and recipes.

.PHONY: navigation-audit
navigation-audit:
	python3 scripts/navigation_tools.py

.PHONY: navigation-save
navigation-save:
	python3 scripts/navigation_tools.py save

.PHONY: navigation-commit
navigation-commit:
	python3 scripts/navigation_tools.py commit

.PHONY: canonical-links-plan
canonical-links-plan:
	python3 scripts/canonical_links.py plan

.PHONY: canonical-links-apply
canonical-links-apply:
	python3 scripts/canonical_links.py apply

.PHONY: canonical-links-verify
canonical-links-verify:
	python3 scripts/canonical_links.py verify

.PHONY: canonical-links-test
canonical-links-test:
	python3 scripts/canonical_links.py test

.PHONY: canonical-links-plan-boss
canonical-links-plan-boss:
	python3 scripts/canonical_links.py plan-boss

.PHONY: canonical-links-plan-mooer
canonical-links-plan-mooer:
	python3 scripts/canonical_links.py plan-mooer

.PHONY: canonical-links-plan-valeton
canonical-links-plan-valeton:
	python3 scripts/canonical_links.py plan-valeton

.PHONY: canonical-links-plan-zoom
canonical-links-plan-zoom:
	python3 scripts/canonical_links.py plan-zoom

.PHONY: canonical-links-plan-mvave
canonical-links-plan-mvave:
	python3 scripts/canonical_links.py plan-mvave

.PHONY: canonical-links-plan-remaining
canonical-links-plan-remaining:
	python3 scripts/canonical_links.py plan-remaining

.PHONY: canonical-links-apply-remaining
canonical-links-apply-remaining:
	python3 scripts/canonical_links.py apply-remaining

.PHONY: brand-sort-sync
brand-sort-sync:
	python3 scripts/brand_sort.py sync

.PHONY: brand-sort-plan
brand-sort-plan:
	python3 scripts/brand_sort.py plan

.PHONY: brand-sort-apply
brand-sort-apply:
	python3 scripts/brand_sort.py apply

.PHONY: brand-sort-verify
brand-sort-verify:
	python3 scripts/brand_sort.py verify

.PHONY: brand-sort-commit
brand-sort-commit:
	python3 scripts/brand_sort.py commit

.PHONY: brand-sort-test
brand-sort-test:
	python3 scripts/brand_sort.py test

.PHONY: brand-filename-plan
brand-filename-plan:
	python3 scripts/brand_filename_migration.py plan

.PHONY: brand-filename-apply
brand-filename-apply:
	python3 scripts/brand_filename_migration.py apply

.PHONY: brand-filename-verify
brand-filename-verify:
	python3 scripts/brand_filename_migration.py verify

.PHONY: brand-filename-stage
brand-filename-stage:
	python3 scripts/brand_filename_migration.py stage

.PHONY: brand-filename-commit
brand-filename-commit:
	python3 scripts/brand_filename_migration.py commit

.PHONY: brand-filename-diff-check
brand-filename-diff-check:
	python3 scripts/brand_filename_migration.py diffcheck

.PHONY: brand-sort-plan-zoom
brand-sort-plan-zoom:
	python3 scripts/brand_sort.py plan brand/ZOOM.md

.PHONY: brand-sort-apply-zoom
brand-sort-apply-zoom:
	python3 scripts/brand_sort.py apply brand/ZOOM.md

.PHONY: brand-sort-plan-boss
brand-sort-plan-boss:
	python3 scripts/brand_sort.py plan brand/BOSS.md

.PHONY: brand-sort-apply-boss
brand-sort-apply-boss:
	python3 scripts/brand_sort.py apply brand/BOSS.md

.PHONY: brand-sort-plan-valeton
brand-sort-plan-valeton:
	python3 scripts/brand_sort.py plan brand/VALETON.md

.PHONY: brand-sort-apply-valeton
brand-sort-apply-valeton:
	python3 scripts/brand_sort.py apply brand/VALETON.md

.PHONY: brand-sort-plan-korg
brand-sort-plan-korg:
	python3 scripts/brand_sort.py plan brand/KORG.md

.PHONY: brand-sort-apply-korg
brand-sort-apply-korg:
	python3 scripts/brand_sort.py apply brand/KORG.md

.PHONY: brand-sort-plan-tc-electronic
brand-sort-plan-tc-electronic:
	python3 scripts/brand_sort.py plan brand/TC-ELECTRONIC.md

.PHONY: brand-sort-apply-tc-electronic
brand-sort-apply-tc-electronic:
	python3 scripts/brand_sort.py apply brand/TC-ELECTRONIC.md

.PHONY: brand-sort-plan-line6
brand-sort-plan-line6:
	python3 scripts/brand_sort.py plan brand/LINE6.md

.PHONY: brand-sort-apply-line6
brand-sort-apply-line6:
	python3 scripts/brand_sort.py apply brand/LINE6.md

.PHONY: brand-sort-plan-morningstar
brand-sort-plan-morningstar:
	python3 scripts/brand_sort.py plan brand/MORNINGSTAR.md

.PHONY: brand-sort-apply-morningstar
brand-sort-apply-morningstar:
	python3 scripts/brand_sort.py apply brand/MORNINGSTAR.md

.PHONY: brand-sort-plan-hologram
brand-sort-plan-hologram:
	python3 scripts/brand_sort.py plan brand/HOLOGRAM.md

.PHONY: brand-sort-apply-hologram
brand-sort-apply-hologram:
	python3 scripts/brand_sort.py apply brand/HOLOGRAM.md

.PHONY: navigation-test-state
navigation-test-state:
	python3 scripts/navigation_tools.py test-state

.PHONY: brand-sort-plan-digitech
brand-sort-plan-digitech:
	python3 scripts/brand_sort.py plan brand/DIGITECH.md

.PHONY: brand-sort-apply-digitech
brand-sort-apply-digitech:
	python3 scripts/brand_sort.py apply brand/DIGITECH.md

.PHONY: brand-sort-plan-flamma
brand-sort-plan-flamma:
	python3 scripts/brand_sort.py plan brand/FLAMMA.md

.PHONY: brand-sort-apply-flamma
brand-sort-apply-flamma:
	python3 scripts/brand_sort.py apply brand/FLAMMA.md

.PHONY: brand-sort-plan-headrush
brand-sort-plan-headrush:
	python3 scripts/brand_sort.py plan brand/HEADRUSH.md

.PHONY: brand-sort-apply-headrush
brand-sort-apply-headrush:
	python3 scripts/brand_sort.py apply brand/HEADRUSH.md

.PHONY: brand-sort-plan-sheeran
brand-sort-plan-sheeran:
	python3 scripts/brand_sort.py plan brand/SHEERAN-LOOPERS.md

.PHONY: brand-sort-apply-sheeran
brand-sort-apply-sheeran:
	python3 scripts/brand_sort.py apply brand/SHEERAN-LOOPERS.md

.PHONY: brand-sort-plan-neural
brand-sort-plan-neural:
	python3 scripts/brand_sort.py plan brand/NEURAL-DSP.md

.PHONY: brand-sort-apply-neural
brand-sort-apply-neural:
	python3 scripts/brand_sort.py apply brand/NEURAL-DSP.md

.PHONY: brand-sort-plan-mooer
brand-sort-plan-mooer:
	python3 scripts/brand_sort.py plan brand/MOOER.md

.PHONY: brand-sort-apply-mooer
brand-sort-apply-mooer:
	python3 scripts/brand_sort.py apply brand/MOOER.md

.PHONY: brand-sort-plan-harley-benton brand-sort-apply-harley-benton
brand-sort-plan-harley-benton:
	python3 scripts/brand_sort.py plan brand/HARLEY-BENTON.md
brand-sort-apply-harley-benton:
	python3 scripts/brand_sort.py apply brand/HARLEY-BENTON.md

.PHONY: brand-sort-plan-jet-pedals brand-sort-apply-jet-pedals
brand-sort-plan-jet-pedals:
	python3 scripts/brand_sort.py plan brand/JET-PEDALS.md
brand-sort-apply-jet-pedals:
	python3 scripts/brand_sort.py apply brand/JET-PEDALS.md
