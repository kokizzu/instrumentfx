"""Preserve public ownership/policy source semantics in the root ledger."""
import hashlib
import difflib
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

def parse_source(path, text=None):
    if text is None:
        text = research_tools.read_preserved_source(path)
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


JSON_GROUPS = {
    'requirements_and_template': {'latest_user_requirements','required_field_groups','record_template','record_template_is_not_an_actual_model','record_template_source','validation_rules','size_bins_mm'},
    'model_inventory_and_commits': {'pages','completed_review_batches','latest_findings','recovered_findings','integration_commits','previous_findings_preserved','inventory_validation','baseline_research_commit','latest_integrated_research_commit','latest_marketplace_index_commit'},
    'conflicts_and_coverage': {'known_conflicts_to_preserve','latest_unresolved','previous_unresolved_retained','retained_conflict_topics','migration_status','marketplace_status'},
    'historical_navigation': {'read_first','methodology','backlog','marketplace_index','cursor','owned_cursor','deferred_cursor'},
    'repository_transfer': {'legacy_misplaced_research','history'},
    'change_history': {'change_log','change_log_latest'},
}

def parse_json_provenance():
    snapshots, index = {}, {}
    categories = JSON_GROUPS
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
        text = research_tools.read_preserved_source(path)
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
    original = json.loads(research_tools.read_preserved_source(JSON_SOURCES[0]))
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
    expected = build_metadata(state)
    preserved = state['public_metadata']['remote_87c7d38_preserved']
    if preserved is not None:
        assert set(preserved) == {'qualification', 'ledger', 'readme', 'expression_category_before_normalization'}
        assert preserved['qualification'] == 'Incoming2026-10-18 branch snapshot; inventory/counts superseded by current root ledger. Preserved losslessly during non-force merge; capability leads still partial.'
        assert preserved['ledger'] == json.loads(research_tools.git('show', '87c7d38:research-state.json')), 'Preserved remote ledger changed'
        assert preserved['readme'] == research_tools.git('show', '87c7d38:README.md').rstrip('\n'), 'Preserved remote README changed'
        # This comparison is the later local pre-normalization snapshot, not the remote file.
        assert digest(preserved['expression_category_before_normalization']) == '6057c38043114721867c7cae40eed6e5d69256cecb6ca04f943e0970c0a71e84', 'Preserved pre-normalization comparison changed'
        expected['remote_87c7d38_preserved'] = preserved
    if state['public_metadata'] != expected:
        before = json.dumps(state['public_metadata'], ensure_ascii=False, indent=2, sort_keys=True).splitlines()
        after = json.dumps(expected, ensure_ascii=False, indent=2, sort_keys=True).splitlines()
        print('\n'.join(difflib.unified_diff(before, after, fromfile='saved public_metadata', tofile='derived public_metadata')))
        raise AssertionError('Metadata drift or lost source semantics')
    assert state['active_model_count'] == len({(b,m) for b,models in state['inventory_by_brand'].items() for m in models})
    for entry in state['public_metadata']['ownership']['entries']:
        if entry['root_profile']:
            path,anchor = entry['root_profile'].split('#',1)
            assert (ROOT/path).is_file() and anchor
    verified_history_entries(state)
    print('PASS:'+str(len(SOURCES))+' Markdown/'+str(len(JSON_SOURCES))+' JSON metadata sources;21ownership entries/20root profiles;all nonblank lines covered;no added models;historical corrections and exclusions retained.')

def strict_json(text):
    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            assert key not in result, 'Duplicate JSON key: '+key
            result[key] = value
        return result
    def reject_constant(value):
        raise ValueError('Non-finite JSON number: '+value)
    return json.loads(text, object_pairs_hook=unique_object, parse_constant=reject_constant)


def reconstruct_historical_json(content):
    groups = content['groups']
    assert set(groups) == set(JSON_GROUPS) | {'identity_counts_and_other_metadata'}
    result = {}
    for group in groups.values():
        assert isinstance(group, dict)
        for key, value in group.items():
            assert key not in result, 'Duplicate grouped JSON key: '+key
            result[key] = value
    assert len(result) == content['source_key_count'], 'Lost historical JSON keys'
    return result


def parse_historical_json(path, body):
    assert path in JSON_SOURCES
    data = strict_json(body)
    assert isinstance(data, dict), 'Historical ledger must be a JSON object'
    def inspect(value):
        if isinstance(value, str):
            assert not re.search(r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}',value,re.I), 'Private email identifier in legacy source'
            assert not re.search(r'mail\.google\.com|outlook\.(live|office)\.com',value,re.I), 'Private mailbox link in legacy source'
        elif isinstance(value, dict):
            for key, child in value.items():
                inspect(key)
                inspect(child)
        elif isinstance(value, list):
            for child in value:
                inspect(child)
    inspect(data)
    groups = {name:{} for name in JSON_GROUPS}
    groups['identity_counts_and_other_metadata'] = {}
    for key, value in data.items():
        matches = [name for name, keys in JSON_GROUPS.items() if key in keys]
        assert len(matches) <= 1
        groups[matches[0] if matches else 'identity_counts_and_other_metadata'][key] = value
    content = dict(source=path, sha256=digest(body), groups=groups, source_key_count=len(data),
                   historical=True, not_current_inventory_or_cursor=True)
    reconstructed = reconstruct_historical_json(content)
    assert json.dumps(reconstructed,sort_keys=True,allow_nan=False) == json.dumps(data,sort_keys=True,allow_nan=False)
    return content


def verify_history_entry(entry, body):
    assert entry['historical'] is True and entry['not_active_instructions'] is True
    assert digest(body) == entry['sha256'], 'Historical metadata blob changed'
    if entry['kind'] == 'historical-metadata-markdown-v1':
        assert entry['source'] in SOURCES
        assert parse_source(entry['source'], body) == entry['content'], 'Historical metadata content lost or altered'
    else:
        assert entry['kind'] == 'historical-metadata-json-v1' and entry['source'] in JSON_SOURCES
        expected = parse_historical_json(entry['source'], body)
        # Python considers False == 0; serialized equality must retain JSON types.
        assert json.dumps(expected,sort_keys=True,allow_nan=False) == json.dumps(entry['content'],sort_keys=True,allow_nan=False), 'Historical JSON value/type lost or altered'
        reconstructed = reconstruct_historical_json(entry['content'])
        assert json.dumps(reconstructed,sort_keys=True,allow_nan=False) == json.dumps(strict_json(body),sort_keys=True,allow_nan=False)


def verified_history_entries(state):
    entries = state['migration'].get('metadata_source_history_audit_20261104', {}).get('reviewed_variants', [])
    verified = {}
    for entry in entries:
        body = research_tools.git('cat-file', '-p', entry['blob'])
        verify_history_entry(entry, body)
        key = (entry['source'], entry['blob'])
        assert key not in verified, 'Duplicate historical metadata review'
        verified[key] = entry
    return verified


def history_preservation_rows(pending, all_current_source=False):
    eligible = [row for row in pending if row['source'] in SOURCES]
    assert eligible, 'No pending Markdown metadata revisions'
    first = eligible[0]
    return ([row for row in eligible if row['source'] == first['source']]
            if all_current_source else [first])


def plan_history_preservation(all_current_source=False):
    research_tools.identity()
    state = json.loads((ROOT/'research-state.json').read_text())
    pending = state['migration']['metadata_source_history_audit_20261104']['pending']
    entries = []
    for row in history_preservation_rows(pending, all_current_source):
        body = research_tools.git('cat-file', '-p', row['blob'])
        assert digest(body) == row['sha256']
        entry = dict(kind='historical-metadata-markdown-v1', **row, historical=True, not_active_instructions=True,
                     content=parse_source(row['source'], body),
                     qualification='Historical source wording, counts, coverage and queues; current root inventory, ownership corrections and cursors take precedence. No new purchase verification or active model admission.')
        verify_history_entry(entry, body)
        entries.append(entry)
    payload = dict(head=research_tools.git('rev-parse','HEAD').strip(), ledger_sha256=digest((ROOT/'research-state.json').read_text()))
    if all_current_source:
        payload['entries'] = entries
    else:
        payload['entry'] = entries[0]
    target = Path('/tmp/instrumentfx-metadata-history-preservation-plan.json')
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
    for entry in entries:
        print(json.dumps(dict(source=entry['source'], blob=entry['blob'], blocks=len(entry['content']['blocks']), nonblank_lines=entry['content']['nonblank_lines']), indent=2))
    print('Review every complete source and ' + str(target) + '; no repository sources modified.')


def history_blobs(raw, path):
    """Include both sides of changes, including deletions and merge parents."""
    blobs = set()
    for line in raw.splitlines():
        match = re.fullmatch(r':[0-7]{6} [0-7]{6} ([0-9a-f]{40}) ([0-9a-f]{40}) [A-Z]\t(.+)', line)
        if match and match[3] == path:
            blobs.update(blob for blob in match.group(1, 2) if blob != '0' * 40)
    return blobs


def history_status(body, preserved, redirects, aliases=()):
    if body == preserved:
        return 'verified-registered-original'
    if body in aliases:
        return 'verified-registered-source-alias'
    if body in redirects:
        return 'verified-compatibility-redirect'
    return 'historical-variant-needs-review'


def test_history():
    pending = [dict(source=SOURCES[0], blob='a'), dict(source=SOURCES[1], blob='b'), dict(source=SOURCES[0], blob='c'), dict(source=JSON_SOURCES[0], blob='d')]
    assert [r['blob'] for r in history_preservation_rows(pending)] == ['a']
    assert [r['blob'] for r in history_preservation_rows(pending, True)] == ['a', 'c'], 'Mixed source groups or JSON into Markdown plan'
    try:
        history_preservation_rows([pending[-1]], True)
    except AssertionError:
        pass
    else:
        raise AssertionError('JSON-only queue accepted as Markdown')
    a, b, zero = 'a' * 40, 'b' * 40, '0' * 40
    path = 'effects/SCOPE.md'
    raw = (f':100644 100644 {a} {b} M\t{path}\n'
           f':100644 000000 {b} {zero} D\t{path}\n'
           f':000000 100644 {zero} {zero} A\t{path}\n'
           f':100644 100644 {a} {zero} D\teffects/OTHER.md\n')
    assert history_blobs(raw, path) == {a, b}, 'Lost deletion/parent blob or included unrelated path'
    assert history_blobs('', path) == set()
    assert history_status('fact', 'fact', {'redirect'}) == 'verified-registered-original'
    assert history_status('redirect', 'fact', {'redirect'}) == 'verified-compatibility-redirect'
    assert history_status('old fact', 'fact', {'redirect'}, {'old fact'}) == 'verified-registered-source-alias'
    assert history_status('old fact changed', 'fact', {'redirect'}, {'old fact'}) == 'historical-variant-needs-review'
    for altered in ('', 'fact changed', 'redirect plus lost fact'):
        assert history_status(altered, 'fact', {'redirect'}) == 'historical-variant-needs-review'
    body = '# Example\n\n| Model | Limit |\n|---|---|\n| A | Unknown |\n| B | Revision conflict |\n\nHistorical queue; not active.\n'
    entry = dict(kind='historical-metadata-markdown-v1', source=SOURCES[0], sha256=digest(body), historical=True, not_active_instructions=True, content=parse_source(SOURCES[0], body))
    verify_history_entry(entry, body)
    import copy
    broken = copy.deepcopy(entry)
    table = next(block for block in broken['content']['blocks'] if block['kind'] == 'table')
    table['rows'].pop()
    try:
        verify_history_entry(broken, body)
    except AssertionError:
        pass
    else:
        raise AssertionError('Lost historical table row accepted')
    try:
        verify_history_entry(entry, body.replace('Unknown', 'No'))
    except AssertionError:
        pass
    else:
        raise AssertionError('Altered unknown qualification accepted')
    sample = {'repository':'kokizzu/instrumentfx', 'cursor':{'model':'Historical only'}, 'record_count':51,
              'required_field_groups':['expression','display'],
              'record_template':{'unknown':None,'no':False,'zero':0,'text':'0','empty_array':[],'empty_object':{}}}
    raw_json = json.dumps(sample)
    content = parse_historical_json(JSON_SOURCES[-1], raw_json)
    assert json.dumps(reconstruct_historical_json(content), sort_keys=True) == json.dumps(sample, sort_keys=True)
    json_entry = dict(kind='historical-metadata-json-v1', source=JSON_SOURCES[-1], sha256=digest(raw_json),
                      historical=True, not_active_instructions=True, content=content)
    verify_history_entry(json_entry, raw_json)
    for field, value in [('unknown',False),('no',0),('zero',False),('text',0),('empty_array',{}),('empty_object',[])]:
        broken = copy.deepcopy(json_entry)
        broken['content']['groups']['requirements_and_template']['record_template'][field] = value
        try:
            verify_history_entry(broken, raw_json)
        except AssertionError:
            pass
        else:
            raise AssertionError('JSON type changed without rejection: '+field)
    broken = copy.deepcopy(json_entry)
    broken['content']['groups']['requirements_and_template']['required_field_groups'].reverse()
    try:
        verify_history_entry(broken, raw_json)
    except AssertionError:
        pass
    else:
        raise AssertionError('Historical array order changed')
    broken = copy.deepcopy(content)
    broken['groups']['historical_navigation']['record_count'] = 51
    try:
        reconstruct_historical_json(broken)
    except AssertionError:
        pass
    else:
        raise AssertionError('Duplicate grouped JSON key accepted')
    for invalid in ('{"a":1,"a":2}', '{"number":NaN}', '{"number":Infinity}'):
        try:
            parse_historical_json(JSON_SOURCES[-1], invalid)
        except (AssertionError, ValueError):
            pass
        else:
            raise AssertionError('Ambiguous JSON accepted')
    print('PASS: metadata history includes deletion parents, isolates paths and rejects changed/lost historical facts; JSON types, empties and array order retained')


def plan_history_json():
    research_tools.identity()
    raw = (ROOT/'research-state.json').read_text()
    state = json.loads(raw)
    pending = state['migration']['metadata_source_history_audit_20261104']['pending']
    entries = []
    for row in pending:
        if row['source'] not in JSON_SOURCES:
            continue
        body = research_tools.git('cat-file','-p',row['blob'])
        assert digest(body) == row['sha256']
        entry = dict(kind='historical-metadata-json-v1', **row, historical=True, not_active_instructions=True,
                     content=parse_historical_json(row['source'],body),
                     qualification='Historical typed JSON values grouped by purpose; not current inventory, ownership, scope or instructions. Current root records and independent queues take precedence.')
        verify_history_entry(entry,body)
        entries.append(entry)
    assert entries, 'No pending historical JSON snapshots'
    target = Path('/tmp/instrumentfx-metadata-json-history-plan.json')
    payload = dict(head=research_tools.git('rev-parse','HEAD').strip(),ledger_sha256=digest(raw),entries=entries)
    target.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps([dict(source=e['source'],blob=e['blob'],keys=e['content']['source_key_count']) for e in entries],indent=2))
    print('Read complete selected sources and review '+str(target)+' before preserving any entry; no tracked files changed.')


def audit_history():
    """Read-only HEAD-reachable metadata revision census; never auto-certify variants."""
    from brand_filename_migration import original_namespace
    import source_retirement
    import json_pointer_removal
    research_tools.identity()
    test_history()
    source_retirement.verify()
    json_pointer_removal.verify()
    state = json.loads((ROOT/'research-state.json').read_text())
    reviewed = verified_history_entries(state)
    pointers = state['migration']['json_pointer_removal']['records']
    assert research_tools.git('rev-parse', '--is-shallow-repository').strip() == 'false', 'Complete history required'
    head = research_tools.git('rev-parse', 'HEAD').strip()
    rows, cache = [], {}
    originals = {path:research_tools.read_preserved_source(path) for path in (*SOURCES, *JSON_SOURCES)}
    aliases = {body:path for path,body in originals.items()}
    for path in (*SOURCES, *JSON_SOURCES):
        raw = research_tools.git('log', '--full-history', '-m', '--format=', '--raw', '--no-abbrev', '--no-renames', head, '--', path)
        blobs = history_blobs(raw, path)
        assert blobs, 'Missing source history: ' + path
        preserved = originals[path]
        redirects = set()
        if path in SOURCES:
            current = (ROOT / path).read_text()
            assert current.startswith('# '), 'Unexpected compatibility file: ' + path
            redirects.update((current, original_namespace(current, path)))
        for blob in sorted(blobs):
            if blob not in cache:
                cache[blob] = research_tools.git('cat-file', '-p', blob)
            body = cache[blob]
            status = history_status(body, preserved, redirects, aliases)
            if status == 'historical-variant-needs-review' and path in pointers and body == pointers[path]['pointer_text']:
                status = 'verified-retired-json-pointer'
            if status == 'historical-variant-needs-review' and (path, blob) in reviewed:
                status = 'verified-historical-metadata-content'
            row = dict(source=path, blob=blob, sha256=digest(body), status=status)
            if status == 'verified-registered-source-alias':
                row['covered_source'] = aliases[body]
            if status == 'historical-variant-needs-review':
                row['historical_body'] = body
                row['diff_from_registered'] = ''.join(difflib.unified_diff(preserved.splitlines(True), body.splitlines(True), fromfile='registered:' + path, tofile='historical:' + blob))
            rows.append(row)
    counts = {}
    for row in rows:
        counts[row['status']] = counts.get(row['status'], 0) + 1
    report = dict(head=head, sources=len(SOURCES) + len(JSON_SOURCES), variants=len(rows), counts=counts, records=rows,
                  limitation='Exact registered-original/alias equality relies on metadata-verify; current Markdown redirects are independently checked by source-retirement verify before byte comparisons. Retired JSON pointers require exact bytes plus independent typed-content/removal verification; historical Markdown requires complete parsed-source equality and historical JSON requires exact typed-value reconstruction against its pinned Git blob. All other HEAD-reachable variants require review. Pending is not proven loss; no source deletion or full migration certification.')
    target = Path('/tmp/instrumentfx-metadata-history-audit.json')
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k:v for k,v in report.items() if k != 'records'}, indent=2))
    print('Review ' + str(target) + '; no repository sources modified.')


def commit(stage=False):
    verify()
    research_tools.verify()
    subprocess.run([sys.executable,str(ROOT/'scripts/comparison_views.py'),'verify'],check=True)
    test_history()
    changed = set(research_tools.git('diff','--name-only').splitlines()) | set(research_tools.git('ls-files','--others','--exclude-standard').splitlines())
    staged = set(research_tools.git('diff','--cached','--name-only').splitlines())
    assert (changed | staged) <= set(PATHS), (changed | staged)-set(PATHS)
    assert not research_tools.git('diff','--check').strip()
    receipt = Path('/tmp/instrumentfx-metadata-staged-review.json')
    if stage:
        assert changed and not staged, 'Unexpected staged changes or nothing to stage'
        research_tools.git('add','--',*sorted(changed))
        diff = research_tools.git('diff','--cached')
        Path('/tmp/instrumentfx-metadata-staged.diff').write_text(diff)
        receipt.write_text(json.dumps(dict(head=research_tools.git('rev-parse','HEAD').strip(), sha256=digest(diff))))
        print(research_tools.git('diff','--cached','--stat'))
        print('Review /tmp/instrumentfx-metadata-staged.diff before make metadata-commit')
    else:
        assert staged and not changed, 'Stage and review first'
        review = json.loads(receipt.read_text())
        assert review['head'] == research_tools.git('rev-parse','HEAD').strip()
        assert review['sha256'] == digest(research_tools.git('diff','--cached'))
        assert not research_tools.git('diff','--cached','--check').strip()
        print(research_tools.git('commit','-m','audit: preserve typed historical JSON research metadata'))

if __name__ == '__main__':
    {'plan':plan,'apply':apply,'verify':verify,'commit':commit,'stage':lambda:commit(stage=True),'audit-history':audit_history,'test-history':test_history,'plan-history':plan_history_preservation,'plan-history-source':lambda:plan_history_preservation(True),'plan-history-json':plan_history_json}[sys.argv[1]]()
