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
if sys.argv[1] not in {'inspect','finalize','auth-check','stage-transport','commit-transport'}:
    assert not git('status','--porcelain'), 'Dirty worktree'
mode = sys.argv[1]
def remote_git(*args):
    # Per-command transport override: never rewrite the saved upstream URL.
    prefix = ['git']
    if mode in {'plan-https', 'apply-https'}:
        prefix += ['-c', 'url.https://github.com/.insteadOf=git@github.com:',
                   '-c', 'credential.helper=', '-c', 'credential.helper=!gh auth git-credential']
    return subprocess.check_output(prefix + list(args), cwd=ROOT, text=True).strip()

if mode in {'stage-transport', 'commit-transport'}:
    import hashlib
    paths = ['Makefile', 'scripts/research_push.py']
    receipt = pathlib.Path('/tmp/instrumentfx-transport-review.json')
    compile((ROOT / paths[1]).read_text(), paths[1], 'exec')
    subprocess.run(['git','diff','--check'], cwd=ROOT, check=True)
    if mode == 'stage-transport':
        assert not git('diff','--cached','--name-only'), 'Existing staged work'
        assert set(git('diff','--name-only').splitlines()) == set(paths), 'Unexpected unstaged files'
        assert not git('ls-files','--others','--exclude-standard'), 'Untracked files need review'
        subprocess.run(['git','add','--',*paths], cwd=ROOT, check=True)
        diff = git('diff','--cached')
        receipt.write_text(json.dumps({'head':git('rev-parse','HEAD'),'hash':hashlib.sha256(diff.encode()).hexdigest()}))
        print(diff)
    else:
        saved = json.loads(receipt.read_text())
        assert not git('diff','--name-only'), 'Unstaged work'
        assert set(git('diff','--cached','--name-only').splitlines()) == set(paths)
        assert saved['head'] == git('rev-parse','HEAD')
        assert saved['hash'] == hashlib.sha256(git('diff','--cached').encode()).hexdigest()
        subprocess.run(['git','diff','--cached','--check'], cwd=ROOT, check=True)
        subprocess.run(['git','commit','-m','build: support reviewed HTTPS publication with GitHub CLI credentials'], cwd=ROOT, check=True)
elif mode == 'auth-check':
    import shutil
    import os
    result = {'ssh_agent_socket_present': bool(os.environ.get('SSH_AUTH_SOCK')), 'gh_available': bool(shutil.which('gh'))}
    for label, command in [('gh_authenticated', ['gh','auth','status','--hostname','github.com']), ('ssh_agent_has_keys', ['ssh-add','-l'])]:
        try:
            result[label] = subprocess.run(command, cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=20).returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            result[label] = False
    print(json.dumps(result, indent=2))
elif mode == 'inspect':
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
    names=['brand/DIGITECH.md','brand/EVENTIDE.md','EXPRESSION-VOLUME.md','brand/IK-MULTIMEDIA.md','brand/LINE6.md','brand/NEURAL-DSP.md','README.md','brand/ZOOM.md','brand/STRYMON.md','research-state.json','scripts/research_push.py','Makefile','all-guitar.md','all-bass.md','all-vocal.md','MULTI-EFFECTS.md']
    for name in names:
        assert not any(line.startswith(('<<<<<<< ','=======','>>>>>>> ')) for line in (ROOT/name).read_text().splitlines()), name
    subprocess.run(['git','add','--',*names],cwd=ROOT,check=True)
    subprocess.run(['git','commit','-m','Merge origin/main expression research preserving current inventory and all evidence'],cwd=ROOT,check=True)
elif mode == 'sync':
    subprocess.run(['git','merge','--no-edit','origin/main'],cwd=ROOT,check=True)
elif mode in {'plan','plan-https'}:
    remote_git('fetch','origin','main')
    ahead, behind = map(int,git('rev-list','--left-right','--count','HEAD...origin/main').split())
    assert behind == 0, 'Remote has new commits; inspect before pushing'
    data = {'head':git('rev-parse','HEAD'),'remote':git('rev-parse','origin/main'),'ahead':ahead,'behind':behind,'transport':'https' if mode == 'plan-https' else 'ssh'}
    PLAN.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))
elif mode in {'apply','apply-https'}:
    data=json.loads(PLAN.read_text())
    assert git('rev-parse','HEAD') == data['head'], 'Re-plan changed head'
    assert git('rev-parse','origin/main') == data['remote'], 'Re-plan changed remote'
    assert data.get('transport','ssh') == ('https' if mode == 'apply-https' else 'ssh'), 'Re-plan transport change'
    remote_git('push','origin','main:main')
    assert remote_git('ls-remote','origin','refs/heads/main').split()[0] == data['head']
    print('Verified remote main matches reviewed local commit')
else:
    raise SystemExit('Use plan or apply')
