"""Review and publish sourced model pictures one model at a time."""
import hashlib, html, json, re, subprocess, sys, time, urllib.parse, urllib.request
from urllib.error import HTTPError, URLError
from pathlib import Path
import firmware_pitch as audit
import firmware_publish as publish
ROOT=audit.ROOT
INPUT=Path('/tmp/instrumentfx-images.json')
PLAN=Path('/tmp/instrumentfx-images-plan.json')
RECEIPT=Path('/tmp/instrumentfx-images-review.json')
ARCHIVE_PLAN=Path('/tmp/instrumentfx-image-archive-plan.json')
def local_asset(value):
 assert re.fullmatch(r'images/[a-z0-9][a-z0-9-]{1,140}\.(?:png|jpe?g|webp|gif|bmp|avif)', value), 'Invalid local image path'
 return ROOT/'brand'/value

def atomic_write(path, body):
 path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
 tmp=path.with_name('.'+path.name+'.tmp')
 tmp.write_bytes(body);tmp.replace(path)

def image_extension(body, content_type):
 if body.startswith(b'\xff\xd8\xff'): return 'jpg'
 if body.startswith(b'\x89PNG\r\n\x1a\n'): return 'png'
 if len(body)>=12 and body[:4]==b'RIFF' and body[8:12]==b'WEBP': return 'webp'
 if body.startswith((b'GIF87a',b'GIF89a')): return 'gif'
 if body.startswith(b'BM'): return 'bmp'
 if len(body)>=12 and body[4:8]==b'ftyp' and body[8:12] in (b'avif',b'avis'): return 'avif'
 return {'image/jpeg':'jpg','image/png':'png','image/webp':'webp','image/gif':'gif','image/bmp':'bmp','image/avif':'avif'}.get(content_type)

def checked_worktree():
 assert not publish.git('diff','--cached','--name-only'),'Staged work must be preserved'
 assert not publish.git('diff','--name-only'),'Working-tree changes must be preserved'
 assert not publish.git('ls-files','--others','--exclude-standard'),'Untracked work must be preserved'

def archive_plan(limit):
 publish.identity();checked_worktree()
 assert isinstance(limit,int) and limit>0
 state=json.loads((ROOT/'research-state.json').read_text());models=[]
 for key,record in state['model_images']['models'].items():
  views={v:{'url':x['image_url'],'sha256':x['sha256']} for v,x in record.get('views',{}).items() if x.get('image_url','').startswith('https://')}
  if views: models.append({'key':key,'views':views})
  if len(models)>=limit: break
 plan={'format':'instrumentfx-image-archive-v1','head':publish.git('rev-parse','HEAD'),'limit':limit,'models':models,'cursor':0,'blocked_hosts':[],'failures':[],'localized_models':0,'localized_views':0}
 atomic_write(ARCHIVE_PLAN,json.dumps(plan,ensure_ascii=False,sort_keys=True).encode())
 print(f"PLAN {len(models)} models / {sum(len(x['views']) for x in models)} remote image files; exact original bytes, SHA-256 verified; destinations brand/images/{{model-view-hash}}.{{format}}")
 for item in models: print(item['key'],', '.join(f"{v}:{x['sha256'][:12]}" for v,x in item['views'].items()))
 print('BASE',plan['head'])

def image_download(url):
 req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 InstrumentFX-image-archive/1.0'})
 with urllib.request.urlopen(req,timeout=45) as response:
  content_type=response.headers.get_content_type()
  assert content_type.startswith('image/'),f'Not an image response: {content_type}'
  body=response.read(8000001)
 assert len(body)<=8000000,'Source image exceeds 8 MB cap'
 return body,content_type

def archive_commit(key, record, created_assets):
 publish.identity()
 state=json.loads((ROOT/'research-state.json').read_text())
 page=state['comparison_model_sources'][key]['link'].split('#')[0]
 assert block(record) in (ROOT/page).read_text(),'Canonical image gallery is stale'
 for view in record['views'].values():
  if not view['image_url'].startswith('https://'):
   assert hashlib.sha256(local_asset(view['image_url']).read_bytes()).hexdigest()==view['sha256']
 import coverage_views as coverage
 expected=coverage.outputs(state)
 for rel,body in expected.items(): assert (ROOT/rel).read_text()==body,('Stale generated view',rel)
 allowed=set(expected)|{page,'research-state.json'}|set(created_assets)
 changed=set(publish.git('diff','--name-only').splitlines())|set(publish.git('ls-files','--others','--exclude-standard').splitlines())
 assert changed<=allowed,('Unrelated changes',sorted(changed-allowed))
 assert changed,'No local image changes to commit'
 subprocess.run(['git','add','--',*sorted(changed)],cwd=ROOT,check=True)
 subprocess.run(['git','diff','--cached','--check'],cwd=ROOT,check=True)
 diff=publish.git('diff','--cached')
 assert diff
 print(publish.git('diff','--cached','--stat'))
 subprocess.run(['git','commit','-m','docs(images): archive '+key.replace('::',' ')+' source images'],cwd=ROOT,check=True)
 subprocess.run(['git','push','origin','main:main'],cwd=ROOT,check=True)
 head=publish.git('rev-parse','HEAD')
 assert publish.git('ls-remote','origin','refs/heads/main').split()[0]==head
 print('PUSH_VERIFIED',publish.git('rev-parse','--short','HEAD'))
 return head

def archive(limit):
 plan=json.loads(ARCHIVE_PLAN.read_text())
 assert plan['format']=='instrumentfx-image-archive-v1' and plan['limit']==limit
 assert plan['head']==publish.git('rev-parse','HEAD')
 host_blocks=set(plan['blocked_hosts']);state=json.loads((ROOT/'research-state.json').read_text())
 local_by_hash={}
 for rec in state['model_images']['models'].values():
  for view in rec.get('views',{}).values():
   if not view.get('image_url','').startswith('https://'):
    local_by_hash[view['sha256']]=view['image_url']
 attempted=0
 for position,item in enumerate(plan['models']):
  if position<plan['cursor']: continue
  checked_worktree();publish.identity()
  state=json.loads((ROOT/'research-state.json').read_text());key=item['key'];record=json.loads(json.dumps(state['model_images']['models'][key]))
  created=[];success=0
  for view,expected in item['views'].items():
   current=record['views'].get(view)
   if not current or current['image_url']!=expected['url'] or current['sha256']!=expected['sha256']:
    if current and not current['image_url'].startswith('https://'): continue
    raise AssertionError(('Image source changed since plan',key,view))
   url=expected['url'];host=urllib.parse.urlsplit(url).netloc.lower()
   if host in host_blocks:
    plan['failures'].append({'model':key,'view':view,'status':'host blocked earlier','host':host});continue
   try:
    if expected['sha256'] in local_by_hash:
     existing=local_asset(local_by_hash[expected['sha256']])
     assert hashlib.sha256(existing.read_bytes()).hexdigest()==expected['sha256']
     record['views'][view]['image_url']=local_by_hash[expected['sha256']];success+=1;continue
    body,content_type=image_download(url)
    digest=hashlib.sha256(body).hexdigest()
    if digest!=expected['sha256']:
     plan['failures'].append({'model':key,'view':view,'status':'source hash changed','host':host,'expected':expected['sha256'],'actual':digest});continue
    ext=image_extension(body,content_type)
    if not ext:
     plan['failures'].append({'model':key,'view':view,'status':'unsupported image encoding','host':host,'content_type':content_type});continue
    slug=re.sub(r'[^a-z0-9]+','-',key.lower()).strip('-')[:78].strip('-')
    rel=f'images/{slug}-{view}-{digest[:12]}.{ext}';dest=local_asset(rel)
    if dest.exists(): assert hashlib.sha256(dest.read_bytes()).hexdigest()==digest,'Asset path collision'
    else: atomic_write(dest,body);created.append(str(dest.relative_to(ROOT)))
    record['views'][view]['image_url']=rel;local_by_hash[digest]=rel;success+=1
    print('FETCHED',key,view,len(body),rel,flush=True)
   except HTTPError as e:
    plan['failures'].append({'model':key,'view':view,'status':'HTTP '+str(e.code),'host':host})
    if e.code in (401,403,429): host_blocks.add(host)
   except (URLError,TimeoutError,OSError,AssertionError) as e:
    plan['failures'].append({'model':key,'view':view,'status':str(e)[:220],'host':host})
   time.sleep(.15)
  if success:
   atomic_write(INPUT,json.dumps(record,ensure_ascii=False).encode())
   plan_fn=globals()['plan'];apply_fn=globals()['apply'];plan_fn();apply_fn()
   plan['head']=archive_commit(key,record,created)
   plan['localized_models']+=1;plan['localized_views']+=success
  else: print('SKIPPED',key,'no source could be archived',flush=True)
  plan['blocked_hosts']=sorted(host_blocks);plan['cursor']=position+1
  atomic_write(ARCHIVE_PLAN,json.dumps(plan,ensure_ascii=False,sort_keys=True).encode())
  attempted+=1
  if attempted%10==0: print('PROGRESS',plan['cursor'],'/',len(plan['models']),'models;',plan['localized_views'],'views localized',flush=True)
  time.sleep(.2)
 print('ARCHIVE_RESULT',json.dumps({'models_processed':plan['cursor'],'models_localized':plan['localized_models'],'views_localized':plan['localized_views'],'remaining_remote':sum(1 for r in json.loads((ROOT/'research-state.json').read_text())['model_images']['models'].values() for v in r.get('views',{}).values() if v['image_url'].startswith('https://')),'blocked_hosts':plan['blocked_hosts'],'failures':len(plan['failures'])},ensure_ascii=False))

def diagram():
 """Render a bounded, explicitly selected source-manual figure; never install firmware."""
 publish.identity()
 r=json.loads(INPUT.read_text()); s=json.loads((ROOT/'research-state.json').read_text())
 assert r['model_key'] in audit.inventory(s)
 d=r['manual_diagram']
 sources={
  'https://cdn.korg.com/us/support/download/files/16704ca55ffe2b8116eaa1fb8857c173.pdf':'Korg::AX10B',
  'https://data.yamaha.com/files/download/other_assets/1/334091/magicstomp_bass_en.pdf':'Yamaha::Magicstomp Bass',
  'https://cdn.korg.com/us/support/download/files/19ca0336fc87d09bb65f5ed34a0a4edc.pdf':'Korg::AX3000B',
  'https://www.danguitar.dk/pub/assets/MVA-MINIX.pdf':'M-VAVE::MINI-X',
 }
 assert sources.get(d['source_url'])==r['model_key'], 'Manual must match reviewed exact model'
 page=d['page']; assert isinstance(page,int) and 1<=page<=128
 request=urllib.request.Request(d['source_url'],headers={'User-Agent':'InstrumentFX-source-review/1.0'})
 with urllib.request.urlopen(request,timeout=30) as response:
  assert response.geturl()==d['source_url']
  body=response.read(8000001)
 assert body.startswith(b'%PDF-') and len(body)<=8000000
 if d.get('source_sha256'):
  assert hashlib.sha256(body).hexdigest()==d['source_sha256'], 'Manual changed; review source before extracting'
 pdf=Path('/tmp/instrumentfx-diagram.pdf');pdf.write_bytes(body)
 subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-scale-to','2400','-singlefile','-png',str(pdf),'/tmp/instrumentfx-diagram-page'],check=True,timeout=30)
 from PIL import Image
 image_path=Path('/tmp/instrumentfx-diagram-page.png')
 with Image.open(image_path) as picture:
  crop=d.get('crop')
  if crop:
   assert len(crop)==4 and all(isinstance(n,int) for n in crop)
   assert 0<=crop[0]<crop[2]<=picture.width and 0<=crop[1]<crop[3]<=picture.height
   picture=picture.crop(crop)
   image_path=Path('/tmp/instrumentfx-diagram-crop.png');picture.save(image_path,optimize=True)
  print(json.dumps({'source_sha256':hashlib.sha256(body).hexdigest(),'page':page,'crop':crop,'image':str(image_path),'size':picture.size,'sha256':hashlib.sha256(image_path.read_bytes()).hexdigest()}))

def data():
 r=json.loads(INPUT.read_text());s=json.loads((ROOT/'research-state.json').read_text())
 assert r['model_key'] in audit.inventory(s)
 assert r['views'] and set(r['views']) <= {'top','rear'}
 for v in r['views'].values():
  assert v['source_url'].startswith('https://')
  if not v['image_url'].startswith('https://'):
   asset=local_asset(v['image_url'])
   assert asset.is_file() and hashlib.sha256(asset.read_bytes()).hexdigest()==v['sha256']
 return r,s
def plan():
 publish.identity();r,s=data()
 path=s['comparison_model_sources'][r['model_key']]['link'].split('#')[0]
 p={'record':r,'path':path,'before':hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),'head':publish.git('rev-parse','HEAD')}
 PLAN.write_text(json.dumps(p));print(json.dumps(p,indent=2))
def fetch():
 p=json.loads(PLAN.read_text())
 for view,v in p['record']['views'].items():
  if not v['image_url'].startswith('https://'):
   asset=local_asset(v['image_url']);print(view,str(asset),hashlib.sha256(asset.read_bytes()).hexdigest());continue
  req=urllib.request.Request(v['image_url'],headers={'User-Agent':'Mozilla/5.0'})
  with urllib.request.urlopen(req,timeout=45) as res:
   assert res.headers.get_content_type().startswith('image/')
   body=res.read(8000001);assert len(body)<=8000000
  dest=Path('/tmp/instrumentfx-image-'+view);dest.write_bytes(body)
  print(view,str(dest),len(body),hashlib.sha256(body).hexdigest())
def block(r):
 key=r['model_key'];out=[f'<!-- model-images:{key} begins -->','<details>','<summary>Product pictures — top and rear ports</summary>','']
 for view in ('top','rear'):
  v=r['views'].get(view)
  if not v:
   out += [f'**{view.title()} view:** not yet verified.',''];continue
  assert v.get('visual_checked'), 'Inspect downloaded photograph first'
  out += [f"**{v['caption']}**",'',f"[![{v['caption']}]({v['image_url']})]({v['image_url']})",'',f"[Image source]({v['source_url']}). {v['note']}",'']
 out += ['</details>',f'<!-- model-images:{key} ends -->','']
 return '\n'.join(out)
def replace_gallery(text,old,new):
 before=block(old);after=block(new)
 assert old['model_key']==new['model_key'], 'Cannot replace a different model'
 assert text.count(before)==1, 'Existing gallery differs from recorded content; preserve manual edits'
 return text.replace(before,after,1)
def test():
 r={'model_key':'Example::One','views':{'top':{'caption':'Top','image_url':'https://example.com/a.jpg','source_url':'https://example.com/','note':'Original','visual_checked':True}}}
 n=json.loads(json.dumps(r));n['views']['top']['note']='Updated'
 original='prefix\n'+block(r)+'suffix\n'
 assert replace_gallery(original,r,n)=='prefix\n'+block(n)+'suffix\n'
 for changed in (original.replace('Original','Manual edit'), original+block(r), 'missing'):
  try: replace_gallery(changed,r,n)
  except AssertionError: pass
  else: raise AssertionError('Unsafe gallery replacement accepted')
 assert local_asset('images/korg-ax10b-rear.png')==ROOT/'brand/images/korg-ax10b-rear.png'
 assert local_asset('images/digitech-rp500-top-263040d83c09.jpg')==ROOT/'brand/images/digitech-rp500-top-263040d83c09.jpg'
 assert local_asset('images/helix-floor-top-abcdef123456.webp')==ROOT/'brand/images/helix-floor-top-abcdef123456.webp'
 assert image_extension(b'\xff\xd8\xffsample','image/jpeg')=='jpg'
 assert image_extension(b'\x89PNG\r\n\x1asample','image/png')=='png'
 assert image_extension(b'RIFFxxxxWEBPsample','image/webp')=='webp'
 for unsafe in ('../secret.png','images/../../secret.png','images/x.svg','https://example.com/a.png','images/a.png?x=1'):
  try: local_asset(unsafe)
  except AssertionError: pass
  else: raise AssertionError('Unsafe local asset accepted')
 print('PASS local image path confinement and content-type detection')
 print('PASS gallery replacement preserves surrounding text and rejects manual edits, duplicate or missing blocks')
def apply():
 publish.identity();p=json.loads(PLAN.read_text());r,s=data()
 assert r==p['record'] and p['head']==publish.git('rev-parse','HEAD')
 path=ROOT/p['path'];assert hashlib.sha256(path.read_bytes()).hexdigest()==p['before']
 key=r['model_key'];text=path.read_text()
 old=s.get('model_images',{}).get('models',{}).get(key)
 if old:
  text=replace_gallery(text,old,r)
 else:
  assert f'<!-- model-images:{key} begins -->' not in text
  marker=f'<!-- firmware-pitch:{key} ends -->'
  assert marker in text,'Model requires canonical audit before image addition'
  text=text.replace(marker,marker+'\n\n'+block(r),1)
 path.write_text(text)
 gallery=s.setdefault('model_images',{'models':{},'scope':'All active models; powered-on top and rear-port photographs; absent views explicitly pending','hover':'GitHub strips CSS/JS; use expandable pictures and direct image links','hover_source':'https://github.com/github/markup#github-markup'})
 gallery['models'][key]=r;gallery['last_model']=key
 (ROOT/'research-state.json').write_text(json.dumps(s,indent=2,ensure_ascii=False)+'\n')
 refresh_views(s)
 print('APPLIED',key)

def refresh_views(s):
 import coverage_views as coverage
 for rel,body in coverage.outputs(s).items():
  path=ROOT/rel
  if not path.is_file() or path.read_text()!=body:
   atomic_write(path,body.encode())
def verify():
 publish.identity();s=json.loads((ROOT/'research-state.json').read_text())
 for key,r in s['model_images']['models'].items():
  path=s['comparison_model_sources'][key]['link'].split('#')[0]
  assert block(r) in (ROOT/path).read_text()
  for v in r['views'].values():
   if not v['image_url'].startswith('https://'):
    assert hashlib.sha256(local_asset(v['image_url']).read_bytes()).hexdigest()==v['sha256']
 subprocess.run(['make','coverage-verify'],cwd=ROOT,check=True)
 subprocess.run(['git','diff','--check'],cwd=ROOT,check=True)
 print('PASS image records and existing catalogue comparisons')
def review():
 verify();p=json.loads(PLAN.read_text());s=json.loads((ROOT/'research-state.json').read_text());paths=[p['path'],'research-state.json','Makefile','make/images.mk','scripts/model_images.py']
 paths += ['scripts/coverage_views.py','scripts/comparison_views.py']
 paths += [str(local_asset(v['image_url']).relative_to(ROOT)) for v in p['record']['views'].values() if not v['image_url'].startswith('https://')]
 import coverage_views as coverage
 paths += list(coverage.outputs(s))
 assert not publish.git('diff','--cached','--name-only')
 changed=set(publish.git('diff','--name-only').splitlines())|set(publish.git('ls-files','--others','--exclude-standard').splitlines())
 assert changed<=set(paths),changed-set(paths)
 subprocess.run(['git','add','--']+sorted(changed),cwd=ROOT,check=True)
 r={'head':publish.git('rev-parse','HEAD'),'model':p['record']['model_key'],'paths':sorted(changed),'sha256':hashlib.sha256(publish.git('diff','--cached').encode()).hexdigest()}
 RECEIPT.write_text(json.dumps(r));print(publish.git('diff','--cached','--stat'));print('REVIEW',r);print('STAGED_DIFF_BEGIN');print(publish.git('diff','--cached'))
def commit():
 publish.identity();r=json.loads(RECEIPT.read_text())
 assert r['head']==publish.git('rev-parse','HEAD')
 assert r['paths']==sorted(publish.git('diff','--cached','--name-only').splitlines())
 assert r['sha256']==hashlib.sha256(publish.git('diff','--cached').encode()).hexdigest()
 assert not publish.git('diff','--name-only')
 if any(path.startswith('brand/images/') for path in r['paths']): message='docs(images): archive '+r['model'].replace('::',' ')+' source images'
 elif 'scripts/model_images.py' in r['paths'] and 'make/images.mk' in r['paths']: message='feat(images): archive verified product photos locally'
 elif 'make/images.mk' in r['paths']: message='feat(images): default archive target to full catalogue'
 else: message='docs(images): update '+r['model'].replace('::',' ')+' pictures'
 subprocess.run(['git','commit','-m',message],cwd=ROOT,check=True)
 subprocess.run(['git','push','origin','main:main'],cwd=ROOT,check=True)
 assert publish.git('ls-remote','origin','refs/heads/main').split()[0]==publish.git('rev-parse','HEAD')
 print('PUSH_VERIFIED',publish.git('rev-parse','--short','HEAD'))
if __name__=='__main__':
 {'diagram':diagram,'test':test,'plan':plan,'fetch':fetch,'apply':apply,'verify':verify,'review':review,'commit':commit,'archive-plan':lambda:archive_plan(int(sys.argv[2])),'archive':lambda:archive(int(sys.argv[2]))}[sys.argv[1]]()
