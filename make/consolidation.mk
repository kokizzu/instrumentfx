# Existing consolidation command API; preserve target names and recipes.

.PHONY: consolidation-plan-g6
consolidation-plan-g6:
	python3 scripts/consolidation_tools.py plan g6

.PHONY: consolidation-apply-g6
consolidation-apply-g6:
	python3 scripts/consolidation_tools.py apply g6

.PHONY: consolidation-commit-g6
consolidation-commit-g6:
	python3 scripts/consolidation_tools.py commit g6

.PHONY: consolidation-plan-g1-four
consolidation-plan-g1-four:
	python3 scripts/consolidation_tools.py plan g1-four

.PHONY: consolidation-apply-g1-four
consolidation-apply-g1-four:
	python3 scripts/consolidation_tools.py apply g1-four

.PHONY: consolidation-commit-g1-four
consolidation-commit-g1-four:
	python3 scripts/consolidation_tools.py commit g1-four

.PHONY: consolidation-plan-g1x-four
consolidation-plan-g1x-four:
	python3 scripts/consolidation_tools.py plan g1x-four

.PHONY: consolidation-apply-g1x-four
consolidation-apply-g1x-four:
	python3 scripts/consolidation_tools.py apply g1x-four

.PHONY: consolidation-commit-g1x-four
consolidation-commit-g1x-four:
	python3 scripts/consolidation_tools.py commit g1x-four

.PHONY: consolidation-verify
consolidation-verify:
	python3 scripts/consolidation_tools.py verify

.PHONY: consolidation-clean-cache-plan
consolidation-clean-cache-plan:
	python3 scripts/consolidation_tools.py cache-plan

.PHONY: consolidation-clean-cache-apply
consolidation-clean-cache-apply:
	python3 scripts/consolidation_tools.py cache-apply

.PHONY: consolidation-plan-g2-four
consolidation-plan-g2-four:
	python3 scripts/consolidation_tools.py plan g2-four

.PHONY: consolidation-apply-g2-four
consolidation-apply-g2-four:
	python3 scripts/consolidation_tools.py apply g2-four

.PHONY: consolidation-commit-g2-four
consolidation-commit-g2-four:
	python3 scripts/consolidation_tools.py commit g2-four

.PHONY: consolidation-plan-g2x-four
consolidation-plan-g2x-four:
	python3 scripts/consolidation_tools.py plan g2x-four

.PHONY: consolidation-apply-g2x-four
consolidation-apply-g2x-four:
	python3 scripts/consolidation_tools.py apply g2x-four

.PHONY: consolidation-commit-g2x-four
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

.PHONY: consolidation-plan-hx-stomp-xl
consolidation-plan-hx-stomp-xl:
	python3 scripts/consolidation_tools.py plan hx-stomp-xl

.PHONY: consolidation-apply-hx-stomp-xl
consolidation-apply-hx-stomp-xl:
	python3 scripts/consolidation_tools.py apply hx-stomp-xl

.PHONY: consolidation-commit-hx-stomp-xl
consolidation-commit-hx-stomp-xl:
	python3 scripts/consolidation_tools.py commit hx-stomp-xl

.PHONY: consolidation-plan-ampero-mini
consolidation-plan-ampero-mini:
	python3 scripts/consolidation_tools.py plan ampero-mini

.PHONY: consolidation-apply-ampero-mini
consolidation-apply-ampero-mini:
	python3 scripts/consolidation_tools.py apply ampero-mini

.PHONY: consolidation-commit-ampero-mini
consolidation-commit-ampero-mini:
	python3 scripts/consolidation_tools.py commit ampero-mini

.PHONY: consolidation-plan-ampero-mp100
consolidation-plan-ampero-mp100:
	python3 scripts/consolidation_tools.py plan ampero-mp100

.PHONY: consolidation-apply-ampero-mp100
consolidation-apply-ampero-mp100:
	python3 scripts/consolidation_tools.py apply ampero-mp100

.PHONY: consolidation-commit-ampero-mp100
consolidation-commit-ampero-mp100:
	python3 scripts/consolidation_tools.py commit ampero-mp100

.PHONY: consolidation-plan-ampero-mp350
consolidation-plan-ampero-mp350:
	python3 scripts/consolidation_tools.py plan ampero-mp350

.PHONY: consolidation-apply-ampero-mp350
consolidation-apply-ampero-mp350:
	python3 scripts/consolidation_tools.py apply ampero-mp350

.PHONY: consolidation-commit-ampero-mp350
consolidation-commit-ampero-mp350:
	python3 scripts/consolidation_tools.py commit ampero-mp350

.PHONY: consolidation-plan-ampero-mp380
consolidation-plan-ampero-mp380:
	python3 scripts/consolidation_tools.py plan ampero-mp380

.PHONY: consolidation-apply-ampero-mp380
consolidation-apply-ampero-mp380:
	python3 scripts/consolidation_tools.py apply ampero-mp380

.PHONY: consolidation-commit-ampero-mp380
consolidation-commit-ampero-mp380:
	python3 scripts/consolidation_tools.py commit ampero-mp380

.PHONY: consolidation-plan-ampero-mp300
consolidation-plan-ampero-mp300:
	python3 scripts/consolidation_tools.py plan ampero-mp300

.PHONY: consolidation-apply-ampero-mp300
consolidation-apply-ampero-mp300:
	python3 scripts/consolidation_tools.py apply ampero-mp300

.PHONY: consolidation-commit-ampero-mp300
consolidation-commit-ampero-mp300:
	python3 scripts/consolidation_tools.py commit ampero-mp300

.PHONY: consolidation-plan-ge100-original
consolidation-plan-ge100-original:
	python3 scripts/consolidation_tools.py plan ge100-original

.PHONY: consolidation-apply-ge100-original
consolidation-apply-ge100-original:
	python3 scripts/consolidation_tools.py apply ge100-original

.PHONY: consolidation-commit-ge100-original
consolidation-commit-ge100-original:
	python3 scripts/consolidation_tools.py commit ge100-original

.PHONY: consolidation-plan-ge150-original
consolidation-plan-ge150-original:
	python3 scripts/consolidation_tools.py plan ge150-original

.PHONY: consolidation-apply-ge150-original
consolidation-apply-ge150-original:
	python3 scripts/consolidation_tools.py apply ge150-original

.PHONY: consolidation-commit-ge150-original
consolidation-commit-ge150-original:
	python3 scripts/consolidation_tools.py commit ge150-original

.PHONY: consolidation-plan-ge200-original
consolidation-plan-ge200-original:
	python3 scripts/consolidation_tools.py plan ge200-original

.PHONY: consolidation-apply-ge200-original
consolidation-apply-ge200-original:
	python3 scripts/consolidation_tools.py apply ge200-original

.PHONY: consolidation-commit-ge200-original
consolidation-commit-ge200-original:
	python3 scripts/consolidation_tools.py commit ge200-original

.PHONY: consolidation-plan-ge150-pro-li
consolidation-plan-ge150-pro-li:
	python3 scripts/consolidation_tools.py plan ge150-pro-li

.PHONY: consolidation-apply-ge150-pro-li
consolidation-apply-ge150-pro-li:
	python3 scripts/consolidation_tools.py apply ge150-pro-li

.PHONY: consolidation-commit-ge150-pro-li
consolidation-commit-ge150-pro-li:
	python3 scripts/consolidation_tools.py commit ge150-pro-li

.PHONY: consolidation-plan-ge100-pro
consolidation-plan-ge100-pro:
	python3 scripts/consolidation_tools.py plan ge100-pro

.PHONY: consolidation-apply-ge100-pro
consolidation-apply-ge100-pro:
	python3 scripts/consolidation_tools.py apply ge100-pro

.PHONY: consolidation-commit-ge100-pro
consolidation-commit-ge100-pro:
	python3 scripts/consolidation_tools.py commit ge100-pro

.PHONY: consolidation-plan-ge100-pro-li
consolidation-plan-ge100-pro-li:
	python3 scripts/consolidation_tools.py plan ge100-pro-li

.PHONY: consolidation-apply-ge100-pro-li
consolidation-apply-ge100-pro-li:
	python3 scripts/consolidation_tools.py apply ge100-pro-li

.PHONY: consolidation-commit-ge100-pro-li
consolidation-commit-ge100-pro-li:
	python3 scripts/consolidation_tools.py commit ge100-pro-li

.PHONY: consolidation-plan-ge200-pro
consolidation-plan-ge200-pro:
	python3 scripts/consolidation_tools.py plan ge200-pro

.PHONY: consolidation-apply-ge200-pro
consolidation-apply-ge200-pro:
	python3 scripts/consolidation_tools.py apply ge200-pro

.PHONY: consolidation-commit-ge200-pro
consolidation-commit-ge200-pro:
	python3 scripts/consolidation_tools.py commit ge200-pro

.PHONY: consolidation-plan-ge200-pro-li
consolidation-plan-ge200-pro-li:
	python3 scripts/consolidation_tools.py plan ge200-pro-li

.PHONY: consolidation-apply-ge200-pro-li
consolidation-apply-ge200-pro-li:
	python3 scripts/consolidation_tools.py apply ge200-pro-li

.PHONY: consolidation-commit-ge200-pro-li
consolidation-commit-ge200-pro-li:
	python3 scripts/consolidation_tools.py commit ge200-pro-li

.PHONY: consolidation-plan-ge150-pro
consolidation-plan-ge150-pro:
	python3 scripts/consolidation_tools.py plan ge150-pro

.PHONY: consolidation-apply-ge150-pro
consolidation-apply-ge150-pro:
	python3 scripts/consolidation_tools.py apply ge150-pro

.PHONY: consolidation-commit-ge150-pro
consolidation-commit-ge150-pro:
	python3 scripts/consolidation_tools.py commit ge150-pro

.PHONY: consolidation-plan-ge150-plus
consolidation-plan-ge150-plus:
	python3 scripts/consolidation_tools.py plan ge150-plus

.PHONY: consolidation-apply-ge150-plus
consolidation-apply-ge150-plus:
	python3 scripts/consolidation_tools.py apply ge150-plus

.PHONY: consolidation-commit-ge150-plus
consolidation-commit-ge150-plus:
	python3 scripts/consolidation_tools.py commit ge150-plus

.PHONY: consolidation-plan-ge150-plus-li
consolidation-plan-ge150-plus-li:
	python3 scripts/consolidation_tools.py plan ge150-plus-li

.PHONY: consolidation-apply-ge150-plus-li
consolidation-apply-ge150-plus-li:
	python3 scripts/consolidation_tools.py apply ge150-plus-li

.PHONY: consolidation-commit-ge150-plus-li
consolidation-commit-ge150-plus-li:
	python3 scripts/consolidation_tools.py commit ge150-plus-li

.PHONY: consolidation-plan-ge150-max
consolidation-plan-ge150-max:
	python3 scripts/consolidation_tools.py plan ge150-max

.PHONY: consolidation-apply-ge150-max
consolidation-apply-ge150-max:
	python3 scripts/consolidation_tools.py apply ge150-max

.PHONY: consolidation-commit-ge150-max
consolidation-commit-ge150-max:
	python3 scripts/consolidation_tools.py commit ge150-max

.PHONY: consolidation-plan-ge150-max-li
consolidation-plan-ge150-max-li:
	python3 scripts/consolidation_tools.py plan ge150-max-li

.PHONY: consolidation-apply-ge150-max-li
consolidation-apply-ge150-max-li:
	python3 scripts/consolidation_tools.py apply ge150-max-li

.PHONY: consolidation-commit-ge150-max-li
consolidation-commit-ge150-max-li:
	python3 scripts/consolidation_tools.py commit ge150-max-li

.PHONY: consolidation-plan-ge1000
consolidation-plan-ge1000:
	python3 scripts/consolidation_tools.py plan ge1000

.PHONY: consolidation-apply-ge1000
consolidation-apply-ge1000:
	python3 scripts/consolidation_tools.py apply ge1000

.PHONY: consolidation-commit-ge1000
consolidation-commit-ge1000:
	python3 scripts/consolidation_tools.py commit ge1000

.PHONY: consolidation-plan-ge1000-li
consolidation-plan-ge1000-li:
	python3 scripts/consolidation_tools.py plan ge1000-li

.PHONY: consolidation-apply-ge1000-li
consolidation-apply-ge1000-li:
	python3 scripts/consolidation_tools.py apply ge1000-li

.PHONY: consolidation-commit-ge1000-li
consolidation-commit-ge1000-li:
	python3 scripts/consolidation_tools.py commit ge1000-li

.PHONY: consolidation-plan-gp-100
consolidation-plan-gp-100:
	python3 scripts/consolidation_tools.py plan gp-100

.PHONY: consolidation-apply-gp-100
consolidation-apply-gp-100:
	python3 scripts/consolidation_tools.py apply gp-100

.PHONY: consolidation-commit-gp-100
consolidation-commit-gp-100:
	python3 scripts/consolidation_tools.py commit gp-100

.PHONY: consolidation-plan-gp-150
consolidation-plan-gp-150:
	python3 scripts/consolidation_tools.py plan gp-150

.PHONY: consolidation-apply-gp-150
consolidation-apply-gp-150:
	python3 scripts/consolidation_tools.py apply gp-150

.PHONY: consolidation-commit-gp-150
consolidation-commit-gp-150:
	python3 scripts/consolidation_tools.py commit gp-150

.PHONY: consolidation-plan-gp-200
consolidation-plan-gp-200:
	python3 scripts/consolidation_tools.py plan gp-200

.PHONY: consolidation-apply-gp-200
consolidation-apply-gp-200:
	python3 scripts/consolidation_tools.py apply gp-200

.PHONY: consolidation-commit-gp-200
consolidation-commit-gp-200:
	python3 scripts/consolidation_tools.py commit gp-200

.PHONY: consolidation-plan-gp-180
consolidation-plan-gp-180:
	python3 scripts/consolidation_tools.py plan gp-180

.PHONY: consolidation-apply-gp-180
consolidation-apply-gp-180:
	python3 scripts/consolidation_tools.py apply gp-180

.PHONY: consolidation-commit-gp-180
consolidation-commit-gp-180:
	python3 scripts/consolidation_tools.py commit gp-180

.PHONY: consolidation-plan-gp-5
consolidation-plan-gp-5:
	python3 scripts/consolidation_tools.py plan gp-5

.PHONY: consolidation-apply-gp-5
consolidation-apply-gp-5:
	python3 scripts/consolidation_tools.py apply gp-5

.PHONY: consolidation-commit-gp-5
consolidation-commit-gp-5:
	python3 scripts/consolidation_tools.py commit gp-5

.PHONY: consolidation-plan-gp-50
consolidation-plan-gp-50:
	python3 scripts/consolidation_tools.py plan gp-50

.PHONY: consolidation-apply-gp-50
consolidation-apply-gp-50:
	python3 scripts/consolidation_tools.py apply gp-50

.PHONY: consolidation-commit-gp-50
consolidation-commit-gp-50:
	python3 scripts/consolidation_tools.py commit gp-50

.PHONY: consolidation-plan-hx-stomp
consolidation-plan-hx-stomp:
	python3 scripts/consolidation_tools.py plan hx-stomp

.PHONY: consolidation-apply-hx-stomp
consolidation-apply-hx-stomp:
	python3 scripts/consolidation_tools.py apply hx-stomp

.PHONY: consolidation-commit-hx-stomp
consolidation-commit-hx-stomp:
	python3 scripts/consolidation_tools.py commit hx-stomp

.PHONY: consolidation-plan-tonex-one
consolidation-plan-tonex-one:
	python3 scripts/consolidation_tools.py plan tonex-one

.PHONY: consolidation-apply-tonex-one
consolidation-apply-tonex-one:
	python3 scripts/consolidation_tools.py apply tonex-one

.PHONY: consolidation-commit-tonex-one
consolidation-commit-tonex-one:
	python3 scripts/consolidation_tools.py commit tonex-one

.PHONY: consolidation-plan-tonex-pedal
consolidation-plan-tonex-pedal:
	python3 scripts/consolidation_tools.py plan tonex-pedal

.PHONY: consolidation-apply-tonex-pedal
consolidation-apply-tonex-pedal:
	python3 scripts/consolidation_tools.py apply tonex-pedal

.PHONY: consolidation-commit-tonex-pedal
consolidation-commit-tonex-pedal:
	python3 scripts/consolidation_tools.py commit tonex-pedal

.PHONY: consolidation-plan-nano-cortex
consolidation-plan-nano-cortex:
	python3 scripts/consolidation_tools.py plan nano-cortex

.PHONY: consolidation-apply-nano-cortex
consolidation-apply-nano-cortex:
	python3 scripts/consolidation_tools.py apply nano-cortex

.PHONY: consolidation-commit-nano-cortex
consolidation-commit-nano-cortex:
	python3 scripts/consolidation_tools.py commit nano-cortex

.PHONY: consolidation-plan-ame-100
consolidation-plan-ame-100:
	python3 scripts/consolidation_tools.py plan ame-100

.PHONY: consolidation-apply-ame-100
consolidation-apply-ame-100:
	python3 scripts/consolidation_tools.py apply ame-100

.PHONY: consolidation-commit-ame-100
consolidation-commit-ame-100:
	python3 scripts/consolidation_tools.py commit ame-100

.PHONY: consolidation-plan-ame-200
consolidation-plan-ame-200:
	python3 scripts/consolidation_tools.py plan ame-200

.PHONY: consolidation-apply-ame-200
consolidation-apply-ame-200:
	python3 scripts/consolidation_tools.py apply ame-200

.PHONY: consolidation-commit-ame-200
consolidation-commit-ame-200:
	python3 scripts/consolidation_tools.py commit ame-200

.PHONY: consolidation-plan-ame-200-pro
consolidation-plan-ame-200-pro:
	python3 scripts/consolidation_tools.py plan ame-200-pro

.PHONY: consolidation-apply-ame-200-pro
consolidation-apply-ame-200-pro:
	python3 scripts/consolidation_tools.py apply ame-200-pro

.PHONY: consolidation-commit-ame-200-pro
consolidation-commit-ame-200-pro:
	python3 scripts/consolidation_tools.py commit ame-200-pro

.PHONY: consolidation-plan-ace-100
consolidation-plan-ace-100:
	python3 scripts/consolidation_tools.py plan ace-100

.PHONY: consolidation-apply-ace-100
consolidation-apply-ace-100:
	python3 scripts/consolidation_tools.py apply ace-100

.PHONY: consolidation-commit-ace-100
consolidation-commit-ace-100:
	python3 scripts/consolidation_tools.py commit ace-100

.PHONY: consolidation-plan-ave-100
consolidation-plan-ave-100:
	python3 scripts/consolidation_tools.py plan ave-100

.PHONY: consolidation-apply-ave-100
consolidation-apply-ave-100:
	python3 scripts/consolidation_tools.py apply ave-100

.PHONY: consolidation-commit-ave-100
consolidation-commit-ave-100:
	python3 scripts/consolidation_tools.py commit ave-100

.PHONY: consolidation-plan-bg300
consolidation-plan-bg300:
	python3 scripts/consolidation_tools.py plan bg300

.PHONY: consolidation-apply-bg300
consolidation-apply-bg300:
	python3 scripts/consolidation_tools.py apply bg300

.PHONY: consolidation-commit-bg300
consolidation-commit-bg300:
	python3 scripts/consolidation_tools.py commit bg300

.PHONY: consolidation-plan-kmf-10
consolidation-plan-kmf-10:
	python3 scripts/consolidation_tools.py plan kmf-10

.PHONY: consolidation-apply-kmf-10
consolidation-apply-kmf-10:
	python3 scripts/consolidation_tools.py apply kmf-10

.PHONY: consolidation-commit-kmf-10
consolidation-commit-kmf-10:
	python3 scripts/consolidation_tools.py commit kmf-10

.PHONY: consolidation-plan-voicelive-play
consolidation-plan-voicelive-play:
	python3 scripts/consolidation_tools.py plan voicelive-play

.PHONY: consolidation-apply-voicelive-play
consolidation-apply-voicelive-play:
	python3 scripts/consolidation_tools.py apply voicelive-play

.PHONY: consolidation-commit-voicelive-play
consolidation-commit-voicelive-play:
	python3 scripts/consolidation_tools.py commit voicelive-play

.PHONY: consolidation-plan-play-acoustic
consolidation-plan-play-acoustic:
	python3 scripts/consolidation_tools.py plan play-acoustic

.PHONY: consolidation-apply-play-acoustic
consolidation-apply-play-acoustic:
	python3 scripts/consolidation_tools.py apply play-acoustic

.PHONY: consolidation-commit-play-acoustic
consolidation-commit-play-acoustic:
	python3 scripts/consolidation_tools.py commit play-acoustic

.PHONY: consolidation-plan-h8
consolidation-plan-h8:
	python3 scripts/consolidation_tools.py plan h8

.PHONY: consolidation-apply-h8
consolidation-apply-h8:
	python3 scripts/consolidation_tools.py apply h8

.PHONY: consolidation-commit-h8
consolidation-commit-h8:
	python3 scripts/consolidation_tools.py commit h8

.PHONY: consolidation-plan-fb100
consolidation-plan-fb100:
	python3 scripts/consolidation_tools.py plan fb100

.PHONY: consolidation-apply-fb100
consolidation-apply-fb100:
	python3 scripts/consolidation_tools.py apply fb100

.PHONY: consolidation-commit-fb100
consolidation-commit-fb100:
	python3 scripts/consolidation_tools.py commit fb100

.PHONY: consolidation-plan-gr-55
consolidation-plan-gr-55:
	python3 scripts/consolidation_tools.py plan gr-55

.PHONY: consolidation-apply-gr-55
consolidation-apply-gr-55:
	python3 scripts/consolidation_tools.py apply gr-55

.PHONY: consolidation-commit-gr-55
consolidation-commit-gr-55:
	python3 scripts/consolidation_tools.py commit gr-55

.PHONY: consolidation-audit-findings
consolidation-audit-findings:
	python3 scripts/consolidation_tools.py audit-findings

.PHONY: consolidation-audit-legacy
consolidation-audit-legacy:
	python3 scripts/consolidation_tools.py audit-legacy

.PHONY: consolidation-audit-compact-gp100
consolidation-audit-compact-gp100:
	python3 scripts/consolidation_tools.py audit-compact GP-100

.PHONY: consolidation-audit-compact-gp150
consolidation-audit-compact-gp150:
	python3 scripts/consolidation_tools.py audit-compact GP-150

.PHONY: consolidation-audit-compact-matribox
consolidation-audit-compact-matribox:
	python3 scripts/consolidation_tools.py audit-compact Matribox

.PHONY: consolidation-audit-compact-gp5
consolidation-audit-compact-gp5:
	python3 scripts/consolidation_tools.py audit-compact GP-5

.PHONY: consolidation-audit-compact-gp50
consolidation-audit-compact-gp50:
	python3 scripts/consolidation_tools.py audit-compact GP-50

.PHONY: consolidation-audit-compact-gp180
consolidation-audit-compact-gp180:
	python3 scripts/consolidation_tools.py audit-compact GP-180

.PHONY: consolidation-audit-compact-smartbox
consolidation-audit-compact-smartbox:
	python3 scripts/consolidation_tools.py audit-compact "Smart Box"

.PHONY: consolidation-audit-compact-pocketmaster
consolidation-audit-compact-pocketmaster:
	python3 scripts/consolidation_tools.py audit-compact "Pocket Master"

.PHONY: consolidation-audit-compact-union
consolidation-audit-compact-union:
	python3 scripts/consolidation_tools.py audit-compact-union

.PHONY: consolidation-audit-floorboard-union
consolidation-audit-floorboard-union:
	python3 scripts/consolidation_tools.py audit-floorboard-union

.PHONY: consolidation-audit-compact-links
consolidation-audit-compact-links:
	python3 scripts/consolidation_tools.py audit-compact-links

.PHONY: consolidation-plan-nux-mg101
consolidation-plan-nux-mg101:
	python3 scripts/consolidation_tools.py plan-nux-mg101

.PHONY: consolidation-plan-nux-mg300
consolidation-plan-nux-mg300:
	python3 scripts/consolidation_tools.py plan-nux-mg300

.PHONY: consolidation-plan-nux-mg300mkii
consolidation-plan-nux-mg300mkii:
	python3 scripts/consolidation_tools.py plan-nux-mg300mkii

.PHONY: consolidation-plan-nux-mg400
consolidation-plan-nux-mg400:
	python3 scripts/consolidation_tools.py plan-nux-mg400

.PHONY: consolidation-plan-nux-mg30
consolidation-plan-nux-mg30:
	python3 scripts/consolidation_tools.py plan-nux-mg30

.PHONY: consolidation-plan-nux-mg50li
consolidation-plan-nux-mg50li:
	python3 scripts/consolidation_tools.py plan-nux-mg50li

.PHONY: consolidation-plan-nux-union
consolidation-plan-nux-union:
	python3 scripts/consolidation_tools.py plan-nux-union

.PHONY: consolidation-audit-nux-union
consolidation-audit-nux-union:
	python3 scripts/consolidation_tools.py audit-nux-union

.PHONY: consolidation-audit-nux-links
consolidation-audit-nux-links:
	python3 scripts/consolidation_tools.py audit-nux-links

.PHONY: consolidation-plan-bass-union
consolidation-plan-bass-union:
	python3 scripts/consolidation_tools.py plan-bass-union

.PHONY: consolidation-audit-bass-union
consolidation-audit-bass-union:
	python3 scripts/consolidation_tools.py audit-bass-union

.PHONY: consolidation-audit-bass-links
consolidation-audit-bass-links:
	python3 scripts/consolidation_tools.py audit-bass-links

.PHONY: consolidation-plan-vocal-union
consolidation-plan-vocal-union:
	python3 scripts/consolidation_tools.py plan-vocal-union

.PHONY: consolidation-audit-vocal-union
consolidation-audit-vocal-union:
	python3 scripts/consolidation_tools.py audit-vocal-union

.PHONY: consolidation-audit-vocal-links
consolidation-audit-vocal-links:
	python3 scripts/consolidation_tools.py audit-vocal-links

.PHONY: consolidation-plan-advanced-hxe
consolidation-plan-advanced-hxe:
	python3 scripts/consolidation_tools.py plan-advanced-hxe

.PHONY: consolidation-plan-advanced-flex
consolidation-plan-advanced-flex:
	python3 scripts/consolidation_tools.py plan-advanced-flex

.PHONY: consolidation-plan-advanced-union
consolidation-plan-advanced-union:
	python3 scripts/consolidation_tools.py plan-advanced-union

.PHONY: consolidation-audit-advanced-union
consolidation-audit-advanced-union:
	python3 scripts/consolidation_tools.py audit-advanced-union

.PHONY: consolidation-audit-advanced-links
consolidation-audit-advanced-links:
	python3 scripts/consolidation_tools.py audit-advanced-links

.PHONY: consolidation-plan-boss-union
consolidation-plan-boss-union:
	python3 scripts/consolidation_tools.py plan-boss-union

.PHONY: consolidation-audit-boss-union
consolidation-audit-boss-union:
	python3 scripts/consolidation_tools.py audit-boss-union

.PHONY: consolidation-audit-boss-links
consolidation-audit-boss-links:
	python3 scripts/consolidation_tools.py audit-boss-links

.PHONY: consolidation-plan-boss-history-union
consolidation-plan-boss-history-union:
	python3 scripts/consolidation_tools.py plan-boss-history-union

.PHONY: consolidation-audit-boss-history-union
consolidation-audit-boss-history-union:
	python3 scripts/consolidation_tools.py audit-boss-history-union

.PHONY: consolidation-audit-boss-history-links
consolidation-audit-boss-history-links:
	python3 scripts/consolidation_tools.py audit-boss-history-links

.PHONY: consolidation-plan-audota-union
consolidation-plan-audota-union:
	python3 scripts/consolidation_tools.py plan-audota-union

.PHONY: consolidation-audit-audota-union
consolidation-audit-audota-union:
	python3 scripts/consolidation_tools.py audit-audota-union

.PHONY: consolidation-audit-audota-links
consolidation-audit-audota-links:
	python3 scripts/consolidation_tools.py audit-audota-links

.PHONY: consolidation-plan-cube-union
consolidation-plan-cube-union:
	python3 scripts/consolidation_tools.py plan-cube-union

.PHONY: consolidation-audit-cube-union
consolidation-audit-cube-union:
	python3 scripts/consolidation_tools.py audit-cube-union

.PHONY: consolidation-audit-cube-links
consolidation-audit-cube-links:
	python3 scripts/consolidation_tools.py audit-cube-links

.PHONY: consolidation-plan-owned-union
consolidation-plan-owned-union:
	python3 scripts/consolidation_tools.py plan-owned-union

.PHONY: consolidation-audit-owned-union
consolidation-audit-owned-union:
	python3 scripts/consolidation_tools.py audit-owned-union

.PHONY: consolidation-audit-owned-links
consolidation-audit-owned-links:
	python3 scripts/consolidation_tools.py audit-owned-links

.PHONY: consolidation-plan-market1-union
consolidation-plan-market1-union:
	python3 scripts/consolidation_tools.py plan-market1-union

.PHONY: consolidation-audit-market1-union
consolidation-audit-market1-union:
	python3 scripts/consolidation_tools.py audit-market1-union

.PHONY: consolidation-audit-market1-links
consolidation-audit-market1-links:
	python3 scripts/consolidation_tools.py audit-market1-links

.PHONY: consolidation-plan-market2-union
consolidation-plan-market2-union:
	python3 scripts/consolidation_tools.py plan-market2-union

.PHONY: consolidation-audit-market2-union
consolidation-audit-market2-union:
	python3 scripts/consolidation_tools.py audit-market2-union

.PHONY: consolidation-audit-market2-links
consolidation-audit-market2-links:
	python3 scripts/consolidation_tools.py audit-market2-links

.PHONY: consolidation-plan-market3-union
consolidation-plan-market3-union:
	python3 scripts/consolidation_tools.py plan-market3-union

.PHONY: consolidation-audit-market3-union
consolidation-audit-market3-union:
	python3 scripts/consolidation_tools.py audit-market3-union

.PHONY: consolidation-audit-market3-links
consolidation-audit-market3-links:
	python3 scripts/consolidation_tools.py audit-market3-links

.PHONY: consolidation-plan-market4-union
consolidation-plan-market4-union:
	python3 scripts/consolidation_tools.py plan-market4-union

.PHONY: consolidation-audit-market4-union
consolidation-audit-market4-union:
	python3 scripts/consolidation_tools.py audit-market4-union

.PHONY: consolidation-audit-market4-links
consolidation-audit-market4-links:
	python3 scripts/consolidation_tools.py audit-market4-links

.PHONY: consolidation-plan-market5-union
consolidation-plan-market5-union:
	python3 scripts/consolidation_tools.py plan-market5-union

.PHONY: consolidation-audit-market5-union
consolidation-audit-market5-union:
	python3 scripts/consolidation_tools.py audit-market5-union

.PHONY: consolidation-audit-market5-links
consolidation-audit-market5-links:
	python3 scripts/consolidation_tools.py audit-market5-links

.PHONY: consolidation-plan-market6-union
consolidation-plan-market6-union:
	python3 scripts/consolidation_tools.py plan-market6-union

.PHONY: consolidation-audit-market6-union
consolidation-audit-market6-union:
	python3 scripts/consolidation_tools.py audit-market6-union

.PHONY: consolidation-audit-market6-links
consolidation-audit-market6-links:
	python3 scripts/consolidation_tools.py audit-market6-links

.PHONY: consolidation-plan-market7-union
consolidation-plan-market7-union:
	python3 scripts/consolidation_tools.py plan-market7-union

.PHONY: consolidation-audit-market7-union
consolidation-audit-market7-union:
	python3 scripts/consolidation_tools.py audit-market7-union

.PHONY: consolidation-audit-market7-links
consolidation-audit-market7-links:
	python3 scripts/consolidation_tools.py audit-market7-links

.PHONY: consolidation-audit-body-differences
consolidation-audit-body-differences:
	python3 scripts/consolidation_tools.py audit-body-differences

.PHONY: consolidation-compact-reference-plan
consolidation-compact-reference-plan:
	python3 scripts/consolidation_tools.py compact-reference-plan

.PHONY: consolidation-commit-preservation-repairs
consolidation-commit-preservation-repairs:
	python3 scripts/consolidation_tools.py commit-preservation-repairs

consolidation-test-preservation-kinds:
	python3 scripts/consolidation_tools.py test-preservation-kinds

consolidation-stage-preservation-repairs:
	python3 scripts/consolidation_tools.py stage-preservation-repairs

.PHONY: consolidation-audit-historical
consolidation-audit-historical:
	python3 scripts/consolidation_tools.py audit-historical

.PHONY: consolidation-audit-source-history
consolidation-audit-source-history:
	python3 scripts/consolidation_tools.py audit-source-history

.PHONY: consolidation-test-source-history
consolidation-test-source-history:
	python3 scripts/consolidation_tools.py test-source-history
