"""Reviewable, lossless model consolidation; keeps legacy sources and their links."""
import hashlib
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
from canonical_links import preservation_text
import comparison_views
import research_tools

ROOT = Path(__file__).resolve().parent.parent
PLAN = Path('/tmp/instrumentfx-consolidation-plan.json')
MODELS = {
    'gr-55': ('GR-55', 'effects/findings/2026-10-14-roland-gr-55.md'),
    'fb100': ('Flybro FB-100', 'effects/findings/2026-10-15-ving-fb100.md'),
    'h8': ('H8', 'effects/findings/2026-10-15-cuvave-h8.md'),
    'play-acoustic': ('Play Acoustic', 'effects/findings/2026-10-14-tchelicon-play-acoustic.md'),
    'voicelive-play': ('VoiceLive Play', 'effects/findings/2026-10-14-tchelicon-voicelive-play.md'),
    'kmf-10': ('KMF-10', 'effects/findings/2026-10-14-scorpion-kmf-10.md'),
    'bg300': ('BG300', 'effects/findings/2026-10-14-boin-audio-bg300.md'),
    'ave-100': ('AVE-100', 'effects/findings/2026-10-15-audota-ave-100.md'),
    'ace-100': ('ACE-100', 'effects/findings/2026-10-15-audota-ace-100.md'),
    'ame-200-pro': ('AME-200 Pro', 'effects/findings/2026-10-15-audota-ame-200-pro.md'),
    'ame-200': ('AME-200', 'effects/findings/2026-10-15-audota-ame-200.md'),
    'ame-100': ('AME-100', 'effects/findings/2026-10-15-audota-ame-100.md'),
    'nano-cortex': ('Nano Cortex', 'effects/advanced-modelers.md'),
    'tonex-pedal': ('TONEX Pedal', 'effects/advanced-modelers.md'),
    'tonex-one': ('TONEX ONE', 'effects/advanced-modelers.md'),
    'hx-stomp': ('HX Stomp', 'effects/advanced-modelers.md'),
    'gp-50': ('GP-50', 'effects/findings/2026-10-14-valeton-gp-50.md'),
    'gp-5': ('GP-5', 'effects/findings/2026-10-14-valeton-gp-5.md'),
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
            source = research_tools.read_preserved_source(entry['source'])
            assert digest(source) == entry['source_sha256'], entry['source']
            model = entry.get('model_name', entry['models'][0].removeprefix('Zoom '))
            text = preservation_text(entry['destination'].split('#')[0])
            section_model = entry.get('destination_section', model)
            section = text.split('\n## ' + section_model + '\n', 1)[1].split('\n## ', 1)[0]
            actual = []
            aliases = {comparison_views.norm(model), comparison_views.norm(entry.get('brand', 'Zoom')+' '+model)}
            aliases.update(comparison_views.norm(a) for a in entry.get('source_model_aliases', []))
            for headers, rows, context in comparison_views.tables(source):
                for row in rows:
                    exact = entry.get('source_exact_model_aliases')
                    label = re.sub(r'\[([^\]]+)\](?:\([^)]*\)|\[[^\]]*\])', r'\1', row[0]).strip()
                    if (label in exact) if exact else (comparison_views.norm(row[0]) in aliases):
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
        source = research_tools.read_preserved_source(entry['source'])
        assert digest(source) == entry['source_sha256'], entry['source']
        if entry.get('source_section'):
            fragment = source.split('\n## ' + entry['source_section'] + '\n', 1)[1].split('\n## ', 1)[0]
            source = '# ' + entry['model_name'] + '\n' + fragment
        text = preservation_text(entry['destination'].split('#')[0])
        prefix = entry['marker']
        body = text.split('<!-- ' + prefix + ' source begins -->\n', 1)[1].split('<!-- ' + prefix + ' source ends -->', 1)[0]
        for old, new in entry.get('link_normalizations', {}).items():
            body = body.replace(new, old)
        for path, expected in entry.get('supporting_source_hashes', {}).items():
            assert digest(research_tools.read_preserved_source(path)) == expected, path
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
    source = research_tools.read_preserved_source(source_path)
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



def plan_hx_stomp():
    research_tools.identity()
    model, source_path = MODELS['hx-stomp']
    state_text = (ROOT/'research-state.json').read_text()
    state = json.loads(state_text)
    assert model not in state['root_brand_content']['LINE6.md']
    comparison = json.loads(Path('/tmp/instrumentfx-comparison-plan.json').read_text())
    assert comparison['ledger_hash'] == digest(state_text), 'Run make comparison-plan first'
    record = comparison['records']['Line 6::HX Stomp']
    assert record['link'] == source_path
    source = research_tools.read_preserved_source(source_path)
    facts = record['facts']
    assert all(f['source'] == source_path for f in facts)
    contexts = [p for p in source.split('\n\n') if p.startswith('Checked **2026-10-14**') or p.startswith('K/F/B =') or p.startswith('The rounded Line 6 FAQ') or p.startswith("**HX Stomp's old FAQ") or p.startswith('USB audio input/output counts')]
    assert len(contexts) == 5
    urls = ['https://line6.com/hx-stomp/','https://kb.line6.com/hx-stomp-faq','https://line6.com/support/page/kb/effects-controllers/helix/helix-30-release-notes-r934/','https://line6.com/software/index.html?hardware=All&name=HX+Edit&os=All&submit_form=set','https://www.thomannmusic.com/zoom_b6.htm']
    section = '\n## HX Stomp\n\nConsolidated2026-10-17. Complete legacy model rows, dated qualifications and URLs are retained below. Display, controls, expression and qualified Shopee offers were additionally checked; indexed manual/guide facts are labelled with access limitations. This existing guitar/bass model adds no inventory count. Verification remains partial.\n\n### HX Stomp historical source evidence\n\n'
    section += '\n\n'.join(contexts) + '\n\n'
    for fact in facts:
        section += '- **'+fact['field']+'** ('+fact['context']+'): '+fact['value']+'\n'
    section += '\nOriginal source URLs: '+', '.join(urls)+'\n\nThe P1 **USD555** observation was checked2026-10-14 at an international store, excluding destination tax/shipping; no IDR conversion or present stock claim is made. [Complete legacy source](effects/advanced-modelers.md) remains available; no source or incoming link was deleted.\n\n### HX Stomp comparison fields\n\n| Field | Dated evidence / qualification |\n|---|---|\n'
    for fact in facts:
        field, value = fact['field'], fact['value']
        if field == 'Other important differences':
            field = 'Other relevant features'
        if field == 'K/F/B':
            value = '**6/3/4**: upper/lower/volume plus three parameter rotaries; three capacitive footswitches; HOME/VIEW,ACTION and two PAGE buttons. Encoder presses counted once; power toggle separate. [HS-P](https://line6.com/hx-stomp/).'
        elif field == 'New USD observation':
            continue
        elif field == 'External expression':
            field = 'Expression'
            value = 'No built-in pedal/toe. Shared EXP1/2–FS4/5 accepts two external expression pedals, two switches, one of each, or compatible Mission pedal/toe-switch combination with appropriate cable/settings. These share one TRS socket, not independent ports. [HS-F](https://kb.line6.com/hx-stomp-faq).'
        elif field == 'Third-party IR':
            value = '**128 custom/third-party IR locations**, Single IR1024/2048 samples; one2048 or two1024 blocks per preset, subject to combined cab/IR and DSP restrictions. [Original3.80 manual, indexed evidence](https://line6.com/data/6/0a00051afdda673cccdb61c9c/application/pdf/HX%20Stomp%203.80%20Owner%27s%20Manual%20-%20English%20.pdf). Full reopen exceeded tool size limit; format/conversion details remain unverified.'
        elif field == 'Preset storage':
            value = '**126 editable presets**, three snapshots each. [HX Edit3.80 guide, indexed device-specific table](https://line6.com/data/6/0a00051aff0e673cd37585ccd/application/pdf/HX%20Edit%20Pilots%20Guide%203.80%20-%20English%20.pdf); full reopening failed. Factory-filled subset remains unverified; do not borrow XL128/four figures.'
        elif field == 'Power; battery/USB-powered?':
            value = 'FAQ officially supports **DC-3G**, legacy source records special2.5mm pin and **no batteries**. Product-panel text calls supplied adapter **DC-3**; name discrepancy retained. Voltage/polarity/current and USB-powered operation not independently verified. [HS-F](https://kb.line6.com/hx-stomp-faq),[HS-P](https://line6.com/hx-stomp/).'
        section += '| '+field+' | '+value+' |\n'
    section += '''| Display | **2.4-inch color LCD**, explicitly published. Touchscreen and numerical pixels unverified; capacitive footswitches do not establish a touch display. [HS-P](https://line6.com/hx-stomp/) |
| Used IDR | **Rp8.900.000**, explicitly Second/Bekas/Preloved, **Habis**; sellerotnielsusanto,shop91725285/item26545060709,Kota Surabaya. Indexed reopening checked2026-10-17; stale25–27September delivery. Historical ask, not an available offer or completed sale. Condition grade/accessories,warranty region,delivered charges and voucher eligibility unconfirmed. [Exact used listing](https://shopee.co.id/Line-6-HX-Stomp-%28Second-Bekas-Preloved%29-Digital-Multi-Effects-Electric-Guitar-Bass-Keyboard-Efek-Gitar-Elektrik-Akustik-i.91725285.26545060709) |
| New / retail IDR | **Rp11.229.000**, ROCKPIZZ MUSIC,shop440477624/item23519849983,Kota Denpasar,black HX Stomp. Indexed reopening checked2026-10-17,stale18August delivery. Retail hardware title; detailed condition,stock,accessories,warranty region,delivery/tax and voucher eligibility unconfirmed. Not HX Stomp XL. [Exact retail listing](https://shopee.co.id/LINE-6-HX-STOMP-MULTI-EFFECTS-GUITAR-PEDAL-BLACK-i.440477624.23519849983) |

### HX Stomp evidence limits

The product page/FAQ still contain six-block wording. Retain the firmware3.0 eight-block correction above; do not revert based on launch copy or equate advertised available-model totals with simultaneous capacity. Firmware-current category counts, exact synth/acoustic algorithms, IR import conversion, NAM/capture support, screen touch/pixels, detailed USB channel/driver/updater requirements and looper/drum limits remain open. No sibling XL specifications are substituted. Published2.4-inch display and numbered control descriptions are model-specific evidence; no screen size was measured from a photo. The3.80 manual/guide details above came from indexed original-document excerpts; full-file reading or visual inspection is not claimed.
'''
    brand = (ROOT/'LINE6.md').read_text().replace('Other legacy Line 6 records still require consolidation; no whole-repository migration claim is made.', 'All eight recorded Line 6 models now have root records; specification checks and market discovery remain incomplete.')
    old_count, old_legacy = state['canonical_root_model_count'],state['legacy_only_model_count']
    state['root_brand_content']['LINE6.md'].append(model)
    state['canonical_root_model_count'] += 1
    state['legacy_only_model_count'] -= 1
    state['consolidation_and_price_findings'].append(dict(models=['Line 6 HX Stomp'],model_name=model,brand='Line 6',destination='LINE6.md#hx-stomp',source=source_path,checked_date='2026-10-17',verification_kind='complete-model-rows-v1',source_sha256=digest(source),retained_comparison_facts=facts,retained_context=contexts,retained_source_urls=urls,status='Consolidated, partial; primary controls/display and qualified IDR offers added; indexed manual access limits explicit'))
    state['discovery_leads'].append(dict(model='Line 6 HX Stomp',checked_date='2026-10-17',status='Existing model refreshed; no duplicate count',urls=['https://shopee.co.id/Line-6-HX-Stomp-%28Second-Bekas-Preloved%29-Digital-Multi-Effects-Electric-Guitar-Bass-Keyboard-Efek-Gitar-Elektrik-Akustik-i.91725285.26545060709','https://shopee.co.id/LINE-6-HX-STOMP-MULTI-EFFECTS-GUITAR-PEDAL-BLACK-i.440477624.23519849983'],qualification='Used8900000,explicitsecond/preloved,Habis,otnielsusanto Surabaya. Retail11229000,ROCKPIZZ MUSIC Denpasar,staleAugust delivery. Condition/accessories/region/checkout stock unconfirmed.'))
    state['migration']['warning'] = f'{old_legacy-1} legacy-only models remain;{old_count+1} root-canonical. Full migration and research incomplete.'
    state['cursor'].update(model='IK Multimedia TONEX ONE — complete legacy consolidation',task='Read complete advanced-modelers source and all model-specific records for TONEX ONE. Preserve20-versus30 preset contradiction and original firmware/software dates; verify model-specific current official evidence and exact Shopee offers, consolidate in root IK-MULTIMEDIA.md and commit before TONEX Pedal. Continue remaining legacy models and fresh discovery.',after_queue=f'Continue unresolved-field checks and lossless consolidation of {old_legacy-1} legacy-only models.')
    readme = (ROOT/'README.md').read_text().replace(f'{old_count} detailed',f'{old_count+1} detailed').replace(f'{old_legacy} still rely',f'{old_legacy-1} still rely').replace('Helix LT,HX Stomp XL |','Helix LT,HX Stomp XL,HX Stomp |')
    multi = (ROOT/'MULTI-EFFECTS.md').read_text().replace(f'{old_count} root-canonical',f'{old_count+1} root-canonical')
    outputs={'LINE6.md':brand+section,'README.md':readme,'MULTI-EFFECTS.md':multi,'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n'}
    payload=dict(model_id='hx-stomp',model=model,inputs={p:digest((ROOT/p).read_text()) for p in list(outputs)+[source_path]},outputs=outputs,rollback_commit=research_tools.git('rev-parse','HEAD').strip())
    PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print('Preview HX Stomp: exact writes '+', '.join(outputs)+f'; canonical {old_count}->{old_count+1}; legacy {old_legacy}->{old_legacy-1}; active unchanged. Rollback '+payload['rollback_commit'])
    print('Plan saved: '+str(PLAN))



def plan_tonex_one():
    research_tools.identity()
    model, source_path = MODELS['tonex-one']
    brand_file = 'IK-MULTIMEDIA.md'
    assert not (ROOT/brand_file).exists(), 'Inspect existing brand content before merging'
    state_text = (ROOT/'research-state.json').read_text()
    state = json.loads(state_text)
    assert model not in state['root_brand_content'].get(brand_file, [])
    comparison = json.loads(Path('/tmp/instrumentfx-comparison-plan.json').read_text())
    assert comparison['ledger_hash'] == digest(state_text), 'Run make comparison-plan first'
    record = comparison['records']['IK Multimedia::TONEX ONE']
    assert record['link'] == source_path
    source = research_tools.read_preserved_source(source_path)
    facts = record['facts']
    assert all(f['source'] == source_path for f in facts)
    contexts = [p for p in source.split('\n\n') if p.startswith('Checked **2026-10-14**') or p.startswith('K/F/B =') or p.startswith("**TONEX ONE's 20-versus-30") or p.startswith('USB audio input/output counts')]
    contexts += [line for line in source.splitlines() if line.startswith('- P2:')]
    assert len(contexts) == 5
    urls = ['https://ikmultimedia.com/products/tonexone','https://www.ikmultimedia.com/products/tonexone/','https://ikmultimedia.com/cdn/shop/files/TONEX_ONE_MG_3569_r2.jpg?v=1783342577&width=1100']
    manual = 'https://www.dlxmusic.no/storage/C4DD59BE093554E6A03FCB475D76A724779D0AC890B654D94F944E14CE1A904F/b7557a90e3bd4196a7a49786bb2d0bc0/pdf/media/f5a0f1b04f054ed4b4182b51109983d9/TONEX_ONE_User_Manual.pdf'
    section = '# IK Multimedia multi-effects\n\nRoot brand records with individual observation dates. TONEX ONE is consolidated below; TONEX Pedal remains in its complete legacy source pending consolidation. Verification and market coverage remain incomplete.\n\n## TONEX ONE\n\nStandard TONEX ONE guitar/bass processor, not TONEX ONE+, Bass Edition or an artist variant. Consolidated and partially refreshed **2026-10-17**; no additional active model.\n\n### Preserved historical evidence\n\n'
    section += '\n\n'.join(contexts)+'\n\n'
    for fact in facts:
        section += '- **'+fact['field']+'** ('+fact['context']+'): '+fact['value']+'\n'
    section += '\nRetained model-source URLs: '+', '.join(urls)+'\n\n[Complete original comparison](effects/advanced-modelers.md) remains available. No legacy source or incoming link was removed.\n\n### Source identity and dates\n\n[M] [Manufacturer-authored TONEX ONE manual mirrored by DLX Music]('+manual+'),34 pages, document version1.0,rev05, dated2024/03/17 on its copyright page. Title, IK Multimedia authorship, standard ONE controls and dimensions match this model; it is an early manual, not evidence for every current firmware feature. Text was inspected; no visual diagram inspection is claimed.\n\n[P] [Current standard product page](https://ikmultimedia.com/products/tonexone), reopened2026-10-17.\n\n[B] [Official standard TONEX ONE launch announcement,24April2024](https://www.ikmultimedia.com/news/index.php?id=TonexOneAnnounced), explicitly documents guitar/bass use. No Bass Edition specification was borrowed.\n\n### TONEX ONE comparison fields\n\n| Field | Evidence and qualification |\n|---|---|\n'
    replacements = {
        'External expression': ('Expression', 'No built-in pedal/toe; no EXP socket in complete manual connection inventory. [M p.18]'),
        'K/F/B': ('K/F/B', '**4/1/1**: main plus three micro knobs, one footswitch, ALT button. [M p.18]'),
        'Preset storage': ('Preset storage', '**Conflict retained:** early manual p.21 has **20 presets and three active slots**; current page still advertises **30**, while its own specs say **20**. Rechecked2026-10-17. Firmware-specific capacity remains unresolved; do not substitute ONE+ storage. [M,P]'),
        'Third-party IR': ('Third-party IR', '**Yes:** create a custom-IR cabinet preset in TONEX Mac/PC, then transfer through Librarian. File formats, sample limits and independent IR capacity unverified. [M p.22]'),
        'Audio/control ports': ('Audio/control ports', 'Mono unbalanced instrument input; mono/stereo unbalanced output shared with headphones; USB-C; DC. Jack sizes remain unverified in this pass. [M p.18]'),
        'Power; battery/USB-powered?': ('Power / battery / USB', '**9V DC,120mA,center-negative**, or **USB5V,260mA**; USB operation explicit. Internal battery not established. [M pp.18,30]'),
        'Configuration apps and USB functions': ('Configuration apps and USB functions', 'Mac/PC Librarian; **USB2-in/2-out processed stereo,24-bit/44.1kHz**, always-active monitoring. Driver/updater/platform-version requirements unresolved. [M pp.29–31]'),
        'Other important differences': ('Other relevant features', 'Dual A/B has no bypass; Stomp mode is on/off. Auto-save, panel lock and mute/thru tuner. [M pp.19–20]'),
    }
    for fact in facts:
        field, value = replacements.get(fact['field'], (fact['field'],fact['value']))
        if field == 'New USD observation':
            continue
        section += '| '+field+' | '+value+' |\n'
    section += '''| Display | Colored LED status/tuner indications; graphical-screen specifications not established. [M pp.18–19] |
| Used IDR | ? — no condition-qualified local used amount established. |
| New / retail IDR | **Rp3.420.000**, Seven Stereo Music & Audio Store,shop16879370/item28250929069,Kota Bandung. Exact standard TONEX ONE hardware title; indexed reopening checked2026-10-17. Stock, detailed condition, accessory/software-license bundle, warranty region, delivered charges and voucher eligibility unconfirmed; relative delivery text is not checkout evidence. [Exact offer](https://shopee.co.id/IK-Multimedia-TONEX-ONE-Stompbox-Modeler-i.16879370.28250929069) |

### Qualified discovery and remaining uncertainty

[TOKOAUDIOPRO.COM](https://shopee.co.id/IK-Multimedia-TONEX-ONE-Amplifier-Cab-Pedal-Modeler-Efek-Gitar-Bass-i.253483262.26851077985),shop253483262/item26851077985,Kota Jakarta Pusat, showed **Rp3.550.000–Rp4.100.000 across two unspecified variations** on2026-10-17. Variant/condition/bundle mapping was not exposed. This unresolved variation range is excluded from the model's retail comparison; neither endpoint is assumed to buy the standard pedal. Stock, region, delivered charges and voucher eligibility remain unknown.

TONEX ONE is added to the shared bass comparison because the standard-model announcement explicitly supports bass and the original manual corroborates it. This does not add a unique model or assert equal bass performance for every effect. The BASS knob alone is not the inclusion basis. Dedicated Bass Edition and ONE+ remain distinct discovery candidates requiring exact hardware leads and variant verification.

The source body retains the original20/30 conflict and historical USD199.99 quote. Updated custom-IR, power and USB facts supersede their historical unknowns for the documented manual revision. Complete current delay/modulation/reverb choices and simultaneous architecture need matching firmware documentation; software descriptions do not automatically establish onboard blocks. Exact NAM compatibility, synth/acoustic algorithms, looper/drums/scenes, editor OS versions and firmware release requirements remain unverified. Capturing one's own rig is a documented companion-software workflow, not onboard hardware capture.
'''
    old_count, old_legacy = state['canonical_root_model_count'],state['legacy_only_model_count']
    state['root_brand_content'][brand_file] = [model]
    state['canonical_root_model_count'] += 1
    state['legacy_only_model_count'] -= 1
    state['consolidation_and_price_findings'].append(dict(models=['IK Multimedia TONEX ONE'],model_name=model,brand='IK Multimedia',destination=brand_file+'#tonex-one',source=source_path,checked_date='2026-10-17',verification_kind='complete-model-rows-v1',source_sha256=digest(source),retained_comparison_facts=facts,retained_context=contexts,retained_source_urls=urls,manual_source=manual,manual_revision='v1.0 rev05 dated2024/03/17',status='Consolidated, partial;20/30 contradiction preserved; standard bass membership supported by direct primary documentation'))
    state['discovery_leads'].append(dict(model='IK Multimedia TONEX ONE',checked_date='2026-10-17',status='Existing model refreshed; no new unique model',urls=['https://shopee.co.id/IK-Multimedia-TONEX-ONE-Stompbox-Modeler-i.16879370.28250929069','https://shopee.co.id/IK-Multimedia-TONEX-ONE-Amplifier-Cab-Pedal-Modeler-Efek-Gitar-Bass-i.253483262.26851077985'],qualification='Seven Stereo Bandung3420000 exact standard hardware; condition/license/bundle/region/checkout stock unknown. TOKOAUDIOPRO JakartaPusat3550000–4100000 two unspecified variations, excluded from retail comparison until mapping verified.'))
    state['migration']['warning'] = f'{old_legacy-1} legacy-only models remain;{old_count+1} root-canonical. Full migration and research incomplete.'
    state['cursor'].update(model='IK Multimedia TONEX Pedal — complete legacy consolidation',task='Read complete TONEX Pedal legacy rows and supporting original comparison. Consolidate in existing IK-MULTIMEDIA.md without losing firmware-qualified effects, prices or source URLs. Verify model-specific bass use and current official/manual/Shopee evidence; commit before another model. Continue remaining legacy models and fresh discovery.',after_queue=f'Continue unresolved-field checks and lossless consolidation of {old_legacy-1} legacy-only models.')
    readme=(ROOT/'README.md').read_text().replace(f'{old_count} detailed',f'{old_count+1} detailed').replace(f'{old_legacy} still rely',f'{old_legacy-1} still rely').replace('55 documented bass-capable models: 11 bass-focused plus 44 shared processors','56 documented bass-capable models: 11 bass-focused plus 45 shared processors')
    readme=readme.replace('| [JOYO.md](JOYO.md)', '| [IK-MULTIMEDIA.md](IK-MULTIMEDIA.md) |TONEX ONE |\n| [JOYO.md](JOYO.md)')
    multi=(ROOT/'MULTI-EFFECTS.md').read_text().replace(f'{old_count} root-canonical',f'{old_count+1} root-canonical')
    outputs={brand_file:section,'README.md':readme,'MULTI-EFFECTS.md':multi,'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n'}
    inputs={p:digest((ROOT/p).read_text()) for p in ['README.md','MULTI-EFFECTS.md','research-state.json',source_path]}
    inputs[brand_file]=None
    payload=dict(model_id='tonex-one',model=model,inputs=inputs,outputs=outputs,new_files=[brand_file],rollback_commit=research_tools.git('rev-parse','HEAD').strip())
    PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print('Preview TONEX ONE: writes '+', '.join(outputs)+f'; canonical {old_count}->{old_count+1}; legacy {old_legacy}->{old_legacy-1}; active unchanged. Creates '+brand_file+'; original absence recorded. Rollback '+payload['rollback_commit'])
    print('Plan saved: '+str(PLAN))



def plan_tonex_pedal():
    research_tools.identity()
    model, source_path = MODELS['tonex-pedal']
    brand_file = 'IK-MULTIMEDIA.md'
    state_text = (ROOT/'research-state.json').read_text()
    state = json.loads(state_text)
    assert model not in state['root_brand_content'][brand_file]
    comparison = json.loads(Path('/tmp/instrumentfx-comparison-plan.json').read_text())
    assert comparison['ledger_hash'] == digest(state_text), 'Run make comparison-plan first'
    record = comparison['records']['IK Multimedia::TONEX Pedal']
    assert record['link'] == source_path
    source = research_tools.read_preserved_source(source_path)
    facts = record['facts']
    assert all(f['source'] == source_path for f in facts)
    contexts = [p for p in source.split('\n\n') if p.startswith('Checked **2026-10-14**') or p.startswith('K/F/B =') or p.startswith('USB audio input/output counts')]
    contexts += [line for line in source.splitlines() if line.startswith('- P1:')]
    assert len(contexts) == 4
    urls = ['https://ikmultimedia.com/products/tonexpedal','https://www.ikmultimedia.com/products/tonexpedal/','https://ikmultimedia.com/cdn/shop/files/TONEX-Pedal---Studio-57101.jpg?v=1783348434&width=1100','https://www.thomannmusic.com/zoom_b6.htm']
    section = '\n## TONEX Pedal\n\nStandard guitar/bass TONEX Pedal, not TONEX ONE, Bass Edition or an anniversary bundle. Consolidated and partially refreshed **2026-10-17**; no new unique model.\n\n### Preserved historical evidence\n\n'
    section += '\n\n'.join(contexts)+'\n\n'
    for fact in facts:
        section += '- **'+fact['field']+'** ('+fact['context']+'): '+fact['value']+'\n'
    section += '\nRetained model-source URLs: '+', '.join(urls)+'\n\n[Complete original comparison](effects/advanced-modelers.md) is retained; no source or incoming link was removed. The USD429.99 official tax-excluded and USD299 international-seller observations retain their2026-10-14 context; no conversion or current delivered-price claim is made.\n\n### Source identity and limits\n\n[TP-M: manufacturer-authored manual mirrored by Kraft Music](https://files.kraftmusic.com/media/ownersmanual/TONEX_Pedal_User_Manual.pdf). English document v1.0.4, dated2023/04/12, printed pp.1–36; the same67-page PDF also contains a separate Japanese v1.0.2 dated2023/02/27. Title, IK Multimedia authorship, standard hardware and connections identify TONEX Pedal. English text was inspected; attempted front-panel PDF rendering failed. No successful visual panel verification is claimed. The attempted direct manufacturer manual endpoint returned403.\n\n[TP-P: current standard product page](https://ikmultimedia.com/products/tonexpedal), rechecked2026-10-17, confirms150 presets and2 delay/5 modulation/6 stereo-reverb choices. These are choices within processing stages, not a simultaneous count or proof of arbitrary duplicate blocks. Newer software TONEX Rig routing is not borrowed into this hardware record.\n\n### TONEX Pedal comparison fields\n\n| Field | Dated evidence / qualification |\n|---|---|\n'
    replacements = {
        'External expression': ('Expression','No built-in pedal/toe; EXT.CONTROL accepts an expression pedal or single/dual switch. External toe behavior unverified. [TP-M pp.16,26–27]'),
        'K/F/B': ('K/F/B','**7/3/0 front-panel**, retained photograph count. Encoder-role mapping has not been newly visually verified; do not add encoder presses as extra buttons. Rear power control separate.'),
        'Preset storage': ('Preset storage','**150 editable presets /50 banks**; Reloaded factory content fills150. Early manual separately specifies **up to300 Tone Models** with automatic replacement when full; this is not300 presets. [TP-M pp.13,18–19;TP-P]'),
        'Third-party IR': ('Third-party IR','**Yes:** create a custom-IR cabinet preset and transfer it through TONEX Librarian. Independent IR capacity, formats and sample conversion remain unverified. [TP-M p.18]'),
        'Audio/control ports': ('Audio/control ports','Mono unbalanced instrument input; L/R unbalanced outputs; headphones; MIDI IN/OUT; EXT.CONTROL; USB-B; DC. Output/headphone jack-size verification remains open. [TP-M p.16;retained source]'),
        'Configuration apps and USB functions': ('Configuration apps and USB functions','**TONEX Editor Mac/PC**; USB audio **24-bit/44.1kHz**. Early manual requires Windows10+ and ASIO driver for interface operation. Current OS/updater versions remain unverified. [TP-P;TP-M pp.28,34]'),
        'Other important differences': ('Other relevant features','Custom IRs and captures remain distinct. Expression macros, lock mode, bank/preset MIDI control. Early manual says dedicated interface needed for full rig modeling; no onboard capture claim. [TP-M pp.16,26–29]'),
    }
    for fact in facts:
        field, value = replacements.get(fact['field'],(fact['field'],fact['value']))
        if field == 'New USD observation':
            continue
        section += '| '+field+' | '+value+' |\n'
    section += '''| Display | Manufacturer indexed original page describes **eight16-segment characters**; manual documents color-coded AMP/CAB/ALT indicators. Published diagonal, touch and precise display technology remain unverified. Colored indicators do not establish a color LCD. [Original product-page index](https://www.ikmultimedia.com/products/tonexpedal/index.php);TP-M pp.14–15 |
| Used IDR | ? — no dependable condition-qualified local used quote established. |
| New / retail IDR | [Eleven Music exact TONEX Pedal offer](https://shopee.co.id/Tonex-Pedal-IK-Multimedia-TONE-X-Pedal-Amplifier-Pedal-Modeler-ToneX-i.12356205.21991009410),shop12356205/item21991009410,Kota Jakarta Pusat: **Rp7.640.000 search versus Rp8.150.000 reopened**, checked2026-10-17. Snapshot discrepancy retained; neither proves live checkout stock. Standard hardware title; condition, accessory/software-license bundle, region, delivered charges and voucher eligibility unconfirmed. No guessed discount or exchange rate. |

### Remaining model questions

A second [CH MUSIC exact Pedal listing](https://shopee.co.id/TONEX-Pedal-IK-Multimedia-TONEX-Pedal-Amplifier-Cabinet-Pedal-Modeler-i.195817632.17298184084),shop195817632/item17298184084,Kota Jakarta Pusat, was indexed at **Rp7.640.000** with **Layanan Tidak Tersedia**; reopening failed. This shipping/service limitation does not establish sold-out stock. Its observation is not substituted for the available checkout price of another seller. Condition, bundle, region and final charges remain unconfirmed.

Standard-model bass capability is explicit in the manufacturer-authored manual and standard Reloaded library; adding this shared bass row does not create another unique model or silently import Bass Edition presets. All fifteen original model fields and associated date/price qualifications remain above.

Current firmware-specific processing concurrency and complete category algorithms, IR limits, exact synth/acoustic functions, native/converted NAM, USB channel counts and bus-powered operation, internal battery, graphical-screen attributes, external toe behavior, scenes/looper/drums and condition-verified stock remain unresolved. Early-manual details retain their revision; new firmware is not assumed installed. No manual screenshot success or physical hardware test is claimed.
'''
    brand = (ROOT/brand_file).read_text().replace('TONEX ONE is consolidated below; TONEX Pedal remains in its complete legacy source pending consolidation.','Both recorded TONEX ONE and TONEX Pedal profiles are consolidated below; original sources remain available.')
    old_count,old_legacy = state['canonical_root_model_count'],state['legacy_only_model_count']
    state['root_brand_content'][brand_file].append(model)
    state['canonical_root_model_count'] += 1
    state['legacy_only_model_count'] -= 1
    state['consolidation_and_price_findings'].append(dict(models=['IK Multimedia TONEX Pedal'],model_name=model,brand='IK Multimedia',destination=brand_file+'#tonex-pedal',source=source_path,checked_date='2026-10-17',verification_kind='complete-model-rows-v1',source_sha256=digest(source),retained_comparison_facts=facts,retained_context=contexts,retained_source_urls=urls,manual_source='https://files.kraftmusic.com/media/ownersmanual/TONEX_Pedal_User_Manual.pdf',manual_revision='English1.0.4 dated2023/04/12;Japanese1.0.2 separate',status='Consolidated, partial; direct model bass evidence, qualified Shopee discrepancies and early manual limitations preserved'))
    state['discovery_leads'].append(dict(model='IK Multimedia TONEX Pedal',checked_date='2026-10-17',status='Existing model refreshed; no new unique model',urls=['https://shopee.co.id/Tonex-Pedal-IK-Multimedia-TONE-X-Pedal-Amplifier-Pedal-Modeler-ToneX-i.12356205.21991009410','https://shopee.co.id/TONEX-Pedal-IK-Multimedia-TONEX-Pedal-Amplifier-Cabinet-Pedal-Modeler-i.195817632.17298184084'],qualification='Eleven Music search7640000 versus reopen8150000. CH MUSIC indexed7640000 shipping/service unavailable,reopen failed. All condition/bundle/license/region/checkout stock unconfirmed.'))
    state['migration']['warning'] = f'{old_legacy-1} legacy-only models remain;{old_count+1} root-canonical. Full migration and research incomplete.'
    state['cursor'].update(model='Neural DSP Nano Cortex — complete legacy consolidation',task='Read complete Nano Cortex record and original advanced-modelers source. Consolidate in root NEURAL-DSP.md, preserving NanOS2 limits, capture versus mic-path distinctions, power restrictions and original uncertainty. Verify primary manual/current firmware and exact Shopee offers. Commit before another model; continue remaining legacy records and fresh discovery.',after_queue=f'Continue unresolved-field checks and lossless consolidation of {old_legacy-1} legacy-only models.')
    readme=(ROOT/'README.md').read_text().replace(f'{old_count} detailed',f'{old_count+1} detailed').replace(f'{old_legacy} still rely',f'{old_legacy-1} still rely').replace('56 documented bass-capable models: 11 bass-focused plus 45 shared processors','57 documented bass-capable models: 11 bass-focused plus 46 shared processors').replace('| [IK-MULTIMEDIA.md](IK-MULTIMEDIA.md) |TONEX ONE |','| [IK-MULTIMEDIA.md](IK-MULTIMEDIA.md) |TONEX ONE,TONEX Pedal |')
    multi=(ROOT/'MULTI-EFFECTS.md').read_text().replace(f'{old_count} root-canonical',f'{old_count+1} root-canonical')
    outputs={brand_file:brand+section,'README.md':readme,'MULTI-EFFECTS.md':multi,'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n'}
    payload=dict(model_id='tonex-pedal',model=model,inputs={p:digest((ROOT/p).read_text()) for p in list(outputs)+[source_path]},outputs=outputs,rollback_commit=research_tools.git('rev-parse','HEAD').strip())
    PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print('Preview TONEX Pedal: writes '+', '.join(outputs)+f'; canonical {old_count}->{old_count+1}; legacy {old_legacy}->{old_legacy-1}; active unchanged. Rollback '+payload['rollback_commit'])
    print('Plan saved: '+str(PLAN))



def plan_nano_cortex():
    research_tools.identity()
    model, source_path = MODELS['nano-cortex']
    brand_file = 'NEURAL-DSP.md'
    assert not (ROOT/brand_file).exists()
    state_text = (ROOT/'research-state.json').read_text()
    state = json.loads(state_text)
    comparison = json.loads(Path('/tmp/instrumentfx-comparison-plan.json').read_text())
    assert comparison['ledger_hash'] == digest(state_text)
    record = comparison['records']['Neural DSP::Nano Cortex']
    assert record['link'] == source_path
    facts = record['facts']
    source = research_tools.read_preserved_source(source_path)
    contexts = [p for p in source.split('\n\n') if p.startswith('Checked **2026-10-14**') or p.startswith('K/F/B =') or p.startswith('USB audio input/output counts')]
    contexts += [p for p in source.splitlines() if p.startswith('- [Nano Cortex current product page]')]
    assert len(contexts) == 4 and len(facts) == 15
    urls = ['https://neuraldsp.com/manual/nano-cortex','https://neuraldsp.com/nano-cortex']
    section = '# Neural DSP multi-effects\n\n## Nano Cortex\n\nComplete original model fields consolidated and partially refreshed **2026-10-17**. Standard Nano Cortex; no Quad Cortex specifications substituted.\n\n### Preserved historical evidence\n\n'+'\n\n'.join(contexts)+'\n\n'
    for f in facts:
        section += '- **'+f['field']+'** ('+f['context']+'): '+f['value']+'\n'
    section += '\nRetained original source URLs: '+', '.join(urls)+'\n\nThe [complete original comparison](effects/advanced-modelers.md) remains available; no source or incoming link removed.\n\n### Current comparison fields\n\n'
    section += (ROOT/'scripts/nano_cortex_record.txt').read_text()
    old_count, old_legacy = state['canonical_root_model_count'],state['legacy_only_model_count']
    state['root_brand_content'][brand_file] = [model]
    state['canonical_root_model_count'] += 1
    state['legacy_only_model_count'] -= 1
    state['consolidation_and_price_findings'].append(dict(models=['Neural DSP Nano Cortex'],model_name=model,brand='Neural DSP',destination=brand_file+'#nano-cortex',source=source_path,checked_date='2026-10-17',verification_kind='complete-model-rows-v1',source_sha256=digest(source),retained_comparison_facts=facts,retained_context=contexts,retained_source_urls=urls,status='Consolidated; partial verification. Explicit bass capability; NanOS2.2 playback versus creation distinction retained.',new_sources=['https://neuraldsp.com/nano-cortex-device-list','https://neuraldsp.com/nano-cortex-updates/nanos-2-2-0-is-now-available','https://neuraldsp.com/nano-cortex-updates/nanos-2-2-1-is-now-available']))
    state['discovery_leads'].append(dict(model='Neural DSP Nano Cortex',checked_date='2026-10-17',status='Existing model refreshed; no unique addition',urls=['https://shopee.co.id/Neural-DSP-Nano-Cortex-Digital-Effects-Processor-i.16879370.51902266280'],qualification='Seven Stereo Music & Audio Store Bandung11900000 Habis indexed. Condition/region/bundle/voucher/final charges unverified; not live stock or used-price evidence.'))
    state['migration']['warning'] = f'{old_legacy-1} legacy-only models remain;{old_count+1} root-canonical. Full migration and research incomplete.'
    state['cursor'].update(model='Audota AME-100 — complete legacy consolidation',task='Read all AME-100 legacy findings and supporting comparisons. Consolidate losslessly in root AUDOTA.md; preserve hardware revisions, ownership distinctions and all original prices/URLs/conflicts. Verify model-specific primary documentation and exact Shopee hardware offers; commit before another model. Continue remaining legacy models, fresh discovery and unresolved fields.',after_queue=f'Continue unresolved-field checks and lossless consolidation of {old_legacy-1} legacy-only models.')
    readme=(ROOT/'README.md').read_text().replace(f'{old_count} detailed',f'{old_count+1} detailed').replace(f'{old_legacy} still rely',f'{old_legacy-1} still rely').replace('57 documented bass-capable models: 11 bass-focused plus 46 shared processors','58 documented bass-capable models: 11 bass-focused plus 47 shared processors')
    readme=readme.replace('| [JOYO.md](JOYO.md)', '| [NEURAL-DSP.md](NEURAL-DSP.md) |Nano Cortex |\n| [JOYO.md](JOYO.md)')
    multi=(ROOT/'MULTI-EFFECTS.md').read_text().replace(f'{old_count} root-canonical',f'{old_count+1} root-canonical')
    outputs={brand_file:section,'README.md':readme,'MULTI-EFFECTS.md':multi,'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n'}
    inputs={p:digest((ROOT/p).read_text()) for p in ['README.md','MULTI-EFFECTS.md','research-state.json',source_path,'scripts/nano_cortex_record.txt']}
    inputs[brand_file]=None
    payload=dict(model_id='nano-cortex',model=model,inputs=inputs,outputs=outputs,new_files=[brand_file],rollback_commit=research_tools.git('rev-parse','HEAD').strip())
    PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print('Preview Nano Cortex exact writes: '+', '.join(outputs)+f'; canonical {old_count}->{old_count+1}; legacy {old_legacy}->{old_legacy-1}; active unchanged; rollback '+payload['rollback_commit'])
    print('Plan saved: '+str(PLAN))


def plan_ame100():
    research_tools.identity()
    model, source_path = MODELS['ame-100']
    brand_file = 'AUDOTA.md'
    assert not (ROOT/brand_file).exists()
    state_text = (ROOT/'research-state.json').read_text()
    state = json.loads(state_text)
    comparison = json.loads(Path('/tmp/instrumentfx-comparison-plan.json').read_text())
    assert comparison['ledger_hash'] == digest(state_text)
    record = comparison['records']['Audota::AME-100']
    assert record['link'] == source_path
    source = research_tools.read_preserved_source(source_path)
    prefix = 'AUDOTA-AME-100'
    body, refs = preserved_body(source, prefix)
    extra = [f for f in record['facts'] if f['source'] != source_path]
    shared = sorted({f['source'] for f in extra})
    assert shared == ['effects/audota.md']
    supporting = (ROOT/shared[0]).read_text()
    contexts = [p for p in supporting.split('\n\n') if p.startswith('**2026-10-15:') or p.startswith('K/F/B=') or p.startswith('A display icon') or p.startswith('No guitar model') or p.startswith('All are datedlisted') or p.startswith('Full findingreferences')]
    section = '# Audota multi-effects\n\nStandard AME-100 is consolidated below. Other recorded Audota models still need their complete root-brand merge. Research remains partial.\n\n## AME-100\n\nConsolidated **2026-10-17**. The complete original finding retains its2026-10-15 date, contradictions and historical next-model notes. Current cursor is in research-state.json. AME-100 ownership does not establish AVE-100 ownership.\n\n<!-- '+prefix+' source begins -->\n'+body+'<!-- '+prefix+' source ends -->\n\n### Preserved supporting comparison evidence\n\nHistorical comparison context below includes superseded catalogue counts; these are provenance, not current totals.\n\n'+'\n\n'.join(contexts)+'\n\n'
    for f in extra:
        section += '- **'+f['field']+'** ('+f['context']+'): '+f['value']+'\n'
    section += '\nSources: [Original finding]('+source_path+'), [Complete supporting comparison](effects/audota.md). Neither legacy source nor incoming link was removed.\n\n<!-- comparison evidence begins -->\n\n### Current AME-100 comparison fields\n\n| Field | Evidence and limitations |\n|---|---|\n'
    for f in record['facts']:
        if f['source'] != source_path or f['field'] == 'Follow-up technical correction':
            continue
        value = f['value']
        if f['field'] == 'NAM':
            value += ' Reopened2026-10-17: official importer explicitly confirms **NAM profile plus IR simultaneously**. This does not establish unrestricted native NAM, duplicate capture blocks or total concurrency. [U1]'
        if f['field'] == 'Editing':
            value += ' Official software index reopened2026-10-17 still lists Studio1.2.3 Windows/macOS and Android1.3.0. V1.2.3 announcement adds PC preset import/export/sharing and backup/restore. [D,U1]'
        section += '| '+f['field']+' | '+value+' |\n'
    section += '\n<!-- comparison evidence ends -->\n\n### Current source access and remaining limits\n\nRechecked **2026-10-17**: [Official importer V1.2.3 announcement,2026-09-02](https://shop.warwick.de/en/Blog/AUDOTA-AME-100) was fully accessible; it additionally reports optimization of built-in amp/cab effects and bug fixes, without a model-by-model change list. NAM conversion architecture restrictions remain unverified. [Official software index](https://en.audota.com/EN_software.html) and [manual index](https://en.audota.com/EN_manuals.html) reopened; the latter names AME-100 Manual_EN but did not expose a manual-file link in extracted text. No file was downloaded or installed.\n\nThe manufacturer AME100EN product page timed out on two attempts. September11 importer page reopened without usable body text, so the historical80/200 preset conflict remains qualified by its original evidence date rather than newly resolved. Touch, precise concurrent limit/category breakdown, USB channels, driver and NAM architecture limits remain unknown. Targeted Shopee Indonesia searches for Audota AME-100/AME100 yielded no exact indexed hardware offer; used/new IDR, seller, condition, stock, bundle, warranty region, vouchers and delivered charges remain unverified. No foreign price was converted.\n'
    old_count, old_legacy = state['canonical_root_model_count'],state['legacy_only_model_count']
    state['root_brand_content'][brand_file] = [model]
    state['canonical_root_model_count'] += 1
    state['legacy_only_model_count'] -= 1
    state['consolidation_and_price_findings'].append(dict(models=['Audota AME-100'],model_name=model,brand='Audota',destination=brand_file+'#ame-100',source=source_path,checked_date='2026-10-17',verification_kind='complete-source-body-v1',source_sha256=digest(source),marker=prefix,renamed_references=refs,retained_comparison_facts=extra,retained_context=contexts,retained_source_urls=[],supporting_sources=shared,supporting_source_hashes={p:digest((ROOT/p).read_text()) for p in shared},status='Complete finding and supporting fields retained; partial technical verification. NAM+IR concurrency and PC backup/sharing rechecked; no exact Shopee offer.'))
    state['migration']['warning'] = f'{old_legacy-1} legacy-only models remain;{old_count+1} root-canonical. Full migration and research incomplete.'
    state['cursor'].update(model='Audota AME-200 — complete legacy consolidation',task='Read complete AME-200 finding and supporting Audota comparison. Merge into existing AUDOTA.md without borrowing Pro power/battery/expression specs. Preserve220/221 and supply-current conflicts, all prices/URLs and firmware restrictions. Verify exact primary and Shopee evidence; commit before next model.',after_queue=f'Continue unresolved-field checks and lossless consolidation of {old_legacy-1} legacy-only models.')
    readme=(ROOT/'README.md').read_text().replace(f'{old_count} detailed',f'{old_count+1} detailed').replace(f'{old_legacy} still rely',f'{old_legacy-1} still rely')
    readme=readme.replace('| [JOYO.md](JOYO.md)', '| [AUDOTA.md](AUDOTA.md) |AME-100 |\n| [JOYO.md](JOYO.md)')
    multi=(ROOT/'MULTI-EFFECTS.md').read_text().replace(f'{old_count} root-canonical',f'{old_count+1} root-canonical')
    outputs={brand_file:section,'README.md':readme,'MULTI-EFFECTS.md':multi,'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n'}
    inputs={p:digest((ROOT/p).read_text()) for p in ['README.md','MULTI-EFFECTS.md','research-state.json',source_path]+shared}
    inputs[brand_file]=None
    payload=dict(model_id='ame-100',model=model,inputs=inputs,outputs=outputs,new_files=[brand_file],rollback_commit=research_tools.git('rev-parse','HEAD').strip())
    PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print('Preview AME-100 exact writes: '+', '.join(outputs)+f'; canonical {old_count}->{old_count+1}; legacy {old_legacy}->{old_legacy-1}; active unchanged; rollback '+payload['rollback_commit'])
    print('Plan saved: '+str(PLAN))

def plan_ame200():
    research_tools.identity()
    model, source_path = MODELS['ame-200']
    brand_file = 'AUDOTA.md'
    assert (ROOT/brand_file).exists()
    assert model not in json.loads((ROOT/'research-state.json').read_text())['root_brand_content'][brand_file]
    state_text = (ROOT/'research-state.json').read_text()
    state = json.loads(state_text)
    comparison = json.loads(Path('/tmp/instrumentfx-comparison-plan.json').read_text())
    assert comparison['ledger_hash'] == digest(state_text)
    record = comparison['records']['Audota::AME-200']
    assert record['link'] == source_path
    source = research_tools.read_preserved_source(source_path)
    prefix = 'AUDOTA-AME-200'
    body, refs = preserved_body(source, prefix)
    extra = [f for f in record['facts'] if f['source'] != source_path]
    shared = sorted({f['source'] for f in extra})
    assert shared == ['effects/audota.md']
    supporting = (ROOT/shared[0]).read_text()
    contexts = [p for p in supporting.split('\n\n') if p.startswith('**2026-10-15:') or p.startswith('K/F/B=') or p.startswith('A display icon') or p.startswith('No guitar model') or p.startswith('All are datedlisted') or p.startswith('Full findingreferences')]
    section = '\n## AME-200\n\nStandard model, not Pro. Consolidated **2026-10-17**, preserving the complete dated finding and all supporting model fields. Historical next-model notes are provenance; current task is in research-state.json.\n\n<!-- '+prefix+' source begins -->\n'+body+'<!-- '+prefix+' source ends -->\n\n### Preserved supporting comparison evidence\n\nHistorical context includes superseded catalogue counts, not current totals.\n\n'+'\n\n'.join(contexts)+'\n\n'
    for f in extra:
        section += '- **'+f['field']+'** ('+f['context']+'): '+f['value']+'\n'
    section += '\nSources: [Original finding]('+source_path+'), [Complete supporting comparison](effects/audota.md). No original source or incoming link removed.\n\n<!-- comparison evidence begins -->\n\n### Current AME-200 comparison fields\n\n| Field | Evidence and limits |\n|---|---|\n'
    for f in record['facts']:
        if f['source'] != source_path or f['field'] == 'Follow-up technical correction':
            continue
        if f['field'] == 'Expression / controls':
            section += '| Expression | No built-in pedal; one6.35mm TRS external EXP input. External toe behavior unverified. [M] |\n| K/F/B | **2 rotary /4 footswitches /4 buttons**: EDIT,MASTER;A/B/C/D;PLAY,BACK,SWITCH,SAVE. Encoder push counted once. [M] |\n'
            continue
        value=f['value']
        if f['field'] == 'Power':
            value += ' English page and importer both reconfirm9V/300mA center-negative on2026-10-17; Chinese page timed out, so its earlier1.5A statement is preserved rather than resolved.'
        if f['field'] == 'Audio/control ports':
            value += ' Manufacturer specs additionally publish input2.2MΩ, output510Ω and headphone32Ω. Importer prose incorrectly describes stereo input; numbered original manual documents one instrument input. [P,M,U]'
        if f['field'] == 'Retail IDR':
            value += ' Reopen again failed2026-10-17; condition, checkout stock, region/warranty, accessory bundle, vouchers and delivered charges remain unverified. Retained historical ask, not a current retail range.'
        if f['field'] == 'NAM':
            value += ' Current importer reopen did not expose the earlier NAM statement; retain its original observation date and unverified workflow. No AME-100 conversion spec borrowed.'
        section += '| '+f['field']+' | '+value+' |\n'
    section += '\n<!-- comparison evidence ends -->\n\n### Current source access and unresolved questions\n\nChecked **2026-10-17**: [English manufacturer page](https://en.audota.com/AME200EN.html) still advertises221 models,50 rhythms,200 presets,20 IR locations,60-second looper and3.5-inch color display. Its included-expression wording conflicts with its own explicit external-pedal description; the numbered original manual remains the control/connector authority. Published operating temperature is0–60°C. No touchscreen capability is inferred.\n\n[Importer standard-model page](https://shop.warwick.de/de/effektpedale-multieffekt-prozessorenaudota-ame-200-amp-modeler-multi-effects) corroborates power/control data and describes volume/wah external expression. Its stereo-input prose conflicts with the numbered manual; no stereo input is silently added. The page does not expose NAM in the present extraction; historical firmware-qualified A1/A2 evidence remains dated and partial.\n\n[Audota-authored original manual text, V01 dated2025-07-25](https://manuals.plus/m/e83dfa8d3d3ef2939052a142e66f922ba406bc6d9f9b8cfad226ccaaa2266893) reopened with matching model/revision identity and model-specific numbered panel/connection/specification text; no generated FAQ or PDF visual inspection used. [Chinese product page](https://www.audota.com/AME200CN.html) timed out. Exact Shopee item reopening failed and targeted search yielded no new exact price. No dependency, software or document file was downloaded or executed.\n\nComplete source bodies retain all original source URLs, revision conflicts and acoustic algorithms. Remaining gaps: toe behavior, touch, exact concurrent DSP budget, factory/user split, NAM conversion/native architecture, USB channels/drivers, battery/bus-power and current condition-specific price/stock. Do not substitute Pro battery or expression specifications.\n'
    old_count, old_legacy = state['canonical_root_model_count'],state['legacy_only_model_count']
    state['root_brand_content'][brand_file].append(model)
    state['canonical_root_model_count'] += 1
    state['legacy_only_model_count'] -= 1
    state['consolidation_and_price_findings'].append(dict(models=['Audota AME-200'],model_name=model,brand='Audota',destination=brand_file+'#ame-200',source=source_path,checked_date='2026-10-17',verification_kind='complete-source-body-v1',source_sha256=digest(source),marker=prefix,renamed_references=refs,retained_comparison_facts=extra,retained_context=contexts,retained_source_urls=[],supporting_sources=shared,supporting_source_hashes={p:digest((ROOT/p).read_text()) for p in shared},status='Complete finding/supporting facts retained. English power corroborated; historical Chinese current,220/221 and40/50 conflicts retained; current NAM and Shopee access remain limited.'))
    state['migration']['warning'] = f'{old_legacy-1} legacy-only models remain;{old_count+1} root-canonical. Full migration and research incomplete.'
    state['cursor'].update(model='Audota AME-200 Pro — complete legacy consolidation',task='Read full Pro finding and supporting Audota comparison. Consolidate in AUDOTA.md, preserving Pro battery/expression differences, charging-time/current/model-count conflicts and all source/price qualifications. Verify exact primary and Shopee evidence; commit before next model.',after_queue=f'Continue unresolved-field checks and lossless consolidation of {old_legacy-1} legacy-only models.')
    readme=(ROOT/'README.md').read_text().replace(f'{old_count} detailed',f'{old_count+1} detailed').replace(f'{old_legacy} still rely',f'{old_legacy-1} still rely')
    readme=readme.replace('| [AUDOTA.md](AUDOTA.md) |AME-100 |', '| [AUDOTA.md](AUDOTA.md) |AME-100,AME-200 |')
    multi=(ROOT/'MULTI-EFFECTS.md').read_text().replace(f'{old_count} root-canonical',f'{old_count+1} root-canonical')
    outputs={brand_file:(ROOT/brand_file).read_text().replace('Standard AME-100 is consolidated below.','Standard AME-100 and AME-200 are consolidated below.')+section,'README.md':readme,'MULTI-EFFECTS.md':multi,'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n'}
    inputs={p:digest((ROOT/p).read_text()) for p in ['README.md','MULTI-EFFECTS.md','research-state.json',source_path]+shared}
    inputs[brand_file]=digest((ROOT/brand_file).read_text())
    payload=dict(model_id='ame-200',model=model,inputs=inputs,outputs=outputs,new_files=[],rollback_commit=research_tools.git('rev-parse','HEAD').strip())
    PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print('Preview AME-200 exact writes: '+', '.join(outputs)+f'; canonical {old_count}->{old_count+1}; legacy {old_legacy}->{old_legacy-1}; active unchanged; rollback '+payload['rollback_commit'])
    print('Plan saved: '+str(PLAN))

def plan_ame200pro():
    research_tools.identity()
    model, source_path = MODELS['ame-200-pro']
    brand_file = 'AUDOTA.md'
    assert (ROOT/brand_file).exists()
    assert model not in json.loads((ROOT/'research-state.json').read_text())['root_brand_content'][brand_file]
    state_text = (ROOT/'research-state.json').read_text()
    state = json.loads(state_text)
    comparison = json.loads(Path('/tmp/instrumentfx-comparison-plan.json').read_text())
    assert comparison['ledger_hash'] == digest(state_text)
    record = comparison['records']['Audota::AME-200 Pro']
    assert record['link'] == source_path
    source = research_tools.read_preserved_source(source_path)
    prefix = 'AUDOTA-AME-200 Pro'
    body, refs = preserved_body(source, prefix)
    extra = [f for f in record['facts'] if f['source'] != source_path]
    shared = sorted({f['source'] for f in extra})
    assert shared == ['effects/audota.md']
    supporting = (ROOT/shared[0]).read_text()
    contexts = [p for p in supporting.split('\n\n') if p.startswith('**2026-10-15:') or p.startswith('K/F/B=') or p.startswith('A display icon') or p.startswith('No guitar model') or p.startswith('All are datedlisted') or p.startswith('Full findingreferences')]
    for headers, rows, context in comparison_views.tables(supporting):
        for row in rows:
            if comparison_views.norm(row[0]) == 'pro':
                extra += [dict(field=h,value=v,source=shared[0],context=context) for h,v in zip(headers[1:],row[1:])]
    contexts += [p for p in supporting.split('\n\n') if p.startswith("Each model's original manual appendix")]
    section = '\n## AME-200 Pro\n\nDistinct Pro hardware: built-in toe-switch expression, CTRL footswitch and rechargeable battery. Consolidated **2026-10-17**; the complete original finding and supporting facts retain their dates and disagreements. Historical next notes are provenance; use research-state.json for current tasks.\n\n<!-- '+prefix+' source begins -->\n'+body+'<!-- '+prefix+' source ends -->\n\n### Preserved supporting comparison evidence\n\nHistorical catalogue totals below are superseded.\n\n'+'\n\n'.join(contexts)+'\n\n'
    for f in extra:
        section += '- **'+f['field']+'** ('+f['context']+'): '+f['value']+'\n'
    section += '\nSources: [Original finding]('+source_path+'), [Complete supporting comparison](effects/audota.md). No legacy source or incoming link removed.\n\n<!-- comparison evidence begins -->\n\n### Current Pro comparison fields\n\n| Field | Evidence and limitations |\n|---|---|\n'
    for f in record['facts']:
        if f['source'] != source_path or f['field'] == 'Follow-up technical correction':
            continue
        if f['field'] == 'Expression / controls':
            section += '| Expression | **Built-in expression with toe switching**; no external EXP socket in complete inventory. [M] |\n| K/F/B | **2 rotary /5 footswitches /4 buttons**: EDIT,MASTER;A/B/C/D+CTRL;PLAY,BACK,SWITCH,SAVE. Toe and power separate. [M] |\n'
            continue
        if f['field'] == 'Display / body':
            section += '| Display | **3.5-inch color**, touch unverified. [P] |\n| Dimensions / weight | **L324.5×W144.7×H49.8mm;1.145kg**; large under either orientation. [P] |\n'
            continue
        value=f['value']
        if f['field'] == 'Power / battery':
            value += ' Rechecked2026-10-17: English manufacturer page still contains both2.5h and3h charge statements; importer says3h. Preserve conflict; ratings not measured runtime.'
        if f['field'] == 'NAM':
            value += ' Importer statement reopened2026-10-17 confirms the same firmware-qualified A1/A2 claim; it does not establish native architecture or conversion procedure.'
        if f['field'] == 'IR / sample memory':
            value += ' Importer still labels combined capacity30 IR slots; retain that source conflict without replacing the manual split. [U]'
        if f['field'] == 'Retail IDR':
            value += ' Reindexed2026-10-17 at the same amount; direct reopen failed. Condition, live stock, accessories, regional warranty, vouchers and delivered charges remain unverified. No used quote inferred.'
        section += '| '+f['field']+' | '+value+' |\n'
    section += '\n<!-- comparison evidence ends -->\n\n### Source qualifications and current marketplace limits\n\nChecked **2026-10-17**: [Manufacturer Pro English page](https://en.audota.com/AME200ProEN.html) corroborates five switches, built-in expression,7.4V2000mAh battery,9V1.5A center-negative supply,7.5h runtime rating and contradictory2.5h/3h charging lines. It still advertises221 models and50 rhythms, preserving the original appendix/operation disagreements. Published operating temperature0–60°C; input2.2MΩ/output510Ω/headphones32Ω. No touch inference or USB charging claim.\n\n[Official importer Pro page](https://shop.warwick.de/en/effect-pedals-multi-effects-processorsaudota-ame-200-pro-amp-modeler-multi-effects) explicitly retains NAM A1/A2 fromV1.37. Its four-foot-switch summary and30-IR wording conflict with manufacturer five switches and original20-IR/10-amp split. Mobile OTG recording is not proof of a mobile full editor. No sibling workflow imported. [Original manual-text mirror](https://device.report/manuals/shenzhen-audota-ame-200pro-user-manual) reopened; original PDF/render inspection claims above retain their original date and are not claimed repeated today. [Chinese manufacturer page](https://www.audota.com/AME200ProCN.html) timed out. No files or dependencies downloaded.\n\nAdditional exact hardware leads, indexed2026-10-17: [Dial Musik](https://shopee.co.id/Audota-AME-200-Pro-Multi-Effects-Digital-AME-200-Pro-AME200Pro-Multi-Efek-i.338305078.41127780541),shop338305078/item41127780541,Kota Palembang, **Rp2.350.000,Habis**,stale2–3October delivery; historical ask, not live stock. [GITARO STORE INDONESIA](https://shopee.co.id/Audota-Ame-200Pro-Amp-Modeler-Multi-Effects-Pedal-Five-Switches-Expression-Pedal-Audota-Ame-200-Pro-i.1643318004.47303247859),shop1643318004/item47303247859,Kota Jakarta Barat, **Rp2.349.999**,indexed title/ask only, checkout stock unverified. Both lack condition-grade, bundle, warranty-region, delivered-charge and usable-voucher verification. Late-delivery compensation is not a current purchase discount.\n\n[Apregio mixed200/Pro listing](https://shopee.co.id/Audota-AME-200-PRO-AME200-PRO-AME-200-Amp-Modeler-Multi-Effects-Pedal-Audota-AME200PRO-Apregio-Musik-i.3012339.55856904342),shop3012339/item55856904342,Kota Surabaya, has two variations and **Rp1.750.000–Rp2.350.000** without exposed selection-to-price mapping. Exclude that range from Pro pricing; lower amount is not assumed to buy Pro. The older second Hurtrock quote retains its June delivery provenance in the preserved record.\n\nRemaining: native/converted NAM architecture and workflow, exact concurrent DSP limits, current firmware category totals, factory-filled preset split, touchscreen, USB channels/drivers/bus power/charging, and condition-qualified local used/live retail offers. All source contradictions remain unresolved where current evidence is insufficient.\n'
    old_count, old_legacy = state['canonical_root_model_count'],state['legacy_only_model_count']
    state['root_brand_content'][brand_file].append(model)
    state['canonical_root_model_count'] += 1
    state['legacy_only_model_count'] -= 1
    state['consolidation_and_price_findings'].append(dict(models=['Audota AME-200 Pro'],model_name=model,brand='Audota',destination=brand_file+'#ame-200-pro',source=source_path,checked_date='2026-10-17',verification_kind='complete-source-body-v1',source_sha256=digest(source),marker=prefix,renamed_references=refs,retained_comparison_facts=extra,retained_context=contexts,retained_source_urls=[],supporting_sources=shared,supporting_source_hashes={p:digest((ROOT/p).read_text()) for p in shared},status='Complete Pro finding and all supporting rows retained; firmware-qualified A1/A2 confirmed, charging/control/IR/count conflicts and qualified Shopee offers preserved.'))
    state['migration']['warning'] = f'{old_legacy-1} legacy-only models remain;{old_count+1} root-canonical. Full migration and research incomplete.'
    state['cursor'].update(model='Audota ACE-100 — complete legacy consolidation',task='Read complete ACE-100 finding and supporting Audota comparison; consolidate losslessly into AUDOTA.md. Verify model-specific controls, load-slot ambiguity, power/application limits and exact Shopee hardware evidence. Preserve all sources/prices/conflicts and commit before another model.',after_queue=f'Continue unresolved-field checks and lossless consolidation of {old_legacy-1} legacy-only models.')
    readme=(ROOT/'README.md').read_text().replace(f'{old_count} detailed',f'{old_count+1} detailed').replace(f'{old_legacy} still rely',f'{old_legacy-1} still rely')
    readme=readme.replace('| [AUDOTA.md](AUDOTA.md) |AME-100,AME-200 |','| [AUDOTA.md](AUDOTA.md) |AME-100,AME-200,AME-200 Pro |')
    multi=(ROOT/'MULTI-EFFECTS.md').read_text().replace(f'{old_count} root-canonical',f'{old_count+1} root-canonical')
    outputs={brand_file:(ROOT/brand_file).read_text().replace('Standard AME-100 and AME-200 are consolidated below.','AME-100, standard AME-200 and AME-200 Pro are consolidated below.')+section,'README.md':readme,'MULTI-EFFECTS.md':multi,'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n'}
    inputs={p:digest((ROOT/p).read_text()) for p in ['README.md','MULTI-EFFECTS.md','research-state.json',source_path]+shared}
    inputs[brand_file]=digest((ROOT/brand_file).read_text())
    payload=dict(model_id='ame-200-pro',model=model,inputs=inputs,outputs=outputs,new_files=[],rollback_commit=research_tools.git('rev-parse','HEAD').strip())
    PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print('Preview AME-200 Pro exact writes: '+', '.join(outputs)+f'; canonical {old_count}->{old_count+1}; legacy {old_legacy}->{old_legacy-1}; active unchanged; rollback '+payload['rollback_commit'])
    print('Plan saved: '+str(PLAN))

def plan_ace100():
    research_tools.identity()
    model, source_path = MODELS['ace-100']
    brand_file = 'AUDOTA.md'
    assert (ROOT/brand_file).exists()
    assert model not in json.loads((ROOT/'research-state.json').read_text())['root_brand_content'][brand_file]
    state_text = (ROOT/'research-state.json').read_text()
    state = json.loads(state_text)
    comparison = json.loads(Path('/tmp/instrumentfx-comparison-plan.json').read_text())
    assert comparison['ledger_hash'] == digest(state_text)
    record = comparison['records']['Audota::ACE-100']
    assert record['link'] == source_path
    source = research_tools.read_preserved_source(source_path)
    prefix = 'AUDOTA-ACE-100'
    body, refs = preserved_body(source, prefix)
    extra = [f for f in record['facts'] if f['source'] != source_path]
    shared = sorted({f['source'] for f in extra})
    assert shared == ['effects/audota.md']
    supporting = (ROOT/shared[0]).read_text()
    contexts = [p for p in supporting.split('\n\n') if p.startswith('**2026-10-15:') or p.startswith('K/F/B=') or p.startswith('A display icon') or p.startswith('No guitar model') or p.startswith('All are datedlisted') or p.startswith('Full findingreferences')]
    section = '\n## ACE-100\n\nConsolidated **2026-10-17**. This is ACE-100 guitar multi-effects, not AME-100 or a power supply. Original dates, source conflicts and historical next-model notes remain below; use research-state.json for current work.\n\n<!-- '+prefix+' source begins -->\n'+body+'<!-- '+prefix+' source ends -->\n\n### Preserved supporting comparison evidence\n\nHistorical catalogue counts below are superseded.\n\n'+'\n\n'.join(contexts)+'\n\n'
    for f in extra:
        section += '- **'+f['field']+'** ('+f['context']+'): '+f['value']+'\n'
    section += '\nSources: [Original finding]('+source_path+'), [Complete supporting comparison](effects/audota.md). No legacy source or incoming link removed.\n\n<!-- comparison evidence begins -->\n\n### Current ACE-100 comparison fields\n\n| Field | Evidence and qualification |\n|---|---|\n'
    for f in record['facts']:
        if f['source'] != source_path or f['field'] == 'Follow-up technical correction':
            continue
        value=f['value']
        if f['field'] == 'Display':
            value += ' Manufacturer English page now explicitly says **LED screen**, rechecked2026-10-17; this corroborates LED over the quick-guide LCD wording, without proving readout color/diagonal/touch.'
        if f['field'] == 'Retail IDR':
            value += ' Exact Apregio listing reopened2026-10-17 at **Rp1.100.000**,Kota Surabaya,now displaying stale27–29August delivery. Keep older July snapshot separately; no authenticated stock, detailed condition, accessory bundle, regional warranty, delivered charges or voucher eligibility verified. Late-delivery compensation is not a purchase discount.'
        section += '| '+f['field']+' | '+value+' |\n'
    section += '\n<!-- comparison evidence ends -->\n\n### Current primary-source review\n\nReopened **2026-10-17**: [Manufacturer English ACE-100 page](https://en.audota.com/ACE100EN.html) explicitly documents LED readout, TRS stereo output via splitter, separate stereo phones, two USB functions, Bluetooth audio/app pairing,40 presets, Live/Preset mode,2000mAh battery,5h runtime and2.5h charging ratings. USB charging specification remains5V/2A using USB-A-to-C only. No operating-while-charging, native NAM or touch capability is inferred. Color-customizable footswitch LED bars remain distinct from the numeric display. Manufacturer accessories are quick guide/data cable; seller bundle contents remain unverified.\n\n[Official importer ACE-100 page](https://shop.warwick.de/en/effect-pedals-multi-effects-processorsaudota-ace-100-intelligent-combined-effects-pedal) still lists the16 named control functions,4 footswitches,40 memories and16 IR slots. MOD chorus/flanger/tremolo,delay digital/analog/tape,reverb room/hall/plate and iOS/Android Audota Studio plus PC editor are explicitly named. Its16-IR shorthand does not independently reconcile the manufacturer loading-slot partition; ADT and cabinet IR capacity remain qualified. No new visual rotary verification was performed.\n\n[Exact Apregio Shopee hardware offer](https://shopee.co.id/Audota-ACE100-Multi-Effects-Guitar-ACE-100-ACE100-Multi-Efek-Gitar-seri-atasnya-MVAVE-TANK-G-Apregio-Musik-i.3012339.44079112801),shop3012339/item44079112801,Kota Surabaya,retains the same amount on indexed reopening. A cached offer and relative seller activity do not prove current checkout availability or authenticity. No dependable used quote or verified storefront-only lower hardware price.\n\nAll original manufacturer-filed quick-guide identity, printing-dimension warning, table-label correction, failed visual inspection and full source URLs remain preserved above. No software, dependencies or document files downloaded. Remaining fields: visual rotary corroboration, readout diagonal/color/touch, precise IR/ADT partition,NAM architecture/workflow, USB channels/driver/OS minimums, charging-operation limits and current qualified local prices.\n'
    old_count, old_legacy = state['canonical_root_model_count'],state['legacy_only_model_count']
    state['root_brand_content'][brand_file].append(model)
    state['canonical_root_model_count'] += 1
    state['legacy_only_model_count'] -= 1
    state['consolidation_and_price_findings'].append(dict(models=['Audota ACE-100'],model_name=model,brand='Audota',destination=brand_file+'#ace-100',source=source_path,checked_date='2026-10-17',verification_kind='complete-source-body-v1',source_sha256=digest(source),marker=prefix,renamed_references=refs,retained_comparison_facts=extra,retained_context=contexts,retained_source_urls=[],supporting_sources=shared,supporting_source_hashes={p:digest((ROOT/p).read_text()) for p in shared},status='Complete ACE finding and supporting facts retained; manufacturer LED wording and exact Apregio historical ask rechecked; memory/NAM/USB/visual-control gaps preserved.'))
    state['migration']['warning'] = f'{old_legacy-1} legacy-only models remain;{old_count+1} root-canonical. Full migration and research incomplete.'
    state['cursor'].update(model='Audota AVE-100 — complete legacy consolidation',task='Read complete AVE-100 finding and supporting Audota vocal comparison. Merge losslessly into AUDOTA.md, preserving vocal-only scope, no ownership inference, original routing/phantom/firmware/looper and all source/price qualifications. Check primary and exact Shopee evidence; commit before another model.',after_queue=f'Continue unresolved-field checks and lossless consolidation of {old_legacy-1} legacy-only models.')
    readme=(ROOT/'README.md').read_text().replace(f'{old_count} detailed',f'{old_count+1} detailed').replace(f'{old_legacy} still rely',f'{old_legacy-1} still rely')
    readme=readme.replace('| [AUDOTA.md](AUDOTA.md) |AME-100,AME-200,AME-200 Pro |','| [AUDOTA.md](AUDOTA.md) |AME-100,AME-200,AME-200 Pro,ACE-100 |')
    multi=(ROOT/'MULTI-EFFECTS.md').read_text().replace(f'{old_count} root-canonical',f'{old_count+1} root-canonical')
    outputs={brand_file:(ROOT/brand_file).read_text().replace('AME-100, standard AME-200 and AME-200 Pro are consolidated below.','AME-100, standard AME-200, AME-200 Pro and ACE-100 are consolidated below.')+section,'README.md':readme,'MULTI-EFFECTS.md':multi,'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n'}
    inputs={p:digest((ROOT/p).read_text()) for p in ['README.md','MULTI-EFFECTS.md','research-state.json',source_path]+shared}
    inputs[brand_file]=digest((ROOT/brand_file).read_text())
    payload=dict(model_id='ace-100',model=model,inputs=inputs,outputs=outputs,new_files=[],rollback_commit=research_tools.git('rev-parse','HEAD').strip())
    PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print('Preview ACE-100 exact writes: '+', '.join(outputs)+f'; canonical {old_count}->{old_count+1}; legacy {old_legacy}->{old_legacy-1}; active unchanged; rollback '+payload['rollback_commit'])
    print('Plan saved: '+str(PLAN))

def plan_ave100():
    research_tools.identity()
    model, source_path = MODELS['ave-100']
    brand_file = 'AUDOTA.md'
    assert (ROOT/brand_file).exists()
    assert model not in json.loads((ROOT/'research-state.json').read_text())['root_brand_content'][brand_file]
    state_text = (ROOT/'research-state.json').read_text()
    state = json.loads(state_text)
    comparison = json.loads(Path('/tmp/instrumentfx-comparison-plan.json').read_text())
    assert comparison['ledger_hash'] == digest(state_text)
    record = comparison['records']['Audota::AVE-100']
    assert record['link'] == source_path
    source = research_tools.read_preserved_source(source_path)
    prefix = 'AUDOTA-AVE-100'
    body, refs = preserved_body(source, prefix)
    extra = [f for f in record['facts'] if f['source'] != source_path]
    shared = sorted({f['source'] for f in extra})
    assert shared == ['effects/audota.md']
    supporting = (ROOT/shared[0]).read_text()
    contexts = [p for p in supporting.split('\n\n') if p.startswith('**2026-10-15:') or p.startswith('K/F/B=') or p.startswith('A display icon') or p.startswith('No guitar model') or p.startswith('All are datedlisted') or p.startswith('Full findingreferences')]
    for headers, rows, context in comparison_views.tables(supporting):
        if context == 'Vocal model: AVE-100':
            extra += [dict(field=row[0],value=row[1],source=shared[0],context=context) for row in rows]
    contexts += [p for p in supporting.split('\n\n') if p.startswith("The original AVE manual's")]
    section = '\n## AVE-100\n\nVocal multi-effects only; no ownership assertion or guitar classification inferred from the combo input. Consolidated **2026-10-17**; original observation/inspection dates and historical next notes remain preserved.\n\n<!-- '+prefix+' source begins -->\n'+body+'<!-- '+prefix+' source ends -->\n\n### Preserved supporting comparison evidence\n\nHistorical catalogue totals below are superseded.\n\n'+'\n\n'.join(contexts)+'\n\n'
    for f in extra:
        section += '- **'+f['field']+'** ('+f['context']+'): '+f['value']+'\n'
    section += '\nSources: [Original finding]('+source_path+'), [Complete supporting comparison](effects/audota.md). No source file or incoming link removed.\n\n<!-- comparison evidence begins -->\n\n### Current AVE-100 comparison fields\n\n| Field | Evidence and qualification |\n|---|---|\n'
    for f in record['facts']:
        if f['source'] != source_path or f['field'] == 'Follow-up technical correction':
            continue
        value=f['value']
        if f['field'] == 'Firmware':
            value += ' Current manufacturer page rechecked2026-10-17 retains these changes and specifies approximately20% higher maximum reverb level/decay; marketing still separately describes two correction modes. Current exact mode allocation remains unresolved.'
        if f['field'] == 'Recording / live':
            value += ' Full official importer page reopened2026-10-17 and explicitly reconfirms65s maximum, unlimited overdubs and AUX/mic KeyLearn. Original volatile-memory statement remains from the manual.'
        if f['field'] == 'Retail IDR':
            value += ' Exact listing reopened2026-10-17: same amount, **Habis**,seller Red Musik Bali,Kota Denpasar. Condition, bundle, warranty region, delivered charges and usable voucher eligibility unverified; relative delivery/seller activity does not prove stock. No used-price inference.'
        section += '| '+{'Audio inputs':'Audio input ports','Audio outputs':'Audio output ports'}.get(f['field'],f['field'])+' | '+value+' |\n'
    section += '\n<!-- comparison evidence ends -->\n\n### Current primary-source and marketplace review\n\nChecked **2026-10-17**: [Manufacturer AVE-100 page](https://en.audota.com/AVE100EN.html) retains the1.2.0 upgrade instructions and20260519 package identity. It documents microphone-compression changes, AutoTune latency/logic and Electric mode, scale/key/harmony fixes and approximately20% expansion of maximum reverb level/decay. Its general feature list still describes two correction modes; no unsupported count of current firmware modes is asserted. Key LEDs distinguish major/minor; these are not a graphical display. Supplied adapter/manual/box are manufacturer packaging, not verified seller bundle contents.\n\n[Official importer AVE-100 page](https://shop.warwick.de/en/effect-pedals-vocal-effectsaudota-ave-100-vocal-multi-effects) fully reopened, confirming65-second recorder, unlimited overdubs, AUX-or-mic key learning,48V phantom, stereo phones, two mono outputs and9V≥500mA center-negative adapter. Its older Natural/Chromatic description does not supersede manufacturer1.2.0 release notes. No battery, USB bus power, instrument capture loading or mobile editor is inferred.\n\n[Exact Shopee hardware offer](https://shopee.co.id/Efek-Vocal-Audota-AVE-100-Vocal-Multi-Effects-Processor-i.198150809.56354336751),shop198150809/item56354336751,Red Musik Bali,Kota Denpasar,again exposes **Rp2.390.000,Habis** through indexed reopening. It is historical retail asking evidence; late-delivery compensation is not a purchase discount. No authenticated checkout/stock, condition grade, accessory/warranty region, delivered charges or used offer established.\n\nComplete original manufacturer manual identity and prior visual-inspection qualifications remain above; no new PDF rendering or file download performed. Remaining: firmware mode allocation, setting retention, USB channel/rate/driver details, battery/bus-power confirmation and qualified current local used/new availability. AVE-100 remains vocal-only and does not inherit AME-100 ownership. All five recorded Audota models are now root-canonical; technical verification and broader market discovery remain incomplete.\n'
    old_count, old_legacy = state['canonical_root_model_count'],state['legacy_only_model_count']
    state['root_brand_content'][brand_file].append(model)
    state['canonical_root_model_count'] += 1
    state['legacy_only_model_count'] -= 1
    state['consolidation_and_price_findings'].append(dict(models=['Audota AVE-100'],model_name=model,brand='Audota',destination=brand_file+'#ave-100',source=source_path,checked_date='2026-10-17',verification_kind='complete-source-body-v1',source_sha256=digest(source),marker=prefix,renamed_references=refs,retained_comparison_facts=extra,retained_context=contexts,retained_source_urls=[],supporting_sources=shared,supporting_source_hashes={p:digest((ROOT/p).read_text()) for p in shared},status='Complete AVE finding and supporting vocal rows retained;1.2.0 notes,65s looper and sold-out Shopee quote rechecked; vocal-only/no ownership inference preserved.'))
    state['migration']['warning'] = f'{old_legacy-1} legacy-only models remain;{old_count+1} root-canonical. Full migration and research incomplete.'
    state['cursor'].update(model='Boin Audio BG300 — complete legacy consolidation',task='Read complete BG300 finding and all supporting comparisons. Consolidate losslessly into root BOIN-AUDIO.md, preserving exact model/source identity, power, firmware, ports, prices and unknowns. Check primary and exact Shopee evidence; commit before next model. Continue remaining legacy consolidation, fresh discovery and unresolved fields.',after_queue=f'Continue unresolved-field checks and lossless consolidation of {old_legacy-1} legacy-only models.')
    readme=(ROOT/'README.md').read_text().replace(f'{old_count} detailed',f'{old_count+1} detailed').replace(f'{old_legacy} still rely',f'{old_legacy-1} still rely')
    readme=readme.replace('| [AUDOTA.md](AUDOTA.md) |AME-100,AME-200,AME-200 Pro,ACE-100 |','| [AUDOTA.md](AUDOTA.md) |AME-100,AME-200,AME-200 Pro,ACE-100,AVE-100 |')
    multi=(ROOT/'MULTI-EFFECTS.md').read_text().replace(f'{old_count} root-canonical',f'{old_count+1} root-canonical')
    outputs={brand_file:(ROOT/brand_file).read_text().replace('AME-100, standard AME-200, AME-200 Pro and ACE-100 are consolidated below. Other recorded Audota models still need their complete root-brand merge. Research remains partial.','All five recorded Audota models are consolidated below: AME-100, standard AME-200, AME-200 Pro, ACE-100 and vocal-only AVE-100. Technical research and market coverage remain partial.')+section,'README.md':readme,'MULTI-EFFECTS.md':multi,'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n'}
    inputs={p:digest((ROOT/p).read_text()) for p in ['README.md','MULTI-EFFECTS.md','research-state.json',source_path]+shared}
    inputs[brand_file]=digest((ROOT/brand_file).read_text())
    payload=dict(model_id='ave-100',model=model,inputs=inputs,outputs=outputs,new_files=[],rollback_commit=research_tools.git('rev-parse','HEAD').strip())
    PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print('Preview AVE-100 exact writes: '+', '.join(outputs)+f'; canonical {old_count}->{old_count+1}; legacy {old_legacy}->{old_legacy-1}; active unchanged; rollback '+payload['rollback_commit'])
    print('Plan saved: '+str(PLAN))

def plan_bg300():
    research_tools.identity()
    model, source_path = MODELS['bg300']
    brand_file = 'BOIN-AUDIO.md'
    assert not (ROOT/brand_file).exists()
    assert model not in json.loads((ROOT/'research-state.json').read_text())['root_brand_content'].get(brand_file, [])
    state_text = (ROOT/'research-state.json').read_text()
    state = json.loads(state_text)
    comparison = json.loads(Path('/tmp/instrumentfx-comparison-plan.json').read_text())
    assert comparison['ledger_hash'] == digest(state_text)
    record = comparison['records']['Boin Audio::BG300']
    assert record['link'] == source_path
    source = research_tools.read_preserved_source(source_path)
    prefix = 'AUDOTA-BG300'
    body, refs = preserved_body(source, prefix)
    normalizations={'(../README.md)':'(README.md)','(../shopee-indonesia.md)':'(effects/shopee-indonesia.md)','(../RESUME.md)':'(effects/RESUME.md)'}
    for old,new in normalizations.items():
        body=body.replace(old,new)
    extra = [f for f in record['facts'] if f['source'] != source_path]
    shared = sorted({f['source'] for f in extra})
    assert shared == ['effects/shopee-multifx-2.md']
    supporting = (ROOT/shared[0]).read_text()
    contexts = [p for p in supporting.split('\n\n') if p.startswith('**8 new partial') or p.startswith('Dimensions are') or p.startswith('These are separate') or p.startswith('No diagonal') or p.startswith('Counts include') or p.startswith('The individual notes retain')]
    section = '# Boin Audio multi-effects\n\n## BG300\n\nConsolidated **2026-10-17**. **Revision not established:** the linked firmware1.1.0 manual is a documented profile, not confirmation that every BG300 listing supplies matching hardware. Retailer and manual display/power/port/algorithm conflicts remain open.\n\n<!-- '+prefix+' source begins -->\n'+body+'<!-- '+prefix+' source ends -->\n\n### Preserved supporting comparison evidence\n\nHistorical catalogue counts below are superseded.\n\n'+'\n\n'.join(contexts)+'\n\n'
    for f in extra:
        section += '- **'+f['field']+'** ('+f['context']+'): '+f['value']+'\n'
    section += '\nSources: [Original finding]('+source_path+'), [Complete supporting comparison](effects/shopee-multifx-2.md). No source or incoming link removed.\n\n<!-- comparison evidence begins -->\n\n### Current BG300 comparison fields\n\nAll technical values below remain the linked-manual profile pending actual hardware/revision confirmation.\n\n| Field | Evidence / qualification |\n|---|---|\n'
    for f in record['facts']:
        if f['source'] != source_path or f['field'] in ('Follow-up technical correction','IDR qualified observations'):
            continue
        value=f['value']
        field=f['field']
        if field == 'Other features':
            field='Other relevant features'
        if field == 'Display':
            value += ' Retailer still advertises1.77-inch TFT; linked manual1.7-inch LCD retained as revision conflict.'
        if field == 'Power / battery':
            value += ' Retailer9V socket/DC-power claim remains conflicting, not added to this manual profile.'
        if field == 'Choices per category':
            value += ' Retailer70-effects/10-cab claims remain unresolved against manual64/15.'
        section += '| '+field+' | '+value+' |\n'
    section += '| Used IDR | ? — no condition-qualified used hardware offer established. |\n| New / retail IDR | **Rp1.749.990**, [Primanada exact With Battery offer](https://shopee.co.id/Boin-Audio-BG300-Efek-Gitar-Bass-BG-300-With-Battery-i.15931156.48853835827),shop15931156/item48853835827,Kota Jakarta Utara, indexed reopening2026-10-17. Exact condition grade, hardware revision, checkout stock, accessory bundle, warranty region, delivered charges and voucher eligibility unverified. Relative delivery/activity is not stock confirmation; late-delivery compensation not a purchase discount. Historical ask, not a completed sale. |\n\n<!-- comparison evidence ends -->\n\n### Current source review and unresolved identity\n\nChecked **2026-10-17**: [Boin Audio manufacturer](https://www.boinaudio.com/en/) still names BG200/300/400, confirms portable multi-effects/pedal family identity and offers a download center without extracted model-specific file links. This does not identify a hardware revision or establish identical siblings. No automotive BOSS Audio or unrelated OEM specifications substituted.\n\n[Nafiri BG300 page](https://nafiriguitar.com/products/boin-audio-bg300-guitar-multi-effects-processor) still points to its firmware1.1.0 manual. Retailer description retains1.77-inch TFT,70 effects,10 cabs,512-point IR,9V input and looper claims that differ from the preserved linked-manual profile. Its Android/PC/Mac/ASIO download link does not independently establish app identity/version or current OS compatibility. Original manual cover identity and earlier visual-inspection qualifications remain above; no PDF file downloaded or rendering repeated in this pass.\n\nSeparate non-Shopee asking observation rechecked2026-10-17: Nafiri **Rp1.500.000**, with both Sold out and Add to cart text. This is historical retailer evidence, not an active range with the Shopee quote, nor proof of a matching revision or completed sale. Full original dated quotes and URLs remain preserved above.\n\nThe exact Primanada Shopee listing reopened at the same1.749.990 amount and identifies Jakarta Utara. Seller title says guitar/bass and With Battery, but seller wording does not independently verify bass capability or revision. BG300 is not newly added to bass membership on that basis. Unresolved: actual panel/firmware/manual match, power/ports/headphone/display/algorithm-count contradictions, IR format/length,NAM/captures, current editor identity, looper/rhythm/scenes/trails and used/current-stock pricing.\n'
    old_count, old_legacy = state['canonical_root_model_count'],state['legacy_only_model_count']
    state['root_brand_content'][brand_file] = [model]
    state['canonical_root_model_count'] += 1
    state['legacy_only_model_count'] -= 1
    state['consolidation_and_price_findings'].append(dict(models=['Boin Audio BG300'],model_name=model,brand='Boin Audio',destination=brand_file+'#bg300',source=source_path,checked_date='2026-10-17',verification_kind='complete-source-body-v1',source_sha256=digest(source),marker=prefix,renamed_references=refs,retained_comparison_facts=extra,retained_context=contexts,retained_source_urls=[],supporting_sources=shared,supporting_source_hashes={p:digest((ROOT/p).read_text()) for p in shared},link_normalizations=normalizations,status='Complete BG300 finding and supporting fields retained; manual-profile revision/display/power/I-O/count conflicts and qualified Shopee/local asks preserved.'))
    state['migration']['warning'] = f'{old_legacy-1} legacy-only models remain;{old_count+1} root-canonical. Full migration and research incomplete.'
    state['cursor'].update(model='Scorpion KMF-10 — complete legacy consolidation',task='Read complete KMF-10 finding and supporting comparisons; consolidate losslessly into root SCORPION.md. Preserve brand-source conflicts, power/current/preset uncertainties and exact prices/URLs. Check primary and Shopee evidence; commit before next model. Continue remaining legacy records, fresh discovery and unresolved fields.',after_queue=f'Continue unresolved-field checks and lossless consolidation of {old_legacy-1} legacy-only models.')
    readme=(ROOT/'README.md').read_text().replace(f'{old_count} detailed',f'{old_count+1} detailed').replace(f'{old_legacy} still rely',f'{old_legacy-1} still rely')
    readme=readme.replace('| [JOYO.md](JOYO.md)', '| [BOIN-AUDIO.md](BOIN-AUDIO.md) |BG300 |\n| [JOYO.md](JOYO.md)')
    multi=(ROOT/'MULTI-EFFECTS.md').read_text().replace(f'{old_count} root-canonical',f'{old_count+1} root-canonical')
    outputs={brand_file:section,'README.md':readme,'MULTI-EFFECTS.md':multi,'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n'}
    inputs={p:digest((ROOT/p).read_text()) for p in ['README.md','MULTI-EFFECTS.md','research-state.json',source_path]+shared}
    inputs[brand_file]=None
    payload=dict(model_id='bg300',model=model,inputs=inputs,outputs=outputs,new_files=[brand_file],rollback_commit=research_tools.git('rev-parse','HEAD').strip())
    PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print('Preview BG300 exact writes: '+', '.join(outputs)+f'; canonical {old_count}->{old_count+1}; legacy {old_legacy}->{old_legacy-1}; active unchanged; rollback '+payload['rollback_commit'])
    print('Plan saved: '+str(PLAN))

def plan_kmf10():
    research_tools.identity()
    model, source_path = MODELS['kmf-10']
    brand_file = 'SCORPION.md'
    assert not (ROOT/brand_file).exists()
    assert model not in json.loads((ROOT/'research-state.json').read_text())['root_brand_content'].get(brand_file, [])
    state_text = (ROOT/'research-state.json').read_text()
    state = json.loads(state_text)
    comparison = json.loads(Path('/tmp/instrumentfx-comparison-plan.json').read_text())
    assert comparison['ledger_hash'] == digest(state_text)
    record = comparison['records']['Scorpion::KMF-10']
    assert record['link'] == source_path
    source = research_tools.read_preserved_source(source_path)
    prefix = 'SCORPION-KMF-10'
    body, refs = preserved_body(source, prefix)
    normalizations={'(../README.md)':'(README.md)','(../shopee-indonesia.md)':'(effects/shopee-indonesia.md)','(../RESUME.md)':'(effects/RESUME.md)'}
    for old,new in normalizations.items():
        body=body.replace(old,new)
    extra = [f for f in record['facts'] if f['source'] != source_path]
    shared = sorted({f['source'] for f in extra})
    assert shared == ['effects/shopee-multifx-2.md']
    supporting = (ROOT/shared[0]).read_text()
    contexts = [p for p in supporting.split('\n\n') if p.startswith('**8 new partial') or p.startswith('Dimensions are') or p.startswith('These are separate') or p.startswith('No diagonal') or p.startswith('Counts include') or p.startswith('The individual notes retain')]
    section = '# Scorpion multi-effects\n\n## KMF-10\n\nConsolidated **2026-10-17**. Complete original brand-based record and supporting model facts retained;300mA/500mA power,10–59 preset notation and amp/cab wording remain unresolved. No sibling/OEM specifications substituted.\n\n<!-- '+prefix+' source begins -->\n'+body+'<!-- '+prefix+' source ends -->\n\n### Preserved supporting comparison evidence\n\nHistorical catalogue counts below are superseded.\n\n'+'\n\n'.join(contexts)+'\n\n'
    for f in extra:
        section += '- **'+f['field']+'** ('+f['context']+'): '+f['value']+'\n'
    section += '\nSources: [Original finding]('+source_path+'), [Complete supporting comparison](effects/shopee-multifx-2.md). No legacy source or incoming link removed.\n\n<!-- comparison evidence begins -->\n\n### Current KMF-10 comparison fields\n\nTechnical observation dates remain2026-10-14; inaccessible brand sources are not newly verified today.\n\n| Field | Evidence and qualification |\n|---|---|\n'
    for f in record['facts']:
        if f['source'] != source_path or f['field'].startswith('Follow-up') or f['field'] == 'IDR qualified observations':
            continue
        field=f['field']
        if field == 'Other features':
            field='Other relevant features'
        if field == 'External control / loops':
            field='External control / loop ports'
        section += '| '+field+' | '+f['value']+' |\n'
    section += '| Used IDR | ? — no condition-qualified used hardware offer established. |\n| New / retail IDR | **Rp1.350.000**, [Imagination Music Store exact hardware](https://shopee.co.id/Scorpion-KMF10-KMF-10-KMF-10-Multi-Effect-Guitar-Processor-i.19576516.44201903491),shop19576516/item44201903491,Kota Jakarta Pusat, indexed reopening checked2026-10-17. Historical asking evidence, not a completed sale or live-stock guarantee. Detailed condition, accessory bundle, warranty region, shipping/tax and voucher eligibility unverified. Relative delivery/activity is not checkout confirmation; late-delivery compensation is not a purchase discount. |\n\n<!-- comparison evidence ends -->\n\n### Current access and unresolved fields\n\nChecked **2026-10-17**: both [brand product/specification page](https://scorpionguitar.com/products/scorpion-kmf10-multi-effect-guitar-pedal) and [brand series page](https://scorpionguitar.com/pages/multi-effect) failed direct opening. The complete original record retains its brand photographs, prior visual-control evidence, six-AA compartment,500mA rear marking versus300mA specification and ambiguous10–59 memory notation. No new hardware/PDF inspection, preset arithmetic or invented firmware explanation is claimed. Published screen diagonal/technology/touch remain unknown; USB connector presence establishes neither power nor recording nor editing.\n\n[Exact Shopee item](https://shopee.co.id/Scorpion-KMF10-KMF-10-KMF-10-Multi-Effect-Guitar-Processor-i.19576516.44201903491) reopened at the same1.350.000 ask and identifies Imagination Music Store,Kota Jakarta Pusat. No price range is constructed from another model, guessed used discount or foreign currency. Seller title does not replace brand technical evidence.\n\nThe complete original finding, source URLs, earlier image-verification qualifications and comparison contexts remain above. No dependencies or files downloaded. Remaining: model-specific original manual, exact preset organization, power-current distinction, output/AUX wiring, battery inclusion/clearance, toe mechanism, IR loading versus factory IR,NAM/capture workflow, editor/USB functions, scenes/trails and current qualified used/new checkout evidence. All records remain partial.\n'
    old_count, old_legacy = state['canonical_root_model_count'],state['legacy_only_model_count']
    state['root_brand_content'][brand_file] = [model]
    state['canonical_root_model_count'] += 1
    state['legacy_only_model_count'] -= 1
    state['consolidation_and_price_findings'].append(dict(models=['Scorpion KMF-10'],model_name=model,brand='Scorpion',destination=brand_file+'#kmf-10',source=source_path,checked_date='2026-10-17',verification_kind='complete-source-body-v1',source_sha256=digest(source),marker=prefix,renamed_references=refs,retained_comparison_facts=extra,retained_context=contexts,retained_source_urls=[],supporting_sources=shared,supporting_source_hashes={p:digest((ROOT/p).read_text()) for p in shared},link_normalizations=normalizations,status='Complete KMF-10 finding and supporting fields retained; brand access unavailable on refresh; exact Shopee ask rechecked; power/preset/amp-cab/USB uncertainty preserved.'))
    state['migration']['warning'] = f'{old_legacy-1} legacy-only models remain;{old_count+1} root-canonical. Full migration and research incomplete.'
    state['cursor'].update(model='TC-Helicon VoiceLive Play — complete legacy consolidation',task='Read complete VoiceLive Play finding and all supporting comparisons. Consolidate losslessly into root TC-HELICON.md. Preserve original firmware model counts, looper/display/memory/power uncertainties, exact URLs and price qualifications. Check primary and Shopee evidence; commit before next model. Continue Play Acoustic and other remaining legacy records, fresh discovery and unresolved fields.',after_queue=f'Continue unresolved-field checks and lossless consolidation of {old_legacy-1} legacy-only models.')
    readme=(ROOT/'README.md').read_text().replace(f'{old_count} detailed',f'{old_count+1} detailed').replace(f'{old_legacy} still rely',f'{old_legacy-1} still rely')
    readme=readme.replace('| [JOYO.md](JOYO.md)', '| [SCORPION.md](SCORPION.md) |KMF-10 |\n| [JOYO.md](JOYO.md)')
    multi=(ROOT/'MULTI-EFFECTS.md').read_text().replace(f'{old_count} root-canonical',f'{old_count+1} root-canonical')
    outputs={brand_file:section,'README.md':readme,'MULTI-EFFECTS.md':multi,'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n'}
    inputs={p:digest((ROOT/p).read_text()) for p in ['README.md','MULTI-EFFECTS.md','research-state.json',source_path]+shared}
    inputs[brand_file]=None
    payload=dict(model_id='kmf-10',model=model,inputs=inputs,outputs=outputs,new_files=[brand_file],rollback_commit=research_tools.git('rev-parse','HEAD').strip())
    PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print('Preview KMF-10 exact writes: '+', '.join(outputs)+f'; canonical {old_count}->{old_count+1}; legacy {old_legacy}->{old_legacy-1}; active unchanged; rollback '+payload['rollback_commit'])
    print('Plan saved: '+str(PLAN))

def plan_voiceliveplay():
    research_tools.identity()
    model, source_path = MODELS['voicelive-play']
    brand_file = 'TC-HELICON.md'
    assert not (ROOT/brand_file).exists()
    assert model not in json.loads((ROOT/'research-state.json').read_text())['root_brand_content'].get(brand_file, [])
    state_text = (ROOT/'research-state.json').read_text()
    state = json.loads(state_text)
    comparison = json.loads(Path('/tmp/instrumentfx-comparison-plan.json').read_text())
    assert comparison['ledger_hash'] == digest(state_text)
    record = comparison['records']['TC-Helicon::VoiceLive Play']
    assert record['link'] == source_path
    source = research_tools.read_preserved_source(source_path)
    prefix = 'SCORPION-VoiceLive Play'
    body, refs = preserved_body(source, prefix)
    normalizations={'(../README.md)':'(README.md)','(../shopee-indonesia.md)':'(effects/shopee-indonesia.md)','(../RESUME.md)':'(effects/RESUME.md)'}
    for old,new in normalizations.items():
        body=body.replace(old,new)
    extra = [f for f in record['facts'] if f['source'] != source_path]
    shared = sorted({f['source'] for f in extra})
    assert shared == ['effects/shopee-multifx-2.md']
    supporting = (ROOT/shared[0]).read_text()
    contexts = [p for p in supporting.split('\n\n') if p.startswith('**8 new partial') or p.startswith('Dimensions are') or p.startswith('These are separate') or p.startswith('No diagonal') or p.startswith('Counts include') or p.startswith('The individual notes retain')]
    section = '# TC-Helicon multi-effects\n\n## VoiceLive Play\n\nBlue VoiceLive Play vocal processor, not GTX or Play Acoustic. Consolidated **2026-10-17**; complete original findings and supporting facts retain their original technical dates. Current firmware remains unverified.\n\n<!-- '+prefix+' source begins -->\n'+body+'<!-- '+prefix+' source ends -->\n\n### Preserved supporting comparison evidence\n\nHistorical catalogue totals below are superseded.\n\n'+'\n\n'.join(contexts)+'\n\n'
    for f in extra:
        section += '- **'+f['field']+'** ('+f['context']+'): '+f['value']+'\n'
    section += '\nSources: [Original finding]('+source_path+'), [Complete supporting comparison](effects/shopee-multifx-2.md). No source or incoming link removed.\n\n<!-- comparison evidence begins -->\n\n### Current VoiceLive Play comparison fields\n\nOriginal manualv1.0 technical context remains explicit; current firmware is not assumed identical.\n\n| Field | Evidence and qualification |\n|---|---|\n'
    mapping={'Other useful features':'Other relevant features','Control/data':'Control/data ports','Harmony / special sounds':'Synth / acoustic and vocal special sounds'}
    for f in record['facts']:
        if f['source'] != source_path or f['field'].startswith('Follow-up') or f['field']=='IDR qualified observations':
            continue
        section += '| '+mapping.get(f['field'],f['field'])+' | '+f['value']+' |\n'
    section += '| Used IDR | ? — no condition-qualified local used offer established. |\n| New / retail IDR | **Rp5.280.000,Habis**, [Asia Pro Sound exact blue VoiceLive Play listing](https://shopee.co.id/TC-Helicon-VoiceLive-Play-Guitar-Effects-i.703046367.26030546305),shop703046367/item26030546305,Kota Bekasi, indexed reopening2026-10-17. Historical sold-out hardware ask, not completed sale or current available stock. Seller title says Guitar Effects but does not establish guitar processing. Condition, accessory bundle, warranty region, delivered charges and voucher eligibility unverified; late-delivery compensation is not a purchase discount. |\n\n<!-- comparison evidence ends -->\n\n### Current access and unresolved fields\n\nChecked **2026-10-17**: [manufacturer model-code page](https://www.tcelectronic.com/tcelectronic/product?modelCode=0726-AAZ) remained inaccessible. A [Music Tribe-hosted original manual lead](https://cdn.mediavalet.com/aunsw/musictribe/UdE6-mBzr0u6TqC_r6vYEw/f65JG-Kc9EWdWD5StvC6ig/Original/VOICELIVE%20PLAY_M_EN.pdf) failed to open. Its searchable title does not establish complete contents or a newer firmware revision. [Electori model-page lead](https://mail.electori.co.jp/tc-helicon/vocal/voicelive_play.php) timed out. Retailer dimensions surfaced in search but were not adopted as independently verified manufacturer specifications; no sibling enclosure dimensions borrowed.\n\nThe exact Shopee item reopened with the same5.280.000 sold-out ask and identifies Asia Pro Sound,Kota Bekasi. Relative delivery text does not override Habis. Old quote dates remain preserved, and no used-price estimate or exchange-rate conversion was created.\n\nOriginal v1.0 manual and VoiceSupport reference identities, complete source URLs, earlier visual-inspection qualifications,15/30-second undo-dependent looper limits, style counts and librarian/updater distinction remain preserved above. No files or dependencies downloaded; no new PDF image inspection claimed. Remaining: matching current firmware release/looper limit, total/factory/user memories, model-specific dimensions/mass, display diagonal/color/touch, phantom voltage/current, power polarity/battery/bus operation, USB channel/rate and present OS/editor compatibility, plus qualified current local offers. Vocal-only inclusion remains; GTX/Play Acoustic are separate models.\n'
    old_count, old_legacy = state['canonical_root_model_count'],state['legacy_only_model_count']
    state['root_brand_content'][brand_file] = [model]
    state['canonical_root_model_count'] += 1
    state['legacy_only_model_count'] -= 1
    state['consolidation_and_price_findings'].append(dict(models=['TC-Helicon VoiceLive Play'],model_name=model,brand='TC-Helicon',destination=brand_file+'#voicelive-play',source=source_path,checked_date='2026-10-17',verification_kind='complete-source-body-v1',source_sha256=digest(source),marker=prefix,renamed_references=refs,retained_comparison_facts=extra,retained_context=contexts,retained_source_urls=[],supporting_sources=shared,supporting_source_hashes={p:digest((ROOT/p).read_text()) for p in shared},link_normalizations=normalizations,status='Complete VoiceLive Play finding/supporting rows retained; v1.0 firmware context preserved; manufacturer access limited and exact sold-out Shopee ask rechecked.'))
    state['migration']['warning'] = f'{old_legacy-1} legacy-only models remain;{old_count+1} root-canonical. Full migration and research incomplete.'
    state['cursor'].update(model='TC-Helicon Play Acoustic — complete legacy consolidation',task='Read complete Play Acoustic finding and supporting comparisons. Merge losslessly into TC-HELICON.md, preserving distinct guitar/vocal paths, BodyRez meaning, global guitar settings, firmware/looper/model-count conflicts and all source/price qualifications. Check primary and exact Shopee evidence; commit before another model. Continue remaining legacy records, discovery and unresolved fields.',after_queue=f'Continue unresolved-field checks and lossless consolidation of {old_legacy-1} legacy-only models.')
    readme=(ROOT/'README.md').read_text().replace(f'{old_count} detailed',f'{old_count+1} detailed').replace(f'{old_legacy} still rely',f'{old_legacy-1} still rely')
    readme=readme.replace('| [JOYO.md](JOYO.md)', '| [TC-HELICON.md](TC-HELICON.md) |VoiceLive Play |\n| [JOYO.md](JOYO.md)')
    multi=(ROOT/'MULTI-EFFECTS.md').read_text().replace(f'{old_count} root-canonical',f'{old_count+1} root-canonical')
    outputs={brand_file:section,'README.md':readme,'MULTI-EFFECTS.md':multi,'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n'}
    inputs={p:digest((ROOT/p).read_text()) for p in ['README.md','MULTI-EFFECTS.md','research-state.json',source_path]+shared}
    inputs[brand_file]=None
    payload=dict(model_id='voicelive-play',model=model,inputs=inputs,outputs=outputs,new_files=[brand_file],rollback_commit=research_tools.git('rev-parse','HEAD').strip())
    PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print('Preview VoiceLive Play exact writes: '+', '.join(outputs)+f'; canonical {old_count}->{old_count+1}; legacy {old_legacy}->{old_legacy-1}; active unchanged; rollback '+payload['rollback_commit'])
    print('Plan saved: '+str(PLAN))

def plan_playacoustic():
    research_tools.identity()
    model, source_path = MODELS['play-acoustic']
    brand_file = 'TC-HELICON.md'
    assert (ROOT/brand_file).exists()
    assert model not in json.loads((ROOT/'research-state.json').read_text())['root_brand_content'][brand_file]
    assert model not in json.loads((ROOT/'research-state.json').read_text())['root_brand_content'].get(brand_file, [])
    state_text = (ROOT/'research-state.json').read_text()
    state = json.loads(state_text)
    comparison = json.loads(Path('/tmp/instrumentfx-comparison-plan.json').read_text())
    assert comparison['ledger_hash'] == digest(state_text)
    record = comparison['records']['TC-Helicon::Play Acoustic']
    assert record['link'] == source_path
    source = research_tools.read_preserved_source(source_path)
    prefix = 'TCHELICON-PLAY-ACOUSTIC'
    body, refs = preserved_body(source, prefix)
    normalizations={'(../README.md)':'(README.md)','(../shopee-indonesia.md)':'(effects/shopee-indonesia.md)','(../RESUME.md)':'(effects/RESUME.md)'}
    for old,new in normalizations.items():
        body=body.replace(old,new)
    extra = [f for f in record['facts'] if f['source'] != source_path]
    shared = sorted({f['source'] for f in extra})
    assert shared == ['effects/shopee-multifx-2.md']
    supporting = (ROOT/shared[0]).read_text()
    contexts = [p for p in supporting.split('\n\n') if p.startswith('**8 new partial') or p.startswith('Dimensions are') or p.startswith('These are separate') or p.startswith('No diagonal') or p.startswith('Counts include') or p.startswith('The individual notes retain')]
    section = '\n## Play Acoustic\n\nSeparate acoustic-guitar and vocal processor, not VoiceLive Play, Play Electric or GTX. Consolidated **2026-10-17**; complete original2014 firmware/manual context retained. BodyRez processing is not proof of IR import or electric-to-acoustic simulation.\n\n<!-- '+prefix+' source begins -->\n'+body+'<!-- '+prefix+' source ends -->\n\n### Preserved supporting comparison evidence\n\nHistorical catalogue totals below are superseded.\n\n'+'\n\n'.join(contexts)+'\n\n'
    for f in extra:
        section += '- **'+f['field']+'** ('+f['context']+'): '+f['value']+'\n'
    section += '\nSources: [Original finding]('+source_path+'), [Complete supporting comparison](effects/shopee-multifx-2.md). No legacy source or incoming link removed.\n\n<!-- comparison evidence begins -->\n\n### Current Play Acoustic comparison fields\n\nInspected original reference is firmware1.0/2014-05-09; later firmware behavior remains unresolved.\n\n| Field | Evidence and qualification |\n|---|---|\n'
    mapping={'Other features':'Other relevant features','Harmony / acoustic functions':'Synth / acoustic and harmony functions'}
    for f in record['facts']:
        if f['source'] != source_path or f['field'].startswith('Follow-up') or f['field']=='IDR qualified observations':
            continue
        section += '| '+mapping.get(f['field'],f['field'])+' | '+f['value']+' |\n'
    section += '| Used IDR | ? — no condition-qualified local used offer established. |\n| New / retail IDR | **Rp5.100.000**, [NEO MUSIC exact Play Acoustic hardware](https://shopee.co.id/TC-HELICON-PLAY-ACOUSTIC-3-Button-Vocal-and-Acoustic-Guitar-Effects-i.158235298.11220047810),shop158235298/item11220047810,Kota Sukabumi, indexed reopening checked2026-10-17. Exact condition grade, accessory bundle, warranty region, delivered charges, voucher eligibility and checkout stock unverified. Historical retail ask, not completed sale or guaranteed availability; relative delivery and late-delivery compensation are not a purchase discount or stock proof. |\n\n<!-- comparison evidence ends -->\n\n### Current source access and firmware lead\n\nChecked **2026-10-17**: [manufacturer model-code page](https://www.tcelectronic.com/tcelectronic/product?modelCode=0726-AAI) returned404. Official search indexed a [Music Tribe English reference manual](https://mediadl.musictribe.com/media/PLM/data/docs/P0DEF/M_TH_P0DEF_PLAY_ACOUSTIC_M.pdf) whose excerpt identifies **2014-07-16**, distinct from the inspected2014-05-09 source. Direct opening failed502, as did the [WW manual lead](https://mediadl.musictribe.com/media/PLM/data/docs/P0DEF/M_TH_0726-AAI_PLAY%20ACOUSTIC_WW.pdf). Search excerpts establish a lead, not full manual inspection or firmware behavior. Do not assign new guitar-preset storage, looper limits, memory counts or USB specifications from an inaccessible file.\n\nThe [exact NEO MUSIC Shopee listing](https://shopee.co.id/TC-HELICON-PLAY-ACOUSTIC-3-Button-Vocal-and-Acoustic-Guitar-Effects-i.158235298.11220047810) reopened at the same5.100.000 ask and identifies Kota Sukabumi. No authenticated checkout, condition, accessories, warranty or delivered-price verification; no used quote inferred. Original dated offer remains above.\n\nComplete original source body,URLs,firmware1.0 category/reverb-duplicate qualification, global guitar-setting limitation and undo-dependent15/30-second loop limits remain preserved. Those original observations do not establish current firmware behavior. BodyRez continues to mean acoustic-pickup EQ/compression/ambience, not user IR or synthesis. Distinct guitar reverb/modulation processing and vocal effects support membership in both guitar and vocal comparisons; the two rows do not add another unique model.\n\nNo files/dependencies downloaded or new PDF visual inspection performed. Remaining: accessible current official firmware/change notes, later manual comparison, preset/guitar-setting behavior, looper duration, factory/user split, screen diagonal/color/touch, USB channels/rates/drivers, power polarity/battery/bus operation, present VoiceSupport compatibility and qualified current local offers.\n'
    old_count, old_legacy = state['canonical_root_model_count'],state['legacy_only_model_count']
    state['root_brand_content'][brand_file].append(model)
    state['canonical_root_model_count'] += 1
    state['legacy_only_model_count'] -= 1
    state['consolidation_and_price_findings'].append(dict(models=['TC-Helicon Play Acoustic'],model_name=model,brand='TC-Helicon',destination=brand_file+'#play-acoustic',source=source_path,checked_date='2026-10-17',verification_kind='complete-source-body-v1',source_sha256=digest(source),marker=prefix,renamed_references=refs,retained_comparison_facts=extra,retained_context=contexts,retained_source_urls=[],supporting_sources=shared,supporting_source_hashes={p:digest((ROOT/p).read_text()) for p in shared},link_normalizations=normalizations,status='Complete Play Acoustic finding/supporting rows retained; inspected May2014 reference preserved, inaccessible July2014 official manual lead recorded; NEO exact ask rechecked.'))
    state['migration']['warning'] = f'{old_legacy-1} legacy-only models remain;{old_count+1} root-canonical. Full migration and research incomplete.'
    state['cursor'].update(model='CUVAVE H8 — complete legacy consolidation',task='Read complete H8 finding and supporting comparisons; consolidate losslessly in root CUVAVE.md, preserving CUVAVE versus M-VAVE brand/model distinctions, exact technical variants, source/price dates and unresolved fields. Check primary and Shopee evidence; commit before another model. Continue remaining VING FB-100/Roland GR-55 legacy records, fresh discovery and unresolved fields.',after_queue=f'Continue unresolved-field checks and lossless consolidation of {old_legacy-1} legacy-only models.')
    readme=(ROOT/'README.md').read_text().replace(f'{old_count} detailed',f'{old_count+1} detailed').replace(f'{old_legacy} still rely',f'{old_legacy-1} still rely')
    readme=readme.replace('| [TC-HELICON.md](TC-HELICON.md) |VoiceLive Play |','| [TC-HELICON.md](TC-HELICON.md) |VoiceLive Play,Play Acoustic |')
    multi=(ROOT/'MULTI-EFFECTS.md').read_text().replace(f'{old_count} root-canonical',f'{old_count+1} root-canonical')
    outputs={brand_file:(ROOT/brand_file).read_text()+section,'README.md':readme,'MULTI-EFFECTS.md':multi,'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n'}
    inputs={p:digest((ROOT/p).read_text()) for p in ['README.md','MULTI-EFFECTS.md','research-state.json',source_path]+shared}
    inputs[brand_file]=digest((ROOT/brand_file).read_text())
    payload=dict(model_id='play-acoustic',model=model,inputs=inputs,outputs=outputs,new_files=[],rollback_commit=research_tools.git('rev-parse','HEAD').strip())
    PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print('Preview Play Acoustic exact writes: '+', '.join(outputs)+f'; canonical {old_count}->{old_count+1}; legacy {old_legacy}->{old_legacy-1}; active unchanged; rollback '+payload['rollback_commit'])
    print('Plan saved: '+str(PLAN))

def plan_h8():
    research_tools.identity()
    model, source_path = MODELS['h8']
    brand_file = 'CUVAVE.md'
    assert not (ROOT/brand_file).exists()
    assert model not in json.loads((ROOT/'research-state.json').read_text())['root_brand_content'].get(brand_file, [])
    state_text = (ROOT/'research-state.json').read_text()
    state = json.loads(state_text)
    comparison = json.loads(Path('/tmp/instrumentfx-comparison-plan.json').read_text())
    assert comparison['ledger_hash'] == digest(state_text)
    record = comparison['records']['CUVAVE::H8']
    assert record['link'] == source_path
    source = research_tools.read_preserved_source(source_path)
    prefix = 'CUVAVE-H8'
    body, refs = preserved_body(source, prefix)
    normalizations={'(../README.md)':'(README.md)','(../shopee-indonesia.md)':'(effects/shopee-indonesia.md)','(../RESUME.md)':'(effects/RESUME.md)'}
    for old,new in normalizations.items():
        body=body.replace(old,new)
    extra = [f for f in record['facts'] if f['source'] != source_path]
    shared = sorted({f['source'] for f in extra})
    assert shared == ['effects/owned-multifx.md']
    supporting = (ROOT/shared[0]).read_text()
    contexts = [p for p in supporting.split('\n\n') if p.startswith('**Seven partial') or p.startswith('K/F/B means') or p.startswith('The original printed VING') or p.startswith('Older manuals') or p.startswith('Exact item/seller') or p.startswith('These five former')]
    original_commit='8c0bb751797bb3dfeca61849245a79393c032b63'
    assert original_commit in supporting
    section = '# CUVAVE multi-effects\n\n## H8\n\nCUVAVE/M-VAVE H8 headphone-format guitar multi-effects, not MINI-X or Pocket Amp. Consolidated **2026-10-17**; existing ownership retained without private receipts or another unique record.\n\n<!-- '+prefix+' source begins -->\n'+body+'<!-- '+prefix+' source ends -->\n\n### Preserved supporting comparison evidence\n\nHistorical counts and next-model notes below are provenance, not current totals/cursor.\n\n'+'\n\n'.join(contexts)+'\n\n'
    for f in extra:
        section += '- **'+f['field']+'** ('+f['context']+'): '+f['value']+'\n'
    section += '\nOriginal individual finding commit: '+original_commit+'. Sources: [Original finding]('+source_path+'), [Complete supporting comparison](effects/owned-multifx.md). No source or incoming link removed.\n\n<!-- comparison evidence begins -->\n\n### Current H8 comparison fields\n\n| Field | Evidence and qualification |\n|---|---|\n'
    for f in record['facts']:
        if f['source'] != source_path or f['field'].startswith('Follow-up'):
            continue
        value=f['value']
        if f['field']=='Software':
            value += ' Manufacturer download index rechecked2026-10-17 still explicitly lists H8 for desktop CubeSuite Windows/Mac; its mobile CubeSuite list does not name H8. No software installed.'
        if f['field']=='Retail IDR':
            value += ' Reopened2026-10-17: MICKEY MOUSE SHOP,Kota Jakarta Utara,same295.000/Habis,stale19–20August delivery; One Two Three Music Store,same city,same411.485,stale16–17September delivery. Earlier shop-holiday observations retain their original date; latest extraction does not expose that label. Neither proves current checkout stock.'
        section += '| '+f['field']+' | '+value+' |\n'
    section += '\n<!-- comparison evidence ends -->\n\n### Current primary-source review\n\nChecked **2026-10-17**: [Manufacturer downloads](https://www.m-vave.com/download) explicitly names H8 in desktop CubeSuite support with Windows/Mac links and USB connection. Its separate mobile CubeSuite list omits H8; this does not prove incompatibility but does not establish a mobile full editor. ANN/NAM tools elsewhere on that page are not assigned to H8. No executable/archive downloaded.\n\n[Sinco-authored H8 numbered manual text](https://manuals.plus/sinco-intelligent-technology/h8-multi-effects-headphone-guitar-amplifier-manual), FCC2ARCP-H8, publishedMarch2022, reopened with the same IR-loading/technical sections. It explicitly provides locations1–10, mic-distance adjustment, factory IR and factory-preset restore. Garbled mass1219 remains unusable as a verified measurement; USB/output subtype ambiguity is not silently repaired from OCR. No generated mirror FAQ used or original image inspection claimed.\n\n[Exact MICKEY MOUSE SHOP offer](https://shopee.co.id/Efek-Gitar-CUVAVE-H8-Multi-Effects-Soundcard-Headphone-Amplifier-Guitar-Pedal-Instrument-i.19700013.15896058200),shop19700013/item15896058200,Kota Jakarta Utara,again shows295.000/Habis. [Exact One Two Three Music Store offer](https://shopee.co.id/Efek-Gitar-CUVAVE-H8-Multi-Effects-Soundcard-Headphone-Amplifier-Guitar-Pedal-Instrument-i.1505062399.28235905225),shop1505062399/item28235905225,same city,again shows411.485. Both are indexed historical asks with stale delivery dates; no range, used-price inference or live-stock guarantee. Condition grade, accessory bundle,warranty region,delivered charges,vouchers and seller authenticity remain unverified. Late-delivery compensation is not a purchase discount.\n\nComplete original body and supporting facts retain all URLs,dates,ownership distinctions,garbled-weight warning and IR-versus-capture distinction. No files/dependencies downloaded. Remaining: original-image mass/connector verification,battery capacity,IR format/sample limits,USB channel/driver/OS details,current editor scope and qualified current local offers.\n'
    old_count, old_legacy = state['canonical_root_model_count'],state['legacy_only_model_count']
    state['root_brand_content'][brand_file] = [model]
    state['canonical_root_model_count'] += 1
    state['legacy_only_model_count'] -= 1
    state['consolidation_and_price_findings'].append(dict(models=['CUVAVE H8'],model_name=model,brand='CUVAVE',destination=brand_file+'#h8',source=source_path,checked_date='2026-10-17',verification_kind='complete-source-body-v1',source_sha256=digest(source),marker=prefix,renamed_references=refs,retained_comparison_facts=extra,retained_context=contexts,retained_source_urls=[],supporting_sources=shared,supporting_source_hashes={p:digest((ROOT/p).read_text()) for p in shared},link_normalizations=normalizations,status='Complete H8 finding and supporting facts retained; desktop CubeSuite support and separate qualified Shopee asks rechecked; weight/connector/mobile-editor gaps preserved.'))
    state['migration']['warning'] = f'{old_legacy-1} legacy-only models remain;{old_count+1} root-canonical. Full migration and research incomplete.'
    state['cursor'].update(model='VING Flybro FB-100 — complete legacy consolidation',task='Read full FB-100 finding and supporting owner comparison; consolidate losslessly in root VING.md. Preserve VING/Flybro identity,400/450g and power-source conflicts, shared FS/EXP socket, developer-app evidence and price discrepancies. Check primary and Shopee evidence; commit before next model. Then consolidate Roland GR-55 and continue fresh discovery/unresolved-field research.',after_queue=f'Continue unresolved-field checks and lossless consolidation of {old_legacy-1} legacy-only models.')
    readme=(ROOT/'README.md').read_text().replace(f'{old_count} detailed',f'{old_count+1} detailed').replace(f'{old_legacy} still rely',f'{old_legacy-1} still rely')
    readme=readme.replace('| [JOYO.md](JOYO.md)', '| [CUVAVE.md](CUVAVE.md) |H8 |\n| [JOYO.md](JOYO.md)')
    multi=(ROOT/'MULTI-EFFECTS.md').read_text().replace(f'{old_count} root-canonical',f'{old_count+1} root-canonical')
    outputs={brand_file:section,'README.md':readme,'MULTI-EFFECTS.md':multi,'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n'}
    inputs={p:digest((ROOT/p).read_text()) for p in ['README.md','MULTI-EFFECTS.md','research-state.json',source_path]+shared}
    inputs[brand_file]=None
    payload=dict(model_id='h8',model=model,inputs=inputs,outputs=outputs,new_files=[brand_file],rollback_commit=research_tools.git('rev-parse','HEAD').strip())
    PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print('Preview H8 exact writes: '+', '.join(outputs)+f'; canonical {old_count}->{old_count+1}; legacy {old_legacy}->{old_legacy-1}; active unchanged; rollback '+payload['rollback_commit'])
    print('Plan saved: '+str(PLAN))

def plan_fb100():
    research_tools.identity()
    model, source_path = MODELS['fb100']
    brand_file = 'VING.md'
    assert not (ROOT/brand_file).exists()
    assert model not in json.loads((ROOT/'research-state.json').read_text())['root_brand_content'].get(brand_file, [])
    state_text = (ROOT/'research-state.json').read_text()
    state = json.loads(state_text)
    comparison = json.loads(Path('/tmp/instrumentfx-comparison-plan.json').read_text())
    assert comparison['ledger_hash'] == digest(state_text)
    record = comparison['records']['VING::Flybro FB-100']
    assert record['link'] == source_path
    source = research_tools.read_preserved_source(source_path)
    prefix = 'VING-FB-100'
    body, refs = preserved_body(source, prefix)
    normalizations={'(../README.md)':'(README.md)','(../shopee-indonesia.md)':'(effects/shopee-indonesia.md)','(../RESUME.md)':'(effects/RESUME.md)'}
    for old,new in normalizations.items():
        body=body.replace(old,new)
    extra = [f for f in record['facts'] if f['source'] != source_path]
    shared = sorted({f['source'] for f in extra})
    assert shared == ['effects/owned-multifx.md']
    supporting = (ROOT/shared[0]).read_text()
    contexts = [p for p in supporting.split('\n\n') if p.startswith('**Seven partial') or p.startswith('K/F/B means') or p.startswith('The original printed VING') or p.startswith('Older manuals') or p.startswith('Exact item/seller') or p.startswith('These five former')]
    original_commit='7962a72f6ecc5864e54fd2437cad25ed93507a5b'
    assert original_commit in supporting
    section = '# VING multi-effects\n\n## Flybro FB-100\n\nVING/Flybro FB-100 desktop guitar multi-effects. Consolidated **2026-10-17**; full original model/revision identity,405g/450g and power-source conflicts retained. Shared manufacturer identity does not make this BG300.\n\n<!-- '+prefix+' source begins -->\n'+body+'<!-- '+prefix+' source ends -->\n\n### Preserved supporting comparison evidence\n\nHistorical counts and next notes below are provenance.\n\n'+'\n\n'.join(contexts)+'\n\n'
    for f in extra:
        section += '- **'+f['field']+'** ('+f['context']+'): '+f['value']+'\n'
    section += '\nOriginal individual finding commit: '+original_commit+'. Sources: [Original finding]('+source_path+'), [Complete supporting comparison](effects/owned-multifx.md). No legacy source or incoming link removed.\n\n<!-- comparison evidence begins -->\n\n### Current FB-100 comparison fields\n\n| Field | Evidence and qualification |\n|---|---|\n'
    for f in record['facts']:
        if f['source'] != source_path or f['field'].startswith('Follow-up'):
            continue
        value=f['value']
        if f['field']=='Apps':
            value += ' Rechecked2026-10-17: same editing/import functions and iOS/iPadOS12+ requirements. Mac compatibility specifies macOS11+/M1+, while listing says not verified for macOS; this is mobile-app compatibility, not a dedicated desktop editor.'
        if f['field']=='Retail IDR':
            value += ' Rechecked2026-10-17: first item exposes only a generic Shopee shell; original1.450.000 ask remains historical. Second item now shows1.860.000 with four unspecified variations and no Habis label in current extraction. Keep all snapshots; no verified variant-to-price mapping or checkout stock, and no current per-model range.'
        field={'Input':'Input ports','Outputs':'Output ports','USB / practice':'USB audio / practical features'}.get(f['field'],f['field'])
        section += '| '+field+' | '+value+' |\n'
    section += '\n<!-- comparison evidence ends -->\n\n### Current primary-source and price qualifications\n\nChecked **2026-10-17**: [Developer VING App Store listing](https://apps.apple.com/th/app/ving/id6740554685) still names preset parameter editing, preset import/export, IR import and drum rhythms. Minimum iOS/iPadOS12 remains explicit. macOS11+/M1+ compatibility applies to the mobile app; listing also says not verified for macOS. Provider identifies Zhuhai boyin Technology, while copyright identifies Shanghai Weiyin Technology; preserve these distinct labels without inventing a corporate/rebadge explanation. The [linked musicving site](https://musicving.com) again failed to open. No Android APK or separate desktop compatibility assumed.\n\n[SEVEN STEREO Malang original item](https://shopee.co.id/Ving-FB100-FB-100-%E2%80%93-Portable-Multi-Effects-Processor-dengan-Bluetooth-Speaker-i.1408254222.28741861094),shop1408254222/item28741861094,now exposes only a generic Shopee shell. Its earlier1.450.000 amount/date is retained, not newly verified. [queenmusicsolo exact listing](https://shopee.co.id/VING-FB100-VING-FLYBRO-FB100-MULTI-EFFECT-PROCESSOR-WITH-SPEAKER-BLUETOOTH-i.60582947.40872427417),shop60582947/item40872427417,Kota Surakarta,now displays **Rp1.860.000 with four unspecified variations**. Earlier1.565.000/Habis body and1.885.000 search snippet remain historical conflicting snapshots. Variation mapping,condition,accessories,regional warranty,checkout stock,shipping/tax and usable vouchers unverified. Exclude unresolved variation amount from a confirmed standard-hardware price range; late-delivery compensation not a purchase discount.\n\nComplete original quick-guide V03/2025-07-02 and testedV1.0 report identities, prior actual visual-inspection qualifications, shared FS/EXP socket, balanced-mono main versus stereo-headphone distinction,405/450g conflict and5V/12V source distinctions remain preserved. No new original-PDF visual verification or file/dependency downloads performed. Remaining: actual power negotiation/hardware-revision match, full category choices, IR capacity/format,NAM/capture compatibility, memory-overwrite rules, touch,USB channels,Android/dedicated desktop support and qualified current used/new offers.\n'
    old_count, old_legacy = state['canonical_root_model_count'],state['legacy_only_model_count']
    state['root_brand_content'][brand_file] = [model]
    state['canonical_root_model_count'] += 1
    state['legacy_only_model_count'] -= 1
    state['consolidation_and_price_findings'].append(dict(models=['VING Flybro FB-100'],model_name=model,brand='VING',destination=brand_file+'#flybro-fb-100',source=source_path,checked_date='2026-10-17',verification_kind='complete-source-body-v1',source_sha256=digest(source),marker=prefix,renamed_references=refs,retained_comparison_facts=extra,retained_context=contexts,retained_source_urls=[],supporting_sources=shared,supporting_source_hashes={p:digest((ROOT/p).read_text()) for p in shared},link_normalizations=normalizations,status='Complete FB-100 body/supporting facts retained; developer app verified and changed four-variation seller snapshot preserved; power/mass/IR/USB uncertainties remain.'))
    state['migration']['warning'] = f'{old_legacy-1} legacy-only models remain;{old_count+1} root-canonical. Full migration and research incomplete.'
    state['cursor'].update(model='Roland GR-55 — complete legacy consolidation',task='Read complete GR-55 original finding/corrections and supporting owner comparisons. Consolidate losslessly into root ROLAND.md; preserve GK/divided-pickup restrictions, guitar/bass firmware1.50 memory changes, exact processing counts and all source/price dates. Verify model-specific primary and exact Shopee evidence, update views and commit. Then audit entire root migration and continue fresh discovery/unresolved-field research; zero legacy-only count alone does not complete the full objective.',after_queue=f'Continue unresolved-field checks and lossless consolidation of {old_legacy-1} legacy-only models.')
    readme=(ROOT/'README.md').read_text().replace(f'{old_count} detailed',f'{old_count+1} detailed').replace(f'{old_legacy} still rely',f'{old_legacy-1} still rely')
    readme=readme.replace('| [JOYO.md](JOYO.md)', '| [VING.md](VING.md) |Flybro FB-100 |\n| [JOYO.md](JOYO.md)')
    multi=(ROOT/'MULTI-EFFECTS.md').read_text().replace(f'{old_count} root-canonical',f'{old_count+1} root-canonical')
    outputs={brand_file:section,'README.md':readme,'MULTI-EFFECTS.md':multi,'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n'}
    inputs={p:digest((ROOT/p).read_text()) for p in ['README.md','MULTI-EFFECTS.md','research-state.json',source_path]+shared}
    inputs[brand_file]=None
    payload=dict(model_id='fb100',model=model,inputs=inputs,outputs=outputs,new_files=[brand_file],rollback_commit=research_tools.git('rev-parse','HEAD').strip())
    PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print('Preview Flybro FB-100 exact writes: '+', '.join(outputs)+f'; canonical {old_count}->{old_count+1}; legacy {old_legacy}->{old_legacy-1}; active unchanged; rollback '+payload['rollback_commit'])
    print('Plan saved: '+str(PLAN))

def plan_gr55():
    research_tools.identity()
    model, source_path = MODELS['gr-55']
    brand_file = 'ROLAND.md'
    assert not (ROOT/brand_file).exists()
    assert model not in json.loads((ROOT/'research-state.json').read_text())['root_brand_content'].get(brand_file, [])
    state_text = (ROOT/'research-state.json').read_text()
    state = json.loads(state_text)
    comparison = json.loads(Path('/tmp/instrumentfx-comparison-plan.json').read_text())
    assert comparison['ledger_hash'] == digest(state_text)
    record = comparison['records']['Roland::GR-55']
    assert record['link'] == source_path
    source = research_tools.read_preserved_source(source_path)
    prefix = 'ROLAND-GR-55'
    body, refs = preserved_body(source, prefix)
    normalizations={'(../OWNERSHIP.md)':'(effects/OWNERSHIP.md)','(2026-10-14-zoom-b1xon.md)':'(ZOOM.md#b1xon)','(../README.md)':'(README.md)','(../shopee-indonesia.md)':'(effects/shopee-indonesia.md)','(../RESUME.md)':'(effects/RESUME.md)'}
    for old,new in normalizations.items():
        body=body.replace(old,new)
    extra = [f for f in record['facts'] if f['source'] != source_path]
    shared = sorted({f['source'] for f in extra})
    assert shared == ['effects/owned-multifx.md']
    supporting = (ROOT/shared[0]).read_text()
    contexts = [p for p in supporting.split('\n\n') if p.startswith('**Seven partial') or p.startswith('K/F/B means') or p.startswith('The original printed VING') or p.startswith('Older manuals') or p.startswith('Exact item/seller') or p.startswith('These five former')]
    original_commit='2b637fb61c243776b1a0a9d192ce17848295eeac'
    correction_commit='da9ff9bb01b8be8109f5b588c656de3daaf41c9c'
    assert original_commit in supporting and correction_commit in supporting
    section = '# Roland multi-effects\n\n## GR-55\n\nGuitar/bass synthesis and multi-effects with13-pin divided-pickup/GK system, not GM-800 Serial GK. Consolidated **2026-10-17**. Full original body and corrections retained; eligible owner history is separate from public specification/price evidence.\n\n<!-- '+prefix+' source begins -->\n'+body+'<!-- '+prefix+' source ends -->\n\n### Preserved supporting comparison evidence\n\nHistorical counts and next notes below are provenance.\n\n'+'\n\n'.join(contexts)+'\n\n'
    for f in extra:
        section += '- **'+f['field']+'** ('+f['context']+'): '+f['value']+'\n'
    section += '\nOriginal finding commit: '+original_commit+'; correction: '+correction_commit+'. Sources: [Original finding]('+source_path+'), [Complete supporting comparison](effects/owned-multifx.md). No original file or incoming link removed.\n\n<!-- comparison evidence begins -->\n\n### Current GR-55 comparison fields\n\n| Field | Evidence and qualification |\n|---|---|\n'
    mapping={'USB/audio extras':'USB audio / other relevant features','Other editors':'Other editor platforms','Acoustic simulation':'Acoustic simulation algorithms'}
    for f in record['facts']:
        if f['source'] != source_path or f['field'].startswith('Follow-up'):
            continue
        value=f['value']
        if f['field']=='Used IDR':
            value='**Rp7.500.000**, seller-labelled SECOND GR-55 **with GK3 pickup**: [HUTAURUK MUSIC exact offer](https://shopee.co.id/ROLAND-GR-55-DENGAN-PICK-UP-GK3-SECOND-ORIGINAL-i.190993829.22101819979),shop190993829/item22101819979,Kota Bekasi,indexed2026-10-17;stale21July delivery. Detailed condition,functionality,13-pin cable/adapter inclusion,warranty region,delivered charges,vouchers and current checkout stock unverified. Historical used-bundle ask,not a completed sale or bare-processor price.'
        if f['field']=='Effect architecture / choices':
            value += ' Roland US page rechecked2026-10-17 corroborates these counts; four source layers remain distinct from effect blocks.'
        if f['field']=='Presets / user memory':
            value += ' v1.50 release page rechecked2026-10-17 corroborates90 guitar/18 bass additions; MIDI program changes may select different patches after updating. No actual unit update performed.'
        section += '| '+mapping.get(f['field'],f['field'])+' | '+value+' |\n'
    section += '\n<!-- comparison evidence ends -->\n\n### Current primary-source and marketplace review\n\nChecked **2026-10-17**: [Roland US GR-55 page](https://www.roland.com/us/products/gr-55/) corroborates model-specific dimensions/mass,240×64 LCD,910 PCM tones,23/17 modeled guitar/bass types, published effects categories,9V700mA draw,PSB-1U supply and complete connector inventory. Its launch270/90 factory counts coexist with later firmware additions. Output and GUITAR OUT impedance2kΩ,nominal−10dBu. GK-included version explicitly supplies GK-3 and5m cable; do not assume every seller bundle does. Ordinary guitar input is through the divided-pickup system, not an added quarter-inch input.\n\n[Roland system1.50 release notes](https://www.roland.com/global/support/by_product/gr-55/updates_drivers/f64a41ce-c897-4fd5-94d7-71ec8ff6f036/) confirms90 guitar/18 bass preset additions and warns of MIDI program-change mapping differences. It also documents fixes for alternate-tuning MIDI notes,piezo sensitivity-meter display,USB-audio noise at high voice counts,PCM interruptions,drum tone levels,CTL/EXP-switch effect status and Librarian drum-kit patch silence. These are documented fixes,not tests on the owner unit. Firmware procedures do not establish new USB power or editor capabilities.\n\n[HUTAURUK MUSIC secondhand GK3 bundle](https://shopee.co.id/ROLAND-GR-55-DENGAN-PICK-UP-GK3-SECOND-ORIGINAL-i.190993829.22101819979) indexed at7.500.000 with old21July delivery; exact condition/stock/accessories remain unverified. Separate [Koko DC Musik Shop listing](https://shopee.co.id/efek-gitar-synthesizer-boss-roland-gr-55-black-hitam-gk3-keyboard-i.4074307.24802346959),shop4074307/item24802346959,Kab.Malang, **Rp7.250.000,Habis**,stale30June–2July delivery. Its title does not establish detailed condition or GK3/cable bundle contents; not classified as verified new or used. Neither is a confirmed transaction or current market range. Regional warranty,shipping/tax and voucher eligibility unknown; late-delivery compensation is not a discount.\n\nGlobal product URL timed out; US primary page provided the corroboration. No original control/signal-flow manual was newly inspected or firmware/software downloaded. Complete original sources and corrections remain above. Open fields: visually checked K/F/B/toe,explicit display diagonal/color/touch, acoustic modeling names,routing concurrency,PSU polarity/battery/bus power,looper duration,USB channels/bit depth,current librarian scope/OS support and condition-qualified new/current used availability.\n'
    old_count, old_legacy = state['canonical_root_model_count'],state['legacy_only_model_count']
    state['root_brand_content'][brand_file] = [model]
    state['canonical_root_model_count'] += 1
    state['legacy_only_model_count'] -= 1
    state['consolidation_and_price_findings'].append(dict(models=['Roland GR-55'],model_name=model,brand='Roland',destination=brand_file+'#gr-55',source=source_path,checked_date='2026-10-17',verification_kind='complete-source-body-v1',source_sha256=digest(source),marker=prefix,renamed_references=refs,retained_comparison_facts=extra,retained_context=contexts,retained_source_urls=[],supporting_sources=shared,supporting_source_hashes={p:digest((ROOT/p).read_text()) for p in shared},link_normalizations=normalizations,status='Complete GR-55 body/supporting facts/correction provenance retained; primary US specs and1.50 additions rechecked; seller-labelled used GK3 bundle qualified.'))
    state['migration']['warning'] = f'{old_legacy-1} legacy-only models remain;{old_count+1} root-canonical. Full migration and research incomplete.'
    state['cursor'].update(model='Full root migration audit and fresh discovery',task='All126 recorded models now have root-brand records; audit complete legacy-source preservation, incoming links, comparison field coverage and root layout against the full objective. Do not equate canonical count with verified specs or completed migration. Identify uncovered bodies/URLs/fields, repair omissions, then continue fresh Shopee discovery by brand/series and unresolved primary-field research one model per commit. Keep six excluded records and ownership boundaries.',after_queue='Audit migration and unresolved fields; fresh eligible Shopee discovery remains required. No legacy-only active model count does not mean obsolete source archives may be deleted.')
    readme=(ROOT/'README.md').read_text().replace(f'{old_count} detailed',f'{old_count+1} detailed').replace(f'{old_legacy} still rely',f'{old_legacy-1} still rely')
    readme=readme.replace('| [JOYO.md](JOYO.md)', '| [ROLAND.md](ROLAND.md) |GR-55 |\n| [JOYO.md](JOYO.md)')
    multi=(ROOT/'MULTI-EFFECTS.md').read_text().replace(f'{old_count} root-canonical',f'{old_count+1} root-canonical')
    outputs={brand_file:section,'README.md':readme,'MULTI-EFFECTS.md':multi,'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n'}
    inputs={p:digest((ROOT/p).read_text()) for p in ['README.md','MULTI-EFFECTS.md','research-state.json',source_path]+shared}
    inputs[brand_file]=None
    payload=dict(model_id='gr-55',model=model,inputs=inputs,outputs=outputs,new_files=[brand_file],rollback_commit=research_tools.git('rev-parse','HEAD').strip())
    PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print('Preview GR-55 exact writes: '+', '.join(outputs)+f'; canonical {old_count}->{old_count+1}; legacy {old_legacy}->{old_legacy-1}; active unchanged; rollback '+payload['rollback_commit'])
    print('Plan saved: '+str(PLAN))

def plan(model_id):
    if model_id == 'gr-55':
        return plan_gr55()
    if model_id == 'fb100':
        return plan_fb100()
    if model_id == 'h8':
        return plan_h8()
    if model_id == 'play-acoustic':
        return plan_playacoustic()
    if model_id == 'voicelive-play':
        return plan_voiceliveplay()
    if model_id == 'kmf-10':
        return plan_kmf10()
    if model_id == 'bg300':
        return plan_bg300()
    if model_id == 'ave-100':
        return plan_ave100()
    if model_id == 'ace-100':
        return plan_ace100()
    if model_id == 'ame-200-pro':
        return plan_ame200pro()
    if model_id == 'ame-200':
        return plan_ame200()
    if model_id == 'ame-100':
        return plan_ame100()
    if model_id == 'nano-cortex':
        return plan_nano_cortex()
    if model_id == 'tonex-pedal':
        return plan_tonex_pedal()
    if model_id == 'tonex-one':
        return plan_tonex_one()
    if model_id == 'hx-stomp':
        return plan_hx_stomp()
    if model_id == 'gp-200':
        return plan_gp200()
    research_tools.identity()
    model, source_path = MODELS[model_id]
    brand = 'Valeton' if model_id in ('gp-5', 'gp-50', 'gp-100', 'gp-150', 'gp-180', 'gp-200') else 'MOOER' if model_id in ('ge100-original','ge150-original','ge200-original','ge150-pro-li','ge100-pro','ge100-pro-li','ge200-pro','ge200-pro-li','ge150-pro','ge150-plus','ge150-plus-li','ge150-max','ge150-max-li','ge1000','ge1000-li') else 'Hotone' if model_id in ('ampero-mini','ampero-mp100','ampero-mp350','ampero-mp380','ampero-mp300') else 'Line 6' if model_id == 'hx-stomp-xl' else 'Zoom'
    brand_file = {'Valeton':'VALETON.md','MOOER':'MOOER.md','Hotone':'HOTONE.md','Line 6':'LINE6.md','Zoom':'ZOOM.md'}[brand]
    state = json.loads((ROOT / 'research-state.json').read_text())
    assert model not in state['root_brand_content'][brand_file], 'Already consolidated'
    comparison = json.loads(Path('/tmp/instrumentfx-comparison-plan.json').read_text())
    assert comparison['ledger_hash'] == digest((ROOT / 'research-state.json').read_text()), 'Run make comparison-plan first'
    record = comparison['records'][brand + '::' + model]
    assert record['link'] == source_path
    source = research_tools.read_preserved_source(source_path)
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
    if model_id in ('gp-5', 'gp-50', 'gp-100', 'gp-150', 'gp-180', 'gp-200'):
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
    if model_id in ('gp-5', 'gp-50', 'gp-100', 'gp-150', 'gp-180', 'gp-200'):
        zoom = zoom.replace('Existing GP-5/50/100/150/180/200 records remain', 'Existing GP-5/50/150/180/200 records remain')
        if model_id == 'gp-5':
            zoom = zoom.replace('Existing GP-5/50 records remain', 'Existing GP-50 records remain')
        if model_id == 'gp-180':
            zoom = zoom.replace('Existing GP-5/50/180 records remain', 'Existing GP-5/50 records remain')
        if model_id == 'gp-150':
            zoom = zoom.replace('Existing GP-5/50/150/180/200 records remain', 'Existing GP-5/50/180/200 records remain')
    if model_id == 'gp-50':
        zoom = zoom.replace('Root-level brand records. New evidence checked **2026-10-15**.', 'Root-level brand records. Evidence retains model-specific dates below.')
        zoom = zoom.replace('Existing GP-50 records remain in legacy files until their complete source-backed content is consolidated here; they are not counted again or deleted by this addition.', 'All eight recorded Valeton models are consolidated below, with GP-200X retained as a GP-200 anniversary variant. Technical verification and market discovery remain incomplete; original sources are retained.')
    zoom = re.sub(r'^The existing .+$', lambda m: m[0].replace(model + ',', '').replace(',' + model + ' records', ' records'), zoom, flags=re.M)
    section = '\n## ' + model + '\n\n'
    section += 'Consolidated 2026-10-17. The complete original observation below retains its technical date, prices, sources, contradictions and unknowns. This is a document consolidation, not a fresh stock or firmware verification. Historical next-model notes are provenance; use research-state.json for current work.\n\n'
    if model_id == 'gp-180':
        section = section.replace('This is a document consolidation, not a fresh stock or firmware verification.', 'NAM compatibility, published power requirements and qualified Shopee snapshots were additionally checked2026-10-17; checkout stock and complete firmware contents remain unverified.')
    if model_id in ('gp-5','gp-50'):
        section = section.replace('This is a document consolidation, not a fresh stock or firmware verification.', 'NAM compatibility and qualified Shopee snapshots were additionally checked2026-10-17; complete firmware contents and checkout stock remain unverified.')
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
    if model_id in ('gp-5', 'gp-50', 'gp-100', 'gp-150', 'gp-180', 'gp-200'):
        section += '\n### ' + model + (' comparison fields — dated evidence' if model_id in ('gp-5','gp-50','gp-180') else ' comparison fields from retained snapshot') + '\n\n| Field | Dated evidence |\n|---|---|\n'
        for fact in extra:
            if 'Archived foreign' not in fact['context']:
                value = fact['value'].replace('[F100]', '[detail](VALETON.md#gp-100)').replace('[F150]', '[detail](VALETON.md#gp-150)').replace('[F180]', '[detail](VALETON.md#gp-180)').replace('[F5]', '[detail](VALETON.md#gp-5)').replace('[F50]', '[detail](VALETON.md#gp-50)').replace('[controls]', '[controls](https://res.valeton.net/Uploads/wp/2026/03/GP-150-GP180-Comparison-2.png)')
                if model_id == 'gp-50' and fact['field'] == 'NAM / captured models':
                    value = '**SnapTone converted NAM**,80 model slots/50 supplied. **NAM A2 conversion requires hardware firmware1.1.0+ and mobile app2.1.0+**, explicitly named for GP-50 in the [official regional notice dated2026-08-18](https://www.hotone.jp/announcements/nama2allbrand), rechecked2026-10-17. Native NAM, exact supported A2 architectures and simultaneous capture limits remain unverified. Preserve older firmware1.0.5 manual context separately.'
                if model_id == 'gp-5' and fact['field'] == 'NAM / captured models':
                    value = '**SnapTone converted NAM**,80 model slots/50 supplied. **NAM A2 conversion requires mobile app2.1.0+**, explicitly named for GP-5 in the [official regional notice dated2026-08-18](https://www.hotone.jp/announcements/nama2allbrand), rechecked2026-10-17. Native NAM, exact supported A2 architectures, hardware firmware prerequisite and simultaneous capture limits remain unverified.'
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
        if model_id == 'gp-5':
            contexts = [p for p in shared_text.split('\n\n') if p.startswith('*GP-100 height') or p.startswith("GP-100's checked firmware") or p.startswith('These earlier observations were recorded') or p.startswith('P2 separately listed') or p.startswith('Prices are individual asking/listed observations') or p.startswith('**Availability warning:**')]
            urls = ['https://www.guitarcenter.com/Valeton/Multi-Effects-Pedals.gc','https://shop.valeton.net/products/gp-5']
            section += '''| New / retail Shopee IDR observations | Checked2026-10-17: [Asia Pro Sound](https://shopee.co.id/Valeton-GP-5-GP5-GP-5-Multi-FX-Amp-And-IR-Loader-Mini-Pedal-i.703046367.29241009193), seller703046367/item29241009193,Kota Bekasi, **Rp1.585.000,Habis** on reopening; search omitted the sold-out label. [kitharraguitarshop](https://shopee.co.id/Valeton-GP-5-Multi-Effects-Processor-SnapTone-IR-Loader-Efek-Gitar-i.331131666.43506785697), seller331131666/item43506785697,Kota Bandung, indexed **Rp1.605.000,Habis**; direct reopen cache miss. These exact hardware listings are historical retail asks, not checkout-confirmed stock or transactions. Condition grade, warranty region, accessory bundle, delivered charges and voucher eligibility unconfirmed. |
'''
        if model_id == 'gp-50':
            contexts = [p for p in shared_text.split('\n\n') if p.startswith('These earlier observations were recorded') or p.startswith('Prices are individual asking/listed observations') or p.startswith('**Availability warning:**')]
            urls = ['https://shop.valeton.net/products/gp-50','https://res.valeton.net/Uploads/wp/2025/12/gp-50-20.png']
            section += '''| New / retail Shopee IDR observations | Checked2026-10-17: [HOLY MUSIC](https://shopee.co.id/VALETON-GP-50-MULTI-EFFECT-PROCESSOR-Gp50-efek-valeton-gp50-i.945642322.55704518866), seller945642322/item55704518866,Kota Jakarta Utara: search **Rp2.245.000**, reopening **Rp2.255.000**; preserve snapshot discrepancy, no authenticated stock. [Diana Musik](https://shopee.co.id/Valeton-GP-50-GP50-Multi-Effects-Processor-i.495337904.56105944082), seller495337904/item56105944082,Kota Yogyakarta: **Rp2.255.000,Habis**, stale8September delivery. Exact hardware retail asks, not completed transactions. Condition, accessory bundle, warranty region, delivered charges and voucher eligibility unconfirmed. No qualified used IDR quote established. |
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
    if model_id in ('gp-5', 'gp-50', 'gp-100', 'gp-150', 'gp-180', 'gp-200'):
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
    if model_id == 'gp-5':
        entry.update(new_sources=['https://www.hotone.jp/announcements/nama2allbrand'],scope='Complete original GP-5 finding and compact comparison preserved; model-specific NAM A2 conversion app2.1.0+ and qualified sold-out Shopee asks checked2026-10-17. July2025 FAQ remains dated, not a blanket current controller limitation.')
        state['cursor']['model'] = 'Valeton GP-50 — complete legacy consolidation and NAM revision'
        state['cursor']['task'] = 'Read complete GP-50 finding and compact supporting source; consolidate into VALETON.md, preserve original dates, verify regional NAM A2 conversion firmware1.1.0+ with mobile2.1.0+, and commit before another model. Then continue remaining legacy records and fresh Shopee discovery.'
        state['discovery_leads'].append(dict(model='Valeton GP-5',checked_date='2026-10-17',status='Existing model refreshed; no count addition',urls=['https://shopee.co.id/Valeton-GP-5-GP5-GP-5-Multi-FX-Amp-And-IR-Loader-Mini-Pedal-i.703046367.29241009193','https://shopee.co.id/Valeton-GP-5-Multi-Effects-Processor-SnapTone-IR-Loader-Efek-Gitar-i.331131666.43506785697'],qualification='Asia Pro Sound1585000 Habis on reopen; search omitted label. kitharraguitarshop1605000 Habis indexed; reopen cache miss. Retail hardware asks, not used-price or live-stock proof. Condition/bundle/region/voucher/delivered charges unconfirmed.'))
    if model_id == 'gp-50':
        entry.update(new_sources=['https://www.hotone.jp/announcements/nama2allbrand'],scope='Complete original GP-50 finding and compact comparison preserved; NAM A2 conversion firmware1.1.0+/mobile2.1.0+ and qualified exact Shopee observations checked2026-10-17. Older1.0.5 manual and sold-out retail evidence retain dates.')
        state['cursor']['model'] = 'Line 6 HX Stomp — complete legacy consolidation'
        state['cursor']['task'] = 'Read complete HX Stomp original finding and all supporting comparison material, consolidate losslessly in LINE6.md, verify model-specific unresolved fields where primary evidence is accessible, update views and commit before another model. Continue fresh Shopee discovery and remaining legacy consolidation; all eight current Valeton models are root-canonical but partial.'
        state['discovery_leads'].append(dict(model='Valeton GP-50',checked_date='2026-10-17',status='Existing model refreshed; no count addition',urls=['https://shopee.co.id/VALETON-GP-50-MULTI-EFFECT-PROCESSOR-Gp50-efek-valeton-gp50-i.945642322.55704518866','https://shopee.co.id/Valeton-GP-50-GP50-Multi-Effects-Processor-i.495337904.56105944082'],qualification='HOLY MUSIC search2245000 versus reopened2255000,stock unconfirmed. Diana Musik2255000 Habis,stale8September delivery. Condition/bundle/region/delivered costs/voucher eligibility unknown.'))
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
        if sha is None:
            assert not (ROOT/p).exists(), 'Concurrent new file: '+p
        else:
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
    paths = ['ROLAND.md', 'VING.md', 'CUVAVE.md', 'TC-HELICON.md', 'SCORPION.md', 'BOIN-AUDIO.md', 'AUDOTA.md', 'NEURAL-DSP.md', 'scripts/nano_cortex_record.txt', 'IK-MULTIMEDIA.md', 'VALETON.md', 'MOOER.md', 'HOTONE.md', 'LINE6.md', 'BOSS.md', 'ZOOM.md', 'README.md', 'MULTI-EFFECTS.md', 'research-state.json', 'ALL-GUITAR.md', 'ALL-BASS.md', 'ALL-VOCAL.md', 'Makefile', 'scripts/consolidation_tools.py', 'scripts/comparison_views.py', 'scripts/research_tools.py']
    print(research_tools.git('status', '--short'))
    print(research_tools.git('add', '--', *paths))
    print(research_tools.git('diff', '--cached', '--stat'))
    if model_id == 've-2':
        print(research_tools.git('commit', '-m', 'research(boss): qualify VE2 driver versions and platform limits'))
        return
    if model_id == 've-8':
        print(research_tools.git('commit', '-m', 'research(boss): resolve VE8 guitar effect concurrency and qualified ask'))
        return
    if model_id == 'b6':
        print(research_tools.git('commit', '-m', 'research(zoom): qualify B6 loop allocation electrical limits and indexed ask'))
        return
    if model_id == 'b2-four':
        print(research_tools.git('commit', '-m', 'research(zoom): qualify B2 FOUR pedal rhythm and tuner limits'))
        return
    if model_id == 'gt-1b':
        print(research_tools.git('commit', '-m', 'research(boss): qualify GT1B live controls and headphone source conflict'))
        return
    if model_id == 've-500':
        print(research_tools.git('commit', '-m', 'research(boss): distinguish VE500 processing ratings from USB format'))
        return
    if model_id == 'ampero-mp350':
        print(research_tools.git('commit', '-m', 'research(hotone): qualify MP-350 scene bypass and DSP routing limits'))
        return
    if model_id == 'gr-55':
        print(research_tools.git('commit', '-m', 'research(roland): consolidate GR-55 with firmware and used-bundle evidence'))
        return
    if model_id == 'fb100':
        print(research_tools.git('commit', '-m', 'research(ving): consolidate FB-100 and preserve variant price conflicts'))
        return
    if model_id == 'h8':
        print(research_tools.git('commit', '-m', 'research(cuvave): consolidate H8 and verify desktop CubeSuite support'))
        return
    if model_id == 'play-acoustic':
        print(research_tools.git('commit', '-m', 'research(tchelicon): consolidate Play Acoustic and preserve firmware limits'))
        return
    if model_id == 'voicelive-play':
        print(research_tools.git('commit', '-m', 'research(tchelicon): record current regional VoiceSupport update evidence'))
        return
    if model_id == 'kmf-10':
        print(research_tools.git('commit', '-m', 'research(scorpion): consolidate KMF-10 and preserve power uncertainty'))
        return
    if model_id == 'bg300':
        print(research_tools.git('commit', '-m', 'research(boin): consolidate BG300 with explicit revision conflicts'))
        return
    if model_id == 'ave-100':
        print(research_tools.git('commit', '-m', 'research(audota): consolidate AVE-100 vocal evidence'))
        return
    if model_id == 'ace-100':
        print(research_tools.git('commit', '-m', 'research(audota): consolidate ACE-100 and clarify LED source evidence'))
        return
    if model_id == 'ame-200-pro':
        print(research_tools.git('commit', '-m', 'research(audota): consolidate AME-200 Pro and preserve source conflicts'))
        return
    if model_id == 'ame-200':
        print(research_tools.git('commit', '-m', 'research(audota): consolidate standard AME-200 evidence'))
        return
    if model_id == 'ame-100':
        print(research_tools.git('commit', '-m', 'research(audota): consolidate AME-100 and verify NAM IR concurrency'))
        return
    if model_id == 'nano-cortex':
        print(research_tools.git('commit', '-m', 'research(neuraldsp): consolidate Nano Cortex and document bass capability'))
        return
    if model_id in ('tonex-one','tonex-pedal'):
        print(research_tools.git('commit', '-m', 'research(ik): consolidate '+MODELS[model_id][0]+' and document bass capability'))
        return
    if model_id == 'hx-stomp':
        print(research_tools.git('commit', '-m', 'docs(line6): retain HX Stomp practical features in comparisons'))
        return
    print(research_tools.git('commit', '-m', 'docs(' + ('valeton' if model_id in ('gp-5', 'gp-50', 'gp-100', 'gp-150', 'gp-180', 'gp-200') else 'mooer' if model_id in ('ge100-original','ge150-original','ge200-original','ge150-pro-li','ge100-pro','ge100-pro-li','ge200-pro','ge200-pro-li','ge150-pro','ge150-plus','ge150-plus-li','ge150-max','ge150-max-li','ge1000','ge1000-li') else 'hotone' if model_id in ('ampero-mini','ampero-mp100','ampero-mp350','ampero-mp380','ampero-mp300') else 'line6' if model_id in ('hx-stomp','hx-stomp-xl') else 'boss' if model_id in ('gt-1b', 'gx-1b', 'me-90b', 've-1', 've-2', 've-500', 've-22', 've-8', 've-20', 'gt-1000core', 'gx-10', 'gt-1', 'gx-1', 'me-90', 'gx-100', 'gt-1000', 'gm-800') else 'zoom') + '): consolidate complete ' + MODELS[model_id][0] + ' evidence'))



def audit_findings():
    research_tools.identity()
    state = json.loads(preservation_text('research-state.json'))
    verify_preserved(state)
    manifests = [e for e in state.get('consolidation_and_price_findings', []) if e.get('verification_kind') == 'complete-source-body-v1']
    pairs = []
    for model, record in state['comparison_model_sources'].items():
        for source in record.get('finding_files', []):
            matches = [e for e in manifests if e['source'] == source and e['destination'] == record['link']]
            pairs.append(dict(model=model, source=source, destination=record['link'], covered=bool(matches)))
    missing = [p for p in pairs if not p['covered']]
    actual = {str(p.relative_to(ROOT)) for p in (ROOT/'effects/findings').glob('*.md')}
    preserved = {e['source'] for e in manifests}
    special = {'effects/findings/2026-10-14-flamma-fv01.md'}
    unregistered = sorted(actual - preserved - special)
    assert not unregistered, 'Actual finding paths without body manifests: '+str(unregistered)
    report = dict(actual_finding_files=len(actual), generic_preserved_files=len(actual & preserved), separately_verified_excluded_files=sorted(actual & special), unregistered_files=unregistered, scope='Registered finding/model pairs and actual finding-directory coverage; FV01 historical-original check is in research-verify. Not shared-source or incoming-link certification', pairs=len(pairs), covered=len(pairs)-len(missing), missing=missing, records=pairs)
    Path('/tmp/instrumentfx-finding-coverage.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k != 'records'}, indent=2))
    assert not missing, 'Registered finding body coverage missing'


def audit_legacy():
    research_tools.identity()
    state = json.loads(preservation_text('research-state.json'))
    files = sorted((ROOT/'effects').rglob('*.md'))
    all_md = sorted(ROOT.glob('*.md')) + files
    texts = {str(p.relative_to(ROOT)): p.read_text() for p in all_md}
    incoming = {str(p.relative_to(ROOT)): [] for p in files}
    # Lexical file-link inventory; deliberately does not certify anchors or prose.
    import urllib.parse
    for source, text in texts.items():
        targets = re.findall(r'\]\(([^\s]+)', text) + re.findall(r'^\[[^\]]+\]:\s*(\S+)', text, re.M)
        for raw in targets:
            raw = raw.rstrip(')')
            if '://' in raw or raw.startswith(('#', 'mailto:')):
                continue
            target = urllib.parse.unquote(raw.split('#',1)[0])
            resolved = (ROOT/source).parent.joinpath(target).resolve()
            try:
                key = str(resolved.relative_to(ROOT))
            except ValueError:
                continue
            if key in incoming:
                incoming[key].append(dict(source=source, link=raw))
    entries = []
    manifests = state.get('consolidation_and_price_findings', [])
    for p in files:
        key = str(p.relative_to(ROOT))
        text = texts[key]
        checked = [dict(destination=e.get('destination'), kind=e.get('verification_kind'), scope=e.get('scope')) for e in manifests if e.get('source') == key]
        entries.append(dict(path=key, sha256=digest(text), lines=len(text.splitlines()), table_count=len(list(comparison_views.tables(text))), manifest_scopes=checked, incoming=incoming[key], retirement_authorized=False))
    shared = [e for e in entries if '/findings/' not in e['path']]
    report = dict(scope='Read-only lexical source/link inventory; manifests do not certify an entire shared file; no retirement authorization', markdown_files=len(entries), shared_files=len(shared), incoming_link_occurrences=sum(len(e['incoming']) for e in entries), files=entries)
    Path('/tmp/instrumentfx-legacy-audit.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k != 'files'},indent=2))
    for e in shared:
        print(e['path']+' | tables='+str(e['table_count'])+' | source-manifests='+str(len(e['manifest_scopes']))+' | incoming='+str(len(e['incoming'])))



def audit_compact_matribox():
    research_tools.identity()
    source = research_tools.read_preserved_source('effects/guitar-compact.md')
    destination = preservation_text('SONICAKE.md').split('\n## Matribox QME-50\n',1)[1].split('\n## ',1)[0]
    facts = []
    for headers, rows, context in comparison_views.tables(source):
        for row in rows:
            label = re.sub(r'\[([^\]]+)\]\[[^\]]+\]', r'\1', row[0])
            if label in ('Matribox', 'Matribox QME-50', 'Sonicake Matribox, QME-50'):
                facts += [(h,v.replace('(findings/', '(effects/findings/')) for h,v in zip(headers[1:],row[1:])]
    assert len(facts) == 23, 'Matribox shared-field count changed'
    for field, value in facts:
        assert value in destination, 'Missing Matribox shared field: '+field
    for prefix in ('**Regional-price warning:**', "Sonicake's checked Matribox"):
        paragraph = next(p for p in source.split('\n\n') if p.startswith(prefix))
        assert paragraph.replace('(findings/', '(effects/findings/') in destination, 'Missing shared context: '+prefix
    print('PASS Matribox: 23 fields/five rows plus exact regional-price and firmware context retained. No source retirement or new firmware/stock verification.')


def audit_compact_smartbox():
    research_tools.identity()
    source = research_tools.read_preserved_source('effects/guitar-compact.md')
    destination = preservation_text('SONICAKE.md').split('\n## Smart Box QME-20\n',1)[1].split('\n## ',1)[0]
    facts = []
    for headers, rows, context in comparison_views.tables(source):
        for row in rows:
            label = re.sub(r'\[([^\]]+)\]\[[^\]]+\]', r'\1', row[0])
            if label in ('Smart Box', 'Smart Box QME-20', 'Sonicake Smart Box, QME-20'):
                facts += [(h,v.replace('(findings/', '(effects/findings/')) for h,v in zip(headers[1:],row[1:])]
    assert len(facts) == 23, 'Smart Box field count changed'
    for field, value in facts:
        assert value in destination, 'Missing Smart Box field: '+field
    for prefix in ("Sonicake's checked Matribox", 'These earlier observations'):
        assert next(p for p in source.split('\n\n') if p.startswith(prefix)) in destination, 'Shared context missing'
    for url in ('effects/findings/2026-10-14-sonicake-smart-box.md', 'https://sonicake.oss-accelerate.aliyuncs.com/res/kU5Y9sWnzs/QME20total.pdf', 'https://www.sonicake.com/products/smart-box'):
        assert ']('+url+')' in destination, 'Source key missing'
    print('PASS Smart Box: 23 fields/five rows, shared firmware/foreign-price context and source-key links retained. No stock or native NAM certification.')

def audit_compact_pocketmaster():
    research_tools.identity()
    source = research_tools.read_preserved_source('effects/guitar-compact.md')
    destination = preservation_text('SONICAKE.md').split('\n## Pocket Master QME-10\n',1)[1].split('\n## ',1)[0]
    facts = []
    for headers, rows, context in comparison_views.tables(source):
        for row in rows:
            label = re.sub(r'\[([^\]]+)\]\[[^\]]+\]', r'\1', row[0])
            if label in ('Pocket Master', 'Pocket Master QME-10', 'Sonicake Pocket Master, QME-10'):
                facts += [(h,v.replace('(findings/', '(effects/findings/')) for h,v in zip(headers[1:],row[1:])]
    assert len(facts) == 23, 'Pocket Master field count changed'
    for field, value in facts:
        assert value in destination, 'Missing Pocket Master field: '+field
    for prefix in ("Sonicake's checked Matribox", 'These earlier observations', '**Availability warning:**'):
        assert next(p for p in source.split('\n\n') if p.startswith(prefix)) in destination, 'Shared context missing'
    for url in ('effects/findings/2026-10-14-sonicake-pocket-master.md', 'https://cdn.shopify.com/s/files/1/0100/1950/4185/files/Pocket_Master_Multi_Languages_User_Manual_Firmware_V1.3.0.pdf?v=1754556312', 'https://www.sonicake.com/products/pocket-master'):
        assert ']('+url+')' in destination, 'Source key missing'
    print('PASS Pocket Master: 23 fields/five rows, shared firmware/foreign-price context and source-key links retained. No stock or native NAM certification.')

def audit_compact(model):
    if model == 'Pocket Master':
        return audit_compact_pocketmaster()
    if model == 'Smart Box':
        return audit_compact_smartbox()
    if model == 'Matribox':
        return audit_compact_matribox()
    research_tools.identity()
    assert model in ('GP-100', 'GP-150', 'GP-5', 'GP-50', 'GP-180'), 'Additional models require explicit scope review'
    state = json.loads(preservation_text('research-state.json'))
    source_path = 'effects/guitar-compact.md'
    source = research_tools.read_preserved_source(source_path)
    entry = next(e for e in state['consolidation_and_price_findings'] if e.get('model_name') == model and e.get('destination') == 'VALETON.md#'+model.lower())
    expected = []
    for headers, rows, context in comparison_views.tables(source):
        for row in rows:
            label = re.sub(r'\[([^\]]+)\]\[[^\]]+\]', r'\1', row[0])
            if label not in (model, 'Valeton '+model):
                continue
            for header, value in zip(headers[1:], row[1:]):
                value = value.replace('(findings/', '(effects/findings/')
                expected.append(dict(field=header,value=value,source=source_path,context=context))
    retained = [f for f in entry['retained_comparison_facts'] if f['source'] == source_path]
    assert len(expected) == 23 and expected == retained, 'Shared model row completeness changed'
    destination = preservation_text('VALETON.md').split('\n## '+model+'\n',1)[1].split('\n## ',1)[0]
    for fact in expected:
        assert fact['value'] in destination, 'Missing shared fact: '+fact['field']
    if model == 'GP-100':
        context = next(p for p in source.split('\n\n') if p.startswith('**Availability warning:**'))
        assert context in destination, 'Shared availability context missing'
    else:
        for context in entry.get('retained_context', []):
            assert context in source and context in destination, 'Shared context missing'
        urls = ('https://res.valeton.net/Uploads/wp/2026/03/GP-150-GP180-Comparison-2.png', 'effects/findings/2026-10-14-valeton-gp-150.md', 'https://shop.valeton.net/products/gp-150') if model == 'GP-150' else ('effects/findings/2026-10-14-valeton-gp-5.md', 'https://www.guitarcenter.com/Valeton/Multi-Effects-Pedals.gc', 'https://shop.valeton.net/products/gp-5')
        if model == 'GP-50':
            urls = ('effects/findings/2026-10-14-valeton-gp-50.md', 'https://shop.valeton.net/products/gp-50', 'https://res.valeton.net/Uploads/wp/2025/12/gp-50-20.png')
        if model == 'GP-180':
            urls = ('effects/findings/2026-10-14-valeton-gp-180.md', 'https://shop.valeton.net/products/gp-180', 'https://res.valeton.net/Uploads/wp/2026/03/GP-150-GP180-Comparison-2.png')
        for url in urls:
            assert ']('+url+')' in destination, 'Reference key missing: '+url
    print('PASS '+model+': 23 fields across five model rows retained, with model-specific context/reference checks. Other models and incoming-link retirement remain unaudited.')


def audit_compact_union():
    research_tools.identity()
    state = json.loads(preservation_text('research-state.json'))
    source = research_tools.read_preserved_source('effects/guitar-compact.md')
    entry = state['migration']['shared_compact_audit']['prose_union']
    assert digest(source) == entry['source_sha256'], 'Compact source changed'
    refs = {m[1].lower():m[2] for m in re.finditer(r'^\[([^\]]+)\]:\s*(\S+)', source, re.M)}
    paragraphs = [p for p in re.split(r'\n\s*\n', source) if p.strip() and not re.match(r'^[#|\[]', p.strip())]
    union = '\n'.join(preservation_text(p) for p in entry['destinations'])
    missing = [p for p in paragraphs if comparison_views.relink(p, 'effects/guitar-compact.md', refs) not in union]
    assert not missing, 'Compact prose missing: '+str(missing)
    urls = set(re.findall(r'https?://[^\s)]+', source))
    assert all(url in union for url in urls), 'Compact external URL missing'
    for model in ('GP-100','GP-150','Matribox','GP-5','GP-50','GP-180','Smart Box','Pocket Master'):
        audit_compact(model)
    print('PASS compact union: '+str(len(paragraphs))+' prose/source-list groups, '+str(len(urls))+' external URLs, eight model-row audits. Incoming links remain; no source retirement.')


def audit_floorboard_union():
    research_tools.identity()
    state = json.loads(preservation_text('research-state.json'))
    entry = state['migration']['shared_floorboard_audit']
    path = entry['source']
    source = research_tools.read_preserved_source(path)
    assert digest(source) == entry['source_sha256'], 'Floorboard source changed'
    refs = {m[1].lower():m[2] for m in re.finditer(r'^\[([^\]]+)\]:\s*(\S+)', source, re.M)}
    paragraphs = [p for p in re.split(r'\n\s*\n', source) if p.strip() and not re.match(r'^[#|\[]', p.strip())]
    union = '\n'.join(preservation_text(p) for p in ('VALETON.md','SONICAKE.md','MULTI-EFFECTS.md'))
    missing = [comparison_views.relink(p,path,refs) for p in paragraphs if comparison_views.relink(p,path,refs) not in union]
    assert not missing, 'Floorboard prose missing: '+str(missing)
    urls = set(re.findall(r'https?://[^\s)]+', source))
    assert all(url in union for url in urls), 'Floorboard external URL missing'
    manifests = [e for e in state['consolidation_and_price_findings'] if e.get('source') == path and e.get('verification_kind') == 'complete-model-rows-v1']
    assert {e['model_name'] for e in manifests} == {'GP-200','Matribox II QME-100','Matribox II Pro QME-200'}
    verify_preserved(state)
    print('PASS floorboard union: '+str(len(paragraphs))+' prose/source groups, '+str(len(urls))+' external URLs, three model manifests / 42 fields. Incoming links remain; no source retirement.')


def audit_compact_links(kind='compact'):
    assert kind in ('compact','nux','bass','vocal','advanced','boss','boss-history','audota','cube','owned','market1','market2','market3','market4','market5','market6','market7')
    """Inventory explicit Markdown links and literal references before source retirement."""
    import urllib.parse
    research_tools.identity()
    source_key = 'effects/'+kind+'.md' if kind in ('bass','vocal','audota') else 'effects/guitar-'+kind+'.md'
    if kind == 'market3':
        source_key = 'effects/shopee-multifx-3.md'
    if kind == 'market4':
        source_key = 'effects/shopee-multifx-4.md'
    if kind == 'market5':
        source_key = 'effects/shopee-multifx-5.md'
    if kind == 'market6':
        source_key = 'effects/shopee-multifx-6.md'
    if kind == 'market7':
        source_key = 'effects/shopee-multifx-7.md'
    if kind == 'market2':
        source_key = 'effects/shopee-multifx-2.md'
    if kind == 'market1':
        source_key = 'effects/shopee-multifx.md'
    if kind == 'owned':
        source_key = 'effects/owned-multifx.md'
    if kind == 'cube':
        source_key = 'effects/cube-baby.md'
    if kind == 'advanced':
        source_key = 'effects/advanced-modelers.md'
    if kind == 'boss-history':
        source_key = 'effects/guitar-boss.history-2026-10-14.md'
    source = research_tools.read_preserved_source(source_key)
    state = json.loads(preservation_text('research-state.json'))
    assert digest(source) == state['migration']['shared_'+kind.replace('-', '_')+'_audit']['source_sha256']
    paths = sorted(ROOT.glob('*.md')) + sorted((ROOT/'effects').rglob('*.md'))
    incoming, outgoing, mentions = [], [], []
    for path in paths:
        text = path.read_text()
        key = str(path.relative_to(ROOT))
        definitions = {m[1].lower(): m[2] for m in re.finditer(r'^\[([^\]]+)\]:\s*(\S+)', text, re.M)}
        links = [(m.start(), m[1], 'inline') for m in re.finditer(r'\]\(([^\s)]+)\)', text)]
        links += [(m.start(), definitions[m[2].lower()], 'reference') for m in re.finditer(r'\[([^\]]+)\]\[([^\]]+)\]', text) if m[2].lower() in definitions]
        links += [(m.start(), m[2], 'definition') for m in re.finditer(r'^\[([^\]]+)\]:\s*(\S+)', text, re.M)]
        for offset, raw, link_kind in links:
            parsed = urllib.parse.urlsplit(raw)
            if parsed.scheme or parsed.netloc:
                continue
            target = path.parent.joinpath(urllib.parse.unquote(parsed.path)).resolve() if parsed.path else path
            try:
                resolved = str(target.relative_to(ROOT))
            except ValueError:
                continue
            entry = dict(source=key, line=text.count('\n', 0, offset)+1, link=raw, kind=link_kind, target=resolved, fragment=urllib.parse.unquote(parsed.fragment), exists=target.is_file())
            if resolved == source_key:
                incoming.append(entry)
            if key == source_key:
                outgoing.append(entry)
        for number, line in enumerate(text.splitlines(), 1):
            if Path(source_key).name in line:
                mentions.append(dict(source=key, line=number))
    # JSON references are recorded separately: provenance is not an incoming navigation link.
    json_mentions = []
    for path in sorted(ROOT.glob('*.json')) + sorted((ROOT/'effects').rglob('*.json')):
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if Path(source_key).name in line:
                json_mentions.append(dict(source=str(path.relative_to(ROOT)), line=number))
    headings = [dict(line=i, heading=line.lstrip('#').strip()) for i,line in enumerate(source.splitlines(),1) if re.match(r'^#{1,6} ',line)]
    report = dict(source=source_key, source_sha256=digest(source), incoming=incoming, outgoing=outgoing, markdown_literal_mentions=mentions, json_literal_mentions=json_mentions, headings=headings, missing_outgoing=[e for e in outgoing if not e['exists']], incoming_fragments=sorted({e['fragment'] for e in incoming if e['fragment']}), retirement_authorized=False, limitations=['Lexical explicit inline/reference/definition links; definition and use are separate occurrences.', 'Shortcut links, HTML, code and external bookmarks are not exhaustively parsed; literal mention locations retained for review.', 'No link rewrite, anchor mapping, source deletion or external availability verification.'])
    Path('/tmp/instrumentfx-'+kind+'-links.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(source=source_key,incoming=len(incoming),outgoing=len(outgoing),missing_outgoing=report['missing_outgoing'],incoming_fragments=report['incoming_fragments'],markdown_mentions=len(mentions),json_mentions=len(json_mentions),headings=len(headings)),indent=2))


def plan_nux_shared(model='MG-101'):
    configs = {
        'MG-101': ('mg101', {'mg101'}, ('[101]:','[US101]:','- MG-101 '), 4),
        'MG-300 original': ('mg300', {'mg300','mg300original'}, ('[300]:','- [MG-300 manufacturer manual]'), 2),
        'MG-300 MKII': ('mg300mkii', {'mg300mkii'}, ('[300ii]:','[US300]:','[NAM]:','- [MG-300 MKII manufacturer manual]'), 4),
        'MG-400': ('mg400', {'mg400'}, ('[400]:','[US400]:','[P1]:','[NAM]:','- [MG-400 control image]'), 5),
        'MG-50Li': ('mg50li', {'mg50li'}, ('[50]:','[US50]:','[NAM]:','- MG-50Li '), 5),
        'MG-30': ('mg30', {'mg30'}, ('[30]:','[NAM]:','- [MG-30 manufacturer V2 manual]'), 3),
    }
    key, labels, url_prefixes, url_count = configs[model]
    research_tools.identity()
    source_path = 'effects/guitar-nux.md'
    source = research_tools.read_preserved_source(source_path)
    destination = (ROOT/'NUX.md').read_text()
    facts = []
    for headers, rows, context in comparison_views.tables(source):
        for row in rows:
            if comparison_views.norm(row[0]) in labels:
                facts += [dict(field=h,value=v,source=source_path,context=context) for h,v in zip(headers[1:],row[1:])]
    assert len(facts) == 15, model+' row scope changed'
    prefixes = ('Checked **2026-10-14**.', 'These are single new-price observations', 'The category numbers describe', 'The global download pages explicitly')
    if model in ('MG-101','MG-300 MKII'):
        prefixes += ('**MG-101 / MG-300 MKII:**',)
    if model != 'MG-101':
        prefixes += ('**NAM:**',)
    if model == 'MG-50Li':
        prefixes += ('**MG-50Li:**',)
    contexts = [p for p in source.split('\n\n') if p.startswith(prefixes)]
    assert len(contexts) == (6 if model in ('MG-300 MKII','MG-50Li') else 5)
    urls = re.findall(r'https?://[^\s)]+', '\n'.join(line for line in source.splitlines() if line.startswith(url_prefixes)))
    assert len(urls) == url_count
    section = destination.split('\n## '+model+'\n',1)[1].split('\n## ',1)[0]
    report = dict(model=model, source=source_path, source_sha256=digest(source), destination_sha256=digest(destination), retained_comparison_facts=facts, retained_context=contexts,retained_source_urls=urls,missing_exact_fields=[f for f in facts if f['value'] not in section])
    Path('/tmp/instrumentfx-nux-'+key+'-plan.json').write_text(json.dumps(report,indent=2)+'\n')
    print(model+':15 fields/3rows,'+str(len(contexts))+' historical context paragraphs,'+str(len(urls))+' source URLs; exact field omissions='+str(len(report['missing_exact_fields'])))


def audit_nux_union(verify=True, kind='nux'):
    assert kind in ('nux','bass','vocal','advanced')
    research_tools.identity()
    state = json.loads(preservation_text('research-state.json'))
    entry = state['migration']['shared_'+kind+'_audit']
    path = entry['source']
    source = research_tools.read_preserved_source(path)
    assert digest(source) == entry['source_sha256'], 'Shared source changed'
    refs = {m[1].lower():m[2] for m in re.finditer(r'^\[([^\]]+)\]:\s*(\S+)', source, re.M)}
    paragraphs = [p for p in re.split(r'\n\s*\n', source) if p.strip() and not re.match(r'^[#|]', p.strip()) and not re.match(r'^\[[^\]]+\]:',p.strip())]
    normalized = [comparison_views.relink(p,path,refs) for p in paragraphs]
    destinations = ('ZOOM.md','BOSS.md','MULTI-EFFECTS.md') if kind in ('bass','vocal') else ('NUX.md','MULTI-EFFECTS.md')
    if kind == 'advanced':
        destinations = ('LINE6.md','NEURAL-DSP.md','IK-MULTIMEDIA.md','HEADRUSH.md','MULTI-EFFECTS.md')
    union = '\n'.join(preservation_text(p) for p in destinations)
    missing = [p for p in normalized if p not in union]
    urls = sorted(set(re.findall(r'https?://[^\s)]+',source)))
    manifests = [e for e in state['consolidation_and_price_findings'] if e.get('source') == path and e.get('verification_kind') == 'complete-model-rows-v1']
    expected = {'ZOOM.md#b1-four','ZOOM.md#b1x-four','ZOOM.md#b2-four','ZOOM.md#b6','BOSS.md#gt-1b','BOSS.md#gx-1b','BOSS.md#me-90b'} if kind == 'bass' else {'NUX.md#'+m for m in ('mg-101','mg-300-original','mg-300-mkii','mg-400','mg-30','mg-50li')}
    if kind == 'vocal':
        expected = {'ZOOM.md#v3','ZOOM.md#v6-sp'} | {'BOSS.md#'+m for m in ('ve-1','ve-2','ve-500','ve-22','ve-8','ve-20')}
    if kind == 'advanced':
        expected = {'LINE6.md#hx-stomp','LINE6.md#hx-effects','NEURAL-DSP.md#nano-cortex','IK-MULTIMEDIA.md#tonex-one','IK-MULTIMEDIA.md#tonex-pedal','HEADRUSH.md#flex-prime'}
    assert {e['destination'] for e in manifests} == expected
    fields = sum(len(e['retained_comparison_facts']) for e in manifests)
    assert fields == {'bass':105,'vocal':112,'nux':90,'advanced':90}[kind]
    report = dict(source=path,source_sha256=digest(source),destinations=list(destinations),paragraph_groups=len(paragraphs),normalized_missing_groups=missing,external_urls=urls,missing_external_urls=[u for u in urls if u not in union],model_manifests=len(manifests),model_fields=fields,retirement_authorized=False)
    Path('/tmp/instrumentfx-'+kind+'-union-plan.json').write_text(json.dumps(report,indent=2)+'\n')
    if verify:
        assert not missing, 'Shared prose/source groups missing ('+kind+'): '+str(missing)
        assert not report['missing_external_urls'], 'Shared URL missing'
        verify_preserved(state)
    print(json.dumps({k:v for k,v in report.items() if k not in ('external_urls','normalized_missing_groups')},indent=2))
    print('Missing prose/source groups: '+str(len(missing)))


def plan_advanced_hxe(model='HX Effects'):
    assert model in ('HX Effects','Flex Prime')
    flex = model == 'Flex Prime'
    brand_file = 'HEADRUSH.md' if flex else 'LINE6.md'
    research_tools.identity()
    path = 'effects/advanced-modelers.md'
    source = research_tools.read_preserved_source(path)
    destination = (ROOT/brand_file).read_text()
    section = destination.split('\n## '+model+'\n',1)[1].split('\n## ',1)[0]
    facts = []
    for headers, rows, context in comparison_views.tables(source):
        for row in rows:
            if comparison_views.norm(row[0]) in (('flexprime','headrushflexprime') if flex else ('hxeffects','line6hxeffects')):
                facts += [dict(field=h,value=v,source=path,context=context) for h,v in zip(headers[1:],row[1:])]
    assert len(facts) == 15
    prefixes = ('Checked **2026-10-14**.', 'K/F/B =', 'The rounded Line 6 FAQ', "**HX Stomp's old FAQ", 'USB audio input/output counts')
    if flex:
        prefixes = ('Checked **2026-10-14**.', 'K/F/B =', '**Flex Prime is not restricted', 'USB audio input/output counts')
    contexts = [p for p in source.split('\n\n') if p.startswith(prefixes)]
    assert len(contexts) == (4 if flex else 5)
    urls = re.findall(r'https?://[^\s)]+', '\n'.join(line for line in source.splitlines() if line.startswith(('[flex]:','- [Flex Prime FAQ]') if flex else ('[hxe]:','- [HX Effects FAQ]'))))
    assert len(urls) == (4 if flex else 3)
    report = dict(model=model,source=path,source_sha256=digest(source),destination_sha256=digest(destination),retained_comparison_facts=facts,retained_context=contexts,retained_source_urls=urls,missing_exact_fields=[f for f in facts if f['value'] not in section])
    Path('/tmp/instrumentfx-advanced-'+('flex' if flex else 'hxe')+'-plan.json').write_text(json.dumps(report,indent=2)+'\n')
    print(model+':15 fields/3rows,'+str(len(contexts))+' shared paragraphs,'+str(len(urls))+' model URLs;exact omissions='+str(len(report['missing_exact_fields'])))


def audit_boss_shared(verify=True, history=False):
    key = 'boss-history' if history else 'boss'
    state_key = 'shared_boss_history_audit' if history else 'shared_boss_audit'
    field_count = 16 if history else 21
    research_tools.identity()
    path = 'effects/guitar-boss.history-2026-10-14.md' if history else 'effects/guitar-boss.md'
    source = research_tools.read_preserved_source(path)
    state = json.loads(preservation_text('research-state.json'))
    assert digest(source) == state['migration'][state_key]['source_sha256']
    destination = preservation_text('BOSS.md')
    models = ('GT-1000CORE','GX-10','GT-1','GX-1','ME-90','GX-100','GT-1000')
    records = []
    for model in models:
        facts = []
        for headers, rows, context in comparison_views.tables(source):
            for row in rows:
                if comparison_views.norm(row[0]) == comparison_views.norm(model):
                    facts += [dict(field=h,value=v,source=path,context=context) for h,v in zip(headers[1:],row[1:])]
        assert len(facts) == field_count, model+' row scope changed'
        section = destination.split('\n## '+model+'\n',1)[1].split('\n## ',1)[0]
        records.append(dict(model=model,destination='BOSS.md#'+model.lower(),facts=facts,missing_fields=[f for f in facts if f['value'] not in section]))
    refs = {m[1].lower():m[2] for m in re.finditer(r'^\[([^\]]+)\]:\s*(\S+)',source,re.M)}
    groups = [p for p in re.split(r'\n\s*\n',source) if p.strip() and not re.match(r'^[#|]',p.strip()) and not re.match(r'^\[[^\]]+\]:',p.strip())]
    normalized = [comparison_views.relink(p,path,refs) for p in groups]
    union = destination+'\n'+preservation_text('MULTI-EFFECTS.md')
    missing = [p for p in normalized if p not in union]
    urls = sorted(set(re.findall(r'https?://[^\s)]+',source)))
    report = dict(source=path,source_sha256=digest(source),records=records,model_fields=field_count*7,paragraph_groups=len(groups),normalized_missing_groups=missing,external_urls=urls,missing_external_urls=[u for u in urls if u not in union],retirement_authorized=False)
    Path('/tmp/instrumentfx-'+key+'-union-plan.json').write_text(json.dumps(report,indent=2)+'\n')
    if verify:
        assert not any(r['missing_fields'] for r in records), 'Missing BOSS fields'
        assert not missing and not report['missing_external_urls'], 'Missing BOSS context/URLs'
        verify_preserved(json.loads(preservation_text('research-state.json')))
    print(json.dumps(dict(models=len(records),fields=field_count*7,missing_model_fields=sum(len(r['missing_fields']) for r in records),paragraph_groups=len(groups),missing_groups=len(missing),external_urls=len(urls),missing_urls=report['missing_external_urls']),indent=2))



def audit_audota_union(verify=True):
    """Check all shared rows, appendix cells, prose and reference targets."""
    research_tools.identity()
    state = json.loads(preservation_text('research-state.json'))
    path = 'effects/audota.md'
    source = research_tools.read_preserved_source(path)
    assert digest(source) == state['migration']['shared_audota_audit']['source_sha256']
    destination = preservation_text('AUDOTA.md')
    union = destination+'\n'+preservation_text('MULTI-EFFECTS.md')
    aliases = {'AME-100':{'ame100'},'AME-200':{'ame200'},'AME-200 Pro':{'ame200pro','pro'},'ACE-100':{'ace100'},'AVE-100':{'ave100'}}
    records = {model:[] for model in aliases}
    appendix = []
    for headers, rows, context in comparison_views.tables(source):
        if context == 'AME-200 and Pro: actual appendix counts':
            appendix = [dict(field=h,value=v) for row in rows for h,v in zip(headers,row)]
            continue
        for row in rows:
            if context == 'Vocal model: AVE-100':
                assert len(row) == 2
                records['AVE-100'].append(dict(field=row[0],value=row[1],source=path,context=context))
                continue
            matched = [m for m, names in aliases.items() if comparison_views.norm(row[0]) in names]
            assert len(matched) == 1, 'Unmapped shared row: '+str(row)
            records[matched[0]] += [dict(field=h,value=v,source=path,context=context) for h,v in zip(headers[1:],row[1:])]
    assert [len(records[m]) for m in aliases] == [14,14,14,14,11]
    assert len(appendix) == 11
    manifests = {e['model_name']:e for e in state['consolidation_and_price_findings'] if e.get('destination','').startswith('AUDOTA.md#')}
    model_reports = []
    ordered = lambda facts: sorted((f['field'],f['value'],f['source'],f['context']) for f in facts)
    for model,facts in records.items():
        entry = manifests[model]
        assert entry['supporting_source_hashes'][path] == digest(source)
        assert ordered(entry['retained_comparison_facts']) == ordered(facts), 'Source/manifest field mismatch: '+model
        section = destination.split('\n## '+model+'\n',1)[1].split('\n## ',1)[0]
        model_reports.append(dict(model=model,fields=len(facts),missing=[f for f in facts if f['value'] not in section]))
    refs = {m[1].lower():m[2] for m in re.finditer(r'^\[([^\]]+)\]:\s*(\S+)',source,re.M)}
    groups = [p for p in re.split(r'\n\s*\n',source) if p.strip() and not re.match(r'^[#|]',p.strip()) and not re.match(r'^\[[^\]]+\]:',p.strip())]
    normalized = [comparison_views.relink(p,path,refs) for p in groups]
    appendix_text = source.split('| Drive |',1)[1].split('\n\n',1)[0]
    appendix_text = '| Drive |'+appendix_text
    targets = [comparison_views.relink('[source]('+target+')',path,{}) for target in refs.values()]
    target_paths = [re.search(r'\]\(([^)]+)\)',target)[1] for target in targets]
    report = dict(source=path,source_sha256=digest(source),model_reports=model_reports,model_fields=67,appendix_cells=appendix,appendix_table_preserved=appendix_text in destination,paragraph_groups=len(groups),normalized_missing_groups=[p for p in normalized if p not in union],reference_targets=target_paths,missing_reference_targets=[target for target in target_paths if target not in union],retirement_authorized=False)
    Path('/tmp/instrumentfx-audota-union-plan.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('model_reports','appendix_cells','normalized_missing_groups','reference_targets')},indent=2))
    print('Missing model fields: '+str(sum(len(r['missing']) for r in model_reports))+';missing prose groups: '+str(len(report['normalized_missing_groups'])))
    if verify:
        assert not any(r['missing'] for r in model_reports)
        assert report['appendix_table_preserved']
        assert not report['normalized_missing_groups'] and not report['missing_reference_targets']
        verify_preserved(state)



def audit_shared_variant_union(verify=True, kind='cube'):
    assert kind in ('cube','owned','market1','market2','market3','market4','market5','market6','market7')
    research_tools.identity()
    state = json.loads(preservation_text('research-state.json'))
    path = {'cube':'effects/cube-baby.md','owned':'effects/owned-multifx.md','market1':'effects/shopee-multifx.md','market2':'effects/shopee-multifx-2.md','market3':'effects/shopee-multifx-3.md','market4':'effects/shopee-multifx-4.md','market5':'effects/shopee-multifx-5.md','market6':'effects/shopee-multifx-6.md','market7':'effects/shopee-multifx-7.md'}[kind]
    source = research_tools.read_preserved_source(path)
    assert digest(source) == state['migration']['shared_'+kind+'_audit']['source_sha256']
    aliases = {'CUBE BABY electric':{'electriccubebaby','electric'},'CUBE BABY AC':{'cubebabyac','ac'},'CUBE BABY BASS':{'cubebabybass','bass'}}
    files = {model:'M-VAVE.md' for model in aliases}
    if kind == 'owned':
        aliases = {'GR-55':{'rolandgr55','gr55'},'B1Xon':{'zoomb1xon','b1xon'},'GEM BOX original':{'joyogemboxoriginal','gemboxoriginal'},'MINI-X':{'mvaveminix','minix'},'Pocket Amp':{'mvavepocketamp','pocketamp'},'H8':{'cuvaveh8','h8'},'Flybro FB-100':{'vingflybrofb100','vingfb100','fb100'}}
        files = {'GR-55':'ROLAND.md','B1Xon':'ZOOM.md','GEM BOX original':'JOYO.md','MINI-X':'M-VAVE.md','Pocket Amp':'M-VAVE.md','H8':'CUVAVE.md','Flybro FB-100':'VING.md'}
    if kind == 'market1':
        aliases = {"TANK MINI":{"mvavetankmini","tankmini"},"TANK-G":{"mvavetankg","tankg","tankgtankb"},"TANK-B":{"mvavetankb","tankb","tankgtankb"},"MK-20":{"mvavemk20","mk20"},"MK-300":{"mvavemk300","mk300"},"Ampero Mini MP-50":{"hotoneamperominimp50","amperomini"},"GE100 original":{"mooerge100original","ge100"},"GE150 original":{"mooerge150original","ge150original"},"GE200 original":{"mooerge200original","ge200original","ge200"},"GE150 Pro Li":{"mooerge150proli","ge150proli"},"G1 FOUR":{"zoomg1four","g1four","g1fourg1xfour"},"G1X FOUR":{"zoomg1xfour","g1xfour","g1fourg1xfour"},"G2 FOUR":{"zoomg2four","g2four","g2fourg2xfour"},"G2X FOUR":{"zoomg2xfour","g2xfour","g2fourg2xfour"},"FX100":{"flammafx100","fx100"},"FX200":{"flammafx200","fx200"}}
        files = {"TANK MINI":"M-VAVE.md","TANK-G":"M-VAVE.md","TANK-B":"M-VAVE.md","MK-20":"M-VAVE.md","MK-300":"M-VAVE.md","Ampero Mini MP-50":"HOTONE.md","GE100 original":"MOOER.md","GE150 original":"MOOER.md","GE200 original":"MOOER.md","GE150 Pro Li":"MOOER.md","G1 FOUR":"ZOOM.md","G1X FOUR":"ZOOM.md","G2 FOUR":"ZOOM.md","G2X FOUR":"ZOOM.md","FX100":"FLAMMA.md","FX200":"FLAMMA.md"}
    if kind == 'market2':
        aliases = {"TANK-PRO":{"mvavetankpro","tankpro"},"ANN Blackbox":{"mvaveannblackbox","annblackbox"},"BG300":{"boinaudiobg300","bg300"},"KMF-10":{"scorpionkmf10","kmf10"},"GEM BOX II":{"joyogemboxii","gemboxii"},"GEM BOX III":{"joyogemboxiii","gemboxiii"},"VoiceLive Play":{"tcheliconvoiceliveplay","voiceliveplay"},"Play Acoustic":{"tcheliconplayacoustic","playacoustic"}}
        files = {"TANK-PRO":"M-VAVE.md","ANN Blackbox":"M-VAVE.md","BG300":"BOIN-AUDIO.md","KMF-10":"SCORPION.md","GEM BOX II":"JOYO.md","GEM BOX III":"JOYO.md","VoiceLive Play":"TC-HELICON.md","Play Acoustic":"TC-HELICON.md"}
    if kind == 'market3':
        aliases = {"Core":{"headrushcore","core"},"Arena2000":{"donnerarena2000","arena2000"},"MG-100":{"nuxmg100","mg100"},"MG-200":{"nuxmg200","mg200"}}
        files = {"Core":"HEADRUSH.md","Arena2000":"DONNER.md","MG-100":"NUX.md","MG-200":"NUX.md"}
    if kind == 'market4':
        aliases = {"GE100 Pro":{"ge100pro","mooerge100pro"},"GE100 Pro Li":{"ge100proli","mooerge100proli"},"GE200 Pro":{"ge200pro","mooerge200pro"},"GE200 Pro Li":{"ge200proli","mooerge200proli"}}
        files = {"GE100 Pro":"MOOER.md","GE100 Pro Li":"MOOER.md","GE200 Pro":"MOOER.md","GE200 Pro Li":"MOOER.md"}
    if kind == 'market5':
        aliases = {"Ampero MP-100":{"hotoneamperomp100","mp100"},"Ampero II MP-350":{"hotoneamperoiimp350","mp350"},"Ampero II Stage MP-380":{"hotoneamperoiistagemp380","mp380"},"GE1000":{"mooerge1000nonli","ge1000"},"GE150 Pro":{"mooerge150prononli","ge150pro"},"HX Stomp XL":{"line6hxstompxl","hxstompxl"}}
        files = {"Ampero MP-100":"HOTONE.md","Ampero II MP-350":"HOTONE.md","Ampero II Stage MP-380":"HOTONE.md","GE1000":"MOOER.md","GE150 Pro":"MOOER.md","HX Stomp XL":"LINE6.md"}
    if kind == 'market6':
        aliases = {"GE150 Plus":{"ge150plusnonli","ge150plus","plus"},"GE150 Plus Li":{"ge150plusli","plusli"},"GE150 Max":{"ge150maxnonli","ge150max","max"},"GE150 Max Li":{"ge150maxli","maxli"},"GE1000 Li":{"ge1000li"}}
        files = {"GE150 Plus":"MOOER.md","GE150 Plus Li":"MOOER.md","GE150 Max":"MOOER.md","GE150 Max Li":"MOOER.md","GE1000 Li":"MOOER.md"}
    if kind == 'market7':
        aliases = {"TRIDENT NME-5":{"nuxtridentnme5","trident"},"G6":{"zoomg6","g6"},"G11":{"zoomg11","g11"},"Ampero II Stomp MP-300":{"amperoiistompmp300","mp300","amperoiistomp"},"POD Go":{"podgostandard","podgo","podgowireless","podgovariants"},"POD Go Wireless":{"podgowireless","podgovariants"},"POD Express Guitar":{"podexpressguitar","expressguitar","podexpressguitarbass","expressvariants"},"POD Express Bass":{"podexpressbass","expressbass","podexpressguitarbass","expressvariants"}}
        files = {"TRIDENT NME-5":"NUX.md","G6":"ZOOM.md","G11":"ZOOM.md","Ampero II Stomp MP-300":"HOTONE.md","POD Go":"LINE6.md","POD Go Wireless":"LINE6.md","POD Express Guitar":"LINE6.md","POD Express Bass":"LINE6.md"}
    destinations = {name:preservation_text(name) for name in set(files.values())}
    union = '\n'.join(destinations.values())+'\n'+preservation_text('MULTI-EFFECTS.md')
    records = {model:[] for model in aliases}
    shared_tables = []
    for headers,rows,context in comparison_views.tables(source):
        if kind == 'market6' and context == 'GE150 Plus and Max manuals: category counts':
            assert len(headers) == 10 and len(rows) == 1 and rows[0] == ['12','28','55','26','3','4','25','9','8','**170**']
            shared_tables.append('| FX/wah/dynamics |'+source.split('| FX/wah/dynamics |',1)[1].split('\n\n',1)[0])
            continue
        for row in rows:
            matched = [m for m,names in aliases.items() if comparison_views.norm(row[0]) in names]
            if kind == 'market7':
                label = re.sub(r'\[([^\]]+)\](?:\([^)]*\)|\[[^\]]*\])', r'\1', row[0]).strip()
                exact = {'POD Go':{'POD Go standard','POD Go','POD Go / Wireless','POD Go variants'},'POD Go Wireless':{'POD Go Wireless','POD Go / Wireless','POD Go variants'}}
                matched = [m for m in matched if m not in exact or label in exact[m]]
            assert 1 <= len(matched) <= (2 if kind in ('market1','market7') else 1), 'Unmapped '+kind+' row: '+str(row)
            for model in matched:
                records[model] += [dict(field=h,value=v,source=path,context=context) for h,v in zip(headers[1:],row[1:])]
    expected = {model:({'market1':18,'market2':17,'market3':20,'market4':17,'market5':11,'market6':15,'market7':15}.get(kind,14)) for model in aliases}
    if kind == 'owned':
        expected['GEM BOX original'] = 15
    actual_counts = {model:len(facts) for model,facts in records.items()}
    assert actual_counts == expected, str(actual_counts)
    reports = []
    for model,facts in records.items():
        section_model = 'POD Go and POD Go Wireless' if kind == 'market7' and model in ('POD Go','POD Go Wireless') else model
        section = destinations[files[model]].split('\n## '+section_model+'\n',1)[1].split('\n## ',1)[0]
        reports.append(dict(model=model,facts=facts,missing=[f for f in facts if f['value'] not in section]))
    refs = {m[1].lower():m[2] for m in re.finditer(r'^\[([^\]]+)\]:\s*(\S+)',source,re.M)}
    groups = [p for p in re.split(r'\n\s*\n',source) if p.strip() and not re.match(r'^[#|]',p.strip()) and not re.match(r'^\[[^\]]+\]:',p.strip())]
    normalized = [comparison_views.relink(p,path,refs) for p in groups]
    targets = [re.search(r'\]\(([^)]+)\)',comparison_views.relink('[source]('+target+')',path,{}))[1] for target in refs.values()]
    urls = sorted(set(re.findall(r'https?://[^\s)]+',source)))
    assert len(shared_tables) == (1 if kind == 'market6' else 0)
    report = dict(shared_tables=shared_tables,missing_shared_tables=[table for table in shared_tables if table not in union],source=path,source_sha256=digest(source),records=reports,model_fields=sum(expected.values()),paragraph_groups=len(groups),normalized_missing_groups=[p for p in normalized if p not in union],reference_targets=targets,missing_reference_targets=[t for t in targets if t not in union],external_urls=urls,missing_external_urls=[u for u in urls if u not in union],retirement_authorized=False)
    Path('/tmp/instrumentfx-'+kind+'-union-plan.json').write_text(json.dumps(report,indent=2)+'\n')
    print(kind+' shared union:'+str(len(records))+'models/'+str(sum(expected.values()))+'fields;missingfields='+str(sum(len(r['missing']) for r in reports))+';prosegroups='+str(len(groups))+';missinggroups='+str(len(report['normalized_missing_groups']))+';missingrefs='+str(len(report['missing_reference_targets']))+';missingURLs='+str(len(report['missing_external_urls'])))
    if verify:
        assert not report['missing_shared_tables'], 'Shared appendix table missing'
        assert not any(r['missing'] for r in reports)
        assert not report['normalized_missing_groups'] and not report['missing_reference_targets'] and not report['missing_external_urls']
        manifests = [e for e in state['consolidation_and_price_findings'] if e.get('source') == path and e.get('verification_kind') == 'complete-model-rows-v1']
        assert {e['model_name'] for e in manifests} == set(aliases)
        verify_preserved(state)


def audit_body_differences():
    """Preview normalized pinned bodies against every retained whole-body archive."""
    import difflib
    research_tools.identity()
    state = json.loads(preservation_text('research-state.json'))
    differences = []
    audited = 0
    skipped = 0
    for entry in state.get('consolidation_and_price_findings', []):
        if entry.get('verification_kind') != 'complete-source-body-v1':
            skipped += 1
            continue
        audited += 1
        source = research_tools.read_preserved_source(entry['source'])
        assert digest(source) == entry['source_sha256']
        if entry.get('source_section'):
            fragment = source.split('\n## '+entry['source_section']+'\n',1)[1].split('\n## ',1)[0]
            source = '# '+entry['model_name']+'\n'+fragment
        expected = source.split('\n',1)[1]
        expected = re.sub(r'^## ', '### ', expected, flags=re.M)
        for ref in entry['renamed_references']:
            expected = expected.replace('['+ref+']','['+entry['marker']+'-'+ref+']')
        for old,new in entry.get('link_normalizations',{}).items():
            expected = expected.replace(old,new)
        path = entry['destination'].split('#')[0]
        text = preservation_text(path)
        actual = text.split('<!-- '+entry['marker']+' source begins -->\n',1)[1].split('<!-- '+entry['marker']+' source ends -->',1)[0]
        if actual != expected:
            differences.append(dict(source=entry['source'],destination=path,marker=entry['marker'],before_sha256=digest(actual),expected_body=expected))
            print(''.join(difflib.unified_diff(expected.splitlines(True),actual.splitlines(True),fromfile=entry['source'],tofile=path)))
    Path('/tmp/instrumentfx-preserved-body-differences.json').write_text(json.dumps(differences,indent=2)+'\n')
    print(f'{len(differences)} mismatched whole-body archives across {audited} registered complete-source bodies; {skipped} other ledger entries outside this audit; preview saved under /tmp')


def compact_reference_plan():
    research_tools.identity()
    source = research_tools.read_preserved_source('effects/guitar-compact.md')
    refs = {m[1].lower():m[2] for m in re.finditer(r'^\[([^\]]+)\]:\s*(\S+)', source, re.M)}
    text = (ROOT/'MULTI-EFFECTS.md').read_text()
    changes = []
    for paragraph in re.split(r'\n\s*\n', source):
        if not paragraph.strip() or re.match(r'^[#|\[]', paragraph.strip()):
            continue
        normalized = comparison_views.relink(paragraph, 'effects/guitar-compact.md', refs)
        if normalized != paragraph and paragraph in text:
            changes.append({'before':paragraph,'after':normalized})
    payload = {'path':'MULTI-EFFECTS.md','sha256':digest(text),'changes':changes}
    Path('/tmp/instrumentfx-compact-reference-plan.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps(payload,indent=2))


def commit_preservation_repairs():
    research_tools.identity()
    assert not research_tools.git('diff','--cached','--name-only').strip(), 'Existing staged changes'
    changed = set(research_tools.git('diff','--name-only').splitlines()) | set(research_tools.git('ls-files','--others','--exclude-standard').splitlines())
    allowed = {'Makefile','scripts/consolidation_tools.py','TC-HELICON.md','MULTI-EFFECTS.md','README.md','research-state.json'}
    assert changed and changed <= allowed, changed - allowed
    research_tools.verify()
    comparison_views.verify_views()
    research_tools.git('add','--',*sorted(changed))
    print(research_tools.git('diff','--cached','--stat'))
    print(research_tools.git('commit','-m','audit: reconcile retirement coverage and reject accessory offer'))

if __name__ == '__main__':
    if sys.argv[1:] == ['commit-preservation-repairs']:
        commit_preservation_repairs()
        raise SystemExit(0)
    if sys.argv[1:] == ['compact-reference-plan']:
        compact_reference_plan()
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-body-differences']:
        audit_body_differences()
        raise SystemExit(0)
    if sys.argv[1:] in (['plan-market7-union'], ['audit-market7-union']):
        audit_shared_variant_union(sys.argv[1] == 'audit-market7-union', 'market7')
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-market7-links']:
        audit_compact_links('market7')
        raise SystemExit(0)
    if sys.argv[1:] in (['plan-market6-union'], ['audit-market6-union']):
        audit_shared_variant_union(sys.argv[1] == 'audit-market6-union', 'market6')
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-market6-links']:
        audit_compact_links('market6')
        raise SystemExit(0)
    if sys.argv[1:] in (['plan-market5-union'], ['audit-market5-union']):
        audit_shared_variant_union(sys.argv[1] == 'audit-market5-union', 'market5')
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-market5-links']:
        audit_compact_links('market5')
        raise SystemExit(0)
    if sys.argv[1:] in (['plan-market4-union'], ['audit-market4-union']):
        audit_shared_variant_union(sys.argv[1] == 'audit-market4-union', 'market4')
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-market4-links']:
        audit_compact_links('market4')
        raise SystemExit(0)
    if sys.argv[1:] in (['plan-market3-union'], ['audit-market3-union']):
        audit_shared_variant_union(sys.argv[1] == 'audit-market3-union', 'market3')
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-market3-links']:
        audit_compact_links('market3')
        raise SystemExit(0)
    if sys.argv[1:] in (['plan-market2-union'], ['audit-market2-union']):
        audit_shared_variant_union(sys.argv[1] == 'audit-market2-union', 'market2')
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-market2-links']:
        audit_compact_links('market2')
        raise SystemExit(0)
    if sys.argv[1:] in (['plan-market1-union'], ['audit-market1-union']):
        audit_shared_variant_union(sys.argv[1] == 'audit-market1-union', 'market1')
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-market1-links']:
        audit_compact_links('market1')
        raise SystemExit(0)
    if sys.argv[1:] in (['plan-owned-union'], ['audit-owned-union']):
        audit_shared_variant_union(sys.argv[1] == 'audit-owned-union', 'owned')
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-owned-links']:
        audit_compact_links('owned')
        raise SystemExit(0)
    if sys.argv[1:] in (['plan-cube-union'], ['audit-cube-union']):
        audit_shared_variant_union(sys.argv[1] == 'audit-cube-union')
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-cube-links']:
        audit_compact_links('cube')
        raise SystemExit(0)
    if sys.argv[1:] in (['plan-audota-union'], ['audit-audota-union']):
        audit_audota_union(sys.argv[1] == 'audit-audota-union')
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-audota-links']:
        audit_compact_links('audota')
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-boss-history-links']:
        audit_compact_links('boss-history')
        raise SystemExit(0)
    if sys.argv[1:] in (['plan-boss-history-union'],['audit-boss-history-union']):
        audit_boss_shared(sys.argv[1] == 'audit-boss-history-union', True)
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-boss-links']:
        audit_compact_links('boss')
        raise SystemExit(0)
    if sys.argv[1:] in (['plan-boss-union'],['audit-boss-union']):
        audit_boss_shared(sys.argv[1] == 'audit-boss-union')
        raise SystemExit(0)
    if sys.argv[1:] in (['plan-advanced-union'], ['audit-advanced-union']):
        audit_nux_union(sys.argv[1] == 'audit-advanced-union', 'advanced')
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-advanced-links']:
        audit_compact_links('advanced')
        raise SystemExit(0)
    if sys.argv[1:] == ['plan-advanced-flex']:
        plan_advanced_hxe('Flex Prime')
        raise SystemExit(0)
    if sys.argv[1:] == ['plan-advanced-hxe']:
        plan_advanced_hxe()
        raise SystemExit(0)
    if sys.argv[1:] in (['plan-vocal-union'], ['audit-vocal-union']):
        audit_nux_union(sys.argv[1] == 'audit-vocal-union', 'vocal')
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-vocal-links']:
        audit_compact_links('vocal')
        raise SystemExit(0)
    if sys.argv[1:] in (['plan-bass-union'], ['audit-bass-union']):
        audit_nux_union(sys.argv[1] == 'audit-bass-union', 'bass')
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-bass-links']:
        audit_compact_links('bass')
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-nux-links']:
        audit_compact_links('nux')
        raise SystemExit(0)
    if sys.argv[1:] in (['plan-nux-union'], ['audit-nux-union']):
        audit_nux_union(sys.argv[1] == 'audit-nux-union')
        raise SystemExit(0)
    if sys.argv[1:] == ['plan-nux-mg50li']:
        plan_nux_shared('MG-50Li')
        raise SystemExit(0)
    if sys.argv[1:] == ['plan-nux-mg30']:
        plan_nux_shared('MG-30')
        raise SystemExit(0)
    if sys.argv[1:] == ['plan-nux-mg400']:
        plan_nux_shared('MG-400')
        raise SystemExit(0)
    if sys.argv[1:] == ['plan-nux-mg300mkii']:
        plan_nux_shared('MG-300 MKII')
        raise SystemExit(0)
    if sys.argv[1:] == ['plan-nux-mg300']:
        plan_nux_shared('MG-300 original')
        raise SystemExit(0)
    if sys.argv[1:] == ['plan-nux-mg101']:
        plan_nux_shared()
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-compact-links']:
        audit_compact_links()
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-floorboard-union']:
        audit_floorboard_union()
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-compact-union']:
        audit_compact_union()
        raise SystemExit(0)
    if len(sys.argv) == 3 and sys.argv[1] == 'audit-compact':
        audit_compact(sys.argv[2])
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-legacy']:
        audit_legacy()
        raise SystemExit(0)
    if sys.argv[1:] == ['audit-findings']:
        audit_findings()
        raise SystemExit(0)
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
