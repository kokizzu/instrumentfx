"""Validate and commit the reviewed Lexicon catalogue integration locally."""
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
    allowed = {'CREATIVE-EFFECTS.md','brand/LEXICON.md','EXPRESSION-VOLUME.md','README.md','MULTI-EFFECTS.md','all-guitar.md','all-bass.md','all-vocal.md','research-state.json','scripts/comparison_views.py','scripts/expression_audit_lexicon.py','Makefile'}
    changed = set(git('diff','--name-only').splitlines()) | set(git('ls-files','--others','--exclude-standard').splitlines())
    assert (changed | staged) <= allowed, (changed | staged) - allowed
    assert not git('diff','--check').strip(), 'Whitespace errors'
    from pathlib import Path
    receipt = Path('/tmp/instrumentfx-lexicon-review.json')
    if sys.argv[1] == 'stage':
        if staged:
            previous = json.loads(receipt.read_text())
            assert previous['head'] == git('rev-parse','HEAD')
            assert previous['hash'] == hashlib.sha256(git('diff','--cached').encode()).hexdigest(), 'Unreviewed staged changes'
        assert changed, 'No changed files to stage'
        git('add','--',*sorted(changed))
        diff = git('diff','--cached')
        receipt.write_text(json.dumps({'head':git('rev-parse','HEAD'),'hash':hashlib.sha256(diff.encode()).hexdigest()}))
        Path('/tmp/instrumentfx-lexicon-staged.diff').write_text(diff)
        print(git('diff','--cached','--stat'))
        print('Review /tmp/instrumentfx-lexicon-staged.diff before committing')
    else:
        saved = json.loads(receipt.read_text())
        assert staged and not changed, 'Stage and review first'
        assert saved['head'] == git('rev-parse','HEAD')
        assert saved['hash'] == hashlib.sha256(git('diff','--cached').encode()).hexdigest()
        assert not git('diff','--cached','--check')
        print(git('commit','-m','research(lexicon): verify MX200 pitch ranges and exact sold-out offer'))
