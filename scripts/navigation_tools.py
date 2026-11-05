"""Audit live local links and complete legacy redirect coverage."""
import json
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path
import sys
sys.dont_write_bytecode=True
import source_retirement as shared
import research_tools as research
ROOT=research.ROOT
REPORT=Path('/tmp/instrumentfx-navigation-audit.json')

def audit():
    research.identity()
    state=json.loads((ROOT/'research-state.json').read_text())
    paths=sorted(ROOT.glob('*.md')) + sorted((ROOT/'brand').glob('*.md'))+sorted((ROOT/'effects').rglob('*.md'))
    links=[link for path in paths for link in shared.local_links(str(path.relative_to(ROOT)),path.read_text())]
    errors=[]
    for link in links:
        target=ROOT/link['target']
        if not target.is_file():
            errors.append(dict(**link,error='missing file'))
        elif link['fragment'] and target.suffix=='.md' and link['fragment'] not in shared.anchors(target.read_text()):
            errors.append(dict(**link,error='missing anchor'))
    legacy=sorted(str(p.relative_to(ROOT)) for p in (ROOT/'effects').rglob('*') if p.is_file() and p.suffix in ('.md','.json'))
    records=state['migration']['retired_sources']
    special='effects/findings/2026-10-14-flamma-fv01.md'
    unclassified=[p for p in legacy if p not in records and p!=special]
    for path,entry in records.items():
        if path.endswith('.md'):
            current=research.read_compatibility_redirect(path,state)
            if shared.digest(current)!=entry['redirect_sha256']:
                errors.append(dict(source=path,error='redirect hash drift'))
        elif (ROOT/path).is_file():
            if shared.digest((ROOT/path).read_text())!=entry['redirect_sha256']:
                errors.append(dict(source=path,error='redirect hash drift'))
        else:
            removed=state['migration'].get('json_pointer_removal',{})
            assert removed.get('status')=='removed' and path in removed.get('records',{}), path
        research.read_preserved_source(path)
    report=dict(scope='Every live local inline/reference/shortcut/definition/HTML link in root and effects Markdown;legacy JSON pointer coverage and pinned-original hashes. External availability and arbitrary JavaScript-generated links not certified.',markdown_files=len(paths),local_link_occurrences=len(links),legacy_files=len(legacy),registered_redirects=len(records),separately_verified_archival_redirect=[special] if special not in records else [],unclassified_legacy_files=unclassified,errors=errors,root_to_legacy_links=sum(l['source'].find('/')<0 and l['target'].startswith('effects/') for l in links))
    # Keep an exact remaining-link census so retirement is based on callers, not model counts.
    from collections import Counter
    boundary = [link for link in links if '/' not in link['source'] and link['target'].startswith('effects/')]
    report['root_to_legacy_by_source'] = dict(sorted(Counter(link['source'] for link in boundary).items()))
    report['root_to_legacy_by_target'] = dict(sorted(Counter(link['target'] for link in boundary).items()))
    report['root_to_legacy_occurrences'] = boundary
    assert sum(report['root_to_legacy_by_source'].values()) == report['root_to_legacy_links']
    legacy_links = [link for link in links if link['target'] in set(legacy)]
    callers = {path: [link for link in legacy_links if link['target'] == path] for path in legacy}
    report['legacy_incoming_by_target'] = {path: len(items) for path, items in callers.items()}
    report['legacy_incoming_occurrences'] = legacy_links
    report['legacy_without_local_incoming'] = [path for path, items in callers.items() if not items]
    report['legacy_retention_basis'] = 'Original anchors and path spellings remain in Git-backed provenance; local callers are audited,external historical callers are not certified.'
    assert sum(report['legacy_incoming_by_target'].values()) == len(legacy_links)
    if state['migration'].get('root_navigation_canonical'):
        assert report['root_to_legacy_links'] == 0, 'Root navigation regressed to legacy compatibility paths'
    REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({key:value for key,value in report.items() if key not in ('root_to_legacy_occurrences', 'legacy_incoming_occurrences', 'legacy_incoming_by_target', 'legacy_without_local_incoming')},ensure_ascii=False,indent=2))
    assert not errors and not unclassified,'Navigation or redirect coverage incomplete'
    research.verify()
    return report


def refresh_migration_status(state,report):
    migration=state['migration']
    remaining=report['legacy_files']
    migration['complete']=bool(migration.get('complete')) and remaining==0
    if 'legacy_file_retirement' in migration:
        migration['legacy_file_retirement']['files_remaining']=remaining
    status='Consolidation verified' if migration['complete'] else 'Final consolidation verification pending'
    migration['content_consolidation_status']=(f"{report['registered_redirects']} registered original paths retain root/Git-backed evidence; "
        +f"{remaining} legacy files remain. {status}; technical and market research remain incomplete.")


def test_state():
    for was_complete, remaining, expected in ((True,0,True),(False,0,False),(True,2,False)):
        state={'migration':{'complete':was_complete,'legacy_file_retirement':{'files_remaining':99}},'cursor':{'model':'unchanged'}}
        report={'legacy_files':remaining,'registered_redirects':117}
        refresh_migration_status(state,report)
        assert state['migration']['complete'] is expected
        assert state['migration']['legacy_file_retirement']['files_remaining']==remaining
        assert state['cursor']=={'model':'unchanged'}
    print('PASS: navigation refresh preserves verified migration only with zero legacy files; never auto-promotes completion or changes research cursor')


def save():
    report=audit()
    import metadata_consolidation
    import technical_retirement
    metadata_consolidation.verify()
    technical_retirement.specialist_verify()
    state=json.loads((ROOT/'research-state.json').read_text())
    state['migration']['navigation_audit']=dict(report,checked_date=datetime.now(ZoneInfo('Asia/Singapore')).date().isoformat(),status='passed',remaining='Technical specifications,current stock andexternal availability are not certified by this preservation/navigation audit.')
    refresh_migration_status(state,report)
    import comparison_views
    comparison_views.verify_views()
    focused = set(comparison_views.BASS_FOCUSED)
    shared_bass = set(comparison_views.BASS_SHARED)
    vocal_only = set(comparison_views.VOCAL_ONLY)
    vocal_shared = set(comparison_views.VOCAL_SHARED)
    assert not focused & shared_bass and not vocal_only & vocal_shared
    membership = state['comparison_membership']
    assert set(membership['all-bass.md']) == focused | shared_bass
    assert set(membership['all-vocal.md']) == vocal_only | vocal_shared
    state['validation'].update(bass_focused_models=len(focused), bass_shared_models=len(shared_bass), vocal_only_models=len(vocal_only))
    state['migration'].update(comparison_views.migration_counts(state,membership))
    readme=comparison_views.readme_counts((ROOT/'README.md').read_text(),state,membership)
    shared.atomic_write(ROOT/'README.md',readme)
    # Preserve the model research cursor; navigation maintenance is not a new model task.
    shared.atomic_write(ROOT/'research-state.json',json.dumps(state,ensure_ascii=False,indent=2)+'\n')

def commit():
    audit()
    import metadata_consolidation
    import comparison_views
    metadata_consolidation.verify()
    comparison_views.verify_views()
    assert not research.git('diff','--cached','--name-only').strip(),'Existing staged changes'
    changed=set(research.git('diff','--name-only').splitlines())|set(research.git('ls-files','--others','--exclude-standard').splitlines())
    allowed={'scripts/navigation_tools.py','scripts/source_retirement.py','scripts/canonical_links.py','scripts/consolidation_tools.py','scripts/technical_retirement.py','scripts/research_tools.py','MULTI-EFFECTS.md','brand/BOSS.md','brand/MOOER.md','brand/VALETON.md','brand/M-VAVE.md','README.md','research-state.json','Makefile','brand/ZOOM.md','all-guitar.md','all-bass.md','all-vocal.md'}
    from canonical_links import REMAINING
    allowed.update(REMAINING)
    assert changed<=allowed,changed-allowed
    research.git('add','--',*sorted(changed))
    print(research.git('diff','--cached','--stat'))
    print(research.git('commit','-m','docs: audit remaining legacy compatibility callers'))

if __name__=='__main__':
    {'audit':audit,'save':save,'commit':commit,'test-state':test_state}[sys.argv[1] if len(sys.argv)>1 else 'audit']()
