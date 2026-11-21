# Sourced photographs; inspect fetched files before marking visual_checked.
.PHONY: model-images-plan
model-images-plan:
	python3 -B scripts/model_images.py plan

.PHONY: model-images-fetch
model-images-fetch:
	python3 -B scripts/model_images.py fetch

.PHONY: model-images-apply
model-images-apply:
	python3 -B scripts/model_images.py apply

.PHONY: model-images-verify
model-images-verify:
	python3 -B scripts/model_images.py verify

.PHONY: model-images-review
model-images-review:
	python3 -B scripts/model_images.py review

.PHONY: model-images-commit
model-images-commit:
	python3 -B scripts/model_images.py commit
