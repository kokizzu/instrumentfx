"""Validate and publish reviewed Atomic partial catalogue evidence locally."""
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
    allowed = {'ATOMIC-AMPS.md', 'EXPRESSION-VOLUME.md', 'README.md', 'research-state.json', 'scripts/atomic_catalogue.py', 'Makefile'}
    changed = set(git('diff', '--name-only').splitlines()) | set(git('ls-files', '--others', '--exclude-standard').splitlines())
    assert changed and changed <= allowed, changed - allowed
    assert not git('diff', '--check').strip(), 'Whitespace errors'
    print(git('diff', '--', *sorted(changed)))
    git('add', '--', *sorted(changed))
    print(git('diff', '--cached', '--stat'))
    print(git('commit', '-m', 'research(atomic): add qualified Ampli-Firebox MK II partial lead'))
