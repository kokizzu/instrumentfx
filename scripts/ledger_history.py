"""Preview root-level ledger changes against the preceding commit."""
import json
import subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
assert "git@github.com:kokizzu/instrumentfx.git" in (ROOT / ".git/config").read_text()
previous = json.loads(subprocess.check_output(["git", "show", "HEAD~1:research-state.json"], cwd=ROOT, text=True))
current = json.loads((ROOT / "research-state.json").read_text())
changed = {key: previous[key] for key in previous if previous[key] != current.get(key)}
preview = Path("/tmp/instrumentfx-ledger-prior.json")
preview.write_text(json.dumps(changed, ensure_ascii=False, indent=2) + "\n")
print("Prior values saved:", preview)
print("Changed root keys:", ", ".join(changed))
