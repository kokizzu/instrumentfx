"""Index explicit uncertainty in current comparison evidence; never certify completeness."""
import hashlib
import json
from pathlib import Path
import re
import sys
sys.dont_write_bytecode = True
import comparison_views
import research_tools

ROOT = Path(__file__).resolve().parents[1]
PLAN = Path('/tmp/instrumentfx-research-gaps.json')
TOKENS = {
    'unknown': r'unknown',
    'unverified': r'unverified',
    'unresolved': r'unresolved',
    'pending': r'pending',
    'conflict': r'conflict',
    'not_established': r'not\s*established|does\s*not\s*establish',
    'question_mark': r'\?',
}

def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()

def fact_signals(fact):
    value = re.sub(r'\[[^\]]*\]\([^)]*\)', '', fact['value'])
    return [name for name, pattern in TOKENS.items() if (re.search(pattern, value, re.I) or (name != 'question_mark' and re.search(pattern, fact['field'], re.I)))]

def test_signals():
    assert 'conflict' in fact_signals(dict(field='Conversion / dynamic-range conflict', value='Manual 101dB versus product 106dB.'))
    assert 'unverified' in fact_signals(dict(field='Power', value='Current unverified.'))
    assert not fact_signals(dict(field='Display', value='2.4-inch color LCD. [source](https://example.test/?unknown=1)'))
    assert not fact_signals(dict(field='Memory', value='40 user presets.'))
    assert not fact_signals(dict(field='USB-powered?', value='No, requires the DC adapter.'))
    print('PASS: explicit field-label conflicts and value uncertainty are retained; source URLs and verified facts do not create flags.')

def plan():
    research_tools.identity()
    evidence = comparison_views.make_plan(persist=False)
    models = {}
    for key, record in sorted(evidence['records'].items()):
        flags = []
        for fact in record['facts']:
            reasons = fact_signals(fact)
            if reasons:
                entry = dict(field=fact['field'], source=fact['source'], signals=reasons)
                if entry not in flags:
                    flags.append(entry)
        models[key] = dict(link=record['link'], flagged_fields=flags)
    report = dict(scope='Explicit uncertainty signals in selected comparison field labels and values only; omissions, stale historical caveats and semantic conflicts need human review. Zero flags never means fully verified.', model_count=len(models), models_with_signals=sum(bool(m['flagged_fields']) for m in models.values()), flagged_field_count=sum(len(m['flagged_fields']) for m in models.values()), models=models)
    report['source_hashes'] = evidence['input_hashes']
    payload = dict(ledger_sha256=digest((ROOT/'research-state.json').read_text()), input_hashes=evidence['input_hashes'], report=report)
    PLAN.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('models','source_hashes')}, indent=2))
    print('Review '+str(PLAN)+' before applying. No evidence or verification status changed.')

def apply():
    research_tools.identity()
    payload=json.loads(PLAN.read_text())
    ledger=ROOT/'research-state.json'
    assert digest(ledger.read_text())==payload['ledger_sha256'], 'Ledger changed; regenerate plan'
    for path, sha in payload['input_hashes'].items():
        assert digest((ROOT/path).read_text())==sha, 'Evidence changed: '+path
    state=json.loads(ledger.read_text())
    assert payload['report']['model_count']==state['active_model_count']
    state['verification_gap_index']=payload['report']
    temp=ledger.with_suffix('.json.tmp')
    temp.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
    temp.replace(ledger)
    print('Saved reviewed uncertainty index; fully_verified_model_count unchanged.')

def commit():
    research_tools.identity()
    test_signals()
    assert not research_tools.git('diff','--cached','--name-only').strip(), 'Existing staged changes'
    changed=set(research_tools.git('diff','--name-only').splitlines())|set(research_tools.git('ls-files','--others','--exclude-standard').splitlines())
    assert changed and changed <= {'scripts/research_gaps.py','Makefile','research-state.json'}, changed
    research_tools.verify()
    comparison_views.verify_views()
    research_tools.git('add','--',*sorted(changed))
    print(research_tools.git('diff','--cached','--stat'))
    print(research_tools.git('commit','-m','research: refresh uncertainty index for all 388 models'))

if __name__=='__main__':
    assert len(sys.argv)==2 and sys.argv[1] in ('plan','apply','commit','test')
    {'plan':plan,'apply':apply,'commit':commit,'test':test_signals}[sys.argv[1]]()
