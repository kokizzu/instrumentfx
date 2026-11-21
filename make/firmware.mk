# One-model firmware and pitch research, with reviewed ordinary publication.
FIRMWARE_EVIDENCE ?= /tmp/instrumentfx-model.json
.PHONY: firmware-model-apply firmware-model-verify firmware-model-review firmware-model-commit
firmware-model-apply:
	python3 -B scripts/firmware_pitch.py apply "$(FIRMWARE_EVIDENCE)"
firmware-model-verify:
	python3 -B scripts/firmware_publish.py verify
firmware-model-review:
	python3 -B scripts/firmware_publish.py review
.PHONY: firmware-model-review-refresh
firmware-model-review-refresh:
	python3 -B scripts/firmware_publish.py refresh-review
firmware-model-commit:
	python3 -B scripts/firmware_publish.py commit

.PHONY: research-source-image-qr
research-source-image-qr:
	python3 scripts/source_image.py qr
