"""Plan, apply and audit the user-requested document layout without changing evidence."""
import sys
sys.dont_write_bytecode=True
import hashlib,json,re,posixpath,subprocess,os
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PLAN=Path('/tmp/instrumentfx-final-layout-plan.json')
PREVIOUS=Path('/tmp/instrumentfx-brand-filename-plan.json')
def git(*args):return subprocess.check_output(['git','-c','core.hooksPath=/dev/null',*args],cwd=ROOT,text=True)
def identity():
    assert git('branch','--show-current').strip()=='main'
    assert git('remote','get-url','origin').strip()=='git@github.com:kokizzu/instrumentfx.git'
    assert git('symbolic-ref','refs/remotes/origin/HEAD').strip()=='refs/remotes/origin/main'
def digest(s):return hashlib.sha256(s.encode()).hexdigest()
def translate(s,mapping):
    rx=r'(?<![A-Za-z0-9_-])('+ '|'.join(re.escape(k) for k in sorted(mapping,key=len,reverse=True))+r')(?![A-Za-z0-9_-])'
    return re.sub(rx,lambda m:mapping[m[0]],s)
def relinks(text,source,dest,mapping):
    def target(raw):
        if raw.startswith(('#','/')) or '://' in raw or raw.startswith(('mailto:','data:')):return raw
        path,sep,anchor=raw.partition('#')
        resolved=posixpath.normpath(posixpath.join(posixpath.dirname(source),path))
        resolved=mapping.get(resolved,resolved)
        result=posixpath.relpath(resolved,posixpath.dirname(dest) or '.')
        return result+(sep+anchor if sep else '')
    text=re.sub(r'(?<=\]\()([^\s)]+)',lambda m:target(m[0]),text)
    return re.sub(r'(^\[[^]\n]+\]:\s*)([^\s]+)',lambda m:m[1]+target(m[2]),text,flags=re.M)
def plan():
    identity();oldplan=json.loads(PREVIOUS.read_text());assert oldplan['head']==git('rev-parse','HEAD').strip()
    names=list(oldplan['mapping'])
    mapping={n:'brand/'+n for n in names}
    mapping.update({n:n.lower() for n in ['ALL-GUITAR.md','ALL-BASS.md','ALL-VOCAL.md','SINGLE-GUITAR.md','SINGLE-BASS.md','SINGLE-VOCAL.md']})
    tracked=git('ls-files').splitlines();rows=[]
    for source in tracked:
        if source.startswith('.github/workflows/') or source in ('Makefile','scripts/brand_filename_migration.py'):continue
        try:old=git('show','HEAD:'+source)
        except (subprocess.CalledProcessError,UnicodeError):continue
        dest=mapping.get(source,source)
        current=oldplan['mapping'].get(source,source)
        if not (ROOT/current).is_file():raise AssertionError(current)
        new=translate(old,mapping)
        if source.endswith('.md'):new=relinks(new,source,dest,{})
        if source=='AGENTS.md':
            new=new.replace('root-level **[BRAND].md**','**brand/[BRAND].md**').replace('root brand sections','brand document sections')
        if source=='scripts/brand_sort.py':
            new=new.replace("r'[A-Z0-9-]+", "r'brand/[A-Z0-9-]+").replace("r'\\| \\[[A-Z0-9-]+", "r'\\| \\[brand/[A-Z0-9-]+")
        if source=='research-state.json':
            data=json.loads(new);prior=json.loads(old)
            data['public_metadata']=prior['public_metadata']
            for e in data['public_metadata']['ownership']['entries']:
                if e['root_profile']:e['root_profile']=translate(e['root_profile'],mapping)
            for old_entry,new_entry in zip(prior['consolidation_and_price_findings'],data['consolidation_and_price_findings']):
                for key in ['link_normalizations','retained_context','retained_comparison_facts','retained_source_urls']:
                    if key in old_entry:new_entry[key]=old_entry[key]
            # Historical rewrite tokens remain exact; only their current document keys change.
            data['migration']['canonical_links']={mapping.get(k,k):v for k,v in prior['migration']['canonical_links'].items()}
            data['document_layout_20261102']={'source_head':oldplan['head'],'mapping':mapping,'brand_documents':59,'instruction':'Shopee Indonesia exact hardware offers first;requested separate footswitch screens across LCD/OLED retain priority among available models','historical_namespace':'Pinned metadata and canonical-link inverse tokens retain original spellings;live destinations use new paths'}
            new=json.dumps(data,ensure_ascii=False,indent=2)+'\n'
        if new!=old or source!=dest:
            rows.append(dict(source=source,current=current,destination=dest,before=digest(old),input_sha256=digest((ROOT/current).read_text()),output=new,after=digest(new)))
    PLAN.write_text(json.dumps(dict(head=oldplan['head'],mapping=mapping,files=rows),indent=2)+'\n')
    print(json.dumps(dict(plan=str(PLAN),renames=mapping,changed_paths=[r['destination'] for r in rows]),indent=2))
def apply():
    identity();p=json.loads(PLAN.read_text());assert git('rev-parse','HEAD').strip()==p['head']
    for r in p['files']:
        assert digest((ROOT/r['current']).read_text())==r['input_sha256'],r['current']
        if r['destination']!=r['current']:assert not (ROOT/r['destination']).exists(),r['destination']
    for r in p['files']:
        source=ROOT/r['current'];dest=ROOT/r['destination'];dest.parent.mkdir(parents=True,exist_ok=True)
        if source!=dest:source.rename(dest)
        dest.write_text(r['output'])
    print('Applied reviewed final layout:59 brand documents and6 lowercase category/instrument files')
@lru_cache(maxsize=1)
def layout_mapping():
    return json.loads((ROOT/'research-state.json').read_text())['document_layout_20261102']['mapping']
def original_namespace(text,path):
    rev={v:k for k,v in layout_mapping().items()}
    return translate(relinks(text,path,rev.get(path,path),rev),rev)
def verify():
    identity(); state=json.loads((ROOT/'research-state.json').read_text()); layout=state['document_layout_20261102']
    p={'mapping':layout['mapping'],'files':[]}
    for source in git('ls-tree','-r','--name-only',layout['source_head']).splitlines():
        if source.endswith('.md') and source!='AGENTS.md':
            old=git('show',layout['source_head']+':'+source)
            p['files'].append({'source':source,'destination':p['mapping'].get(source,source),'before':digest(old)})
    for old,new in p['mapping'].items():assert not (ROOT/old).exists() and (ROOT/new).is_file(),new
    assert not list(ROOT.glob('brand-*.md'))
    for r in p['files']:
        if not r['source'].endswith('.md') or r['source']=='AGENTS.md':continue
        now=(ROOT/r['destination']).read_text()
        assert digest(original_namespace(now,r['destination']))==r['before'],r['destination']
    print('PASS:65 document moves;all Markdown evidence byte-identical after inverse path normalization')
def diffcheck():
    result=subprocess.run(['git','diff','--check'],cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    print(result.stdout); print('exit',result.returncode)
def stage():
    identity();p=json.loads(PLAN.read_text())
    if git('diff','--cached','--name-only').strip():
        previous=json.loads(Path('/tmp/instrumentfx-layout-review.json').read_text())
        assert previous['head']==git('rev-parse','HEAD').strip() and previous['sha256']==digest(git('diff','--cached')), 'Existing staged work changed since reviewed checkpoint'
    allowed={r['source'] for r in p['files']}|{r['destination'] for r in p['files']}|{'Makefile','scripts/brand_filename_migration.py','scripts/source_retirement.py'}
    changed=set(git('diff','--name-only').splitlines())|set(git('ls-files','--others','--exclude-standard').splitlines())
    assert changed<=allowed,changed-allowed
    assert not git('diff','--check').strip();git('add','--',*sorted(changed))
    diff=git('diff','--cached');Path('/tmp/instrumentfx-layout-staged.diff').write_text(diff)
    Path('/tmp/instrumentfx-layout-review.json').write_text(json.dumps(dict(head=git('rev-parse','HEAD').strip(),sha256=digest(diff))))
    print(git('diff','--cached','--stat'))
def commit():
    identity();r=json.loads(Path('/tmp/instrumentfx-layout-review.json').read_text())
    assert not git('diff','--name-only').strip() and not git('ls-files','--others','--exclude-standard').strip()
    assert r['head']==git('rev-parse','HEAD').strip() and r['sha256']==digest(git('diff','--cached'))
    assert not git('diff','--cached','--check').strip()
    print(git('commit','-m','docs: move brand profiles and lowercase instrument archives'))
if __name__=='__main__':globals()[sys.argv[1]]()
