"""Validate and publish a reviewed Roland catalogue findings."""
import sys
import hashlib
from pathlib import Path
sys.dont_write_bytecode = True
from research_tools import git, verify
import comparison_views

if __name__ == '__main__':
    assert sys.argv[1:] in (['stage'], ['commit'])
    review_path = Path('/tmp/instrumentfx-roland-staged-review.json')
    verify()
    comparison_views.verify_views()
    comparison_views.test_readme_brand_counts()
    comparison_views.test_validation_counts()
    allowed = {'CREATIVE-EFFECTS.md', 'EXPRESSION-VOLUME.md', 'brand/ROLAND.md', 'all-guitar.md', 'all-bass.md', 'all-vocal.md', 'research-state.json', 'scripts/research_audit_roland.py', 'Makefile'}
    changed = set(git('diff','--name-only').splitlines()) | set(git('ls-files','--others','--exclude-standard').splitlines())
    staged = set(git('diff','--cached','--name-only').splitlines())
    assert (changed | staged) <= allowed, (changed | staged) - allowed
    assert not git('diff','--check').strip(), 'Whitespace errors'
    if sys.argv[1:] == ['stage']:
        if staged:
            import json
            previous = json.loads(review_path.read_text())
            assert previous['head'] == git('rev-parse','HEAD').strip(), 'HEAD changed since review'
            assert previous['sha256'] == hashlib.sha256(git('diff','--cached').encode()).hexdigest(), 'Unreviewed staged changes'
        assert changed, 'No changes to review'
        git('add','--',*sorted(changed))
        diff = git('diff','--cached')
        Path('/tmp/instrumentfx-roland-staged.diff').write_text(diff)
        import json
        review_path.write_text(json.dumps({'head': git('rev-parse','HEAD').strip(), 'sha256': hashlib.sha256(diff.encode()).hexdigest()}))
        print(git('diff','--cached','--stat'))
        print('Review /tmp/instrumentfx-roland-staged.diff before make research-commit-roland')
    else:
        assert staged and not changed, 'Stage and review all intended changes first'
        import json
        review = json.loads(review_path.read_text())
        assert review['head'] == git('rev-parse','HEAD').strip(), 'HEAD changed since review'
        assert review['sha256'] == hashlib.sha256(git('diff','--cached').encode()).hexdigest(), 'Staged diff changed since review'
        assert not git('diff','--cached','--check').strip(), 'Staged whitespace errors'
        print(git('commit','-m','research(roland): distinguish GR-55 synth pitch and special processing'))
