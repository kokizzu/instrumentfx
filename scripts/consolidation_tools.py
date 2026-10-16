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
    'gp-180': ('GP-180', 'effects/findings/2026-10-14-valeton-gp-180.md'),
    'gp-200': ('GP-200', 'effects/guitar-floorboards.md'),
    'gp-150': ('GP-150', 'effects/findings/2026-10-14-valeton-gp-150.md'),
    'gp-100': ('GP-100', 'effects/findings/2026-10-14-valeton-gp-100.md'),
    'ge1000-li': ('GE1000 Li', 'effects/findings/2026-10-15-mooer-ge1000-li.md'),
    'ge1000': ('GE1000', 'effects/findings/2026-10-14-mooer-ge1000.md'),
    'ge150-max-li': ('GE150 Max Li', 'effects/findings/2026-10-15-mooer-ge150-max-li.md'),
    'ge150-max': ('GE150 Max', 'effects/findings/2026-10-15-mooer-ge150-max.md'),
    'ge150-plus-li': ('GE150 Plus Li', 'effects/findings/2026-10-15-mooer-ge150-plus-li.md'),
    'ge150-plus': ('GE150 Plus', 'effects/findings/2026-10-15-mooer-ge150-plus.md'),
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



def plan_gp200():
    research_tools.identity()
    model, source_path = MODELS['gp-200']
    brand_file = 'VALETON.md'
    state_text = (ROOT/'research-state.json').read_text()
    state = json.loads(state_text)
    assert model not in state['root_brand_content'][brand_file]
    comparison = json.loads(Path('/tmp/instrumentfx-comparison-plan.json').read_text())
    assert comparison['ledger_hash'] == digest(state_text), 'Run make comparison-plan first'
    record = comparison['records']['Valeton::GP-200']
    assert record['link'] == source_path
    source = (ROOT/source_path).read_text()
    facts = record['facts']
    assert all(f['source'] == source_path for f in facts)
    contexts = [p for p in source.split('\n\n') if p.startswith('Checked **2026-10-14**') or p.startswith('All three have built-in expression') or p.startswith('New prices are individual') ] + [line for line in source.splitlines() if line.startswith("- GP-200's published")]
    assert len(contexts) == 4
    urls = ['https://www.valeton.net/product/gp-200/']
    section = '\n## GP-200\n\nConsolidated 2026-10-17. Historical observations below retain their 2026-10-14 date. GP-200X is retained as an anniversary variant of this existing model, not another active count. Technical verification remains partial.\n\n### Complete legacy GP-200 evidence\n\n'
    section += '\n\n'.join(contexts) + '\n\n'
    for fact in facts:
        section += '- **' + fact['field'] + '** (' + fact['context'] + '): ' + fact['value'] + '\n'
    section += '\nOriginal primary source: ' + urls[0] + '\nLegacy source: [guitar-floorboards](effects/guitar-floorboards.md). No source file or incoming link was removed.\n\n### GP-200 comparison fields\n\n| Field | Evidence / qualification |\n|---|---|\n'
    for fact in facts:
        value = fact['value']
        if fact['field'] == 'NAM':
            value = '**NAM A2 conversion**, desktop software **1.8.1+**, explicitly names GP-200, GP-200X and GP-200R in the official regional notice dated 2026-08-18. Native unrestricted NAM, architecture limits and simultaneous import capacity remain unverified. [GP200-N](https://www.hotone.jp/announcements/nama2allbrand). Supersedes the historical unestablished NAM field above.'
        section += '| ' + fact['field'] + ' | ' + value + ' |\n'
    section += '''| Expression | Built-in optical expression; external TRS EXP/FS socket. Toe-switch behavior remains unverified. [GP200-P](https://en.valeton.net/product/gp-200/) |
| Display | Published 4.3-inch 480×272 TFT LCD; color/touch not independently established in this pass. No diagonal estimated from a photograph. [GP200-P](https://en.valeton.net/product/gp-200/) |
| New / retail IDR — GP-200X anniversary variant only | **Rp6.486.800 with voucher**, Gallery Music Bekasi, seller760002726/item48805823582, Kota Bekasi; indexed reopen checked2026-10-17. Search snapshot instead showed **Rp6.620.000 with voucher** for this same item. Both are conditional cached observations, not a verified standard GP-200 price or live stock. Condition, bundle, warranty region, shipping/tax and checkout voucher eligibility unconfirmed. [GP200-S](https://shopee.co.id/Valeton-GP-200X-Multi-Effects-Processor-GP200X-GP-200-X-GP-200X-GP200-X-i.760002726.48805823582) |

### GP-200X anniversary variant and offer limitations

[Valeton's own GP-200X page](https://www.valeton.net/product/gp-200x/) explicitly states shared features/functions with GP-200. It documents navy/red finishing, anniversary firmware, **28 artist presets from12 artists** and a gift box with pick and copper/leather pick-holder keychain. GP-200/GP-200R can receive the firmware and artist presets too. Do not add28 to the256-location capacity or assume seller bundles contain every advertised gift. The variant has its own physical finish and packaging; its offers must remain labelled GP-200X.

A second [Sunny Music Palembang offer](https://shopee.co.id/Valeton-GP-200X-Multi-Effect-Processor-GP-200-X-GP-200X-i.548551522.27173361420), seller548551522/item27173361420, was indexed at **Rp6.350.000, Habis**, with stale9–12July delivery text. Direct reopening returned a cache miss. This is a historical sold-out anniversary-variant ask, not used-price evidence, a live-stock offer or a standard GP-200 quote. Checked2026-10-17; condition, bundle, warranty region and delivered charges remain unknown. No voucher arithmetic or currency conversion was applied.

The Gallery item's search snapshot had stale4–5October delivery; reopening supplied a different conditional amount and relative delivery text. This disagreement is retained, not resolved by guessing a discount. Neither amount is checkout-confirmed. No dependable used IDR offer was established for GP-200 or its anniversary variant.

### Outstanding GP-200 checks

Separate rotary/button counts and toe operation; complete current category choices and synth/simulator algorithms; factory-memory overwrite rules; IR formats/conversion; NAM architectures/concurrency; explicit screen color/touch; battery/USB operation; driver/updater versions, scenes/routing and qualified standard-model used/new Shopee evidence remain unresolved. Do not import sibling GP-200JR/LT manual specifications without model-specific evidence.
'''
    brand = (ROOT/brand_file).read_text().replace('Existing GP-5/50/180/200 records remain','Existing GP-5/50/180 records remain')
    old_count, old_legacy = state['canonical_root_model_count'], state['legacy_only_model_count']
    state['root_brand_content'][brand_file].append(model)
    state['canonical_root_model_count'] += 1
    state['legacy_only_model_count'] -= 1
    entry = dict(models=['Valeton GP-200'],model_name=model,brand='Valeton',destination='VALETON.md#gp-200',source=source_path,checked_date='2026-10-17',verification_kind='complete-model-rows-v1',source_sha256=digest(source),retained_comparison_facts=facts,retained_context=contexts,retained_source_urls=urls,status='Consolidated; new GP-200X offer and NAM-conversion evidence; partial')
    state['consolidation_and_price_findings'].append(entry)
    state['discovery_leads'].append(dict(model='Valeton GP-200X',checked_date='2026-10-17',status='Anniversary variant retained under GP-200; no additional model count',url='https://shopee.co.id/Valeton-GP-200X-Multi-Effects-Processor-GP200X-GP-200-X-GP-200X-GP200-X-i.760002726.48805823582',seller='Gallery Music Bekasi',seller_id='760002726',item_id='48805823582',indexed_idr=6620000,reopened_indexed_idr=6486800,qualification='Both with-voucher cached snapshots; discrepant values retained. Condition/bundle/region/checkout stock unconfirmed. Other sold-out exact item548551522/27173361420 indexed6350000; reopen cache miss.'))
    state['discovery_search_pass_20261017'] = dict(queries=['site:shopee.co.id MOOER GS1000 Li','site:shopee.co.id Valeton GP-200X'],result='No exact GS1000 Li hardware lead returned. GP-200X exact hardware offers found; official shared-feature statement supports variant within existing GP-200 record. Counts unchanged; absence of another exact lead is not market coverage.')
    state['migration']['warning'] = f'{old_legacy-1} legacy-only models remain;{old_count+1} root-canonical. Full migration and research incomplete.'
    state['cursor'].update(model='Valeton GP-150 — firmware-qualified NAM correction',task='Fresh official regional notice explicitly documents GP-150/180 native NAM A2 Lite at firmware1.1.1+. Review GP-150 first, preserve older SnapTone-only evidence and its date, update comparison fields and commit before GP-180. Notice also warrants separate GP-100 conversion review. Then resume fresh Shopee discovery and lossless consolidation.',after_queue=f'Continue unresolved-field checks and lossless consolidation of {old_legacy-1} legacy-only models.')
    readme=(ROOT/'README.md').read_text().replace(f'{old_count} detailed',f'{old_count+1} detailed').replace(f'{old_legacy} still rely',f'{old_legacy-1} still rely').replace('GP-200LT,GP-200JR,GP-100,GP-150 |','GP-200LT,GP-200JR,GP-100,GP-150,GP-200 (GP-200X variant) |')
    multi=(ROOT/'MULTI-EFFECTS.md').read_text().replace(f'{old_count} root-canonical',f'{old_count+1} root-canonical')
    outputs={brand_file:brand+section,'README.md':readme,'MULTI-EFFECTS.md':multi,'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n'}
    payload=dict(model_id='gp-200',model=model,inputs={p:digest((ROOT/p).read_text()) for p in list(outputs)+[source_path]},outputs=outputs,rollback_commit=research_tools.git('rev-parse','HEAD').strip())
    PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print('Preview GP-200: writes '+', '.join(outputs)+f'; canonical {old_count}->{old_count+1}; legacy {old_legacy}->{old_legacy-1}; active unchanged. No deletion. Rollback '+payload['rollback_commit'])
    print('Plan saved: '+str(PLAN))


def plan(model_id):
    if model_id == 'gp-200':
        return plan_gp200()
    research_tools.identity()
    model, source_path = MODELS[model_id]
    brand = 'Valeton' if model_id in ('gp-100', 'gp-150', 'gp-180', 'gp-200') else 'MOOER' if model_id in ('ge100-original','ge150-original','ge200-original','ge150-pro-li','ge100-pro','ge100-pro-li','ge200-pro','ge200-pro-li','ge150-pro','ge150-plus','ge150-plus-li','ge150-max','ge150-max-li','ge1000','ge1000-li') else 'Hotone' if model_id in ('ampero-mini','ampero-mp100','ampero-mp350','ampero-mp380','ampero-mp300') else 'Line 6' if model_id == 'hx-stomp-xl' else 'Zoom'
    brand_file = {'Valeton':'VALETON.md','MOOER':'MOOER.md','Hotone':'HOTONE.md','Line 6':'LINE6.md','Zoom':'ZOOM.md'}[brand]
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
    if model_id == 'ge1000-li':
        link_normalizations = {'(2026-10-14-mooer-ge1000.md)':'(MOOER.md#ge1000)'}
        for old, new in link_normalizations.items():
            body = body.replace(old, new)
    if model_id in ('gp-100', 'gp-150', 'gp-180', 'gp-200'):
        link_normalizations = {'(../guitar-compact.md)':'(effects/guitar-compact.md)', '(../RESUME.md)':'(effects/RESUME.md)'}
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
    if model_id == 'ge150-plus':
        zoom = zoom.replace('Six previously researched GE models still require complete consolidation; the original GE models and consolidated Pro variants are below.', 'Five previously researched GE models still require complete consolidation; the original GE models and consolidated Plus/Pro variants are below.')
    if model_id == 'ge150-plus-li':
        zoom = zoom.replace('Five previously researched GE models still require complete consolidation; the original GE models and consolidated Plus/Pro variants are below.', 'Four previously researched GE models still require complete consolidation; the original GE models and consolidated Plus/Pro variants are below.')
    if model_id == 'ge150-max':
        zoom = zoom.replace('Four previously researched GE models still require complete consolidation; the original GE models and consolidated Plus/Pro variants are below.', 'Three previously researched GE models still require complete consolidation; the original GE models and consolidated Max/Plus/Pro variants are below.')
    if model_id == 'ge150-max-li':
        zoom = zoom.replace('Three previously researched GE models still require complete consolidation; the original GE models and consolidated Max/Plus/Pro variants are below.', 'Two previously researched GE models still require complete consolidation; the original GE models and consolidated Max/Plus/Pro variants are below.')
    if model_id == 'ge1000':
        zoom = zoom.replace('Two previously researched GE models still require complete consolidation; the original GE models and consolidated Max/Plus/Pro variants are below.', 'GE1000 Li is the remaining previously researched GE model awaiting complete consolidation; other recorded MOOER models are consolidated below.')
    if model_id == 'ge1000-li':
        zoom = zoom.replace('GE1000 Li is the remaining previously researched GE model awaiting complete consolidation; other recorded MOOER models are consolidated below.', 'All eighteen recorded MOOER models have root records below; technical verification and market discovery remain incomplete. Original legacy sources are retained.')
    if model_id in ('gp-100', 'gp-150', 'gp-180', 'gp-200'):
        zoom = zoom.replace('Existing GP-5/50/100/150/180/200 records remain', 'Existing GP-5/50/150/180/200 records remain')
        if model_id == 'gp-180':
            zoom = zoom.replace('Existing GP-5/50/180 records remain', 'Existing GP-5/50 records remain')
        if model_id == 'gp-150':
            zoom = zoom.replace('Existing GP-5/50/150/180/200 records remain', 'Existing GP-5/50/180/200 records remain')
    zoom = re.sub(r'^The existing .+$', lambda m: m[0].replace(model + ',', '').replace(',' + model + ' records', ' records'), zoom, flags=re.M)
    section = '\n## ' + model + '\n\n'
    section += 'Consolidated 2026-10-17. The complete original observation below retains its technical date, prices, sources, contradictions and unknowns. This is a document consolidation, not a fresh stock or firmware verification. Historical next-model notes are provenance; use research-state.json for current work.\n\n'
    if model_id == 'gp-180':
        section = section.replace('This is a document consolidation, not a fresh stock or firmware verification.', 'NAM compatibility, published power requirements and qualified Shopee snapshots were additionally checked2026-10-17; checkout stock and complete firmware contents remain unverified.')
    section += '<!-- ' + prefix + ' source begins -->\n' + body + '<!-- ' + prefix + ' source ends -->\n'
    if model_id == 'ge100-pro-li':
        section += '\n### GE100 Pro Li comparison dimensions\n\n| Field | Preserved qualification |\n|---|---|\n| Dimensions / weight | 255.7×144×53.5mm;856g. W/D labels and raised-pedal height unverified;medium/large bin awaits axis verification. |\n'
    if model_id == 'ge150-pro':
        section += '\n### GE150 Pro comparison category counts\n\n| Field | Preserved firmware qualification |\n|---|---|\n| Category choices | Firmware1.5.0:FX12,drive28,AMP55,CAB26,NS3,EQ4,MOD25,delay9,reverb8=170 including amps/cabs. Current NAM-enabled firmware not recounted;empty user slots are not algorithms. |\n'
    if model_id == 'ge1000':
        section += '\n### GE1000 comparison category counts\n\n| Field | Preserved manual qualification |\n|---|---|\n| Category choices | Manual2.5:dynamic13,filter13,drive35,power-amp11,EQ9,FX-loop3,MOD30,delay16,reverb11;cabs25 classic+54 boutique+10 bass;28 boutique preamps,26 complete boutique amps,10 bass preamps;classic amp subtotal incomplete. Manual340+ versus regional280+ retained;not a current native-NAM inventory. |\n'
    if model_id == 'ampero-mp380':
        section += '\n### Stage processing comparison fields\n\n| Field | Preserved source qualification |\n|---|---|\n| Category choices | 460+ published;68 cabs,100+ pedal models,60+ originals;87 versus90+ amp conflict. Current category subtotals unresolved. |\n| IR / NAM / captures | 50 user IR slots,24-bit/44.1kHz mono WAV,1024/2048 samples;20 Celestion IRs separate. Native NAM A2 Lite firmware1.7.0+,not A2 Full;earlier Sound Clone conversion and Tone Catch are separate. |\n| Synth / acoustic | Acoustic effects/presets advertised;exact electric-to-acoustic and synth algorithms unverified. |\n'
    section += '\n### ' + model + ' — supporting comparison provenance\n\n'
    section += 'The complete supporting comparison was read before merging. Its model-specific values are retained below, including historical shorthand. These do not override fuller qualifications above. Original files and incoming links remain available.\n\n'
    for fact in extra:
        section += '- **' + fact['field'] + '** (' + fact['context'] + '): ' + fact['value'] + '\n'
    if model_id in ('gp-100', 'gp-150', 'gp-180', 'gp-200'):
        section += '\n### ' + model + (' comparison fields — dated evidence' if model_id == 'gp-180' else ' comparison fields from retained snapshot') + '\n\n| Field | Dated evidence |\n|---|---|\n'
        for fact in extra:
            if 'Archived foreign' not in fact['context']:
                value = fact['value'].replace('[F100]', '[detail](VALETON.md#gp-100)').replace('[F150]', '[detail](VALETON.md#gp-150)').replace('[F180]', '[detail](VALETON.md#gp-180)').replace('[controls]', '[controls](https://res.valeton.net/Uploads/wp/2026/03/GP-150-GP180-Comparison-2.png)')
                if model_id == 'gp-180' and fact['field'] == 'NAM / captured models':
                    value = '**Native NAM A2 Lite at firmware1.1.1+**, per [official regional notice,2026-08-18](https://www.hotone.jp/announcements/nama2allbrand), rechecked2026-10-17. The product page still describes SnapTone conversion with100 slots/50 supplied; preserve this earlier workflow separately. Native A2 Full, other architectures and native capacity/concurrency remain unverified; conversion-slot counts do not establish native capacity.'
                if model_id == 'gp-180' and fact['field'] == 'Power and battery':
                    value = '3000mAh/3.7V battery; DC9V center-negative,5.5×2.1mm. Official page lists DC≥1.5A, minimum operating1A, charging2A; retain these distinct figures without assuming one adapter rating resolves them. USB-C5V≥1A, minimum operating1A, PD fast-charge3A. DC/USB operation and charging advertised. Over6h battery claim at screen brightnessII is manufacturer-rated, not measured. [GP180-P](https://www.valeton.net/product/gp-180/)'
                section += '| ' + fact['field'] + ' | ' + value + ' |' + '\n'
        shared_text = (ROOT / shared[0]).read_text()
        contexts = [p for p in shared_text.split('\n\n') if p.startswith('*GP-100 height') or p.startswith('GP-100\'s checked firmware') or p.startswith('These earlier observations were recorded') or p.startswith('P2 separately listed')]
        urls = ['https://www.guitarcenter.com/Valeton/Used-Valeton-GP-100-Effect-Processor-122531515.gc','https://www.thomannmusic.com/valeton_gp_100.htm','https://nafiriguitar.com/products/valeton-gp-100-multi-effects-processor']
        if model_id == 'gp-150':
            contexts = [p for p in shared_text.split('\n\n') if p.startswith('*GP-100 height') or p.startswith('GP-150/180 documentation') or p.startswith('These earlier observations were recorded') or p.startswith('Prices are individual asking/listed observations')]
            urls = ['https://shop.valeton.net/products/gp-150','https://res.valeton.net/Uploads/wp/2026/03/GP-150-GP180-Comparison-2.png']
        if model_id == 'gp-180':
            contexts = [p for p in shared_text.split('\n\n') if p.startswith('GP-150/180 documentation') or p.startswith('These earlier observations were recorded') or p.startswith('Prices are individual asking/listed observations')]
            urls = ['https://shop.valeton.net/products/gp-180','https://res.valeton.net/Uploads/wp/2026/03/GP-150-GP180-Comparison-2.png']
            section += '''| New / retail Shopee IDR observations | Checked2026-10-17: [Bandung Music Gallery](https://shopee.co.id/Valeton-GP180-Multi-Effects-Processor-GP-180-i.394955725.48113176759), seller394955725/item48113176759, Kota Bandung, indexed **Rp3.619.140**, comparison Rp3.693.000, displayed2% reduction; stale August delivery. [Artech Music](https://shopee.co.id/Valeton-GP180-Multi-Effects-Processor-GP-180-i.31171541.51763144425), seller31171541/item51763144425, Kota Bekasi: search showed **Rp3.693.000,Habis**; reopening instead showed Rp3.619.140/comparison Rp3.693.000 without that label. Preserve discrepancy; neither is checkout-confirmed stock. Condition, bundle, warranty region, tax/shipping and voucher eligibility unconfirmed. No dependable used quote established. |
'''
        section += '\n'+'\n\n'.join(contexts)+'\n\nHistorical ' + model + ' source URLs: '+', '.join(urls)+'\n'
    section += '\nSources: ' + ', '.join('[' + p + '](' + p + ')' for p in [source_path] + shared) + '. No legacy file was deleted.\n'
    state['root_brand_content'][brand_file].append(model)
    old_count = state['canonical_root_model_count']
    old_legacy = state['legacy_only_model_count']
    state['canonical_root_model_count'] += 1
    state['legacy_only_model_count'] -= 1
    entry = dict(models=[brand + ' ' + model], model_name=model, brand=brand, destination=brand_file+'#' + comparison_views.slug(model), source=source_path,
                 checked_date='2026-10-17', verification_kind='complete-source-body-v1', marker=prefix,
                 source_sha256=digest(source), renamed_references=refs, retained_comparison_facts=extra,
                 link_normalizations=link_normalizations, supporting_sources=shared, status='Consolidated; technical verification remains partial')
    if model_id in ('gp-100', 'gp-150', 'gp-180', 'gp-200'):
        entry.update(retained_context=contexts,retained_source_urls=urls,supporting_source_hashes={p:digest((ROOT/p).read_text()) for p in shared})
    state['consolidation_and_price_findings'].append(entry)
    state['migration']['warning'] = f"{old_legacy-1} legacy-only models remain;{old_count+1} root-canonical. Full migration and research incomplete."
    state['cursor']['task'] = 'Continue fresh Shopee discovery by brand/series, lossless legacy consolidation and unresolved-field research; use current counts.'
    state['cursor']['after_queue'] = f'Continue unresolved-field checks and lossless consolidation of {old_legacy-1} legacy-only models.'
    if model_id == 'gp-180':
        entry.update(new_sources=['https://www.hotone.jp/announcements/nama2allbrand','https://www.valeton.net/product/gp-180/'],scope='Complete historical body and supporting comparison fields preserved; native NAM A2 Lite firmware1.1.1+, model-specific power distinctions and two qualified Shopee offers checked2026-10-17.')
        state['cursor']['model'] = 'Valeton GP-100 — NAM A2 conversion review'
        state['cursor']['task'] = 'Review official regional GP-100 NAM A2 conversion requirement desktop1.5.1+; preserve earlier unestablished evidence, update root/comparisons and commit. Then consolidate GP-5/GP-50 and remaining legacy records; continue fresh Shopee discovery.'
        state['discovery_leads'].append(dict(model='Valeton GP-180',checked_date='2026-10-17',status='Existing model refreshed; no count addition',urls=['https://shopee.co.id/Valeton-GP180-Multi-Effects-Processor-GP-180-i.394955725.48113176759','https://shopee.co.id/Valeton-GP180-Multi-Effects-Processor-GP-180-i.31171541.51763144425'],qualification='Bandung Music Gallery indexed3619140/comparison3693000,2% label,stale August delivery. Artech search3693000 Habis versus reopened3619140 without sold-out label. Condition/bundle/region/checkout stock unknown.'))
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
    paths = ['VALETON.md', 'MOOER.md', 'HOTONE.md', 'LINE6.md', 'BOSS.md', 'ZOOM.md', 'README.md', 'MULTI-EFFECTS.md', 'research-state.json', 'ALL-GUITAR.md', 'ALL-BASS.md', 'ALL-VOCAL.md', 'Makefile', 'scripts/consolidation_tools.py', 'scripts/comparison_views.py', 'scripts/research_tools.py']
    print(research_tools.git('status', '--short'))
    print(research_tools.git('add', '--', *paths))
    print(research_tools.git('diff', '--cached', '--stat'))
    print(research_tools.git('commit', '-m', 'docs(' + ('valeton' if model_id in ('gp-100', 'gp-150', 'gp-180', 'gp-200') else 'mooer' if model_id in ('ge100-original','ge150-original','ge200-original','ge150-pro-li','ge100-pro','ge100-pro-li','ge200-pro','ge200-pro-li','ge150-pro','ge150-plus','ge150-plus-li','ge150-max','ge150-max-li','ge1000','ge1000-li') else 'hotone' if model_id in ('ampero-mini','ampero-mp100','ampero-mp350','ampero-mp380','ampero-mp300') else 'line6' if model_id == 'hx-stomp-xl' else 'boss' if model_id in ('gt-1b', 'gx-1b', 'me-90b', 've-1', 've-2', 've-500', 've-22', 've-8', 've-20', 'gt-1000core', 'gx-10', 'gt-1', 'gx-1', 'me-90', 'gx-100', 'gt-1000', 'gm-800') else 'zoom') + '): consolidate complete ' + MODELS[model_id][0] + ' evidence'))


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
