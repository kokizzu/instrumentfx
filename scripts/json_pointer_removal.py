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
    migration=state['migration']
    migration['legacy_reference_files']=[path for path in migration.get('legacy_reference_files',[]) if path in existing_references]
    remaining=markdown_count+(0 if removed else len(PATHS))
    accounting=migration.get('legacy_file_retirement')
    original_count=accounting['original_paths'] if accounting is not None else markdown_count+len(PATHS)
    if accounting is not None:
        accounting['files_remaining']=remaining
    migration['complete']=bool(migration.get('complete')) and remaining==0
    migration['content_consolidation_status']=(f'{original_count} original legacy paths retain root/Git-backed evidence; '
        +f'{remaining} compatibility files remain after JSON pointer '+('removal' if removed else 'restoration')
        +'. Technical and market research remain incomplete.')
    # Cleanup and rollback do not replace independent model-research cursors.


def test_live_metadata():
    for count in (342,344,400):
        for removed in (True,False):
            for markdown_count in (0,114):
                sample=dict(active_model_count=count,cursor={'model':'preserved research','after_queue':'preserved queue'},migration={
                    'complete':True,'legacy_file_retirement':{'original_paths':117,'files_remaining':0},
                    'legacy_reference_files':['effects/research-state.json','effects/RESUME.md']})
                expected_cursor=dict(sample['cursor'])
                existing={'effects/RESUME.md'} if markdown_count else set()
                if not removed:
                    existing.add('effects/research-state.json')
                refresh_live_metadata(sample,removed,markdown_count,existing)
                remaining=markdown_count+(0 if removed else len(PATHS))
                assert sample['cursor']==expected_cursor, 'JSON maintenance changed independent research cursor'
                assert sample['migration']['complete'] is (remaining==0)
                assert sample['migration']['legacy_file_retirement']['files_remaining']==remaining
                assert set(sample['migration']['legacy_reference_files'])==existing
                assert '117' in sample['migration']['content_consolidation_status']
    incomplete={'migration':{'complete':False},'cursor':{}}
    refresh_live_metadata(incomplete,True,0,set())
    assert incomplete['migration']['complete'] is False, 'Cleanup must not auto-certify migration'
    print('PASS: JSON maintenance preserves research cursor andoriginal path count; rollback invalidates completion and updates live file count')


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
                   scope='Only three JSON pointer paths; Markdown retirement state and research queues unchanged')
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
        assert not target.is_symlink() and target.resolve().is_relative_to(ROOT.resolve()), 'Invalid JSON pointer location: '+path
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
                from compatibility_removal import restore_missing
                restore_missing(target,entry['pointer_text'])
            state['migration']['retired_sources'][path]['status'] = 'retired_json_pointer'
        checkpoint['paths'][path] = 'applied'
        CHECKPOINT.write_text(json.dumps(checkpoint,indent=2)+'\n')
    removed = payload['operation'] == 'remove'
    from datetime import datetime
    from zoneinfo import ZoneInfo
    state['migration']['json_pointer_removal'] = dict(status='removed' if removed else 'restored',checked_date=datetime.now(ZoneInfo('Asia/Singapore')).date().isoformat(),records=payload['records'],rollback=payload['rollback'],source_commit=payload['source_commit'],remaining_markdown_compatibility_paths=len(list((ROOT/'effects').rglob('*.md'))))
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
