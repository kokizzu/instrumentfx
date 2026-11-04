"""Validate and commit the reviewed Zoom expression audit locally."""
import sys
import hashlib
import json
from pathlib import Path
sys.dont_write_bytecode = True
from research_tools import git, verify
import comparison_views

if __name__ == '__main__':
    assert sys.argv[1:] in (['stage'], ['commit'], ['commit-505'], ['commit-606'], ['commit-607'])
    import subprocess
    subprocess.run([sys.executable, "scripts/brand_sort.py", "test"], check=True)
    # Check the edited brand order without rewriting unrelated brands for spacing.
    import re
    headers = re.findall(r"^## (.+)$", Path("brand/ZOOM.md").read_text(), re.M)
    natural = lambda text: tuple((0, int(p)) if p.isdigit() else (1, p) for p in re.split(r"(\d+)", text.casefold()))
    assert headers == sorted(headers, key=natural), "Zoom model sections are not naturally sorted"
    verify()
    comparison_views.verify_views()
    comparison_views.test_readme_brand_counts()
    comparison_views.test_validation_counts()
    allowed = {'brand/EVENTIDE.md','brand/HEADRUSH.md','brand/FENDER.md','brand/MELOFTY.md','brand/NEURAL-DSP.md','brand/TC-ELECTRONIC.md','scripts/brand_sort.py','CREATIVE-EFFECTS.md','brand/MOOER.md','brand/BOSS.md','brand/FRACTAL-AUDIO.md','brand/LINE6.md','FOOTSWITCH-DISPLAYS.md','brand/VALETON.md','brand/NUX.md','brand/IK-MULTIMEDIA.md','brand/ZOOM.md','EXPRESSION-VOLUME.md','README.md','MULTI-EFFECTS.md','all-guitar.md','all-bass.md','all-vocal.md','research-state.json','scripts/comparison_views.py','scripts/expression_audit_zoom.py','Makefile'}
    changed = set(git('diff','--name-only').splitlines()) | set(git('ls-files','--others','--exclude-standard').splitlines())
    staged = set(git('diff','--cached','--name-only').splitlines())
    assert (changed | staged) <= allowed, (changed | staged) - allowed
    assert not git('diff','--check').strip(), 'Whitespace errors'
    review_path = Path('/tmp/instrumentfx-zoom-staged-review.json')
    if sys.argv[1] == 'stage':
        if staged:
            previous = json.loads(review_path.read_text())
            assert previous['head'] == git('rev-parse','HEAD').strip(), 'HEAD changed since review'
            assert previous['sha256'] == hashlib.sha256(git('diff','--cached').encode()).hexdigest(), 'Unreviewed staged changes'
        assert changed or staged, 'No changes to review'
        git('add','--',*sorted(changed))
        diff = git('diff','--cached')
        Path('/tmp/instrumentfx-zoom-staged.diff').write_text(diff)
        review_path.write_text(json.dumps({'head': git('rev-parse','HEAD').strip(), 'sha256': hashlib.sha256(diff.encode()).hexdigest()}))
        print(git('diff','--cached','--stat'))
        print('Review /tmp/instrumentfx-zoom-staged.diff before make expression-audit-commit-zoom')
        raise SystemExit(0)
    if sys.argv[1] == 'commit':
        assert staged and not changed, 'Stage and review intended changes first'
        review = json.loads(review_path.read_text())
        assert review['head'] == git('rev-parse','HEAD').strip(), 'HEAD changed since review'
        assert review['sha256'] == hashlib.sha256(git('diff','--cached').encode()).hexdigest(), 'Staged diff changed since review'
        assert not git('diff','--cached','--check').strip(), 'Staged whitespace errors'
    else:
        assert not staged, 'Existing staged changes'
        git('add','--',*sorted(changed))
        print(git('diff','--cached','--stat'))
    message = 'research(zoom): document original 505 conditional expression volume' if sys.argv[1]=='commit-505' else 'research(zoom): qualify exact MS-70CDR Plus Shopee voucher offer'
    if sys.argv[1] in ['commit-606','commit-607']:
        model=sys.argv[1].split('-')[1]
        message='research(zoom): reconcile '+model+' built-in treadle shortlist exclusion'
    if sys.argv[1]=='commit':
        message='research(melofty): qualify developer processing and tuner changes'
    print(git('commit','-m',message))
