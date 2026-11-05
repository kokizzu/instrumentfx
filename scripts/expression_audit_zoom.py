"""Validate and commit reviewed research with inventory and preservation checks."""
import sys
import hashlib
import json
from pathlib import Path
sys.dont_write_bytecode = True
from research_tools import git, verify
import comparison_views
import consolidation_tools

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
    # New findings must not rewrite registered historical bodies or comparison values.
    consolidation_tools.verify_preserved(json.loads(Path("research-state.json").read_text()))
    comparison_views.verify_views()
    comparison_views.test_readme_brand_counts()
    comparison_views.test_validation_counts()
    allowed = {'scripts/creative_effects.py','brand/JOYO.md','brand/JET-PEDALS.md','make/navigation.mk','brand/SHEERAN-LOOPERS.md','brand/RJM-MUSIC.md','scripts/json_pointer_removal.py','AGENTS.md','scripts/navigation_tools.py','single-guitar.md','single-vocal.md','scripts/archive_retirement.py','scripts/source_retirement.py','scripts/metadata_consolidation.py','scripts/compatibility_removal.py','scripts/research_tools.py','scripts/consolidation_tools.py','scripts/technical_retirement.py','brand/HOLOGRAM.md','brand/KORG.md','brand/KEELEY.md','brand/DIGITECH.md','brand/FAMC.md','brand/BLACKSTAR.md','brand/FLAMMA.md','brand/DONNER.md','brand/AUDOTA.md','brand/DARKGLASS.md','brand/KEMPER.md','brand/SORAN.md','brand/SONICAKE.md','brand/DK.md','brand/VING.md','brand/M-VAVE.md','brand/HOTONE.md','brand/TECH21.md','brand/MORNINGSTAR.md','brand/HARLEY-BENTON.md','brand/CUVAVE.md','brand/EVENTIDE.md','brand/HEADRUSH.md','brand/FENDER.md','brand/MELOFTY.md','brand/NEURAL-DSP.md','brand/TC-ELECTRONIC.md','scripts/brand_sort.py','CREATIVE-EFFECTS.md','brand/MOOER.md','brand/BOSS.md','brand/FRACTAL-AUDIO.md','brand/LINE6.md','FOOTSWITCH-DISPLAYS.md','brand/VALETON.md','brand/NUX.md','brand/IK-MULTIMEDIA.md','brand/ZOOM.md','EXPRESSION-VOLUME.md','README.md','MULTI-EFFECTS.md','all-guitar.md','all-bass.md','all-vocal.md','research-state.json','scripts/comparison_views.py','scripts/expression_audit_zoom.py','Makefile'}
    allowed.update(json.loads(Path('research-state.json').read_text()).get('migration',{}).get('removed_technical_redirects',{}))
    allowed.update(json.loads(Path('research-state.json').read_text()).get('migration',{}).get('removed_metadata_redirects',{}))
    allowed.update(json.loads(Path('research-state.json').read_text()).get('migration',{}).get('removed_archive_redirects',{}))
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
        message='research(boss): index GT-1 creative and pitch feedback boundaries'
    print(git('commit','-m',message))
