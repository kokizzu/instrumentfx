"""Review and publish one creative-effects model without touching other queues."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
sys.dont_write_bytecode = True
from research_tools import ROOT, git, identity

REVIEW = Path('/tmp/instrumentfx-creative-review.json')
def main():
    identity()
    assert sys.argv[1:] in (['stage'], ['commit'])
    state = json.loads((ROOT/'research-state.json').read_text())
    audit = state['creative_effects_comparison']
    key = audit['publication_model']
    record = audit['models'][key]
    allowed = {record['brand_path'], 'CREATIVE-EFFECTS.md', 'research-state.json',
               'all-guitar.md', 'all-bass.md', 'all-vocal.md',
               'scripts/creative_effects.py', 'Makefile'}
    changed = set(git('diff','--name-only').splitlines()) | set(git('ls-files','--others','--exclude-standard').splitlines())
    staged = set(git('diff','--cached','--name-only').splitlines())
    assert (changed | staged) <= allowed, (changed | staged) - allowed
    for target in ('comparison-verify', 'research-verify', 'brand-sort-test'):
        subprocess.run(['make', target], cwd=ROOT, check=True)
    assert not git('diff','--check').strip()
    if sys.argv[1] == 'stage':
        assert changed or staged, 'No changes'
        git('add','--',*sorted(changed))
        diff = git('diff','--cached')
        Path('/tmp/instrumentfx-creative-staged.diff').write_text(diff)
        REVIEW.write_text(json.dumps({'head':git('rev-parse','HEAD').strip(), 'sha256':hashlib.sha256(diff.encode()).hexdigest(), 'model':key}))
        print(git('diff','--cached','--stat'))
        print('Review /tmp/instrumentfx-creative-staged.diff before creative-commit')
    else:
        assert staged and not changed
        review = json.loads(REVIEW.read_text())
        assert review['head'] == git('rev-parse','HEAD').strip()
        assert review['model'] == key
        assert review['sha256'] == hashlib.sha256(git('diff','--cached').encode()).hexdigest()
        assert not git('diff','--cached','--check').strip()
        print(git('commit','-m','docs: compare '+record['label']+' creative effects'))
if __name__ == '__main__':
    main()
