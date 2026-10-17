"""Build complete instrument comparison views from retained evidence, without research/network."""
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
PLAN = Path('/tmp/instrumentfx-comparison-plan.json')

def norm(text):
    text = re.sub(r'\[([^\]]+)\](?:\([^)]*\)|\[[^\]]*\])', r'\1', text)
    return re.sub(r'[^a-z0-9]', '', text.lower())

def slug(text):
    return re.sub(r'[^\w\- ]', '', text.lower()).replace(' ', '-')

def identity():
    assert 'git@github.com:kokizzu/instrumentfx.git' in (ROOT / '.git/config').read_text()

def sections(text):
    matches = list(re.finditer(r'^## (.+)$', text, re.M))
    return [(m[1], text[m.end():matches[i+1].start() if i+1<len(matches) else len(text)]) for i,m in enumerate(matches)]

def tables(text):
    lines = text.splitlines()
    context = ''
    i = 0
    while i < len(lines)-1:
        if lines[i].startswith('#'):
            context = lines[i].lstrip('# ').strip()
        if lines[i].startswith('|') and re.fullmatch(r'\|[\s:|\-]+\|', lines[i+1]):
            headers = [c.strip() for c in lines[i].strip('|').split('|')]
            i += 2
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                row = [c.strip() for c in lines[i].strip('|').split('|')]
                if len(row)==len(headers):
                    rows.append(row)
                i += 1
            yield headers, rows, context
        else:
            i += 1

def aliases(brand, model):
    names = {model, brand+' '+model}
    cleaned = re.sub(r' original$', '', model)
    names |= {cleaned, brand+' '+cleaned}
    for suffix in (' MP-50',' MP-100',' MP-350',' MP-380',' MP-300',' MP-80',' QME-50',' QME-20',' QME-10',' QME-100',' QME-200',' QCE-50',' NME-5',' NME-3',' FB-100'):
        if model.endswith(suffix):
            names |= {model[:-len(suffix)], suffix.strip()}
    extra = {
        'GEM BOX original':['GEM BOX','Original GEM BOX'],
        'POD Go':['POD Go standard','POD Go, standard non-Wireless'],
        'CUBE BABY electric':['CUBE BABY','Cube Baby Electric','Cube Baby electric'],
        'ANN Blackbox':['ANN Blackbox','ANN BLACK BOX'],
        'Ampero Mini MP-50':['Ampero Mini'],
        'Matribox QME-50':['Matribox','Sonicake Matribox, QME-50'],
        'Matribox II QME-100':['Matribox II','Sonicake Matribox II, QME-100'],
        'Matribox II Pro QME-200':['Matribox II Pro','Sonicake Matribox II Pro, QME-200'],
        'TRIDENT NME-5':['TRIDENT'],
    }
    names |= set(extra.get(model, []))
    return {norm(n) for n in names}

def relink(value, source, refs):
    value = re.sub(r'(?<!!)[\[]([^\]]+)\]\[([^\]]*)\]', lambda m: '['+m[1]+']('+refs[(m[2] or m[1]).lower()]+')' if (m[2] or m[1]).lower() in refs else m[0], value)
    value = re.sub(r'(?<!!)(?<!\\)\[([^\[\]]+)\](?![\[(])', lambda m: '['+m[1]+']('+refs[m[1].lower()]+')' if m[1].lower() in refs else m[0], value)
    def link(m):
        target = m[2]
        if '://' in target or target.startswith('mailto:'):
            return m[0]
        path, sep, anchor = target.partition('#')
        absolute = (ROOT / source).parent / unquote(path) if path else ROOT / source
        target = str(absolute.resolve().relative_to(ROOT)) + (sep+anchor if sep else '')
        return '['+m[1]+']('+target+')'
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, value)

def comparison_body(body):
    """Use an explicitly maintained comparison without repeating the retained archive."""
    start = '<!-- comparison evidence begins -->'
    end = '<!-- comparison evidence ends -->'
    if start not in body and end not in body:
        return body
    assert body.count(start) == body.count(end) == 1, 'Ambiguous comparison evidence markers'
    selected = body.split(start, 1)[1].split(end, 1)[0]
    assert body.index(start) < body.index(end) and selected.strip(), 'Invalid comparison evidence range'
    return selected

def source_map(state, files):
    result = {}
    root_aliases = {'Line 6':'LINE6.md', 'M-VAVE':'M-VAVE.md', 'IK Multimedia':'IK-MULTIMEDIA.md'}
    for brand, models in state['inventory_by_brand'].items():
        for model in models:
            key = brand+'::'+model
            alias = aliases(brand, model)
            canonical = None
            for filename, listed in state['root_brand_content'].items():
                if model in listed:
                    # Model names Core etc. are unique across this inventory.
                    for heading, body in sections(files[filename]):
                        if norm(heading) in alias or (model in ('POD Go','POD Go Wireless') and heading=='POD Go and POD Go Wireless'):
                            canonical = (filename, heading, comparison_body(body))
                            break
            result[key] = dict(brand=brand, model=model, aliases=alias, canonical=canonical)
    return result


def field_value(headers, row):
    """Retain a technical finding's separate evidence column, when present."""
    value = row[1]
    if len(headers) == 3 and row[2].strip():
        value += ' — ' + headers[2] + ': ' + row[2]
    return value


def manifest_findings(state, files, destination):
    """Keep explicit full-body provenance when filename aliases omit a model code."""
    return {entry['source'] for entry in state.get('consolidation_and_price_findings', [])
            if entry.get('verification_kind') == 'complete-source-body-v1'
            and entry.get('destination') == destination
            and '/findings/' in entry.get('source', '') and entry['source'] in files}


def verify_evidence_owners(records, guards):
    """Pin reviewed exact-item evidence to its model, including negative sibling checks."""
    for guard in guards:
        token, owner = guard['token'], guard['model']
        actual = {key for key, record in records.items()
                  if any(token in fact['value'] for fact in record['facts'])}
        assert actual == {owner}, ('Evidence model mismatch', token, owner, sorted(actual))

def test_evidence_owners():
    guards = [{'token': 'seller/item123', 'model': 'Brand::Model'}]
    valid = {'Brand::Model': {'facts': [{'value': 'seller/item123'}]},
             'Brand::Sibling': {'facts': []}}
    verify_evidence_owners(valid, guards)
    for invalid in (
        {'Brand::Model': {'facts': []}, 'Brand::Sibling': {'facts': [{'value': 'seller/item123'}]}},
        {key: {'facts': [{'value': 'seller/item123'}]} for key in valid},
        {key: {'facts': []} for key in valid},
    ):
        try:
            verify_evidence_owners(invalid, guards)
        except AssertionError:
            pass
        else:
            raise AssertionError('Wrong, duplicated or missing item ownership was accepted')
    print('PASS: exact evidence ownership rejects sibling placement, duplication and omission.')

def make_plan():
    identity()
    files = {str(p.relative_to(ROOT)):p.read_text() for p in ROOT.rglob('*.md') if '.git' not in p.parts and 'history' not in p.name}
    state = json.loads((ROOT/'research-state.json').read_text())
    records = source_map(state, files)
    references = {path:{m[1].lower():m[2] for m in re.finditer(r'^\[([^\]]+)\]:\s*(\S+)', text, re.M)} for path,text in files.items()}
    facts = defaultdict(list)
    root_models = set(records)
    finding_for = defaultdict(set)
    # Exact model names in model-column tables; no substring matching across variants.
    for path, text in files.items():
        if not path.startswith('effects/') or '/findings/' in path:
            continue
        if any(x in path for x in ('COVERAGE','RESUME','MIGRATION','README','OWNERSHIP','SCOPE','METHODOLOGY','shopee-indonesia')):
            continue
        for headers, rows, context in tables(text):
            if 'model' not in headers[0].lower():
                continue
            if any(x in ' '.join(headers).lower() for x in ('findings commit','original findings','initial findings','individually saved','original model commit')) and len(headers)<4:
                continue
            for row in rows:
                label = norm(row[0])
                matches = [k for k,r in records.items() if label in r['aliases']]
                # Certain legacy tables abbreviate these exact variants.
                if path.endswith('shopee-multifx-6.md'):
                    short={'plus':'GE150 Plus','plusli':'GE150 Plus Li','max':'GE150 Max','maxli':'GE150 Max Li'}
                    if label in short:
                        matches=['MOOER::'+short[label]]
                for key in matches:
                    for h,v in zip(headers[1:],row[1:]):
                        facts[key].append(dict(field=h,value=relink(v,path,references[path]),source=path,context=context))
                    # Complete model findings linked in the original model cell.
                    resolved = relink(row[0], path, references[path])
                    for link in re.findall(r'\]\(([^)#]+)',resolved):
                        if link in files and '/findings/' in link:
                            finding_for[key].add(link)
    # Some findings are not linked by name in a newer comparison. Resolve by filename alias,
    # with a unique longest match, never by sibling-model specification substitution.
    for path in files:
        if '/findings/' not in path:
            continue
        name = re.sub(r'^\d{4}-\d{2}-\d{2}-','',Path(path).stem)
        name = re.sub(r'-display-idr$','',name)
        n=norm(name)
        matches=[(len(a),k) for k,r in records.items() for a in r['aliases'] if len(a)>4 and n==a]
        if matches:
            longest=max(x[0] for x in matches)
            keys={k for length,k in matches if length==longest}
            if len(keys)==1:
                finding_for[next(iter(keys))].add(path)
    for key,r in records.items():
        if r['canonical']:
            filename, heading, body = r['canonical']
            sources=[(filename,body)]
            r['link']=filename+'#'+slug(heading)
            finding_for[key].update(manifest_findings(state, files, r['link']))
            # Canonical records supersede stale legacy summaries (e.g. POD Express dimensions).
            facts[key]=[]
        else:
            sources=[(p,files[p]) for p in sorted(finding_for[key])]
            r['link']=next(iter(sorted(finding_for[key])),facts[key][0]['source'] if facts[key] else '')
            if key=='BOSS::GM-800':
                sources=[('effects/specialist.md',dict(sections(files['effects/specialist.md']))['Eligible record: BOSS GM-800'])]
                r['link']='effects/specialist.md#eligible-record-boss-gm-800'
        for path,text in sources:
            refs=references[path]
            for headers, rows, context in tables(text):
                field_table = len(headers) in (2,3) and any(x in headers[0].lower() for x in ('field','required'))
                price_table = any(x in ' '.join(headers).lower() for x in ('amount','idr','price','condition','seller')) and not field_table
                family_table = path=='LINE6.md' and headers[1].startswith('POD Go,')
                if not field_table and not price_table and not family_table and ('category' in headers[0].lower() or re.search(r'fx/|^fx$|^fx/wah',headers[0],re.I)):
                    values=['; '.join(h+': '+v for h,v in zip(headers,row)) for row in rows]
                    facts[key].append(dict(field='Category choices, dated source table',value=relink(' / '.join(values),path,refs),source=path,context=context))
                for row in rows:
                    if family_table:
                        col=2 if r['model']=='POD Go Wireless' else 1
                        value=row[col]
                        if col==2 and value.startswith('Same'):
                            value=row[1]+'; Wireless: '+value
                        facts[key].append(dict(field=row[0],value=relink(value,path,refs),source=path,context=context))
                    elif field_table:
                        facts[key].append(dict(field=row[0],value=relink(field_value(headers,row),path,refs),source=path,context=context))
                    elif price_table:
                        if r['model'] in ('POD Go','POD Go Wireless'):
                            if ('Wireless' in row[0]) != (r['model']=='POD Go Wireless'):
                                continue
                        facts[key].append(dict(field='IDR '+row[0],value=relink(' — '.join(row[1:]),path,refs),source=path,context=context))
            # Preserve model-specific prose evidence, excluding source lists and stale next cursors.
            prose_heading=''
            for paragraph in re.split(r'\n\s*\n',text):
                paragraph=paragraph.strip()
                if paragraph.startswith('#'):
                    prose_heading=paragraph.lstrip('# ').strip()
                if path=='LINE6.md' and r['model']=='POD Go' and prose_heading=='Wireless-specific operation':
                    continue
                if re.search(r'provenance',prose_heading,re.I):
                    continue
                if not paragraph or paragraph.startswith(('|','#','[','Sources:','Source:','Original source')):
                    continue
                if 'Next:' in paragraph or 'Next model' in paragraph or 'next model' in paragraph:
                    continue
                if re.search(r'Rp[\d\s.]',paragraph):
                    facts[key].append(dict(field='IDR qualified observations',value=relink(paragraph.replace('\n',' '),path,refs),source=path,context='model-specific price prose'))
                elif not r['canonical'] and re.search(r'display|screen|rotary|footswitch|current|looper',paragraph,re.I):
                    facts[key].append(dict(field='Follow-up '+('display' if re.search('display|screen',paragraph,re.I) else 'technical correction'),value=relink(paragraph.replace('\n',' '),path,refs),source=path,context='model-specific follow-up prose'))
                elif r['canonical'] and paragraph.startswith('Ports:'):
                    facts[key].append(dict(field='Ports',value=relink(paragraph,path,refs),source=path,context='canonical model-specific prose'))
                elif r['canonical'] and re.search(r'ports|connections|i/o|power|software|routing|category|firmware|recording|stage|operation',prose_heading,re.I) and not re.search(r'source|provenance|verification|idr|price|remaining',prose_heading,re.I):
                    label=prose_heading
                    plain=paragraph.replace('**','')
                    if plain.startswith('Power:'):
                        label='Power'
                    elif plain.startswith('Pro Control full editor:'):
                        label='Editor platforms'
                    elif plain.startswith('USB') or plain.startswith('Normal USB mode:'):
                        label='USB audio / recording / routing'
                    elif plain.startswith('Rear diagram:') or plain.startswith('One') or plain.startswith('Four send/return'):
                        label='Audio/control ports'
                    elif plain.startswith('AMP OUT'):
                        label='I/O routing'
                    elif plain.startswith('Looper'):
                        label='Looper / live'
                    facts[key].append(dict(field=label,value=relink(paragraph.replace('\n',' '),path,refs),source=path,context='canonical model-specific prose'))
        r['facts']=facts[key]
        r['sources']=sorted({f['source'] for f in facts[key]})
        r['findings']=sorted(finding_for[key])
    serial = {k:{a:b for a,b in r.items() if a not in ('canonical','aliases')} for k,r in records.items()}
    verify_evidence_owners(serial, state.get('evidence_identity_guards', []))
    missing=[k for k,r in serial.items() if not r['facts'] or not r['link']]
    payload={'input_hashes':{p:hashlib.sha256(text.encode()).hexdigest() for p,text in files.items()},'ledger_hash':hashlib.sha256((ROOT/'research-state.json').read_bytes()).hexdigest(),'records':serial,'missing':missing}
    payload.update(render(serial,state))
    archives=archive_outputs(files)
    payload['outputs'].update(archives)
    payload['outputs']['README.md'] = readme_counts(files['README.md'], state, payload['view_membership'])
    PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print(f'Preview saved: {PLAN}; {len(serial)} records; missing evidence: {missing}')
    print('Per-model evidence fields:')
    for k,r in serial.items():
        print(k+' | '+r['link']+' | '+str(len(r['facts']))+' fields')

def archive_outputs(files):
    if all(p in files for p in ('SINGLE-GUITAR.md','SINGLE-BASS.md','SINGLE-VOCAL.md')):
        return {}
    path='effects/specialist.md'
    original=files[path]
    marker='## Excluded archive — not part of the multi-effects comparison'
    before,archive=original.split(marker,1)
    archive=marker+archive
    migrated=archive.replace('[SCOPE.md](SCOPE.md)','[SCOPE.md](effects/SCOPE.md)')
    guitar='# Single-purpose guitar effects — separate archive\n\n[All guitar multi-effects](ALL-GUITAR.md) · [Single bass](SINGLE-BASS.md) · [Single vocal](SINGLE-VOCAL.md) · [Repository](README.md)\n\nDedicated synthesis, acoustic simulation, vocoding and pitch pedals are kept here, **outside ALL-GUITAR and active multi-effects counts**. This is preserved partial research checked 2026-10-14, reorganized 2026-10-16, not a new price/specification verification. A mode or preset count is not a simultaneous multi-effects architecture.\n\n'+migrated
    # Every original archive fact, qualifier, URL and date survives the relocation.
    assert migrated.replace('[SCOPE.md](effects/SCOPE.md)','[SCOPE.md](SCOPE.md)')==archive
    redirect='## Excluded archive — not part of the multi-effects comparison\n\nThe complete five-model dedicated-effect archive was moved losslessly to [SINGLE-GUITAR.md](../SINGLE-GUITAR.md). It remains excluded from active counts. GM-800 above remains eligible because of its independent MFX architecture.\n\n'
    for heading in re.findall(r'^### (.+)$',archive,re.M):
        redirect+='### '+heading+'\n\n[Complete preserved archive](../SINGLE-GUITAR.md#'+slug(heading)+').\n\n'
    specialist=before+redirect
    fvpath='effects/findings/2026-10-14-flamma-fv01.md'
    fv=files[fvpath]
    fvbody=fv.split('\n',1)[1]
    migrated_fv=re.sub(r'^## ', '### ',fvbody,flags=re.M).replace('(../SCOPE.md)','(effects/SCOPE.md)')
    vocal='# Single-purpose and explicitly excluded vocal effects\n\n[All vocal multi-effects](ALL-VOCAL.md) · [Single guitar](SINGLE-GUITAR.md) · [Repository](README.md)\n\nThis archive is separate from the active multi-effects comparisons. FV01 is retained because the user explicitly excluded it, not because every supporting effect must be denied. BOSS VO-1 is a dedicated vocoder with microphone input; its complete preserved record is in [SINGLE-GUITAR](SINGLE-GUITAR.md#archived-processing-and-memory), not the vocal multi-effects table. No new technical or market verification is claimed.\n\n## Flamma FV01 Corrector\n'+migrated_fv
    assert migrated_fv.replace('(effects/SCOPE.md)','(../SCOPE.md)').replace('\n### ','\n## ')==fvbody
    fvredirect=fv.split('\n',1)[0]+'\n\nThe complete archived record is now [SINGLE-VOCAL.md](../../SINGLE-VOCAL.md#flamma-fv01-corrector). It remains explicitly excluded; no facts or sources were discarded.\n\n'
    for heading in re.findall(r'^## (.+)$',fvbody,re.M):
        fvredirect+='## '+heading+'\n\n[Preserved section](../../SINGLE-VOCAL.md#'+slug(heading)+').\n\n'
    bass='# Single-purpose bass effects — separate archive\n\n[All bass multi-effects](ALL-BASS.md) · [Single guitar](SINGLE-GUITAR.md) · [Repository](README.md)\n\nDedicated pedals are not promoted to bass multi-effects merely because they have multiple sounds or memories. These are shared records, not new active catalogue entries. No new price or specification verification is claimed.\n\n| Dedicated model | Bass-related function | Complete preserved comparison |\n|---|---|---|\n| BOSS SY-1 | Standard-input guitar/bass synthesizer; one selected engine, 121 sounds | [Controls, memory, I/O, power, historical prices and sources](SINGLE-GUITAR.md#archived-hardware-and-expression) |\n| BOSS SY-200 | Standard-input guitar/bass synthesizer; one selected engine, 171 sounds and 128 memories | [Full archive](SINGLE-GUITAR.md#archived-processing-and-memory) |\n\nOther dedicated bass-effect records have not been researched here. Absence is not a negative capability claim or market-coverage claim.\n'
    return {'SINGLE-GUITAR.md':guitar,'SINGLE-VOCAL.md':vocal,'SINGLE-BASS.md':bass,path:specialist,fvpath:fvredirect}

def apply_plan():
    identity()
    payload=json.loads(PLAN.read_text())
    assert not payload['missing'],payload['missing']
    for path,digest in payload['input_hashes'].items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,'Concurrent change: '+path
    assert hashlib.sha256((ROOT/'research-state.json').read_bytes()).hexdigest()==payload['ledger_hash'],'Concurrent ledger change'
    for path in payload['outputs']:
        assert path in payload['input_hashes'] or not (ROOT/path).exists(),'Concurrent new file: '+path
    # Rollback is the pre-apply Git commit; only exact reviewed documents are written.
    for path,text in payload['outputs'].items():
        (ROOT/path).write_text(text)
        assert (ROOT/path).read_text()==text
    state=json.loads((ROOT/'research-state.json').read_text())
    state['user_requested_comparison_rebuild']['status']='implemented_pending_validation'
    state['user_requested_comparison_rebuild']['next']='Validate all four table memberships, exclusions, model-specific variant values, root/archive links and saved commits; then resume '+state['cursor']['model']+'.'
    state['comparison_membership']=payload['view_membership']
    state['comparison_bass_basis']=payload['bass_membership_basis']
    state['comparison_model_sources']={k:{'link':r['link'],'source_files':r['sources'],'finding_files':r['findings']} for k,r in payload['records'].items()}
    state['instrument_views']['ALL-GUITAR.md']={'record_count':len(payload['view_membership']['ALL-GUITAR.md']),'scope':'All recorded eligible guitar/acoustic multi-effects; four complete comparison tables, not navigation only','technical_refresh':False}
    state['instrument_views']['ALL-BASS.md']={'record_count':len(payload['view_membership']['ALL-BASS.md']),'bass_focused_record_count':len(BASS_FOCUSED),'shared_bass_capable_count':len(BASS_SHARED),'scope':'All positively documented bass-capable records in current classification, compared across four tables; remaining guitar classification explicitly unresolved','technical_refresh':False}
    state['instrument_views']['ALL-VOCAL.md']={'record_count':len(payload['view_membership']['ALL-VOCAL.md']),'vocal_only_count':len(VOCAL_ONLY),'combined_instrument_count':len(VOCAL_SHARED),'scope':'All retained vocal/live-mic records across four comparison tables','technical_refresh':False}
    state.setdefault('separate_specialist_archives',{'SINGLE-GUITAR.md':['BOSS SY-1','BOSS SY-200','BOSS AC-3','BOSS VO-1','BOSS XS-100'],'SINGLE-BASS.md':['BOSS SY-1','BOSS SY-200'],'SINGLE-VOCAL.md':['Flamma FV01','BOSS VO-1 (cross-reference)'],'counted_as_active':False,'moved_on':'2026-10-16','legacy_anchor_redirects_preserved':True,'source_before_move_sha256':{p:payload['input_hashes'][p] for p in ('effects/specialist.md','effects/findings/2026-10-14-flamma-fv01.md')}})
    state['validation'].update(unique_brand_model_pairs=state['active_model_count'],canonical_root_models=state['canonical_root_model_count'],legacy_only_models=state['legacy_only_model_count'],guitar_view_models=len(payload['view_membership']['ALL-GUITAR.md']),bass_view_models=len(payload['view_membership']['ALL-BASS.md']),bass_shared_models=len(BASS_SHARED),vocal_view_models=len(payload['view_membership']['ALL-VOCAL.md']))
    (ROOT/'research-state.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
    print('Applied reviewed plan: '+', '.join(payload['outputs']))


def readme_counts(text, state, membership):
    """Project inventory counts into the existing navigation without changing evidence."""
    rows = {
        'ALL-GUITAR.md': (r'(\|)\d+ guitar/acoustic', r'\g<1>' + str(len(membership['ALL-GUITAR.md'])) + ' guitar/acoustic'),
        'ALL-BASS.md': (r'(\|)\d+ documented bass-capable models: \d+ bass-focused plus \d+ shared', r'\g<1>' + str(len(membership['ALL-BASS.md'])) + ' documented bass-capable models: ' + str(len(BASS_FOCUSED)) + ' bass-focused plus ' + str(len(BASS_SHARED)) + ' shared'),
        'ALL-VOCAL.md': (r'(\|)\d+ vocal/live', r'\g<1>' + str(len(membership['ALL-VOCAL.md'])) + ' vocal/live'),
    }
    lines = text.splitlines(keepends=True)
    for filename, (pattern, replacement) in rows.items():
        matching = [i for i,line in enumerate(lines) if line.startswith('| **[' + filename + ']')]
        assert len(matching) == 1, 'Ambiguous README view: ' + filename
        i = matching[0]
        lines[i], count = re.subn(pattern, replacement, lines[i])
        assert count == 1, 'README count format changed: ' + filename
    for filename, models in state['root_brand_content'].items():
        prefix = '| [' + filename + '](' + filename + ') |'
        matching = [i for i, line in enumerate(lines) if line.startswith(prefix)]
        assert len(matching) == 1, 'Ambiguous README brand: ' + filename
        assert all('|' not in model and '\n' not in model for model in models), 'Invalid model label'
        labels = {'VALETON.md': {'GP-200': 'GP-200 (GP-200X variant)'}}
        lines[matching[0]] = prefix + ', '.join(labels.get(filename, {}).get(model, model) for model in models) + ' |\n'
    text = ''.join(lines)
    count = state['canonical_root_model_count']
    for pattern, replacement in (
        (r'All \d+ recorded models have root brand sections\.', f'All {count} recorded models have root brand sections.'),
        (r'Organization migration is incomplete:\*\* \d+ detailed models are root-canonical; \d+ still rely on legacy source records\.', f"Organization migration is incomplete:** {count} detailed models are root-canonical; {state['legacy_only_model_count']} still rely on legacy source records."),
        (r'(?<=profiles; )\d+ detailed models are root-canonical', f'{count} detailed models are root-canonical'),
        (r'\*\*\d+ active model records', f"**{state['active_model_count']} active model records"),
    ):
        text, matches = re.subn(pattern, replacement, text)
        assert matches == 1, 'README catalogue count format changed: ' + pattern
    return text

def verify_views():
    identity()
    state=json.loads((ROOT/'research-state.json').read_text())
    assert set(state['comparison_model_sources'])=={b+'::'+m for b,ms in state['inventory_by_brand'].items() for m in ms}
    readme = (ROOT/'README.md').read_text()
    assert readme_counts(readme, state, state['comparison_membership']) == readme, 'README catalogue/view counts are stale'
    for filename,ids in state['comparison_membership'].items():
        assert len(ids)==len(set(ids))
        text=(ROOT/filename).read_text()
        comparison_tables=[(h,r,c) for h,r,c in tables(text) if h[0]=='Model / complete evidence']
        assert len(comparison_tables)==4,(filename,len(comparison_tables))
        rendered = {key: {'facts': []} for key in ids}
        labels = {key.replace('::', ' '): key for key in ids}
        for headers, rows, context in comparison_tables:
            for row in rows:
                label = re.match(r'\[([^\]]+)\]', row[0])[1]
                if label in labels:
                    rendered[labels[label]]['facts'].append({'value': ' '.join(row[1:])})
        verify_evidence_owners(rendered, [g for g in state.get('evidence_identity_guards', []) if g['model'] in ids])
        expected=[k.replace('::',' ') for k in ids]
        for headers,rows,context in comparison_tables:
            actual=[re.match(r'\[([^\]]+)\]',r[0])[1] for r in rows]
            assert actual==expected,(filename,context,'membership mismatch')
            assert not set(actual)&set(state['excluded_models'])
        assert '](#)' not in text
        print(f'PASS {filename}: {len(ids)} exact models in each of 4 comparison tables; no excluded model rows')
    for filename in ('ALL-GUITAR.md','ALL-BASS.md'):
        assert (ROOT/filename).read_text().count('[Line 6 HX Effects](LINE6.md#hx-effects)')>=4
    for filename in ('ALL-GUITAR.md','ALL-BASS.md'):
        rows=[r for h,rs,c in tables((ROOT/filename).read_text()) if h[0]=='Model / complete evidence' and c=='Hardware and expression' for r in rs]
        wireless=next(r for r in rows if r[0].startswith('[Line 6 POD Go Wireless]'))
        standard=next(r for r in rows if r[0].startswith('[Line 6 POD Go]'))
        assert '**2.5 kg**' in wireless[-1] and '**2.35 kg**' not in wireless[-1]
        assert '**2.35 kg**' in standard[-1]
        all_standard_rows=[r for h,rs,c in tables((ROOT/filename).read_text()) if h[0]=='Model / complete evidence' for r in rs if r[0].startswith('[Line 6 POD Go]')]
        assert not any('Wireless-specific operation' in ' '.join(r) for r in all_standard_rows), 'Wireless-only prose leaked into standard POD Go'

    assert (ROOT/'SINGLE-GUITAR.md').exists() and (ROOT/'SINGLE-VOCAL.md').exists() and (ROOT/'SINGLE-BASS.md').exists()
    assert not list((ROOT/'.github/workflows').glob('*'))
    print('PASS: HX Effects guitar/bass inclusion, POD Go variant mass, specialist segregation and no workflows')

# Instrument membership is explicit and reviewable. It is not inferred from a shared
# enclosure, a BASS tone knob, a capture microphone, or an output connector.
BASS_FOCUSED = ['Korg::AX10B','Zoom::B1X original','Zoom::607','Tech 21::Bass Fly Rig v2','BOSS::ME-50B','Zoom::B2.1u','Flamma::FB200','Zoom::708II','Valeton::Dapper Bass Mini MES-2','Valeton::Dapper Bass VES-2','VOX::StompLab 2B','BOSS::ME-20B','BOSS::GT-1B','BOSS::GX-1B','BOSS::ME-90B','M-VAVE::TANK-B','M-VAVE::CUBE BABY BASS','Line 6::POD Express Bass','Zoom::B1 FOUR','Zoom::B1X FOUR','Zoom::B2 FOUR','Zoom::B6','Zoom::B1Xon','Zoom::B3n','Zoom::MS-60B','Zoom::MS-60B Plus','Zoom::B1on','Zoom::B3']
VOCAL_ONLY = ['Roland::VT-4','TC-Helicon::Critical Mass','JOYO::R-16 Vocal Lab','Flamma::FV04 Harmony','Flamma::FV03 Character','Flamma::FV02 Doubling','TC-Helicon::Harmony Singer 2','TC-Helicon::Duplicator','TC-Helicon::Mic Mechanic 2','HeadRush::VX5','BOSS::VE-5','TC-Helicon::PERFORM-VE','TC-Helicon::PERFORM-VK','TC-Helicon::PERFORM-V','Audota::AVE-100','BOSS::VE-1','BOSS::VE-2','BOSS::VE-500','BOSS::VE-22','BOSS::VE-20','TC-Helicon::VoiceLive Play','Zoom::V3','Zoom::V6-SP']
VOCAL_SHARED = ['Eventide::H90','Zoom::RFX-2200','Zoom::1201','BOSS::GT-001','Zoom::RFX-1000','Yamaha::REV500','TC Electronic::M-One XL','Lexicon::MPX100','Alesis::MIDIverb III','TC Electronic::M350','TC Electronic::M100','Zoom::RFX-2000','Yamaha::SPX1000','Yamaha::SPX2000','Lexicon::MX400','Lexicon::MX300','DigiTech::GNX4','Zoom::RFX-1100','Yamaha::SPX990','Yamaha::SPX900','Alesis::MIDIverb 4','Alesis::MicroVerb 4','Behringer::FX2000','Lexicon::MX200','Line 6::POD X3 Live','Line 6::POD HD500X','Line 6::Helix Stadium XL Floor','Line 6::Helix Floor','TC-Helicon::PERFORM-VG','TC-Helicon::VoiceLive 3 Extreme','BOSS::VE-8','TC-Helicon::Play Acoustic','HeadRush::Core','HeadRush::Prime','Hotone::Ampero II MP-350','Hotone::Ampero II Stage MP-380','Fender::Tone Master Pro','MOOER::GS1000']
BASS_SHARED = {
    "Kemper::PROFILER Head MK2": "Exact Head MK2 manufacturer page explicitly identifies electric guitar and bass. [Manufacturer](https://www.kemper-amps.com/store/en/profiler-head-b.html).",
    "Kemper::PROFILER PowerRack MK2": "Exact PowerRack MK2 manufacturer page explicitly identifies electric guitar and bass. [Manufacturer](https://www.kemper-amps.com/store/en_ca/profiler-powerrack-b.html).",
    "Kemper::PROFILER PowerHead MK2": "Exact manufacturer PowerHead MK2 page explicitly identifies electric guitar and bass. [Manufacturer](https://www.kemper-amps.com/store/en/profiler-powerhead-b.html).",
    "Kemper::PROFILER Rack MK2": "Exact manufacturer Rack MK2 page explicitly identifies electric guitar and bass. [Manufacturer](https://www.kemper-amps.com/store/uk/profiler-rack-b.html).",
    "Kemper::PROFILER Stage MK2": "Manufacturer Stage guide p.7 explicitly supports bass; current MK2 store identifies complete Stage processing architecture. [Guide](https://www.kemper-amps.com/download/static/263/Profiler%20Stage%20Quick%20Start%202021.pdf). Exact bass library/low-end performance not certified.",
    "Fractal Audio::FM9 MKII Turbo": "Exact MKII Turbo manufacturer store explicitly supports guitar and bass. [Manufacturer](https://shop.fractalaudio.com/products/fm9-mark-ii-turbo-amp-modeler-multi-fx-floor-unit).",
    "Kemper::PROFILER Player": "Official Player bundle explicitly describes bass use and bass PROFILE/DI routing. [Manufacturer](https://www.kemper-amps.com/store/au/profiler-player-power-bundle.html).",
    "Fractal Audio::FM3 MKII Turbo": "Manufacturer explicitly identifies guitar and bass processing. [Product](https://www.fractalaudio.com/fm3/).",
    "Sonicake::Matribox II QME-100": "Own Matribox II product explicitly lists guitar/bass/acoustic effects. Shared bass,not inferred from Pro or an EQ control. [Manufacturer](https://www.sonicake.com/products/matribox-ii).",
    "Sonicake::Matribox QME-50": "Own original Matribox product explicitly supports guitar/bass/acoustic processing. Shared bass,not low-end performance certification. [Manufacturer](https://www.sonicake.com/products/matribox).",
    "Sonicake::Pocket Master QME-10": "Own Pocket Master product explicitly lists guitar/bass/acoustic amp types. Shared bass;exact bass inventory/performance unresolved. [Manufacturer](https://www.sonicake.com/products/pocket-master).",
    "Sonicake::Matribox II Pro QME-200": "Own firmware1.1.1 manual pp41,44 lists A BassVT/A BassFT bass amps and bass cabinets. Shared bass capability;not performance certification. [Official regional manual](https://www.hotone.jp/files/brands/sonicake/products/matribox-ii-pro/manual/20260803-070736-v5r131-matribox_ii_pro_jp.pdf).",
    "Sonicake::Smart Box QME-20": "Manufacturer Smart Box page explicitly describes presets optimized for guitar and bass. Shared bass capability; bass-specific algorithms and low-end performance remain unverified. [Manufacturer product](https://www.sonicake.com/products/smart-box).",
    'Donner::Arena2000': "Own2022 Arena2000 manual p4 explicitly identifies input for guitar/bass;not connector-only inference. Bass-specific models/low-end performance remain unverified. [Original manufacturer manual](https://device.report/m/173567df81806b4e2da08b004d48be3265a7446aaebd91f140530baca984eb05_optim.pdf).",
    'Eventide::H90': 'Own manual1.12.5 Global Source Type explicitly lists Bass(Tenor) and Sub(Bass), adapting pitch tracking, filters and tone controls. Not sibling or EQ-knob inference. [Manufacturer manual](https://cdn.eventideaudio.com/manuals/h90/1.12.5/content/system-menu/global.html).',
    'Eventide::H9 Max': 'Own H9 User Guide p43 explicitly offers BASS and SYN.BAS source modes optimizing pitch algorithms and filter ranges; not inferred from an EQ knob or sibling. [Manufacturer manual](https://cdn.eventideaudio.com/uploads/2020/07/H9-Manual.pdf).',
    'Zoom::1201': 'Own1201 manual p4 explicitly covers electric guitar or bass through a preamp/compact effect;not direct high-impedance input. [Manufacturer manual](https://www.zoom.co.jp/sites/default/files/products/downloads/pdfs/E_1201.pdf).',
    "Hotone::Ampero Mini MP-50": "Own Mini firmware V2.2 manual explicitly lists five bass amp/preamp models, including SVT and B-15 models; model-specific processing evidence, not inferred from an EQ knob or sibling. [Manufacturer manual](https://res.hotoneaudio.com/prod/support/Ampero%20Mini_Online%C2%A0Manual_EN_Firmware%20V2.2.1773036333483.pdf).",
    'Line 6::Floor POD Plus': 'Own EnglishRevB section2•11 explicitly recommends TubePreamp as direct box for bass;not inferred from Bassman ancestry. [Manual](https://line6.com/data/l/0a060072caf7499051779818f/application/pdf/Floor_POD_Plus_user_manual.pdf)',
    'Behringer::V-AMP 3': 'Manufacturer manual p8 documents two bass-preset banks, with recording-oriented qualification;not bass-specialist equivalence. [Source](https://mediadl.musictribe.com/media/sys_master/h56/hb7/8849514528798.pdf)',
    "Line 6::POD HD300": "Own HD300/HD400 Flash2.0+ Advanced Guide includes Flip Top bass amp and115FlipTop bass cab;installed firmware must be checked.",
    "Fender::Mustang Micro": "Own PR5833 manual Studio Preamp explicitly ideal for bass/acoustic instruments;not inferred from plug compatibility.",
    'BOSS::KATANA:GO':'Own product explicitly provides bass mode3amps and30memories. https://www.boss.info/global/products/katana-go/',
    'Fender::Mustang Micro Plus':'Firmware1.1.11 adds10bassamps;installedfirmware must be checked. https://support.fender.com/hc/en-us/articles/45453482607899-Fender-Mustang-Micro-Plus-Firmware-Update-Instructions',
    'NUX::Mighty Plug MP-2':'Own product explicitly supports guitar and bass processing. https://nuxaudio.com/product/mightyplug/',
    'NUX::Mighty Plug Pro MP-3':'Own product explicitly identifies guitar and bass processing. https://nuxaudio.com/product/mightyplugpro/',
    'TC Electronic::PLETHORA X5':'Own official product explicitly documents bass-oriented global cabinet simulation. https://www.tcelectronic.com/en/products/0709-AIK',
    'Lexicon::MX400':'Own combined MX400/MX400XL manual p25 explicitly lists bass-track compression; appropriate line-level preamp/mixer or recorded-track routing required. https://adn.harmanpro.com/product_documents/documents/921_1516997571/MX400_and_MX400XL_Manual_18-0446V-F_original.pdf',
    'Lexicon::MX300':'Own manufacturer manual E p25 explicitly lists bass-track compression; use suitable line-level preamp/mixer or recorded-track routing. https://adn.harmanpro.com/product_documents/documents/916_1515793555/MX300_Manual_18-0473V-E_original.pdf',
    'Yamaha::SPX990':'Own Yamaha operation manual preset applications explicitly include Bass, Guitar and Vocal, printed pp12–13; suitable line-level preamp/mixer routing. [Manual](https://www.audiorama-berlin.de/pdf/yamahaspx990man.pdf).',
    'Behringer::FX2000':'Manufacturer explicitly lists bass,guitar andvocals;use suitable line-level amp/mixer routing. [Product](https://www.behringer.com/en/products/0828-AAG).',
    'DigiTech::GNX4':'Own manual p19 explicitly connects guitar or bass and documents amp modeling for both. https://digitech.com/wp-content/uploads/2022/09/GNX4Manual_original.pdf',
    'DigiTech::GNX3':'Manufacturer explicitly documents bass amp modeling for recording rhythm tracks. [GNX3 product](https://digitech.com/dp/gnx3/).',
    "Line 6::POD HD400":"Own HD300/400 Advanced Guide RevA for Flash2.0 lists Flip Top bass amp and115 Flip Top bass cab,pp5•9–11. [Official guide](https://line6.com/data/6/0a06434df9be5005ac8bcc52f/application/pdf/POD%20HD300%20Advanced%20Guide%20%28%20Rev%20A%20%29.pdf).",
    'Line 6::POD XT Live':'Conditional: manufacturer Bass Expansion listing explicitly includes PODxt Live and adds28 bass amps/22 cabinets. Optional authorization required; seller license and current activation unverified. [Manufacturer listing](https://shop-us.line6.com/standard-model-packs/bass-expansion-pack/).',
    'Line 6::POD X3 Live':'Own Live product documentation explicitly lists bass amp/cab models and instrument input. [Product](https://line6.com/legacy/podx3live?locale=en_US).',
    'Behringer::Bass V-AMP PRO':'Own manufacturer manual explicitly covers rack PRO for bass, acoustic/electric guitar and keyboards, with its own rack I/O columns. [Manual](https://images.thomann.de/pics/atg/atgdata/document/manual/163587_manual_engl.pdf).',
    'Behringer::Bass V-AMP':'Manufacturer explicitly advertises desktop Bass V-AMP for bass, acoustic/electric guitar and keyboards; shared multi-instrument classification preserves its bass role. [Product](https://www.behringer.com/en/products/0709-AAC).',
    'Line 6::AMPLIFi FX100':'Manufacturer AMPLIFi/Firehawk model descriptions explicitly describe Tube Instrument Preamp as intended for piezo acoustic or bass. [Model descriptions](https://kb.line6.com/full-list-of-amplifi-firehawk-series-amps-effects-and-cabs).',
    'Line 6::POD HD500X':'Own Advanced Guide Rev A section6•4 explicitly recommends Flip Top bass amp/cab; section7•9 documents Vintage Pre with bass amps. [Official guide](https://l6c-acdn2.line6.net/data/6/0a06434c6fb051e03e8ab63dc/application/pdf/POD%20HD500X%20Advanced%20Guide%20%28%20Rev%20A%20%29.pdf).',
    'Line 6::Helix Stadium XL Floor':'Own Stadium rear manual explicitly supports bass amplifiers in4/7cable setups;USB chapter explicitly identifies bass DI input processing.',
    'Line 6::Helix Floor':'Own Floor product AUX input explicitly accepts active bass;own Cheat Sheet says guitar or bass instrument input.',
    'HeadRush::Pedalboard':'Own official Pedalboard product explicitly models Ampeg B15/SVT bass amps and Darkglass bass preamp; not inferred from a BASS EQ knob or sibling.',
    'HeadRush::Gigboard':'Own official Gigboard product explicitly identifies instrument input for guitars and basses; not inferred from other boards.',
    'BOSS::Pocket GT':'Own Parameter Guide Rev02 pp17–18 explicitly labels presets71–90 for bass guitar; not inferred from GT1 sibling or EQ.',
    'Line 6::HX One':'Official HX One FAQ explicitly identifies guitarists and bassists; product input instructions explicitly include bass guitar. One selected model plus gate.',
    'Line 6::Pocket POD':'Own Reference Manual §3•2 explicitly suggests Tube Preamp as a direct box for bass; not general certification of all guitar models.',
    'Line 6::M9':'Official M5/M9/M13 FX Parameters §3•6 explicitly documents Bass Octaver for bass; algorithm suitability varies.',
    'Line 6::M5':'Official M5/M9/M13 FX Parameters §3•6 explicitly describes Bass Octaver as great for bass; §3•9 also documents bass use for 4 Band Shift EQ. One selected model plus gate; suitability varies by algorithm.',
    "Line 6::POD HD500":"Original HD500 Advanced Guide v2.10 Rev A pp.6•4,6•6,6•13,6•15 explicitly recommends Flip Top bass amp, matching 1×15 cabinet and eight bass-cab microphone models. This establishes model-specific bass support without relying on HD500X or later paid packs. [Official guide](https://l6c-acdn2.line6.net/data/6/0a06434dc1a55085c5d6532bf/application/pdf/POD%20HD500%20Advanced%20Guide%20v2.10%20%28%20Rev%20A%20%29.pdf).",
    'Korg::PANDORA stomp':'Korg specifies guitar/bass input and explicitly marks bass-specific amps/cabs/effects.',
    'Zoom::MS-70CDR Plus':'Own manufacturer preset Ver1.00 patch004 Phase Room explicitly covers guitar or bass;own effects include bass chorus andbass autowah. Not original/seller inference. [Preset list](https://zoomcorp.com/media/documents/E_MS-70CDRplus_Patchlist.pdf).',
    'Zoom::MS-70CDR':'Original manufacturer MS-70CDR product explicitly identifies guitar/bass effects and manual p.4 bass input. Not inferred from plus or a BASS EQ knob. [Primary product](https://zoomcorp.com/en/us/multi-effects/multistomp-pedals/ms-70cdr/).',
    'Zoom::A1X FOUR':'Official shared A1 FOUR/A1X FOUR product explicitly names acoustic bass. Scope is acoustic bass;A1 FOUR demonstration is not an A1X-specific demonstration or universal electric-bass certification. [Primary product](https://zoomcorp.com/en/gb/multi-effects/acoustic/A1-FOUR-A1X-FOUR/).',
    'Zoom::A1 FOUR':'Official A1 FOUR/A1X FOUR product page explicitly names acoustic bass and demonstrates A1 FOUR with upright bass; octaves and piezo processing. Scope is acoustic/upright bass,not universal electric-bass equivalence. [Primary product](https://zoomcorp.com/en/gb/multi-effects/acoustic/A1-FOUR-A1X-FOUR/).',
    'Neural DSP::Nano Cortex':'Exact manufacturer product page explicitly describes a complete guitar or bass rig; device list includes four bass amp captures, a bass drive capture and two bass cabinets. [Primary product](https://neuraldsp.com/nano-cortex).',
    'IK Multimedia::TONEX Pedal':'Standard TONEX Pedal manufacturer-authored manual v1.0.4 pp.4,13 explicitly identifies guitar/bass use; current standard Reloaded preset documentation includes bass banks. [Original manual mirror](https://files.kraftmusic.com/media/ownersmanual/TONEX_Pedal_User_Manual.pdf). Not inferred from Bass Edition.',
    'IK Multimedia::TONEX ONE':'Standard TONEX ONE manufacturer announcement24April2024 explicitly identifies guitar/bass rigs; original model manual v1.0rev05 pp.4,32 confirms. Not inferred from Bass Edition or a BASS EQ knob. [Primary announcement](https://www.ikmultimedia.com/news/index.php?id=TonexOneAnnounced).',
    'Line 6::Helix LT':'LT-specific manufacturer comparison chart v1.03 explicitly lists twelve bass amp models and Return1/2 guitar/bass inputs; not sibling inference.',
    'MOOER::GS1000':'Exact manufacturer manual specifies guitar/bass input, ten bass amp models and ten bass cabinet models; regional product confirms bass use.',
    'HeadRush::Prime':'Model-specific manufacturer Prime input/routing and bass library evidence; not inferred from Core.',
    'Audota::AME-200':'Model-specific finding explicitly describes guitar/bass capability.',
    'Audota::AME-200 Pro':'Separate Pro finding explicitly describes guitar/bass capability.',
    'BOSS::GT-1000CORE':'Bass mode and bass drive types in retained BOSS comparison.',
    'BOSS::GT-1000':'Guitar/bass processing in retained BOSS comparison.',
    'BOSS::GX-10':'Nine bass amps in the documented 32-amp library.',
    'BOSS::GX-100':'Version 2 adds six bass amps; retained dated primary evidence.',
    'BOSS::GM-800':'GK-5B/Serial GK bass use; requires divided pickup/interface.',
    'HeadRush::Core':'Guitar/bass processing retained in existing bass classification; mic is separate.',
    'HeadRush::MX5':'Root model explicitly identifies guitar/bass processing.',
    'HeadRush::Flex Prime':'Root model explicitly documents guitar/bass library.',
    'Fender::Tone Master Pro':'Root model explicitly identifies guitar/bass processing.',
    'Hotone::Ampero MP-100':'Complete model-specific finding identifies guitar/bass multi-effects.',
    'Hotone::Ampero II Stomp MP-300':'Complete model-specific finding identifies guitar/bass multi-effects.',
    'Hotone::Ampero II MP-350':'Complete model-specific finding explicitly identifies guitar/bass/vocal processing.',
    'Hotone::Ampero II Stage MP-380':'Separate Stage finding explicitly identifies guitar/bass/vocal processing.',
    'Hotone::Ampero One MP-80':'Manufacturer input and model-specific acoustic/bass library evidence.',
    'Line 6::HX Stomp':'Documented bass-capable HX processing in retained bass classification.',
    'Line 6::HX Effects':'Manufacturer FAQ explicitly identifies guitar and bass rigs.',
    'Line 6::HX Stomp XL':'Firmware 3.80 appendix includes seventeen bass amp models.',
    'Line 6::POD Go':'Model-specific bass amps and firmware 2.50 bass additions.',
    'Line 6::POD Go Wireless':'Explicit manufacturer-shared POD Go documentation includes bass models.',
    'MOOER::GE1000':'Model-specific appendix includes bass preamps and cabinets.',
    'MOOER::GE1000 Li':'Manufacturer shared manual explicitly covers Li; guitar/bass finding retained.',
    'MOOER::GE250':'Existing bass view documents bass-capable library; count conflicts retained.',
    'M-VAVE::TANK MINI':'Five bass amps and factory bass banks.',
    'M-VAVE::MK-20':'Model-specific finding explicitly identifies guitar/bass processing.',
    'M-VAVE::MK-300':'Thirty bass amps and twenty-five bass cabinets in retained library.',
    'M-VAVE::TANK-PRO':'Model-specific bass EQ/amp entries.',
    'M-VAVE::ANN Blackbox':'Five bass amps/cabs and bass factory presets.',
    'M-VAVE::Pocket Amp':'Five bass amps/cabs in the model-specific library.',
    'NUX::MG-300 original':'Model-specific root profile retains firmware-added bass processing.',
    'NUX::MG-400':'Model-specific acoustic/bass cabinet content documented; no blanket bass-amp claim.',
    'NUX::MG-30':'Five bass amps in manufacturer 35-amp breakdown.',
    'Roland::GR-55':'Separate guitar/bass modes with bass modeling and firmware-qualified factory memory; GK required.',
    'Valeton::GP-100':'Forty-five guitar/bass/acoustic amp models in retained evidence.',
    'Valeton::GP-150':'Ten bass factory presets in retained model-specific record.',
    'Valeton::GP-180':'Documented bass-related processing in retained bass comparison; full profile remains partial.',
    'Valeton::GP-200':'Explicit guitar/bass/acoustic amp/cab library.',
    'Valeton::GP-200LT':'Root record explicitly identifies guitar/bass/acoustic processing.',
    'Valeton::GP-200JR':'Root record explicitly identifies guitar/bass/acoustic processing; manual copy errors retained.',
    'Zoom::G11':'V2 adds nine bass amps and bass effects; root record retains dated distinctions.',
}

GROUPS = {
    'expression': r'expression|\bEXP\b|^external control|^control / FS01 assignments$',
    'controls': r'k/f/b|knob|rotary|footswitch|buttons|^controls|physical controls|expression.*controls',
    'display': r'display|screen|diagonal|monochrome|touch|^evidence and remaining uncertainty$',
    'body': r'dimension|width|w×|weight|body|size|mass|^physical$',
    'processing': r'^delay / (?:source wording|time limits)$|^historical count conflict$|^delay claim conflict$|^firmware-qualified model|processing|simultaneous|architecture|model-total disagreement|block|categor|choice|library|^modules|factory amps|efx|^effects',
    'memory': r'memory|preset|storage',
    'sound': r'^bass capability|^(?:bass / (?:instrument|vocal)|instrument) scope$|synth|acoustic|harmony|special sound|^sound|^vocal$|^instrument/function$',
    'loading': r'\birs?\b|capture|\bnam\b|loading|import(?:ing|s)?\b|proprietary|conversion',
    'io': r'^instrument / input requirements$|^midi / backup$|^analog|^conversion.*analog|^audio(?:/control| inputs?| outputs?)$|^level conflict$|^built-in instrument wireless$|\bports?\b|connections?|i/o|^inputs?|^(?:main )?outputs?|^aux|headphones?|fx loop|microphone|phantom|pickup|midi.*usb|usb.*control|data.*control|control.*data|instrument.*loop|instrument.*aux',
    'power': r'power|battery|^dc|^supply$',
    'editor': r'^usb / (?:monitoring(?: and cable)?|windows driver|macos driver|midi)$|app|software|edit|config|record|usb.*audio|^audio$|^usb$|^digital|^audio interface$',
    'live': r'^save / tuner / gate$|^tuner / bypass$|automation|live|practice|practical|stage|loop|drum|extra|feature|scene|firmware|routing|operation',
}

def clean(value):
    # Source marker shorthand is resolved through the linked full model record;
    # never leave broken reference-style links in generated standalone views.
    value=re.sub(r'(?<!!)\[([^\]]+)\](?!\()',r'\1',value)
    value=value.replace('|','&#124;').replace('\n',' ')
    return re.sub(r'\s+',' ',value).strip()

def cell(record, group):
    selected=[]
    seen=set()
    # Canonical/complete field rows take precedence over looser legacy summary rows.
    for fact in record['facts']:
        field=fact['field']
        if re.search(r'IDR|USD|price|retail|used evidence|commit',field,re.I):
            continue
        if not re.search(GROUPS[group],field,re.I):
            continue
        if group=='loading' and re.search(r'analog|converter',field,re.I) and not re.search(r'\bIRs?\b|\bNAM\b|capture',field,re.I):
            continue
        if group=='io' and re.search(r'display|screen|diagonal',field,re.I):
            continue
        value=clean(fact['value'])
        identity=(field.lower(),value)
        if identity in seen or value in ('?','**?**',''):
            continue
        seen.add(identity)
        if group=='expression' and field=='External expression':
            if 'No built-in' in fact['context']:
                value='Built-in: no. External: '+value
            elif 'Built-in expression' in fact['context']:
                value='Built-in: yes. External: '+value
        selected.append('**'+clean(field).replace('**','')+':** '+value)
    return '<br>'.join(selected) if selected else '? — not established in retained model evidence'

def price_cells(record):
    used=[]
    other=[]
    for fact in record['facts']:
        label=fact['field']
        value=clean(fact['value'])
        if not re.search(r'IDR|retail evidence|retail observation|^prices|^idr$',label,re.I):
            continue
        if 'USD' in label or not ('Rp' in value or '?' in value):
            continue
        entry='**'+clean(label).replace('**','')+':** '+value
        if re.search(r'\b(?:used|preloved|bekas|second)\b',label,re.I) and not re.search(r'new|retail',label,re.I):
            used.append(entry)
        else:
            other.append(entry)
            # Many canonical records preserve qualified used evidence in a retail/used
            # paragraph. Keep its wording rather than extracting an unqualified number.
            hit=re.search(r'(?:\*\*)?(?:Explicit\s*)?(?:used|usedlike-new|Used IDR|seller-labelled used)[\s\S]*',value,re.I)
            if hit and 'Rp' in hit[0] and not re.search(r'(?:not establish|not proof of|not verified as)\s*$',value[:hit.start()]+' ',re.I):
                used.append(hit[0])
    return ('<br>'.join(dict.fromkeys(used)) or '? — no qualified used IDR amount established'), ('<br>'.join(dict.fromkeys(other)) or '? — no qualified retail/new IDR amount established; foreign prices are not converted')

def table(records, ids, headers, groups):
    result=['| Model / complete evidence | '+' | '.join(headers)+' |','|'+'---|'*(len(headers)+1)]
    for key in ids:
        record=records[key]
        name=record['brand']+' '+record['model']
        cells=price_cells(record) if groups==['prices'] else [cell(record,g) for g in groups]
        result.append('| ['+name+']('+record['link']+') | '+' | '.join(cells)+' |')
    return '\n'.join(result)+'\n'

def render(records,state):
    assert len(records)==state['active_model_count']
    guitar=[k for k in records if k not in BASS_FOCUSED+VOCAL_ONLY]
    bass=[k for k in records if k in BASS_FOCUSED or k in BASS_SHARED]
    vocal=[k for k in records if k in VOCAL_ONLY+VOCAL_SHARED]
    ids={'ALL-GUITAR.md':guitar,'ALL-BASS.md':bass,'ALL-VOCAL.md':vocal}
    descriptions={
        'ALL-GUITAR.md':'All '+str(len(guitar))+' recorded guitar/acoustic **multi-effects**, including effects-only HX Effects and Cerberus. Amp modeling, an expression pedal and floor operation are not inclusion requirements. Dedicated single-function pedals are in [SINGLE-GUITAR.md](SINGLE-GUITAR.md), outside these tables and active counts.',
        'ALL-BASS.md':str(len(bass))+' recorded bass-focused or explicitly documented bass-capable multi-effects: '+str(len(BASS_FOCUSED))+' bass-focused and '+str(len(BASS_SHARED))+' shared models. This compares actual model records, not only bass-branded units. Capability evidence is listed below; it does not establish equal low-end retention or every effect working equally well on bass.',
        'ALL-VOCAL.md':'All '+str(len(vocal))+' recorded vocal or live mic-path multi-effects: '+str(len(VOCAL_ONLY))+' vocal-only and '+str(len(VOCAL_SHARED))+' with independent acoustic/general-instrument processing. Guitar-thru/chord detection is not a processed guitar path. FV01 remains excluded in [SINGLE-VOCAL.md](SINGLE-VOCAL.md); a mic input does not imply harmony or pitch correction.',
    }
    outputs={}
    for filename,model_ids in ids.items():
        title={'ALL-GUITAR.md':'All guitar and acoustic-guitar multi-effects — comparison','ALL-BASS.md':'All bass multi-effects — comparison','ALL-VOCAL.md':'All vocal and live mic-path multi-effects — comparison'}[filename]
        text='# '+title+'\n\n[Guitar](ALL-GUITAR.md) · [Bass](ALL-BASS.md) · [Vocal](ALL-VOCAL.md) · [Category](MULTI-EFFECTS.md) · [Repository](README.md)\n\n'+descriptions[filename]+'\n\n'
        text+='These are **comparisons of the recorded catalogue**, not exhaustive market coverage or fresh stock certification. Organized 2026-10-16 from the linked source records; their original technical/price dates, firmware, revision and access limits still apply. Every model remains partial. **? means unverified, not No.** Read the complete linked record for sources and conflicting evidence; this view does not silently resolve those conflicts.\n\n'
        text+='K/F/B = independently adjustable rotary controls / footswitches / separate buttons; toe and power switches are additional unless explicitly stated. Body axes and mass qualifications are retained. Color does not prove touch; USB audio does not prove bus power; IRs, native NAM, converted NAM and proprietary captures differ.\n\n'
        text+='## Hardware and expression\n\n'+table(records,model_ids,['Built-in / external / toe expression','Knobs / footswitches / buttons','Display diagonal / color / touch','Dimensions / mass / size'],['expression','controls','display','body'])
        text+='\n## Processing and memory\n\n'+table(records,model_ids,['Simultaneous blocks / category choices','Factory / user / total memory','Synth / acoustic or vocal functions','IR / NAM / proprietary captures'],['processing','memory','sound','loading'])
        text+='\n## Connections, power and practical use\n\n'+table(records,model_ids,['Audio / control I/O','Voltage / polarity / current / battery / USB power','Editors / recording / platform distinctions','Looper / drums / scenes / routing'],['io','power','editor','live'])
        text+='\n## Separate IDR asking-price evidence\n\nAll amounts are dated asking observations, **not a verified used-to-new range, completed sale or checkout stock**. Sold-out, voucher, region, bundle, condition and cached-access qualifications belong to the offer and remain visible. Missing IDR is not estimated from USD. A retail-labelled offer is not independently confirmed new condition.\n\n'+table(records,model_ids,['Used IDR evidence / limitations','Retail, new, conditional or historical IDR evidence / limitations'],['prices'])
        if filename=='ALL-BASS.md':
            text+='\n## Why shared models are included\n\n| Shared model | Retained bass evidence |\n|---|---|\n'
            text+='\n'.join('| ['+records[k]['brand']+' '+records[k]['model']+']('+records[k]['link']+') | '+basis+' |' for k,basis in BASS_SHARED.items())+'\n'
            unresolved=[k for k in guitar if k not in BASS_SHARED]
            text+='\n## Bass classification still unresolved\n\nThese other guitar/acoustic records have **not been certified bass-capable or unsuitable** by this pass. They stay outside the positive bass comparison until model-specific evidence establishes the intended processing path; a BASS EQ knob or sibling product is insufficient.\n\n'
            text+='; '.join('['+records[k]['brand']+' '+records[k]['model']+']('+records[k]['link']+')' for k in unresolved)+'.\n'
        text+='\n## Scope and provenance\n\nInstrument views overlap and must not be summed. All '+str(state['active_model_count'])+' active models count once in `research-state.json`; the six explicitly excluded archives never enter these tables. Former/donated eligible devices remain without private receipt/order/payment details. Root brand records take precedence where consolidated; legacy sources remain for full evidence until a checked lossless merge. No GitHub workflow is used.\n'
        outputs[filename]=text
        Path('/tmp/instrumentfx-'+filename).write_text(text)
    return {'outputs':outputs,'view_membership':ids,'bass_membership_basis':BASS_SHARED}

def test_comparison_selection():
    current = '| Required field | Evidence |\n|---|---|\n| IR | 16 user slots |\n'
    fixture = 'Historical capacity unknown\n<!-- comparison evidence begins -->'+current+'<!-- comparison evidence ends -->Archive remains'
    assert comparison_body(fixture) == current
    assert comparison_body('Legacy without markers') == 'Legacy without markers'
    for invalid in ('<!-- comparison evidence begins -->', '<!-- comparison evidence ends -->', '<!-- comparison evidence ends --><!-- comparison evidence begins -->', fixture+fixture):
        try:
            comparison_body(invalid)
        except AssertionError:
            pass
        else:
            raise AssertionError('Malformed comparison range accepted')
    state = json.loads((ROOT/'research-state.json').read_text())
    readme = (ROOT/'README.md').read_text()
    stale = re.sub(r'(\| \[JOYO.md\]\(JOYO.md\) \|)[^\n]+', r'\g<1>GEM BOX original,II,III |', readme)
    projected = readme_counts(stale, state, state['comparison_membership'])
    joyo_row = next(line for line in projected.splitlines() if line.startswith('| [JOYO.md]'))
    assert all(model in joyo_row for model in state['root_brand_content']['JOYO.md']), 'README brand navigation dropped a recorded model'
    assert readme_counts(projected, state, state['comparison_membership']) == projected
    print('PASS: explicit comparison selection keeps current evidence, preserves legacy fallback and rejects malformed ranges.')


def test_field_projection():
    negative = {'facts':[{'field':'IDR qualified observations','value':'Seller name does not establish used condition. Another offer Rp5.929.110 is sold out.','context':''}]}
    assert price_cells(negative)[0].startswith('?'), 'Negated condition leaked into used-price evidence'
    positive = {'facts':[{'field':'Used IDR','value':'Rp3.000.000 seller-labelled used; stock unconfirmed','context':''}]}
    assert 'Rp3.000.000' in price_cells(positive)[0]
    cases = {
        'expression': ['Built-in / external EXP', 'Control / FS01 assignments'],
        'io': ['Instrument / input requirements', 'MIDI / backup', 'Audio/control', 'Audio input', 'Audio inputs', 'Audio output', 'Audio outputs', 'Level conflict', 'Built-in instrument wireless', 'Analog levels / conversion', 'Conversion / analog levels'],
        'sound': ['Vocal', 'Instrument/function', 'Bass capability', 'Bass capability / license condition', 'Bass / instrument scope', 'Bass / vocal scope', 'Instrument scope'],
        'processing': ['Delay / source wording', 'Delay / time limits', 'Model-total disagreement', 'Firmware-qualified model changes', 'Historical count conflict', 'Delay claim conflict'],
        'editor': ['Audio interface', 'USB / monitoring', 'USB / Windows driver', 'USB / macOS driver', 'USB / monitoring and cable', 'USB / MIDI'],
        'power': ['Supply'],
        'display': ['Evidence and remaining uncertainty'],
        'live': ['Backing-track automation', 'Save / tuner / gate', 'Tuner / bypass'],
    }
    for group, labels in cases.items():
        for label in labels:
            record = {'facts': [{'field': label, 'value': 'Retained qualified evidence', 'context': ''}]}
            assert 'Retained qualified evidence' in cell(record, group), (group, label)
    for label in ('Analog levels / conversion', 'Conversion / analog levels'):
        record = {'facts': [{'field': label, 'value': '24-bit converters, analog level limits', 'context': ''}]}
        assert '24-bit converters' not in cell(record, 'loading'), 'Analog conversion leaked into IR/capture column'
    assert 'Retained qualified evidence' not in cell({'facts': [{'field': 'Manufacturer identity', 'value': 'Retained qualified evidence', 'context': ''}]}, 'processing')
    print('PASS: technical field labels reach their intended columns; manufacturer identity stays in the full record.')


def test_field_extraction():
    test_evidence_owners()
    fixture = {'consolidation_and_price_findings': [
        {'verification_kind':'complete-source-body-v1', 'destination':'BRAND.md#model', 'source':'effects/findings/original.md'},
        {'verification_kind':'complete-source-body-v1', 'destination':'BRAND.md#sibling', 'source':'effects/findings/sibling.md'},
        {'verification_kind':'complete-source-body-v1', 'destination':'BRAND.md#model', 'source':'effects/findings/missing.md'}]}
    assert manifest_findings(fixture, {'effects/findings/original.md':'', 'effects/findings/sibling.md':''}, 'BRAND.md#model') == {'effects/findings/original.md'}
    headers = ['Field', 'Finding', 'Evidence']
    row = ['Expression', 'External only', '[Manufacturer][manual]']
    value = field_value(headers, row)
    assert value == 'External only — Evidence: [Manufacturer][manual]'
    linked = relink(value, 'HEADRUSH.md', {'manual': 'https://example.com/original-manual.pdf'})
    assert '[Manufacturer](https://example.com/original-manual.pdf)' in linked
    refs = {'ad8-m': 'https://example.com/ad8.pdf'}
    assert relink('Evidence [AD8-M].', 'BOSS.md', refs) == 'Evidence [AD8-M](https://example.com/ad8.pdf).'
    assert relink('[Manual][]', 'BOSS.md', {'manual': 'https://example.com/manual.pdf'}) == '[Manual](https://example.com/manual.pdf)'
    assert relink('[unknown] and [inline](https://example.com/page)', 'BOSS.md', refs) == '[unknown] and [inline](https://example.com/page)'
    assert relink('![AD8-M](photo.png)', 'BOSS.md', refs) == '![AD8-M](photo.png)'
    assert field_value(['Field', 'Finding'], row[:2]) == 'External only'
    assert field_value(headers, row[:2]+['']) == 'External only'
    print('PASS: separate source-column evidence survives extraction and reference resolution; two-column values stay unchanged.')

if __name__=='__main__':
    if sys.argv[1]=='test-extraction':
        test_field_extraction()
    elif sys.argv[1]=='test-fields':
        test_field_projection()
    elif sys.argv[1]=='test-selection':
        test_comparison_selection()
    elif sys.argv[1]=='plan':
        make_plan()
    elif sys.argv[1]=='apply':
        apply_plan()
    elif sys.argv[1]=='verify':
        verify_views()
    else:
        raise SystemExit('Only reviewed preview mode is currently implemented')
