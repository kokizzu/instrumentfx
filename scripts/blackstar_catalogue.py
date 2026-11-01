"""Validate and commit the reviewed Blackstar catalogue integration locally."""
import sys
from pathlib import Path
sys.dont_write_bytecode = True
from research_tools import git, verify
import comparison_views

if __name__ == '__main__':
    assert sys.argv[1:] == ['commit']
    verify()
    comparison_views.verify_views()
    assert not git('diff', '--cached', '--name-only').strip(), 'Existing staged changes'
    allowed = {'FRACTAL-AUDIO.md', 'BLACKSTAR.md', 'README.md', 'MULTI-EFFECTS.md', 'ALL-GUITAR.md', 'ALL-BASS.md', 'ALL-VOCAL.md', 'research-state.json', 'scripts/comparison_views.py', 'scripts/blackstar_catalogue.py', 'Makefile'}
    changed = set(git('diff', '--name-only').splitlines()) | set(git('ls-files', '--others', '--exclude-standard').splitlines())
    assert changed <= allowed, changed - allowed
    assert not git('diff', '--check').strip(), 'Whitespace errors'
    if 'FRACTAL-AUDIO.md' in changed:
        previous = git('show', 'HEAD:FRACTAL-AUDIO.md')
        current = Path('FRACTAL-AUDIO.md').read_text()
        assert previous.split() == current.split(), 'Unrelated Fractal content changed'
    print(git('diff', '--', *sorted(changed)))
    git('add', '--', *sorted(changed))
    print(git('diff', '--cached', '--stat'))
    print(git('commit', '-m', 'research(blackstar): preserve distinct Floor Two discovery lead'))
