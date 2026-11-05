"""Exact-preview technical redirect removal and restoration; no broad deletion."""
import hashlib
import json
import re
from pathlib import Path
import sys
sys.dont_write_bytecode = True
import research_tools as research
import technical_retirement as technical
import source_retirement as shared

ROOT = research.ROOT
PLAN = Path('/tmp/instrumentfx-compatibility-operation.json')
CHECKPOINT = Path('/tmp/instrumentfx-compatibility-operation-checkpoint.json')


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def observed(path):
    target = ROOT/path
    assert not target.is_symlink(), 'Symlink is not an operation target: '+path
    assert target.resolve().is_relative_to(ROOT.resolve()), 'Path escapes repository'
    return digest(target.read_text()) if target.exists() else None


def validate_observations(before, live, after, resuming=False):
    """Validate the complete selection before performing the first mutation."""
    assert set(live) == set(before), 'File inventory changed since preview'
    assert set(after) <= set(before), 'Unreviewed output path'
    for path, expected in before.items():
        allowed = {expected}
        if resuming and path in after:
            allowed.add(after[path])
        assert live[path] in allowed, 'Changed reviewed input: '+path


def operation_paths(extra=(), names=None):
    assert set(extra) <= set(technical.SOURCES), 'Unknown technical operation path'
    if names is None:
        names = research.git('ls-files', '-z', '--cached', '--others', '--exclude-standard').split('\0')
    return sorted(set(filter(None, names)) | set(extra))


def select_redirect_commit(path, head, tracked_in_head, pins):
    commit = head if path in tracked_in_head else pins[path]['redirect_commit']
    assert re.fullmatch(r'[0-9a-f]{40}', commit), 'Invalid saved redirect pin'
    return commit


def build_outputs(before, action, items):
    state = json.loads(before['research-state.json'])
    removed = state['migration'].setdefault('removed_technical_redirects', {})
    if action == 'remove':
        for item in items:
            assert item['path'] not in removed
            removed[item['path']] = dict(redirect_commit=item['redirect_commit'],
                                         redirect_sha256=item['redirect_sha256'])
    else:
        for item in items:
            assert removed[item['path']]['redirect_sha256'] == item['redirect_sha256']
            del removed[item['path']]
    pins = state['migration'].get('technical_compatibility_removal', {}).get('redirect_pins', {}).copy()
    pins.update({item['path']: dict(redirect_commit=item['redirect_commit'], redirect_sha256=item['redirect_sha256']) for item in items})
    state['migration']['technical_compatibility_removal'] = dict(
        redirect_pins=pins,
        status='partial' if removed else 'restored', removed_paths=sorted(removed),
        original_evidence='Pinned original sources and canonical brand/shared evidence remain unchanged.',
        remaining='Metadata/specialist compatibility and independent technical research remain unfinished.',
        rollback='make technical-compatibility-restore-plan; review exact preview; make technical-compatibility-operation-apply')
    readme = before['README.md']
    old = 'Historical link spellings remain recoverable through mappings in `research-state.json`; legacy compatibility files preserve old anchors and pinned-source provenance. Their continued presence means the overall migration remains incomplete.'
    new = 'Historical link spellings and pinned-source provenance remain recoverable through `research-state.json` and Git. Remaining legacy compatibility files mean the overall migration is still incomplete.'
    if action == 'remove':
        assert old in readme or new in readme, 'README navigation paragraph changed'
        readme = readme.replace(old, new)
    return {'research-state.json': json.dumps(state, ensure_ascii=False, indent=2)+'\n', 'README.md': readme}


def plan(action):
    research.identity()
    assert action in ('remove', 'restore')
    assert not research.git('diff', '--cached', '--name-only').strip(), 'Existing staged work'
    head = research.git('rev-parse', 'HEAD').strip()
    state = json.loads((ROOT/'research-state.json').read_text())
    removed = state['migration'].get('removed_technical_redirects', {})
    selected = sorted(set(technical.SOURCES) - set(removed) if action == 'remove' else removed)
    assert selected and set(selected) <= set(technical.SOURCES)
    if action == 'remove':
        history = json.loads(Path('/tmp/instrumentfx-source-history-audit.json').read_text())
        assert history['head'] == head and history['sources'] == len(technical.SOURCES), 'Refresh current history audit'
        assert not history['counts'].get('historical-variant-needs-review', 0)
        assert not technical.incoming(), 'Legacy links must be resolved before removal'
    items = []
    tracked_in_head = set(research.git('ls-tree', '-r', '--name-only', head).splitlines())
    pins = state['migration'].get('technical_compatibility_removal', {}).get('redirect_pins', {})
    for path in selected:
        record = state['migration']['retired_sources'][path]
        text = research.read_compatibility_redirect(path, state)
        assert text == technical.redirect(path, research.read_preserved_source(path), record['source_commit'])
        assert digest(text) == record['redirect_sha256']
        if action == 'remove' and path not in tracked_in_head:
            assert pins[path]['redirect_sha256'] == record['redirect_sha256'], 'Saved redirect hash mismatch'
        commit = select_redirect_commit(path, head, tracked_in_head, pins) if action == 'remove' else removed[path]['redirect_commit']
        assert digest(research.git('show', commit+':'+path)) == digest(text)
        items.append(dict(path=path, redirect_commit=commit, redirect_sha256=digest(text), body=text))
    before_text = {path: (ROOT/path).read_text() for path in ('research-state.json', 'README.md')}
    outputs = build_outputs(before_text, action, items)
    paths = operation_paths(selected)
    assert set(selected) <= set(paths), 'Selection must remain tracked before publication'
    before = {path: observed(path) for path in paths}
    after = {path: digest(text) for path, text in outputs.items()}
    after.update({item['path']: None if action == 'remove' else item['redirect_sha256'] for item in items})
    payload = dict(head=head, action=action, items=items, inputs=before,
                   before_text=before_text, outputs=outputs, after=after)
    PLAN.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(dict(plan=str(PLAN), action=action, paths=[x['path'] for x in items],
                          count=len(items), rollback='Pinned exact redirect bodies in plan and Git', mutated=0), indent=2))



def restore_missing(target, text):
    """Publish a complete restored file atomically, refusing an existing path."""
    import os
    import tempfile
    with tempfile.NamedTemporaryFile('w', dir=target.parent, prefix='.'+target.name+'.', delete=False) as stream:
        stream.write(text)
        temporary = Path(stream.name)
    try:
        os.chmod(temporary, 0o644)
        os.link(temporary, target)
    finally:
        temporary.unlink()


def save_checkpoint(checkpoint):
    text = json.dumps(checkpoint, indent=2)+'\n'
    if CHECKPOINT.exists():
        shared.atomic_write(CHECKPOINT, text)
    else:
        restore_missing(CHECKPOINT, text)

def apply():
    research.identity()
    assert not research.git('diff', '--cached', '--name-only').strip(), 'Staging changed since preview'
    raw = PLAN.read_text()
    payload = json.loads(raw)
    assert research.git('rev-parse', 'HEAD').strip() == payload['head'], 'HEAD changed since preview'
    assert payload['action'] in ('remove', 'restore')
    paths = [item['path'] for item in payload['items']]
    assert paths and paths == sorted(set(paths)) and set(paths) <= set(technical.SOURCES)
    assert payload['outputs'] == build_outputs(payload['before_text'], payload['action'], payload['items'])
    assert set(payload['after']) == set(paths) | {'research-state.json', 'README.md'}
    expected_after = {path: digest(text) for path, text in payload['outputs'].items()}
    expected_after.update({item['path']: None if payload['action'] == 'remove' else item['redirect_sha256'] for item in payload['items']})
    assert payload['after'] == expected_after, 'Unreviewed output hashes'
    for path, text in payload['before_text'].items():
        assert digest(text) == payload['inputs'][path], 'Original ledger/navigation hash changed'
    original_state = json.loads(payload['before_text']['research-state.json'])
    for item in payload['items']:
        assert re.fullmatch(r'[0-9a-f]{40}', item['redirect_commit']), 'Invalid pinned redirect commit'
        assert original_state['migration']['retired_sources'][item['path']]['redirect_sha256'] == item['redirect_sha256']
        assert digest(item['body']) == item['redirect_sha256']
        assert research.git('show', item['redirect_commit']+':'+item['path']) == item['body']
    checkpoint = json.loads(CHECKPOINT.read_text()) if CHECKPOINT.exists() else {}
    resuming = checkpoint.get('plan_sha256') == digest(raw) and checkpoint.get('started') is True
    names = operation_paths(paths)
    assert set(names) == set(payload['inputs']), 'Tracked/untracked file inventory changed'
    validate_observations(payload['inputs'], {p: observed(p) for p in names}, payload['after'], resuming)
    checkpoint = dict(plan_sha256=digest(raw), started=True, complete=False, action=payload['action'], paths={p:'pending' for p in paths})
    save_checkpoint(checkpoint)
    # The ledger records explicit intent first. An interruption is resumed only
    # with the same plan digest; unrelated edits are rejected before replay.
    for path, text in payload['outputs'].items():
        shared.atomic_write(ROOT/path, text)
    for item in payload['items']:
        target = ROOT/item['path']
        if payload['action'] == 'remove':
            if target.exists():
                assert observed(item['path']) == item['redirect_sha256']
                target.unlink()
        else:
            if target.exists():
                assert observed(item['path']) == item['redirect_sha256']
            else:
                restore_missing(target, item['body'])
        checkpoint['paths'][item['path']] = 'removed' if payload['action'] == 'remove' else 'restored'
        save_checkpoint(checkpoint)
    for path, expected in payload['after'].items():
        assert observed(path) == expected, 'Operation result differs from preview: '+path
    checkpoint['complete'] = True
    save_checkpoint(checkpoint)
    print('PASS: exact reviewed '+payload['action']+' completed for '+str(len(paths))+' paths; checkpoint '+str(CHECKPOINT))


def test():
    assert operation_paths(['effects/bass.md'], ['README.md']) == ['README.md', 'effects/bass.md']
    assert select_redirect_commit('effects/bass.md', 'a'*40, set(), {'effects/bass.md': {'redirect_commit': 'b'*40}}) == 'b'*40
    assert select_redirect_commit('effects/bass.md', 'a'*40, {'effects/bass.md'}, {}) == 'a'*40
    import tempfile
    with tempfile.TemporaryDirectory(prefix='instrumentfx-restore-test-') as directory:
        target = Path(directory)/'redirect.md'
        restore_missing(target, 'exact redirect\n')
        assert target.read_text() == 'exact redirect\n'
        try:
            restore_missing(target, 'overwrite attempt')
        except FileExistsError:
            pass
        else:
            raise AssertionError('Restore overwrote an existing file')
        assert target.read_text() == 'exact redirect\n'
    before = {'effects/a.md':'a', 'effects/b.md':'b', 'research-state.json':'old'}
    after = {'effects/a.md':None, 'effects/b.md':None, 'research-state.json':'new'}
    validate_observations(before, dict(before), after)
    partial = dict(before, **{'effects/a.md':None, 'research-state.json':'new'})
    validate_observations(before, partial, after, True)
    for bad, resume in ((partial, False), (dict(before, **{'effects/b.md':'user edit'}), False),
                        (dict(before, **{'extra.md':'extra'}), False),
                        (dict(partial, **{'effects/b.md':'user edit'}), True)):
        try:
            validate_observations(before, bad, after, resume)
        except AssertionError:
            pass
        else:
            raise AssertionError('Unreviewed mutation or accidental absence accepted')
    restore_before = {p: None if p.startswith('effects/') else 'new' for p in before}
    validate_observations(restore_before, dict(restore_before), before)
    validate_observations(restore_before, dict(restore_before, **{'effects/a.md':'a'}), before, True)
    print('PASS: removal/restore validation rejects drift, unreviewed paths and accidental absence; exact interrupted operations can resume')


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'test':
        test()
    elif mode in ('remove-plan', 'restore-plan'):
        plan(mode.split('-')[0])
    elif mode == 'apply':
        apply()
    else:
        raise SystemExit('Unknown operation')
