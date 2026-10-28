"""Validate and commit the reviewed catalogue/category update locally."""
import sys
sys.dont_write_bytecode = True
from research_tools import git, verify
import comparison_views

if __name__ == '__main__':
    if sys.argv[1:] == ['review']:
        from pathlib import Path
        Path('/tmp/instrumentfx-hotone-base-ledger.json').write_text(git('show', 'HEAD:research-state.json'))
        print(git('diff', '--', 'HOTONE.md', 'research-state.json', 'scripts/hotone_catalogue.py', 'Makefile', 'ALL-GUITAR.md', 'ALL-BASS.md'))
        raise SystemExit(0)
    assert sys.argv[1:] == ['commit']
    verify()
    comparison_views.verify_views()
    comparison_views.test_readme_brand_counts()
    comparison_views.test_validation_counts()
    assert not git('diff', '--cached', '--name-only').strip(), 'Existing staged changes'
    allowed = {'HOTONE.md','EXPRESSION-VOLUME.md','README.md','MULTI-EFFECTS.md','ALL-GUITAR.md','ALL-BASS.md','ALL-VOCAL.md','research-state.json','scripts/comparison_views.py','scripts/hotone_catalogue.py','Makefile','scripts/research_push.py'}
    changed = set(git('diff','--name-only').splitlines()) | set(git('ls-files','--others','--exclude-standard').splitlines())
    assert changed <= allowed, changed - allowed
    assert not git('diff','--check').strip(), 'Whitespace errors'
    git('add','--',*sorted(changed))
    print(git('diff','--cached','--stat'))
    print(git('commit','-m','research(hotone): count Mini cabinets delays and reverbs'))
