# Existing comparisons command API; preserve target names and recipes.

.PHONY: comparison-plan
comparison-plan:
	python3 scripts/comparison_views.py plan

.PHONY: comparison-apply
comparison-apply:
	python3 scripts/comparison_views.py apply

.PHONY: comparison-verify
comparison-verify:
	python3 scripts/comparison_views.py verify

.PHONY: comparison-test-selection
comparison-test-selection:
	python3 scripts/comparison_views.py test-selection

.PHONY: comparison-test-fields
comparison-test-fields:
	python3 scripts/comparison_views.py test-fields

.PHONY: comparison-test-extraction
comparison-test-extraction:
	python3 scripts/comparison_views.py test-extraction

.PHONY: comparison-test-counts
comparison-test-counts:
	python3 scripts/comparison_views.py test-counts

.PHONY: research-gaps-plan
research-gaps-plan:
	python3 scripts/research_gaps.py plan

.PHONY: research-gaps-apply
research-gaps-apply:
	python3 scripts/research_gaps.py apply

.PHONY: research-gaps-commit
research-gaps-commit:
	python3 scripts/research_gaps.py commit

.PHONY: research-gaps-test
research-gaps-test:
	python3 scripts/research_gaps.py test

.PHONY: comparison-stage
comparison-stage:
	python3 scripts/comparison_publication.py stage

.PHONY: comparison-commit
comparison-commit:
	python3 scripts/comparison_publication.py commit

.PHONY: discovery-resolution-test
discovery-resolution-test:
	python3 scripts/discovery_resolution.py test

.PHONY: discovery-resolution-plan
discovery-resolution-plan:
	python3 scripts/discovery_resolution.py plan

.PHONY: discovery-resolution-apply
discovery-resolution-apply:
	python3 scripts/discovery_resolution.py apply

.PHONY: discovery-resolution-stage
discovery-resolution-stage:
	python3 scripts/discovery_resolution.py stage

.PHONY: discovery-resolution-commit
discovery-resolution-commit:
	python3 scripts/discovery_resolution.py commit

.PHONY: creative-stage
creative-stage:
	python3 scripts/creative_effects.py stage

.PHONY: creative-commit
creative-commit:
	python3 scripts/creative_effects.py commit

.PHONY: creative-verify
creative-verify:
	python3 scripts/creative_effects.py verify

.PHONY: creative-publication-audit
creative-publication-audit:
	python3 scripts/creative_publication_audit.py

.PHONY: creative-publication-stage
creative-publication-stage:
	python3 scripts/creative_publication_audit.py stage

.PHONY: creative-publication-commit
creative-publication-commit:
	python3 scripts/creative_publication_audit.py commit

.PHONY: creative-publication-push
creative-publication-push:
	python3 scripts/creative_publication_audit.py publish

.PHONY: research-field-audit
research-field-audit:
	python3 scripts/comparison_views.py research-field-audit

.PHONY: research-field-audit-test
research-field-audit-test:
	python3 scripts/comparison_views.py research-field-audit-test
