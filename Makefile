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
