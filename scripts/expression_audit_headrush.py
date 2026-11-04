"""Validate and publish a reviewed HeadRush catalogue findings."""
import sys
import hashlib
from pathlib import Path
sys.dont_write_bytecode = True
from research_tools import git, verify
import comparison_views

if __name__ == '__main__':
    assert sys.argv[1:] in (['stage'], ['commit'])
    review_path = Path('/tmp/instrumentfx-headrush-staged-review.json')
    verify()
    comparison_views.verify_views()
    comparison_views.test_readme_brand_counts()
    comparison_views.test_validation_counts()
    allowed = {'CREATIVE-EFFECTS.md', 'FOOTSWITCH-DISPLAYS.md', 'brand/HEADRUSH.md', 'all-guitar.md', 'all-bass.md', 'all-vocal.md', 'research-state.json', 'scripts/expression_audit_headrush.py', 'Makefile'}
    changed = set(git('diff','--name-only').splitlines()) | set(git('ls-files','--others','--exclude-standard').splitlines())
    staged = set(git('diff','--cached','--name-only').splitlines())
    assert (changed | staged) <= allowed, (changed | staged) - allowed
    assert not git('diff','--check').strip(), 'Whitespace errors'
    if sys.argv[1:] == ['stage']:
        assert not staged, 'Existing staged changes'
        assert changed, 'No changes to review'
        git('add','--',*sorted(changed))
        diff = git('diff','--cached')
        Path('/tmp/instrumentfx-headrush-staged.diff').write_text(diff)
        import json
        review_path.write_text(json.dumps({'head': git('rev-parse','HEAD').strip(), 'sha256': hashlib.sha256(diff.encode()).hexdigest()}))
        print(git('diff','--cached','--stat'))
        print('Review /tmp/instrumentfx-headrush-staged.diff before make expression-audit-commit-headrush')
    else:
        assert staged and not changed, 'Stage and review all intended changes first'
        import json
        review = json.loads(review_path.read_text())
        assert review['head'] == git('rev-parse','HEAD').strip(), 'HEAD changed since review'
        assert review['sha256'] == hashlib.sha256(git('diff','--cached').encode()).hexdigest(), 'Staged diff changed since review'
        assert not git('diff','--cached','--check').strip(), 'Staged whitespace errors'
        print(git('commit','-m','research(headrush): record Prime pedal recommendations and exact offer'))
