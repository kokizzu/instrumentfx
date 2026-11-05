# Existing expression command API; preserve target names and recipes.

.PHONY: expression-audit-commit-neural
expression-audit-commit-neural:
	python3 scripts/expression_audit_neural.py commit

.PHONY: expression-audit-commit-valeton
expression-audit-commit-valeton:
	python3 scripts/expression_audit_valeton.py commit

.PHONY: expression-audit-commit-line6
expression-audit-commit-line6:
	python3 scripts/expression_audit_line6.py commit

.PHONY: expression-audit-commit-boss
expression-audit-commit-boss:
	python3 scripts/expression_audit_boss.py commit

.PHONY: expression-audit-commit-mvave
expression-audit-commit-mvave:
	python3 scripts/expression_audit_mvave.py commit

.PHONY: expression-audit-commit-headrush
expression-audit-commit-headrush:
	python3 scripts/expression_audit_headrush.py commit

.PHONY: expression-audit-commit-tc
expression-audit-commit-tc:
	python3 scripts/expression_audit_tc.py commit

.PHONY: expression-audit-commit-zoom
expression-audit-commit-zoom:
	python3 scripts/expression_audit_zoom.py commit

.PHONY: expression-audit-commit-digitech
expression-audit-commit-digitech:
	python3 scripts/expression_audit_digitech.py commit

.PHONY: expression-audit-commit-nux
expression-audit-commit-nux:
	python3 scripts/expression_audit_nux.py commit

.PHONY: expression-audit-commit-sonicake
expression-audit-commit-sonicake:
	python3 scripts/expression_audit_sonicake.py commit

.PHONY: expression-audit-commit-eventide
expression-audit-commit-eventide:
	python3 scripts/expression_audit_eventide.py commit

.PHONY: expression-audit-commit-ik
expression-audit-commit-ik:
	python3 scripts/expression_audit_ik.py commit

.PHONY: expression-audit-commit-zoom-505
expression-audit-commit-zoom-505:
	python3 scripts/expression_audit_zoom.py commit-505

.PHONY: expression-audit-commit-zoom-606
expression-audit-commit-zoom-606:
	python3 scripts/expression_audit_zoom.py commit-606

.PHONY: expression-audit-commit-zoom-607
expression-audit-commit-zoom-607:
	python3 scripts/expression_audit_zoom.py commit-607

.PHONY: expression-audit-commit-korg
expression-audit-commit-korg:
	python3 scripts/expression_audit_korg.py commit

.PHONY: expression-audit-commit-fender
expression-audit-commit-fender:
	python3 scripts/expression_audit_fender.py commit

.PHONY: expression-audit-commit-kemper
expression-audit-commit-kemper:
	python3 scripts/expression_audit_kemper.py commit

.PHONY: expression-audit-commit-flamma
expression-audit-commit-flamma:
	python3 scripts/expression_audit_flamma.py commit

.PHONY: expression-audit-commit-fractal
expression-audit-commit-fractal:
	python3 scripts/expression_audit_fractal.py commit

.PHONY: expression-audit-commit-vox
expression-audit-commit-vox:
	python3 scripts/expression_audit_vox.py commit

.PHONY: expression-audit-commit-audota
expression-audit-commit-audota:
	python3 scripts/expression_audit_audota.py commit

.PHONY: expression-audit-commit-behringer
expression-audit-commit-behringer:
	python3 scripts/expression_audit_behringer.py commit

.PHONY: expression-audit-commit-lexicon
expression-audit-commit-lexicon:
	python3 scripts/expression_audit_lexicon.py commit

.PHONY: expression-audit-commit-alesis
expression-audit-commit-alesis:
	python3 scripts/expression_audit_alesis.py commit

.PHONY: expression-audit-commit-ammoon
expression-audit-commit-ammoon:
	python3 scripts/expression_audit_ammoon.py commit

.PHONY: expression-audit-commit-donner
expression-audit-commit-donner:
	python3 scripts/expression_audit_donner.py commit

.PHONY: expression-audit-commit-keeley
expression-audit-commit-keeley:
	python3 scripts/expression_audit_keeley.py commit

.PHONY: research-commit-melofty-display
research-commit-melofty-display:
	python3 scripts/display_audit_melofty.py

.PHONY: research-commit-display-collection
research-commit-display-collection:
	python3 scripts/display_audit_melofty.py collection

.PHONY: research-commit-morningstar-display
research-commit-morningstar-display:
	python3 scripts/display_audit_melofty.py morningstar

.PHONY: research-commit-famc-display
research-commit-famc-display:
	python3 scripts/display_audit_melofty.py famc

.PHONY: expression-audit-commit-mod
expression-audit-commit-mod:
	python3 scripts/expression_audit_mod.py commit

.PHONY: expression-audit-commit-hologram
expression-audit-commit-hologram:
	python3 scripts/expression_audit_mod.py commit-hologram

.PHONY: expression-audit-stage-fractal
expression-audit-stage-fractal:
	python3 scripts/expression_audit_fractal.py stage

.PHONY: expression-audit-stage-zoom
expression-audit-stage-zoom:
	python3 scripts/expression_audit_zoom.py stage

.PHONY: expression-audit-stage-mod
expression-audit-stage-mod:
	python3 scripts/expression_audit_mod.py stage

.PHONY: research-stage-display-collection
research-stage-display-collection:
	python3 scripts/display_audit_melofty.py stage-collection

.PHONY: expression-audit-stage-headrush
expression-audit-stage-headrush:
	python3 scripts/expression_audit_headrush.py stage

.PHONY: expression-audit-stage-line6
expression-audit-stage-line6:
	python3 scripts/expression_audit_line6.py stage

.PHONY: expression-audit-stage-valeton
expression-audit-stage-valeton:
	python3 scripts/expression_audit_valeton.py stage

.PHONY: expression-audit-stage-boss
expression-audit-stage-boss:
	python3 scripts/expression_audit_boss.py stage

.PHONY: expression-audit-stage-digitech
expression-audit-stage-digitech:
	python3 scripts/expression_audit_digitech.py stage

.PHONY: expression-audit-stage-empress
expression-audit-stage-empress:
	python3 scripts/expression_audit_empress.py stage

.PHONY: expression-audit-commit-empress
expression-audit-commit-empress:
	python3 scripts/expression_audit_empress.py commit

.PHONY: expression-audit-stage-eventide
expression-audit-stage-eventide:
	python3 scripts/expression_audit_eventide.py stage

.PHONY: expression-audit-stage-poly
expression-audit-stage-poly:
	python3 scripts/expression_audit_poly.py stage

.PHONY: expression-audit-commit-poly
expression-audit-commit-poly:
	python3 scripts/expression_audit_poly.py commit

.PHONY: expression-audit-stage-fender
expression-audit-stage-fender:
	python3 scripts/expression_audit_fender.py stage

.PHONY: expression-audit-stage-mvave
expression-audit-stage-mvave:
	python3 scripts/expression_audit_mvave.py stage

.PHONY: expression-audit-stage-nux
expression-audit-stage-nux:
	python3 scripts/expression_audit_nux.py stage

.PHONY: expression-audit-stage-neural
expression-audit-stage-neural:
	python3 scripts/expression_audit_neural.py stage

.PHONY: expression-audit-stage-sonicake
expression-audit-stage-sonicake:
	python3 scripts/expression_audit_sonicake.py stage

expression-audit-stage-walrus:
	python3 scripts/expression_audit_poly.py stage-walrus

expression-audit-commit-walrus:
	python3 scripts/expression_audit_poly.py commit-walrus

expression-audit-stage-korg:
	python3 scripts/expression_audit_korg.py stage

.PHONY: expression-audit-stage-fishman
expression-audit-stage-fishman:
	python3 scripts/expression_audit_poly.py stage-fishman

.PHONY: expression-audit-commit-fishman
expression-audit-commit-fishman:
	python3 scripts/expression_audit_poly.py commit-fishman

.PHONY: expression-audit-stage-darkglass
expression-audit-stage-darkglass:
	python3 scripts/expression_audit_darkglass.py stage

.PHONY: expression-audit-commit-darkglass
expression-audit-commit-darkglass:
	python3 scripts/expression_audit_darkglass.py commit

.PHONY: expression-audit-stage-behringer
expression-audit-stage-behringer:
	python3 scripts/expression_audit_behringer.py stage

.PHONY: expression-audit-stage-lexicon
expression-audit-stage-lexicon:
	python3 scripts/expression_audit_lexicon.py stage
