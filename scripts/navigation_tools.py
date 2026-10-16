"""Audit live local links and complete legacy redirect coverage."""
import json
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
    REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))
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
    state['migration']['navigation_audit']=dict(report,checked_date='2026-10-17',status='passed',remaining='Compatibility paths and preserved historical links intentionally remain;this audit does not certify external offers or full model specifications.')
    state['migration']['content_consolidation_status']='All117 legacy Markdown/JSON paths accounted for;root content and pinned-original checks pass;compatibility redirects remain.'
    state['migration']['complete']=False
    state['migration']['warning']='135 root-canonical models;0 legacy-only. Legacy compatibility files remain;specification and market research incomplete.'
    state['cursor'].update(model='Fresh Shopee discovery and remaining model fields',task='Navigation audit passed across146 Markdown files/2029 local link occurrences;117 legacy paths accounted for. Do not repeat completed source retirement. Resume fresh Shopee Indonesia discovery by brand/series and model-specific manufacturer gaps,committing each model before the next.',after_queue='Unknown fields and qualified historical prices remain explicit;no exhaustive market or stock claim. Keep legacy redirects until a separate reviewed cleanup is warranted.')
    shared.atomic_write(ROOT/'research-state.json',json.dumps(state,ensure_ascii=False,indent=2)+'\n')

def commit():
    audit()
    import metadata_consolidation
    import comparison_views
    metadata_consolidation.verify()
    comparison_views.verify_views()
    assert not research.git('diff','--cached','--name-only').strip(),'Existing staged changes'
    changed=set(research.git('diff','--name-only').splitlines())|set(research.git('ls-files','--others','--exclude-standard').splitlines())
    allowed={'scripts/navigation_tools.py','scripts/source_retirement.py','README.md','research-state.json','Makefile'}
    assert changed<=allowed,changed-allowed
    research.git('add','--',*sorted(changed))
    print(research.git('diff','--cached','--stat'))
    print(research.git('commit','-m','docs: audit all legacy navigation and reconcile migration status'))

if __name__=='__main__':
    {'audit':audit,'save':save,'commit':commit}[sys.argv[1] if len(sys.argv)>1 else 'audit']()
