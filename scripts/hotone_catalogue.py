"""Validate and commit the reviewed catalogue/category update locally."""
import sys
sys.dont_write_bytecode = True
from research_tools import git, verify
import comparison_views

if __name__ == '__main__':
    if sys.argv[1:] == ['review']:
        from pathlib import Path
        Path('/tmp/instrumentfx-hotone-base-ledger.json').write_text(git('show', 'HEAD:research-state.json'))
        print(git('diff', '--', 'brand/HOTONE.md', 'research-state.json', 'scripts/hotone_catalogue.py', 'Makefile', 'all-guitar.md', 'all-bass.md'))
        raise SystemExit(0)
    assert sys.argv[1:] in (['stage'], ['commit'])
    verify()
    comparison_views.verify_views()
    comparison_views.test_readme_brand_counts()
    comparison_views.test_validation_counts()
    staged = set(git('diff','--cached','--name-only').splitlines())
    allowed = {'brand/HOTONE.md','EXPRESSION-VOLUME.md','README.md','MULTI-EFFECTS.md','all-guitar.md','all-bass.md','all-vocal.md','research-state.json','scripts/comparison_views.py','scripts/hotone_catalogue.py','Makefile','scripts/research_push.py'}
    changed = set(git('diff','--name-only').splitlines()) | set(git('ls-files','--others','--exclude-standard').splitlines())
    assert (changed | staged) <= allowed, (changed | staged) - allowed
    assert not git('diff','--check').strip(), 'Whitespace errors'
    from pathlib import Path
    import hashlib, json
    review_path = Path('/tmp/instrumentfx-hotone-staged-review.json')
    if sys.argv[1:] == ['stage']:
        assert not staged and changed, 'Unexpected staged changes or no changes'
        git('add','--',*sorted(changed))
        diff = git('diff','--cached')
        Path('/tmp/instrumentfx-hotone-staged.diff').write_text(diff)
        review_path.write_text(json.dumps({'head':git('rev-parse','HEAD').strip(),'sha256':hashlib.sha256(diff.encode()).hexdigest()}))
        print(git('diff','--cached','--stat'))
        raise SystemExit(0)
    assert staged and not changed, 'Stage and review first'
    review = json.loads(review_path.read_text())
    assert review['head'] == git('rev-parse','HEAD').strip()
    assert review['sha256'] == hashlib.sha256(git('diff','--cached').encode()).hexdigest()
    assert not git('diff','--cached','--check').strip()
    print(git('diff','--cached','--stat'))
    print(git('commit','-m','research(hotone): qualify sold-out Mini adapter-bundle ask'))
