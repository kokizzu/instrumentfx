"""Validate and publish a reviewed Positive Grid partial catalogue profile."""
import sys
import hashlib
from pathlib import Path
sys.dont_write_bytecode = True
from research_tools import git, verify
import comparison_views

if __name__ == '__main__':
    assert sys.argv[1:] in (['stage'], ['commit'])
    review_path = Path('/tmp/instrumentfx-positive-grid-staged-review.json')
    verify()
    comparison_views.verify_views()
    comparison_views.test_readme_brand_counts()
    comparison_views.test_validation_counts()
    allowed = {'POSITIVE-GRID.md', 'EXPRESSION-VOLUME.md', 'README.md', 'research-state.json', 'scripts/positive_grid_catalogue.py', 'Makefile'}
    changed = set(git('diff','--name-only').splitlines()) | set(git('ls-files','--others','--exclude-standard').splitlines())
    staged = set(git('diff','--cached','--name-only').splitlines())
    assert (changed | staged) <= allowed, (changed | staged) - allowed
    assert not git('diff','--check').strip(), 'Whitespace errors'
    if sys.argv[1:] == ['stage']:
        assert not staged, 'Existing staged changes'
        assert changed, 'No changes to review'
        git('add','--',*sorted(changed))
        diff = git('diff','--cached')
        Path('/tmp/instrumentfx-positive-grid-staged.diff').write_text(diff)
        import json
        review_path.write_text(json.dumps({'head': git('rev-parse','HEAD').strip(), 'sha256': hashlib.sha256(diff.encode()).hexdigest()}))
        print(git('diff','--cached','--stat'))
        print('Review /tmp/instrumentfx-positive-grid-staged.diff before make research-commit-positive-grid')
    else:
        assert staged and not changed, 'Stage and review all intended changes first'
        import json
        review = json.loads(review_path.read_text())
        assert review['head'] == git('rev-parse','HEAD').strip(), 'HEAD changed since review'
        assert review['sha256'] == hashlib.sha256(git('diff','--cached').encode()).hexdigest(), 'Staged diff changed since review'
        assert not git('diff','--cached','--check').strip(), 'Staged whitespace errors'
        print(git('commit','-m','research(positive-grid): qualify Spark PEDAL chain and MIDI volume'))
