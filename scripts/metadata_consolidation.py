"""Preserve public ownership/policy source semantics in the root ledger."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

sys.dont_write_bytecode = True
import research_tools

ROOT = Path(__file__).resolve().parent.parent
PLAN = Path('/tmp/instrumentfx-metadata-plan.json')
SOURCES = ('effects/OWNERSHIP.md','effects/OWNERSHIP.history-2026-10-14.md','effects/SCOPE.md','effects/METHODOLOGY.md','effects/shopee-indonesia.md','effects/shopee-indonesia.history-2026-10-14.md','effects/shopee-indonesia.history-2026-10-15-pre-boss.md',"effects/COVERAGE.md","effects/COVERAGE.history-2026-10-14.md","effects/COVERAGE.history-2026-10-15-pre-boss.md","effects/README.md","effects/RESUME.md","effects/MIGRATION.md")
JSON_SOURCES = ('effects/research-state.history-2026-10-14.json','effects/research-state.history-2026-10-15-pre-cube-baby.json','effects/research-state.json')
OWNED = ('Boin Audio::BG300','Sonicake::Matribox QME-50','BOSS::GM-800','Roland::GR-55','Line 6::HX Effects','M-VAVE::MK-300','JOYO::GEM BOX III','NUX::MG-101','M-VAVE::MK-20','Scorpion::KMF-10','JOYO::GEM BOX II','JOYO::GEM BOX original',None,'M-VAVE::MINI-X','M-VAVE::Pocket Amp','CUVAVE::H8','Zoom::B1Xon','MOOER::GE100 original','VING::Flybro FB-100','Sonicake::Pocket Master QME-10','Audota::AME-100')
PATHS = ('scripts/metadata_consolidation.py','Makefile','README.md','research-state.json')

def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()

def parse_source(path):
    text = (ROOT/path).read_text()
    lines = text.splitlines()
    blocks, covered = [], set()
    i, context = 0, ''
    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue
        start = i
        heading = re.match(r'^(#{1,6}) (.+)$', lines[i])
        if heading:
            context = heading[2]
            block = dict(kind='heading',level=len(heading[1]),text=context)
            i += 1
        elif i+1 < len(lines) and lines[i].startswith('|') and re.fullmatch(r'\|[\s:|\-]+\|',lines[i+1]):
            headers = [c.strip() for c in lines[i].strip('|').split('|')]
            alignment = lines[i+1]
            i += 2
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                row = [c.strip() for c in lines[i].strip('|').split('|')]
                assert len(row) == len(headers), path+': malformed table row'
                rows.append(dict(zip(headers,row)))
                i += 1
            block = dict(kind='table',headers=headers,alignment=alignment,rows=rows)
        else:
            values = []
            while i < len(lines) and lines[i].strip() and not re.match(r'^#{1,6} ',lines[i]):
                if i > start and i+1 < len(lines) and lines[i].startswith('|') and re.fullmatch(r'\|[\s:|\-]+\|',lines[i+1]):
                    break
                values.append(lines[i])
                i += 1
            assert values, path+': unparsed source line'
            block = dict(kind='paragraph',text='\n'.join(values))
        assert not covered.intersection(range(start,i))
        covered.update(range(start,i))
        block.update(context=context,line=start+1,end_line=i)
        blocks.append(block)
    required = {i for i,line in enumerate(lines) if line.strip()}
    assert required <= covered, path+': dropped nonblank source lines'
    return dict(source=path,sha256=digest(text),historical=True,not_active_instructions=True,nonblank_lines=len(required),blocks=blocks)


def parse_json_provenance():
    snapshots, index = {}, {}
    categories = {
        'requirements_and_template': {'latest_user_requirements','required_field_groups','record_template','record_template_is_not_an_actual_model','record_template_source','validation_rules','size_bins_mm'},
        'model_inventory_and_commits': {'pages','completed_review_batches','latest_findings','recovered_findings','integration_commits','previous_findings_preserved','inventory_validation','baseline_research_commit','latest_integrated_research_commit','latest_marketplace_index_commit'},
        'conflicts_and_coverage': {'known_conflicts_to_preserve','latest_unresolved','previous_unresolved_retained','retained_conflict_topics','migration_status','marketplace_status'},
        'historical_navigation': {'read_first','methodology','backlog','marketplace_index','cursor','owned_cursor','deferred_cursor'},
        'repository_transfer': {'legacy_misplaced_research','history'},
        'change_history': {'change_log','change_log_latest'},
    }
    def inspect(value):
        if isinstance(value,str):
            assert not re.search(r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}',value,re.I), 'Private email identifier in legacy source'
            assert not re.search(r'mail\.google\.com|outlook\.(live|office)\.com',value,re.I), 'Private mailbox link in legacy source'
        elif isinstance(value,dict):
            for child in value.values():
                inspect(child)
        elif isinstance(value,list):
            for child in value:
                inspect(child)
    for path in JSON_SOURCES:
        text = (ROOT/path).read_text()
        data = json.loads(text)
        inspect(data)
        sha = digest(text)
        index[path] = dict(sha256=sha,snapshot=sha,historical=True,not_active_instructions=True)
        if sha in snapshots:
            continue
        groups = {name:{} for name in categories}
        groups['identity_counts_and_other_metadata'] = {}
        for key,value in data.items():
            matches = [name for name,keys in categories.items() if key in keys]
            assert len(matches) <= 1
            groups[matches[0] if matches else 'identity_counts_and_other_metadata'][key] = value
        reconstructed = {key:value for group in groups.values() for key,value in group.items()}
        assert reconstructed == data and sum(map(len,groups.values())) == len(data), 'Lost legacy JSON keys/values'
        snapshots[sha] = dict(groups=groups,source_key_count=len(data),historical=True,not_current_inventory_or_cursor=True)
    original = json.loads((ROOT/JSON_SOURCES[0]).read_text())
    return dict(source_index=index,unique_snapshots=snapshots,source_count=len(index),unique_snapshot_count=len(snapshots),record_template=original['record_template'],record_template_is_not_an_actual_model=True,template_scope='Historical reusable template;current required_fields and active scope take precedence',current_inventory='inventory_by_brand',current_cursor='cursor')

def build_metadata(state):
    sources = {path:parse_source(path) for path in SOURCES}
    current = next(b for b in sources[SOURCES[0]]['blocks'] if b['kind']=='table' and b['context']=='Identified entries')
    assert len(current['rows']) == len(OWNED) == 21
    entries = []
    for number,(row,model) in enumerate(zip(current['rows'],OWNED),1):
        assert int(row['#']) == number
        link = state['comparison_model_sources'][model]['link'] if model else None
        entries.append(dict(id=number,source_model=row['Model'],canonical_model=model,root_profile=link,last_supported_context=row['Last supported ownership context'],historical_technical_coverage=row['Technical coverage'],technical_coverage='root profile present;partial' if link else 'revision identity unresolved;no extra active model',current_possession='not independently reverified',source=SOURCES[0],source_date='2026-10-15'))
    assert sum(e['root_profile'] is not None for e in entries) == 20
    history = next(b for b in sources[SOURCES[1]]['blocks'] if b['kind']=='table' and b['context']=='Identified ownership history')
    assert len(history['rows']) == 20
    exclusion = next(b for b in sources['effects/SCOPE.md']['blocks'] if b['kind']=='table')
    assert len(exclusion['rows']) == 6
    discovery_paths = SOURCES[4:7]
    discovery_rows = []
    duplicates, seen = {}, {}
    for path in discovery_paths:
        parsed = sources[path]
        if parsed['sha256'] in seen:
            duplicates[path] = seen[parsed['sha256']]
            continue
        seen[parsed['sha256']] = path
        for block_index,block in enumerate(parsed['blocks']):
            if block['kind'] != 'table':
                continue
            for row_index,row in enumerate(block['rows']):
                first = next(iter(row.values()))
                context = block['context']
                kind = 'historical_listing_or_summary'
                if context.startswith('D. Search hits'):
                    kind = 'rejected_price_evidence_accessory_preset_or_unresolved_variant'
                elif 'Flamma FV01' in first:
                    kind = 'excluded_specialist_history'
                elif context.startswith('C. Hardware') or context.startswith('Pending technical'):
                    kind = 'superseded_research_queue_not_current_status'
                urls = sorted(set(re.findall(r'https?://[^\s)]+',' '.join(row.values()))))
                discovery_rows.append(dict(source=path,block_index=block_index,row_index=row_index,context=context,classification=kind,external_urls=urls,historical=True,live_stock_verified=False))
    marketplace = dict(sources=list(discovery_paths),duplicate_snapshots=duplicates,indexed_rows=discovery_rows,row_count=len(discovery_rows),new_active_models=0,scope='Dated discovery/offer/summary evidence;full row cells in sources blocks,not current offers or an active queue',current_research_cursor='cursor',excluded_specialist_rows_stay_excluded=True)
    checkpoint_paths = SOURCES[7:]
    checkpoint_duplicates, checkpoint_seen, checkpoint_tables = {}, {}, []
    template_fields = []
    for path in checkpoint_paths:
        parsed = sources[path]
        if parsed['sha256'] in checkpoint_seen:
            checkpoint_duplicates[path] = checkpoint_seen[parsed['sha256']]
        else:
            checkpoint_seen[parsed['sha256']] = path
        for block_index,block in enumerate(parsed['blocks']):
            if block['kind'] == 'table':
                checkpoint_tables.append(dict(source=path,block_index=block_index,context=block['context'],rows=len(block['rows']),historical=True,not_current_counts_or_queue=True))
            if path == 'effects/COVERAGE.history-2026-10-14.md' and block['kind']=='paragraph' and block['text'].startswith(chr(96)*3+'text'):
                template_fields = [line for line in block['text'].splitlines()[1:-1] if line.strip()]
    assert len(template_fields) >= 20, 'Historical field checklist missing'
    checkpoints = dict(sources=list(checkpoint_paths),duplicate_snapshots=checkpoint_duplicates,table_index=checkpoint_tables,historical_record_checklist=template_fields,current_inventory='inventory_by_brand',current_cursor='cursor',scope_warning='Historical specialist/drive/utility targets and stale counts are preserved as provenance,not active research scope',transfer_warning='Original transfer and old-repository cleanup statements retain their dated snapshots;this consolidation does not reverify remote trees')
    return dict(schema_version=1,checked_date='2026-10-17',legacy_json=parse_json_provenance(),sources=sources,marketplace=marketplace,checkpoints=checkpoints,ownership=dict(entry_count=21,root_profiles=20,additional_active_models=0,entries=entries,former_and_donated_included=True,unresolved=['Owned2025 BlackBox revision','Exact Zoom vocal model and V6/V6-SP bundle','Separate AVE-100 ownership not established','RH-4 ownership candidate only'],not_confirmed_owned={'NUX MG-400':'Owner rejected earlier fake-seller purchase evidence','Valeton GP-50':'Backup plan,not verified purchase'},audota_correction='AME-100 ownership established;does not establish AVE-100 ownership'),current_policy=dict(active_scope='Guitar multi-effects,documented bass-capable and genuine vocal paths;dedicated effects separate',excluded_models=state['excluded_models'],unknown_is_not_no=True,source_priority='Manufacturer model-specific product/manual/firmware evidence;offers establish prices,not technical specifications',price_currency='IDR;separate condition/date/stock/bundle/voucher contexts;no invented exchange rates',ownership_is_not_specification_evidence=True,source_dates_not_refreshed_by_consolidation=True),remaining_work='Sources retained. Incoming navigation and source retirement are not completed by this semantic consolidation.')

def plan():
    research_tools.identity()
    ledger_text = (ROOT/'research-state.json').read_text()
    state = json.loads(ledger_text)
    metadata = build_metadata(state)
    state['public_metadata'] = metadata
    state['migration']['public_metadata_consolidation'] = dict(date='2026-10-17',sources={p:metadata['sources'][p]['sha256'] for p in SOURCES},destination='research-state.json#public_metadata',ownership_entries=21,root_profile_links=20,source_retired=False,verification='Structured tables,headings and complete paragraph groups;every nonblank source line accounted for;current overlay resolves existing root models without adding records')
    state['cursor'] = dict(model='Public ownership and policy metadata',task='Ownership/current and original history plus scope/methodology semantics consolidated in root public_metadata;21entries/20rootprofiles,unresolved identities and exclusions retained. Discovery index/history now preserved with rejected-price hits and duplicate snapshots identified. Coverage,README,RESUME and MIGRATION semantics now preserved with duplicate checkpoints and original transfer evidence. All three legacy JSON files now preserve complete typed provenance and original template in grouped snapshots. Next map incoming navigation and anchors,validate destinations,and plan source retirement with Git-backed rollback. Technical gaps and fresh discovery remain.',next_models=[],after_queue='No private receipts/mail/order/payment contents included;historical source cursors are not active instructions.')
    readme = (ROOT/'README.md').read_text()
    note = '\nThe root [research ledger](research-state.json) also contains the structured ownership overlay,dated policy/history,marketplace discovery,coverage/checkpoints and legacy JSON templates/provenance under public_metadata:21 identified entries,20 root-profile links,explicit identity corrections,rejected-price hits and superseded queues. Historical states and duplicate snapshots do not add catalogue models or establish live stock.\n'
    readme = re.sub(r'\nThe root \[research ledger\]\(research-state.json\) also contains[^\n]+\n', '\n', readme)
    anchor = '\n## Evidence and resuming\n'
    assert anchor in readme
    outputs = {'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n','README.md':readme.replace(anchor,note+anchor)}
    inputs = {p:digest((ROOT/p).read_text()) for p in (*SOURCES,*JSON_SOURCES,*PATHS)}
    payload = dict(inputs=inputs,rollback_commit=research_tools.git('rev-parse','HEAD').strip(),outputs=outputs,summary=dict(sources=len(SOURCES),json_sources=len(JSON_SOURCES),unique_json_snapshots=metadata['legacy_json']['unique_snapshot_count'],source_blocks=sum(len(v['blocks']) for v in metadata['sources'].values()),source_nonblank_lines=sum(v['nonblank_lines'] for v in metadata['sources'].values()),ownership_entries=21,root_profile_links=20,new_models=0,deleted_files=[]))
    PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(payload['summary'],indent=2))
    print('Reviewed plan path: '+str(PLAN)+'; rollback commit: '+payload['rollback_commit'])

def apply():
    research_tools.identity()
    payload = json.loads(PLAN.read_text())
    for path,expected in payload['inputs'].items():
        assert digest((ROOT/path).read_text()) == expected, 'Changed input: '+path
    assert set(payload['outputs']) == {'README.md','research-state.json'}
    for path,text in payload['outputs'].items():
        (ROOT/path).write_text(text)
    verify()

def verify():
    research_tools.identity()
    state = json.loads((ROOT/'research-state.json').read_text())
    assert state['public_metadata'] == build_metadata(state), 'Metadata drift or lost source semantics'
    assert state['active_model_count'] == len({(b,m) for b,models in state['inventory_by_brand'].items() for m in models})
    for entry in state['public_metadata']['ownership']['entries']:
        if entry['root_profile']:
            path,anchor = entry['root_profile'].split('#',1)
            assert (ROOT/path).is_file() and anchor
    print('PASS:'+str(len(SOURCES))+' Markdown/'+str(len(JSON_SOURCES))+' JSON metadata sources;21ownership entries/20root profiles;all nonblank lines covered;no added models;historical corrections and exclusions retained.')

def commit():
    verify()
    research_tools.verify()
    subprocess.run([sys.executable,str(ROOT/'scripts/comparison_views.py'),'verify'],check=True)
    assert not research_tools.git('diff','--cached','--name-only').strip(), 'Existing staged changes'
    changed = set(research_tools.git('diff','--name-only').splitlines()) | set(research_tools.git('ls-files','--others','--exclude-standard').splitlines())
    assert changed <= set(PATHS), changed-set(PATHS)
    research_tools.git('add','--',*PATHS)
    print(research_tools.git('diff','--cached','--stat'))
    print(research_tools.git('commit','-m','docs: consolidate typed legacy JSON provenance and reusable record template'))

if __name__ == '__main__':
    {'plan':plan,'apply':apply,'verify':verify,'commit':commit}[sys.argv[1]]()
