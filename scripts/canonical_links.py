"""Plan and apply canonical root navigation without losing historical link spellings."""
import json, re, hashlib, sys
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
PLAN=Path('/tmp/instrumentfx-canonical-links-plan.json')
def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()
def preservation_text(path):
    text=(ROOT/path).read_text()
    if path not in ('MULTI-EFFECTS.md','BOSS.md','MOOER.md','VALETON.md','ZOOM.md','M-VAVE.md'):
        return text
    entry=json.loads((ROOT/'research-state.json').read_text()).get('migration',{}).get('canonical_links',{}).get(path)
    if not entry:
        return text
    return restore_text(text,entry)

def restore_text(text,entry):
    assert text.count('<!-- historical-link:') == len(entry['changes']), 'Historical marker drift'
    for change in entry['changes']:
        assert text.count(change['after']) == 1, 'Missing or duplicated canonical link: '+change['id']
        text=text.replace(change['after'],change['before'])
    return text

def plan(path='MULTI-EFFECTS.md'):
    import research_tools as research
    import source_retirement as shared
    research.identity()
    assert not research.git('diff','--cached','--name-only').strip(), 'Existing staged changes'
    changed=set(research.git('diff','--name-only').splitlines())|set(research.git('ls-files','--others','--exclude-standard').splitlines())
    assert changed <= {'Makefile','scripts/canonical_links.py','scripts/consolidation_tools.py','scripts/navigation_tools.py','BOSS.md','MOOER.md','VALETON.md','ZOOM.md','M-VAVE.md','research-state.json'}, changed
    state=json.loads((ROOT/'research-state.json').read_text())
    assert path in ('MULTI-EFFECTS.md','BOSS.md','MOOER.md','VALETON.md','ZOOM.md','M-VAVE.md')
    assert path not in state['migration'].get('canonical_links',{}), 'Already migrated'
    original=(ROOT/path).read_text()
    changes=[]
    def rewrite(match):
        raw=match[1]
        key=raw.split('#',1)[0]
        if not key.startswith('effects/'):
            return match[0]
        if key == 'effects/findings/2026-10-14-flamma-fv01.md':
            dest='SINGLE-VOCAL.md#flamma-fv01-corrector'
        else:
            assert key in state['migration']['retired_sources'], key
            dest=state['migration']['retired_sources'][key]['destination']
        overrides={'effects/specialist.md':'SINGLE-GUITAR.md','effects/guitar-compact.md':'ALL-GUITAR.md','effects/guitar-floorboards.md':'ALL-GUITAR.md','effects/shopee-indonesia.md':'research-state.json'}
        if key.startswith('effects/shopee-multifx'):
            dest='research-state.json'
        dest=overrides.get(key,dest)
        if raw == 'effects/specialist.md#eligible-record-boss-gm-800':
            dest='BOSS.md#gm-800'
        assert not dest.startswith('effects/'), dest
        shared.validate_target(dest)
        ident=path.removesuffix('.md').lower()+'-'+str(len(changes)+1).zfill(3)
        after=']('+dest+')<!-- historical-link:'+ident+' -->'
        changes.append(dict(id=ident,before=match[0],after=after,original_target=raw,destination=dest))
        return after
    updated=re.sub(r'\]\(([^\s)]+)\)',rewrite,original)
    assert len(changes)=={'MULTI-EFFECTS.md':138,'BOSS.md':43,'MOOER.md':41,'VALETON.md':35,'ZOOM.md':25,'M-VAVE.md':20}[path], len(changes)
    restored=updated
    for change in changes:
        assert restored.count(change['after'])==1
        restored=restored.replace(change['after'],change['before'])
    assert restored==original, 'Non-link content changed'
    assert not [x for x in shared.local_links(path,updated) if x['target'].startswith('effects/')]
    PLAN.write_text(json.dumps(dict(path=path,input_sha256=digest(original),ledger_sha256=digest((ROOT/'research-state.json').read_text()),output=updated,changes=changes),indent=2)+'\n')
    print(json.dumps(dict(plan=str(PLAN),path=path,count=len(changes),changes=[dict(id=c['id'],old=c['original_target'],new=c['destination']) for c in changes]),indent=2))

def apply():
    import research_tools as research
    import source_retirement as shared
    research.identity()
    plan=json.loads(PLAN.read_text())
    path=plan['path']
    assert path in ('MULTI-EFFECTS.md','BOSS.md','MOOER.md','VALETON.md','ZOOM.md','M-VAVE.md')
    assert digest((ROOT/path).read_text())==plan['input_sha256'], 'Category changed since preview'
    assert digest((ROOT/'research-state.json').read_text())==plan['ledger_sha256'], 'Ledger changed since preview'
    state=json.loads((ROOT/'research-state.json').read_text())
    state['migration'].setdefault('canonical_links',{})[path]=dict(changes=plan['changes'],original_sha256=plan['input_sha256'],checked_date='2026-10-18',invariant='Reverse only these marked links to recover exact pre-edit category text;all other content unchanged',rollback='Replace each exact after token with before;remove only this canonical_links entry')
    shared.atomic_write(ROOT/'research-state.json',json.dumps(state,ensure_ascii=False,indent=2)+'\n')
    shared.atomic_write(ROOT/path,plan['output'])
    assert digest(preservation_text(path))==plan['input_sha256']
    print('PASS: '+str(len(plan['changes']))+' reviewed destinations applied;exact inverse reproduces original '+path)

def verify():
    import source_retirement as shared
    import research_tools as research
    research.identity()
    state=json.loads((ROOT/'research-state.json').read_text())
    for path,entry in state['migration']['canonical_links'].items():
        text=(ROOT/path).read_text()
        assert not [x for x in shared.local_links(path,text) if x['target'].startswith('effects/')], path
        restored=preservation_text(path)
        for c in entry['changes']:
            shared.validate_target(c['destination'])
            assert c['before'] in restored
    print('PASS: all migrated canonical destinations exist;all historical tokens recoverable')



def test():
    # Two different historical references may legitimately share a current destination.
    changes=[dict(id='one',before='](effects/old-a.md)',after='](README.md)<!-- historical-link:one -->'),dict(id='two',before='](effects/old-b.md)',after='](README.md)<!-- historical-link:two -->')]
    entry=dict(changes=changes)
    text='Fact and date [A'+changes[0]['after']+'; [B'+changes[1]['after']
    assert restore_text(text,entry)=='Fact and date [A](effects/old-a.md); [B](effects/old-b.md)'
    for broken in (text.replace('historical-link:one','historical-link:unknown'),text+changes[0]['after'],text.replace('](README.md)','](BOSS.md)',1)):
        try:
            restore_text(broken,entry)
        except AssertionError:
            pass
        else:
            raise AssertionError('Corrupt historical provenance accepted')
    print('PASS: shared destinations restore distinct sources;missing,duplicated andaltered provenance rejected')

if __name__=='__main__':
    {'plan':plan,'apply':apply,'verify':verify,'test':test,'plan-boss':lambda:plan('BOSS.md'),'plan-mooer':lambda:plan('MOOER.md'),'plan-valeton':lambda:plan('VALETON.md'),'plan-zoom':lambda:plan('ZOOM.md'),'plan-mvave':lambda:plan('M-VAVE.md')}[sys.argv[1]]()
