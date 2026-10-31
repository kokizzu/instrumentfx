"""Validate and publish only the reviewed AXOM MAX discovery checkpoint."""
import sys
sys.dont_write_bytecode = True
from research_tools import git, verify, identity
import comparison_views

identity()
verify()
comparison_views.verify_views()
comparison_views.test_readme_brand_counts()
comparison_views.test_validation_counts()
assert not git("diff", "--cached", "--name-only").strip(), "Existing staged work"
allowed = {"RJM-MUSIC.md", "SINGULAR-SOUND.md", "MELOFTY.md", "MULTI-EFFECTS.md", "research-state.json", "Makefile", "scripts/display_audit_melofty.py", "FOOTSWITCH-DISPLAYS.md", "README.md", "MORNINGSTAR.md"}
changed = set(git("diff", "--name-only").splitlines()) | set(git("ls-files", "--others", "--exclude-standard").splitlines())
assert changed <= allowed, changed - allowed
assert not git("diff", "--check").strip()
git("add", "--", *sorted(changed))
print(git("diff", "--cached", "--stat"))
message = "docs: prioritize individual LCD footswitch processors" if sys.argv[1:] == ["collection"] else "research(melofty): qualify current Apple control-app requirements"
if sys.argv[1:] == ["morningstar"]:
    message = "research(morningstar): distinguish MC8 PRO screens and switches"
if "RJM-MUSIC.md" in changed:
    message = "research(rjm): add exact GT16 individual LCD controller"
print(git("commit", "-m", message))
