"""Losslessly sort root brand sections and navigation; no workflows."""
import collections, hashlib, json, re, subprocess, sys
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
PLAN=Path('/tmp/instrumentfx-brand-sort.json')
START='<!-- brand-index begins -->\n'
END='<!-- brand-index ends -->\n'
def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT,text=True).rstrip()
def identity():
    assert git('branch','--show-current')=='main'
    assert git('remote','get-url','origin') in ['git@github.com:kokizzu/instrumentfx.git','https://github.com/kokizzu/instrumentfx.git']
def key(text):
    return tuple((0,int(p)) if p.isdigit() else (1,p) for p in re.split(r'(\d+)',text.casefold()))
def sections(text):
    matches=list(re.finditer(r'^## (.+)\n',text,re.M))
    if not matches:return text,[]
    return text[:matches[0].start()],[(m.group(1),text[m.start():matches[i+1].start() if i+1<len(matches) else len(text)]) for i,m in enumerate(matches)]
def slug(text):
    return re.sub(r'[^\w\- ]','',text.lower().replace(chr(96),'')).replace(' ','-')
def transform(text):
    prefix,parts=sections(text)
    prefix=re.sub(re.escape(START)+r'.*?'+re.escape(END)+r'\n?', '',prefix,flags=re.S)
    ordered=sorted(parts,key=lambda p:key(p[0]))
    assert len({slug(h) for h,_ in parts})==len(parts), 'Duplicate section anchors require manual handling'
    toc=START+'**Model and section index — A–Z, natural numeric order**\n\n'+''.join(f'- [{h}](#{slug(h)})\n' for h,_ in ordered)+END+'\n'
    result=(prefix+toc+''.join(body.rstrip()+'\n\n' for _,body in ordered)).rstrip()+'\n'
    assert collections.Counter(body.rstrip() for _,body in parts)==collections.Counter(body.rstrip() for _,body in sections(result)[1]),'Section content changed'
    return result

def outputs():
    state=json.loads((ROOT/'research-state.json').read_text())
    result={n:transform((ROOT/n).read_text()) for n in state['root_brand_content']}
    text=(ROOT/'README.md').read_text()
    before,body=text.split('## Root brand documents\n',1)
    table,after=body.split('\n## Research ledger',1)
    lines=table.splitlines(keepends=True)
    indexes=[i for i,line in enumerate(lines) if re.match(r'\| \[[A-Z0-9-]+\.md\]',line)]
    rows=[]
    for i in indexes:
        cells=lines[i].split('|')
        cells[2]=' '+', '.join(sorted(cells[2].strip().split(', '),key=key))+' '
        rows.append('|'.join(cells))
    for i,row in zip(indexes,sorted(rows,key=lambda r:key(re.search(r'\[([^]]+)\]',r).group(1)))):lines[i]=row
    result['README.md']=before+'## Root brand documents\n'+''.join(lines)+'\n## Research ledger'+after
    return result

def test_navigation():
    import comparison_views as cv
    fixture='## PowerHead\n\n[shared]: https://example.test/powerhead\n\n## Head\n\n[shared]: https://example.test/head\n'
    refs=cv.model_references(fixture,'PowerHead')
    assert refs['shared']=='https://example.test/powerhead'
    assert cv.model_references(''.join(reversed([fixture[:fixture.index('## Head')],fixture[fixture.index('## Head'):]])),'PowerHead')==refs
    assert sorted(['GP-100','GP-5','GP-50'],key=key)==['GP-5','GP-50','GP-100']
    print('PASS: natural model order and section-scoped source references survive reordering')

def verify():
    for name,want in outputs().items():assert (ROOT/name).read_text()==want,'Not sorted: '+name
    subprocess.run(['git','diff','--check'],cwd=ROOT,check=True)
    print(f'PASS: all {len(outputs()) - 1} root brand files sorted, indexed, and idempotent; README brand/model navigation sorted')

identity()
mode=sys.argv[1]
if mode=='sync':
    print(git('status','--short'))
    allowed={'Makefile','scripts/brand_sort.py'}
    for line in git('status','--porcelain').splitlines():assert line[3:] in allowed,line
    assert not git('diff','--cached','--name-only')
    subprocess.run(['git','pull','--ff-only'],cwd=ROOT,check=True)
    assert git('symbolic-ref','refs/remotes/origin/HEAD')=='refs/remotes/origin/main'
elif mode=='plan':
    rows=[]
    for name,new in outputs().items():
        old=(ROOT/name).read_text()
        if old!=new:
            rows.append({'path':name,'before_sha256':hashlib.sha256(old.encode()).hexdigest(),'after_sha256':hashlib.sha256(new.encode()).hexdigest(),'sections':len(sections(old)[1])})
            print(name,':', ' -> '.join(h for h,_ in sections(new)[1]))
    PLAN.write_text(json.dumps({'head':git('rev-parse','HEAD'),'files':rows},indent=2))
    print('Planned',len(rows),'documents; section bodies byte-identical')
elif mode=='apply':
    plan=json.loads(PLAN.read_text());assert git('rev-parse','HEAD')==plan['head']
    result=outputs()
    for row in plan['files']:
        path=ROOT/row['path'];assert hashlib.sha256(path.read_bytes()).hexdigest()==row['before_sha256']
        assert hashlib.sha256(result[row['path']].encode()).hexdigest()==row['after_sha256']
    for row in plan['files']:(ROOT/row['path']).write_text(result[row['path']])
    verify()
elif mode=='test':test_navigation()
elif mode=='verify':verify()
elif mode=='commit':
    verify()
    for name in json.loads((ROOT/'research-state.json').read_text())['root_brand_content']:
        original=git('show','HEAD:'+name)
        current=(ROOT/name).read_text()
        assert collections.Counter(b.rstrip() for _,b in sections(original+'\n')[1])==collections.Counter(b.rstrip() for _,b in sections(current)[1]),'Evidence changed: '+name
    names=list(json.loads((ROOT/'research-state.json').read_text())['root_brand_content'])+['README.md','scripts/brand_sort.py','scripts/comparison_views.py','Makefile','AGENTS.md','research-state.json','ALL-GUITAR.md','ALL-BASS.md','ALL-VOCAL.md','MULTI-EFFECTS.md']
    assert not git('diff','--cached','--name-only')
    subprocess.run(['git','add','--',*names],cwd=ROOT,check=True)
    assert set(git('diff','--cached','--name-only').splitlines())<=set(names)
    subprocess.run(['git','diff','--cached','--check'],cwd=ROOT,check=True)
    print(git('diff','--cached','--stat'))
    subprocess.run(['git','commit','-m','docs: sort root brand profiles and add model indexes'],cwd=ROOT,check=True)
else:raise SystemExit(mode)
