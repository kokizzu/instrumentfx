"""Review and publish sourced model pictures one model at a time."""
import hashlib, html, json, re, subprocess, sys, urllib.request
from pathlib import Path
import firmware_pitch as audit
import firmware_publish as publish
ROOT=audit.ROOT
INPUT=Path('/tmp/instrumentfx-images.json')
PLAN=Path('/tmp/instrumentfx-images-plan.json')
RECEIPT=Path('/tmp/instrumentfx-images-review.json')
def local_asset(value):
 assert re.fullmatch(r'images/[a-z0-9][a-z0-9-]{1,100}\.png', value), 'Invalid local diagram path'
 return ROOT/'brand'/value

def diagram():
 """Render a bounded, explicitly selected original-manual figure; never install firmware."""
 publish.identity()
 r=json.loads(INPUT.read_text()); s=json.loads((ROOT/'research-state.json').read_text())
 assert r['model_key'] in audit.inventory(s)
 d=r['manual_diagram']
 assert d['source_url']=='https://cdn.korg.com/us/support/download/files/16704ca55ffe2b8116eaa1fb8857c173.pdf'
 page=d['page']; assert isinstance(page,int) and 1<=page<=128
 request=urllib.request.Request(d['source_url'],headers={'User-Agent':'InstrumentFX-source-review/1.0'})
 with urllib.request.urlopen(request,timeout=30) as response:
  assert response.geturl()==d['source_url']
  body=response.read(8000001)
 assert body.startswith(b'%PDF-') and len(body)<=8000000
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
 for unsafe in ('../secret.png','images/../../secret.png','images/x.svg','https://example.com/a.png','images/a.png?x=1'):
  try: local_asset(unsafe)
  except AssertionError: pass
  else: raise AssertionError('Unsafe local asset accepted')
 print('PASS local diagram path confinement')
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
 print('APPLIED',key)
def verify():
 publish.identity();s=json.loads((ROOT/'research-state.json').read_text())
 for key,r in s['model_images']['models'].items():
  path=s['comparison_model_sources'][key]['link'].split('#')[0]
  assert block(r) in (ROOT/path).read_text()
  for v in r['views'].values():
   if not v['image_url'].startswith('https://'):
    assert hashlib.sha256(local_asset(v['image_url']).read_bytes()).hexdigest()==v['sha256']
 subprocess.run(['make','research-verify'],cwd=ROOT,check=True)
 subprocess.run(['make','comparison-verify'],cwd=ROOT,check=True)
 subprocess.run(['git','diff','--check'],cwd=ROOT,check=True)
 print('PASS image records and existing catalogue comparisons')
def review():
 verify();p=json.loads(PLAN.read_text());paths=[p['path'],'research-state.json','Makefile','make/images.mk','scripts/model_images.py']
 paths += [str(local_asset(v['image_url']).relative_to(ROOT)) for v in p['record']['views'].values() if not v['image_url'].startswith('https://')]
 assert not publish.git('diff','--cached','--name-only')
 changed=set(publish.git('diff','--name-only').splitlines())|set(publish.git('ls-files','--others','--exclude-standard').splitlines())
 assert changed<=set(paths),changed-set(paths)
 subprocess.run(['git','add','--']+sorted(changed),cwd=ROOT,check=True)
 r={'head':publish.git('rev-parse','HEAD'),'model':p['record']['model_key'],'paths':sorted(changed),'sha256':hashlib.sha256(publish.git('diff','--cached').encode()).hexdigest()}
 RECEIPT.write_text(json.dumps(r));print(publish.git('diff','--cached','--stat'));print('REVIEW',r)
def commit():
 publish.identity();r=json.loads(RECEIPT.read_text())
 assert r['head']==publish.git('rev-parse','HEAD')
 assert r['paths']==sorted(publish.git('diff','--cached','--name-only').splitlines())
 assert r['sha256']==hashlib.sha256(publish.git('diff','--cached').encode()).hexdigest()
 assert not publish.git('diff','--name-only')
 subprocess.run(['git','commit','-m','docs(images): update '+r['model'].replace('::',' ')+' pictures'],cwd=ROOT,check=True)
 subprocess.run(['git','push','origin','main:main'],cwd=ROOT,check=True)
 assert publish.git('ls-remote','origin','refs/heads/main').split()[0]==publish.git('rev-parse','HEAD')
 print('PUSH_VERIFIED',publish.git('rev-parse','--short','HEAD'))
if __name__=='__main__':
 {'diagram':diagram,'test':test,'plan':plan,'fetch':fetch,'apply':apply,'verify':verify,'review':review,'commit':commit}[sys.argv[1]]()
