"""Preview and retrieve one bounded manufacturer photograph for visual research."""
import hashlib
import json
from pathlib import Path
import sys
sys.dont_write_bytecode = True
import urllib.parse
import urllib.request
from research_tools import ROOT, identity

PLAN = Path('/tmp/instrumentfx-source-image-plan.json')
RECEIPT = Path('/tmp/instrumentfx-source-image-receipt.json')
IMAGE = Path('/tmp/instrumentfx-source-image.jpg')
LIMIT = 8 * 1024 * 1024
HOSTS = {'zoomcorp.com', 'static.roland.com', 'cdn.roland.com',
         'line6.com', 'nuxaudio.cherubtechnology.com', 'cdn-media.empowertribe.com', 'cdn.inmusicbrands.com'}


def check_url(url):
    parsed = urllib.parse.urlsplit(url)
    if (parsed.scheme != 'https' or parsed.hostname not in HOSTS
            or parsed.username or parsed.password or parsed.port not in (None, 443)):
        raise ValueError('Expected an HTTPS manufacturer image URL')
    return url


class ManufacturerRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        check_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def validate_image(data):
    if len(data) > LIMIT:
        raise ValueError('Image exceeds 8 MiB limit')
    if not (data.startswith(b'\xff\xd8\xff') or data.startswith(b'\x89PNG\r\n\x1a\n')):
        raise ValueError('Response is not a JPEG or PNG photograph')
    return hashlib.sha256(data).hexdigest()


def atomic_write(path, data):
    pending = path.with_name(path.name + '.pending')
    with pending.open('wb') as output:
        output.write(data)
    pending.replace(path)


def plan():
    identity()
    state = json.loads((ROOT / 'research-state.json').read_text())
    url = check_url(state['source_image_inspection']['requested_url'])
    value = {'url': url, 'output': str(IMAGE), 'limit_bytes': LIMIT,
             'replaces_existing_working_image': IMAGE.exists(),
             'previous_sha256': hashlib.sha256(IMAGE.read_bytes()).hexdigest() if IMAGE.exists() else None}
    atomic_write(PLAN, (json.dumps(value, indent=2) + '\n').encode())
    print(json.dumps(value, indent=2))


def apply():
    identity()
    value = json.loads(PLAN.read_text())
    assert value['output'] == str(IMAGE) and value['limit_bytes'] == LIMIT
    url = check_url(value['url'])
    state = json.loads((ROOT / 'research-state.json').read_text())
    assert state['source_image_inspection']['requested_url'] == url, 'Request changed; rerun plan'
    previous = hashlib.sha256(IMAGE.read_bytes()).hexdigest() if IMAGE.exists() else None
    assert previous == value['previous_sha256'], 'Working image changed; rerun plan'
    opener = urllib.request.build_opener(ManufacturerRedirect())
    request = urllib.request.Request(url, headers={'User-Agent': 'InstrumentFX-source-review/1.0'})
    with opener.open(request, timeout=40) as response:
        final_url = check_url(response.geturl())
        data = response.read(LIMIT + 1)
    digest = validate_image(data)
    atomic_write(IMAGE, data)
    receipt = {'url': url, 'final_url': final_url, 'output': str(IMAGE),
               'bytes': len(data), 'sha256': digest,
               'visual_inspection': 'Not established by retrieval; inspect image separately'}
    atomic_write(RECEIPT, (json.dumps(receipt, indent=2) + '\n').encode())
    print(json.dumps(receipt, indent=2))


def test():
    for bad in ('http://zoomcorp.com/a.jpg', 'https://localhost/a.jpg',
                'https://zoomcorp.com.evil.example/a.jpg',
                'https://user:secret@zoomcorp.com/a.jpg'):
        try:
            check_url(bad)
        except ValueError:
            pass
        else:
            raise AssertionError('Unsafe source accepted')
    check_url('https://zoomcorp.com/media/example.jpg')
    for bad in (b'<html>error</html>', b'\xff\xd8\xff' + bytes(LIMIT)):
        try:
            validate_image(bad)
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid image accepted')
    assert validate_image(b'\xff\xd8\xffexample')
    print('PASS: HTTPS host restrictions, credentials, image signatures and size limit')


if __name__ == '__main__':
    {'plan': plan, 'apply': apply, 'test': test}[sys.argv[1]]()
