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
	python3 -u scripts/technical_retirement.py verify
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

.PHONY: research-commit-ms60bplus
research-commit-ms60bplus:
	python3 scripts/research_tools.py commit-ms60bplus

.PHONY: research-commit-b1on
research-commit-b1on:
	python3 scripts/research_tools.py commit-b1on

.PHONY: research-commit-me80
research-commit-me80:
	python3 scripts/research_tools.py commit-me80

.PHONY: research-commit-me70
research-commit-me70:
	python3 scripts/research_tools.py commit-me70

.PHONY: research-commit-rp360xp
research-commit-rp360xp:
	python3 scripts/research_tools.py commit-rp360xp

.PHONY: research-commit-me25
research-commit-me25:
	python3 scripts/research_tools.py commit-me25

.PHONY: research-commit-g3
research-commit-g3:
	python3 scripts/research_tools.py commit-g3

.PHONY: research-commit-b3
research-commit-b3:
	python3 scripts/research_tools.py commit-b3

.PHONY: research-commit-vl3x
research-commit-vl3x:
	python3 scripts/research_tools.py commit-vl3x

.PHONY: research-commit-pandora
research-commit-pandora:
	python3 scripts/research_tools.py commit-pandora

.PHONY: research-commit-ax3000g
research-commit-ax3000g:
	python3 scripts/research_tools.py commit-ax3000g

.PHONY: research-commit-b2-followup
research-commit-b2-followup:
	python3 scripts/research_tools.py commit-b2-followup

.PHONY: research-commit-me50
research-commit-me50:
	python3 scripts/research_tools.py commit-me50

.PHONY: research-commit-me20b
research-commit-me20b:
	python3 scripts/research_tools.py commit-me20b

.PHONY: research-commit-gt10
research-commit-gt10:
	python3 scripts/research_tools.py commit-gt10

.PHONY: research-commit-gt8
research-commit-gt8:
	python3 scripts/research_tools.py commit-gt8

.PHONY: research-commit-rp255
research-commit-rp255:
	python3 scripts/research_tools.py commit-rp255

.PHONY: research-commit-ax1500g
research-commit-ax1500g:
	python3 scripts/research_tools.py commit-ax1500g

.PHONY: research-commit-tonelab-le
research-commit-tonelab-le:
	python3 scripts/research_tools.py commit-tonelab-le

.PHONY: research-commit-tonelab-st
research-commit-tonelab-st:
	python3 scripts/research_tools.py commit-tonelab-st

.PHONY: research-commit-tonelab-se
research-commit-tonelab-se:
	python3 scripts/research_tools.py commit-tonelab-se

.PHONY: research-commit-stomplab2b
research-commit-stomplab2b:
	python3 scripts/research_tools.py commit-stomplab2b

.PHONY: research-commit-discovery
research-commit-discovery:
	python3 scripts/research_tools.py commit-discovery

.PHONY: research-commit-perform-v
research-commit-perform-v:
	python3 scripts/research_tools.py commit-perform-v

.PHONY: research-commit-perform-vk
research-commit-perform-vk:
	python3 scripts/research_tools.py commit-perform-vk

.PHONY: research-commit-perform-vg
research-commit-perform-vg:
	python3 scripts/research_tools.py commit-perform-vg

.PHONY: research-commit-stomplab1g
research-commit-stomplab1g:
	python3 scripts/research_tools.py commit-stomplab1g

.PHONY: research-commit-perform-ve
research-commit-perform-ve:
	python3 scripts/research_tools.py commit-perform-ve

.PHONY: research-commit-stomplab2g
research-commit-stomplab2g:
	python3 scripts/research_tools.py commit-stomplab2g

.PHONY: research-commit-g1xon
research-commit-g1xon:
	python3 scripts/research_tools.py commit-g1xon

.PHONY: research-commit-g1on
research-commit-g1on:
	python3 scripts/research_tools.py commit-g1on

.PHONY: research-commit-hd500
research-commit-hd500:
	python3 scripts/research_tools.py commit-hd500

.PHONY: research-commit-dapper-bass
research-commit-dapper-bass:
	python3 scripts/research_tools.py commit-dapper-bass

.PHONY: research-commit-dapper-bass-mini
research-commit-dapper-bass-mini:
	python3 scripts/research_tools.py commit-dapper-bass-mini

.PHONY: research-commit-dapper-mini
research-commit-dapper-mini:
	python3 scripts/research_tools.py commit-dapper-mini

.PHONY: research-commit-dapper-acoustic-mini
research-commit-dapper-acoustic-mini:
	python3 scripts/research_tools.py commit-dapper-acoustic-mini

.PHONY: research-commit-dapper-dark
research-commit-dapper-dark:
	python3 scripts/research_tools.py commit-dapper-dark

.PHONY: research-commit-flyrig5v2
research-commit-flyrig5v2:
	python3 scripts/research_tools.py commit-flyrig5v2

.PHONY: research-commit-blackhammer
research-commit-blackhammer:
	python3 scripts/research_tools.py commit-blackhammer

.PHONY: research-commit-dapper-dark-mini
research-commit-dapper-dark-mini:
	python3 scripts/research_tools.py commit-dapper-dark-mini

.PHONY: research-commit-dapper-indie
research-commit-dapper-indie:
	python3 scripts/research_tools.py commit-dapper-indie

.PHONY: research-commit-rockstage
research-commit-rockstage:
	python3 scripts/research_tools.py commit-rockstage

.PHONY: research-commit-ax5g
research-commit-ax5g:
	python3 scripts/research_tools.py commit-ax5g

.PHONY: research-commit-ving-coverage
research-commit-ving-coverage:
	python3 scripts/research_tools.py commit-ving-coverage

.PHONY: research-commit-505ii
research-commit-505ii:
	python3 scripts/research_tools.py commit-505ii

.PHONY: research-commit-ms50gplus
research-commit-ms50gplus:
	python3 scripts/research_tools.py commit-ms50gplus

.PHONY: research-commit-g5
research-commit-g5:
	python3 scripts/research_tools.py commit-g5

.PHONY: research-commit-g3x
research-commit-g3x:
	python3 scripts/research_tools.py commit-g3x

.PHONY: research-commit-g21u
research-commit-g21u:
	python3 scripts/research_tools.py commit-g21u

.PHONY: research-commit-rp500
research-commit-rp500:
	python3 scripts/research_tools.py commit-rp500

.PHONY: research-commit-ax10g
research-commit-ax10g:
	python3 scripts/research_tools.py commit-ax10g

.PHONY: research-commit-rp90
research-commit-rp90:
	python3 scripts/research_tools.py commit-rp90

.PHONY: research-commit-gfx3
research-commit-gfx3:
	python3 scripts/research_tools.py commit-gfx3

.PHONY: research-commit-gfx5
research-commit-gfx5:
	python3 scripts/research_tools.py commit-gfx5

.PHONY: research-commit-ax1000g
research-commit-ax1000g:
	python3 scripts/research_tools.py commit-ax1000g

.PHONY: research-commit-gfx4
research-commit-gfx4:
	python3 scripts/research_tools.py commit-gfx4

.PHONY: research-commit-ve20-followup
research-commit-ve20-followup:
	python3 scripts/research_tools.py commit-ve20-followup

.PHONY: research-commit-rp250
research-commit-rp250:
	python3 scripts/research_tools.py commit-rp250

.PHONY: research-commit-g71ut
research-commit-g71ut:
	python3 scripts/research_tools.py commit-g71ut

.PHONY: research-commit-me20
research-commit-me20:
	python3 scripts/research_tools.py commit-me20

.PHONY: research-commit-ax3g
research-commit-ax3g:
	python3 scripts/research_tools.py commit-ax3g

.PHONY: research-commit-m5
research-commit-m5:
	python3 scripts/research_tools.py commit-m5

.PHONY: research-commit-m9
research-commit-m9:
	python3 scripts/research_tools.py commit-m9

.PHONY: research-commit-pocketpod
research-commit-pocketpod:
	python3 scripts/research_tools.py commit-pocketpod

.PHONY: research-commit-hxone
research-commit-hxone:
	python3 scripts/research_tools.py commit-hxone

.PHONY: research-commit-gt6
research-commit-gt6:
	python3 scripts/research_tools.py commit-gt6

.PHONY: research-commit-rp1000
research-commit-rp1000:
	python3 scripts/research_tools.py commit-rp1000

.PHONY: research-commit-ve5
research-commit-ve5:
	python3 scripts/research_tools.py commit-ve5

.PHONY: research-commit-pocketgt
research-commit-pocketgt:
	python3 scripts/research_tools.py commit-pocketgt

.PHONY: research-commit-gigboard
research-commit-gigboard:
	python3 scripts/research_tools.py commit-gigboard

.PHONY: research-commit-pedalboard
research-commit-pedalboard:
	python3 scripts/research_tools.py commit-pedalboard

.PHONY: research-commit-vx5
research-commit-vx5:
	python3 scripts/research_tools.py commit-vx5

.PHONY: research-commit-helixfloor
research-commit-helixfloor:
	python3 scripts/research_tools.py commit-helixfloor

.PHONY: research-commit-stadiumxl
research-commit-stadiumxl:
	python3 scripts/research_tools.py commit-stadiumxl

.PHONY: research-commit-hd500x
research-commit-hd500x:
	python3 scripts/research_tools.py commit-hd500x

.PHONY: research-commit-amplifi-fx100
research-commit-amplifi-fx100:
	python3 scripts/research_tools.py commit-amplifi-fx100

.PHONY: research-commit-bass-vamp
research-commit-bass-vamp:
	python3 scripts/research_tools.py commit-bass-vamp

.PHONY: research-commit-bass-vamp-pro
research-commit-bass-vamp-pro:
	python3 scripts/research_tools.py commit-bass-vamp-pro

.PHONY: research-commit-vamp2
research-commit-vamp2:
	python3 scripts/research_tools.py commit-vamp2

.PHONY: research-commit-rp155
research-commit-rp155:
	python3 scripts/research_tools.py commit-rp155

.PHONY: research-commit-ax30g
research-commit-ax30g:
	python3 scripts/research_tools.py commit-ax30g

.PHONY: research-commit-707ii
research-commit-707ii:
	python3 scripts/research_tools.py commit-707ii

.PHONY: research-commit-708ii
research-commit-708ii:
	python3 scripts/research_tools.py commit-708ii

.PHONY: research-commit-mic-mechanic2
research-commit-mic-mechanic2:
	python3 scripts/research_tools.py commit-mic-mechanic2

.PHONY: research-commit-duplicator
research-commit-duplicator:
	python3 scripts/research_tools.py commit-duplicator

.PHONY: research-commit-harmony-singer2
research-commit-harmony-singer2:
	python3 scripts/research_tools.py commit-harmony-singer2

.PHONY: research-commit-x3live
research-commit-x3live:
	python3 scripts/research_tools.py commit-x3live

.PHONY: research-commit-xtlive
research-commit-xtlive:
	python3 scripts/research_tools.py commit-xtlive

.PHONY: research-commit-hd400
research-commit-hd400:
	python3 scripts/research_tools.py commit-hd400

.PHONY: research-commit-readme-counts
research-commit-readme-counts:
	python3 scripts/research_tools.py commit-readme-counts

.PHONY: research-commit-fv02
research-commit-fv02:
	python3 scripts/research_tools.py commit-fv02

.PHONY: research-commit-fb200
research-commit-fb200:
	python3 scripts/research_tools.py commit-fb200

.PHONY: research-commit-fv03
research-commit-fv03:
	python3 scripts/research_tools.py commit-fv03

.PHONY: research-commit-fv04
research-commit-fv04:
	python3 scripts/research_tools.py commit-fv04

.PHONY: research-commit-fg200
research-commit-fg200:
	python3 scripts/research_tools.py commit-fg200

.PHONY: research-commit-fx50
research-commit-fx50:
	python3 scripts/research_tools.py commit-fx50

.PHONY: research-commit-r16
research-commit-r16:
	python3 scripts/research_tools.py commit-r16

.PHONY: research-commit-b1xfour-followup
research-commit-b1xfour-followup:
	python3 scripts/research_tools.py commit-b1xfour-followup

.PHONY: research-commit-b1four-followup
research-commit-b1four-followup:
	python3 scripts/research_tools.py commit-b1four-followup

.PHONY: research-commit-gnx3
research-commit-gnx3:
	python3 scripts/research_tools.py commit-gnx3

.PHONY: research-commit-mx200
research-commit-mx200:
	python3 scripts/research_tools.py commit-mx200

.PHONY: research-commit-fx2000
research-commit-fx2000:
	python3 scripts/research_tools.py commit-fx2000

.PHONY: research-commit-microverb4
research-commit-microverb4:
	python3 scripts/research_tools.py commit-microverb4

.PHONY: research-commit-midiverb4
research-commit-midiverb4:
	python3 scripts/research_tools.py commit-midiverb4

.PHONY: research-commit-spx900
research-commit-spx900:
	python3 scripts/research_tools.py commit-spx900

.PHONY: research-commit-spx990
research-commit-spx990:
	python3 scripts/research_tools.py commit-spx990

.PHONY: research-commit-rfx1100
research-commit-rfx1100:
	python3 scripts/research_tools.py commit-rfx1100

.PHONY: research-commit-b21u
research-commit-b21u:
	python3 scripts/research_tools.py commit-b21u

.PHONY: research-commit-criticalmass
research-commit-criticalmass:
	python3 scripts/research_tools.py commit-criticalmass

.PHONY: research-commit-hxe-price
research-commit-hxe-price:
	python3 scripts/research_tools.py commit-hxe-price

.PHONY: research-commit-m100
research-commit-m100:
	python3 scripts/research_tools.py commit-m100

.PHONY: research-commit-mg20
research-commit-mg20:
	python3 scripts/research_tools.py commit-mg20

.PHONY: research-commit-microplus
research-commit-microplus:
	python3 scripts/research_tools.py commit-microplus

.PHONY: research-commit-katana-go
research-commit-katana-go:
	python3 scripts/research_tools.py commit-katana-go

.PHONY: research-commit-ampero-one
research-commit-ampero-one:
	python3 scripts/research_tools.py commit-ampero-one

.PHONY: research-commit-vt4
research-commit-vt4:
	python3 scripts/research_tools.py commit-vt4

.PHONY: research-commit-1201
research-commit-1201:
	python3 scripts/research_tools.py commit-1201

.PHONY: research-commit-h9max
research-commit-h9max:
	python3 scripts/research_tools.py commit-h9max

.PHONY: consolidation-audit-body-differences
consolidation-audit-body-differences:
	python3 scripts/consolidation_tools.py audit-body-differences

.PHONY: consolidation-compact-reference-plan
consolidation-compact-reference-plan:
	python3 scripts/consolidation_tools.py compact-reference-plan

.PHONY: consolidation-commit-preservation-repairs
consolidation-commit-preservation-repairs:
	python3 scripts/consolidation_tools.py commit-preservation-repairs

.PHONY: research-commit-fm3
research-commit-fm3:
	python3 scripts/research_tools.py commit-fm3

.PHONY: research-commit-player
research-commit-player:
	python3 scripts/research_tools.py commit-player

.PHONY: research-commit-quad
research-commit-quad:
	python3 scripts/research_tools.py commit-quad

.PHONY: research-commit-v6-live
research-commit-v6-live:
	python3 scripts/research_tools.py commit-v6-live

.PHONY: research-commit-play-qsg
research-commit-play-qsg:
	python3 scripts/research_tools.py commit-play-qsg

.PHONY: research-commit-g1-original
research-commit-g1-original:
	python3 scripts/research_tools.py commit-g1-original

.PHONY: research-commit-prime-p2
research-commit-prime-p2:
	python3 scripts/research_tools.py commit-prime-p2

.PHONY: research-commit-prime-m1
research-commit-prime-m1:
	python3 scripts/research_tools.py commit-prime-m1

.PHONY: research-commit-prime-m2
research-commit-prime-m2:
	python3 scripts/research_tools.py commit-prime-m2

.PHONY: research-commit-stageman
research-commit-stageman:
	python3 scripts/research_tools.py commit-stageman

.PHONY: research-commit-fv05
research-commit-fv05:
	python3 scripts/research_tools.py commit-fv05

.PHONY: research-commit-b2-conversion
research-commit-b2-conversion:
	python3 scripts/research_tools.py commit-b2-conversion

.PHONY: research-commit-aas
research-commit-aas:
	python3 scripts/research_tools.py commit-aas

.PHONY: research-commit-ax10b
research-commit-ax10b:
	python3 scripts/research_tools.py commit-ax10b

.PHONY: research-commit-ve1
research-commit-ve1:
	python3 scripts/research_tools.py commit-ve1

.PHONY: research-commit-ve22
research-commit-ve22:
	python3 scripts/research_tools.py commit-ve22

.PHONY: research-commit-ms80ir
research-commit-ms80ir:
	python3 scripts/research_tools.py commit-ms80ir

.PHONY: research-commit-spx2000
research-commit-spx2000:
	python3 scripts/research_tools.py commit-spx2000

.PHONY: research-commit-floorpodplus
research-commit-floorpodplus:
	python3 scripts/research_tools.py commit-floorpodplus

.PHONY: research-commit-gt10b
research-commit-gt10b:
	python3 scripts/research_tools.py commit-gt10b

.PHONY: research-commit-vlt2
research-commit-vlt2:
	python3 scripts/research_tools.py commit-vlt2

.PHONY: research-commit-fx600
research-commit-fx600:
	python3 scripts/research_tools.py commit-fx600

.PHONY: research-commit-gorigb
research-commit-gorigb:
	python3 scripts/research_tools.py commit-gorigb

.PHONY: research-commit-tinystomp
research-commit-tinystomp:
	python3 scripts/research_tools.py commit-tinystomp

.PHONY: research-commit-dualstomp
research-commit-dualstomp:
	python3 scripts/research_tools.py commit-dualstomp

.PHONY: research-commit-dualstomplite
research-commit-dualstomplite:
	python3 scripts/research_tools.py commit-dualstomplite

.PHONY: research-commit-gorig2
research-commit-gorig2:
	python3 scripts/research_tools.py commit-gorig2

.PHONY: research-commit-me90b-control
research-commit-me90b-control:
	python3 scripts/research_tools.py commit-me90b-control

.PHONY: research-commit-sol918
research-commit-sol918:
	python3 scripts/research_tools.py commit-sol918

.PHONY: research-commit-tc1
research-commit-tc1:
	python3 scripts/research_tools.py commit-tc1

.PHONY: research-commit-tc2
research-commit-tc2:
	python3 scripts/research_tools.py commit-tc2

.PHONY: research-commit-v3compat
research-commit-v3compat:
	python3 scripts/research_tools.py commit-v3compat

.PHONY: research-commit-rd5
research-commit-rd5:
	python3 scripts/research_tools.py commit-rd5

.PHONY: research-commit-ms3
research-commit-ms3:
	python3 scripts/research_tools.py commit-ms3

.PHONY: research-commit-rc5
research-commit-rc5:
	python3 scripts/research_tools.py commit-rc5

.PHONY: research-commit-dc5
research-commit-dc5:
	python3 scripts/research_tools.py commit-dc5

.PHONY: research-commit-fx20
research-commit-fx20:
	python3 scripts/research_tools.py commit-fx20

.PHONY: research-commit-fx150b
research-commit-fx150b:
	python3 scripts/research_tools.py commit-fx150b

.PHONY: research-commit-pockrock
research-commit-pockrock:
	python3 scripts/research_tools.py commit-pockrock

.PHONY: research-commit-blacktruck
research-commit-blacktruck:
	python3 scripts/research_tools.py commit-blacktruck

.PHONY: research-commit-prime-s1
research-commit-prime-s1:
	python3 scripts/research_tools.py commit-prime-s1

.PHONY: research-commit-anagram
research-commit-anagram:
	python3 scripts/research_tools.py commit-anagram

.PHONY: research-commit-mfx10
research-commit-mfx10:
	python3 scripts/research_tools.py commit-mfx10

.PHONY: canonical-links-plan canonical-links-apply canonical-links-verify
canonical-links-plan:
	python3 scripts/canonical_links.py plan
canonical-links-apply:
	python3 scripts/canonical_links.py apply
canonical-links-verify:
	python3 scripts/canonical_links.py verify

.PHONY: canonical-links-test
canonical-links-test:
	python3 scripts/canonical_links.py test

.PHONY: canonical-links-plan-boss canonical-links-plan-mooer
canonical-links-plan-boss:
	python3 scripts/canonical_links.py plan-boss
canonical-links-plan-mooer:
	python3 scripts/canonical_links.py plan-mooer

.PHONY: canonical-links-plan-valeton canonical-links-plan-zoom canonical-links-plan-mvave
canonical-links-plan-valeton:
	python3 scripts/canonical_links.py plan-valeton
canonical-links-plan-zoom:
	python3 scripts/canonical_links.py plan-zoom
canonical-links-plan-mvave:
	python3 scripts/canonical_links.py plan-mvave

.PHONY: canonical-links-plan-remaining canonical-links-apply-remaining
canonical-links-plan-remaining:
	python3 scripts/canonical_links.py plan-remaining
canonical-links-apply-remaining:
	python3 scripts/canonical_links.py apply-remaining

.PHONY: research-commit-gp200x
research-commit-gp200x:
	python3 scripts/research_tools.py commit-gp200x

.PHONY: research-commit-rp200
research-commit-rp200:
	python3 scripts/research_tools.py commit-rp200

.PHONY: research-commit-me50b
research-commit-me50b:
	python3 scripts/research_tools.py commit-me50b

.PHONY: research-commit-g2four-market
research-commit-g2four-market:
	python3 scripts/research_tools.py commit-g2four-market

.PHONY: research-commit-ad10
research-commit-ad10:
	python3 scripts/research_tools.py commit-ad10

.PHONY: research-commit-rp70
research-commit-rp70:
	python3 scripts/research_tools.py commit-rp70

.PHONY: research-commit-me30
research-commit-me30:
	python3 scripts/research_tools.py commit-me30

.PHONY: research-commit-vamp3
research-commit-vamp3:
	python3 scripts/research_tools.py commit-vamp3

.PHONY: research-commit-ax100g
research-commit-ax100g:
	python3 scripts/research_tools.py commit-ax100g

.PHONY: research-commit-g1four-market
research-commit-g1four-market:
	python3 scripts/research_tools.py commit-g1four-market

.PHONY: research-commit-g1xfour-followup
research-commit-g1xfour-followup:
	python3 scripts/research_tools.py commit-g1xfour-followup

.PHONY: research-commit-gnx4
research-commit-gnx4:
	python3 scripts/research_tools.py commit-gnx4

.PHONY: research-commit-b1x-original
research-commit-b1x-original:
	python3 scripts/research_tools.py commit-b1x-original

.PHONY: research-commit-505-original
research-commit-505-original:
	python3 scripts/research_tools.py commit-505-original

.PHONY: research-ledger-history
research-ledger-history:
	python3 scripts/ledger_history.py

.PHONY: research-commit-rh101
research-commit-rh101:
	python3 scripts/research_tools.py commit-rh101

.PHONY: research-commit-rh100
research-commit-rh100:
	python3 scripts/research_tools.py commit-rh100

.PHONY: research-commit-cerberus
research-commit-cerberus:
	python3 scripts/research_tools.py commit-cerberus

.PHONY: research-commit-mx400
research-commit-mx400:
	python3 scripts/research_tools.py commit-mx400

.PHONY: research-commit-ame100
research-commit-ame100:
	python3 scripts/research_tools.py commit-ame100

.PHONY: json-pointer-removal-plan json-pointer-removal-apply json-pointer-removal-verify json-pointer-removal-commit json-pointer-rollback-plan
json-pointer-removal-plan:
	python3 scripts/json_pointer_removal.py plan
json-pointer-removal-apply:
	python3 scripts/json_pointer_removal.py apply
json-pointer-removal-verify:
	python3 scripts/json_pointer_removal.py verify
json-pointer-removal-commit:
	python3 scripts/json_pointer_removal.py commit
json-pointer-rollback-plan:
	python3 scripts/json_pointer_removal.py rollback-plan

.PHONY: research-commit-rev500
research-commit-rev500:
	python3 scripts/research_tools.py commit-rev500

.PHONY: research-commit-dsp2024p
research-commit-dsp2024p:
	python3 scripts/research_tools.py commit-dsp2024p

.PHONY: research-commit-ie550
research-commit-ie550:
	python3 scripts/research_tools.py commit-ie550

.PHONY: comparison-test-counts
comparison-test-counts:
	python3 scripts/comparison_views.py test-counts

.PHONY: research-commit-blackstar
research-commit-blackstar:
	python3 scripts/blackstar_catalogue.py commit

.PHONY: research-commit-lekato
research-commit-lekato:
	python3 scripts/lekato_catalogue.py commit

.PHONY: research-commit-keeley
research-commit-keeley:
	python3 scripts/keeley_catalogue.py commit

.PHONY: research-commit-demonfx
research-commit-demonfx:
	python3 scripts/demonfx_catalogue.py commit

.PHONY: research-commit-rowin
research-commit-rowin:
	python3 scripts/rowin_catalogue.py commit

.PHONY: research-commit-erok
research-commit-erok:
	python3 scripts/erok_catalogue.py commit

.PHONY: research-commit-tech21
research-commit-tech21:
	python3 scripts/tech21_catalogue.py commit

.PHONY: research-gaps-plan research-gaps-apply research-gaps-commit
research-gaps-plan:
	python3 scripts/research_gaps.py plan
research-gaps-apply:
	python3 scripts/research_gaps.py apply
research-gaps-commit:
	python3 scripts/research_gaps.py commit

.PHONY: research-commit-yamaha
research-commit-yamaha:
	python3 scripts/yamaha_catalogue.py commit

.PHONY: research-gaps-test
research-gaps-test:
	python3 scripts/research_gaps.py test

.PHONY: research-commit-digitech
research-commit-digitech:
	python3 scripts/digitech_catalogue.py commit

.PHONY: research-commit-levitate
research-commit-levitate:
	python3 scripts/research_tools.py commit-levitate

.PHONY: research-commit-bfactory
research-commit-bfactory:
	python3 scripts/research_tools.py commit-bfactory

.PHONY: research-commit-pg2
research-commit-pg2:
	python3 scripts/research_tools.py commit-pg2

.PHONY: research-commit-m350
research-commit-m350:
	python3 scripts/research_tools.py commit-m350

.PHONY: research-commit-harley-benton
research-commit-harley-benton:
	python3 scripts/harley_benton_catalogue.py commit

.PHONY: research-commit-boss
research-commit-boss:
	python3 scripts/boss_catalogue.py commit

.PHONY: research-commit-zoom
research-commit-zoom:
	python3 scripts/zoom_catalogue.py commit

.PHONY: research-commit-mooer
research-commit-mooer:
	python3 scripts/mooer_catalogue.py commit

.PHONY: research-commit-hotone
research-commit-hotone:
	python3 scripts/hotone_catalogue.py commit

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

.PHONY: research-push-plan research-push-apply
research-push-plan:
	python3 scripts/research_push.py plan
research-push-apply:
	python3 scripts/research_push.py apply

.PHONY: research-push-inspect research-push-sync
research-push-inspect:
	python3 scripts/research_push.py inspect
research-push-sync:
	python3 scripts/research_push.py sync

.PHONY: research-push-finalize
research-push-finalize:
	python3 scripts/research_push.py finalize

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

.PHONY: brand-sort-sync brand-sort-plan brand-sort-apply brand-sort-verify brand-sort-commit
brand-sort-sync:
	python3 scripts/brand_sort.py sync
brand-sort-plan:
	python3 scripts/brand_sort.py plan
brand-sort-apply:
	python3 scripts/brand_sort.py apply
brand-sort-verify:
	python3 scripts/brand_sort.py verify
brand-sort-commit:
	python3 scripts/brand_sort.py commit

.PHONY: brand-sort-test
brand-sort-test:
	python3 scripts/brand_sort.py test
