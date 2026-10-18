"""Remove only reviewed, fully preserved legacy JSON pointers; retain Markdown anchors."""
import hashlib
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
import research_tools
import source_retirement as retirement

ROOT = retirement.ROOT
PLAN = Path('/tmp/instrumentfx-json-pointer-removal-plan.json')
CHECKPOINT = Path('/tmp/instrumentfx-json-pointer-removal-checkpoint.json')
PATHS = retirement.JSON_PATHS
TOOLS = ('scripts/json_pointer_removal.py', 'scripts/source_retirement.py', 'Makefile')


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def assert_scope(records):
    assert set(records) == set(PATHS), 'Selection must be the three preserved JSON pointers'
    for path, entry in records.items():
        assert path.startswith('effects/') and Path(path).suffix == '.json'
        assert '..' not in Path(path).parts
        assert entry['path'] == path
        assert entry['sha256'] == digest(entry['pointer_text'])


def refresh_live_metadata(state, removed, markdown_count, existing_references):
    migration = state['migration']
    migration['legacy_reference_files'] = [
        path for path in migration.get('legacy_reference_files', [])
        if path in existing_references
    ]
    original_count = markdown_count + len(PATHS)
    if removed:
        migration['content_consolidation_status'] = (
            f'All{original_count} original legacy paths accounted for;three JSON pointers removed '
            f'after typed root reconstruction;{markdown_count} Markdown compatibility files '
            'retained for historical anchors. Overall migration and technical research remain incomplete.'
        )
        task = ('Three redundant JSON pointers removed after exact typed-content verification; '
                'Markdown redirects remain for historical anchors. Continue technical research '
                'and audit remaining compatibility layout.')
    else:
        migration['content_consolidation_status'] = (
            f'All{original_count} legacy compatibility paths retained after JSON pointer rollback;'
            'typed root reconstruction remains verified.'
        )
        task = ('Three JSON pointers restored from reviewed exact bytes; Markdown redirects '
                'remain for historical anchors. Continue technical research and compatibility audit.')
    state['cursor'].update(
        model='Legacy JSON pointer cleanup', task=task,
        after_queue=f"{state['active_model_count']} partial unique models; Markdown compatibility paths retained. No downloads/workflows/push."
    )


def test_live_metadata():
    # Exercise metadata only: no pointer deletion/restoration or filesystem writes.
    for count in (342, 344, 400):
        for removed in (True, False):
            sample = dict(active_model_count=count, cursor={}, migration={
                'legacy_reference_files':['effects/research-state.json','effects/RESUME.md']})
            existing = {'effects/RESUME.md'}
            if not removed:
                existing.add('effects/research-state.json')
            refresh_live_metadata(sample, removed, 114, existing)
            assert sample['cursor']['after_queue'].startswith(str(count)+' partial')
            assert set(sample['migration']['legacy_reference_files']) == existing
            assert ('removed' if removed else 'restored') in sample['cursor']['task']
            assert '117' in sample['migration']['content_consolidation_status']


def verify():
    test_live_metadata()
    retirement.json_verify()
    state = json.loads((ROOT/'research-state.json').read_text())
    evidence = state['migration'].get('json_pointer_removal')
    if evidence is None:
        print('JSON pointers not removed; preservation verification passed.')
        return
    assert_scope(evidence['records'])
    for path in state['migration'].get('legacy_reference_files', []):
        assert (ROOT/path).is_file(), 'Missing live legacy reference: '+path
    removed = evidence['status'] == 'removed'
    for path, entry in evidence['records'].items():
        if removed:
            assert not (ROOT/path).exists(), path
            assert state['migration']['retired_sources'][path]['status'] == 'removed_json_pointer'
        else:
            assert (ROOT/path).read_text() == entry['pointer_text'], path
    assert not retirement.json_incoming(), 'Incoming Markdown links to removed pointers'
    print('PASS: exact three JSON pointer paths, pinned originals, typed root content and zero incoming Markdown links.')


def plan(rollback=False):
    research_tools.identity()
    verify()
    assert not research_tools.git('diff','--cached','--name-only').strip(), 'Existing staged changes'
    assert not retirement.json_incoming(), 'Incoming links require canonicalization first'
    state = json.loads((ROOT/'research-state.json').read_text())
    old = state['migration'].get('json_pointer_removal')
    records = {}
    for path in PATHS:
        entry = state['migration']['retired_sources'][path]
        if rollback:
            assert old and old['status'] == 'removed'
            records[path] = old['records'][path]
            assert not (ROOT/path).exists()
        else:
            assert entry['status'] == 'retired_json_pointer', path
            target = ROOT/path
            assert target.is_file() and not target.is_symlink()
            text = target.read_text()
            assert text == retirement.json_pointer(path,entry)
            records[path] = dict(path=path, sha256=digest(text), pointer_text=text)
    assert_scope(records)
    inputs = {p:digest((ROOT/p).read_text()) for p in (*TOOLS,'research-state.json')}
    payload = dict(operation='restore' if rollback else 'remove', inputs=inputs, records=records,
                   source_commit=research_tools.git('rev-parse','HEAD').strip(),
                   rollback='make json-pointer-rollback-plan then make json-pointer-removal-apply',
                   scope='Only three JSON pointers; all Markdown redirects and historical anchors retained')
    PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(plan=str(PLAN),operation=payload['operation'],exact_paths=[dict(path=p,sha256=e['sha256'],bytes=len(e['pointer_text'].encode())) for p,e in records.items()],incoming_markdown_links=0,original_and_typed_root_content_verified=True,rollback=payload['rollback']),indent=2))


def apply():
    research_tools.identity()
    payload = json.loads(PLAN.read_text())
    assert_scope(payload['records'])
    assert payload['operation'] in ('remove','restore')
    assert not retirement.json_incoming(), 'Incoming links changed'
    for path, expected in payload['inputs'].items():
        assert digest((ROOT/path).read_text()) == expected, 'Changed input: '+path
    plan_sha = digest(PLAN.read_text())
    checkpoint = json.loads(CHECKPOINT.read_text()) if CHECKPOINT.exists() else {}
    resume = checkpoint.get('plan_sha256') == plan_sha
    for path, entry in payload['records'].items():
        target = ROOT/path
        if payload['operation'] == 'remove':
            assert (resume and not target.exists()) or (target.is_file() and not target.is_symlink() and digest(target.read_text()) == entry['sha256']), 'Changed pointer: '+path
        else:
            assert not target.exists() or (resume and target.read_text() == entry['pointer_text']), 'Restore collision: '+path
    checkpoint = dict(plan_sha256=plan_sha,operation=payload['operation'],paths={p:'pending' for p in PATHS})
    CHECKPOINT.write_text(json.dumps(checkpoint,indent=2)+'\n')
    # Reconstruct every original and compare typed data before deleting anything.
    state = json.loads((ROOT/'research-state.json').read_text())
    for path in PATHS:
        original = json.loads(research_tools.read_preserved_source(path))
        snapshot = state['public_metadata']['legacy_json']['source_index'][path]['snapshot']
        groups = state['public_metadata']['legacy_json']['unique_snapshots'][snapshot]['groups']
        restored = {key:value for group in groups.values() for key,value in group.items()}
        assert original == restored, 'Typed content changed: '+path
    for path, entry in payload['records'].items():
        target = ROOT/path
        if payload['operation'] == 'remove':
            if target.exists():
                target.unlink()
            state['migration']['retired_sources'][path]['status'] = 'removed_json_pointer'
        else:
            if not target.exists():
                target.write_text(entry['pointer_text'])
            state['migration']['retired_sources'][path]['status'] = 'retired_json_pointer'
        checkpoint['paths'][path] = 'applied'
        CHECKPOINT.write_text(json.dumps(checkpoint,indent=2)+'\n')
    removed = payload['operation'] == 'remove'
    state['migration']['json_pointer_removal'] = dict(status='removed' if removed else 'restored',checked_date='2026-10-18',records=payload['records'],rollback=payload['rollback'],source_commit=payload['source_commit'],remaining_markdown_compatibility_paths=len(list((ROOT/'effects').rglob('*.md'))))
    state['migration']['legacy_json_retirement'].update(pointer_files_removed=removed,no_source_deletion=not removed)
    refresh_live_metadata(state, removed, len(list((ROOT/'effects').rglob('*.md'))),
                          {p for p in state['migration'].get('legacy_reference_files', []) if (ROOT/p).is_file()})
    retirement.atomic_write(ROOT/'research-state.json',json.dumps(state,ensure_ascii=False,indent=2)+'\n')
    verify()


def commit():
    verify()
    research_tools.verify()
    import comparison_views
    comparison_views.verify_views()
    assert not research_tools.git('diff','--cached','--name-only').strip(), 'Existing staged changes'
    changed = set(research_tools.git('diff','--name-only').splitlines()) | set(research_tools.git('ls-files','--others','--exclude-standard').splitlines())
    allowed = set(PATHS)|set(TOOLS)|{'research-state.json'}
    assert changed <= allowed, changed-allowed
    research_tools.git('add','--',*sorted(changed))
    print(research_tools.git('diff','--cached','--stat'))
    print(research_tools.git('commit','-m','fix: keep live migration references and cleanup cursors current'))


if __name__ == '__main__':
    {'plan':plan,'apply':apply,'verify':verify,'commit':commit,'rollback-plan':lambda:plan(True)}[sys.argv[1]]()
