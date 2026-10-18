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
if sys.argv[1] not in {'inspect','finalize'}:
    assert not git('status','--porcelain'), 'Dirty worktree'
mode = sys.argv[1]
if mode == 'inspect':
    print(git('rev-list','--left-right','--count','HEAD...origin/main'))
    print(git('log','--oneline','HEAD..origin/main'))
    print(git('diff','--stat','HEAD...origin/main'))
    print(git('diff','HEAD...origin/main','--','AGENTS.md','Makefile'))
    names=git('diff','--name-only','HEAD...origin/main').splitlines()
    snapshots={name:{'remote':git('show','origin/main:'+name),'ours':git('show','HEAD:'+name) if name in git('ls-tree','-r','--name-only','HEAD').splitlines() else '', 'base':git('show',git('merge-base','HEAD','origin/main')+':'+name) if name in git('ls-tree','-r','--name-only',git('merge-base','HEAD','origin/main')).splitlines() else ''} for name in names}
    pathlib.Path('/tmp/instrumentfx-remote-review.json').write_text(json.dumps(snapshots))
elif mode == 'finalize':
    sys.dont_write_bytecode=True
    from research_tools import verify
    import comparison_views
    verify()
    comparison_views.verify_views()
    comparison_views.test_readme_brand_counts()
    comparison_views.test_validation_counts()
    names=['DIGITECH.md','EVENTIDE.md','EXPRESSION-VOLUME.md','IK-MULTIMEDIA.md','LINE6.md','NEURAL-DSP.md','README.md','ZOOM.md','STRYMON.md','research-state.json','scripts/research_push.py','Makefile','ALL-GUITAR.md','ALL-BASS.md','ALL-VOCAL.md','MULTI-EFFECTS.md']
    for name in names:
        assert not any(line.startswith(('<<<<<<< ','=======','>>>>>>> ')) for line in (ROOT/name).read_text().splitlines()), name
    subprocess.run(['git','add','--',*names],cwd=ROOT,check=True)
    subprocess.run(['git','commit','-m','Merge origin/main expression research preserving current inventory and all evidence'],cwd=ROOT,check=True)
elif mode == 'sync':
    subprocess.run(['git','merge','--no-edit','origin/main'],cwd=ROOT,check=True)
elif mode == 'plan':
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
