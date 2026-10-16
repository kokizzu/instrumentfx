"""Preview and retire consolidated metadata pages with pinned evidence and rollback."""
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import urllib.parse

sys.dont_write_bytecode = True
import metadata_consolidation
import research_tools

ROOT = Path(__file__).resolve().parent.parent
PLAN = Path('/tmp/instrumentfx-metadata-retirement-plan.json')
ROLLBACK = Path('/tmp/instrumentfx-metadata-rollback-plan.json')
CHECKPOINT = Path('/tmp/instrumentfx-metadata-retirement-checkpoint.json')
SOURCES = metadata_consolidation.SOURCES
TOOLS = ('scripts/source_retirement.py','scripts/research_tools.py','scripts/metadata_consolidation.py','Makefile')
OLD_STATUS = 'No source file was deleted. Other legacy records remain until destination contents and incoming links are checked.'
NEW_STATUS = 'All 117 legacy paths are retained as compatibility redirects or JSON pointers: 13 metadata pages, 100 technical pages, one previously redirected excluded archive and three JSON snapshots. Their complete content is preserved in root documents/ledger and pinned Git history. Local navigation and original heading anchors have been audited; compatibility files remain, so the overall migration is not marked complete. Technical verification and market discovery remain incomplete.'

def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()

def headings(text):
    return re.findall(r'^#{1,6} .+$',text,re.M)

def anchors(text):
    used, result = {}, set()
    for heading in headings(text):
        title = heading.lstrip('# ').replace(chr(96),'')
        base = re.sub(r'[^\w\- ]','',title.lower()).replace(' ','-')
        number = used.get(base,0)
        used[base] = number+1
        result.add(base+('-'+str(number) if number else ''))
    return result

def destination(path):
    name = Path(path).name
    if name.startswith('OWNERSHIP') or name == 'SCOPE.md':
        return 'README.md#scope-and-ownership'
    if name.startswith('COVERAGE'):
        return 'README.md#what-remains'
    if name.startswith('shopee-indonesia'):
        return 'MULTI-EFFECTS.md'
    return 'README.md#evidence-and-resuming' if name != 'README.md' else 'README.md'

def validate_target(link):
    path,_,fragment = link.partition('#')
    target = ROOT/path
    assert target.is_file(), 'Missing root destination: '+link
    assert not fragment or fragment in anchors(target.read_text()), 'Missing root anchor: '+link

def local_links(path,text):
    definitions = {m[1].strip().lower():m[2] for m in re.finditer(r'^\[([^\]]+)\]:\s*(\S+)',text,re.M)}
    links = [(m.start(),m[1],'inline') for m in re.finditer(r'\]\(([^\s)]+)',text)]
    for match in re.finditer(r'\[([^\]]+)\]\[([^\]]*)\]',text):
        key = (match[2] or match[1]).strip().lower()
        if key in definitions:
            links.append((match.start(),definitions[key],'reference'))
    for match in re.finditer(r'\[([^\]]+)\](?![\[(])',text):
        if match[1].strip().lower() in definitions:
            links.append((match.start(),definitions[match[1].strip().lower()],'shortcut'))
    links += [(m.start(),m[2],'definition') for m in re.finditer(r'^\[([^\]]+)\]:\s*(\S+)',text,re.M)]
    links += [(m.start(),m[1],'html') for m in re.finditer(r'href=["\x27]([^"\x27]+)["\x27]',text)]
    result = []
    for offset,raw,kind in links:
        parsed = urllib.parse.urlsplit(raw)
        if parsed.scheme or parsed.netloc:
            continue
        target = ((ROOT/path).parent/urllib.parse.unquote(parsed.path)).resolve() if parsed.path else ROOT/path
        try:
            key = str(target.relative_to(ROOT))
        except ValueError:
            continue
        result.append(dict(source=path,line=text.count('\n',0,offset)+1,target=key,fragment=urllib.parse.unquote(parsed.fragment),kind=kind,raw=raw))
    return result

def incoming():
    results = []
    for path in sorted(ROOT.glob('*.md'))+sorted((ROOT/'effects').rglob('*.md')):
        key = str(path.relative_to(ROOT))
        results += [link for link in local_links(key,path.read_text()) if link['target'] in SOURCES]
    return results

def redirect(path,original,commit):
    old_headings = headings(original)
    assert old_headings and old_headings[0].startswith('# ')
    link = destination(path)
    validate_target(link)
    current = '../'+link
    text = old_headings[0]+'\n\nThis legacy metadata page has been consolidated. Use the root documents and ledger for current scope,counts and continuation. Historical queues on this page are retired.\n\n'
    text += '[Current destination]('+current+') · [Complete dated content and provenance](../research-state.json)\n\n'
    text += 'Original source: '+chr(96)+commit+':'+path+chr(96)+'. Original SHA-256: '+chr(96)+digest(original)+chr(96)+'. The complete original is retained in local Git and verified against the structured root ledger.\n\n'
    for heading in old_headings[1:]:
        text += heading+'\n\n[Continue in the root documents]('+current+'). Full dated source details are preserved in [the root ledger](../research-state.json).\n\n'
    assert headings(text) == old_headings and anchors(text) == anchors(original)
    return text

def atomic_write(path,text):
    mode = path.stat().st_mode & 0o777
    with tempfile.NamedTemporaryFile('w',dir=path.parent,prefix='.'+path.name+'.',delete=False) as temp:
        temp.write(text)
        temporary = Path(temp.name)
    os.chmod(temporary,mode)
    os.replace(temporary,path)

def plan():
    research_tools.identity()
    metadata_consolidation.verify()
    state = json.loads((ROOT/'research-state.json').read_text())
    assert not any(p in state['migration'].get('retired_sources',{}) for p in SOURCES)
    commit = research_tools.git('rev-parse','HEAD').strip()
    links = incoming()
    records, outputs = {}, {}
    for path in SOURCES:
        original = (ROOT/path).read_text()
        assert research_tools.git('show',commit+':'+path) == original
        assert digest(original) == state['public_metadata']['sources'][path]['sha256']
        related = [link for link in links if link['target']==path]
        assert all(not link['fragment'] or link['fragment'] in anchors(original) for link in related), 'Unresolved incoming anchor: '+path
        stub = redirect(path,original,commit)
        records[path] = dict(source_commit=commit,source_sha256=digest(original),redirect_sha256=digest(stub),destination=destination(path),original_headings=headings(original),incoming_before=related,status='retired_metadata_redirect',rollback='Restore only this exact path from source_commit,then remove its retired_sources entry')
        outputs[path] = stub
    state['migration'].setdefault('retired_sources',{}).update(records)
    state['migration']['metadata_retirement'] = dict(date='2026-10-17',count=len(records),source_commit=commit,deleted_files=[],historical_anchors_preserved=True,remaining='Technical legacy pages and remaining navigation still require retirement;overall migration incomplete')
    state['cursor'] = dict(model='Metadata redirects and technical source retirement',task='Thirteen consolidated metadata pages now redirect to root documents with original heading anchors. Original evidence remains pinned in Git and root ledger. Next audit/map technical legacy source anchors and preserve Git-backed verification before retiring technical pages;technical gaps and fresh discovery remain.',next_models=[],after_queue='Metadata rollback is available through metadata-retirement-rollback-plan/apply;no source files deleted.')
    readme = (ROOT/'README.md').read_text()
    assert OLD_STATUS in readme
    readme = readme.replace(OLD_STATUS,NEW_STATUS)
    readme = re.sub(r'\n{3,}(?=The root \[research ledger\])','\n\n',readme)
    outputs = {'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n',**outputs,'README.md':readme}
    inputs = {p:digest((ROOT/p).read_text()) for p in (*SOURCES,*TOOLS,'README.md','research-state.json','MULTI-EFFECTS.md')}
    payload = dict(kind='retirement',inputs=inputs,outputs=outputs,source_commit=commit,records=records,scope='Existing consolidated metadata pages only;no technical source changes or deletions')
    PLAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(plan=str(PLAN),source_commit=commit,exact_paths=list(records),incoming_occurrences=len(links),preserved_headings=sum(len(r['original_headings']) for r in records.values()),deleted_files=[]),indent=2))

def apply(plan_path=PLAN):
    research_tools.identity()
    payload = json.loads(plan_path.read_text())
    plan_sha = digest(plan_path.read_text())
    checkpoint = json.loads(CHECKPOINT.read_text()) if CHECKPOINT.exists() else {}
    resuming = checkpoint.get('plan_sha256') == plan_sha
    for path,expected in payload['inputs'].items():
        live = digest((ROOT/path).read_text())
        already_written = path in payload['outputs'] and live == digest(payload['outputs'][path])
        assert live == expected or (resuming and already_written), 'Changed input: '+path
    assert set(payload['outputs']) == set(SOURCES)|{'README.md','research-state.json'}
    checkpoint = dict(plan_sha256=plan_sha,kind=payload['kind'],paths={p:'pending' for p in payload['outputs']})
    CHECKPOINT.write_text(json.dumps(checkpoint,indent=2)+'\n')
    for path,text in payload['outputs'].items():
        if (ROOT/path).read_text() != text:
            atomic_write(ROOT/path,text)
        checkpoint['paths'][path] = 'written'
        CHECKPOINT.write_text(json.dumps(checkpoint,indent=2)+'\n')
    verify()

def verify():
    research_tools.identity()
    state = json.loads((ROOT/'research-state.json').read_text())
    records = state['migration'].get('retired_sources',{})
    if not any(path in records for path in SOURCES):
        metadata_consolidation.verify()
        print('Metadata sources restored;no metadata retirement entries remain.')
        return
    assert all(path in records for path in SOURCES)
    for path in SOURCES:
        entry = records[path]
        original = research_tools.read_preserved_source(path)
        current = (ROOT/path).read_text()
        assert digest(current) == entry['redirect_sha256'], 'Redirect changed: '+path
        assert current == redirect(path,original,entry['source_commit'])
        assert headings(current) == entry['original_headings']
        validate_target(entry['destination'])
    links = incoming()
    for link in links:
        assert not link['fragment'] or link['fragment'] in anchors((ROOT/link['target']).read_text()), 'Incoming anchor lost: '+str(link)
    metadata_consolidation.verify()
    print('PASS:13 metadata redirects;all original headings/incoming anchors and root destinations resolve;complete pinned originals match root metadata;no source deletion.')

def rollback_plan():
    research_tools.identity()
    verify()
    state = json.loads((ROOT/'research-state.json').read_text())
    records = state['migration']['retired_sources']
    originals = {path:research_tools.read_preserved_source(path) for path in SOURCES}
    for path in SOURCES:
        del records[path]
    state['migration']['metadata_retirement']['status'] = 'rolled_back'
    state['cursor']['task'] = 'Metadata redirect retirement rolled back;complete root metadata remains. Review navigation plan before reapplying.'
    readme = (ROOT/'README.md').read_text()
    assert NEW_STATUS in readme
    outputs = {'research-state.json':json.dumps(state,ensure_ascii=False,indent=2)+'\n',**originals,'README.md':readme.replace(NEW_STATUS,OLD_STATUS)}
    inputs = {p:digest((ROOT/p).read_text()) for p in (*SOURCES,*TOOLS,'README.md','research-state.json','MULTI-EFFECTS.md')}
    ROLLBACK.write_text(json.dumps(dict(kind='rollback',inputs=inputs,outputs=outputs),ensure_ascii=False,indent=2)+'\n')
    print('Rollback preview saved: '+str(ROLLBACK)+'; exact restored paths: '+json.dumps(list(SOURCES)))

def commit():
    verify()
    research_tools.verify()
    import subprocess
    subprocess.run([sys.executable,str(ROOT/'scripts/comparison_views.py'),'verify'],check=True)
    subprocess.run([sys.executable,str(ROOT/'scripts/consolidation_tools.py'),'verify'],check=True)
    assert not research_tools.git('diff','--cached','--name-only').strip(), 'Existing staged changes'
    paths = set(SOURCES)|set(TOOLS)|{'README.md','research-state.json'}
    changed = set(research_tools.git('diff','--name-only').splitlines()) | set(research_tools.git('ls-files','--others','--exclude-standard').splitlines())
    assert changed <= paths, changed-paths
    research_tools.git('add','--',*sorted(paths))
    print(research_tools.git('diff','--cached','--stat'))
    print(research_tools.git('commit','-m','docs: retire consolidated metadata into root redirects with pinned provenance'))


JSON_PLAN = Path('/tmp/instrumentfx-json-retirement-plan.json')
JSON_PATHS = metadata_consolidation.JSON_SOURCES

def json_pointer(path,entry):
    return json.dumps(dict(status='retired_historical_snapshot',current_ledger='../research-state.json',preserved_content='public_metadata.legacy_json.unique_snapshots.'+entry['source_sha256'],source_commit=entry['source_commit'],source_path=path,source_sha256=entry['source_sha256'],not_current_inventory_or_cursor=True),ensure_ascii=False,indent=2)+'\n'

def json_incoming():
    return [link for path in sorted(ROOT.glob('*.md'))+sorted((ROOT/'effects').rglob('*.md')) for link in local_links(str(path.relative_to(ROOT)),path.read_text()) if link['target'] in JSON_PATHS]

def json_verify():
    research_tools.identity()
    metadata_consolidation.verify()
    state=json.loads((ROOT/'research-state.json').read_text())
    retired=state['migration'].get('retired_sources',{})
    archive=state['public_metadata']['legacy_json']
    for path in JSON_PATHS:
        original=research_tools.read_preserved_source(path)
        index=archive['source_index'][path]
        assert digest(original)==index['sha256']
        groups=archive['unique_snapshots'][index['snapshot']]['groups']
        restored={key:value for group in groups.values() for key,value in group.items()}
        assert json.dumps(restored,sort_keys=True)==json.dumps(json.loads(original),sort_keys=True),'Typed JSON loss: '+path
        if path in retired:
            assert (ROOT/path).read_text()==json_pointer(path,retired[path])
            assert digest((ROOT/path).read_text())==retired[path]['redirect_sha256']
    for link in json_incoming():
        assert (ROOT/link['target']).is_file() and not link['fragment'],str(link)
    print('PASS:3 original JSON files/2 unique typed snapshots reconstructed exactly;current ledger,provenance and incoming paths resolve.')

def json_plan(rollback=False):
    json_verify()
    state=json.loads((ROOT/'research-state.json').read_text())
    records=state['migration'].setdefault('retired_sources',{})
    selected=[p for p in JSON_PATHS if (p in records)==rollback]
    assert len(selected)==3,'JSON retirement is all-or-none'
    commit=research_tools.git('rev-parse','HEAD').strip()
    outputs={}
    for path in selected:
        original=research_tools.read_preserved_source(path)
        if rollback:
            outputs[path]=original
            del records[path]
        else:
            assert research_tools.git('show',commit+':'+path)==original
            entry=dict(source_commit=commit,source_sha256=digest(original),destination='research-state.json',status='retired_json_pointer',incoming_before=[l for l in json_incoming() if l['target']==path])
            outputs[path]=json_pointer(path,entry)
            entry['redirect_sha256']=digest(outputs[path])
            records[path]=entry
    state['migration']['legacy_json_retirement']=dict(status='rolled_back' if rollback else 'retired',source_paths=list(JSON_PATHS),source_count=3,unique_snapshots=2,typed_root_content_verified=True,no_source_deletion=True)
    state['cursor'].update(model='Complete navigation and field coverage audit',task='All legacy JSON snapshots have typed root-ledger provenance and pinned originals;all technical/metadata Markdown pages are redirects. Audit every legacy path and live navigation before claiming organization complete;technical gaps and fresh Shopee discovery remain.')
    outputs['research-state.json']=json.dumps(state,ensure_ascii=False,indent=2)+'\n'
    inputs={p:digest((ROOT/p).read_text()) for p in [*outputs,'scripts/source_retirement.py','scripts/metadata_consolidation.py','Makefile']}
    JSON_PLAN.write_text(json.dumps(dict(inputs=inputs,outputs=outputs,kind='rollback' if rollback else 'retire',rollback_commit=commit),ensure_ascii=False,indent=2)+'\n')
    print('Exact JSON plan: '+str(JSON_PLAN)+';paths='+json.dumps(list(outputs)))

def json_apply():
    research_tools.identity()
    payload=json.loads(JSON_PLAN.read_text())
    assert set(payload['outputs'])==set(JSON_PATHS)|{'research-state.json'}
    for path,sha in payload['inputs'].items():
        current=(ROOT/path).read_text()
        assert digest(current)==sha or payload['outputs'].get(path)==current,'Changed input: '+path
    for path in ['research-state.json',*JSON_PATHS]:
        atomic_write(ROOT/path,payload['outputs'][path])
    json_verify()

def json_commit():
    json_verify()
    research_tools.verify()
    import comparison_views
    comparison_views.verify_views()
    assert not research_tools.git('diff','--cached','--name-only').strip(),'Existing staged changes'
    changed=set(research_tools.git('diff','--name-only').splitlines())|set(research_tools.git('ls-files','--others','--exclude-standard').splitlines())
    allowed=set(JSON_PATHS)|{'research-state.json','scripts/source_retirement.py','scripts/metadata_consolidation.py','Makefile'}
    assert changed<=allowed,changed-allowed
    research_tools.git('add','--',*sorted(changed))
    print(research_tools.git('diff','--cached','--stat'))
    print(research_tools.git('commit','-m','docs: retire legacy JSON snapshots with typed root provenance'))

if __name__ == '__main__':
    modes = {'json-plan':json_plan,'json-apply':json_apply,'json-verify':json_verify,'json-commit':json_commit,'json-rollback-plan':lambda:json_plan(True),'plan':plan,'apply':apply,'verify':verify,'commit':commit,'rollback-plan':rollback_plan,'rollback-apply':lambda:apply(ROLLBACK)}
    modes[sys.argv[1]]()
