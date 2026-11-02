"""Validate and commit the reviewed TC capability audit locally."""
import sys
sys.dont_write_bytecode = True
from research_tools import git, verify
import comparison_views

if __name__ == '__main__':
    assert sys.argv[1:] == ['commit']
    import subprocess
    subprocess.run([sys.executable, "scripts/brand_sort.py", "verify"], check=True)
    verify()
    comparison_views.verify_views()
    comparison_views.test_readme_brand_counts()
    comparison_views.test_validation_counts()
    assert not git('diff', '--cached', '--name-only').strip(), 'Existing staged changes'
    allowed = {'brand/ZOOM.md','brand/NEURAL-DSP.md','brand/FRACTAL-AUDIO.md','FOOTSWITCH-DISPLAYS.md','brand/JOYO.md','brand/TC-HELICON.md','brand/TC-ELECTRONIC.md','EXPRESSION-VOLUME.md','README.md','MULTI-EFFECTS.md','all-guitar.md','all-bass.md','all-vocal.md','research-state.json','scripts/comparison_views.py','scripts/expression_audit_tc.py','Makefile'}
    changed = set(git('diff','--name-only').splitlines()) | set(git('ls-files','--others','--exclude-standard').splitlines())
    assert changed <= allowed, changed - allowed
    assert not git('diff', '--check').strip(), 'Whitespace errors'
    git('add','--',*sorted(changed))
    print(git('diff','--cached','--stat'))
    print(git('commit','-m','research(tc): qualify X1 factory map and display pickup scope'))
