# Existing retirement command API; preserve target names and recipes.

.PHONY: metadata-plan
metadata-plan:
	python3 scripts/metadata_consolidation.py plan

.PHONY: metadata-apply
metadata-apply:
	python3 scripts/metadata_consolidation.py apply

.PHONY: metadata-verify
metadata-verify:
	python3 scripts/metadata_consolidation.py verify

.PHONY: metadata-commit
metadata-commit:
	python3 scripts/metadata_consolidation.py commit

.PHONY: metadata-retirement-plan
metadata-retirement-plan:
	python3 scripts/source_retirement.py plan

.PHONY: metadata-retirement-apply
metadata-retirement-apply:
	python3 scripts/source_retirement.py apply

.PHONY: metadata-retirement-verify
metadata-retirement-verify:
	python3 scripts/source_retirement.py verify

.PHONY: metadata-retirement-commit
metadata-retirement-commit:
	python3 scripts/source_retirement.py commit

.PHONY: metadata-retirement-rollback-plan
metadata-retirement-rollback-plan:
	python3 scripts/source_retirement.py rollback-plan

.PHONY: metadata-retirement-rollback-apply
metadata-retirement-rollback-apply:
	python3 scripts/source_retirement.py rollback-apply

.PHONY: technical-retirement-plan
technical-retirement-plan:
	python3 scripts/technical_retirement.py plan

.PHONY: technical-retirement-apply
technical-retirement-apply:
	python3 scripts/technical_retirement.py apply

.PHONY: technical-retirement-verify
technical-retirement-verify:
	python3 -u scripts/technical_retirement.py verify

.PHONY: technical-retirement-commit
technical-retirement-commit:
	python3 scripts/technical_retirement.py commit

.PHONY: technical-retirement-rollback-plan
technical-retirement-rollback-plan:
	python3 scripts/technical_retirement.py rollback-plan

.PHONY: specialist-retirement-plan
specialist-retirement-plan:
	python3 scripts/technical_retirement.py specialist-plan

.PHONY: specialist-retirement-apply
specialist-retirement-apply:
	python3 scripts/technical_retirement.py specialist-apply

.PHONY: specialist-retirement-verify
specialist-retirement-verify:
	python3 scripts/technical_retirement.py specialist-verify

.PHONY: specialist-retirement-commit
specialist-retirement-commit:
	python3 scripts/technical_retirement.py specialist-commit

.PHONY: json-retirement-plan
json-retirement-plan:
	python3 scripts/source_retirement.py json-plan

.PHONY: json-retirement-apply
json-retirement-apply:
	python3 scripts/source_retirement.py json-apply

.PHONY: json-retirement-verify
json-retirement-verify:
	python3 scripts/source_retirement.py json-verify

.PHONY: json-retirement-commit
json-retirement-commit:
	python3 scripts/source_retirement.py json-commit

.PHONY: json-retirement-rollback-plan
json-retirement-rollback-plan:
	python3 scripts/source_retirement.py json-rollback-plan

.PHONY: research-ledger-history
research-ledger-history:
	python3 scripts/ledger_history.py

.PHONY: json-pointer-removal-plan
json-pointer-removal-plan:
	python3 scripts/json_pointer_removal.py plan

.PHONY: json-pointer-removal-apply
json-pointer-removal-apply:
	python3 scripts/json_pointer_removal.py apply

.PHONY: json-pointer-removal-verify
json-pointer-removal-verify:
	python3 scripts/json_pointer_removal.py verify

.PHONY: json-pointer-removal-commit
json-pointer-removal-commit:
	python3 scripts/json_pointer_removal.py commit

.PHONY: json-pointer-rollback-plan
json-pointer-rollback-plan:
	python3 scripts/json_pointer_removal.py rollback-plan

.PHONY: metadata-history-audit
metadata-history-audit:
	python3 scripts/metadata_consolidation.py audit-history

.PHONY: metadata-history-test
metadata-history-test:
	python3 scripts/metadata_consolidation.py test-history

.PHONY: metadata-stage
metadata-stage:
	python3 scripts/metadata_consolidation.py stage

.PHONY: metadata-history-preservation-plan
metadata-history-preservation-plan:
	python3 scripts/metadata_consolidation.py plan-history

.PHONY: metadata-history-source-plan
metadata-history-source-plan:
	python3 scripts/metadata_consolidation.py plan-history-source

.PHONY: metadata-history-json-plan
metadata-history-json-plan:
	python3 scripts/metadata_consolidation.py plan-history-json

.PHONY: preservation-review-ge100-pro
preservation-review-ge100-pro:
	python3 scripts/preservation_review.py effects/findings/2026-10-14-mooer-ge100-pro.md

.PHONY: preservation-review-ge100-pro-li
preservation-review-ge100-pro-li:
	python3 scripts/preservation_review.py effects/findings/2026-10-14-mooer-ge100-pro-li.md

.PHONY: preservation-review-ampero-ii-stomp
preservation-review-ampero-ii-stomp:
	python3 scripts/preservation_review.py effects/findings/2026-10-15-hotone-ampero-ii-stomp-mp300.md

.PHONY: preservation-review-trident
preservation-review-trident:
	python3 scripts/preservation_review.py effects/findings/2026-10-15-nux-trident.md

.PHONY: technical-compatibility-removal-preview
technical-compatibility-removal-preview:
	python3 scripts/technical_retirement.py compatibility-preview

.PHONY: technical-compatibility-preview-test
technical-compatibility-preview-test:
	python3 scripts/technical_retirement.py compatibility-preview-test

.PHONY: technical-compatibility-operation-test
technical-compatibility-operation-test:
	python3 scripts/compatibility_removal.py test

.PHONY: technical-compatibility-remove-plan
technical-compatibility-remove-plan:
	python3 scripts/compatibility_removal.py remove-plan

.PHONY: technical-compatibility-restore-plan
technical-compatibility-restore-plan:
	python3 scripts/compatibility_removal.py restore-plan

.PHONY: technical-compatibility-operation-apply
technical-compatibility-operation-apply:
	python3 scripts/compatibility_removal.py apply

.PHONY: metadata-compatibility-remove-plan
metadata-compatibility-remove-plan:
	python3 scripts/compatibility_removal.py metadata-remove-plan

.PHONY: metadata-compatibility-restore-plan
metadata-compatibility-restore-plan:
	python3 scripts/compatibility_removal.py metadata-restore-plan

.PHONY: archive-history-test
archive-history-test:
	python3 scripts/archive_retirement.py test

.PHONY: archive-history-audit
archive-history-audit:
	python3 scripts/archive_retirement.py audit

.PHONY: archive-preservation-plan
archive-preservation-plan:
	python3 scripts/archive_retirement.py preservation-plan

.PHONY: archive-preservation-apply
archive-preservation-apply:
	python3 scripts/archive_retirement.py preservation-apply

.PHONY: archive-preservation-verify
archive-preservation-verify:
	python3 scripts/archive_retirement.py verify

.PHONY: archive-registration-plan
archive-registration-plan:
	python3 scripts/archive_retirement.py registration-plan

.PHONY: archive-registration-apply
archive-registration-apply:
	python3 scripts/archive_retirement.py registration-apply

.PHONY: archive-compatibility-remove-plan
archive-compatibility-remove-plan:
	python3 scripts/compatibility_removal.py archive-remove-plan

.PHONY: archive-compatibility-restore-plan
archive-compatibility-restore-plan:
	python3 scripts/compatibility_removal.py archive-restore-plan
