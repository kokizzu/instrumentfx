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

.PHONY: model-images-test
model-images-test:
	python3 -B scripts/model_images.py test

# Bounded extraction of an original manufacturer manual figure.
.PHONY: model-images-diagram
model-images-diagram:
	python3 -B scripts/model_images.py diagram

# Archive the exact SHA-verified source image bytes under brand/images.
IMAGE_ARCHIVE_LIMIT ?= 402
.PHONY: model-images-archive-plan model-images-archive
model-images-archive-plan:
	python3 -B scripts/model_images.py archive-plan $(IMAGE_ARCHIVE_LIMIT)

model-images-archive:
	python3 -B scripts/model_images.py archive $(IMAGE_ARCHIVE_LIMIT)
