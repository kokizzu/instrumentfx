"""Validate and commit the reviewed Tech 21 catalogue integration locally."""
import sys
sys.dont_write_bytecode = True
from research_tools import git, verify
import comparison_views

if __name__ == '__main__':
    assert sys.argv[1:] in (['stage'], ['commit'])
    verify()
    comparison_views.verify_views()
    comparison_views.test_readme_brand_counts()
    comparison_views.test_validation_counts()
    allowed = {'EXPRESSION-VOLUME.md','brand/TECH21.md','README.md','MULTI-EFFECTS.md','all-guitar.md','all-bass.md','all-vocal.md','research-state.json','scripts/comparison_views.py','scripts/tech21_catalogue.py','Makefile'}
    changed = set(git('diff','--name-only').splitlines()) | set(git('ls-files','--others','--exclude-standard').splitlines())
    import hashlib
    import json
    from pathlib import Path
    staged = set(git('diff','--cached','--name-only').splitlines())
    assert (changed | staged) <= allowed, (changed | staged) - allowed
    assert not git('diff','--check').strip()
    receipt = Path('/tmp/instrumentfx-tech21-review.json')
    if sys.argv[1:] == ['stage']:
        assert not staged, 'Existing staged changes'
        assert changed, 'No changes'
        git('add','--',*sorted(changed))
        diff = git('diff','--cached')
        Path('/tmp/instrumentfx-tech21-staged.diff').write_text(diff)
        receipt.write_text(json.dumps({'head':git('rev-parse','HEAD'),'hash':hashlib.sha256(diff.encode()).hexdigest()}))
        print(git('diff','--cached','--stat'))
        print('Review /tmp/instrumentfx-tech21-staged.diff before committing')
    else:
        saved = json.loads(receipt.read_text())
        assert staged and not changed, 'Stage and review first'
        assert saved['head'] == git('rev-parse','HEAD')
        assert saved['hash'] == hashlib.sha256(git('diff','--cached').encode()).hexdigest()
        assert not git('diff','--cached','--check').strip()
        print(git('commit','-m','docs(tech21): restore Fly Rig expression evidence to model scope'))
