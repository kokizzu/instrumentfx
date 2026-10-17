"""Local research checks and explicit per-model commits; never uses Actions."""
import html
import json
from pathlib import Path
import re
import subprocess
import sys
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parent.parent

def git(*args):
    return subprocess.check_output(['git', '-c', 'core.hooksPath=/dev/null', '-C', str(ROOT), *args], text=True)

def identity():
    remote = git('remote', 'get-url', 'origin').strip()
    assert remote in ('git@github.com:kokizzu/instrumentfx.git', 'https://github.com/kokizzu/instrumentfx.git'), remote
    assert git('branch', '--show-current').strip() == 'main'


def read_preserved_source(path):
    """Read pinned original evidence after a legacy page becomes a redirect."""
    import hashlib
    key = str(path)
    state = json.loads((ROOT/'research-state.json').read_text())
    entry = state.get('migration',{}).get('retired_sources',{}).get(key)
    if entry is None:
        return (ROOT/key).read_text()
    assert key.startswith('effects/') and '..' not in Path(key).parts
    assert re.fullmatch(r'[0-9a-f]{40}',entry['source_commit'])
    original = git('show',entry['source_commit']+':'+key)
    assert hashlib.sha256(original.encode()).hexdigest() == entry['source_sha256'], 'Pinned evidence hash mismatch: '+key
    return original

def verify():
    sys.dont_write_bytecode=True
    from canonical_links import preservation_text
    identity()
    state = json.loads((ROOT / 'research-state.json').read_text())
    pairs = [(b, m) for b, models in state['inventory_by_brand'].items() for m in models]
    assert len(pairs) == len(set(pairs)) == state['active_model_count'], (len(pairs), state['active_model_count'])
    canonical = sum(map(len, state['root_brand_content'].values()))
    assert canonical == state['canonical_root_model_count']
    assert len(pairs) - canonical == state['legacy_only_model_count']
    excluded = set(state['excluded_models'])
    assert not excluded.intersection(m for _, m in pairs)
    workflows = list((ROOT / '.github' / 'workflows').glob('*'))
    assert not workflows, workflows
    assert not git('ls-files', '.github/workflows').strip()
    if 'B1Xon' in state['root_brand_content'].get('ZOOM.md',[]):
        original=read_preserved_source('effects/findings/2026-10-14-zoom-b1xon.md').split('\n',1)[1]
        preserved=preservation_text('ZOOM.md').split('<!-- B1Xon preserved source begins -->\n',1)[1].split('<!-- B1Xon preserved source ends -->',1)[0]
        assert preserved.replace('\n### ','\n## ').replace('(effects/OWNERSHIP.md)','(../OWNERSHIP.md)')==original,'B1Xon consolidation lost source material'
    if state.get('separate_specialist_archives'):
        original=git('show','9c8d296:effects/specialist.md')
        marker='## Excluded archive — not part of the multi-effects comparison'
        preserved=preservation_text('SINGLE-GUITAR.md').split(marker,1)[1].replace('[SCOPE.md](effects/SCOPE.md)','[SCOPE.md](SCOPE.md)')
        assert original.split(marker,1)[1]==preserved,'Guitar archive lost original material'
        original_fv=git('show','9c8d296:effects/findings/2026-10-14-flamma-fv01.md')
        body=preservation_text('SINGLE-VOCAL.md').split('## Flamma FV01 Corrector\n',1)[1]
        assert body.replace('(effects/SCOPE.md)','(../SCOPE.md)').replace('\n### ','\n## ')==original_fv.split('\n',1)[1],'FV01 archive lost original material'
    errors = []
    for path in ROOT.glob('*.md'):
        text = path.read_text()
        for link in re.findall(r'\]\(([^)\s]+)(?:\s+"[^"]*")?\)', text):
            if '://' in link or link.startswith('mailto:'):
                continue
            dest, _, anchor = urllib.parse.unquote(link).partition('#')
            target = path.parent / dest if dest else path
            if not target.exists():
                errors.append(f'{path.name}: missing {link}')
                continue
            if anchor and target.suffix == '.md':
                headings = re.findall(r'^#+\s+(.+)$', target.read_text(), re.M)
                slugs = [re.sub(r'[^\w\- ]', '', h.lower().replace('`', '')).replace(' ', '-') for h in headings]
                if anchor not in slugs:
                    errors.append(f'{path.name}: missing anchor {link}')
    assert not errors, '\n'.join(errors)
    print(f'PASS: {len(pairs)} unique active models; {canonical} root-canonical; {len(pairs)-canonical} legacy-only; root links resolve; no workflows.')

def gp200jr():
    url = 'https://www.valeton.net/wpfd_file/gp-200jr_online-manual_en_firmware-v1-8-0-pdf/'
    with urllib.request.urlopen(url, timeout=40) as response:
        text = response.read().decode()
    links = [html.unescape(x) for x in re.findall(r'href=[\"\x27]([^\"\x27]+)', text)]
    links = [urllib.parse.urljoin(url, x) for x in links if 'download' in x or '.pdf' in x]
    print(json.dumps(links, indent=2), flush=True)
    pdfs = [x for x in links if 'gp-200jr' in x and x.endswith('.pdf')]
    assert len(set(pdfs)) == 1, pdfs
    cache = Path('/tmp/instrumentfx-sources')
    cache.mkdir(exist_ok=True)
    dest = cache / 'gp-200jr-v1.8.0.pdf'
    with urllib.request.urlopen(pdfs[0], timeout=60) as response:
        content = response.read()
    assert content.startswith(b'%PDF'), content[:100]
    dest.write_bytes(content)
    subprocess.run(['pdftotext', '-layout', str(dest), str(dest.with_suffix('.txt'))], check=True)
    print(f'Saved primary manual and extracted text: {dest}')

def main():
    identity()
    mode = sys.argv[1]
    if mode == 'status':
        print(git('status', '--short', '--branch'))
        print(git('diff', '--cached', '--stat'))
        print(git('log', '-5', '--oneline'))
    elif mode in ('commit-g1xfour-followup','commit-g1four-market','commit-ax100g','commit-vamp3','commit-me30','commit-rp70','commit-ad10','commit-g2four-market','commit-me50b','commit-rp200','commit-gp200x','commit-mfx10','commit-anagram','commit-prime-s1','commit-blacktruck','commit-pockrock','commit-fx150b','commit-fx20','commit-dc5','commit-rc5','commit-ms3','commit-rd5','commit-v3compat','commit-tc2','commit-tc1','commit-sol918','commit-me90b-control','commit-gorig2','commit-dualstomplite','commit-dualstomp','commit-tinystomp','commit-gorigb','commit-fx600','commit-vlt2','commit-gt10b','commit-floorpodplus','commit-spx2000','commit-ms80ir','commit-ve22','commit-ve1','commit-ax10b','commit-aas','commit-b2-conversion','commit-fv05','commit-stageman','commit-prime-m2','commit-prime-m1','commit-prime-p2','commit-fm3','commit-player','commit-quad','commit-v6-live','commit-play-qsg','commit-g1-original'):
        verify()
        subprocess.run(['python3',str(ROOT/'scripts/comparison_views.py'),'verify'],check=True)
        assert not git('diff','--cached','--name-only').strip(), 'Existing staged changes'
        paths=[('ZOOM.md' if mode in ('commit-g1xfour-followup','commit-g1four-market') else 'KORG.md' if mode == 'commit-ax100g' else 'BEHRINGER.md' if mode == 'commit-vamp3' else 'BOSS.md' if mode == 'commit-me30' else 'DIGITECH.md' if mode == 'commit-rp70' else 'BOSS.md' if mode == 'commit-ad10' else 'ZOOM.md' if mode == 'commit-g2four-market' else 'BOSS.md' if mode == 'commit-me50b' else 'DIGITECH.md' if mode == 'commit-rp200' else 'VALETON.md' if mode == 'commit-gp200x' else 'NUX.md' if mode == 'commit-mfx10' else 'DARKGLASS.md' if mode == 'commit-anagram' else 'MOOER.md' if mode in ('commit-blacktruck','commit-prime-s1') else 'AMMOON.md' if mode == 'commit-pockrock' else 'ZOOM.md' if mode == 'commit-v3compat' else 'JOYO.md' if mode in ('commit-tc1','commit-tc2') else 'MOSKY.md' if mode in ('commit-sol918','commit-rd5','commit-rc5','commit-dc5') else 'SORAN.md' if mode in ('commit-gorigb','commit-tinystomp','commit-dualstomp','commit-dualstomplite','commit-gorig2') else 'BEHRINGER.md' if mode == 'commit-fx600' else 'BOSS.md' if mode in ('commit-ms3','commit-me90b-control','commit-ve1','commit-ve22','commit-gt10b') else 'LINE6.md' if mode == 'commit-floorpodplus' else 'YAMAHA.md' if mode == 'commit-spx2000' else 'KORG.md' if mode == 'commit-ax10b' else 'ZOOM.md' if mode in ('commit-b2-conversion','commit-ms80ir') else 'FLAMMA.md' if mode in ('commit-fv05','commit-fx20','commit-fx150b') else 'NUX.md' if mode in ('commit-stageman','commit-aas') else 'MOOER.md' if mode in ('commit-prime-m2','commit-prime-m1','commit-prime-p2') else 'TC-HELICON.md' if mode in ('commit-play-qsg','commit-vlt2') else 'ZOOM.md' if mode in ('commit-v6-live','commit-g1-original') else 'NEURAL-DSP.md' if mode == 'commit-quad' else 'KEMPER.md' if mode == 'commit-player' else 'FRACTAL-AUDIO.md'),'README.md','MULTI-EFFECTS.md','research-state.json','ALL-GUITAR.md','ALL-BASS.md','ALL-VOCAL.md','scripts/comparison_views.py','scripts/research_tools.py','Makefile']
        changed=set(git('diff','--name-only').splitlines())|set(git('ls-files','--others','--exclude-standard').splitlines())
        assert changed <= set(paths), changed-set(paths)
        git('add','--',*sorted(changed))
        print(git('diff','--cached','--stat'))
        print(git('commit','-m','research(zoom): distinguish G1X FOUR pedal effects from Output VP' if mode == 'commit-g1xfour-followup' else 'research(zoom): complete G1 FOUR published category census' if mode == 'commit-g1four-market' else 'research(korg): qualify AX100G acoustic compressor and pedal wording' if mode == 'commit-ax100g' else 'research(behringer): qualify VAMP3 control layers and MIDI port role' if mode == 'commit-vamp3' else 'research(boss): qualify ME30 compressor and pedal-pitch choices' if mode == 'commit-me30' else 'research(digitech): qualify RP70 shared selector and output behavior' if mode == 'commit-rp70' else 'research(boss): qualify AD10 feedback EQ and output-level options' if mode == 'commit-ad10' else 'research(zoom): preserve G2 FOUR offers and voucher disagreement' if mode == 'commit-g2four-market' else 'research(boss): qualify ME50B synth waveforms and pedal alternatives' if mode == 'commit-me50b' else 'research(digitech): qualify RP200 tuner mute and live operation' if mode == 'commit-rp200' else 'research(valeton): flag GP200 FAQ hardware conflicts and operating limits' if mode == 'commit-gp200x' else 'research(nux): verify MFX10 user memory and drum-loop operation' if mode == 'commit-mfx10' else 'research(darkglass): qualify Axioma tracking and Guitar Essentials edition' if mode == 'commit-anagram' else 'research(mooer): qualify Prime S1 regional library charging and bank conflict' if mode == 'commit-prime-s1' else 'research(mooer): qualify Black Truck digital format tuner and supply ratings' if mode == 'commit-blacktruck' else 'research(ammoon): recover PockRock primary page and preserve specification conflicts' if mode == 'commit-pockrock' else 'docs(flamma): consolidate current FX150b comparison and retain complete evidence' if mode == 'commit-fx150b' else 'research(flamma): preserve FX20 original effect-list and control-audit limits' if mode == 'commit-fx20' else 'research(mosky): add DC5 with grouped-function and cached-offer qualifications' if mode == 'commit-dc5' else 'research(mosky): add RC5 preserving manufacturer function-count conflict' if mode == 'commit-rc5' else 'research(boss): corroborate MS-3 MIDI setup count and tempo hold' if mode == 'commit-ms3' else 'research(mosky): add RD5 with primary specification and qualified hardware asks' if mode == 'commit-rd5' else 'research(zoom): qualify V3 effect parameter and selected bypass scope' if mode == 'commit-v3compat' else 'research(joyo): add distinct Tone Chain TC-2 with own controls and qualified offer' if mode == 'commit-tc2' else 'research(joyo): preserve exact TC-1 original manual lead and access limits' if mode == 'commit-tc1' else 'research(mosky): add SOL918 with qualified loop count and exact hardware offers' if mode == 'commit-sol918' else 'research(boss): include documented ME-90B guitar processing in shared comparisons' if mode == 'commit-me90b-control' else 'research(soran): qualify Go Rig II electrical limits battery indicators and offer access' if mode == 'commit-gorig2' else 'research(soran): preserve Lite electrical limits and qualify JME-02 manual lead' if mode == 'commit-dualstomplite' else 'research(soran): qualify Dual Stomp electrical limits and reject unsupported power claim' if mode == 'commit-dualstomp' else 'research(soran): audit Tiny Stomp factory choices separately from import slots' if mode == 'commit-tinystomp' else 'research(soran): preserve Go Rig B electrical specifications and converter label difference' if mode == 'commit-gorigb' else 'research(behringer): qualify FX600 cached asks and reject unresolved used variant' if mode == 'commit-fx600' else 'research(tc-helicon): qualify VoiceLive Play analog levels and USB wording conflict' if mode == 'commit-vlt2' else 'research(boss): distinguish GT-10B loop modes and bass algorithms' if mode == 'commit-gt10b' else 'research(line6): distinguish Floor POD Plus expression calibration procedure' if mode == 'commit-floorpodplus' else 'research(yamaha): qualify SPX2000 clock and logical MIDI port routing' if mode == 'commit-spx2000' else 'research(zoom): qualify MS-80IR Plus electrical and battery ratings' if mode == 'commit-ms80ir' else 'research(boss): qualify VE-22 driver support and backing output routing' if mode == 'commit-ve22' else 'research(boss): clarify VE-1 correction speed and memory write' if mode == 'commit-ve1' else 'research(korg): verify AX10B saving reset scope and pedal assignment dependency' if mode == 'commit-ax10b' else 'research(nux): preserve Amp Academy Stomp regional capacity and routing conflicts' if mode == 'commit-aas' else 'research(zoom): qualify B2 FOUR Android app and OTG compatibility limits' if mode == 'commit-b2-conversion' else 'research(flamma): qualify FV05 auto recording and source accessibility' if mode == 'commit-fv05' else 'research(nux): preserve exact used Stageman Floor hardware asking price' if mode == 'commit-stageman' else 'research(mooer): qualify Prime M2 outputs dimensions and stem separation' if mode == 'commit-prime-m2' else 'research(mooer): document Prime M1 IR cache and charging cable limits' if mode == 'commit-prime-m1' else 'research(mooer): qualify Prime P2 dynamic modules and regional charging conflict' if mode == 'commit-prime-p2' else 'research(zoom): document original G1 preselect and rhythm restrictions' if mode == 'commit-g1-original' else 'research(vocal): qualify VoiceLive Play regional specs and historical preset list' if mode == 'commit-play-qsg' else 'research(zoom): qualify V6 output power and bundle evidence' if mode == 'commit-v6-live' else 'research(neural): qualify Quad Cortex capture and plugin prerequisites' if mode == 'commit-quad' else 'research(kemper): preserve second exact Head MK2 asking price' if mode == 'commit-player' else 'research(fractal): add FM9 MKII Turbo and preserve revision limits'))
    elif mode == 'commit-discovery':
        verify()
        assert not git('diff', '--cached', '--name-only').strip(), 'Existing staged changes'
        paths = ['research-state.json', 'Makefile', 'scripts/research_tools.py']
        changed = set(git('diff', '--name-only').splitlines())
        assert changed <= set(paths), changed - set(paths)
        git('add', '--', *paths)
        print(git('diff', '--cached', '--stat'))
        print(git('commit', '-m', 'research(discovery): queue Wisdom DFX2000 with brand identity unresolved'))
    elif mode in ('commit-h9max', 'commit-1201', 'commit-vt4', 'commit-ampero-one', 'commit-katana-go', 'commit-microplus', 'commit-mg20', 'commit-m100', 'commit-hxe-price', 'commit-criticalmass', 'commit-b21u', 'commit-rfx1100', 'commit-spx990', 'commit-spx900', 'commit-midiverb4', 'commit-microverb4', 'commit-fx2000', 'commit-mx200', 'commit-gnx3', 'commit-b1four-followup', 'commit-b1xfour-followup', 'commit-r16', 'commit-fx50', 'commit-fg200', 'commit-fv04', 'commit-fv03', 'commit-fb200', 'commit-fv02', 'commit-readme-counts', 'commit-hd400', 'commit-xtlive', 'commit-x3live', 'commit-harmony-singer2', 'commit-duplicator', 'commit-mic-mechanic2', 'commit-708ii', 'commit-707ii', 'commit-ax30g', 'commit-rp155', 'commit-vamp2', 'commit-bass-vamp-pro', 'commit-bass-vamp', 'commit-amplifi-fx100', 'commit-hd500x', 'commit-stadiumxl', 'commit-helixfloor', 'commit-vx5', 'commit-pedalboard', 'commit-gigboard', 'commit-pocketgt', 'commit-ve5', 'commit-rp1000', 'commit-gt6', 'commit-hxone', 'commit-pocketpod', 'commit-m9', 'commit-m5', 'commit-ax3g', 'commit-me20', 'commit-g71ut', 'commit-rp250', 'commit-ve20-followup', 'commit-gfx4', 'commit-ax1000g', 'commit-gfx5', 'commit-gfx3', 'commit-rp90', 'commit-ax10g', 'commit-rp500', 'commit-g21u', 'commit-g3x', 'commit-g5', 'commit-ms50gplus', 'commit-505ii', 'commit-ving-coverage', 'commit-ax5g', 'commit-rockstage', 'commit-dapper-indie', 'commit-dapper-dark-mini', 'commit-blackhammer', 'commit-flyrig5v2', 'commit-dapper-dark', 'commit-dapper-acoustic-mini', 'commit-dapper-mini', 'commit-dapper-bass-mini', 'commit-dapper-bass', 'commit-hd500', 'commit-g1on', 'commit-g1xon', 'commit-stomplab2g', 'commit-perform-ve', 'commit-stomplab1g', 'commit-perform-vg', 'commit-perform-vk', 'commit-perform-v', 'commit-stomplab2b', 'commit-tonelab-se', 'commit-tonelab-st', 'commit-tonelab-le', 'commit-ax1500g', 'commit-rp255', 'commit-gt8', 'commit-gt10', 'commit-me20b', 'commit-me50', 'commit-b2-followup', 'commit-ax3000g', 'commit-pandora', 'commit-vl3x', 'commit-b3', 'commit-g3', 'commit-me25', 'commit-rp360xp', 'commit-me70', 'commit-me80', 'commit-field-projection', 'commit-field-extraction', 'commit-pe100', 'commit-g3xn', 'commit-g3n', 'commit-b3n', 'commit-a1four', 'commit-a1xfour', 'commit-ms50g', 'commit-ms70cdr', 'commit-ms70cdrplus', 'commit-ms60bplus', 'commit-b1on', 'commit-ms60b', 'commit-g5n', 'commit-pod-express-guitar-preservation', 'commit-pod-express-bass-preservation', 'commit-g11-preservation', 'commit-arena-preservation', 'commit-fx100-preservation', 'commit-fx200-preservation', 'commit-core-preservation', 'commit-gembox-preservation', 'commit-gembox-ii-preservation', 'commit-gembox-iii-preservation', 'commit-podgo-preservation', 'commit-podgo-wireless-preservation', 'commit-tank-g-preservation', 'commit-tank-b-preservation', 'commit-tank-mini-preservation', 'commit-mk20-preservation', 'commit-mk300-preservation', 'commit-tankpro-preservation', 'commit-annblackbox-preservation', 'commit-minix-preservation', 'commit-pocketamp-preservation', 'commit-cubebabyac-preservation', 'commit-cubebabybass-preservation', 'commit-cubebabyelectric-preservation', 'commit-mg100-preservation', 'commit-mg200-preservation', 'commit-trident-preservation', 'commit-finding-audit', 'commit-legacy-audit', 'commit-nux-mg101-audit', 'commit-nux-mg300-audit', 'commit-nux-mg300mkii-audit', 'commit-nux-mg400-audit', 'commit-nux-mg30-audit', 'commit-nux-mg50li-audit', 'commit-nux-union', 'commit-bass-union', 'commit-vocal-union', 'commit-advanced-hxe-audit', 'commit-advanced-flex-audit', 'commit-advanced-union', 'commit-boss-union', 'commit-boss-history-union', 'commit-audota-union', 'commit-cube-union', 'commit-owned-union', 'commit-market1-union', 'commit-market7-union', 'commit-market6-union', 'commit-market5-union', 'commit-market4-union', 'commit-market3-union', 'commit-market2-union', 'commit-compact-union', 'commit-floorboard-union', 'commit-floorboard-matribox-ii', 'commit-floorboard-matribox-ii-pro', 'commit-compact-gp100-audit', 'commit-compact-gp150-audit', 'commit-compact-matribox-audit', 'commit-compact-gp5-audit', 'commit-compact-gp50-audit', 'commit-compact-gp180-audit', 'commit-compact-smartbox-audit', 'commit-compact-pocketmaster-audit'):
        verify()
        for check in ('test-fields', 'test-extraction', 'test-selection', 'verify'):
            subprocess.run([sys.executable, str(ROOT/'scripts/comparison_views.py'), check], check=True)
        assert not git('diff', '--cached', '--name-only').strip(), 'Existing staged changes'
        paths = ['Makefile', 'scripts/research_tools.py', 'scripts/comparison_views.py', 'ALL-GUITAR.md', 'ALL-BASS.md', 'ALL-VOCAL.md', 'README.md', 'research-state.json']
        if mode == 'commit-h9max':
            paths += ['EVENTIDE.md']
        if mode == 'commit-1201':
            paths += ['ZOOM.md']
        if mode == 'commit-vt4':
            paths += ['ROLAND.md']
        if mode == 'commit-ampero-one':
            paths += ['HOTONE.md']
        if mode == 'commit-katana-go':
            paths += ['BOSS.md']
        if mode == 'commit-microplus':
            paths += ['FENDER.md']
        if mode == 'commit-mg20':
            paths += ['NUX.md']
        if mode == 'commit-m100':
            paths += ['TC-ELECTRONIC.md']
        if mode == 'commit-hxe-price':
            paths += ['LINE6.md']
        if mode == 'commit-criticalmass':
            paths += ['TC-HELICON.md']
        if mode in ('commit-b21u', 'commit-rfx1100', 'commit-b1four-followup', 'commit-b1xfour-followup'):
            paths += ['ZOOM.md']
        if mode in ('commit-midiverb4', 'commit-microverb4'):
            paths += ['ALESIS.md']
        if mode == 'commit-fx2000':
            paths += ['BEHRINGER.md']
        if mode in ('commit-spx990', 'commit-spx900'):
            paths += ['YAMAHA.md']
        if mode == 'commit-mx200':
            paths += ['LEXICON.md']
        if mode == 'commit-gnx3':
            paths += ['DIGITECH.md']
        if mode == 'commit-r16':
            paths += ['JOYO.md', 'MULTI-EFFECTS.md']
        if mode in ('commit-fx50', 'commit-fg200', 'commit-fv04', 'commit-fv03', 'commit-fb200', 'commit-fv02'):
            paths += ['FLAMMA.md', 'MULTI-EFFECTS.md']
        if mode in ('commit-vx5', 'commit-pedalboard', 'commit-gigboard'):
            paths += ['HEADRUSH.md', 'MULTI-EFFECTS.md']
        if mode in ('commit-gt8', 'commit-gt10', 'commit-me20b', 'commit-me50'):
            paths += ['BOSS.md', 'MULTI-EFFECTS.md']
        if mode == 'commit-ve20-followup':
            paths += ['BOSS.md']
        if mode in ('commit-708ii', 'commit-707ii', 'commit-g71ut', 'commit-gfx4', 'commit-gfx5', 'commit-gfx3', 'commit-g21u', 'commit-g3x', 'commit-g5', 'commit-ms50gplus', 'commit-505ii'):
            paths += ['ZOOM.md', 'MULTI-EFFECTS.md']
        if mode == 'commit-b2-followup':
            paths += ['ZOOM.md']
        if mode in ('commit-ax30g', 'commit-ax3g', 'commit-ax1000g', 'commit-ax10g', 'commit-ax1500g', 'commit-ax3000g', 'commit-pandora'):
            paths += ['KORG.md', 'MULTI-EFFECTS.md']
        if mode in ('commit-harmony-singer2', 'commit-duplicator', 'commit-mic-mechanic2', 'commit-vl3x'):
            paths += ['TC-HELICON.md', 'MULTI-EFFECTS.md']
        if mode in ('commit-rp155', 'commit-rp1000', 'commit-rp250', 'commit-rp90', 'commit-rp500', 'commit-rp255', 'commit-rp360xp'):
            paths += ['DIGITECH.md', 'MULTI-EFFECTS.md']
        if mode in ('commit-pocketgt', 'commit-ve5', 'commit-gt6', 'commit-me20', 'commit-me25', 'commit-me70', 'commit-me80'):
            paths += ['BOSS.md', 'MULTI-EFFECTS.md']
        if mode in ('commit-dapper-indie', 'commit-dapper-dark-mini', 'commit-dapper-dark', 'commit-dapper-acoustic-mini', 'commit-dapper-mini', 'commit-dapper-bass', 'commit-dapper-bass-mini'):
            paths += ['VALETON.md', 'MULTI-EFFECTS.md']
        if mode == 'commit-flyrig5v2':
            paths += ['TECH21.md', 'MULTI-EFFECTS.md']
        if mode in ('commit-rockstage', 'commit-blackhammer'):
            paths += ['SONICAKE.md', 'MULTI-EFFECTS.md']
        if mode == 'commit-ving-coverage':
            paths += ['VING.md']
        if mode == 'commit-ax5g':
            paths += ['KORG.md', 'MULTI-EFFECTS.md']
        if mode in ('commit-vamp2', 'commit-bass-vamp-pro', 'commit-bass-vamp'):
            paths += ['BEHRINGER.md', 'MULTI-EFFECTS.md']
        if mode in ('commit-hd400', 'commit-xtlive', 'commit-x3live', 'commit-amplifi-fx100', 'commit-hd500x', 'commit-stadiumxl', 'commit-helixfloor', 'commit-hxone', 'commit-pocketpod', 'commit-m9', 'commit-m5', 'commit-hd500'):
            paths += ['LINE6.md', 'MULTI-EFFECTS.md']
        if mode == 'commit-pe100':
            paths += ['MOOER.md', 'MULTI-EFFECTS.md']
        if mode in ('commit-g1on', 'commit-g1xon', 'commit-b3', 'commit-g3', 'commit-g3xn', 'commit-g3n', 'commit-b3n', 'commit-a1four', 'commit-a1xfour', 'commit-ms50g', 'commit-ms70cdr', 'commit-ms70cdrplus', 'commit-ms60bplus', 'commit-b1on', 'commit-g5n', 'commit-ms60b'):
            paths += ['ZOOM.md', 'MULTI-EFFECTS.md']
        if mode in ('commit-pod-express-guitar-preservation', 'commit-pod-express-bass-preservation'):
            paths += ['LINE6.md']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'verify'], check=True)
        if mode == 'commit-g11-preservation':
            paths += ['ZOOM.md']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'verify'], check=True)
        if mode == 'commit-arena-preservation':
            paths += ['DONNER.md']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'verify'], check=True)
        if mode in ('commit-fx100-preservation', 'commit-fx200-preservation'):
            paths += ['FLAMMA.md']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'verify'], check=True)
        if mode == 'commit-core-preservation':
            paths += ['HEADRUSH.md']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'verify'], check=True)
        if mode in ('commit-gembox-preservation', 'commit-gembox-ii-preservation', 'commit-gembox-iii-preservation'):
            paths += ['JOYO.md']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'verify'], check=True)
        if mode in ('commit-podgo-preservation', 'commit-podgo-wireless-preservation'):
            paths += ['LINE6.md']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'verify'], check=True)
        if mode in ('commit-tank-g-preservation', 'commit-tank-b-preservation', 'commit-tank-mini-preservation', 'commit-mk20-preservation', 'commit-mk300-preservation', 'commit-tankpro-preservation', 'commit-annblackbox-preservation', 'commit-minix-preservation', 'commit-pocketamp-preservation', 'commit-cubebabyac-preservation', 'commit-cubebabybass-preservation', 'commit-cubebabyelectric-preservation'):
            paths += ['M-VAVE.md']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'verify'], check=True)
        if mode in ('commit-mg100-preservation', 'commit-mg200-preservation', 'commit-trident-preservation'):
            paths += ['NUX.md']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'verify'], check=True)
        if mode == 'commit-cubebabyelectric-preservation':
            paths += ['scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-findings'], check=True)
        if mode == 'commit-finding-audit':
            paths += ['scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-findings'], check=True)
        if mode in ('commit-floorboard-matribox-ii', 'commit-floorboard-matribox-ii-pro'):
            paths += ['SONICAKE.md', 'scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'verify'], check=True)
        if mode == 'commit-floorboard-union':
            paths += ['MULTI-EFFECTS.md', 'scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-floorboard-union'], check=True)
        if mode == 'commit-market2-union':
            paths += ["M-VAVE.md","BOIN-AUDIO.md","SCORPION.md","JOYO.md","TC-HELICON.md","MULTI-EFFECTS.md","scripts/consolidation_tools.py"]
            for audit in ('audit-market2-union', 'audit-market2-links', 'audit-market1-union', 'audit-owned-union', 'audit-cube-union'):
                subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), audit], check=True)
        if mode == 'commit-market3-union':
            paths += ["HEADRUSH.md","DONNER.md","NUX.md","MULTI-EFFECTS.md","scripts/consolidation_tools.py"]
            for audit in ('audit-market3-union', 'audit-market3-links', 'audit-market1-union', 'audit-owned-union', 'audit-cube-union'):
                subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), audit], check=True)
        if mode == 'commit-market4-union':
            paths += ["MOOER.md","MULTI-EFFECTS.md","scripts/consolidation_tools.py"]
            for audit in ('audit-market4-union', 'audit-market4-links', 'audit-market1-union', 'audit-owned-union', 'audit-cube-union'):
                subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), audit], check=True)
        if mode == 'commit-market5-union':
            paths += ["HOTONE.md","MOOER.md","LINE6.md","MULTI-EFFECTS.md","scripts/consolidation_tools.py"]
            for audit in ('audit-market5-union', 'audit-market5-links', 'audit-market1-union', 'audit-owned-union', 'audit-cube-union'):
                subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), audit], check=True)
        if mode == 'commit-market6-union':
            paths += ["MOOER.md","MULTI-EFFECTS.md","scripts/consolidation_tools.py"]
            for audit in ('audit-market6-union', 'audit-market6-links', 'audit-market1-union', 'audit-owned-union', 'audit-cube-union'):
                subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), audit], check=True)
        if mode == 'commit-market7-union':
            paths += ["NUX.md","ZOOM.md","HOTONE.md","LINE6.md","MULTI-EFFECTS.md","scripts/consolidation_tools.py"]
            for audit in ('audit-market7-union', 'audit-market7-links', 'audit-market1-union', 'audit-owned-union', 'audit-cube-union'):
                subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), audit], check=True)
        if mode == 'commit-market1-union':
            paths += ['M-VAVE.md', 'HOTONE.md', 'MOOER.md', 'ZOOM.md', 'FLAMMA.md', 'MULTI-EFFECTS.md', 'scripts/consolidation_tools.py']
            for audit in ('audit-market1-union', 'audit-market1-links', 'audit-owned-union', 'audit-cube-union'):
                subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), audit], check=True)
        if mode == 'commit-owned-union':
            paths += ['ROLAND.md', 'ZOOM.md', 'JOYO.md', 'M-VAVE.md', 'CUVAVE.md', 'VING.md', 'MULTI-EFFECTS.md', 'scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-owned-union'], check=True)
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-owned-links'], check=True)
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-cube-union'], check=True)
        if mode == 'commit-cube-union':
            paths += ['M-VAVE.md', 'MULTI-EFFECTS.md', 'scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-cube-union'], check=True)
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-cube-links'], check=True)
        if mode == 'commit-audota-union':
            paths += ['AUDOTA.md', 'MULTI-EFFECTS.md', 'scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-audota-union'], check=True)
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-audota-links'], check=True)
        if mode == 'commit-boss-history-union':
            paths += ['MULTI-EFFECTS.md', 'scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-boss-history-union'], check=True)
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-boss-history-links'], check=True)
        if mode == 'commit-boss-union':
            paths += ['MULTI-EFFECTS.md', 'scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-boss-union'], check=True)
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-boss-links'], check=True)
        if mode == 'commit-advanced-union':
            paths += ['MULTI-EFFECTS.md', 'scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-advanced-union'], check=True)
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-advanced-links'], check=True)
        if mode == 'commit-advanced-flex-audit':
            paths += ['HEADRUSH.md', 'scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'verify'], check=True)
        if mode == 'commit-advanced-hxe-audit':
            paths += ['LINE6.md', 'scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'verify'], check=True)
        if mode == 'commit-vocal-union':
            paths += ['MULTI-EFFECTS.md', 'scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-vocal-union'], check=True)
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-vocal-links'], check=True)
        if mode == 'commit-bass-union':
            paths += ['MULTI-EFFECTS.md', 'scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-bass-union'], check=True)
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-bass-links'], check=True)
        if mode == 'commit-nux-union':
            paths += ['MULTI-EFFECTS.md', 'scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-nux-union'], check=True)
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-nux-links'], check=True)
        if mode == 'commit-compact-union':
            paths += ['MULTI-EFFECTS.md', 'scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-compact-union'], check=True)
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-compact-links'], check=True)
        if mode in ('commit-nux-mg101-audit', 'commit-nux-mg300-audit', 'commit-nux-mg300mkii-audit', 'commit-nux-mg400-audit', 'commit-nux-mg30-audit', 'commit-nux-mg50li-audit'):
            paths += ['NUX.md', 'scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'verify'], check=True)
        if mode == 'commit-legacy-audit':
            paths += ['scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-legacy'], check=True)
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-findings'], check=True)
        if mode in ('commit-compact-gp100-audit', 'commit-compact-gp150-audit'):
            paths += ['VALETON.md', 'scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-compact', 'GP-150' if mode == 'commit-compact-gp150-audit' else 'GP-100'], check=True)
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'verify'], check=True)
        if mode == 'commit-compact-matribox-audit':
            paths += ['SONICAKE.md', 'scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-compact', 'Matribox'], check=True)
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'verify'], check=True)
        if mode in ('commit-compact-gp5-audit', 'commit-compact-gp50-audit'):
            paths += ['VALETON.md', 'scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-compact', 'GP-50' if mode == 'commit-compact-gp50-audit' else 'GP-5'], check=True)
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'verify'], check=True)
        if mode == 'commit-compact-gp180-audit':
            paths += ['VALETON.md', 'scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-compact', 'GP-180'], check=True)
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'verify'], check=True)
        if mode in ('commit-compact-smartbox-audit', 'commit-compact-pocketmaster-audit'):
            paths += ['SONICAKE.md', 'scripts/consolidation_tools.py']
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'audit-compact', 'Pocket Master' if mode == 'commit-compact-pocketmaster-audit' else 'Smart Box'], check=True)
            subprocess.run([sys.executable, str(ROOT/'scripts/consolidation_tools.py'), 'verify'], check=True)
        if mode in ('commit-perform-ve', 'commit-perform-vg', 'commit-perform-vk', 'commit-perform-v'):
            paths += ['TC-HELICON.md', 'MULTI-EFFECTS.md']
        if mode in ('commit-stomplab2g', 'commit-stomplab1g', 'commit-stomplab2b', 'commit-tonelab-se', 'commit-tonelab-st', 'commit-tonelab-le'):
            paths += ['VOX.md', 'MULTI-EFFECTS.md']
        changed = set(git('diff', '--name-only').splitlines())
        assert changed <= set(paths), changed - set(paths)
        git('add', '--', *paths)
        print(git('diff', '--cached', '--stat'))
        message = 'fix(comparisons): preserve separate technical source columns' if mode == 'commit-field-extraction' else 'fix(comparisons): retain USB control and live operation evidence'
        if mode == 'commit-ampero-one':
            message = 'research(hotone): corroborate MP-350 loop controls and preserve serial conflict'
        if mode == 'commit-nux-mg50li-audit':
            message = 'audit(nux): preserve MG-50Li shared fields and conflicting source counts'
        if mode == 'commit-nux-mg30-audit':
            message = 'research(nux): verify MG-30 editable preset memory and regional model counts'
        if mode == 'commit-nux-mg400-audit':
            message = 'audit(nux): preserve MG-400 shared fields and historical firmware scope'
        if mode == 'commit-nux-mg300mkii-audit':
            message = 'research(nux): preserve MKII calibration conflict and IR routing limits'
        if mode == 'commit-nux-mg300-audit':
            message = 'research(nux): document original MG-300 output and calibration modes'
        if mode == 'commit-nux-mg101-audit':
            message = 'audit(nux): preserve MG-101 source evidence and verification tooling'
        if mode == 'commit-h9max':
            message = 'research(eventide): verify H90 snapshots and performance control limits'
        if mode == 'commit-1201':
            message = 'research(zoom): verify RFX-2200 analog levels and impedances'
        if mode == 'commit-vt4':
            message = 'research(roland): verify VT-4 output balance and USB processing constraints'
        if mode == 'commit-pe100':
            message = 'research(mooer): preserve second exact PE100 historical hardware ask'
        if mode == 'commit-ms60b':
            message = 'research(zoom): verify MS-60B patch saving tempo and internal routing'
        if mode == 'commit-rp360xp':
            message = 'research(digitech): distinguish RP360XP model and Direct choice counts'
        if mode == 'commit-perform-ve':
            message = 'research(tc-helicon): restore PERFORM-VE routing conflicts and qualified offer coverage'
        if mode == 'commit-perform-vg':
            message = 'research(tc-helicon): add qualified PERFORM-VG preorder observation'
        if mode == 'commit-perform-vk':
            message = 'research(tc-helicon): qualify Perform VK keyboard split and transpose scope'
        if mode == 'commit-perform-v':
            message = 'research(tc-helicon): restore PERFORM-V conflicts remote rules and offer in comparisons'
        if mode == 'commit-dapper-indie':
            message = 'research(valeton): clarify Indie fields and reconcile recorded discovery status'
        if mode == 'commit-dapper-dark-mini':
            message = 'research(valeton): add separate Dark Mini with indexed-manual qualifications'
        if mode == 'commit-rp500':
            message = 'research(digitech): verify RP500 electrical and USB specifications'
        if mode == 'commit-g21u':
            message = 'research(zoom): qualify G2.1u USB monitoring and global switch functions'
        if mode == 'commit-r16':
            message = 'research(joyo): add R-16 vocal processor with source conflicts and qualified offers'
        if mode == 'commit-fx50':
            message = 'research(flamma): add FX50 with explicit manual and seller variation limits'
        if mode == 'commit-fg200':
            message = 'fix(comparisons): retain firmware qualifications beside model counts'
        if mode == 'commit-fv04':
            message = 'research(flamma): add FV04 vocal harmony with qualified source and price limits'
        if mode == 'commit-fv03':
            message = 'research(flamma): add FV03 vocal processor with revision-qualified power conflicts'
        if mode == 'commit-fb200':
            message = 'research(flamma): add FB200 bass processor with charging and mapping limits'
        if mode == 'commit-fv02':
            message = 'research(flamma): add FV02 vocal processor with power revision conflicts'
        if mode == 'commit-midiverb4':
            message = 'research(alesis): qualify MIDIverb III configuration and delay limits'
        if mode == 'commit-microverb4':
            message = 'research(alesis): document MicroVerb 4 tap control and display terminology conflict'
        if mode == 'commit-fx2000':
            message = 'research(behringer): resolve FX2000 numbered control and connector inventory'
        if mode == 'commit-hxe-price':
            message = 'research(line6): qualify HX Effects controller and stereo behavior'
        if mode == 'commit-criticalmass':
            message = 'research(tchelicon): clarify Critical Mass control combinations'
        if mode == 'commit-b21u':
            message = 'research(zoom): qualify B2.1u synth tracking and dry-path routing'
        if mode == 'commit-katana-go':
            message = 'research(boss): verify GT-1 battery fallback and backup scope'
        if mode == 'commit-microplus':
            message = 'research(fender): qualify original Micro firmware and updater platforms'
        if mode == 'commit-mg20':
            message = 'research(nux): clarify Cerberus V5 footswitch and expression assignments'
        if mode == 'commit-m100':
            message = 'research(tc-electronic): reconcile Plethora X3 controls and latency'
        if mode == 'commit-rfx1100':
            message = 'research(zoom): enumerate RFX-1000 banks and qualify combined delay limits'
        if mode == 'commit-spx990':
            message = 'research(yamaha): qualify REV500 topologies editing and MIDI map limits'
        if mode == 'commit-spx900':
            message = 'research(yamaha): add SPX900 with original manual and qualified line-level scope'
        if mode == 'commit-mx200':
            message = 'research(lexicon): reconcile MPX100 banks and preserve delay conflict'
        if mode == 'commit-gnx3':
            message = 'research(digitech): document GNX4 channel EQ and cabinet tuning ranges'
        if mode == 'commit-b1four-followup':
            message = 'research(zoom): preserve separate B1 FOUR cveri cached hardware ask'
        if mode == 'commit-b1xfour-followup':
            message = 'research(zoom): resolve B1X FOUR display memory and looper qualifications'
        if mode == 'commit-readme-counts':
            message = 'fix(navigation): synchronize complete brand model lists from ledger'
        if mode == 'commit-hd400':
            message = 'research(line6): clarify HD400 USB recording and monitoring'
        if mode == 'commit-xtlive':
            message = 'research(line6): qualify XT Live Silicon support and discontinued updater'
        if mode == 'commit-x3live':
            message = 'research(line6): qualify X3 Live Silicon support and updater restrictions'
        if mode == 'commit-harmony-singer2':
            message = 'research(tc-helicon): corroborate Harmony Singer 2 guide from manufacturer index'
        if mode == 'commit-duplicator':
            message = 'research(tc-helicon): add Duplicator with model-specific bypass and source conflicts'
        if mode == 'commit-mic-mechanic2':
            message = 'research(tc-helicon): add Mic Mechanic 2 and preserve phantom power conflicts'
        if mode == 'commit-708ii':
            message = 'research(zoom): reconcile 708II category counts and qualify hold delay'
        if mode == 'commit-707ii':
            message = 'research(zoom): reconcile 707II effect counts and separate sampler from hold delay'
        if mode == 'commit-ax30g':
            message = 'research(korg): complete AX100G pedal choices and adapter compatibility'
        if mode == 'commit-rp155':
            message = 'research(digitech): qualify RP70 power digital ports and software support'
        if mode == 'commit-vamp2':
            message = 'research(behringer): preserve preliminary V-AMP 3 brochure conflicts'
        if mode == 'commit-bass-vamp-pro':
            message = 'research(behringer): document Bass V-AMP PRO MIDI backup and control limits'
        if mode == 'commit-bass-vamp':
            message = 'research(behringer): clarify Bass V-AMP dry routing and cabinet selection'
        if mode == 'commit-amplifi-fx100':
            message = 'research(line6): verify FX100 synth wah and music routing details'
        if mode == 'commit-hd500x':
            message = 'research(line6): add distinct POD HD500X with own manual and qualified offers'
        if mode == 'commit-stadiumxl':
            message = 'research: save discovery cursor compatible with comparison generation'
        if mode == 'commit-helixfloor':
            message = 'research(line6): verify Helix Floor loop limits and improve record readability'
        if mode == 'commit-vx5':
            message = 'research(headrush): qualify VX5 harmony choices and conflicting firmware notes'
        if mode == 'commit-pedalboard':
            message = 'research(headrush): verify Pedalboard looper revisions and routing restrictions'
        if mode == 'commit-gigboard':
            message = 'research(headrush): reconcile Gigboard firmware categories and factory rigs'
        if mode == 'commit-pocketgt':
            message = 'research(boss): audit Pocket GT memory categories and explicit bass presets'
        if mode == 'commit-ve5':
            message = 'research(boss): separate VE-5 red hardware ask from unresolved variants'
        if mode == 'commit-rp1000':
            message = 'research(digitech): enumerate RP1000 amp cabinet and shared FX choices'
        if mode == 'commit-gt6':
            message = 'research(boss): preserve separate GT5 cached hardware offer'
        if mode == 'commit-hxone':
            message = 'research(line6): clarify HX One impedance bypass and preset queue'
        if mode == 'commit-pocketpod':
            message = 'research(line6): qualify Pocket POD combo tuner and save behavior'
        if mode == 'commit-m9':
            message = 'research(line6): qualify M9 knob scene and DryThru behavior'
        if mode == 'commit-m5':
            message = 'research(line6): enumerate M5 models and document bass suitability'
        if mode == 'commit-ax3g':
            message = 'research(korg): reconcile AX3G algorithms and distinguish drone from synth'
        if mode == 'commit-ax1000g':
            message = 'research(korg): preserve second AX1000G sold-out offer separately'
        if mode == 'commit-ve20-followup':
            message = 'research(boss): qualify VE20 pitch modes and indexed offer context'
        if mode == 'commit-g71ut':
            message = 'research(zoom): reconcile G7.1ut category inventory to 92 effects'
        if mode == 'commit-field-projection':
            message = 'test(comparisons): reject unclassified catalogue evidence before rendering'
        if mode == 'commit-gfx4':
            message = 'research(zoom): document GFX-4 hold delay and conditional continuation'
        if mode == 'commit-gfx5':
            message = 'research(zoom): qualify GFX-5 expression routing and ARRM conflicts'
        if mode == 'commit-gfx3':
            message = 'research(zoom): qualify GFX-3 pedal tuner and mixed-variant offer'
        if mode == 'commit-rp250':
            message = 'research(digitech): enumerate RP250 categories and preserve ChorusFX gaps'
        if mode == 'commit-rp90':
            message = 'research(digitech): verify RP70 electrical and practice specifications'
        if mode == 'commit-ax10g':
            message = 'research(korg): qualify AX10B Japanese adapter and NR evidence'
        if mode == 'commit-g3x':
            message = 'research(zoom): verify G3X synth DSP and expression qualifications'
        if mode == 'commit-g5':
            message = 'research(zoom): qualify G5 controls looper and tube-booster restrictions'
        if mode == 'commit-ms50gplus':
            message = 'research(zoom): reconcile B1X FOUR library categories and amp cabinet choices'
        if mode == 'commit-505ii':
            message = 'research(zoom): enumerate 505II category modes without inflating algorithm totals'
        if mode == 'commit-ving-coverage':
            message = 'research(ving): preserve seller and app identity qualifications in comparison rows'
        if mode == 'commit-ax5g':
            message = 'research(korg): clarify AX5G six-effect accounting and amp-only output targets'
        if mode == 'commit-rockstage':
            message = 'research(sonicake): qualify RockStage regional corroboration and manual limits'
        if mode == 'commit-blackhammer':
            message = 'research(sonicake): add Black Hammer QCE-30 with qualified manufacturer evidence'
        if mode == 'commit-flyrig5v2':
            message = 'research(tech21): preserve revision-unresolved used RK5 offer and power distinctions'
        if mode == 'commit-dapper-dark':
            message = 'research(valeton): qualify Dapper Dark indexed controls and loop routing'
        if mode == 'commit-dapper-acoustic-mini':
            message = 'research(valeton): preserve Acoustic Mini historical Semarang offer'
        if mode == 'commit-dapper-mini':
            message = 'research(valeton): retain Amp Mini parameter and amp model evidence'
        if mode == 'commit-dapper-bass-mini':
            message = 'research(valeton): corroborate MES-2 manual and clarify comparison record'
        if mode == 'commit-dapper-bass':
            message = 'research(valeton): verify Dapper Bass controls and routing qualifications'
        if mode == 'commit-hd500':
            message = 'research(line6): qualify HD500 global EQ and firmware editor fixes'
        if mode == 'commit-g1on':
            message = 'research(zoom): verify G1on controls routing and looper limits'
        if mode == 'commit-g1xon':
            message = 'research(zoom): reconcile G1Xon library counts and acoustic algorithm'
        if mode == 'commit-stomplab2g':
            message = 'research(vox): restore StompLab 2G pedal storage limits and qualified offer coverage'
        if mode == 'commit-stomplab1g':
            message = 'research(vox): restore StompLab 1G output behavior and price qualifications in comparisons'
        if mode == 'commit-stomplab2b':
            message = 'research(vox): preserve StompLab 2B sold-out variant and voucher ambiguity'
        if mode == 'commit-tonelab-se':
            message = 'research(vox): preserve ToneLab EX height conflict and reconcile effect totals'
        if mode == 'commit-tonelab-st':
            message = 'research(vox): include qualified ToneLab ST historical offer in comparison'
        if mode == 'commit-tonelab-le':
            message = 'research(vox): clarify ToneLab EX save scope and total equalizer'
        if mode == 'commit-ax1500g':
            message = 'research(korg): preserve separate AX1500G condition-unverified offers'
        if mode == 'commit-rp255':
            message = 'research(digitech): include qualified RP255 historical hardware offer in comparison'
        if mode == 'commit-gt8':
            message = 'research(boss): verify GT-8 category choices shared custom settings and MIDI backups'
        if mode == 'commit-gt10':
            message = 'research(boss): qualify GT-10 preamp enumeration and drive count discrepancy'
        if mode == 'commit-me20b':
            message = 'research(boss): verify ME20B electrical levels and patch master'
        if mode == 'commit-me50':
            message = 'research(boss): verify ME-50 named controls and toe-switch calibration'
        if mode == 'commit-b2-followup':
            message = 'research(zoom): qualify B2 FOUR dated macOS and DAW compatibility'
        if mode == 'commit-ax3000g':
            message = 'research(korg): preserve qualified AX3000G second-title historical offer'
        if mode == 'commit-pandora':
            message = 'research(korg): qualify Pandora stomp oscillator and filter controls'
        if mode == 'commit-vl3x':
            message = 'research(tc-helicon): preserve VL3X exact offer and conflicting cache prices'
        if mode == 'commit-b3':
            message = 'research(zoom): qualify B3 tuner bypass mute and eco standby'
        if mode == 'commit-g3':
            message = 'research(zoom): document G3 battery settings eco behavior and tuner modes'
        if mode == 'commit-me20':
            message = 'research(boss): qualify ME-20 routing memory controls and tuner output'
        if mode == 'commit-me25':
            message = 'research(boss): qualify ME-25 library software and converter specifications'
        if mode == 'commit-me70':
            message = 'research(boss): qualify ME-70 groups loop stopping and catalogue dimensions'
        if mode == 'commit-me80':
            message = 'research(boss): resolve ME-80 buttons battery mass and loop erasure'
        if mode == 'commit-b1on':
            message = 'research(zoom): verify original B1X electrical and rhythm specifications'
        if mode == 'commit-ms60bplus':
            message = 'research(zoom): add bass-focused MS-60B Plus with own routing and qualified offer'
        if mode == 'commit-ms70cdrplus':
            message = 'research(zoom): add MS-70CDR Plus with own bass presets MIDI and qualified offer'
        if mode == 'commit-ms70cdr':
            message = 'research(zoom): add original MS-70CDR with revision conflicts and qualified Shopee ask'
        if mode == 'commit-ms50g':
            message = 'research(zoom): add original MS-50G and retain firmware library and offer conflicts'
        if mode == 'commit-a1xfour':
            message = 'research(zoom): verify A1X FOUR toe controls DSP limits and patch saving'
        if mode == 'commit-a1four':
            message = 'research(zoom): document A1 FOUR synth algorithms and additional-effect scope'
        if mode == 'commit-b3n':
            message = 'research(zoom): qualify B3n pedal setup and additional IDR offers'
        if mode == 'commit-g3n':
            message = 'research(zoom): verify G3n external expression enable path'
        if mode == 'commit-g5n':
            message = 'research(zoom): establish G5n acoustic simulation and qualify synth-style presets'
        if mode == 'commit-g3xn':
            message = 'research(zoom): document G3Xn pedal calibration and patch preselection'
        if mode == 'commit-pod-express-guitar-preservation':
            message = 'fix(line6): restore complete POD Express Guitar provenance and dimensions'
        if mode == 'commit-pod-express-bass-preservation':
            message = 'fix(line6): restore complete POD Express Bass evidence and historical offer'
        if mode == 'commit-g11-preservation':
            message = 'fix(zoom): preserve complete G11 original evidence and count qualifications'
        if mode == 'commit-arena-preservation':
            message = 'research(donner): include documented Arena2000 bass processing'
        if mode == 'commit-fx100-preservation':
            message = 'research(flamma): retain FX100 original and qualify mass and USB evidence'
        if mode == 'commit-fx200-preservation':
            message = 'research(flamma): preserve FX200 source and qualify versioned routing'
        if mode == 'commit-core-preservation':
            message = 'research(headrush): preserve Core original and document routing and clone limits'
        if mode == 'commit-gembox-preservation':
            message = 'research(joyo): preserve original GEM BOX finding and clarify digital and tuner fields'
        if mode == 'commit-gembox-ii-preservation':
            message = 'docs(joyo): verify GEM BOX II original and qualify overdub evidence'
        if mode == 'commit-gembox-iii-preservation':
            message = 'research(joyo): verify GEM BOX III dimensions and retain regional IR conflict'
        if mode == 'commit-podgo-preservation':
            message = 'research(line6): preserve standard POD Go and specify IR conversion limits'
        if mode == 'commit-podgo-wireless-preservation':
            message = 'fix(line6): isolate Wireless operation and preserve complete POD Go Wireless finding'
        if mode == 'commit-tank-g-preservation':
            message = 'research(mvave): preserve TANK-G original and qualify converted-model firmware'
        if mode == 'commit-tank-b-preservation':
            message = 'research(mvave): preserve three qualified TANK-B asking-price observations'
        if mode == 'commit-tank-mini-preservation':
            message = 'research(mvave): preserve TANK MINI source and qualify app and firmware limits'
        if mode == 'commit-mk20-preservation':
            message = 'research(mvave): preserve MK-20 source and qualify A2 software evidence'
        if mode == 'commit-mk300-preservation':
            message = 'research(mvave): preserve MK-300 source and qualify firmware and stereo evidence'
        if mode == 'commit-tankpro-preservation':
            message = 'research(mvave): preserve TANK-PRO original and qualify A2 app evidence'
        if mode == 'commit-annblackbox-preservation':
            message = 'research(mvave): preserve ANN Blackbox source and qualify firmware identity'
        if mode == 'commit-minix-preservation':
            message = 'research(mvave): preserve MINI-X source and expose comparison field limits'
        if mode == 'commit-pocketamp-preservation':
            message = 'research(mvave): qualify Pocket Amp native NAM A2 by firmware and preserve source'
        if mode == 'commit-cubebabyac-preservation':
            message = 'research(mvave): preserve CUBE BABY AC and separate comparison evidence fields'
        if mode == 'commit-cubebabyelectric-preservation':
            message = 'audit(mvave): preserve electric CUBE BABY original and check actual finding coverage'
        if mode == 'commit-cubebabybass-preservation':
            message = 'research(mvave): document CUBE BABY BASS save volume and editor behavior'
        if mode == 'commit-mg100-preservation':
            message = 'research(nux): preserve MG-100 source and retain official reverb conflict'
        if mode == 'commit-mg200-preservation':
            message = 'docs(nux): preserve MG-200 complete source and comparison qualifications'
        if mode == 'commit-trident-preservation':
            message = 'research(nux): preserve TRIDENT original and qualify USB and loop routing'
        if mode == 'commit-finding-audit':
            message = 'audit: reconcile B1Xon and verify registered finding-body coverage'
        if mode == 'commit-floorboard-matribox-ii-pro':
            message = 'research(sonicake): qualify Matribox II Pro firmware effects and Clone support'
        if mode == 'commit-floorboard-matribox-ii':
            message = 'research(sonicake): preserve Matribox II electrical specifications and output conflict'
        if mode == 'commit-floorboard-union':
            message = 'docs: restore original floorboard manual URL and diagnose shared-source gaps'
        if mode == 'commit-market2-union':
            message = 'audit: preserve complete second Shopee expansion shared comparison and qualifications'
        if mode == 'commit-market3-union':
            message = 'audit: preserve complete third Shopee expansion shared comparison and qualifications'
        if mode == 'commit-market4-union':
            message = 'audit: preserve complete fourth Shopee expansion shared comparison and qualifications'
        if mode == 'commit-market5-union':
            message = 'audit: preserve complete fifth Shopee expansion shared comparison and qualifications'
        if mode == 'commit-market6-union':
            message = 'audit: preserve complete sixth Shopee expansion shared comparison and qualifications'
        if mode == 'commit-market7-union':
            message = 'audit: preserve complete seventh Shopee expansion shared comparison and qualifications'
        if mode == 'commit-market1-union':
            message = 'docs: restore FX200 historical count conflict and verify source preservation'
        if mode == 'commit-owned-union':
            message = 'docs: restore B1Xon historical commit provenance in owned summary'
        if mode == 'commit-cube-union':
            message = 'audit(mvave): preserve all Cube Baby shared rows and historical qualifications'
        if mode == 'commit-audota-union':
            message = 'audit(audota): verify shared source union and preserve appendix and scope context'
        if mode == 'commit-boss-history-union':
            message = 'audit(boss): verify original historical source and preserve price provenance'
        if mode == 'commit-boss-union':
            message = 'audit(boss): preserve shared qualifications and verify complete current source union'
        if mode == 'commit-advanced-union':
            message = 'audit: verify advanced-modeler source union and incoming navigation'
        if mode == 'commit-advanced-flex-audit':
            message = 'audit(headrush): preserve exact Flex Prime shared-source fields'
        if mode == 'commit-advanced-hxe-audit':
            message = 'audit(line6): preserve exact HX Effects shared-source history'
        if mode == 'commit-vocal-union':
            message = 'audit(vocal): preserve shared source context and verify root content union'
        if mode == 'commit-bass-union':
            message = 'audit(bass): preserve shared source context and verify root content union'
        if mode == 'commit-nux-union':
            message = 'docs(nux): restore exact MG-101 source image timestamps'
        if mode == 'commit-compact-union':
            message = 'docs: restore exact compact-source URLs and diagnose floorboard preservation'
        if mode == 'commit-legacy-audit':
            message = 'audit: inventory legacy source hashes and incoming Markdown references'
        if mode == 'commit-compact-gp100-audit':
            message = 'audit(valeton): verify GP-100 shared rows and retain availability conflict'
        if mode == 'commit-compact-gp150-audit':
            message = 'audit(valeton): verify GP-150 shared rows and resolve provenance labels'
        if mode == 'commit-compact-matribox-audit':
            message = 'research(sonicake): document Matribox live control and expression limits'
        if mode == 'commit-compact-gp5-audit':
            message = 'audit(valeton): verify GP-5 shared source and resolve historical references'
        if mode == 'commit-compact-gp50-audit':
            message = 'audit(valeton): verify GP-50 shared fields and resolve provenance sources'
        if mode == 'commit-compact-gp180-audit':
            message = 'audit(valeton): verify GP-180 shared provenance and preserve version distinctions'
        if mode == 'commit-compact-smartbox-audit':
            message = 'research(sonicake): document Smart Box converted NAM A2 support'
        if mode == 'commit-compact-pocketmaster-audit':
            message = 'research(sonicake): preserve qualified Pocket Master Shopee offers'
        print(git('commit', '-m', message))
    elif mode == 'verify':
        verify()
    elif mode == 'restore-archive-provenance':
        state=json.loads((ROOT/'research-state.json').read_text())
        import hashlib
        state['separate_specialist_archives']['source_before_move_sha256']={p:hashlib.sha256(git('show','9c8d296:'+p).encode()).hexdigest() for p in ('effects/specialist.md','effects/findings/2026-10-14-flamma-fv01.md')}
        (ROOT/'research-state.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
        verify()
    elif mode == 'source-b2-controls':
        url='https://zoomcorp.com/media/original_images/Hero_1_0EAQFMB.png.768x0_q60_focal_area-825%2C633%2C1650%2C1267.png'
        with urllib.request.urlopen(url,timeout=40) as response:
            data=response.read()
        assert data.startswith(b'\x89PNG')
        path=Path('/tmp/instrumentfx-sources/b2-four-official-controls.png')
        path.parent.mkdir(exist_ok=True)
        path.write_bytes(data)
        print('Saved official control photograph: '+str(path))
    elif mode == 'source-gs1000':
        url='https://media.rockboard.de/Artikell_PDF/Manual_PDF/Mooer/EN/ME_GS1000_Manual_EN.pdf'
        cache=Path('/tmp/instrumentfx-sources')
        cache.mkdir(exist_ok=True)
        path=cache/'mooer-gs1000-original.pdf'
        with urllib.request.urlopen(url,timeout=60) as response:
            data=response.read()
        assert data.startswith(b'%PDF')
        path.write_bytes(data)
        subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],check=True)
        subprocess.run(['pdftoppm','-f','8','-l','10','-scale-to','1600','-png',str(path),str(cache/'gs1000-panel')],check=True)
        print('Saved manufacturer manual and rendered controls/connections: '+str(path))
    elif mode == 'gp200jr':
        gp200jr()
    elif mode == 'render-gp200jr':
        subprocess.run(['pdftoppm', '-f', '5', '-l', '6', '-scale-to', '1800', '-png', '/tmp/instrumentfx-sources/gp-200jr-v1.8.0.pdf', '/tmp/instrumentfx-sources/gp200jr-panel'], check=True)
    elif mode in ('source-prime','source-ge300'):
        cache=Path('/tmp/instrumentfx-sources')
        cache.mkdir(exist_ok=True)
        prime=mode=='source-prime'
        path=cache/('headrush-prime-v5.2.pdf' if prime else 'mooer-ge300-original.pdf')
        url='https://cdn.inmusicbrands.com/Software/SGEE/52/HeadRush%20Prime%20-%20User%20Guide%20-%20v5.2.0.pdf' if prime else 'https://media.rockboard.de/Artikell_PDF/Manual_PDF/Mooer/EN/ME_GE_300_Manual_EN.pdf'
        with urllib.request.urlopen(url,timeout=60) as response:
            data=response.read()
        assert data.startswith(b'%PDF')
        path.write_bytes(data)
        subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],check=True)
        subprocess.run(['pdftoppm','-f','6','-l','7','-scale-to','1600','-png',str(path),str(cache/('prime-panel' if prime else 'ge300-panel'))],check=True)
        print('Saved and rendered original manufacturer manual: '+str(path))
    elif mode in ('commit-gp150-nam','commit-gp100-nam'):
        verify()
        subprocess.run(['python3',str(ROOT/'scripts/comparison_views.py'),'verify'],check=True)
        assert not git('diff','--cached','--name-only').strip(), 'Existing staged changes must be inspected'
        paths=['VALETON.md','research-state.json','ALL-GUITAR.md','ALL-BASS.md','ALL-VOCAL.md','Makefile','scripts/research_tools.py']
        print(git('status','--short'))
        print(git('add','--',*paths))
        print(git('diff','--cached','--stat'))
        print(git('commit','-m','research(valeton): document GP-100 NAM A2 conversion requirements' if mode == 'commit-gp100-nam' else 'research(valeton): qualify GP-150 native NAM A2 Lite by firmware'))
    elif mode in ('commit-gp200jr', 'commit-hx-effects', 'commit-comparisons', 'commit-prime','commit-ge300','commit-gs1000','commit-b1xon','commit-helix-lt','commit-gt100'):
        verify()
        print(git('status', '--short', '--branch'))
        assert not git('diff', '--cached', '--name-only').strip(), 'Unrelated staged changes; inspect before committing'
        paths = ['Makefile', 'scripts/research_tools.py', 'ALL-GUITAR.md', 'ALL-BASS.md', 'MULTI-EFFECTS.md', 'README.md', 'research-state.json']
        if mode in ('commit-comparisons','commit-prime','commit-ge300','commit-gs1000','commit-b1xon','commit-helix-lt','commit-gt100'):
            paths += ['ALL-VOCAL.md','scripts/comparison_views.py','AGENTS.md','SINGLE-GUITAR.md','SINGLE-BASS.md','SINGLE-VOCAL.md','effects/specialist.md','effects/findings/2026-10-14-flamma-fv01.md']
            subprocess.run(['python3',str(ROOT/'scripts/comparison_views.py'),'verify'],check=True)
            if mode=='commit-prime':
                paths.append('HEADRUSH.md')
            elif mode in ('commit-ge300','commit-gs1000'):
                paths.append('MOOER.md')
            elif mode=='commit-b1xon':
                paths.append('ZOOM.md')
            elif mode=='commit-helix-lt':
                paths.append('LINE6.md')
            elif mode=='commit-gt100':
                paths.append('BOSS.md')
        else:
            paths.append('VALETON.md' if mode == 'commit-gp200jr' else 'LINE6.md')
        print(git('add', '--', *paths))
        print(git('diff', '--cached', '--stat'))
        if mode == 'commit-hx-effects':
            subprocess.run([sys.executable,str(ROOT/'scripts/comparison_views.py'),'verify'],check=True)
        subject = 'research(valeton): clarify GP-200 controls and tuner output modes' if mode == 'commit-gp200jr' else 'research(line6): verify HX Effects3.80 acoustic simulation and looper limits'
        if mode=='commit-comparisons':
            subject='fix(comparisons): synchronize category inventory count and reject stale introductions'
        elif mode=='commit-prime':
            subject='research(headrush): add Prime with native NAM limits and qualified used retail evidence'
        elif mode=='commit-ge300':
            subject='research(mooer): preserve Red Truck manual supply-version differences'
        elif mode=='commit-gs1000':
            subject='research(mooer): add GS1000 across guitar bass and live mic comparisons'
        elif mode=='commit-b1xon':
            subject='docs(zoom): consolidate complete B1Xon owner-history record'
        if mode=='commit-helix-lt':
            subject='research(line6): add Helix LT with dated specifications and qualified hardware offer'
        if mode=='commit-gt100':
            subject='research(boss): add GT-100 with version-qualified specifications and sold-out offers'
        print(git('commit', '-m', subject))
    else:
        raise SystemExit('Unknown operation')

if __name__ == '__main__':
    main()
