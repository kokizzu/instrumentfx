# Existing publication command API; preserve target names and recipes.

.PHONY: research-push-plan
research-push-plan:
	python3 scripts/research_push.py plan

.PHONY: research-push-apply
research-push-apply:
	python3 scripts/research_push.py apply

.PHONY: research-push-inspect
research-push-inspect:
	python3 scripts/research_push.py inspect

.PHONY: research-push-sync
research-push-sync:
	python3 scripts/research_push.py sync

.PHONY: research-push-finalize
research-push-finalize:
	python3 scripts/research_push.py finalize

.PHONY: research-auth-check
research-auth-check:
	python3 scripts/research_push.py auth-check

.PHONY: research-push-plan-https
research-push-plan-https:
	python3 scripts/research_push.py plan-https

.PHONY: research-push-apply-https
research-push-apply-https:
	python3 scripts/research_push.py apply-https

.PHONY: research-stage-transport
research-stage-transport:
	python3 scripts/research_push.py stage-transport

.PHONY: research-commit-transport
research-commit-transport:
	python3 scripts/research_push.py commit-transport
