"""Validate and commit the reviewed Zoom expression audit locally."""
import sys
sys.dont_write_bytecode = True
from research_tools import git, verify
import comparison_views

if __name__ == '__main__':
    assert sys.argv[1:] == ['commit']
    verify()
    comparison_views.verify_views()
    comparison_views.test_readme_brand_counts()
    comparison_views.test_validation_counts()
    assert not git('diff', '--cached', '--name-only').strip(), 'Existing staged changes'
    allowed = {'ZOOM.md','EXPRESSION-VOLUME.md','README.md','MULTI-EFFECTS.md','ALL-GUITAR.md','ALL-BASS.md','ALL-VOCAL.md','research-state.json','scripts/comparison_views.py','scripts/expression_audit_zoom.py','Makefile'}
    changed = set(git('diff','--name-only').splitlines()) | set(git('ls-files','--others','--exclude-standard').splitlines())
    assert changed <= allowed, changed - allowed
    git('add','--',*sorted(changed))
    print(git('diff','--cached','--stat'))
    print(git('commit','-m','research(zoom): audit B3n pedal volume and preserve coverage gaps'))
