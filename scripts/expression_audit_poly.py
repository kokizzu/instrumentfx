"""Validate and publish a reviewed Poly Effects catalogue findings."""
import sys
import hashlib
from pathlib import Path
sys.dont_write_bytecode = True
from research_tools import git, verify
import comparison_views

if __name__ == '__main__':
    assert sys.argv[1:] in (['stage'], ['commit'], ['stage-walrus'], ['commit-walrus'], ['stage-fishman'], ['commit-fishman'])
    walrus = sys.argv[1].endswith('-walrus')
    fishman = sys.argv[1].endswith('-fishman')
    stage_mode = sys.argv[1].startswith('stage')
    review_path = Path('/tmp/instrumentfx-poly-staged-review.json')
    verify()
    comparison_views.verify_views()
    comparison_views.test_readme_brand_counts()
    comparison_views.test_validation_counts()
    allowed = {'EXPRESSION-VOLUME.md', 'brand/POLY-EFFECTS.md', 'README.md', 'research-state.json', 'scripts/expression_audit_poly.py', 'Makefile'}
    if walrus:
        allowed.remove('brand/POLY-EFFECTS.md')
        allowed.add('brand/WALRUS-AUDIO.md')
    if fishman:
        allowed.remove('brand/POLY-EFFECTS.md')
        allowed.add('brand/FISHMAN.md')
    changed = set(git('diff','--name-only').splitlines()) | set(git('ls-files','--others','--exclude-standard').splitlines())
    staged = set(git('diff','--cached','--name-only').splitlines())
    assert (changed | staged) <= allowed, (changed | staged) - allowed
    assert not git('diff','--check').strip(), 'Whitespace errors'
    if stage_mode:
        assert not staged, 'Existing staged changes'
        assert changed, 'No changes to review'
        git('add','--',*sorted(changed))
        diff = git('diff','--cached')
        Path('/tmp/instrumentfx-poly-staged.diff').write_text(diff)
        import json
        review_path.write_text(json.dumps({'head': git('rev-parse','HEAD').strip(), 'sha256': hashlib.sha256(diff.encode()).hexdigest()}))
        print(git('diff','--cached','--stat'))
        print('Review /tmp/instrumentfx-poly-staged.diff before make expression-audit-commit-poly')
    else:
        assert staged and not changed, 'Stage and review all intended changes first'
        import json
        review = json.loads(review_path.read_text())
        assert review['head'] == git('rev-parse','HEAD').strip(), 'HEAD changed since review'
        assert review['sha256'] == hashlib.sha256(git('diff','--cached').encode()).hexdigest(), 'Staged diff changed since review'
        assert not git('diff','--cached','--check').strip(), 'Staged whitespace errors'
        message = 'research(walrus): screen ACS1 MKII direct expression and footprint' if walrus else 'research(poly): qualify Beebo Nano NAM and capture workflow'
        if fishman:
            message = 'research(fishman): screen ToneDEQ expression and Indonesian offers'
        print(git('commit','-m',message))
