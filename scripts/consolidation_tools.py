"""Reviewable, lossless model consolidation; keeps legacy sources and their links."""
import hashlib
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
import comparison_views
import research_tools

ROOT = Path(__file__).resolve().parent.parent
PLAN = Path('/tmp/instrumentfx-consolidation-plan.json')
MODELS = {
    'ge150-pro': ('GE150 Pro', 'effects/findings/2026-10-14-mooer-ge150-pro.md'),
    'ge200-pro-li': ('GE200 Pro Li', 'effects/findings/2026-10-14-mooer-ge200-pro-li.md'),
    'ge200-pro': ('GE200 Pro', 'effects/findings/2026-10-14-mooer-ge200-pro.md'),
    'ge100-pro-li': ('GE100 Pro Li', 'effects/findings/2026-10-14-mooer-ge100-pro-li.md'),
    'ge100-pro': ('GE100 Pro', 'effects/findings/2026-10-14-mooer-ge100-pro.md'),
    'ge150-pro-li': ('GE150 Pro Li', 'effects/findings/2026-10-14-mooer-ge150-pro-li.md'),
    'ge200-original': ('GE200 original', 'effects/findings/2026-10-14-mooer-ge200.md'),
    'ge150-original': ('GE150 original', 'effects/findings/2026-10-14-mooer-ge150.md'),
    'ge100-original': ('GE100 original', 'effects/findings/2026-10-14-mooer-ge100.md'),
    'ampero-mp300': ('Ampero II Stomp MP-300', 'effects/findings/2026-10-15-hotone-ampero-ii-stomp-mp300.md'),
    'ampero-mp380': ('Ampero II Stage MP-380', 'effects/findings/2026-10-14-hotone-ampero-ii-stage-mp380.md'),
    'ampero-mp350': ('Ampero II MP-350', 'effects/findings/2026-10-14-hotone-ampero-ii-mp350.md'),
    'ampero-mp100': ('Ampero MP-100', 'effects/findings/2026-10-14-hotone-ampero-mp100.md'),
    'ampero-mini': ('Ampero Mini MP-50', 'effects/findings/2026-10-14-hotone-ampero-mini.md'),
    'hx-stomp-xl': ('HX Stomp XL', 'effects/findings/2026-10-14-line6-hx-stomp-xl.md'),
    'g6': ('G6', 'effects/findings/2026-10-15-zoom-g6.md'),
    'g1-four': ('G1 FOUR', 'effects/findings/2026-10-14-zoom-g1-four.md'),
    'g1x-four': ('G1X FOUR', 'effects/findings/2026-10-14-zoom-g1x-four.md'),
    'g2-four': ('G2 FOUR', 'effects/findings/2026-10-14-zoom-g2-four.md'),
    'g2x-four': ('G2X FOUR', 'effects/findings/2026-10-14-zoom-g2x-four.md'),
    'b1-four': ('B1 FOUR', 'effects/bass.md'),
    'b1x-four': ('B1X FOUR', 'effects/bass.md'),
    'b2-four': ('B2 FOUR', 'effects/bass.md'),
    'b6': ('B6', 'effects/bass.md'),
    'v3': ('V3', 'effects/vocal.md'),
    'v6-sp': ('V6-SP', 'effects/vocal.md'),
    'gt-1b': ('GT-1B', 'effects/bass.md'),
    'gx-1b': ('GX-1B', 'effects/bass.md'),
    'me-90b': ('ME-90B', 'effects/bass.md'),
    've-1': ('VE-1', 'effects/vocal.md'),
    've-2': ('VE-2', 'effects/vocal.md'),
    've-500': ('VE-500', 'effects/vocal.md'),
    've-22': ('VE-22', 'effects/vocal.md'),
    've-8': ('VE-8', 'effects/vocal.md'),
    've-20': ('VE-20', 'effects/vocal.md'),
    'gm-800': ('GM-800', 'effects/specialist.md'),
    'gt-1000': ('GT-1000', 'effects/findings/2026-10-15-boss-gt1000-display-idr.md'),
    'gx-100': ('GX-100', 'effects/findings/2026-10-15-boss-gx100-display-idr.md'),
    'me-90': ('ME-90', 'effects/findings/2026-10-15-boss-me90-display-idr.md'),
    'gx-1': ('GX-1', 'effects/findings/2026-10-15-boss-gx1-display-idr.md'),
    'gt-1': ('GT-1', 'effects/findings/2026-10-15-boss-gt1-display-idr.md'),
    'gx-10': ('GX-10', 'effects/findings/2026-10-15-boss-gx10-display-idr.md'),
    'gt-1000core': ('GT-1000CORE', 'effects/findings/2026-10-15-boss-gt1000core-display-idr.md'),
}


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def preserved_body(source, prefix):
    body = source.split('\n', 1)[1]
    body = re.sub(r'^## ', '### ', body, flags=re.M)
    refs = re.findall(r'^\[([^\]]+)\]:', body, re.M)
    for ref in refs:
        body = body.replace('[' + ref + ']', '[' + prefix + '-' + ref + ']')
    return body, refs


def verify_preserved(state):
    for entry in state.get('consolidation_and_price_findings', []):
        if entry.get('verification_kind') == 'complete-model-rows-v1':
            source = (ROOT / entry['source']).read_text()
            assert digest(source) == entry['source_sha256'], entry['source']
            model = entry.get('model_name', entry['models'][0].removeprefix('Zoom '))
            text = (ROOT / entry['destination'].split('#')[0]).read_text()
            section = text.split('\n## ' + model + '\n', 1)[1].split('\n## ', 1)[0]
            actual = []
            aliases = {comparison_views.norm(model), comparison_views.norm(entry.get('brand', 'Zoom')+' '+model)}
            for headers, rows, context in comparison_views.tables(source):
                for row in rows:
                    if comparison_views.norm(row[0]) in aliases:
                        actual += [dict(field=h,value=v,source=entry['source'],context=context) for h,v in zip(headers[1:],row[1:])]
            assert actual == entry['retained_comparison_facts'], 'Changed or missing source rows: '+model
            for fact in actual:
                assert fact['value'] in section, 'Lost model field: '+fact['field']
            for paragraph in entry['retained_context']:
                assert paragraph in source and paragraph in section, 'Lost model context: '+model
            for url in entry['retained_source_urls']:
                assert url in source and url in section, 'Lost source URL: '+url
            continue
        if entry.get('verification_kind') != 'complete-source-body-v1':
            continue
        source = (ROOT / entry['source']).read_text()
        assert digest(source) == entry['source_sha256'], entry['source']
        if entry.get('source_section'):
            fragment = source.split('\n## ' + entry['source_section'] + '\n', 1)[1].split('\n## ', 1)[0]
            source = '# ' + entry['model_name'] + '\n' + fragment
        text = (ROOT / entry['destination'].split('#')[0]).read_text()
        prefix = entry['marker']
        body = text.split('<!-- ' + prefix + ' source begins -->\n', 1)[1].split('<!-- ' + prefix + ' source ends -->', 1)[0]
        for old, new in entry.get('link_normalizations', {}).items():
            body = body.replace(new, old)
        for path, expected in entry.get('supporting_source_hashes', {}).items():
            assert digest((ROOT / path).read_text()) == expected, path
        for paragraph in entry.get('retained_context', []):
            assert paragraph in text, 'Lost historical context'
        for url in entry.get('retained_source_urls', []):
            assert url in text, 'Lost historical URL'
        for ref in entry['renamed_references']:
            body = body.replace('[' + prefix + '-' + ref + ']', '[' + ref + ']')
        body = re.sub(r'^### ', '## ', body, flags=re.M)
        assert body == source.split('\n', 1)[1], 'Lost original body: ' + entry['source']
        model = entry.get('model_name', entry['models'][0].removeprefix('Zoom '))
        section = text.split('\n## ' + model + '\n', 1)[1].split('\n## ', 1)[0]
        for fact in entry['retained_comparison_facts']:
            assert fact['value'] in section, 'Lost supporting evidence: ' + fact['field']
    print('PASS: complete consolidated bodies and supporting comparison facts retained.')


def plan(model_id):
    research_tools.identity()
    model, source_path = MODELS[model_id]
    brand = 'MOOER' if model_id in ('ge100-original','ge150-original','ge200-original','ge150-pro-li','ge100-pro','ge100-pro-li','ge200-pro','ge200-pro-li','ge150-pro') else 'Hotone' if model_id in ('ampero-mini','ampero-mp100','ampero-mp350','ampero-mp380','ampero-mp300') else 'Line 6' if model_id == 'hx-stomp-xl' else 'Zoom'
    brand_file = {'MOOER':'MOOER.md','Hotone':'HOTONE.md','Line 6':'LINE6.md','Zoom':'ZOOM.md'}[brand]
    state = json.loads((ROOT / 'research-state.json').read_text())
    assert model not in state['root_brand_content'][brand_file], 'Already consolidated'
    comparison = json.loads(Path('/tmp/instrumentfx-comparison-plan.json').read_text())
    assert comparison['ledger_hash'] == digest((ROOT / 'research-state.json').read_text()), 'Run make comparison-plan first'
    record = comparison['records'][brand + '::' + model]
    assert record['link'] == source_path
    source = (ROOT / source_path).read_text()
    prefix = brand_file.removesuffix('.md') + '-' + model_id.upper()
    body, refs = preserved_body(source, prefix)
    link_normalizations = {}
    if model_id in ('ampero-mp100','ampero-mp350'):
        link_normalizations = {'(../SCOPE.md)':'(effects/SCOPE.md)', '(../RESUME.md)':'(effects/RESUME.md)'}
        for old, new in link_normalizations.items():
            body = body.replace(old, new)
    if model_id == 'ge100-pro-li':
        link_normalizations = {'(2026-10-14-mooer-ge100-pro.md)':'(MOOER.md#ge100-pro)'}
        for old, new in link_normalizations.items():
            body = body.replace(old, new)
    if model_id == 'ge200-pro-li':
        link_normalizations = {'(2026-10-14-mooer-ge200-pro.md)':'(MOOER.md#ge200-pro)'}
        for old, new in link_normalizations.items():
            body = body.replace(old, new)
    extra = [f for f in record['facts'] if f['source'] != source_path]
    shared = sorted({f['source'] for f in extra})
    zoom = (ROOT / brand_file).read_text()
    if model_id == 'ampero-mini':
        zoom = zoom.replace('The five already-researched Hotone models still require complete consolidation', 'Four other already-researched Hotone models still require complete consolidation')
        zoom = zoom.replace('Already-researched Ampero Mini MP-50,Ampero MP-100,', 'Already-researched Ampero MP-100,')
    if model_id == 'ampero-mp100':
        zoom = zoom.replace('Four other already-researched Hotone models', 'Three other already-researched Hotone models')
        zoom = zoom.replace('Already-researched Ampero MP-100,Ampero II Stomp', 'Already-researched Ampero II Stomp')
    if model_id == 'ampero-mp350':
        zoom = zoom.replace('Three other already-researched Hotone models', 'Two other already-researched Hotone models')
        zoom = zoom.replace('Ampero II Stomp MP-300,Ampero II MP-350 and Ampero II Stage MP-380 remain', 'Ampero II Stomp MP-300 and Ampero II Stage MP-380 remain')
    if model_id == 'ampero-mp380':
        zoom = zoom.replace('Two other already-researched Hotone models still require', 'One other already-researched Hotone model still requires')
        zoom = zoom.replace('Already-researched Ampero II Stomp MP-300 and Ampero II Stage MP-380 remain', 'Already-researched Ampero II Stomp MP-300 remains')
    if model_id == 'ampero-mp300':
        zoom = zoom.replace('One other already-researched Hotone model still requires complete consolidation from their legacy records; they must not be counted again or discarded.', 'All six recorded Hotone models are consolidated below; technical verification remains partial.')
        zoom = zoom.replace('## Existing Hotone records awaiting complete consolidation', '## Hotone consolidation scope')
        zoom = zoom.replace('Already-researched Ampero II Stomp MP-300 remains in their legacy source records. They are not new models. Merge their complete details,sources,price qualifications and firmware conflicts here before retiring the originals. The root brand migration is not finished merely because this MP-80 entry exists.', 'The six recorded Hotone models now retain their complete model findings and supporting comparison facts here. Original legacy sources remain available. Consolidation does not establish exhaustive market coverage or close unresolved specification and price fields.')
    if model_id == 'ge100-original':
        zoom = zoom.replace('The fifteen previously researched GE models remain in their legacy source files until their full evidence has been consolidated here.', 'Fourteen previously researched GE models still require complete consolidation; GE100 original is consolidated below.')
    if model_id == 'ge150-original':
        zoom = zoom.replace('Fourteen previously researched GE models still require complete consolidation; GE100 original is consolidated below.', 'Thirteen previously researched GE models still require complete consolidation; GE100 original and GE150 original are consolidated below.')
    if model_id == 'ge200-original':
        zoom = zoom.replace('Thirteen previously researched GE models still require complete consolidation; GE100 original and GE150 original are consolidated below.', 'Twelve previously researched GE models still require complete consolidation; original GE100,GE150 and GE200 are consolidated below.')
    if model_id == 'ge150-pro-li':
        zoom = zoom.replace('Twelve previously researched GE models still require complete consolidation; original GE100,GE150 and GE200 are consolidated below.', 'Eleven previously researched GE models still require complete consolidation; original GE100,GE150,GE200 and GE150 Pro Li are consolidated below.')
    if model_id == 'ge100-pro':
        zoom = zoom.replace('Eleven previously researched GE models still require complete consolidation; original GE100,GE150,GE200 and GE150 Pro Li are consolidated below.', 'Ten previously researched GE models still require complete consolidation; original GE100,GE150,GE200,GE150 Pro Li and GE100 Pro are consolidated below.')
    if model_id == 'ge100-pro-li':
        zoom = zoom.replace('Ten previously researched GE models still require complete consolidation; original GE100,GE150,GE200,GE150 Pro Li and GE100 Pro are consolidated below.', 'Nine previously researched GE models still require complete consolidation; original GE100,GE150,GE200,GE150 Pro Li,GE100 Pro and GE100 Pro Li are consolidated below.')
    if model_id == 'ge200-pro':
        zoom = zoom.replace('Nine previously researched GE models still require complete consolidation; original GE100,GE150,GE200,GE150 Pro Li,GE100 Pro and GE100 Pro Li are consolidated below.', 'Eight previously researched GE models still require complete consolidation; the original GE models and consolidated Pro variants are below.')
    if model_id == 'ge200-pro-li':
        zoom = zoom.replace('Eight previously researched GE models still require complete consolidation; the original GE models and consolidated Pro variants are below.', 'Seven previously researched GE models still require complete consolidation; the original GE models and consolidated Pro variants are below.')
    if model_id == 'ge150-pro':
        zoom = zoom.replace('Seven previously researched GE models still require complete consolidation; the original GE models and consolidated Pro variants are below.', 'Six previously researched GE models still require complete consolidation; the original GE models and consolidated Pro variants are below.')
    zoom = re.sub(r'^The existing .+$', lambda m: m[0].replace(model + ',', '').replace(',' + model + ' records', ' records'), zoom, flags=re.M)
    section = '\n## ' + model + '\n\n'
    section += 'Consolidated 2026-10-16. The complete original observation below retains its technical date, prices, sources, contradictions and unknowns. This is a document consolidation, not a fresh stock or firmware verification. Historical next-model notes are provenance; use research-state.json for current work.\n\n'
    section += '<!-- ' + prefix + ' source begins -->\n' + body + '<!-- ' + prefix + ' source ends -->\n'
    if model_id == 'ge100-pro-li':
        section += '\n### GE100 Pro Li comparison dimensions\n\n| Field | Preserved qualification |\n|---|---|\n| Dimensions / weight | 255.7×144×53.5mm;856g. W/D labels and raised-pedal height unverified;medium/large bin awaits axis verification. |\n'
    if model_id == 'ge150-pro':
        section += '\n### GE150 Pro comparison category counts\n\n| Field | Preserved firmware qualification |\n|---|---|\n| Category choices | Firmware1.5.0:FX12,drive28,AMP55,CAB26,NS3,EQ4,MOD25,delay9,reverb8=170 including amps/cabs. Current NAM-enabled firmware not recounted;empty user slots are not algorithms. |\n'
    if model_id == 'ampero-mp380':
        section += '\n### Stage processing comparison fields\n\n| Field | Preserved source qualification |\n|---|---|\n| Category choices | 460+ published;68 cabs,100+ pedal models,60+ originals;87 versus90+ amp conflict. Current category subtotals unresolved. |\n| IR / NAM / captures | 50 user IR slots,24-bit/44.1kHz mono WAV,1024/2048 samples;20 Celestion IRs separate. Native NAM A2 Lite firmware1.7.0+,not A2 Full;earlier Sound Clone conversion and Tone Catch are separate. |\n| Synth / acoustic | Acoustic effects/presets advertised;exact electric-to-acoustic and synth algorithms unverified. |\n'
    section += '\n### ' + model + ' — supporting comparison provenance\n\n'
    section += 'The complete supporting comparison was read before merging. Its model-specific values are retained below, including historical shorthand. These do not override fuller qualifications above. Original files and incoming links remain available.\n\n'
    for fact in extra:
        section += '- **' + fact['field'] + '** (' + fact['context'] + '): ' + fact['value'] + '\n'
    section += '\nSources: ' + ', '.join('[' + p + '](' + p + ')' for p in [source_path] + shared) + '. No legacy file was deleted.\n'
    state['root_brand_content'][brand_file].append(model)
    old_count = state['canonical_root_model_count']
    old_legacy = state['legacy_only_model_count']
    state['canonical_root_model_count'] += 1
    state['legacy_only_model_count'] -= 1
    entry = dict(models=[brand + ' ' + model], model_name=model, brand=brand, destination=brand_file+'#' + comparison_views.slug(model), source=source_path,
                 checked_date='2026-10-16', verification_kind='complete-source-body-v1', marker=prefix,
                 source_sha256=digest(source), renamed_references=refs, retained_comparison_facts=extra,
                 link_normalizations=link_normalizations, supporting_sources=shared, status='Consolidated; technical verification remains partial')
    state['consolidation_and_price_findings'].append(entry)
    state['migration']['warning'] = f"{old_legacy-1} legacy-only models remain;{old_count+1} root-canonical. Full migration and research incomplete."
    state['cursor']['task'] = 'Continue fresh Shopee discovery by brand/series, lossless legacy consolidation and unresolved-field research; use current counts.'
    state['cursor']['after_queue'] = f'Continue unresolved-field checks and lossless consolidation of {old_legacy-1} legacy-only models.'
    readme = (ROOT / 'README.md').read_text().replace(f'{old_count} detailed', f'{old_count+1} detailed').replace(f'{old_legacy} still rely', f'{old_legacy-1} still rely')
    readme = re.sub(r'(\| \['+re.escape(brand_file)+r'\]\('+re.escape(brand_file)+r'\) \|)([^\n]+) \|', lambda m: m[1]+m[2]+','+model+' |', readme)
    multi = (ROOT / 'MULTI-EFFECTS.md').read_text().replace(f'{old_count} root-canonical', f'{old_count+1} root-canonical')
    outputs = {brand_file: zoom + section, 'README.md': readme, 'MULTI-EFFECTS.md': multi,
               'research-state.json': json.dumps(state, ensure_ascii=False, indent=2) + '\n'}
    inputs = {p: digest((ROOT / p).read_text()) for p in list(outputs) + [source_path] + shared}
    payload = dict(model_id=model_id, model=model, inputs=inputs, outputs=outputs,
                   rollback_commit=research_tools.git('rev-parse', 'HEAD').strip())
    PLAN.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
    print('Preview: ' + model + '; rollback is existing Git HEAD ' + payload['rollback_commit'])
    print('Exact writes: ' + ', '.join(outputs))
    print('Read source: ' + source_path + '; supporting sources: ' + ', '.join(shared))
    print(f'Counts: {old_count}->{old_count+1} canonical; {old_legacy}->{old_legacy-1} legacy; active count unchanged')
    print('Plan saved: ' + str(PLAN))


def apply(model_id):
    research_tools.identity()
    payload = json.loads(PLAN.read_text())
    assert payload['model_id'] == model_id
    for p, sha in payload['inputs'].items():
        assert digest((ROOT / p).read_text()) == sha, 'Concurrent change: ' + p
    for p, text in payload['outputs'].items():
        (ROOT / p).write_text(text)
    verify_preserved(json.loads((ROOT / 'research-state.json').read_text()))
    print('Applied only the reviewed exact outputs; legacy sources untouched.')


def commit(model_id):
    research_tools.identity()
    state = json.loads((ROOT / 'research-state.json').read_text())
    verify_preserved(state)
    research_tools.verify()
    comparison_views.verify_views()
    assert not research_tools.git('diff', '--cached', '--name-only').strip(), 'Existing staged work must be inspected'
    paths = ['MOOER.md', 'HOTONE.md', 'LINE6.md', 'BOSS.md', 'ZOOM.md', 'README.md', 'MULTI-EFFECTS.md', 'research-state.json', 'ALL-GUITAR.md', 'ALL-BASS.md', 'ALL-VOCAL.md', 'Makefile', 'scripts/consolidation_tools.py', 'scripts/comparison_views.py', 'scripts/research_tools.py']
    print(research_tools.git('status', '--short'))
    print(research_tools.git('add', '--', *paths))
    print(research_tools.git('diff', '--cached', '--stat'))
    print(research_tools.git('commit', '-m', 'docs(' + ('mooer' if model_id in ('ge100-original','ge150-original','ge200-original','ge150-pro-li','ge100-pro','ge100-pro-li','ge200-pro','ge200-pro-li','ge150-pro') else 'hotone' if model_id in ('ampero-mini','ampero-mp100','ampero-mp350','ampero-mp380','ampero-mp300') else 'line6' if model_id == 'hx-stomp-xl' else 'boss' if model_id in ('gt-1b', 'gx-1b', 'me-90b', 've-1', 've-2', 've-500', 've-22', 've-8', 've-20', 'gt-1000core', 'gx-10', 'gt-1', 'gx-1', 'me-90', 'gx-100', 'gt-1000', 'gm-800') else 'zoom') + '): consolidate complete ' + MODELS[model_id][0] + ' evidence'))


if __name__ == '__main__':
    if sys.argv[1:] == ['cache-plan']:
        research_tools.identity()
        files = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'scripts/__pycache__').glob('*.pyc') if p.name.startswith(('comparison_views.', 'research_tools.'))}
        Path('/tmp/instrumentfx-bytecode-cleanup.json').write_text(json.dumps(files, indent=2))
        print('Generated bytecode only; reproducible by Python import. Exact deletion preview:')
        print(json.dumps(files, indent=2))
        raise SystemExit(0)
    if sys.argv[1:] == ['cache-apply']:
        research_tools.identity()
        files = json.loads(Path('/tmp/instrumentfx-bytecode-cleanup.json').read_text())
        for p, sha in files.items():
            path = Path(p)
            assert path.parent == ROOT/'scripts/__pycache__' and path.suffix == '.pyc' and not path.is_symlink()
            assert hashlib.sha256(path.read_bytes()).hexdigest() == sha
        for p in files:
            Path(p).unlink()
            print('Removed reviewed generated file: ' + p)
        raise SystemExit(0)
    if sys.argv[1:] == ['verify']:
        research_tools.identity()
        verify_preserved(json.loads((ROOT / 'research-state.json').read_text()))
        raise SystemExit(0)
    mode, model_id = sys.argv[1:]
    assert model_id in MODELS
    {'plan': plan, 'apply': apply, 'commit': commit}[mode](model_id)
