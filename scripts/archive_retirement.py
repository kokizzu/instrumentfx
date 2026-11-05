"""Audit exact reachable specialist/archive source revisions before retirement."""
import hashlib
import json
import re
from pathlib import Path
import sys
sys.dont_write_bytecode = True
import research_tools as research
import metadata_consolidation as metadata
from brand_filename_migration import original_namespace

ROOT = research.ROOT
SOURCES = ('effects/specialist.md', 'effects/findings/2026-10-14-flamma-fv01.md')
REPORT = Path('/tmp/instrumentfx-archive-history-audit.json')

def digest(body):
    return hashlib.sha256(body.encode()).hexdigest()

def classify(body, known):
    for kind, text in known.items():
        if body == text:
            return kind
    return 'historical-variant-needs-review'

DESTINATIONS = {
    SOURCES[0]: ('single-guitar.md', '\n## Superseded original specialist comparison\n'),
    SOURCES[1]: ('single-vocal.md', '\n## Superseded original FV01 research wording\n'),
}
PRESERVATION_PLAN = Path('/tmp/instrumentfx-archive-preservation-plan.json')

def render_history(entry, body):
    text = re.sub(r'^(#{1,3}) ', r'##\1 ', body, flags=re.M)
    links = {'(METHODOLOGY.md)': '(README.md#evidence-and-resuming)',
             '(guitar-floorboards.md)': '(all-guitar.md)', '(vocal.md)': '(all-vocal.md)',
             '(COVERAGE.md)': '(README.md#what-remains)'}
    for old, new in links.items():
        text = text.replace(old, new)
    return (DESTINATIONS[entry['source']][1]+'\n'
            +'Historical pre-exclusion wording follows verbatim apart from heading depth and canonical local links. '
            +'Its former classification, queue and dedicated-pedal expansion statements are superseded; '
            +'the six excluded records remain outside active counts. Prices, dates, contradictions and uncertainties retain their original scope.\n\n'
            +'<!-- archive-history:'+entry['blob']+' begins -->\n'+text
            +'<!-- archive-history:'+entry['blob']+' ends -->\n')

def verify_entry(entry, body, current):
    assert entry['source'] in DESTINATIONS
    assert entry['historical'] is True and entry['not_active_instructions'] is True
    assert entry['sha256'] == digest(body)
    assert entry['content'] == metadata.parse_source(entry['source'], body), 'Historical source content altered'
    boundary = DESTINATIONS[entry['source']][1]
    assert current.count(boundary) == 1, 'Missing or duplicated historical archive'
    assert boundary+current.split(boundary, 1)[1] == render_history(entry, body), 'Archived source wording changed'

def without_archive_appendix(path, text, state):
    entries = state['migration'].get('archive_history_preservation', [])
    selected = [entry for entry in entries if entry['destination'] == path]
    if not selected:
        return text
    assert len(selected) == 1
    boundary = DESTINATIONS[selected[0]['source']][1]
    assert text.count(boundary) == 1
    return text.split(boundary, 1)[0]

def history_entries(state):
    entries = state['migration'].get('archive_history_preservation', [])
    if 'archive_history_review_20261105' in state:
        assert len(entries) == state['archive_history_review_20261105']['newly_preserved'] == 2, 'Registered archive body omitted'
        assert {e['source'] for e in entries} == set(SOURCES), 'Registered archive scope changed'
    return entries


def verify_history(state=None):
    if state is None:
        state = json.loads((ROOT/'research-state.json').read_text())
    entries = history_entries(state)
    seen = set()
    for entry in entries:
        key = (entry['source'], entry['blob'])
        assert key not in seen
        seen.add(key)
        body = research.git('cat-file', '-p', entry['blob'])
        assert entry['destination'] == DESTINATIONS[entry['source']][0]
        verify_entry(entry, body, (ROOT/entry['destination']).read_text())
    print('PASS: '+str(len(entries))+' superseded original archive bodies and every parsed nonblank line retained')

def preservation_plan():
    research.identity()
    report = json.loads(REPORT.read_text())
    head = research.git('rev-parse', 'HEAD').strip()
    assert report['head'] == head
    rows = [row for row in report['records'] if row['status'] == 'historical-variant-needs-review']
    assert len(rows) == 2 and {r['source'] for r in rows} == set(SOURCES)
    state = json.loads((ROOT/'research-state.json').read_text())
    assert not state['migration'].get('archive_history_preservation')
    outputs, entries = {}, []
    for row in rows:
        body = research.git('cat-file', '-p', row['blob'])
        assert body == row['body'] and digest(body) == row['sha256']
        path, boundary = DESTINATIONS[row['source']]
        current = (ROOT/path).read_text()
        assert boundary not in current
        entry = dict(source=row['source'], blob=row['blob'], sha256=row['sha256'],
                     destination=path, historical=True, not_active_instructions=True,
                     content=metadata.parse_source(row['source'], body))
        outputs[path] = current+render_history(entry, body)
        verify_entry(entry, body, outputs[path])
        entries.append(entry)
    state['migration']['archive_history_preservation'] = entries
    state['archive_history_review_20261105'] = dict(head=head, sources=2, variants=9,
        newly_preserved=2, scope='Original pre-exclusion wording retained in existing root specialist archives; exclusion and current research queues unchanged.',
        next='Reaudit allnine variants andreaders before any final redirect removal; technical research andexactShopee/display gaps remain.')
    outputs['research-state.json'] = json.dumps(state, ensure_ascii=False, indent=2)+'\n'
    payload = dict(head=head, inputs={p:digest((ROOT/p).read_text()) for p in outputs}, outputs=outputs,
                   rollback=dict(commit=head, exact_paths=list(outputs), condition='Only restore exact reviewed files before subsequent edits; never overwrite unrelated work'))
    PRESERVATION_PLAN.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(dict(plan=str(PRESERVATION_PLAN), paths=list(outputs), entries=[{k:e[k] for k in ('source','blob','sha256','destination')} for e in entries]), indent=2))

def preservation_apply():
    import source_retirement
    research.identity()
    plan = json.loads(PRESERVATION_PLAN.read_text())
    assert research.git('rev-parse', 'HEAD').strip() == plan['head']
    assert set(plan['outputs']) == {'single-guitar.md', 'single-vocal.md', 'research-state.json'}
    for path, sha in plan['inputs'].items():
        assert digest((ROOT/path).read_text()) in (sha, digest(plan['outputs'][path])), 'Input changed: '+path
    for path, body in plan['outputs'].items():
        source_retirement.atomic_write(ROOT/path, body)
    verify_history()

def test():
    assert classify('exact', {'original': 'exact'}) == 'original'
    assert classify('changed', {'original': 'exact'}) == 'historical-variant-needs-review'
    assert classify('exact\n', {'original': 'exact'}) == 'historical-variant-needs-review'
    sample = dict(source=SOURCES[1], blob='a'*40, sha256=digest('# Original\n\nPrice ?\n'),
                  historical=True, not_active_instructions=True,
                  content=metadata.parse_source(SOURCES[1], '# Original\n\nPrice ?\n'))
    body = '# Original\n\nPrice ?\n'
    rendered = render_history(sample, body)
    verify_entry(sample, body, rendered)
    for changed in (rendered.replace('Price ?', 'Price 5'), rendered+'extra claim\n', rendered.replace('Original', 'Altered')):
        try:
            verify_entry(sample, body, changed)
        except AssertionError:
            pass
        else:
            raise AssertionError('Altered archive accepted')
    fixture = {'migration': {'archive_history_preservation': [{'source': p} for p in SOURCES]},
               'archive_history_review_20261105': {'newly_preserved': 2}}
    assert len(history_entries(fixture)) == 2
    for entries in (fixture['migration']['archive_history_preservation'][:1], [{'source': SOURCES[0]}]*2):
        try:
            history_entries(dict(fixture, migration={'archive_history_preservation': entries}))
        except AssertionError:
            pass
        else:
            raise AssertionError('Registered archive source omitted')
    metadata.test_history()
    print('PASS: archive classification requires exact bodies; no dropped history or normalized facts')

def audit():
    research.identity()
    test()
    research.verify()
    state = json.loads((ROOT/'research-state.json').read_text())
    head = research.git('rev-parse', 'HEAD').strip()
    assert research.git('rev-parse', '--is-shallow-repository').strip() == 'false'
    verify_history(state)
    reviewed = {(e['source'], e['blob']): e for e in state['migration'].get('archive_history_preservation', [])}
    rows = []
    for path in SOURCES:
        current = (ROOT/path).read_text()
        original = research.git('show', '9c8d296:'+path)
        assert digest(original) == state['separate_specialist_archives']['source_before_move_sha256'][path]
        known = {'pre-archive-original': original, 'current-redirect': current,
                 'pre-layout-redirect': original_namespace(current, path)}
        if path in state['migration']['retired_sources']:
            known['registered-original'] = research.read_preserved_source(path)
            if path == SOURCES[0]:
                boundary = '\n## Excluded archive — not part of the multi-effects comparison\n'
                assert original.split(boundary,1)[0] == known['registered-original'].split(boundary,1)[0], 'Earlier GM800/context differs from registered source'
        raw = research.git('log', '--full-history', '-m', '--format=', '--raw', '--no-abbrev', '--no-renames', head, '--', path)
        blobs = metadata.history_blobs(raw, path)
        assert blobs, path
        for blob in sorted(blobs):
            body = research.git('cat-file', '-p', blob)
            status = classify(body, known)
            if status == 'historical-variant-needs-review' and (path, blob) in reviewed:
                status = 'verified-superseded-original-archive'
            rows.append(dict(source=path, blob=blob, sha256=digest(body), status=status, body=body))
    counts = {}
    for row in rows:
        counts[row['status']] = counts.get(row['status'], 0)+1
    result = dict(head=head, sources=len(SOURCES), variants=len(rows), counts=counts, records=rows,
                  limitation='Exact reachable archive/specialist body census only; unknown variants require complete preservation review before removal. No files removed.')
    REPORT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'records'}, indent=2))
    print('Review '+str(REPORT))

if __name__ == '__main__':
    if sys.argv[1:] == ['test']:
        test()
    elif sys.argv[1:] == ['audit']:
        audit()
    elif sys.argv[1:] == ['preservation-plan']:
        preservation_plan()
    elif sys.argv[1:] == ['preservation-apply']:
        preservation_apply()
    elif sys.argv[1:] == ['verify']:
        verify_history()
    else:
        raise SystemExit('Use test or audit')
