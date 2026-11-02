"""Validate and commit reviewed display-processor and controller research."""
import sys
sys.dont_write_bytecode = True
from research_tools import git, verify, identity
import comparison_views

identity()
verify()
comparison_views.verify_views()
comparison_views.test_readme_brand_counts()
comparison_views.test_validation_counts()
if sys.argv[1:] in (["stage-collection"], ["collection"]):
    import hashlib
    import json
    from pathlib import Path
    allowed = {"MELOFTY.md", "FOOTSWITCH-DISPLAYS.md", "MULTI-EFFECTS.md", "README.md", "research-state.json", "scripts/display_audit_melofty.py", "Makefile"}
    changed = set(git("diff", "--name-only").splitlines()) | set(git("ls-files", "--others", "--exclude-standard").splitlines())
    staged = set(git("diff", "--cached", "--name-only").splitlines())
    assert (changed | staged) <= allowed, (changed | staged) - allowed
    review_path = Path("/tmp/instrumentfx-display-staged-review.json")
    assert not git("diff", "--check").strip()
    if sys.argv[1:] == ["stage-collection"]:
        assert changed and not staged, "Existing staging or no changes"
        git("add", "--", *sorted(changed))
        diff = git("diff", "--cached")
        Path("/tmp/instrumentfx-display-staged.diff").write_text(diff)
        review_path.write_text(json.dumps({"head": git("rev-parse", "HEAD").strip(), "sha256": hashlib.sha256(diff.encode()).hexdigest()}))
        print(git("diff", "--cached", "--stat"))
        print("Review /tmp/instrumentfx-display-staged.diff before make research-commit-display-collection")
    else:
        assert staged and not changed, "Stage and review all intended changes first"
        review = json.loads(review_path.read_text())
        assert review["head"] == git("rev-parse", "HEAD").strip()
        assert review["sha256"] == hashlib.sha256(git("diff", "--cached").encode()).hexdigest()
        assert not git("diff", "--cached", "--check").strip()
        message = "research(melofty): distinguish screen census and performance-switch roles" if "MELOFTY.md" in staged else "docs: restore requested separate-screen processor priority"
        print(git("commit", "-m", message))
    raise SystemExit(0)

assert not git("diff", "--cached", "--name-only").strip(), "Existing staged work"
allowed = {"GIGRIG.md", "FAMC.md", "RJM-MUSIC.md", "SINGULAR-SOUND.md", "MELOFTY.md", "MULTI-EFFECTS.md", "research-state.json", "Makefile", "scripts/display_audit_melofty.py", "FOOTSWITCH-DISPLAYS.md", "EXPRESSION-VOLUME.md", "README.md", "MORNINGSTAR.md"}
changed = set(git("diff", "--name-only").splitlines()) | set(git("ls-files", "--others", "--exclude-standard").splitlines())
assert changed <= allowed, changed - allowed
assert not git("diff", "--check").strip()
git("add", "--", *sorted(changed))
print(git("diff", "--cached", "--stat"))
message = "docs: compare LCD shortlist headphones and preset controls" if sys.argv[1:] == ["collection"] else "research(melofty): qualify independent firmware 1.9 review leads"
if sys.argv[1:] == ["morningstar"]:
    message = "research(morningstar): distinguish MC8 PRO screens and switches"
if "RJM-MUSIC.md" in changed:
    message = "research(rjm): document GT10 supported pedal and toe connection"
if "SINGULAR-SOUND.md" in changed:
    message = "research(singular): qualify MIDI Maestro iOS 26 firmware advisory"
if sys.argv[1:] == ["famc"]:
    assert "FAMC.md" in changed, "Missing FAMC controller record"
    message = "research(famc): collect JR+ individual-display candidate with limits"
if "GIGRIG.md" in changed:
    message = "research(gigrig): collect G3S OLED controller with display conflict"
print(git("commit", "-m", message))
