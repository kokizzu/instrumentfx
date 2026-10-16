"""Preview/apply lossless retirement of complete-body technical findings."""
import json
from pathlib import Path
import sys
sys.dont_write_bytecode = True
import research_tools as research
import consolidation_tools as consolidation
import comparison_views
import source_retirement as shared
ROOT = research.ROOT
SOURCES = {
  "effects/findings/2026-10-14-zoom-b1xon.md": "ZOOM.md#b1xon",
  "effects/findings/2026-10-15-zoom-g6.md": "ZOOM.md#g6",
  "effects/findings/2026-10-14-zoom-g1-four.md": "ZOOM.md#g1-four",
  "effects/findings/2026-10-14-zoom-g1x-four.md": "ZOOM.md#g1x-four",
  "effects/findings/2026-10-14-zoom-g2-four.md": "ZOOM.md#g2-four",
  "effects/findings/2026-10-14-zoom-g2x-four.md": "ZOOM.md#g2x-four",
  "effects/findings/2026-10-15-boss-gt1000core-display-idr.md": "BOSS.md#gt-1000core",
  "effects/findings/2026-10-15-boss-gx10-display-idr.md": "BOSS.md#gx-10",
  "effects/findings/2026-10-15-boss-gt1-display-idr.md": "BOSS.md#gt-1",
  "effects/findings/2026-10-15-boss-gx1-display-idr.md": "BOSS.md#gx-1",
  "effects/findings/2026-10-15-boss-me90-display-idr.md": "BOSS.md#me-90",
  "effects/findings/2026-10-15-boss-gx100-display-idr.md": "BOSS.md#gx-100",
  "effects/findings/2026-10-15-boss-gt1000-display-idr.md": "BOSS.md#gt-1000",
  "effects/findings/2026-10-14-line6-hx-stomp-xl.md": "LINE6.md#hx-stomp-xl",
  "effects/findings/2026-10-14-hotone-ampero-mini.md": "HOTONE.md#ampero-mini-mp-50",
  "effects/findings/2026-10-14-hotone-ampero-mp100.md": "HOTONE.md#ampero-mp-100",
  "effects/findings/2026-10-14-hotone-ampero-ii-mp350.md": "HOTONE.md#ampero-ii-mp-350",
  "effects/findings/2026-10-14-hotone-ampero-ii-stage-mp380.md": "HOTONE.md#ampero-ii-stage-mp-380",
  "effects/findings/2026-10-15-hotone-ampero-ii-stomp-mp300.md": "HOTONE.md#ampero-ii-stomp-mp-300",
  "effects/findings/2026-10-14-mooer-ge100.md": "MOOER.md#ge100-original",
  "effects/findings/2026-10-14-mooer-ge150.md": "MOOER.md#ge150-original",
  "effects/findings/2026-10-14-mooer-ge200.md": "MOOER.md#ge200-original",
  "effects/findings/2026-10-14-mooer-ge150-pro-li.md": "MOOER.md#ge150-pro-li",
  "effects/findings/2026-10-14-mooer-ge100-pro.md": "MOOER.md#ge100-pro",
  "effects/findings/2026-10-14-mooer-ge100-pro-li.md": "MOOER.md#ge100-pro-li",
  "effects/findings/2026-10-14-mooer-ge200-pro.md": "MOOER.md#ge200-pro",
  "effects/findings/2026-10-14-mooer-ge200-pro-li.md": "MOOER.md#ge200-pro-li",
  "effects/findings/2026-10-14-mooer-ge150-pro.md": "MOOER.md#ge150-pro",
  "effects/findings/2026-10-15-mooer-ge150-plus.md": "MOOER.md#ge150-plus",
  "effects/findings/2026-10-15-mooer-ge150-plus-li.md": "MOOER.md#ge150-plus-li",
  "effects/findings/2026-10-15-mooer-ge150-max.md": "MOOER.md#ge150-max",
  "effects/findings/2026-10-15-mooer-ge150-max-li.md": "MOOER.md#ge150-max-li",
  "effects/findings/2026-10-14-mooer-ge1000.md": "MOOER.md#ge1000",
  "effects/findings/2026-10-15-mooer-ge1000-li.md": "MOOER.md#ge1000-li",
  "effects/findings/2026-10-14-valeton-gp-100.md": "VALETON.md#gp-100",
  "effects/findings/2026-10-14-valeton-gp-150.md": "VALETON.md#gp-150",
  "effects/findings/2026-10-14-valeton-gp-180.md": "VALETON.md#gp-180",
  "effects/findings/2026-10-14-valeton-gp-5.md": "VALETON.md#gp-5",
  "effects/findings/2026-10-14-valeton-gp-50.md": "VALETON.md#gp-50",
  "effects/findings/2026-10-15-audota-ame-100.md": "AUDOTA.md#ame-100",
  "effects/findings/2026-10-15-audota-ame-200.md": "AUDOTA.md#ame-200",
  "effects/findings/2026-10-15-audota-ame-200-pro.md": "AUDOTA.md#ame-200-pro",
  "effects/findings/2026-10-15-audota-ace-100.md": "AUDOTA.md#ace-100",
  "effects/findings/2026-10-15-audota-ave-100.md": "AUDOTA.md#ave-100",
  "effects/findings/2026-10-14-boin-audio-bg300.md": "BOIN-AUDIO.md#bg300",
  "effects/findings/2026-10-14-scorpion-kmf-10.md": "SCORPION.md#kmf-10",
  "effects/findings/2026-10-14-tchelicon-voicelive-play.md": "TC-HELICON.md#voicelive-play",
  "effects/findings/2026-10-14-tchelicon-play-acoustic.md": "TC-HELICON.md#play-acoustic",
  "effects/findings/2026-10-15-cuvave-h8.md": "CUVAVE.md#h8",
  "effects/findings/2026-10-15-ving-fb100.md": "VING.md#flybro-fb-100",
  "effects/findings/2026-10-14-roland-gr-55.md": "ROLAND.md#gr-55",
  "effects/findings/2026-10-15-line6-pod-express-guitar.md": "LINE6.md#pod-express-guitar",
  "effects/findings/2026-10-15-line6-pod-express-bass.md": "LINE6.md#pod-express-bass",
  "effects/findings/2026-10-15-zoom-g11.md": "ZOOM.md#g11",
  "effects/findings/2026-10-14-donner-arena2000.md": "DONNER.md#arena2000",
  "effects/findings/2026-10-14-flamma-fx100.md": "FLAMMA.md#fx100",
  "effects/findings/2026-10-14-flamma-fx200.md": "FLAMMA.md#fx200",
  "effects/findings/2026-10-14-headrush-core.md": "HEADRUSH.md#core",
  "effects/findings/2026-10-15-joyo-gembox-original.md": "JOYO.md#gem-box-original",
  "effects/findings/2026-10-14-joyo-gembox-ii.md": "JOYO.md#gem-box-ii",
  "effects/findings/2026-10-14-joyo-gembox-iii.md": "JOYO.md#gem-box-iii",
  "effects/findings/2026-10-15-line6-pod-go.md": "LINE6.md#pod-go-and-pod-go-wireless",
  "effects/findings/2026-10-15-line6-pod-go-wireless.md": "LINE6.md#pod-go-and-pod-go-wireless",
  "effects/findings/2026-10-14-mvave-tank-g.md": "M-VAVE.md#tank-g",
  "effects/findings/2026-10-14-mvave-tank-b.md": "M-VAVE.md#tank-b",
  "effects/findings/2026-10-14-mvave-tank-mini.md": "M-VAVE.md#tank-mini",
  "effects/findings/2026-10-14-mvave-mk-20.md": "M-VAVE.md#mk-20",
  "effects/findings/2026-10-14-mvave-mk-300.md": "M-VAVE.md#mk-300",
  "effects/findings/2026-10-14-mvave-tank-pro.md": "M-VAVE.md#tank-pro",
  "effects/findings/2026-10-14-mvave-ann-blackbox.md": "M-VAVE.md#ann-blackbox",
  "effects/findings/2026-10-15-mvave-mini-x.md": "M-VAVE.md#mini-x",
  "effects/findings/2026-10-15-mvave-pocket-amp.md": "M-VAVE.md#pocket-amp",
  "effects/findings/2026-10-15-mvave-cube-baby-ac.md": "M-VAVE.md#cube-baby-ac",
  "effects/findings/2026-10-15-mvave-cube-baby-bass.md": "M-VAVE.md#cube-baby-bass",
  "effects/findings/2026-10-14-nux-mg-100.md": "NUX.md#mg-100",
  "effects/findings/2026-10-14-nux-mg-200.md": "NUX.md#mg-200",
  "effects/findings/2026-10-15-nux-trident.md": "NUX.md#trident-nme-5",
  "effects/findings/2026-10-14-sonicake-matribox.md": "SONICAKE.md#matribox-qme-50",
  "effects/findings/2026-10-14-sonicake-smart-box.md": "SONICAKE.md#smart-box-qme-20",
  "effects/findings/2026-10-14-sonicake-pocket-master.md": "SONICAKE.md#pocket-master-qme-10",
  "effects/findings/2026-10-15-mvave-cube-baby.md": "M-VAVE.md#cube-baby-electric"
}
SHARED = {
  "effects/guitar-compact.md": "shared_compact_audit",
  "effects/guitar-floorboards.md": "shared_floorboard_audit",
  "effects/guitar-nux.md": "shared_nux_audit",
  "effects/bass.md": "shared_bass_audit",
  "effects/vocal.md": "shared_vocal_audit",
  "effects/advanced-modelers.md": "shared_advanced_audit",
  "effects/guitar-boss.md": "shared_boss_audit",
  "effects/guitar-boss.history-2026-10-14.md": "shared_boss_history_audit",
  "effects/audota.md": "shared_audota_audit",
  "effects/cube-baby.md": "shared_cube_audit",
  "effects/owned-multifx.md": "shared_owned_audit",
  "effects/shopee-multifx.md": "shared_market1_audit",
  "effects/shopee-multifx-2.md": "shared_market2_audit",
  "effects/shopee-multifx-3.md": "shared_market3_audit",
  "effects/shopee-multifx-4.md": "shared_market4_audit",
  "effects/shopee-multifx-5.md": "shared_market5_audit",
  "effects/shopee-multifx-6.md": "shared_market6_audit",
  "effects/shopee-multifx-7.md": "shared_market7_audit"
}
SOURCES.update({
  "effects/guitar-compact.md": "MULTI-EFFECTS.md",
  "effects/guitar-floorboards.md": "MULTI-EFFECTS.md",
  "effects/guitar-nux.md": "NUX.md",
  "effects/bass.md": "ALL-BASS.md",
  "effects/vocal.md": "ALL-VOCAL.md",
  "effects/advanced-modelers.md": "MULTI-EFFECTS.md",
  "effects/guitar-boss.md": "BOSS.md",
  "effects/guitar-boss.history-2026-10-14.md": "BOSS.md",
  "effects/audota.md": "AUDOTA.md",
  "effects/cube-baby.md": "M-VAVE.md",
  "effects/owned-multifx.md": "MULTI-EFFECTS.md",
  "effects/shopee-multifx.md": "MULTI-EFFECTS.md",
  "effects/shopee-multifx-2.md": "MULTI-EFFECTS.md",
  "effects/shopee-multifx-3.md": "MULTI-EFFECTS.md",
  "effects/shopee-multifx-4.md": "MULTI-EFFECTS.md",
  "effects/shopee-multifx-5.md": "MULTI-EFFECTS.md",
  "effects/shopee-multifx-6.md": "MULTI-EFFECTS.md",
  "effects/shopee-multifx-7.md": "MULTI-EFFECTS.md"
})
PLAN = Path('/tmp/instrumentfx-technical-retirement-plan.json')
TOOLS = ['scripts/technical_retirement.py','scripts/consolidation_tools.py','scripts/research_tools.py','Makefile']

def incoming():
    return [link for path in sorted(ROOT.glob('*.md'))+sorted((ROOT/'effects').rglob('*.md'))
            for link in shared.local_links(str(path.relative_to(ROOT)),path.read_text()) if link['target'] in SOURCES]

def redirect(path,original,commit):
    headings=shared.headings(original)
    target=('../'*len(Path(path).parent.parts))+SOURCES[path]
    text=headings[0]+'\n\nThis technical finding is consolidated in [the complete root model record]('+target+'). Original dates, prices, qualifications and unresolved contradictions remain there.\n\n'
    text+='Pinned original: '+chr(96)+commit+':'+path+chr(96)+'. SHA-256: '+chr(96)+shared.digest(original)+chr(96)+'.\n\n'
    for heading in headings[1:]:
        text+=heading+'\n\n[Read the preserved technical evidence]('+target+').\n\n'
    assert shared.headings(text)==headings and shared.anchors(text)==shared.anchors(original)
    return text

def verify():
    research.identity()
    state=json.loads((ROOT/'research-state.json').read_text())
    consolidation.verify_preserved(state)
    consolidation.audit_compact_union()
    consolidation.audit_floorboard_union()
    for kind in ('nux','bass','vocal','advanced'):
        consolidation.audit_nux_union(kind=kind)
    consolidation.audit_boss_shared()
    consolidation.audit_boss_shared(history=True)
    consolidation.audit_audota_union()
    for kind in ('cube','owned','market1','market2','market3','market4','market5','market6','market7'):
        consolidation.audit_shared_variant_union(kind=kind)
    records=state['migration'].get('retired_sources',{})
    retired=0
    for path,destination in SOURCES.items():
        original=research.read_preserved_source(path)
        if path in SHARED:
            audit=state['migration'][SHARED[path]]
            assert audit['complete_source_read']
            assert shared.digest(original)==audit['source_sha256'],path
        else:
            manifests=[e for e in state['consolidation_and_price_findings'] if e.get('source')==path and e.get('verification_kind')=='complete-source-body-v1']
            assert len(manifests)==1 and manifests[0]['destination']==destination
            assert not manifests[0].get('source_section'),'Partial source not eligible: '+path
            assert shared.digest(original)==manifests[0]['source_sha256'],path
        shared.validate_target(destination)
        if path in records:
            entry=records[path]
            current=(ROOT/path).read_text()
            assert current==redirect(path,original,entry['source_commit']),path
            assert shared.digest(current)==entry['redirect_sha256'],path
            assert shared.headings(current)==entry['original_headings'],path
            retired+=1
    links=incoming()
    for link in links:
        assert not link['fragment'] or link['fragment'] in shared.anchors((ROOT/link['target']).read_text()),str(link)
    print('PASS: '+str(len(SOURCES))+' technical sources; '+str(retired)+' retired; '+str(len(links))+' incoming link occurrences; every original heading/root destination preserved.')

def plan(rollback=False):
    verify()
    state=json.loads((ROOT/'research-state.json').read_text())
    records=state['migration'].setdefault('retired_sources',{})
    selected=[p for p in SOURCES if (p in records)==rollback]
    assert selected,'No matching sources to plan'
    links=incoming()
    outputs={}
    commit=research.git('rev-parse','HEAD').strip()
    for path in selected:
        original=research.read_preserved_source(path)
        if rollback:
            outputs[path]=original
            del records[path]
            if path in SHARED:
                state['migration'][SHARED[path]]['source_retired']=False
        else:
            assert research.git('show',commit+':'+path)==original,path
            outputs[path]=redirect(path,original,commit)
            records[path]=dict(source_commit=commit,source_sha256=shared.digest(original),redirect_sha256=shared.digest(outputs[path]),destination=SOURCES[path],original_headings=shared.headings(original),incoming_before=[l for l in links if l['target']==path],status='retired_technical_redirect',rollback='make technical-retirement-rollback-plan then make technical-retirement-apply')
    for path in SHARED:
        if path in records:
            state['migration'][SHARED[path]].update(source_retired=True,remaining_work='Redirect and all original heading anchors verified;technical research remains partial.')
    retired=[p for p in SOURCES if p in records]
    state['migration']['technical_retirement']=dict(status='partial' if retired else 'rolled_back',sources=retired,complete_body_finding_count=len(SOURCES)-len(SHARED),shared_source_count=len(SHARED),remaining='Excluded archival finding, remaining technical/navigation sources and legacy JSON audits remain;research remains incomplete.')
    state['cursor']['model']='Shared technical source retirement'
    state['cursor']['task']=str(len(retired))+' technical sources redirect with all old headings and pinned originals. Next audit remaining legacy technical/navigation files and preserved JSON snapshots. Technical gaps and fresh Shopee discovery remain.'
    state['cursor']['after_queue']='Technical rollback: make technical-retirement-rollback-plan then make technical-retirement-apply;metadata rollback targets remain available.'
    outputs['research-state.json']=json.dumps(state,ensure_ascii=False,indent=2)+'\n'
    inputs={p:shared.digest((ROOT/p).read_text()) for p in sorted(set(SOURCES)|set(TOOLS)|{'research-state.json'}|{d.split('#')[0] for d in SOURCES.values()})}
    # Also guard navigation scanned during preview against concurrent edits.
    for path in sorted(ROOT.glob('*.md'))+sorted((ROOT/'effects').rglob('*.md')):
        inputs[str(path.relative_to(ROOT))]=shared.digest(path.read_text())
    PLAN.write_text(json.dumps(dict(kind='rollback' if rollback else 'retire',selected=selected,inputs=inputs,outputs=outputs),ensure_ascii=False,indent=2)+'\n')
    print('Exact plan: '+str(PLAN)+'; '+str(len(selected))+' source paths: '+json.dumps(selected))

def apply():
    research.identity()
    payload=json.loads(PLAN.read_text())
    selected=payload['selected']
    assert selected and len(selected)==len(set(selected)) and set(selected)<=set(SOURCES)
    assert set(payload['outputs'])==set(selected)|{'research-state.json'}
    for path,sha in payload['inputs'].items():
        live=shared.digest((ROOT/path).read_text())
        already_written=path in payload['outputs'] and live==shared.digest(payload['outputs'][path])
        assert live==sha or already_written,'Changed input: '+path
    # Ledger first enables pinned readers. Replay accepts only exact reviewed outputs.
    for path in ['research-state.json',*selected]:
        shared.atomic_write(ROOT/path,payload['outputs'][path])
    verify()

def commit():
    verify()
    research.verify()
    comparison_views.verify_views()
    assert not research.git('diff','--cached','--name-only').strip(),'Existing staged changes'
    allowed=set(TOOLS)|set(SOURCES)|{'research-state.json'}
    changed=set(research.git('diff','--name-only').splitlines())|set(research.git('ls-files','--others','--exclude-standard').splitlines())
    assert changed<=allowed,changed-allowed
    research.git('add','--',*sorted(changed))
    print(research.git('diff','--cached','--stat'))
    print(research.git('commit','-m','docs: retire audited shared technical sources with pinned evidence'))


SPECIALIST = 'effects/specialist.md'
SPECIALIST_PLAN = Path('/tmp/instrumentfx-specialist-retirement-plan.json')
SPECIALIST_MARKER = '<!-- specialist page context begins -->'

def specialist_context(original):
    prefix=original.split('\n## Eligible record: BOSS GM-800\n',1)[0].split('\n',1)[1]
    tail='\n## Excluded archive — not part of the multi-effects comparison\n'+original.split('\n## Excluded archive — not part of the multi-effects comparison\n',1)[1]
    text=comparison_views.relink(prefix+tail,SPECIALIST,{})
    import re
    return re.sub(r'^(#{2,5}) ',r'\1# ',text,flags=re.M)

def specialist_stub(original,commit):
    text=''
    for index,heading in enumerate(shared.headings(original)):
        target='BOSS.md#gm-800' if index<2 else 'SINGLE-GUITAR.md'
        if heading.startswith('### '):
            candidate=next(iter(shared.anchors(heading)))
            target+=' #'+candidate
            target=target.replace(' #','#')
        shared.validate_target(target)
        text+=heading+'\n\n[Complete root evidence](../'+target+'). GM-800 remains eligible; dedicated effects remain excluded.\n\n'
        if index==0:
            text+='Original source: '+chr(96)+commit+':'+SPECIALIST+chr(96)+'; SHA-256 '+chr(96)+shared.digest(original)+chr(96)+'.\n\n'
    assert shared.headings(text)==shared.headings(original)
    return text

def specialist_incoming():
    return [link for path in sorted(ROOT.glob('*.md'))+sorted((ROOT/'effects').rglob('*.md')) for link in shared.local_links(str(path.relative_to(ROOT)),path.read_text()) if link['target']==SPECIALIST]

def specialist_verify():
    research.identity()
    state=json.loads((ROOT/'research-state.json').read_text())
    consolidation.verify_preserved(state)
    research.verify()
    original=research.read_preserved_source(SPECIALIST)
    record=state['migration'].get('retired_sources',{}).get(SPECIALIST)
    if record:
        boss=(ROOT/'BOSS.md').read_text()
        body=boss.split(SPECIALIST_MARKER+'\n',1)[1].split('<!-- specialist page context ends -->',1)[0]
        assert body==specialist_context(original)
        assert (ROOT/SPECIALIST).read_text()==specialist_stub(original,record['source_commit'])
        assert shared.digest((ROOT/SPECIALIST).read_text())==record['redirect_sha256']
    for link in specialist_incoming():
        assert not link['fragment'] or link['fragment'] in shared.anchors((ROOT/SPECIALIST).read_text()),str(link)
    print('PASS: GM-800 complete section, excluded original archive, specialist context and incoming anchors;retired='+str(bool(record)))

def specialist_plan():
    specialist_verify()
    state=json.loads((ROOT/'research-state.json').read_text())
    assert SPECIALIST not in state['migration']['retired_sources']
    original=(ROOT/SPECIALIST).read_text()
    commit=research.git('rev-parse','HEAD').strip()
    assert research.git('show',commit+':'+SPECIALIST)==original
    boss=(ROOT/'BOSS.md').read_text()
    assert SPECIALIST_MARKER not in boss
    before,section=boss.split('\n## GM-800\n',1)
    body,separator,after=section.partition('\n## ')
    context='\n### Preserved specialist scope and archive navigation\n\nHistorical page context;original technical snapshot and excluded-scope wording retained.\n\n'+SPECIALIST_MARKER+'\n'+specialist_context(original)+'<!-- specialist page context ends -->\n'
    boss=before+'\n## GM-800\n'+body+context+(separator+after if separator else '')
    stub=specialist_stub(original,commit)
    state['migration']['retired_sources'][SPECIALIST]=dict(source_commit=commit,source_sha256=shared.digest(original),redirect_sha256=shared.digest(stub),destination='BOSS.md#gm-800',original_headings=shared.headings(original),incoming_before=specialist_incoming(),status='retired_specialist_redirect',context_destination='BOSS.md#preserved-specialist-scope-and-archive-navigation',excluded_destination='SINGLE-GUITAR.md')
    state['cursor'].update(model='Legacy JSON and navigation audit',task='Specialist page now preserves GM-800 body,full original excluded archive and remaining scope/navigation context in root documents. All technical legacy Markdown pages are redirects;verify remaining JSON snapshots and complete navigation coverage. Technical gaps and fresh Shopee discovery remain.')
    outputs={SPECIALIST:stub,'BOSS.md':boss,'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n'}
    inputs={p:shared.digest((ROOT/p).read_text()) for p in [*outputs,'SINGLE-GUITAR.md','SINGLE-VOCAL.md','scripts/technical_retirement.py','Makefile']}
    SPECIALIST_PLAN.write_text(json.dumps(dict(inputs=inputs,outputs=outputs,rollback=dict(source_commit=commit,exact_paths=list(outputs),method='Restore these exact files from pinned source_commit before any later edits;original Git blobs are retained')),ensure_ascii=False,indent=2)+'\n')
    print('Exact specialist plan: '+str(SPECIALIST_PLAN)+';paths='+json.dumps(list(outputs)))

def specialist_apply():
    research.identity()
    payload=json.loads(SPECIALIST_PLAN.read_text())
    assert set(payload['outputs'])=={SPECIALIST,'BOSS.md','research-state.json'}
    for path,sha in payload['inputs'].items():
        live=(ROOT/path).read_text()
        assert shared.digest(live)==sha or payload['outputs'].get(path)==live,'Changed input: '+path
    for path in ['BOSS.md','research-state.json',SPECIALIST]:
        shared.atomic_write(ROOT/path,payload['outputs'][path])
    specialist_verify()

def specialist_commit():
    specialist_verify()
    comparison_views.verify_views()
    assert not research.git('diff','--cached','--name-only').strip(),'Existing staged work'
    changed=set(research.git('diff','--name-only').splitlines())|set(research.git('ls-files','--others','--exclude-standard').splitlines())
    allowed={SPECIALIST,'BOSS.md','research-state.json','scripts/technical_retirement.py','Makefile'}
    assert changed<=allowed,changed-allowed
    research.git('add','--',*sorted(changed))
    print(research.git('diff','--cached','--stat'))
    print(research.git('commit','-m','docs(boss): complete specialist scope consolidation and legacy redirects'))

if __name__=='__main__':
    {'plan':plan,'apply':apply,'verify':verify,'commit':commit,'rollback-plan':lambda:plan(True),'specialist-plan':specialist_plan,'specialist-apply':specialist_apply,'specialist-verify':specialist_verify,'specialist-commit':specialist_commit}[sys.argv[1]]()
