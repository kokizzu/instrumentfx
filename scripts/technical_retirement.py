"""Retire verified technical findings through exact preview/apply and Git rollback."""
import json
from pathlib import Path
import sys
sys.dont_write_bytecode = True
import research_tools as research
import consolidation_tools as consolidation
import comparison_views
import source_retirement as shared

ROOT = research.ROOT
SOURCE = 'effects/findings/2026-10-15-zoom-g6.md'
DESTINATION = 'ZOOM.md#g6'
PLAN = Path('/tmp/instrumentfx-technical-retirement-plan.json')
TOOLS = ['scripts/technical_retirement.py','scripts/consolidation_tools.py','Makefile']

def incoming():
    return [link for path in sorted(ROOT.glob('*.md'))+sorted((ROOT/'effects').rglob('*.md'))
            for link in shared.local_links(str(path.relative_to(ROOT)),path.read_text()) if link['target']==SOURCE]

def redirect(original, commit):
    headings = shared.headings(original)
    target = '../../'+DESTINATION
    text = headings[0]+'\n\nThis technical finding is consolidated in [the complete root model record]('+target+'). Original dates, prices, qualifications and unresolved contradictions remain there.\n\n'
    text += 'Pinned original: '+chr(96)+commit+':'+SOURCE+chr(96)+'. SHA-256: '+chr(96)+shared.digest(original)+chr(96)+'.\n\n'
    for heading in headings[1:]:
        text += heading+'\n\n[Read the preserved technical evidence]('+target+').\n\n'
    assert shared.headings(text)==headings
    assert shared.anchors(text)==shared.anchors(original)
    return text

def verify():
    research.identity()
    state=json.loads((ROOT/'research-state.json').read_text())
    consolidation.verify_preserved(state)
    entry=state['migration'].get('retired_sources',{}).get(SOURCE)
    original=research.read_preserved_source(SOURCE)
    manifest=[e for e in state['consolidation_and_price_findings'] if e.get('source')==SOURCE and e.get('verification_kind')=='complete-source-body-v1']
    assert len(manifest)==1 and manifest[0]['destination']==DESTINATION
    assert shared.digest(original)==manifest[0]['source_sha256']
    shared.validate_target(DESTINATION)
    if entry:
        current=(ROOT/SOURCE).read_text()
        assert current==redirect(original,entry['source_commit'])
        assert shared.digest(current)==entry['redirect_sha256']
        assert shared.headings(current)==entry['original_headings']
    for link in incoming():
        assert not link['fragment'] or link['fragment'] in shared.anchors((ROOT/SOURCE).read_text()), str(link)
    print('PASS: G6 complete original body, root destination and all incoming anchors preserved;retired='+str(bool(entry)))

def plan(rollback=False):
    verify()
    state=json.loads((ROOT/'research-state.json').read_text())
    records=state['migration'].setdefault('retired_sources',{})
    original=research.read_preserved_source(SOURCE)
    if rollback:
        assert SOURCE in records
        del records[SOURCE]
        content=original
        state['migration']['technical_retirement']['status']='rolled_back'
    else:
        assert SOURCE not in records
        commit=research.git('rev-parse','HEAD').strip()
        assert research.git('show',commit+':'+SOURCE)==original
        content=redirect(original,commit)
        records[SOURCE]=dict(source_commit=commit,source_sha256=shared.digest(original),redirect_sha256=shared.digest(content),destination=DESTINATION,original_headings=shared.headings(original),incoming_before=incoming(),status='retired_technical_redirect',rollback='make technical-retirement-rollback-plan then make technical-retirement-apply')
        state['migration']['technical_retirement']=dict(status='partial',sources=[SOURCE],remaining='Other technical legacy sources still require retirement audits;research remains incomplete.')
    state['migration']['root_category_and_instrument_views']='Four-table comparisons:113 guitar,62 documented bass-capable,17 vocal;remaining technical retirement and field verification incomplete.'
    state['migration']['warning']='0 legacy-only models;135 root-canonical. Full migration and research incomplete.'
    state['cursor']['model']='Technical source retirement'
    state['cursor']['task']='G6 legacy finding '+('restoration planned' if rollback else 'redirect preserves every old heading and full pinned original;continue with other fully consolidated findings and shared-source navigation audits')+'. Technical gaps and fresh Shopee discovery remain.'
    state['cursor']['after_queue']='Technical rollback: make technical-retirement-rollback-plan then make technical-retirement-apply;metadata rollback targets remain available.'
    outputs={SOURCE:content,'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n'}
    inputs={p:shared.digest((ROOT/p).read_text()) for p in [SOURCE,'research-state.json','ZOOM.md',*TOOLS]}
    PLAN.write_text(json.dumps(dict(kind='rollback' if rollback else 'retire',inputs=inputs,outputs=outputs),ensure_ascii=False,indent=2)+'\n')
    print('Exact plan: '+str(PLAN)+'; '+json.dumps(list(outputs))+'; incoming='+str(len(incoming())))

def apply():
    research.identity()
    payload=json.loads(PLAN.read_text())
    assert set(payload['outputs'])=={SOURCE,'research-state.json'}
    for path,sha in payload['inputs'].items():
        live=shared.digest((ROOT/path).read_text())
        already_written=path in payload['outputs'] and live==shared.digest(payload['outputs'][path])
        assert live==sha or already_written,'Changed input: '+path
    # Ledger first enables pinned-original readers before the stub is installed.
    for path in ['research-state.json',SOURCE]:
        shared.atomic_write(ROOT/path,payload['outputs'][path])
    verify()

def commit():
    verify()
    research.verify()
    comparison_views.verify_views()
    assert not research.git('diff','--cached','--name-only').strip(),'Existing staged changes'
    allowed=set(TOOLS+[SOURCE,'research-state.json'])
    changed=set(research.git('diff','--name-only').splitlines())|set(research.git('ls-files','--others','--exclude-standard').splitlines())
    assert changed<=allowed,changed-allowed
    research.git('add','--',*sorted(allowed))
    print(research.git('diff','--cached','--stat'))
    print(research.git('commit','-m','docs(zoom): retire G6 legacy finding with pinned evidence and stable anchors'))

if __name__=='__main__':
    {'plan':plan,'apply':apply,'verify':verify,'commit':commit,'rollback-plan':lambda:plan(True)}[sys.argv[1]]()
