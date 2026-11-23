.PHONY: coverage-generate coverage-verify coverage-review coverage-commit
coverage-generate:
	python3 -B scripts/coverage_views.py generate
coverage-verify:
	python3 -B scripts/coverage_views.py verify
coverage-review:
	python3 -B scripts/coverage_views.py review
coverage-commit:
	python3 -B scripts/coverage_views.py commit

.PHONY: coverage-review-refresh
coverage-review-refresh:
	python3 -B scripts/coverage_views.py refresh
