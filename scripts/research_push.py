"""Preview and push main without force or workflow operations."""
import json
import pathlib
import subprocess
import sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
PLAN = pathlib.Path('/tmp/instrumentfx-push-plan.json')
def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()
assert git('branch','--show-current') == 'main'
assert git('remote','get-url','origin') == 'git@github.com:kokizzu/instrumentfx.git'
assert not git('status','--porcelain'), 'Dirty worktree'
mode = sys.argv[1]
if mode == 'plan':
    subprocess.run(['git','fetch','origin','main'], cwd=ROOT, check=True)
    ahead, behind = map(int,git('rev-list','--left-right','--count','HEAD...origin/main').split())
    assert behind == 0, 'Remote has new commits; inspect before pushing'
    data = {'head':git('rev-parse','HEAD'),'remote':git('rev-parse','origin/main'),'ahead':ahead,'behind':behind}
    PLAN.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))
elif mode == 'apply':
    data=json.loads(PLAN.read_text())
    assert git('rev-parse','HEAD') == data['head'], 'Re-plan changed head'
    assert git('rev-parse','origin/main') == data['remote'], 'Re-plan changed remote'
    subprocess.run(['git','push','origin','main:main'],cwd=ROOT,check=True)
    assert git('ls-remote','origin','refs/heads/main').split()[0] == data['head']
    print('Verified remote main matches reviewed local commit')
else:
    raise SystemExit('Use plan or apply')
