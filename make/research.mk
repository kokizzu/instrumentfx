# Existing research command API; preserve target names and recipes.

.PHONY: research-status
research-status:
	python3 scripts/research_tools.py status

.PHONY: research-verify
research-verify:
	python3 scripts/research_tools.py verify

.PHONY: research-source-gp200jr
research-source-gp200jr:
	python3 scripts/research_tools.py gp200jr

.PHONY: research-render-gp200jr
research-render-gp200jr:
	python3 scripts/research_tools.py render-gp200jr

.PHONY: research-commit-gp200jr
research-commit-gp200jr:
	python3 scripts/research_tools.py commit-gp200jr

.PHONY: research-commit-hx-effects
research-commit-hx-effects:
	python3 scripts/research_tools.py commit-hx-effects

.PHONY: research-commit-comparisons
research-commit-comparisons:
	python3 scripts/research_tools.py commit-comparisons

.PHONY: research-source-prime
research-source-prime:
	python3 scripts/research_tools.py source-prime

.PHONY: research-commit-prime
research-commit-prime:
	python3 scripts/research_tools.py commit-prime

.PHONY: research-verify-archive-provenance
research-verify-archive-provenance:
	python3 scripts/research_tools.py restore-archive-provenance

.PHONY: research-source-ge300
research-source-ge300:
	python3 scripts/research_tools.py source-ge300

.PHONY: research-commit-ge300
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

.PHONY: research-source-b2-controls
research-source-b2-controls:
	python3 scripts/research_tools.py source-b2-controls

.PHONY: research-commit-helix-lt
research-commit-helix-lt:
	python3 scripts/research_tools.py commit-helix-lt

.PHONY: research-commit-gt100
research-commit-gt100:
	python3 scripts/research_tools.py commit-gt100

.PHONY: research-commit-gp150-nam
research-commit-gp150-nam:
	python3 scripts/research_tools.py commit-gp150-nam

.PHONY: research-commit-gp100-nam
research-commit-gp100-nam:
	python3 scripts/research_tools.py commit-gp100-nam

.PHONY: research-commit-field-projection
research-commit-field-projection:
	python3 scripts/research_tools.py commit-field-projection

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

.PHONY: research-commit-finding-audit
research-commit-finding-audit:
	python3 scripts/research_tools.py commit-finding-audit

.PHONY: research-commit-legacy-audit
research-commit-legacy-audit:
	python3 scripts/research_tools.py commit-legacy-audit

.PHONY: research-commit-compact-gp100-audit
research-commit-compact-gp100-audit:
	python3 scripts/research_tools.py commit-compact-gp100-audit

.PHONY: research-commit-compact-gp150-audit
research-commit-compact-gp150-audit:
	python3 scripts/research_tools.py commit-compact-gp150-audit

.PHONY: research-commit-compact-matribox-audit
research-commit-compact-matribox-audit:
	python3 scripts/research_tools.py commit-compact-matribox-audit

.PHONY: research-commit-compact-gp5-audit
research-commit-compact-gp5-audit:
	python3 scripts/research_tools.py commit-compact-gp5-audit

.PHONY: research-commit-compact-gp50-audit
research-commit-compact-gp50-audit:
	python3 scripts/research_tools.py commit-compact-gp50-audit

.PHONY: research-commit-compact-gp180-audit
research-commit-compact-gp180-audit:
	python3 scripts/research_tools.py commit-compact-gp180-audit

.PHONY: research-commit-compact-smartbox-audit
research-commit-compact-smartbox-audit:
	python3 scripts/research_tools.py commit-compact-smartbox-audit

.PHONY: research-commit-compact-pocketmaster-audit
research-commit-compact-pocketmaster-audit:
	python3 scripts/research_tools.py commit-compact-pocketmaster-audit

.PHONY: research-commit-cubebabyelectric-preservation
research-commit-cubebabyelectric-preservation:
	python3 scripts/research_tools.py commit-cubebabyelectric-preservation

.PHONY: research-commit-compact-union
research-commit-compact-union:
	python3 scripts/research_tools.py commit-compact-union

.PHONY: research-commit-floorboard-matribox-ii
research-commit-floorboard-matribox-ii:
	python3 scripts/research_tools.py commit-floorboard-matribox-ii

.PHONY: research-commit-floorboard-matribox-ii-pro
research-commit-floorboard-matribox-ii-pro:
	python3 scripts/research_tools.py commit-floorboard-matribox-ii-pro

.PHONY: research-commit-floorboard-union
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

.PHONY: research-commit-nux-mg101-audit
research-commit-nux-mg101-audit:
	python3 scripts/research_tools.py commit-nux-mg101-audit

.PHONY: research-commit-nux-mg300-audit
research-commit-nux-mg300-audit:
	python3 scripts/research_tools.py commit-nux-mg300-audit

.PHONY: research-commit-nux-mg300mkii-audit
research-commit-nux-mg300mkii-audit:
	python3 scripts/research_tools.py commit-nux-mg300mkii-audit

.PHONY: research-commit-nux-mg400-audit
research-commit-nux-mg400-audit:
	python3 scripts/research_tools.py commit-nux-mg400-audit

.PHONY: research-commit-nux-mg30-audit
research-commit-nux-mg30-audit:
	python3 scripts/research_tools.py commit-nux-mg30-audit

.PHONY: research-commit-nux-mg50li-audit
research-commit-nux-mg50li-audit:
	python3 scripts/research_tools.py commit-nux-mg50li-audit

.PHONY: research-commit-nux-union
research-commit-nux-union:
	python3 scripts/research_tools.py commit-nux-union

.PHONY: research-commit-bass-union
research-commit-bass-union:
	python3 scripts/research_tools.py commit-bass-union

.PHONY: research-commit-vocal-union
research-commit-vocal-union:
	python3 scripts/research_tools.py commit-vocal-union

.PHONY: research-commit-advanced-hxe-audit
research-commit-advanced-hxe-audit:
	python3 scripts/research_tools.py commit-advanced-hxe-audit

.PHONY: research-commit-advanced-flex-audit
research-commit-advanced-flex-audit:
	python3 scripts/research_tools.py commit-advanced-flex-audit

.PHONY: research-commit-advanced-union
research-commit-advanced-union:
	python3 scripts/research_tools.py commit-advanced-union

.PHONY: research-commit-boss-union
research-commit-boss-union:
	python3 scripts/research_tools.py commit-boss-union

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

.PHONY: research-commit-audota-union
research-commit-audota-union:
	python3 scripts/research_tools.py commit-audota-union

.PHONY: research-commit-cube-union
research-commit-cube-union:
	python3 scripts/research_tools.py commit-cube-union

.PHONY: research-commit-owned-union
research-commit-owned-union:
	python3 scripts/research_tools.py commit-owned-union

.PHONY: research-commit-market1-union
research-commit-market1-union:
	python3 scripts/research_tools.py commit-market1-union

.PHONY: research-commit-market2-union
research-commit-market2-union:
	python3 scripts/research_tools.py commit-market2-union

.PHONY: research-commit-market3-union
research-commit-market3-union:
	python3 scripts/research_tools.py commit-market3-union

.PHONY: research-commit-market4-union
research-commit-market4-union:
	python3 scripts/research_tools.py commit-market4-union

.PHONY: research-commit-market5-union
research-commit-market5-union:
	python3 scripts/research_tools.py commit-market5-union

.PHONY: research-commit-market6-union
research-commit-market6-union:
	python3 scripts/research_tools.py commit-market6-union

.PHONY: research-commit-market7-union
research-commit-market7-union:
	python3 scripts/research_tools.py commit-market7-union

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

.PHONY: research-commit-rev500
research-commit-rev500:
	python3 scripts/research_tools.py commit-rev500

.PHONY: research-commit-dsp2024p
research-commit-dsp2024p:
	python3 scripts/research_tools.py commit-dsp2024p

.PHONY: research-commit-ie550
research-commit-ie550:
	python3 scripts/research_tools.py commit-ie550

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

.PHONY: research-commit-yamaha
research-commit-yamaha:
	python3 scripts/yamaha_catalogue.py commit

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

.PHONY: research-commit-gfi
research-commit-gfi:
	python3 scripts/gfi_catalogue.py commit

.PHONY: research-review-hotone
research-review-hotone:
	python3 scripts/hotone_catalogue.py review

.PHONY: research-commit-atomic
research-commit-atomic:
	python3 scripts/atomic_catalogue.py commit

.PHONY: research-stage-positive-grid
research-stage-positive-grid:
	python3 scripts/positive_grid_catalogue.py stage

.PHONY: research-commit-positive-grid
research-commit-positive-grid:
	python3 scripts/positive_grid_catalogue.py commit

.PHONY: research-stage-mooer
research-stage-mooer:
	python3 scripts/mooer_catalogue.py stage

.PHONY: research-stage-hotone
research-stage-hotone:
	python3 scripts/hotone_catalogue.py stage

research-stage-blackstar:
	python3 scripts/blackstar_catalogue.py stage

.PHONY: research-stage-harley-benton
research-stage-harley-benton:
	python3 scripts/harley_benton_catalogue.py stage

.PHONY: research-test-canonical-sections
research-test-canonical-sections:
	python3 scripts/test_research_tools.py

.PHONY: research-stage-gfi
research-stage-gfi:
	python3 scripts/gfi_catalogue.py stage

.PHONY: research-stage-yamaha
research-stage-yamaha:
	python3 scripts/yamaha_catalogue.py stage

.PHONY: research-stage-tech21
research-stage-tech21:
	python3 scripts/tech21_catalogue.py stage

.PHONY: research-test-compatibility-reader
research-test-compatibility-reader:
	python3 scripts/research_tools.py test-compatibility-reader

.PHONY: research-verify-compatibility-readers
research-verify-compatibility-readers:
	python3 scripts/research_tools.py verify-compatibility-readers

.PHONY: research-stage-roland
research-stage-roland:
	python3 scripts/research_audit_roland.py stage

.PHONY: research-commit-roland
research-commit-roland:
	python3 scripts/research_audit_roland.py commit

# Manufacturer-image retrieval uses a reviewed URL and one rolling /tmp image.
.PHONY: research-source-image-plan research-source-image-apply research-source-image-test
research-source-image-plan:
	python3 scripts/source_image.py plan

research-source-image-apply:
	python3 scripts/source_image.py apply

research-source-image-test:
	python3 scripts/source_image.py test

.PHONY: research-source-image-render
research-source-image-render:
	python3 scripts/source_image.py render

.PHONY: research-source-image-text
research-source-image-text:
	python3 scripts/source_image.py text

.PHONY: research-source-index
research-source-index:
	python3 scripts/source_image.py index
