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
        preserved=(ROOT/'ZOOM.md').read_text().split('<!-- B1Xon preserved source begins -->\n',1)[1].split('<!-- B1Xon preserved source ends -->',1)[0]
        assert preserved.replace('\n### ','\n## ').replace('(effects/OWNERSHIP.md)','(../OWNERSHIP.md)')==original,'B1Xon consolidation lost source material'
    if state.get('separate_specialist_archives'):
        original=git('show','9c8d296:effects/specialist.md')
        marker='## Excluded archive — not part of the multi-effects comparison'
        preserved=(ROOT/'SINGLE-GUITAR.md').read_text().split(marker,1)[1].replace('[SCOPE.md](effects/SCOPE.md)','[SCOPE.md](SCOPE.md)')
        assert original.split(marker,1)[1]==preserved,'Guitar archive lost original material'
        original_fv=git('show','9c8d296:effects/findings/2026-10-14-flamma-fv01.md')
        body=(ROOT/'SINGLE-VOCAL.md').read_text().split('## Flamma FV01 Corrector\n',1)[1]
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
    elif mode == 'commit-discovery':
        verify()
        assert not git('diff', '--cached', '--name-only').strip(), 'Existing staged changes'
        paths = ['research-state.json', 'Makefile', 'scripts/research_tools.py']
        changed = set(git('diff', '--name-only').splitlines())
        assert changed <= set(paths), changed - set(paths)
        git('add', '--', *paths)
        print(git('diff', '--cached', '--stat'))
        print(git('commit', '-m', 'research: save exact Shopee discovery leads and qualification limits'))
    elif mode in ('commit-katana-go', 'commit-microplus', 'commit-mg20', 'commit-m100', 'commit-hxe-price', 'commit-criticalmass', 'commit-b21u', 'commit-rfx1100', 'commit-spx990', 'commit-spx900', 'commit-midiverb4', 'commit-microverb4', 'commit-fx2000', 'commit-mx200', 'commit-gnx3', 'commit-b1four-followup', 'commit-b1xfour-followup', 'commit-r16', 'commit-fx50', 'commit-fg200', 'commit-fv04', 'commit-fv03', 'commit-fb200', 'commit-fv02', 'commit-readme-counts', 'commit-hd400', 'commit-xtlive', 'commit-x3live', 'commit-harmony-singer2', 'commit-duplicator', 'commit-mic-mechanic2', 'commit-708ii', 'commit-707ii', 'commit-ax30g', 'commit-rp155', 'commit-vamp2', 'commit-bass-vamp-pro', 'commit-bass-vamp', 'commit-amplifi-fx100', 'commit-hd500x', 'commit-stadiumxl', 'commit-helixfloor', 'commit-vx5', 'commit-pedalboard', 'commit-gigboard', 'commit-pocketgt', 'commit-ve5', 'commit-rp1000', 'commit-gt6', 'commit-hxone', 'commit-pocketpod', 'commit-m9', 'commit-m5', 'commit-ax3g', 'commit-me20', 'commit-g71ut', 'commit-rp250', 'commit-ve20-followup', 'commit-gfx4', 'commit-ax1000g', 'commit-gfx5', 'commit-gfx3', 'commit-rp90', 'commit-ax10g', 'commit-rp500', 'commit-g21u', 'commit-g3x', 'commit-g5', 'commit-ms50gplus', 'commit-505ii', 'commit-ving-coverage', 'commit-ax5g', 'commit-rockstage', 'commit-dapper-indie', 'commit-dapper-dark-mini', 'commit-blackhammer', 'commit-flyrig5v2', 'commit-dapper-dark', 'commit-dapper-acoustic-mini', 'commit-dapper-mini', 'commit-dapper-bass-mini', 'commit-dapper-bass', 'commit-hd500', 'commit-g1on', 'commit-g1xon', 'commit-stomplab2g', 'commit-perform-ve', 'commit-stomplab1g', 'commit-perform-vg', 'commit-perform-vk', 'commit-perform-v', 'commit-stomplab2b', 'commit-tonelab-se', 'commit-tonelab-st', 'commit-tonelab-le', 'commit-ax1500g', 'commit-rp255', 'commit-gt8', 'commit-gt10', 'commit-me20b', 'commit-me50', 'commit-b2-followup', 'commit-ax3000g', 'commit-pandora', 'commit-vl3x', 'commit-b3', 'commit-g3', 'commit-me25', 'commit-rp360xp', 'commit-me70', 'commit-me80', 'commit-field-projection', 'commit-field-extraction', 'commit-pe100', 'commit-g3xn', 'commit-g3n', 'commit-b3n', 'commit-a1four', 'commit-a1xfour', 'commit-ms50g', 'commit-ms70cdr', 'commit-ms70cdrplus', 'commit-ms60bplus', 'commit-b1on', 'commit-ms60b', 'commit-g5n', 'commit-pod-express-guitar-preservation', 'commit-pod-express-bass-preservation', 'commit-g11-preservation', 'commit-arena-preservation', 'commit-fx100-preservation', 'commit-fx200-preservation', 'commit-core-preservation', 'commit-gembox-preservation', 'commit-gembox-ii-preservation', 'commit-gembox-iii-preservation', 'commit-podgo-preservation', 'commit-podgo-wireless-preservation', 'commit-tank-g-preservation', 'commit-tank-b-preservation', 'commit-tank-mini-preservation', 'commit-mk20-preservation', 'commit-mk300-preservation', 'commit-tankpro-preservation', 'commit-annblackbox-preservation', 'commit-minix-preservation', 'commit-pocketamp-preservation', 'commit-cubebabyac-preservation', 'commit-cubebabybass-preservation', 'commit-cubebabyelectric-preservation', 'commit-mg100-preservation', 'commit-mg200-preservation', 'commit-trident-preservation', 'commit-finding-audit', 'commit-legacy-audit', 'commit-nux-mg101-audit', 'commit-nux-mg300-audit', 'commit-nux-mg300mkii-audit', 'commit-nux-mg400-audit', 'commit-nux-mg30-audit', 'commit-nux-mg50li-audit', 'commit-nux-union', 'commit-bass-union', 'commit-vocal-union', 'commit-advanced-hxe-audit', 'commit-advanced-flex-audit', 'commit-advanced-union', 'commit-boss-union', 'commit-boss-history-union', 'commit-audota-union', 'commit-cube-union', 'commit-owned-union', 'commit-market1-union', 'commit-market7-union', 'commit-market6-union', 'commit-market5-union', 'commit-market4-union', 'commit-market3-union', 'commit-market2-union', 'commit-compact-union', 'commit-floorboard-union', 'commit-floorboard-matribox-ii', 'commit-floorboard-matribox-ii-pro', 'commit-compact-gp100-audit', 'commit-compact-gp150-audit', 'commit-compact-matribox-audit', 'commit-compact-gp5-audit', 'commit-compact-gp50-audit', 'commit-compact-gp180-audit', 'commit-compact-smartbox-audit', 'commit-compact-pocketmaster-audit'):
        verify()
        for check in ('test-fields', 'test-extraction', 'test-selection', 'verify'):
            subprocess.run([sys.executable, str(ROOT/'scripts/comparison_views.py'), check], check=True)
        assert not git('diff', '--cached', '--name-only').strip(), 'Existing staged changes'
        paths = ['Makefile', 'scripts/research_tools.py', 'scripts/comparison_views.py', 'ALL-GUITAR.md', 'ALL-BASS.md', 'ALL-VOCAL.md', 'README.md', 'research-state.json']
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
        message = 'fix(comparisons): preserve separate technical source columns' if mode == 'commit-field-extraction' else 'fix(comparisons): route analog conversion and automation to useful columns'
        if mode == 'commit-nux-mg50li-audit':
            message = 'audit(nux): preserve MG-50Li shared fields and conflicting source counts'
        if mode == 'commit-nux-mg30-audit':
            message = 'audit(nux): preserve MG-30 shared fields and qualify historical price citation'
        if mode == 'commit-nux-mg400-audit':
            message = 'audit(nux): preserve MG-400 shared fields and historical firmware scope'
        if mode == 'commit-nux-mg300mkii-audit':
            message = 'audit(nux): preserve MG-300 MKII shared fields and GEN2 qualifications'
        if mode == 'commit-nux-mg300-audit':
            message = 'audit(nux): preserve original MG-300 shared evidence and variant boundaries'
        if mode == 'commit-nux-mg101-audit':
            message = 'audit(nux): preserve MG-101 source evidence and verification tooling'
        if mode == 'commit-pe100':
            message = 'research(mooer): expose output conflicts in comparison view'
        if mode == 'commit-ms60b':
            message = 'research(zoom): verify MS-60B patch saving tempo and internal routing'
        if mode == 'commit-rp360xp':
            message = 'research(digitech): document RP360XP USB monitoring and output mode controls'
        if mode == 'commit-perform-ve':
            message = 'research(tc-helicon): restore PERFORM-VE routing conflicts and qualified offer coverage'
        if mode == 'commit-perform-vg':
            message = 'research(tc-helicon): add qualified PERFORM-VG preorder observation'
        if mode == 'commit-perform-vk':
            message = 'research(tc-helicon): restore PERFORM-VK harmony routing and offer comparison coverage'
        if mode == 'commit-perform-v':
            message = 'research(tc-helicon): restore PERFORM-V conflicts remote rules and offer in comparisons'
        if mode == 'commit-dapper-indie':
            message = 'research(valeton): clarify Indie fields and reconcile recorded discovery status'
        if mode == 'commit-dapper-dark-mini':
            message = 'research(valeton): add separate Dark Mini with indexed-manual qualifications'
        if mode == 'commit-rp500':
            message = 'research(digitech): count RP500 amp cabinet and shared FX alternatives'
        if mode == 'commit-g21u':
            message = 'research(zoom): reconcile G2.1u category inventory and delay routing limits'
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
            message = 'research(line6): separate HX Effects preset and Favorites capacities'
        if mode == 'commit-criticalmass':
            message = 'research(tchelicon): qualify Critical Mass style wording and power specificity'
        if mode == 'commit-b21u':
            message = 'research(zoom): reconcile B2.1u module choices and acoustic amp distinction'
        if mode == 'commit-katana-go':
            message = 'research(boss): verify GT-1 battery fallback and backup scope'
        if mode == 'commit-microplus':
            message = 'research(fender): qualify original Micro firmware and updater platforms'
        if mode == 'commit-mg20':
            message = 'research(nux): retain MP-2 effect choices and audio driver qualifications'
        if mode == 'commit-m100':
            message = 'research(tc-electronic): enumerate M-One XL choices and preserve MIDI conflict'
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
            message = 'research(zoom): preserve exact sold-out B2 FOUR adapter-bundle ask'
        if mode == 'commit-b1xfour-followup':
            message = 'research(zoom): resolve B1X FOUR display memory and looper qualifications'
        if mode == 'commit-readme-counts':
            message = 'fix(navigation): synchronize complete brand model lists from ledger'
        if mode == 'commit-hd400':
            message = 'research(line6): qualify HX Effects power source and rating limits'
        if mode == 'commit-xtlive':
            message = 'research(line6): qualify XT Live Silicon support and discontinued updater'
        if mode == 'commit-x3live':
            message = 'research(line6): qualify X3 Live Silicon support and updater restrictions'
        if mode == 'commit-harmony-singer2':
            message = 'research(tc-helicon): qualify Harmony Singer 2 quick-start revision differences'
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
            message = 'research(behringer): add separate Bass V-AMP PRO and preserve specification conflicts'
        if mode == 'commit-bass-vamp':
            message = 'research(behringer): clarify desktop routing and MIDI sampler requirements'
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
            message = 'research(boss): qualify VE-5 loop modes retention and global controls'
        if mode == 'commit-rp1000':
            message = 'research(digitech): enumerate RP1000 amp cabinet and shared FX choices'
        if mode == 'commit-gt6':
            message = 'research(boss): enumerate AD-10 choices and qualify looper operation'
        if mode == 'commit-hxone':
            message = 'research(line6): verify HX One dimensions and qualify regional specifications'
        if mode == 'commit-pocketpod':
            message = 'research(line6): reconcile Pocket POD effect choices and USB limits'
        if mode == 'commit-m9':
            message = 'research(line6): corroborate M9 AC supply and qualify looper MIDI limits'
        if mode == 'commit-m5':
            message = 'research(line6): enumerate M5 models and document bass suitability'
        if mode == 'commit-ax3g':
            message = 'research(korg): reconcile AX3G algorithms and distinguish drone from synth'
        if mode == 'commit-ax1000g':
            message = 'research(korg): preserve second AX1000G sold-out offer separately'
        if mode == 'commit-ve20-followup':
            message = 'research(boss): verify VE-20 effect type counts and custom pedal groups'
        if mode == 'commit-g71ut':
            message = 'research(zoom): reconcile G7.1ut category inventory to 92 effects'
        if mode == 'commit-gfx4':
            message = 'research(zoom): verify GFX-4 rotary controls and explicit-save behavior'
        if mode == 'commit-gfx5':
            message = 'research(zoom): enumerate GFX-5 controls and qualify bypass routing'
        if mode == 'commit-gfx3':
            message = 'research(zoom): add GFX-3 and preserve module-count conflict'
        if mode == 'commit-rp250':
            message = 'research(digitech): enumerate RP250 categories and preserve ChorusFX gaps'
        if mode == 'commit-rp90':
            message = 'research(digitech): clarify RP90 calibration reset and tuner behavior'
        if mode == 'commit-ax10g':
            message = 'research(korg): qualify AX10B Japanese adapter and NR evidence'
        if mode == 'commit-g3x':
            message = 'research(zoom): verify G3X synth DSP and expression qualifications'
        if mode == 'commit-g5':
            message = 'research(zoom): qualify G5 controls looper and tube-booster restrictions'
        if mode == 'commit-ms50gplus':
            message = 'research(zoom): qualify GFX-707 drive label discrepancy and amp variants'
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
            message = 'research(tech21): verify Bass Fly Rig v2 channel EQ and effect mixing limits'
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
            message = 'research(vox): include qualified StompLab 2B historical offer in bass comparison'
        if mode == 'commit-tonelab-se':
            message = 'research(vox): preserve ToneLab EX height conflict and reconcile effect totals'
        if mode == 'commit-tonelab-st':
            message = 'research(vox): include qualified ToneLab ST historical offer in comparison'
        if mode == 'commit-tonelab-le':
            message = 'research(vox): qualify ToneLab LE Hold Delay and editor MIDI requirements'
        if mode == 'commit-ax1500g':
            message = 'research(korg): preserve separate AX1500G condition-unverified offers'
        if mode == 'commit-rp255':
            message = 'research(digitech): include qualified RP255 historical hardware offer in comparison'
        if mode == 'commit-gt8':
            message = 'research(boss): verify GT-8 category choices shared custom settings and MIDI backups'
        if mode == 'commit-gt10':
            message = 'research(boss): qualify GT-10 preamp enumeration and drive count discrepancy'
        if mode == 'commit-me20b':
            message = 'research(boss): preserve ME-50B tuner conflict and verify adapter compatibility'
        if mode == 'commit-me50':
            message = 'research(boss): verify ME-50 named controls and toe-switch calibration'
        if mode == 'commit-b2-followup':
            message = 'research(zoom): reconcile B2 FOUR effect category inventory'
        if mode == 'commit-ax3000g':
            message = 'research(korg): document AX3000G MIDI ESS and adapter compatibility limits'
        if mode == 'commit-pandora':
            message = 'research(korg): include qualified PANDORA stomp historical offer in comparisons'
        if mode == 'commit-vl3x':
            message = 'research(tc-helicon): preserve exact VL3X indexed asking price'
        if mode == 'commit-b3':
            message = 'research(zoom): distinguish B3 rhythm entries and automatic patch saving'
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
            message = 'research(zoom): clarify B1on save tuner and control qualifications'
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
            message = 'research(zoom): correct B3n headphone certainty and loop persistence'
        if mode == 'commit-g3n':
            message = 'research(zoom): resolve G3n acoustic patches rhythm memory and looper limits'
        if mode == 'commit-g5n':
            message = 'research(zoom): establish G5n acoustic simulation and qualify synth-style presets'
        if mode == 'commit-g3xn':
            message = 'research(zoom): add G3Xn with qualified used offers and revision limits'
        if mode == 'commit-pod-express-guitar-preservation':
            message = 'fix(line6): restore complete POD Express Guitar provenance and dimensions'
        if mode == 'commit-pod-express-bass-preservation':
            message = 'fix(line6): restore complete POD Express Bass evidence and historical offer'
        if mode == 'commit-g11-preservation':
            message = 'fix(zoom): preserve complete G11 original evidence and count qualifications'
        if mode == 'commit-arena-preservation':
            message = 'research(donner): preserve alternate official manual provenance'
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
            message = 'research(mvave): preserve TANK-B source and distinguish original and V2 firmware'
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
            message = 'docs(mvave): preserve CUBE BABY BASS provenance and comparison field limits'
        if mode == 'commit-mg100-preservation':
            message = 'research(nux): preserve MG-100 source and retain official reverb conflict'
        if mode == 'commit-mg200-preservation':
            message = 'docs(nux): preserve MG-200 complete source and comparison qualifications'
        if mode == 'commit-trident-preservation':
            message = 'research(nux): preserve TRIDENT original and qualify USB and loop routing'
        if mode == 'commit-finding-audit':
            message = 'audit: reconcile B1Xon and verify registered finding-body coverage'
        if mode == 'commit-floorboard-matribox-ii-pro':
            message = 'audit(sonicake): preserve Matribox II Pro rows and MIDI contradiction'
        if mode == 'commit-floorboard-matribox-ii':
            message = 'audit(sonicake): preserve exact Matribox II floorboard rows and context'
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
            message = 'audit(sonicake): preserve complete Matribox original and qualify finding coverage'
        if mode == 'commit-compact-gp5-audit':
            message = 'audit(valeton): verify GP-5 shared source and resolve historical references'
        if mode == 'commit-compact-gp50-audit':
            message = 'audit(valeton): verify GP-50 shared fields and resolve provenance sources'
        if mode == 'commit-compact-gp180-audit':
            message = 'audit(valeton): verify GP-180 shared provenance and preserve version distinctions'
        if mode == 'commit-compact-smartbox-audit':
            message = 'audit(sonicake): preserve complete Smart Box original and rebuild provenance'
        if mode == 'commit-compact-pocketmaster-audit':
            message = 'audit(sonicake): preserve complete Pocket Master original and stock limits'
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
        subject = 'research(valeton): reconcile GP-200R variant offers without duplicate counting' if mode == 'commit-gp200jr' else 'research(line6): verify HX Effects3.80 acoustic simulation and looper limits'
        if mode=='commit-comparisons':
            subject='docs(comparisons): compare every recorded instrument model and separate specialist archives'
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
