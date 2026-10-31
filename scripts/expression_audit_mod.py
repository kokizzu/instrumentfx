"""Validate and commit reviewed MOD Audio research; no workflows."""
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
    allowed = {'MOD-AUDIO.md', 'README.md', 'MULTI-EFFECTS.md', 'ALL-GUITAR.md', 'ALL-BASS.md', 'ALL-VOCAL.md', 'scripts/comparison_views.py', 'FOOTSWITCH-DISPLAYS.md', 'EXPRESSION-VOLUME.md', 'research-state.json', 'scripts/expression_audit_mod.py', 'Makefile'}
    changed = set(git('diff', '--name-only').splitlines()) | set(git('ls-files', '--others', '--exclude-standard').splitlines())
    assert changed and changed <= allowed, changed - allowed
    assert not git('diff', '--check').strip(), 'Whitespace errors'
    git('add', '--', *sorted(changed))
    print(git('diff', '--cached', '--stat'))
    print(git('commit', '-m', 'research(mod): add original Duo partial profile to instrument comparisons'))
