.PHONY: research-status research-verify research-source-gp200jr research-commit-gp200jr

research-status:
	python3 scripts/research_tools.py status

research-verify:
	python3 scripts/research_tools.py verify

research-source-gp200jr:
	python3 scripts/research_tools.py gp200jr

.PHONY: research-render-gp200jr
research-render-gp200jr:
	python3 scripts/research_tools.py render-gp200jr

research-commit-gp200jr:
	python3 scripts/research_tools.py commit-gp200jr

.PHONY: research-commit-hx-effects
research-commit-hx-effects:
	python3 scripts/research_tools.py commit-hx-effects

.PHONY: comparison-plan
comparison-plan:
	python3 scripts/comparison_views.py plan

.PHONY: comparison-apply comparison-verify research-commit-comparisons
comparison-apply:
	python3 scripts/comparison_views.py apply

comparison-verify:
	python3 scripts/comparison_views.py verify

research-commit-comparisons:
	python3 scripts/research_tools.py commit-comparisons

.PHONY: research-source-prime research-commit-prime
research-source-prime:
	python3 scripts/research_tools.py source-prime

research-commit-prime:
	python3 scripts/research_tools.py commit-prime

.PHONY: research-verify-archive-provenance
research-verify-archive-provenance:
	python3 scripts/research_tools.py restore-archive-provenance

.PHONY: research-source-ge300 research-commit-ge300
research-source-ge300:
	python3 scripts/research_tools.py source-ge300

research-commit-ge300:
	python3 scripts/research_tools.py commit-ge300

.PHONY: research-source-gs1000
research-source-gs1000:
	python3 scripts/research_tools.py source-gs1000

.PHONY: research-commit-gs1000
research-commit-gs1000:
	python3 scripts/research_tools.py commit-gs1000

.PHONY: research-commit-b1xon
research-commit-b1xon:
	python3 scripts/research_tools.py commit-b1xon

.PHONY: consolidation-plan-g6 consolidation-apply-g6 consolidation-commit-g6
consolidation-plan-g6:
	python3 scripts/consolidation_tools.py plan g6
consolidation-apply-g6:
	python3 scripts/consolidation_tools.py apply g6
consolidation-commit-g6:
	python3 scripts/consolidation_tools.py commit g6

.PHONY: consolidation-plan-g1-four consolidation-apply-g1-four consolidation-commit-g1-four
consolidation-plan-g1-four:
	python3 scripts/consolidation_tools.py plan g1-four
consolidation-apply-g1-four:
	python3 scripts/consolidation_tools.py apply g1-four
consolidation-commit-g1-four:
	python3 scripts/consolidation_tools.py commit g1-four

.PHONY: consolidation-plan-g1x-four consolidation-apply-g1x-four consolidation-commit-g1x-four
consolidation-plan-g1x-four:
	python3 scripts/consolidation_tools.py plan g1x-four
consolidation-apply-g1x-four:
	python3 scripts/consolidation_tools.py apply g1x-four
consolidation-commit-g1x-four:
	python3 scripts/consolidation_tools.py commit g1x-four

.PHONY: consolidation-verify
consolidation-verify:
	python3 scripts/consolidation_tools.py verify

.PHONY: consolidation-clean-cache-plan consolidation-clean-cache-apply
consolidation-clean-cache-plan:
	python3 scripts/consolidation_tools.py cache-plan
consolidation-clean-cache-apply:
	python3 scripts/consolidation_tools.py cache-apply
