# One-model firmware and pitch research, with reviewed ordinary publication.
FIRMWARE_EVIDENCE ?= /tmp/instrumentfx-model.json
.PHONY: firmware-model-apply firmware-model-verify firmware-model-review firmware-model-commit
firmware-model-apply:
	python3 -B scripts/firmware_pitch.py apply "$(FIRMWARE_EVIDENCE)"
firmware-model-verify:
	python3 -B scripts/firmware_publish.py verify
firmware-model-review:
	python3 -B scripts/firmware_publish.py review
firmware-model-commit:
	python3 -B scripts/firmware_publish.py commit
