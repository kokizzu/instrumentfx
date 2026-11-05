# Command index. Keep recipes in cohesive make/ modules.
# The historical default is explicit so include order cannot change it.
.DEFAULT_GOAL := research-status

include make/research.mk
include make/consolidation.mk
include make/comparisons.mk
include make/navigation.mk
include make/expression.mk
include make/retirement.mk
include make/publication.mk

.PHONY: make-modules-plan
make-modules-plan:
	python3 scripts/make_modules.py plan

.PHONY: make-modules-apply
make-modules-apply:
	python3 scripts/make_modules.py apply

.PHONY: make-modules-test
make-modules-test:
	python3 scripts/make_modules.py test

.PHONY: make-modules-verify
make-modules-verify:
	python3 scripts/make_modules.py verify

.PHONY: make-modules-stage
make-modules-stage:
	python3 scripts/make_modules.py stage

.PHONY: make-modules-commit
make-modules-commit:
	python3 scripts/make_modules.py commit
