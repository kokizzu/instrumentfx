"""Validate and publish exactly one firmware/pitch model at a time."""
import hashlib,json,subprocess,sys
from pathlib import Path
import firmware_pitch as audit
ROOT=audit.ROOT
RECEIPT=Path('/tmp/instrumentfx-firmware-review.json')
def git(*args):return audit.lifecycle.git(*args)
def identity():
 audit.lifecycle.identity()
 refs=git('ls-remote','--symref','origin','HEAD')
 assert 'ref: refs/heads/main\tHEAD' in refs,'Verified upstream primary must be main'
def verify():
 identity();audit.verify()
 for target in ['brand-sort-test','research-verify','comparison-verify']:
  subprocess.run(['make',target],cwd=ROOT,check=True)
 for path in ['scripts/firmware_publish.py','scripts/research_push.py','scripts/source_image.py']:
  compile((ROOT/path).read_text(),path,'exec')
 subprocess.run(['git','diff','--check'],cwd=ROOT,check=True)
def selection():
 state=json.loads((ROOT/'research-state.json').read_text());key=state['firmware_lifecycle']['last_model']
 record=state['firmware_lifecycle']['models'][key]
 paths=[audit.model_link(state,record).split('#')[0],'research-state.json','FIRMWARE-UPDATES.md','PITCH-SHIFTING.md','all-guitar.md','all-bass.md','all-vocal.md','README.md']
 paths+=['.gitignore','Makefile','make/firmware.mk','scripts/firmware_publish.py','scripts/research_push.py','scripts/source_image.py']
 return key,paths
def review():
 verify();key,paths=selection()
 assert not git('diff','--cached','--name-only'),'Existing staged changes must be preserved'
 changed=set(git('diff','--name-only').splitlines())|set(git('ls-files','--others','--exclude-standard').splitlines())
 assert changed<=set(paths),('Unrelated changes require individual review',sorted(changed-set(paths)))
 subprocess.run(['git','add','--']+[p for p in paths if p in changed],cwd=ROOT,check=True)
 diff=git('diff','--cached');assert diff
 receipt={'head':git('rev-parse','HEAD'),'model':key,'sha256':hashlib.sha256(diff.encode()).hexdigest(),'paths':git('diff','--cached','--name-only').splitlines()}
 RECEIPT.write_text(json.dumps(receipt))
 print(git('diff','--cached','--stat'))
 # Full research changes are inspected in their canonical files before this gate.
 print('MODEL',key,'REVIEW_SHA256',receipt['sha256'])
def commit():
 identity();key,paths=selection();saved=json.loads(RECEIPT.read_text())
 assert saved['head']==git('rev-parse','HEAD') and key==saved['model']
 assert saved['paths']==git('diff','--cached','--name-only').splitlines()
 assert saved['sha256']==hashlib.sha256(git('diff','--cached').encode()).hexdigest(),'Staged diff changed'
 assert not git('diff','--name-only'),'Unstaged changes appeared'
 subprocess.run(['git','diff','--cached','--check'],cwd=ROOT,check=True)
 subprocess.run(['git','commit','-m','docs(firmware-pitch): audit '+key.replace('::',' ')],cwd=ROOT,check=True)
 subprocess.run(['git','push','origin','main:main'],cwd=ROOT,check=True)
 assert git('ls-remote','origin','refs/heads/main').split()[0]==git('rev-parse','HEAD')
 print('PUSH_VERIFIED',git('rev-parse','--short','HEAD'))
def refresh_review():
 """Restage only this workflow's unchanged, previously reviewed selection."""
 identity();key,paths=selection();saved=json.loads(RECEIPT.read_text())
 assert saved['head']==git('rev-parse','HEAD') and key==saved['model']
 assert saved['paths']==git('diff','--cached','--name-only').splitlines()
 assert set(saved['paths'])<=set(paths)
 assert saved['sha256']==hashlib.sha256(git('diff','--cached').encode()).hexdigest(),'Staged diff changed'
 subprocess.run(['git','restore','--staged','--']+saved['paths'],cwd=ROOT,check=True)
 review()
if __name__=='__main__':{'verify':verify,'review':review,'refresh-review':refresh_review,'commit':commit}[sys.argv[1]]()
