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

.PHONY: consolidation-plan-g2-four consolidation-apply-g2-four consolidation-commit-g2-four
consolidation-plan-g2-four:
	python3 scripts/consolidation_tools.py plan g2-four
consolidation-apply-g2-four:
	python3 scripts/consolidation_tools.py apply g2-four
consolidation-commit-g2-four:
	python3 scripts/consolidation_tools.py commit g2-four

.PHONY: consolidation-plan-g2x-four consolidation-apply-g2x-four consolidation-commit-g2x-four
consolidation-plan-g2x-four:
	python3 scripts/consolidation_tools.py plan g2x-four
consolidation-apply-g2x-four:
	python3 scripts/consolidation_tools.py apply g2x-four
consolidation-commit-g2x-four:
	python3 scripts/consolidation_tools.py commit g2x-four

.PHONY: consolidation-commit-b1-four
consolidation-commit-b1-four:
	python3 scripts/consolidation_tools.py commit b1-four

.PHONY: consolidation-commit-b1x-four
consolidation-commit-b1x-four:
	python3 scripts/consolidation_tools.py commit b1x-four

.PHONY: consolidation-commit-b2-four
consolidation-commit-b2-four:
	python3 scripts/consolidation_tools.py commit b2-four

.PHONY: research-source-b2-controls
research-source-b2-controls:
	python3 scripts/research_tools.py source-b2-controls

.PHONY: consolidation-commit-b6
consolidation-commit-b6:
	python3 scripts/consolidation_tools.py commit b6

.PHONY: consolidation-commit-v3
consolidation-commit-v3:
	python3 scripts/consolidation_tools.py commit v3

.PHONY: consolidation-commit-v6-sp
consolidation-commit-v6-sp:
	python3 scripts/consolidation_tools.py commit v6-sp

.PHONY: consolidation-commit-gt-1b
consolidation-commit-gt-1b:
	python3 scripts/consolidation_tools.py commit gt-1b

.PHONY: consolidation-commit-gx-1b
consolidation-commit-gx-1b:
	python3 scripts/consolidation_tools.py commit gx-1b

.PHONY: consolidation-commit-me-90b
consolidation-commit-me-90b:
	python3 scripts/consolidation_tools.py commit me-90b

.PHONY: consolidation-commit-ve-1
consolidation-commit-ve-1:
	python3 scripts/consolidation_tools.py commit ve-1

.PHONY: consolidation-commit-ve-2
consolidation-commit-ve-2:
	python3 scripts/consolidation_tools.py commit ve-2

.PHONY: consolidation-commit-ve-500
consolidation-commit-ve-500:
	python3 scripts/consolidation_tools.py commit ve-500

.PHONY: consolidation-commit-ve-22
consolidation-commit-ve-22:
	python3 scripts/consolidation_tools.py commit ve-22

.PHONY: consolidation-commit-ve-8
consolidation-commit-ve-8:
	python3 scripts/consolidation_tools.py commit ve-8

.PHONY: consolidation-commit-ve-20
consolidation-commit-ve-20:
	python3 scripts/consolidation_tools.py commit ve-20

.PHONY: consolidation-commit-gt-1000core
consolidation-commit-gt-1000core:
	python3 scripts/consolidation_tools.py commit gt-1000core

.PHONY: consolidation-commit-gx-10
consolidation-commit-gx-10:
	python3 scripts/consolidation_tools.py commit gx-10

.PHONY: comparison-test-selection
comparison-test-selection:
	python3 scripts/comparison_views.py test-selection

.PHONY: consolidation-commit-gt-1
consolidation-commit-gt-1:
	python3 scripts/consolidation_tools.py commit gt-1

.PHONY: consolidation-commit-gx-1
consolidation-commit-gx-1:
	python3 scripts/consolidation_tools.py commit gx-1

.PHONY: consolidation-commit-me-90
consolidation-commit-me-90:
	python3 scripts/consolidation_tools.py commit me-90

.PHONY: consolidation-commit-gx-100
consolidation-commit-gx-100:
	python3 scripts/consolidation_tools.py commit gx-100

.PHONY: consolidation-commit-gt-1000
consolidation-commit-gt-1000:
	python3 scripts/consolidation_tools.py commit gt-1000

.PHONY: consolidation-commit-gm-800
consolidation-commit-gm-800:
	python3 scripts/consolidation_tools.py commit gm-800

.PHONY: research-commit-helix-lt
research-commit-helix-lt:
	python3 scripts/research_tools.py commit-helix-lt

.PHONY: research-commit-gt100
research-commit-gt100:
	python3 scripts/research_tools.py commit-gt100

.PHONY: consolidation-plan-hx-stomp-xl consolidation-apply-hx-stomp-xl consolidation-commit-hx-stomp-xl
consolidation-plan-hx-stomp-xl:
	python3 scripts/consolidation_tools.py plan hx-stomp-xl
consolidation-apply-hx-stomp-xl:
	python3 scripts/consolidation_tools.py apply hx-stomp-xl
consolidation-commit-hx-stomp-xl:
	python3 scripts/consolidation_tools.py commit hx-stomp-xl

.PHONY: consolidation-plan-ampero-mini consolidation-apply-ampero-mini consolidation-commit-ampero-mini
consolidation-plan-ampero-mini:
	python3 scripts/consolidation_tools.py plan ampero-mini
consolidation-apply-ampero-mini:
	python3 scripts/consolidation_tools.py apply ampero-mini
consolidation-commit-ampero-mini:
	python3 scripts/consolidation_tools.py commit ampero-mini

.PHONY: consolidation-plan-ampero-mp100 consolidation-apply-ampero-mp100 consolidation-commit-ampero-mp100
consolidation-plan-ampero-mp100:
	python3 scripts/consolidation_tools.py plan ampero-mp100
consolidation-apply-ampero-mp100:
	python3 scripts/consolidation_tools.py apply ampero-mp100
consolidation-commit-ampero-mp100:
	python3 scripts/consolidation_tools.py commit ampero-mp100

.PHONY: consolidation-plan-ampero-mp350 consolidation-apply-ampero-mp350 consolidation-commit-ampero-mp350
consolidation-plan-ampero-mp350:
	python3 scripts/consolidation_tools.py plan ampero-mp350
consolidation-apply-ampero-mp350:
	python3 scripts/consolidation_tools.py apply ampero-mp350
consolidation-commit-ampero-mp350:
	python3 scripts/consolidation_tools.py commit ampero-mp350

.PHONY: consolidation-plan-ampero-mp380 consolidation-apply-ampero-mp380 consolidation-commit-ampero-mp380
consolidation-plan-ampero-mp380:
	python3 scripts/consolidation_tools.py plan ampero-mp380
consolidation-apply-ampero-mp380:
	python3 scripts/consolidation_tools.py apply ampero-mp380
consolidation-commit-ampero-mp380:
	python3 scripts/consolidation_tools.py commit ampero-mp380

.PHONY: consolidation-plan-ampero-mp300 consolidation-apply-ampero-mp300 consolidation-commit-ampero-mp300
consolidation-plan-ampero-mp300:
	python3 scripts/consolidation_tools.py plan ampero-mp300
consolidation-apply-ampero-mp300:
	python3 scripts/consolidation_tools.py apply ampero-mp300
consolidation-commit-ampero-mp300:
	python3 scripts/consolidation_tools.py commit ampero-mp300

.PHONY: consolidation-plan-ge100-original consolidation-apply-ge100-original consolidation-commit-ge100-original
consolidation-plan-ge100-original:
	python3 scripts/consolidation_tools.py plan ge100-original
consolidation-apply-ge100-original:
	python3 scripts/consolidation_tools.py apply ge100-original
consolidation-commit-ge100-original:
	python3 scripts/consolidation_tools.py commit ge100-original

.PHONY: consolidation-plan-ge150-original consolidation-apply-ge150-original consolidation-commit-ge150-original
consolidation-plan-ge150-original:
	python3 scripts/consolidation_tools.py plan ge150-original
consolidation-apply-ge150-original:
	python3 scripts/consolidation_tools.py apply ge150-original
consolidation-commit-ge150-original:
	python3 scripts/consolidation_tools.py commit ge150-original

.PHONY: consolidation-plan-ge200-original consolidation-apply-ge200-original consolidation-commit-ge200-original
consolidation-plan-ge200-original:
	python3 scripts/consolidation_tools.py plan ge200-original
consolidation-apply-ge200-original:
	python3 scripts/consolidation_tools.py apply ge200-original
consolidation-commit-ge200-original:
	python3 scripts/consolidation_tools.py commit ge200-original

.PHONY: consolidation-plan-ge150-pro-li consolidation-apply-ge150-pro-li consolidation-commit-ge150-pro-li
consolidation-plan-ge150-pro-li:
	python3 scripts/consolidation_tools.py plan ge150-pro-li
consolidation-apply-ge150-pro-li:
	python3 scripts/consolidation_tools.py apply ge150-pro-li
consolidation-commit-ge150-pro-li:
	python3 scripts/consolidation_tools.py commit ge150-pro-li

.PHONY: consolidation-plan-ge100-pro consolidation-apply-ge100-pro consolidation-commit-ge100-pro
consolidation-plan-ge100-pro:
	python3 scripts/consolidation_tools.py plan ge100-pro
consolidation-apply-ge100-pro:
	python3 scripts/consolidation_tools.py apply ge100-pro
consolidation-commit-ge100-pro:
	python3 scripts/consolidation_tools.py commit ge100-pro

.PHONY: consolidation-plan-ge100-pro-li consolidation-apply-ge100-pro-li consolidation-commit-ge100-pro-li
consolidation-plan-ge100-pro-li:
	python3 scripts/consolidation_tools.py plan ge100-pro-li
consolidation-apply-ge100-pro-li:
	python3 scripts/consolidation_tools.py apply ge100-pro-li
consolidation-commit-ge100-pro-li:
	python3 scripts/consolidation_tools.py commit ge100-pro-li

.PHONY: consolidation-plan-ge200-pro consolidation-apply-ge200-pro consolidation-commit-ge200-pro
consolidation-plan-ge200-pro:
	python3 scripts/consolidation_tools.py plan ge200-pro
consolidation-apply-ge200-pro:
	python3 scripts/consolidation_tools.py apply ge200-pro
consolidation-commit-ge200-pro:
	python3 scripts/consolidation_tools.py commit ge200-pro

.PHONY: consolidation-plan-ge200-pro-li consolidation-apply-ge200-pro-li consolidation-commit-ge200-pro-li
consolidation-plan-ge200-pro-li:
	python3 scripts/consolidation_tools.py plan ge200-pro-li
consolidation-apply-ge200-pro-li:
	python3 scripts/consolidation_tools.py apply ge200-pro-li
consolidation-commit-ge200-pro-li:
	python3 scripts/consolidation_tools.py commit ge200-pro-li

.PHONY: consolidation-plan-ge150-pro consolidation-apply-ge150-pro consolidation-commit-ge150-pro
consolidation-plan-ge150-pro:
	python3 scripts/consolidation_tools.py plan ge150-pro
consolidation-apply-ge150-pro:
	python3 scripts/consolidation_tools.py apply ge150-pro
consolidation-commit-ge150-pro:
	python3 scripts/consolidation_tools.py commit ge150-pro

.PHONY: consolidation-plan-ge150-plus consolidation-apply-ge150-plus consolidation-commit-ge150-plus
consolidation-plan-ge150-plus:
	python3 scripts/consolidation_tools.py plan ge150-plus
consolidation-apply-ge150-plus:
	python3 scripts/consolidation_tools.py apply ge150-plus
consolidation-commit-ge150-plus:
	python3 scripts/consolidation_tools.py commit ge150-plus

.PHONY: consolidation-plan-ge150-plus-li consolidation-apply-ge150-plus-li consolidation-commit-ge150-plus-li
consolidation-plan-ge150-plus-li:
	python3 scripts/consolidation_tools.py plan ge150-plus-li
consolidation-apply-ge150-plus-li:
	python3 scripts/consolidation_tools.py apply ge150-plus-li
consolidation-commit-ge150-plus-li:
	python3 scripts/consolidation_tools.py commit ge150-plus-li

.PHONY: consolidation-plan-ge150-max consolidation-apply-ge150-max consolidation-commit-ge150-max
consolidation-plan-ge150-max:
	python3 scripts/consolidation_tools.py plan ge150-max
consolidation-apply-ge150-max:
	python3 scripts/consolidation_tools.py apply ge150-max
consolidation-commit-ge150-max:
	python3 scripts/consolidation_tools.py commit ge150-max

.PHONY: consolidation-plan-ge150-max-li consolidation-apply-ge150-max-li consolidation-commit-ge150-max-li
consolidation-plan-ge150-max-li:
	python3 scripts/consolidation_tools.py plan ge150-max-li
consolidation-apply-ge150-max-li:
	python3 scripts/consolidation_tools.py apply ge150-max-li
consolidation-commit-ge150-max-li:
	python3 scripts/consolidation_tools.py commit ge150-max-li

.PHONY: consolidation-plan-ge1000 consolidation-apply-ge1000 consolidation-commit-ge1000
consolidation-plan-ge1000:
	python3 scripts/consolidation_tools.py plan ge1000
consolidation-apply-ge1000:
	python3 scripts/consolidation_tools.py apply ge1000
consolidation-commit-ge1000:
	python3 scripts/consolidation_tools.py commit ge1000

.PHONY: consolidation-plan-ge1000-li consolidation-apply-ge1000-li consolidation-commit-ge1000-li
consolidation-plan-ge1000-li:
	python3 scripts/consolidation_tools.py plan ge1000-li
consolidation-apply-ge1000-li:
	python3 scripts/consolidation_tools.py apply ge1000-li
consolidation-commit-ge1000-li:
	python3 scripts/consolidation_tools.py commit ge1000-li

.PHONY: consolidation-plan-gp-100 consolidation-apply-gp-100 consolidation-commit-gp-100
consolidation-plan-gp-100:
	python3 scripts/consolidation_tools.py plan gp-100
consolidation-apply-gp-100:
	python3 scripts/consolidation_tools.py apply gp-100
consolidation-commit-gp-100:
	python3 scripts/consolidation_tools.py commit gp-100

.PHONY: consolidation-plan-gp-150 consolidation-apply-gp-150 consolidation-commit-gp-150
consolidation-plan-gp-150:
	python3 scripts/consolidation_tools.py plan gp-150
consolidation-apply-gp-150:
	python3 scripts/consolidation_tools.py apply gp-150
consolidation-commit-gp-150:
	python3 scripts/consolidation_tools.py commit gp-150

.PHONY: consolidation-plan-gp-200 consolidation-apply-gp-200 consolidation-commit-gp-200
consolidation-plan-gp-200:
	python3 scripts/consolidation_tools.py plan gp-200
consolidation-apply-gp-200:
	python3 scripts/consolidation_tools.py apply gp-200
consolidation-commit-gp-200:
	python3 scripts/consolidation_tools.py commit gp-200

.PHONY: research-commit-gp150-nam
research-commit-gp150-nam:
	python3 scripts/research_tools.py commit-gp150-nam

.PHONY: consolidation-plan-gp-180 consolidation-apply-gp-180 consolidation-commit-gp-180
consolidation-plan-gp-180:
	python3 scripts/consolidation_tools.py plan gp-180
consolidation-apply-gp-180:
	python3 scripts/consolidation_tools.py apply gp-180
consolidation-commit-gp-180:
	python3 scripts/consolidation_tools.py commit gp-180

.PHONY: research-commit-gp100-nam
research-commit-gp100-nam:
	python3 scripts/research_tools.py commit-gp100-nam

.PHONY: consolidation-plan-gp-5 consolidation-apply-gp-5 consolidation-commit-gp-5
consolidation-plan-gp-5:
	python3 scripts/consolidation_tools.py plan gp-5
consolidation-apply-gp-5:
	python3 scripts/consolidation_tools.py apply gp-5
consolidation-commit-gp-5:
	python3 scripts/consolidation_tools.py commit gp-5

.PHONY: consolidation-plan-gp-50 consolidation-apply-gp-50 consolidation-commit-gp-50
consolidation-plan-gp-50:
	python3 scripts/consolidation_tools.py plan gp-50
consolidation-apply-gp-50:
	python3 scripts/consolidation_tools.py apply gp-50
consolidation-commit-gp-50:
	python3 scripts/consolidation_tools.py commit gp-50

.PHONY: consolidation-plan-hx-stomp consolidation-apply-hx-stomp consolidation-commit-hx-stomp
consolidation-plan-hx-stomp:
	python3 scripts/consolidation_tools.py plan hx-stomp
consolidation-apply-hx-stomp:
	python3 scripts/consolidation_tools.py apply hx-stomp
consolidation-commit-hx-stomp:
	python3 scripts/consolidation_tools.py commit hx-stomp

.PHONY: consolidation-plan-tonex-one consolidation-apply-tonex-one consolidation-commit-tonex-one
consolidation-plan-tonex-one:
	python3 scripts/consolidation_tools.py plan tonex-one
consolidation-apply-tonex-one:
	python3 scripts/consolidation_tools.py apply tonex-one
consolidation-commit-tonex-one:
	python3 scripts/consolidation_tools.py commit tonex-one

.PHONY: consolidation-plan-tonex-pedal consolidation-apply-tonex-pedal consolidation-commit-tonex-pedal
consolidation-plan-tonex-pedal:
	python3 scripts/consolidation_tools.py plan tonex-pedal
consolidation-apply-tonex-pedal:
	python3 scripts/consolidation_tools.py apply tonex-pedal
consolidation-commit-tonex-pedal:
	python3 scripts/consolidation_tools.py commit tonex-pedal

.PHONY: consolidation-plan-nano-cortex consolidation-apply-nano-cortex consolidation-commit-nano-cortex
consolidation-plan-nano-cortex:
	python3 scripts/consolidation_tools.py plan nano-cortex
consolidation-apply-nano-cortex:
	python3 scripts/consolidation_tools.py apply nano-cortex
consolidation-commit-nano-cortex:
	python3 scripts/consolidation_tools.py commit nano-cortex

.PHONY: consolidation-plan-ame-100 consolidation-apply-ame-100 consolidation-commit-ame-100
consolidation-plan-ame-100:
	python3 scripts/consolidation_tools.py plan ame-100
consolidation-apply-ame-100:
	python3 scripts/consolidation_tools.py apply ame-100
consolidation-commit-ame-100:
	python3 scripts/consolidation_tools.py commit ame-100

.PHONY: consolidation-plan-ame-200 consolidation-apply-ame-200 consolidation-commit-ame-200
consolidation-plan-ame-200:
	python3 scripts/consolidation_tools.py plan ame-200
consolidation-apply-ame-200:
	python3 scripts/consolidation_tools.py apply ame-200
consolidation-commit-ame-200:
	python3 scripts/consolidation_tools.py commit ame-200

.PHONY: consolidation-plan-ame-200-pro consolidation-apply-ame-200-pro consolidation-commit-ame-200-pro
consolidation-plan-ame-200-pro:
	python3 scripts/consolidation_tools.py plan ame-200-pro
consolidation-apply-ame-200-pro:
	python3 scripts/consolidation_tools.py apply ame-200-pro
consolidation-commit-ame-200-pro:
	python3 scripts/consolidation_tools.py commit ame-200-pro

.PHONY: consolidation-plan-ace-100 consolidation-apply-ace-100 consolidation-commit-ace-100
consolidation-plan-ace-100:
	python3 scripts/consolidation_tools.py plan ace-100
consolidation-apply-ace-100:
	python3 scripts/consolidation_tools.py apply ace-100
consolidation-commit-ace-100:
	python3 scripts/consolidation_tools.py commit ace-100

.PHONY: consolidation-plan-ave-100 consolidation-apply-ave-100 consolidation-commit-ave-100
consolidation-plan-ave-100:
	python3 scripts/consolidation_tools.py plan ave-100
consolidation-apply-ave-100:
	python3 scripts/consolidation_tools.py apply ave-100
consolidation-commit-ave-100:
	python3 scripts/consolidation_tools.py commit ave-100

.PHONY: consolidation-plan-bg300 consolidation-apply-bg300 consolidation-commit-bg300
consolidation-plan-bg300:
	python3 scripts/consolidation_tools.py plan bg300
consolidation-apply-bg300:
	python3 scripts/consolidation_tools.py apply bg300
consolidation-commit-bg300:
	python3 scripts/consolidation_tools.py commit bg300

.PHONY: consolidation-plan-kmf-10 consolidation-apply-kmf-10 consolidation-commit-kmf-10
consolidation-plan-kmf-10:
	python3 scripts/consolidation_tools.py plan kmf-10
consolidation-apply-kmf-10:
	python3 scripts/consolidation_tools.py apply kmf-10
consolidation-commit-kmf-10:
	python3 scripts/consolidation_tools.py commit kmf-10

.PHONY: consolidation-plan-voicelive-play consolidation-apply-voicelive-play consolidation-commit-voicelive-play
consolidation-plan-voicelive-play:
	python3 scripts/consolidation_tools.py plan voicelive-play
consolidation-apply-voicelive-play:
	python3 scripts/consolidation_tools.py apply voicelive-play
consolidation-commit-voicelive-play:
	python3 scripts/consolidation_tools.py commit voicelive-play

.PHONY: consolidation-plan-play-acoustic consolidation-apply-play-acoustic consolidation-commit-play-acoustic
consolidation-plan-play-acoustic:
	python3 scripts/consolidation_tools.py plan play-acoustic
consolidation-apply-play-acoustic:
	python3 scripts/consolidation_tools.py apply play-acoustic
consolidation-commit-play-acoustic:
	python3 scripts/consolidation_tools.py commit play-acoustic

.PHONY: consolidation-plan-h8 consolidation-apply-h8 consolidation-commit-h8
consolidation-plan-h8:
	python3 scripts/consolidation_tools.py plan h8
consolidation-apply-h8:
	python3 scripts/consolidation_tools.py apply h8
consolidation-commit-h8:
	python3 scripts/consolidation_tools.py commit h8

.PHONY: consolidation-plan-fb100 consolidation-apply-fb100 consolidation-commit-fb100
consolidation-plan-fb100:
	python3 scripts/consolidation_tools.py plan fb100
consolidation-apply-fb100:
	python3 scripts/consolidation_tools.py apply fb100
consolidation-commit-fb100:
	python3 scripts/consolidation_tools.py commit fb100

.PHONY: consolidation-plan-gr-55 consolidation-apply-gr-55 consolidation-commit-gr-55
consolidation-plan-gr-55:
	python3 scripts/consolidation_tools.py plan gr-55
consolidation-apply-gr-55:
	python3 scripts/consolidation_tools.py apply gr-55
consolidation-commit-gr-55:
	python3 scripts/consolidation_tools.py commit gr-55

.PHONY: comparison-test-fields
comparison-test-fields:
	python3 scripts/comparison_views.py test-fields

.PHONY: research-commit-field-projection
research-commit-field-projection:
	python3 scripts/research_tools.py commit-field-projection

.PHONY: comparison-test-extraction
comparison-test-extraction:
	python3 scripts/comparison_views.py test-extraction

.PHONY: research-commit-field-extraction
research-commit-field-extraction:
	python3 scripts/research_tools.py commit-field-extraction

.PHONY: research-commit-pe100
research-commit-pe100:
	python3 scripts/research_tools.py commit-pe100

.PHONY: research-commit-g3xn
research-commit-g3xn:
	python3 scripts/research_tools.py commit-g3xn

.PHONY: research-commit-pod-express-guitar-preservation
research-commit-pod-express-guitar-preservation:
	python3 scripts/research_tools.py commit-pod-express-guitar-preservation

.PHONY: research-commit-pod-express-bass-preservation
research-commit-pod-express-bass-preservation:
	python3 scripts/research_tools.py commit-pod-express-bass-preservation

.PHONY: research-commit-g11-preservation
research-commit-g11-preservation:
	python3 scripts/research_tools.py commit-g11-preservation

.PHONY: research-commit-arena-preservation
research-commit-arena-preservation:
	python3 scripts/research_tools.py commit-arena-preservation

.PHONY: research-commit-fx100-preservation
research-commit-fx100-preservation:
	python3 scripts/research_tools.py commit-fx100-preservation

.PHONY: research-commit-fx200-preservation
research-commit-fx200-preservation:
	python3 scripts/research_tools.py commit-fx200-preservation

.PHONY: research-commit-core-preservation
research-commit-core-preservation:
	python3 scripts/research_tools.py commit-core-preservation

.PHONY: research-commit-gembox-preservation
research-commit-gembox-preservation:
	python3 scripts/research_tools.py commit-gembox-preservation

.PHONY: research-commit-gembox-ii-preservation
research-commit-gembox-ii-preservation:
	python3 scripts/research_tools.py commit-gembox-ii-preservation

.PHONY: research-commit-gembox-iii-preservation
research-commit-gembox-iii-preservation:
	python3 scripts/research_tools.py commit-gembox-iii-preservation

.PHONY: research-commit-podgo-preservation
research-commit-podgo-preservation:
	python3 scripts/research_tools.py commit-podgo-preservation

.PHONY: research-commit-podgo-wireless-preservation
research-commit-podgo-wireless-preservation:
	python3 scripts/research_tools.py commit-podgo-wireless-preservation

.PHONY: research-commit-tank-g-preservation
research-commit-tank-g-preservation:
	python3 scripts/research_tools.py commit-tank-g-preservation

.PHONY: research-commit-tank-b-preservation
research-commit-tank-b-preservation:
	python3 scripts/research_tools.py commit-tank-b-preservation

.PHONY: research-commit-tank-mini-preservation
research-commit-tank-mini-preservation:
	python3 scripts/research_tools.py commit-tank-mini-preservation

.PHONY: research-commit-mk20-preservation
research-commit-mk20-preservation:
	python3 scripts/research_tools.py commit-mk20-preservation

.PHONY: research-commit-mk300-preservation
research-commit-mk300-preservation:
	python3 scripts/research_tools.py commit-mk300-preservation

.PHONY: research-commit-tankpro-preservation
research-commit-tankpro-preservation:
	python3 scripts/research_tools.py commit-tankpro-preservation

.PHONY: research-commit-annblackbox-preservation
research-commit-annblackbox-preservation:
	python3 scripts/research_tools.py commit-annblackbox-preservation

.PHONY: research-commit-minix-preservation
research-commit-minix-preservation:
	python3 scripts/research_tools.py commit-minix-preservation

.PHONY: research-commit-pocketamp-preservation
research-commit-pocketamp-preservation:
	python3 scripts/research_tools.py commit-pocketamp-preservation

.PHONY: research-commit-cubebabyac-preservation
research-commit-cubebabyac-preservation:
	python3 scripts/research_tools.py commit-cubebabyac-preservation

.PHONY: research-commit-cubebabybass-preservation
research-commit-cubebabybass-preservation:
	python3 scripts/research_tools.py commit-cubebabybass-preservation

.PHONY: research-commit-mg100-preservation
research-commit-mg100-preservation:
	python3 scripts/research_tools.py commit-mg100-preservation

.PHONY: research-commit-mg200-preservation
research-commit-mg200-preservation:
	python3 scripts/research_tools.py commit-mg200-preservation

.PHONY: research-commit-trident-preservation
research-commit-trident-preservation:
	python3 scripts/research_tools.py commit-trident-preservation

.PHONY: consolidation-audit-findings research-commit-finding-audit
consolidation-audit-findings:
	python3 scripts/consolidation_tools.py audit-findings
research-commit-finding-audit:
	python3 scripts/research_tools.py commit-finding-audit

.PHONY: consolidation-audit-legacy
consolidation-audit-legacy:
	python3 scripts/consolidation_tools.py audit-legacy

.PHONY: research-commit-legacy-audit
research-commit-legacy-audit:
	python3 scripts/research_tools.py commit-legacy-audit

.PHONY: consolidation-audit-compact-gp100
consolidation-audit-compact-gp100:
	python3 scripts/consolidation_tools.py audit-compact GP-100

.PHONY: research-commit-compact-gp100-audit
research-commit-compact-gp100-audit:
	python3 scripts/research_tools.py commit-compact-gp100-audit

.PHONY: consolidation-audit-compact-gp150 research-commit-compact-gp150-audit
consolidation-audit-compact-gp150:
	python3 scripts/consolidation_tools.py audit-compact GP-150
research-commit-compact-gp150-audit:
	python3 scripts/research_tools.py commit-compact-gp150-audit

.PHONY: consolidation-audit-compact-matribox research-commit-compact-matribox-audit
consolidation-audit-compact-matribox:
	python3 scripts/consolidation_tools.py audit-compact Matribox
research-commit-compact-matribox-audit:
	python3 scripts/research_tools.py commit-compact-matribox-audit

.PHONY: consolidation-audit-compact-gp5 research-commit-compact-gp5-audit
consolidation-audit-compact-gp5:
	python3 scripts/consolidation_tools.py audit-compact GP-5
research-commit-compact-gp5-audit:
	python3 scripts/research_tools.py commit-compact-gp5-audit

.PHONY: consolidation-audit-compact-gp50 research-commit-compact-gp50-audit
consolidation-audit-compact-gp50:
	python3 scripts/consolidation_tools.py audit-compact GP-50
research-commit-compact-gp50-audit:
	python3 scripts/research_tools.py commit-compact-gp50-audit

.PHONY: consolidation-audit-compact-gp180 research-commit-compact-gp180-audit
consolidation-audit-compact-gp180:
	python3 scripts/consolidation_tools.py audit-compact GP-180
research-commit-compact-gp180-audit:
	python3 scripts/research_tools.py commit-compact-gp180-audit

.PHONY: consolidation-audit-compact-smartbox research-commit-compact-smartbox-audit
consolidation-audit-compact-smartbox:
	python3 scripts/consolidation_tools.py audit-compact "Smart Box"
research-commit-compact-smartbox-audit:
	python3 scripts/research_tools.py commit-compact-smartbox-audit

.PHONY: consolidation-audit-compact-pocketmaster research-commit-compact-pocketmaster-audit
consolidation-audit-compact-pocketmaster:
	python3 scripts/consolidation_tools.py audit-compact "Pocket Master"
research-commit-compact-pocketmaster-audit:
	python3 scripts/research_tools.py commit-compact-pocketmaster-audit

.PHONY: research-commit-cubebabyelectric-preservation
research-commit-cubebabyelectric-preservation:
	python3 scripts/research_tools.py commit-cubebabyelectric-preservation

.PHONY: consolidation-audit-compact-union research-commit-compact-union
consolidation-audit-compact-union:
	python3 scripts/consolidation_tools.py audit-compact-union
research-commit-compact-union:
	python3 scripts/research_tools.py commit-compact-union

.PHONY: research-commit-floorboard-matribox-ii
research-commit-floorboard-matribox-ii:
	python3 scripts/research_tools.py commit-floorboard-matribox-ii

.PHONY: research-commit-floorboard-matribox-ii-pro
research-commit-floorboard-matribox-ii-pro:
	python3 scripts/research_tools.py commit-floorboard-matribox-ii-pro

.PHONY: consolidation-audit-floorboard-union research-commit-floorboard-union
consolidation-audit-floorboard-union:
	python3 scripts/consolidation_tools.py audit-floorboard-union
research-commit-floorboard-union:
	python3 scripts/research_tools.py commit-floorboard-union

.PHONY: research-commit-g5n
research-commit-g5n:
	python3 scripts/research_tools.py commit-g5n

.PHONY: research-commit-g3n
research-commit-g3n:
	python3 scripts/research_tools.py commit-g3n

.PHONY: research-commit-b3n
research-commit-b3n:
	python3 scripts/research_tools.py commit-b3n

.PHONY: research-commit-a1four
research-commit-a1four:
	python3 scripts/research_tools.py commit-a1four

.PHONY: consolidation-audit-compact-links
consolidation-audit-compact-links:
	python3 scripts/consolidation_tools.py audit-compact-links

.PHONY: consolidation-plan-nux-mg101
consolidation-plan-nux-mg101:
	python3 scripts/consolidation_tools.py plan-nux-mg101

.PHONY: research-commit-nux-mg101-audit
research-commit-nux-mg101-audit:
	python3 scripts/research_tools.py commit-nux-mg101-audit

.PHONY: consolidation-plan-nux-mg300
consolidation-plan-nux-mg300:
	python3 scripts/consolidation_tools.py plan-nux-mg300

.PHONY: research-commit-nux-mg300-audit
research-commit-nux-mg300-audit:
	python3 scripts/research_tools.py commit-nux-mg300-audit

.PHONY: consolidation-plan-nux-mg300mkii
consolidation-plan-nux-mg300mkii:
	python3 scripts/consolidation_tools.py plan-nux-mg300mkii

.PHONY: research-commit-nux-mg300mkii-audit
research-commit-nux-mg300mkii-audit:
	python3 scripts/research_tools.py commit-nux-mg300mkii-audit

.PHONY: consolidation-plan-nux-mg400
consolidation-plan-nux-mg400:
	python3 scripts/consolidation_tools.py plan-nux-mg400

.PHONY: research-commit-nux-mg400-audit
research-commit-nux-mg400-audit:
	python3 scripts/research_tools.py commit-nux-mg400-audit

.PHONY: consolidation-plan-nux-mg30
consolidation-plan-nux-mg30:
	python3 scripts/consolidation_tools.py plan-nux-mg30

.PHONY: research-commit-nux-mg30-audit
research-commit-nux-mg30-audit:
	python3 scripts/research_tools.py commit-nux-mg30-audit

.PHONY: consolidation-plan-nux-mg50li
consolidation-plan-nux-mg50li:
	python3 scripts/consolidation_tools.py plan-nux-mg50li

.PHONY: research-commit-nux-mg50li-audit
research-commit-nux-mg50li-audit:
	python3 scripts/research_tools.py commit-nux-mg50li-audit

.PHONY: consolidation-plan-nux-union consolidation-audit-nux-union
consolidation-plan-nux-union:
	python3 scripts/consolidation_tools.py plan-nux-union
consolidation-audit-nux-union:
	python3 scripts/consolidation_tools.py audit-nux-union

.PHONY: consolidation-audit-nux-links
consolidation-audit-nux-links:
	python3 scripts/consolidation_tools.py audit-nux-links

.PHONY: research-commit-nux-union
research-commit-nux-union:
	python3 scripts/research_tools.py commit-nux-union

.PHONY: consolidation-plan-bass-union consolidation-audit-bass-union consolidation-audit-bass-links
consolidation-plan-bass-union:
	python3 scripts/consolidation_tools.py plan-bass-union
consolidation-audit-bass-union:
	python3 scripts/consolidation_tools.py audit-bass-union
consolidation-audit-bass-links:
	python3 scripts/consolidation_tools.py audit-bass-links

.PHONY: research-commit-bass-union
research-commit-bass-union:
	python3 scripts/research_tools.py commit-bass-union

.PHONY: consolidation-plan-vocal-union consolidation-audit-vocal-union consolidation-audit-vocal-links
consolidation-plan-vocal-union:
	python3 scripts/consolidation_tools.py plan-vocal-union
consolidation-audit-vocal-union:
	python3 scripts/consolidation_tools.py audit-vocal-union
consolidation-audit-vocal-links:
	python3 scripts/consolidation_tools.py audit-vocal-links

.PHONY: research-commit-vocal-union
research-commit-vocal-union:
	python3 scripts/research_tools.py commit-vocal-union

.PHONY: consolidation-plan-advanced-hxe
consolidation-plan-advanced-hxe:
	python3 scripts/consolidation_tools.py plan-advanced-hxe

.PHONY: research-commit-advanced-hxe-audit
research-commit-advanced-hxe-audit:
	python3 scripts/research_tools.py commit-advanced-hxe-audit

.PHONY: consolidation-plan-advanced-flex
consolidation-plan-advanced-flex:
	python3 scripts/consolidation_tools.py plan-advanced-flex

.PHONY: research-commit-advanced-flex-audit
research-commit-advanced-flex-audit:
	python3 scripts/research_tools.py commit-advanced-flex-audit

.PHONY: consolidation-plan-advanced-union consolidation-audit-advanced-union consolidation-audit-advanced-links
consolidation-plan-advanced-union:
	python3 scripts/consolidation_tools.py plan-advanced-union
consolidation-audit-advanced-union:
	python3 scripts/consolidation_tools.py audit-advanced-union
consolidation-audit-advanced-links:
	python3 scripts/consolidation_tools.py audit-advanced-links

.PHONY: research-commit-advanced-union
research-commit-advanced-union:
	python3 scripts/research_tools.py commit-advanced-union

.PHONY: consolidation-plan-boss-union consolidation-audit-boss-union
consolidation-plan-boss-union:
	python3 scripts/consolidation_tools.py plan-boss-union
consolidation-audit-boss-union:
	python3 scripts/consolidation_tools.py audit-boss-union

.PHONY: consolidation-audit-boss-links
consolidation-audit-boss-links:
	python3 scripts/consolidation_tools.py audit-boss-links

.PHONY: research-commit-boss-union
research-commit-boss-union:
	python3 scripts/research_tools.py commit-boss-union

.PHONY: consolidation-plan-boss-history-union consolidation-audit-boss-history-union
consolidation-plan-boss-history-union:
	python3 scripts/consolidation_tools.py plan-boss-history-union
consolidation-audit-boss-history-union:
	python3 scripts/consolidation_tools.py audit-boss-history-union

.PHONY: consolidation-audit-boss-history-links
consolidation-audit-boss-history-links:
	python3 scripts/consolidation_tools.py audit-boss-history-links

.PHONY: research-commit-boss-history-union
research-commit-boss-history-union:
	python3 scripts/research_tools.py commit-boss-history-union

.PHONY: research-commit-ms60b
research-commit-ms60b:
	python3 scripts/research_tools.py commit-ms60b

.PHONY: research-commit-a1xfour
research-commit-a1xfour:
	python3 scripts/research_tools.py commit-a1xfour

.PHONY: research-commit-ms50g
research-commit-ms50g:
	python3 scripts/research_tools.py commit-ms50g

.PHONY: consolidation-plan-audota-union consolidation-audit-audota-union consolidation-audit-audota-links
consolidation-plan-audota-union:
	python3 scripts/consolidation_tools.py plan-audota-union
consolidation-audit-audota-union:
	python3 scripts/consolidation_tools.py audit-audota-union
consolidation-audit-audota-links:
	python3 scripts/consolidation_tools.py audit-audota-links

.PHONY: research-commit-audota-union
research-commit-audota-union:
	python3 scripts/research_tools.py commit-audota-union

.PHONY: consolidation-plan-cube-union consolidation-audit-cube-union consolidation-audit-cube-links
consolidation-plan-cube-union:
	python3 scripts/consolidation_tools.py plan-cube-union
consolidation-audit-cube-union:
	python3 scripts/consolidation_tools.py audit-cube-union
consolidation-audit-cube-links:
	python3 scripts/consolidation_tools.py audit-cube-links

.PHONY: research-commit-cube-union
research-commit-cube-union:
	python3 scripts/research_tools.py commit-cube-union

.PHONY: consolidation-plan-owned-union consolidation-audit-owned-union consolidation-audit-owned-links
consolidation-plan-owned-union:
	python3 scripts/consolidation_tools.py plan-owned-union
consolidation-audit-owned-union:
	python3 scripts/consolidation_tools.py audit-owned-union
consolidation-audit-owned-links:
	python3 scripts/consolidation_tools.py audit-owned-links

.PHONY: research-commit-owned-union
research-commit-owned-union:
	python3 scripts/research_tools.py commit-owned-union

.PHONY: consolidation-plan-market1-union consolidation-audit-market1-union consolidation-audit-market1-links
consolidation-plan-market1-union:
	python3 scripts/consolidation_tools.py plan-market1-union
consolidation-audit-market1-union:
	python3 scripts/consolidation_tools.py audit-market1-union
consolidation-audit-market1-links:
	python3 scripts/consolidation_tools.py audit-market1-links

.PHONY: research-commit-market1-union
research-commit-market1-union:
	python3 scripts/research_tools.py commit-market1-union

.PHONY: consolidation-plan-market2-union consolidation-audit-market2-union consolidation-audit-market2-links
consolidation-plan-market2-union:
	python3 scripts/consolidation_tools.py plan-market2-union
consolidation-audit-market2-union:
	python3 scripts/consolidation_tools.py audit-market2-union
consolidation-audit-market2-links:
	python3 scripts/consolidation_tools.py audit-market2-links

.PHONY: research-commit-market2-union
research-commit-market2-union:
	python3 scripts/research_tools.py commit-market2-union

.PHONY: consolidation-plan-market3-union consolidation-audit-market3-union consolidation-audit-market3-links
consolidation-plan-market3-union:
	python3 scripts/consolidation_tools.py plan-market3-union
consolidation-audit-market3-union:
	python3 scripts/consolidation_tools.py audit-market3-union
consolidation-audit-market3-links:
	python3 scripts/consolidation_tools.py audit-market3-links

.PHONY: research-commit-market3-union
research-commit-market3-union:
	python3 scripts/research_tools.py commit-market3-union

.PHONY: consolidation-plan-market4-union consolidation-audit-market4-union consolidation-audit-market4-links
consolidation-plan-market4-union:
	python3 scripts/consolidation_tools.py plan-market4-union
consolidation-audit-market4-union:
	python3 scripts/consolidation_tools.py audit-market4-union
consolidation-audit-market4-links:
	python3 scripts/consolidation_tools.py audit-market4-links

.PHONY: research-commit-market4-union
research-commit-market4-union:
	python3 scripts/research_tools.py commit-market4-union

.PHONY: consolidation-plan-market5-union consolidation-audit-market5-union consolidation-audit-market5-links
consolidation-plan-market5-union:
	python3 scripts/consolidation_tools.py plan-market5-union
consolidation-audit-market5-union:
	python3 scripts/consolidation_tools.py audit-market5-union
consolidation-audit-market5-links:
	python3 scripts/consolidation_tools.py audit-market5-links

.PHONY: research-commit-market5-union
research-commit-market5-union:
	python3 scripts/research_tools.py commit-market5-union

.PHONY: consolidation-plan-market6-union consolidation-audit-market6-union consolidation-audit-market6-links
consolidation-plan-market6-union:
	python3 scripts/consolidation_tools.py plan-market6-union
consolidation-audit-market6-union:
	python3 scripts/consolidation_tools.py audit-market6-union
consolidation-audit-market6-links:
	python3 scripts/consolidation_tools.py audit-market6-links

.PHONY: research-commit-market6-union
research-commit-market6-union:
	python3 scripts/research_tools.py commit-market6-union

.PHONY: consolidation-plan-market7-union consolidation-audit-market7-union consolidation-audit-market7-links
consolidation-plan-market7-union:
	python3 scripts/consolidation_tools.py plan-market7-union
consolidation-audit-market7-union:
	python3 scripts/consolidation_tools.py audit-market7-union
consolidation-audit-market7-links:
	python3 scripts/consolidation_tools.py audit-market7-links

.PHONY: research-commit-market7-union
research-commit-market7-union:
	python3 scripts/research_tools.py commit-market7-union

.PHONY: metadata-plan metadata-apply metadata-verify metadata-commit
metadata-plan:
	python3 scripts/metadata_consolidation.py plan
metadata-apply:
	python3 scripts/metadata_consolidation.py apply
metadata-verify:
	python3 scripts/metadata_consolidation.py verify
metadata-commit:
	python3 scripts/metadata_consolidation.py commit

.PHONY: metadata-retirement-plan metadata-retirement-apply metadata-retirement-verify metadata-retirement-commit metadata-retirement-rollback-plan metadata-retirement-rollback-apply
metadata-retirement-plan:
	python3 scripts/source_retirement.py plan
metadata-retirement-apply:
	python3 scripts/source_retirement.py apply
metadata-retirement-verify:
	python3 scripts/source_retirement.py verify
metadata-retirement-commit:
	python3 scripts/source_retirement.py commit
metadata-retirement-rollback-plan:
	python3 scripts/source_retirement.py rollback-plan
metadata-retirement-rollback-apply:
	python3 scripts/source_retirement.py rollback-apply

.PHONY: technical-retirement-plan technical-retirement-apply technical-retirement-verify technical-retirement-commit technical-retirement-rollback-plan
technical-retirement-plan:
	python3 scripts/technical_retirement.py plan
technical-retirement-apply:
	python3 scripts/technical_retirement.py apply
technical-retirement-verify:
	python3 scripts/technical_retirement.py verify
technical-retirement-commit:
	python3 scripts/technical_retirement.py commit
technical-retirement-rollback-plan:
	python3 scripts/technical_retirement.py rollback-plan

.PHONY: specialist-retirement-plan specialist-retirement-apply specialist-retirement-verify specialist-retirement-commit
specialist-retirement-plan:
	python3 scripts/technical_retirement.py specialist-plan
specialist-retirement-apply:
	python3 scripts/technical_retirement.py specialist-apply
specialist-retirement-verify:
	python3 scripts/technical_retirement.py specialist-verify
specialist-retirement-commit:
	python3 scripts/technical_retirement.py specialist-commit

.PHONY: json-retirement-plan json-retirement-apply json-retirement-verify json-retirement-commit json-retirement-rollback-plan
json-retirement-plan:
	python3 scripts/source_retirement.py json-plan
json-retirement-apply:
	python3 scripts/source_retirement.py json-apply
json-retirement-verify:
	python3 scripts/source_retirement.py json-verify
json-retirement-commit:
	python3 scripts/source_retirement.py json-commit
json-retirement-rollback-plan:
	python3 scripts/source_retirement.py json-rollback-plan

.PHONY: navigation-audit
navigation-audit:
	python3 scripts/navigation_tools.py

.PHONY: navigation-save navigation-commit
navigation-save:
	python3 scripts/navigation_tools.py save
navigation-commit:
	python3 scripts/navigation_tools.py commit

.PHONY: research-commit-ms70cdr
research-commit-ms70cdr:
	python3 scripts/research_tools.py commit-ms70cdr

.PHONY: research-commit-ms70cdrplus
research-commit-ms70cdrplus:
	python3 scripts/research_tools.py commit-ms70cdrplus
