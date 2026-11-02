"""Reconcile named discovery leads without altering their historical observations."""
import copy
import hashlib
import json
from pathlib import Path
import sys
sys.dont_write_bytecode = True
from research_tools import identity, git, verify
ROOT = Path(__file__).resolve().parents[1]
PLAN = Path('/tmp/instrumentfx-discovery-resolution.json')
ALIASES = {'Fractal Audio': ('Fractal',), 'TC-Helicon': ('TC-HELICON',)}
def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()
def reconcile(state):
    names = {}
    for brand, models in state['inventory_by_brand'].items():
        for model in models:
            key = brand+'::'+model
            for prefix in (brand,)+ALIASES.get(brand, ()):
                names[prefix+' '+model] = key
    result = copy.deepcopy(state['discovery_leads'])
    for lead in result:
        name = lead.get('model')
        if not name:
            continue
        key = names.get(name)
        if key:
            source = state['comparison_model_sources'][key]['link']
            lead['current_resolution'] = dict(status='existing partial canonical profile', model_key=key, canonical_record=source, qualification='Not fully verified; offer identity, condition and stock remain qualified by the original observation and canonical record. Do not add another model.')
        else:
            lead['current_resolution'] = dict(status='exact-name resolution pending', qualification='No exact inventory-name match; this is not proof of absence or a new model. Preserve variant, revision and grouped-lead qualifications; inspect canonical records before admission.')
    return result

def test():
    s = dict(inventory_by_brand={'Fractal Audio':['FM9 MKII Turbo'], 'Valeton':['GP-200']}, comparison_model_sources={'Fractal Audio::FM9 MKII Turbo':{'link':'brand/FRACTAL-AUDIO.md#fm9-mkii-turbo'},'Valeton::GP-200':{'link':'brand/VALETON.md#gp-200'}}, discovery_leads=[{'model':'Fractal FM9 MKII Turbo','status':'Unrecorded','idr':44}, {'model':'Fractal FM9 MKI'}, {'model':'Valeton GP-200X'}, {'model':'Valeton GP-200 identity pending'}, {'models':['grouped']}])
    before = copy.deepcopy(s)
    out = reconcile(s)
    assert s == before, 'Input/history modified'
    assert out[0]['current_resolution']['model_key']=='Fractal Audio::FM9 MKII Turbo'
    assert all(x['current_resolution']['status']=='exact-name resolution pending' for x in out[1:4]), 'Sibling/revision guessed'
    assert out[4]==s['discovery_leads'][4], 'Grouped lead rewritten'
    for old,new in zip(s['discovery_leads'],out):
        assert {k:v for k,v in new.items() if k!='current_resolution'}==old
    print('PASS: exact identity only; sibling/revision/grouped leads not guessed; historical observations unchanged.')

def main(mode):
    identity()
    ledger=ROOT/'research-state.json'
    if mode=='test':
        test(); return
    if mode=='plan':
        text=ledger.read_text(); state=json.loads(text)
        leads=reconcile(state)
        payload=dict(ledger_sha256=digest(text),leads=leads)
        PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
        for i,lead in enumerate(leads):
            print(i,lead.get('model','[grouped/unnamed]'),lead.get('current_resolution',{}).get('status','preserved grouped lead'))
        print('Review',PLAN,'before apply; no inventory or verification status changed.'); return
    if mode=='apply':
        p=json.loads(PLAN.read_text()); text=ledger.read_text()
        assert digest(text)==p['ledger_sha256'], 'Ledger changed since preview'
        state=json.loads(text)
        assert p['leads']==reconcile(state), 'Preview does not match deterministic exact-name resolution'
        state['discovery_leads']=p['leads']
        state['discovery_resolution_scope']='current_resolution supersedes historical discovery status only for queue routing. Exact-name match is not offer authentication, full verification or permission to merge revision-ambiguous leads. Grouped/unnamed leads remain unchanged.'
        ledger.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
        print('Applied reviewed discovery resolutions; historical fields and inventory unchanged.'); return
    assert mode in ('stage','commit')
    verify()
    allowed={'scripts/discovery_resolution.py','Makefile','research-state.json'}
    changed=set(git('diff','--name-only').splitlines())|set(git('ls-files','--others','--exclude-standard').splitlines())
    staged=set(git('diff','--cached','--name-only').splitlines())
    assert (changed|staged)<=allowed
    review=Path('/tmp/instrumentfx-discovery-staged-review.json')
    assert not git('diff','--check').strip()
    if mode=='stage':
        assert changed
        if staged:
            previous=json.loads(review.read_text())
            assert previous['head']==git('rev-parse','HEAD').strip() and previous['sha256']==digest(git('diff','--cached')), 'Existing staging differs from saved review'
        git('add','--',*sorted(changed)); diff=git('diff','--cached')
        Path('/tmp/instrumentfx-discovery-staged.diff').write_text(diff)
        review.write_text(json.dumps(dict(head=git('rev-parse','HEAD').strip(),sha256=digest(diff))))
        print(git('diff','--cached','--stat')); return
    assert staged and not changed
    r=json.loads(review.read_text())
    assert r['head']==git('rev-parse','HEAD').strip() and r['sha256']==digest(git('diff','--cached'))
    assert not git('diff','--cached','--check').strip()
    print(git('commit','-m','research: reconcile stale discovery labels with canonical inventory'))
if __name__=='__main__':
    main(sys.argv[1])
