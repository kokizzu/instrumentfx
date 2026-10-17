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
    paths=sorted(ROOT.glob('*.md'))+sorted((ROOT/'effects').rglob('*.md'))
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
        if shared.digest((ROOT/path).read_text())!=entry['redirect_sha256']:
            errors.append(dict(source=path,error='redirect hash drift'))
        research.read_preserved_source(path)
    report=dict(scope='Every live local inline/reference/shortcut/definition/HTML link in root and effects Markdown;legacy JSON pointer coverage and pinned-original hashes. External availability and arbitrary JavaScript-generated links not certified.',markdown_files=len(paths),local_link_occurrences=len(links),legacy_files=len(legacy),registered_redirects=len(records),separately_verified_archival_redirect=[special],unclassified_legacy_files=unclassified,errors=errors,root_to_legacy_links=sum(l['source'].find('/')<0 and l['target'].startswith('effects/') for l in links))
    # Keep an exact remaining-link census so retirement is based on callers, not model counts.
    from collections import Counter
    boundary = [link for link in links if '/' not in link['source'] and link['target'].startswith('effects/')]
    report['root_to_legacy_by_source'] = dict(sorted(Counter(link['source'] for link in boundary).items()))
    report['root_to_legacy_by_target'] = dict(sorted(Counter(link['target'] for link in boundary).items()))
    report['root_to_legacy_occurrences'] = boundary
    assert sum(report['root_to_legacy_by_source'].values()) == report['root_to_legacy_links']
    REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({key:value for key,value in report.items() if key != 'root_to_legacy_occurrences'},ensure_ascii=False,indent=2))
    assert not errors and not unclassified,'Navigation or redirect coverage incomplete'
    research.verify()
    return report


def save():
    report=audit()
    import metadata_consolidation
    import technical_retirement
    metadata_consolidation.verify()
    technical_retirement.specialist_verify()
    state=json.loads((ROOT/'research-state.json').read_text())
    state['migration']['navigation_audit']=dict(report,checked_date=datetime.now(ZoneInfo('Asia/Singapore')).date().isoformat(),status='passed',remaining='Compatibility paths and preserved historical links intentionally remain;this audit does not certify external offers or full model specifications.')
    state['migration']['content_consolidation_status']='All117 legacy Markdown/JSON paths accounted for;root content and pinned-original checks pass;compatibility redirects remain.'
    state['migration']['complete']=False
    import comparison_views
    comparison_views.verify_views()
    focused = set(comparison_views.BASS_FOCUSED)
    shared_bass = set(comparison_views.BASS_SHARED)
    vocal_only = set(comparison_views.VOCAL_ONLY)
    vocal_shared = set(comparison_views.VOCAL_SHARED)
    assert not focused & shared_bass and not vocal_only & vocal_shared
    membership = state['comparison_membership']
    assert set(membership['ALL-BASS.md']) == focused | shared_bass
    assert set(membership['ALL-VOCAL.md']) == vocal_only | vocal_shared
    state['validation'].update(bass_focused_models=len(focused), bass_shared_models=len(shared_bass), vocal_only_models=len(vocal_only))
    state['migration']['warning']=f"{state['canonical_root_model_count']} root-canonical models;{state['legacy_only_model_count']} legacy-only. Legacy compatibility files remain;specification and market research incomplete."
    state['migration']['root_category_and_instrument_views']=f"Four-table comparisons: {len(membership['ALL-GUITAR.md'])} guitar, {len(membership['ALL-BASS.md'])} documented bass-capable, {len(membership['ALL-VOCAL.md'])} vocal; technical and market verification remain incomplete."
    readme=(ROOT/'README.md').read_text()
    import re
    readme, n1=re.subn(r'All \d+ recorded models have root brand sections\.', f"All {state['canonical_root_model_count']} recorded models have root brand sections.", readme)
    readme, n2=re.subn(r'Organization migration is incomplete:\*\* \d+ detailed models are root-canonical; \d+ still rely on legacy source records\.', f"Organization migration is incomplete:** {state['canonical_root_model_count']} detailed models are root-canonical; {state['legacy_only_model_count']} still rely on legacy source records.", readme)
    assert n1 == n2 == 1, 'README count statements changed; inspect before saving'
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
    allowed={'scripts/navigation_tools.py','scripts/source_retirement.py','scripts/canonical_links.py','scripts/consolidation_tools.py','scripts/technical_retirement.py','MULTI-EFFECTS.md','BOSS.md','MOOER.md','README.md','research-state.json','Makefile','ZOOM.md','ALL-GUITAR.md','ALL-BASS.md','ALL-VOCAL.md'}
    assert changed<=allowed,changed-allowed
    research.git('add','--',*sorted(changed))
    print(research.git('diff','--cached','--stat'))
    print(research.git('commit','-m','docs: migrate BOSS and MOOER navigation with recoverable provenance'))

if __name__=='__main__':
    {'audit':audit,'save':save,'commit':commit}[sys.argv[1] if len(sys.argv)>1 else 'audit']()
