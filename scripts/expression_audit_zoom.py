"""Validate and commit the reviewed Zoom expression audit locally."""
import sys
sys.dont_write_bytecode = True
from research_tools import git, verify
import comparison_views

if __name__ == '__main__':
    assert sys.argv[1:] in (['commit'], ['commit-505'], ['commit-606'], ['commit-607'])
    verify()
    comparison_views.verify_views()
    comparison_views.test_readme_brand_counts()
    comparison_views.test_validation_counts()
    assert not git('diff', '--cached', '--name-only').strip(), 'Existing staged changes'
    allowed = {'FOOTSWITCH-DISPLAYS.md','VALETON.md','NUX.md','IK-MULTIMEDIA.md','ZOOM.md','EXPRESSION-VOLUME.md','README.md','MULTI-EFFECTS.md','ALL-GUITAR.md','ALL-BASS.md','ALL-VOCAL.md','research-state.json','scripts/comparison_views.py','scripts/expression_audit_zoom.py','Makefile'}
    changed = set(git('diff','--name-only').splitlines()) | set(git('ls-files','--others','--exclude-standard').splitlines())
    assert changed <= allowed, changed - allowed
    assert not git('diff','--check').strip(), 'Whitespace errors'
    git('add','--',*sorted(changed))
    print(git('diff','--cached','--stat'))
    message = 'research(zoom): document original 505 conditional expression volume' if sys.argv[1]=='commit-505' else 'research(zoom): qualify exact MS-70CDR Plus Shopee voucher offer'
    if sys.argv[1] in ['commit-606','commit-607']:
        model=sys.argv[1].split('-')[1]
        message='research(zoom): reconcile '+model+' built-in treadle shortlist exclusion'
    if sys.argv[1]=='commit':
        message='research(zoom): verify G3Xn separate LCD effect units'
    print(git('commit','-m',message))
