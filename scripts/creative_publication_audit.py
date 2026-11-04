"""Read-only audit of selected creative records on fetched upstream main."""
import json
import hashlib
import sys
import subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()
assert git('remote', 'get-url', 'origin') == 'git@github.com:kokizzu/instrumentfx.git'
assert git('branch', '--show-current') == 'main'
mode = sys.argv[1] if len(sys.argv) > 1 else 'audit'
paths = ['Makefile','scripts/creative_publication_audit.py']
receipt = Path('/tmp/instrumentfx-creative-publication-review.json')
if mode == 'stage':
    assert not git('diff','--cached','--name-only'), 'Existing staged work'
    subprocess.run(['git','diff','--check','--',*paths],cwd=ROOT,check=True)
    subprocess.run(['git','add','--',*paths],cwd=ROOT,check=True)
    diff = git('diff','--cached')
    Path('/tmp/instrumentfx-creative-publication-staged.diff').write_text(diff)
    receipt.write_text(json.dumps({'head':git('rev-parse','HEAD'),'hash':hashlib.sha256(diff.encode()).hexdigest()}))
    print(diff)
    sys.exit(0)
if mode == 'commit':
    saved = json.loads(receipt.read_text())
    assert set(git('diff','--cached','--name-only').splitlines()) == set(paths)
    assert saved['head'] == git('rev-parse','HEAD')
    assert saved['hash'] == hashlib.sha256(git('diff','--cached').encode()).hexdigest()
    assert not git('diff','--name-only','--',*paths)
    subprocess.run(['git','diff','--cached','--check'],cwd=ROOT,check=True)
    subprocess.run(['git','commit','-m','test: verify creative-effects publication against upstream main'],cwd=ROOT,check=True)
    sys.exit(0)
assert mode in {'audit','publish'}
subprocess.run(['git','fetch','origin','main'], cwd=ROOT, check=True)
if mode == 'publish':
    assert git('rev-list','--count','HEAD..origin/main') == '0', 'Remote advanced'
    subprocess.run(['git','push','origin','main:main'],cwd=ROOT,check=True)
    assert git('ls-remote','origin','refs/heads/main').split()[0] == git('rev-parse','HEAD')
    print('Remote main matches local HEAD')
assert git('ls-remote','--symref','origin','HEAD').splitlines()[0].startswith('ref: refs/heads/main')
remote = git('rev-parse','origin/main')
state = json.loads(git('show','origin/main:research-state.json'))
audit = state['creative_effects_comparison']
doc = git('show','origin/main:CREATIVE-EFFECTS.md')
selected = doc.split('## Selected exact-model comparison',1)[1].split('## Limits',1)[0]
assert len([line for line in selected.splitlines() if line.startswith('| [')]) == 7
assert state['active_model_count'] == audit['inventory_count_unchanged'] == 402
assert len(audit['models']) == 7
for key, record in audit['models'].items():
    sha = audit['published_model_commits'][key]
    subprocess.run(['git','merge-base','--is-ancestor',sha,'origin/main'],cwd=ROOT,check=True)
    assert record['label'] in selected
    assert all(cell in selected for cell in record['matrix'])
    assert record['sources']
    canonical = git('show','origin/main:'+record['brand_path'])
    assert canonical and record['label'] in git('show',sha+':CREATIVE-EFFECTS.md')
    print(key, sha)
print('Verified upstream main:',remote)
print('Selected rows: 7; active inventory: 402; additional catalogue records:',len(audit['additional_catalogue_matches']))
print('Local changes preserved:')
print(git('status','--short'))
