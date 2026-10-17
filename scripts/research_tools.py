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
    elif mode in ('commit-gfx4', 'commit-ax1000g', 'commit-gfx5', 'commit-gfx3', 'commit-rp90', 'commit-ax10g', 'commit-rp500', 'commit-g21u', 'commit-g3x', 'commit-g5', 'commit-ms50gplus', 'commit-505ii', 'commit-ving-coverage', 'commit-ax5g', 'commit-rockstage', 'commit-dapper-indie', 'commit-dapper-dark-mini', 'commit-blackhammer', 'commit-flyrig5v2', 'commit-dapper-dark', 'commit-dapper-acoustic-mini', 'commit-dapper-mini', 'commit-dapper-bass-mini', 'commit-dapper-bass', 'commit-hd500', 'commit-g1on', 'commit-g1xon', 'commit-stomplab2g', 'commit-perform-ve', 'commit-stomplab1g', 'commit-perform-vg', 'commit-perform-vk', 'commit-perform-v', 'commit-stomplab2b', 'commit-tonelab-se', 'commit-tonelab-st', 'commit-tonelab-le', 'commit-ax1500g', 'commit-rp255', 'commit-gt8', 'commit-gt10', 'commit-me20b', 'commit-me50', 'commit-b2-followup', 'commit-ax3000g', 'commit-pandora', 'commit-vl3x', 'commit-b3', 'commit-g3', 'commit-me25', 'commit-rp360xp', 'commit-me70', 'commit-me80', 'commit-field-projection', 'commit-field-extraction', 'commit-pe100', 'commit-g3xn', 'commit-g3n', 'commit-b3n', 'commit-a1four', 'commit-a1xfour', 'commit-ms50g', 'commit-ms70cdr', 'commit-ms70cdrplus', 'commit-ms60bplus', 'commit-b1on', 'commit-ms60b', 'commit-g5n', 'commit-pod-express-guitar-preservation', 'commit-pod-express-bass-preservation', 'commit-g11-preservation', 'commit-arena-preservation', 'commit-fx100-preservation', 'commit-fx200-preservation', 'commit-core-preservation', 'commit-gembox-preservation', 'commit-gembox-ii-preservation', 'commit-gembox-iii-preservation', 'commit-podgo-preservation', 'commit-podgo-wireless-preservation', 'commit-tank-g-preservation', 'commit-tank-b-preservation', 'commit-tank-mini-preservation', 'commit-mk20-preservation', 'commit-mk300-preservation', 'commit-tankpro-preservation', 'commit-annblackbox-preservation', 'commit-minix-preservation', 'commit-pocketamp-preservation', 'commit-cubebabyac-preservation', 'commit-cubebabybass-preservation', 'commit-cubebabyelectric-preservation', 'commit-mg100-preservation', 'commit-mg200-preservation', 'commit-trident-preservation', 'commit-finding-audit', 'commit-legacy-audit', 'commit-nux-mg101-audit', 'commit-nux-mg300-audit', 'commit-nux-mg300mkii-audit', 'commit-nux-mg400-audit', 'commit-nux-mg30-audit', 'commit-nux-mg50li-audit', 'commit-nux-union', 'commit-bass-union', 'commit-vocal-union', 'commit-advanced-hxe-audit', 'commit-advanced-flex-audit', 'commit-advanced-union', 'commit-boss-union', 'commit-boss-history-union', 'commit-audota-union', 'commit-cube-union', 'commit-owned-union', 'commit-market1-union', 'commit-market7-union', 'commit-market6-union', 'commit-market5-union', 'commit-market4-union', 'commit-market3-union', 'commit-market2-union', 'commit-compact-union', 'commit-floorboard-union', 'commit-floorboard-matribox-ii', 'commit-floorboard-matribox-ii-pro', 'commit-compact-gp100-audit', 'commit-compact-gp150-audit', 'commit-compact-matribox-audit', 'commit-compact-gp5-audit', 'commit-compact-gp50-audit', 'commit-compact-gp180-audit', 'commit-compact-smartbox-audit', 'commit-compact-pocketmaster-audit'):
        verify()
        for check in ('test-fields', 'test-extraction', 'test-selection', 'verify'):
            subprocess.run([sys.executable, str(ROOT/'scripts/comparison_views.py'), check], check=True)
        assert not git('diff', '--cached', '--name-only').strip(), 'Existing staged changes'
        paths = ['Makefile', 'scripts/research_tools.py', 'scripts/comparison_views.py', 'ALL-GUITAR.md', 'ALL-BASS.md', 'ALL-VOCAL.md', 'README.md', 'research-state.json']
        if mode in ('commit-gt8', 'commit-gt10', 'commit-me20b', 'commit-me50'):
            paths += ['BOSS.md', 'MULTI-EFFECTS.md']
        if mode in ('commit-gfx4', 'commit-gfx5', 'commit-gfx3', 'commit-g21u', 'commit-g3x', 'commit-g5', 'commit-ms50gplus', 'commit-505ii'):
            paths += ['ZOOM.md', 'MULTI-EFFECTS.md']
        if mode == 'commit-b2-followup':
            paths += ['ZOOM.md']
        if mode in ('commit-ax1000g', 'commit-ax10g', 'commit-ax1500g', 'commit-ax3000g', 'commit-pandora'):
            paths += ['KORG.md', 'MULTI-EFFECTS.md']
        if mode == 'commit-vl3x':
            paths += ['TC-HELICON.md', 'MULTI-EFFECTS.md']
        if mode in ('commit-rp90', 'commit-rp500', 'commit-rp255', 'commit-rp360xp'):
            paths += ['DIGITECH.md', 'MULTI-EFFECTS.md']
        if mode in ('commit-me25', 'commit-me70', 'commit-me80'):
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
        if mode == 'commit-hd500':
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
            message = 'research(mooer): add PE100 portable multi-effects with qualified Shopee evidence'
        if mode == 'commit-ms60b':
            message = 'research(zoom): verify MS-60B patch saving tempo and internal routing'
        if mode == 'commit-rp360xp':
            message = 'research(digitech): document RP360XP USB monitoring and output mode controls'
        if mode == 'commit-perform-ve':
            message = 'research(tc-helicon): restore PERFORM-VE routing conflicts and qualified offer coverage'
        if mode == 'commit-perform-vg':
            message = 'research(tc-helicon): restore PERFORM-VG styles remote rules and offer in comparisons'
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
        if mode == 'commit-ax1000g':
            message = 'research(korg): preserve second AX1000G sold-out offer separately'
        if mode == 'commit-gfx4':
            message = 'research(zoom): add GFX-4 with AC power and qualified shop lead'
        if mode == 'commit-gfx5':
            message = 'research(zoom): enumerate GFX-5 controls and qualify bypass routing'
        if mode == 'commit-gfx3':
            message = 'research(zoom): add GFX-3 and preserve module-count conflict'
        if mode == 'commit-rp90':
            message = 'research(digitech): add RP90 with own manual and qualified faulty offer'
        if mode == 'commit-ax10g':
            message = 'research(korg): verify AX10G simultaneous architecture and guide conflict'
        if mode == 'commit-g3x':
            message = 'research(zoom): verify G3X synth DSP and expression qualifications'
        if mode == 'commit-g5':
            message = 'research(zoom): qualify G5 controls looper and tube-booster restrictions'
        if mode == 'commit-ms50gplus':
            message = 'research(zoom): distinguish MS-50G Plus document categories from installed effects'
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
            message = 'research(tech21): verify Fly Rig v2 rotary controls and delay behavior'
        if mode == 'commit-dapper-dark':
            message = 'research(valeton): qualify Dapper Dark indexed controls and loop routing'
        if mode == 'commit-dapper-acoustic-mini':
            message = 'research(valeton): clarify Acoustic Mini tuner indicators and headphone control'
        if mode == 'commit-dapper-mini':
            message = 'research(valeton): verify MES-1 controls tap mode and cab routing'
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
            message = 'research(vox): include qualified ToneLab SE sold-out offer in comparison'
        if mode == 'commit-tonelab-st':
            message = 'research(vox): include qualified ToneLab ST historical offer in comparison'
        if mode == 'commit-tonelab-le':
            message = 'research(vox): qualify ToneLab LE Hold Delay and editor MIDI requirements'
        if mode == 'commit-ax1500g':
            message = 'research(korg): enumerate AX1500G blocks and verify volatile phrase storage'
        if mode == 'commit-rp255':
            message = 'research(digitech): include qualified RP255 historical hardware offer in comparison'
        if mode == 'commit-gt8':
            message = 'research(boss): verify GT-8 category choices shared custom settings and MIDI backups'
        if mode == 'commit-gt10':
            message = 'research(boss): qualify GT-10 preamp enumeration and drive count discrepancy'
        if mode == 'commit-me20b':
            message = 'research(boss): qualify ME-20B delay tuner and exact marketplace link'
        if mode == 'commit-me50':
            message = 'research(boss): verify ME-50 named controls and toe-switch calibration'
        if mode == 'commit-b2-followup':
            message = 'research(zoom): restore B2 FOUR offer projection and clarify master output scope'
        if mode == 'commit-ax3000g':
            message = 'research(korg): document AX3000G MIDI ESS and adapter compatibility limits'
        if mode == 'commit-pandora':
            message = 'research(korg): include qualified PANDORA stomp historical offer in comparisons'
        if mode == 'commit-vl3x':
            message = 'research(tc-helicon): verify VL3X loop slots saving and guitar output routing'
        if mode == 'commit-b3':
            message = 'research(zoom): distinguish B3 rhythm entries and automatic patch saving'
        if mode == 'commit-g3':
            message = 'research(zoom): document G3 battery settings eco behavior and tuner modes'
        if mode == 'commit-me25':
            message = 'research(boss): qualify ME-25 library software and converter specifications'
        if mode == 'commit-me70':
            message = 'research(boss): qualify ME-70 groups loop stopping and catalogue dimensions'
        if mode == 'commit-me80':
            message = 'research(boss): resolve ME-80 buttons battery mass and loop erasure'
        if mode == 'commit-b1on':
            message = 'research(zoom): add B1on with original-model conflicts and qualified sold-out ask'
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
            message = 'docs(donner): verify complete Arena2000 legacy finding retention'
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
            message = 'audit: verify floorboard source union and preserve historical source context'
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
            message = 'audit: preserve complete first Shopee shared comparison and historical qualifications'
        if mode == 'commit-owned-union':
            message = 'audit: preserve seven owned-model shared summaries and identity context'
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
            message = 'audit(nux): verify shared source union and inventory incoming navigation'
        if mode == 'commit-compact-union':
            message = 'audit: inventory compact source navigation and incoming references'
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
        subject = 'research(valeton): verify GP-200JR and reconcile newer catalogue checkpoints' if mode == 'commit-gp200jr' else 'research(line6): verify HX Effects3.80 acoustic simulation and looper limits'
        if mode=='commit-comparisons':
            subject='docs(comparisons): compare every recorded instrument model and separate specialist archives'
        elif mode=='commit-prime':
            subject='research(headrush): add Prime with native NAM limits and qualified used retail evidence'
        elif mode=='commit-ge300':
            subject='research(mooer): add GE300 with converted NAM and firmware-qualified IR capacity'
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
