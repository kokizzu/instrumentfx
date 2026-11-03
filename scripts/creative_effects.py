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
    assert sys.argv[1:] in (['stage'], ['commit'], ['verify'])
    state = json.loads((ROOT/'research-state.json').read_text())
    audit = state['creative_effects_comparison']
    key = audit['publication_model']
    record = audit['models'][key]
    if audit.get('publication_action') == 'reconcile':
        expected = {'Line 6::HX Effects', 'BOSS::GT-1000CORE', 'Eventide::H90',
                    'MOOER::GE300', 'Zoom::B1on', 'BOSS::GM-800', 'NUX::MG-300 MKII'}
        assert set(audit['models']) == expected
        assert state['active_model_count'] == audit['inventory_count_unchanged'] == 402
        doc = (ROOT/'CREATIVE-EFFECTS.md').read_text()
        selected = doc.split('## Selected exact-model comparison', 1)[1].split('## Limits', 1)[0]
        assert len([line for line in selected.splitlines() if line.startswith('| [')]) == 7
        for model in audit['models'].values():
            assert len(model['matrix']) == 4 and model['sources']
            assert all(cell in selected for cell in model['matrix'])
        owned = {key for key, model in audit['models'].items() if model.get('owned')}
        assert owned == {'Line 6::HX Effects','BOSS::GT-1000CORE','BOSS::GM-800','Zoom::B1on','NUX::MG-300 MKII'}
        for key, sha in audit['published_model_commits'].items():
            subprocess.run(['git','merge-base','--is-ancestor',sha,'HEAD'], cwd=ROOT, check=True)
            published = git('show',sha+':CREATIVE-EFFECTS.md')
            assert audit['models'][key]['label'] in published
        previous = json.loads(git('show','HEAD:research-state.json'))
        assert {k:v for k,v in state.items() if k != 'creative_effects_comparison'} == {k:v for k,v in previous.items() if k != 'creative_effects_comparison'}, 'Unrelated queue changed'
        print('PASS: seven selected rows, explicit ownership, published model commits, 402 inventory and independent queues')
    if sys.argv[1] == 'verify':
        print(git('status','--short'))
        print('HEAD '+git('rev-parse','HEAD').strip())
        return
    allowed = {record['brand_path'], 'CREATIVE-EFFECTS.md', 'research-state.json',
               'all-guitar.md', 'all-bass.md', 'all-vocal.md',
               'scripts/creative_effects.py', 'Makefile'}
    changed = set(git('diff','--name-only').splitlines()) | set(git('ls-files','--others','--exclude-standard').splitlines())
    staged = set(git('diff','--cached','--name-only').splitlines())
    assert (changed | staged) <= allowed, (changed | staged) - allowed
    if sys.argv[1] == 'stage':
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
        message = 'docs: index existing creative-effects matches and reconcile selected audit' if audit.get('publication_action') == 'reconcile' else 'docs: compare '+record['label']+' creative effects'
        print(git('commit','-m',message))
if __name__ == '__main__':
    main()
