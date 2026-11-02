"""Validate and commit the reviewed M-VAVE controller capability audit locally."""
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
    allowed = {'brand/ROWIN.md','brand/HARLEY-BENTON.md','brand/FLAMMA.md','brand/BLACKSTAR.md','brand/KEELEY.md','brand/DEMONFX.md','brand/MOSKY.md','brand/VING.md','brand/EROK.md','brand/SORAN.md','brand/DK.md','brand/KEMPER.md','brand/CUVAVE.md','brand/M-VAVE.md','EXPRESSION-VOLUME.md','README.md','MULTI-EFFECTS.md','all-guitar.md','all-bass.md','all-vocal.md','research-state.json','scripts/comparison_views.py','scripts/expression_audit_mvave.py','Makefile'}
    changed = set(git('diff','--name-only').splitlines()) | set(git('ls-files','--others','--exclude-standard').splitlines())
    assert changed <= allowed, changed - allowed
    assert not git('diff','--check').strip(), 'Whitespace errors'
    git('add','--',*sorted(changed))
    print(git('diff','--cached','--stat'))
    print(git('commit','-m','research(mvave): qualify TANK-B v100 import and hardware scope'))
