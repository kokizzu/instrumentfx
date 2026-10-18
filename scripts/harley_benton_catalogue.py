"""Validate and commit the reviewed Harley Benton catalogue integration locally."""
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
    allowed = {'HARLEY-BENTON.md','README.md','MULTI-EFFECTS.md','ALL-GUITAR.md','ALL-BASS.md','ALL-VOCAL.md','research-state.json','scripts/comparison_views.py','scripts/harley_benton_catalogue.py','Makefile'}
    changed = set(git('diff','--name-only').splitlines()) | set(git('ls-files','--others','--exclude-standard').splitlines())
    assert changed <= allowed, changed - allowed
    git('add','--',*sorted(changed))
    print(git('diff','--cached','--stat'))
    print(git('commit','-m','research(harley-benton): include Core and verify requested pedals'))
