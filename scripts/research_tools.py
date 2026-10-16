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
    elif mode == 'verify':
        verify()
    elif mode == 'gp200jr':
        gp200jr()
    elif mode == 'render-gp200jr':
        subprocess.run(['pdftoppm', '-f', '5', '-l', '6', '-scale-to', '1800', '-png', '/tmp/instrumentfx-sources/gp-200jr-v1.8.0.pdf', '/tmp/instrumentfx-sources/gp200jr-panel'], check=True)
    elif mode in ('commit-gp200jr', 'commit-hx-effects', 'commit-comparisons'):
        verify()
        print(git('status', '--short', '--branch'))
        assert not git('diff', '--cached', '--name-only').strip(), 'Unrelated staged changes; inspect before committing'
        paths = ['Makefile', 'scripts/research_tools.py', 'ALL-GUITAR.md', 'ALL-BASS.md', 'MULTI-EFFECTS.md', 'README.md', 'research-state.json']
        if mode=='commit-comparisons':
            paths += ['scripts/comparison_views.py','AGENTS.md','SINGLE-GUITAR.md','SINGLE-BASS.md','SINGLE-VOCAL.md','effects/specialist.md','effects/findings/2026-10-14-flamma-fv01.md']
            subprocess.run(['python3',str(ROOT/'scripts/comparison_views.py'),'verify'],check=True)
        else:
            paths.append('VALETON.md' if mode == 'commit-gp200jr' else 'LINE6.md')
        print(git('add', '--', *paths))
        print(git('diff', '--cached', '--stat'))
        subject = 'research(valeton): verify GP-200JR and reconcile newer catalogue checkpoints' if mode == 'commit-gp200jr' else 'research(line6): consolidate HX Effects as guitar and bass multi-effects'
        if mode=='commit-comparisons':
            subject='docs(comparisons): compare every recorded instrument model and separate specialist archives'
        print(git('commit', '-m', subject))
    else:
        raise SystemExit('Unknown operation')

if __name__ == '__main__':
    main()
