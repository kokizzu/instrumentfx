"""Validate and commit the reviewed Behringer catalogue integration locally."""
import sys
import json
import hashlib
sys.dont_write_bytecode = True
from research_tools import git, verify
import comparison_views

if __name__ == '__main__':
    assert sys.argv[1:] in (['stage'], ['commit'])
    verify()
    comparison_views.verify_views()
    comparison_views.test_readme_brand_counts()
    comparison_views.test_validation_counts()
    staged = set(git('diff','--cached','--name-only').splitlines())
    allowed = {'brand/BEHRINGER.md','EXPRESSION-VOLUME.md','README.md','MULTI-EFFECTS.md','all-guitar.md','all-bass.md','all-vocal.md','research-state.json','scripts/comparison_views.py','scripts/expression_audit_behringer.py','Makefile'}
    changed = set(git('diff','--name-only').splitlines()) | set(git('ls-files','--others','--exclude-standard').splitlines())
    assert (changed | staged) <= allowed, (changed | staged) - allowed
    assert not git('diff','--check').strip(), 'Whitespace errors'
    from pathlib import Path
    receipt = Path('/tmp/instrumentfx-behringer-review.json')
    if sys.argv[1] == 'stage':
        assert not staged and changed, 'Existing staged work or no changes'
        git('add','--',*sorted(changed))
        diff = git('diff','--cached')
        receipt.write_text(json.dumps({'head':git('rev-parse','HEAD'),'hash':hashlib.sha256(diff.encode()).hexdigest()}))
        print(diff)
    else:
        saved = json.loads(receipt.read_text())
        assert staged and not changed, 'Stage and review first'
        assert saved['head'] == git('rev-parse','HEAD')
        assert saved['hash'] == hashlib.sha256(git('diff','--cached').encode()).hexdigest()
        assert not git('diff','--cached','--check')
        print(git('commit','-m','research(behringer): verify FX2000 sampler carriers and exact sold-out offer'))
