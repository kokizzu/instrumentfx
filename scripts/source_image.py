"""Preview and retrieve one bounded manufacturer visual source for research."""
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
LIMIT = 48 * 1024 * 1024
HOSTS = {'res.diversitone.com', 'images.ctfassets.net', 'mod.audio', 'zoomcorp.com', 'static.roland.com', 'cdn.roland.com',
         'cdn.rockboard.de', 'line6.com', 'nuxaudio.cherubtechnology.com', 'cdn-media.empowertribe.com', 'cdn.inmusicbrands.com'}


def check_url(url):
    parsed = urllib.parse.urlsplit(url)
    if (parsed.scheme != 'https' or parsed.hostname not in HOSTS
            or parsed.username or parsed.password or parsed.port not in (None, 443)):
        raise ValueError('Expected an HTTPS reviewed visual-source URL')
    return url


class ManufacturerRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        check_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def svg_root(data):
    """Accept only static self-contained SVG; never retrieve linked resources."""
    import re
    import xml.etree.ElementTree as ET
    if not data.lstrip().startswith((b'<svg', b'<?xml')):
        return None
    lowered = data.lower()
    assert b'<!doctype' not in lowered and b'<!entity' not in lowered, 'SVG entities forbidden'
    root = ET.fromstring(data)
    assert root.tag.split('}')[-1] == 'svg', 'Expected SVG root'
    for item in root.iter():
        assert item.tag.split('}')[-1].lower() not in ('script', 'foreignobject', 'image'), 'Non-static SVG element'
        for key, value in item.attrib.items():
            local = key.split('}')[-1].lower()
            assert not local.startswith('on'), 'SVG event handler'
            if local in ('href', 'src'):
                assert value.startswith('#'), 'External SVG reference'
    text = data.decode('utf-8')
    assert '@import' not in text.lower(), 'External SVG stylesheet'
    for reference in re.findall(r'url\s*\(([^)]*)\)', text, re.I):
        assert reference.strip(' \"\'').startswith('#'), 'External SVG resource'
    return root


def render_svg(data, output):
    import cairosvg
    root = svg_root(data)
    assert root is not None
    viewbox = [float(value) for value in root.attrib['viewBox'].replace(',', ' ').split()]
    assert len(viewbox) == 4
    width, height = viewbox[2:]
    assert width > 0 and height > 0 and 0.1 <= width / height <= 10
    factor = 1600 / max(width, height)
    cairosvg.svg2png(bytestring=data, write_to=str(output),
                    output_width=max(1, round(width * factor)),
                    output_height=max(1, round(height * factor)), unsafe=False)


def validate_image(data):
    if len(data) > LIMIT:
        raise ValueError('Visual source exceeds 48 MiB limit')
    if not (data.startswith(b'\xff\xd8\xff') or data.startswith(b'\x89PNG\r\n\x1a\n')
            or data.startswith((b'GIF87a', b'GIF89a', b'%PDF-')) or svg_root(data) is not None):
        raise ValueError('Response is not a JPEG, PNG, GIF, PDF or static SVG visual source')
    return hashlib.sha256(data).hexdigest()


def atomic_write(path, data):
    pending = path.with_name(path.name + '.pending')
    with pending.open('wb') as output:
        output.write(data)
    pending.replace(path)


def source_path(url):
    return IMAGE.with_suffix('.pdf') if urllib.parse.urlsplit(url).path.lower().endswith('.pdf') else IMAGE


def previous_source():
    if RECEIPT.exists():
        previous = Path(json.loads(RECEIPT.read_text())['output'])
        assert previous in (IMAGE, IMAGE.with_suffix('.pdf')), 'Unexpected cache path'
        return previous if previous.exists() else None
    return IMAGE if IMAGE.exists() else None


def plan():
    identity()
    state = json.loads((ROOT / 'research-state.json').read_text())
    url = check_url(state['source_image_inspection']['requested_url'])
    output = source_path(url)
    previous = previous_source()
    assert output == previous or not output.exists(), 'Unexpected destination collision'
    value = {'url': url, 'output': str(output), 'limit_bytes': LIMIT,
             'previous_output': str(previous) if previous else None,
             'retire_previous_working_file': str(previous) if previous and previous != output else None,
             'previous_sha256': hashlib.sha256(previous.read_bytes()).hexdigest() if previous else None}
    if urllib.parse.urlsplit(url).path.lower().endswith('.pdf'):
        opener = urllib.request.build_opener(ManufacturerRedirect())
        request = urllib.request.Request(url, method='HEAD',
            headers={'User-Agent': 'InstrumentFX-source-review/1.0'})
        with opener.open(request, timeout=20) as response:
            length = response.headers.get('Content-Length', '')
            value['reported_source_bytes'] = int(length) if length.isdigit() else None
    atomic_write(PLAN, (json.dumps(value, indent=2) + '\n').encode())
    print(json.dumps(value, indent=2))


def apply():
    identity()
    value = json.loads(PLAN.read_text())
    url = check_url(value['url'])
    output = source_path(url)
    assert value['output'] == str(output) and value['limit_bytes'] == LIMIT
    state = json.loads((ROOT / 'research-state.json').read_text())
    assert state['source_image_inspection']['requested_url'] == url, 'Request changed; rerun plan'
    previous = previous_source()
    assert (str(previous) if previous else None) == value['previous_output'], 'Cache path changed'
    digest_before = hashlib.sha256(previous.read_bytes()).hexdigest() if previous else None
    assert digest_before == value['previous_sha256'], 'Working source changed; rerun plan'
    assert output == previous or not output.exists(), 'Unexpected destination collision'
    retire = str(previous) if previous and previous != output else None
    assert retire == value['retire_previous_working_file']
    opener = urllib.request.build_opener(ManufacturerRedirect())
    request = urllib.request.Request(url, headers={'User-Agent': 'InstrumentFX-source-review/1.0'})
    with opener.open(request, timeout=40) as response:
        final_url = check_url(response.geturl())
        data = response.read(LIMIT + 1)
    digest = validate_image(data)
    atomic_write(output, data)
    if retire:
        assert hashlib.sha256(previous.read_bytes()).hexdigest() == digest_before
        assert hashlib.sha256(output.read_bytes()).hexdigest() == digest
        previous.unlink()  # Only the exact generated cache path/hash reviewed by plan.
    receipt = {'url': url, 'final_url': final_url, 'output': str(output),
               'bytes': len(data), 'sha256': digest,
               'visual_inspection': 'Not established by retrieval; inspect image separately'}
    atomic_write(RECEIPT, (json.dumps(receipt, indent=2) + '\n').encode())
    print(json.dumps(receipt, indent=2))


def render_pdf(source, output, page):
    import subprocess
    assert isinstance(page, int) and 0 <= page < 128
    assert output.suffix == '.png'
    subprocess.run(['pdftoppm', '-f', str(page + 1), '-l', str(page + 1),
                    '-singlefile', '-scale-to', '1600', '-png', str(source),
                    str(output.with_suffix(''))], check=True, timeout=30)


def render():
    """Decode a reviewed source into one bounded frame; never execute its content."""
    from PIL import Image
    identity()
    state = json.loads((ROOT / 'research-state.json').read_text())['source_image_inspection']
    receipt = json.loads(RECEIPT.read_text())
    working = Path(receipt['output'])
    assert working == source_path(state['requested_url']), 'Rerun reviewed retrieval for source format'
    data = working.read_bytes()
    assert receipt['url'] == state['requested_url'], 'Source changed; retrieve reviewed source'
    assert validate_image(data) == receipt['sha256'], 'Source bytes changed'
    frame = state.get('frame', 0)
    assert isinstance(frame, int) and 0 <= frame < 128
    Image.MAX_IMAGE_PIXELS = 8 * 1024 * 1024
    if data.startswith(b'%PDF-'):
        output = Path('/tmp/instrumentfx-source-image-view.png')
        render_pdf(working, output, frame)
        with Image.open(output) as rendered:
            assert rendered.width * rendered.height <= Image.MAX_IMAGE_PIXELS
            print(json.dumps({'url': receipt['url'], 'sha256': receipt['sha256'],
                              'pdf_page_zero_based': frame, 'size': rendered.size,
                              'rendered': str(output)}))
        return
    if svg_root(data) is not None:
        output = Path('/tmp/instrumentfx-source-image-view.png')
        render_svg(data, output)
        with Image.open(output) as rendered:
            assert rendered.width * rendered.height <= Image.MAX_IMAGE_PIXELS
            print(json.dumps({'url': receipt['url'], 'sha256': receipt['sha256'],
                              'static_svg': True, 'size': rendered.size, 'rendered': str(output)}))
        return
    with Image.open(working) as source:
        assert source.width * source.height <= Image.MAX_IMAGE_PIXELS
        frames = getattr(source, 'n_frames', 1)
        assert frames <= 128 and frame < frames
        source.seek(frame)
        output = Path('/tmp/instrumentfx-source-image-view.png')
        source.convert('RGB').save(output, format='PNG')
        print(json.dumps({'url': receipt['url'], 'sha256': receipt['sha256'],
                          'frame': frame, 'total_frames': frames,
                          'size': source.size, 'rendered': str(output)}))


def extract_text():
    """Read a selected PDF range to stdout, without retaining a text duplicate."""
    import subprocess
    identity()
    state = json.loads((ROOT / 'research-state.json').read_text())['source_image_inspection']
    receipt = json.loads(RECEIPT.read_text())
    source = Path(receipt['output'])
    assert source == source_path(state['requested_url']) and source.suffix == '.pdf'
    assert receipt['url'] == state['requested_url']
    data = source.read_bytes()
    assert data.startswith(b'%PDF-') and validate_image(data) == receipt['sha256']
    pages = state.get('text_pages', [state.get('frame', 0)] * 2)
    assert len(pages) == 2 and all(isinstance(value, int) for value in pages)
    first, last = pages
    assert 0 <= first <= last < 128 and last - first < 16
    info = subprocess.run(['pdfinfo', str(source)], check=True, capture_output=True, text=True, timeout=20)
    result = subprocess.run(['pdftotext', '-f', str(first + 1), '-l', str(last + 1),
                             '-layout', str(source), '-'], check=True, capture_output=True, text=True, timeout=30)
    assert len(result.stdout) <= 65536, 'Select a smaller PDF text range'
    print(info.stdout)
    print('PDF zero-based pages:', first, last)
    print(result.stdout)


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
    assert source_path('https://zoomcorp.com/a.jpg') == IMAGE
    assert source_path('https://cdn.rockboard.de/a.pdf?revision=1').suffix == '.pdf'
    for bad in (b'<html>error</html>', b'\xff\xd8\xff' + bytes(LIMIT)):
        try:
            validate_image(bad)
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid image accepted')
    assert validate_image(b'\xff\xd8\xffexample')
    from PIL import Image
    from io import BytesIO
    fixture = BytesIO()
    Image.new('RGB', (2, 2), 'red').save(fixture, format='GIF', save_all=True,
        append_images=[Image.new('RGB', (2, 2), 'blue')], duration=100)
    assert validate_image(fixture.getvalue())
    fixture.seek(0)
    with Image.open(fixture) as decoded:
        assert decoded.n_frames == 2
        decoded.seek(1)
        assert decoded.convert('RGB').getpixel((0, 0)) == (0, 0, 255)
    import shutil
    import tempfile
    assert shutil.which('pdftoppm'), 'Poppler pdftoppm is required for PDF visual review'
    with tempfile.TemporaryDirectory(prefix='instrumentfx-pdf-test-') as directory:
        source = Path(directory) / 'fixture.pdf'
        output = Path(directory) / 'fixture.png'
        Image.new('RGB', (32, 24), 'red').save(source, format='PDF')
        assert validate_image(source.read_bytes())
        render_pdf(source, output, 0)
        with Image.open(output) as decoded:
            assert decoded.width > decoded.height
            red, green, blue = decoded.convert('RGB').getpixel((0, 0))
            assert red > 200 and green < 30 and blue < 30
    with tempfile.TemporaryDirectory(prefix='instrumentfx-svg-test-') as directory:
        output = Path(directory) / 'fixture.png'
        fixture = b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect width="32" height="24" fill="red"/></svg>'
        assert validate_image(fixture)
        render_svg(fixture, output)
        with Image.open(output) as decoded:
            assert decoded.size == (1600, 1200)
            assert decoded.convert('RGB').getpixel((0, 0)) == (255, 0, 0)
        for bad in (fixture.replace(b'<rect', b'<script/><rect'),
                    fixture.replace(b'<rect', b'<image href="https://example.com/a.png"/><rect'),
                    fixture.replace(b'fill="red"', b'fill="url(https://example.com/a)"'),
                    fixture.replace(b'<rect', b'<style>@import "https://example.com/a";</style><rect')):
            try:
                validate_image(bad)
            except AssertionError:
                pass
            else:
                raise AssertionError('Active/external SVG accepted')
    print('PASS: bounded image/PDF/static-SVG rendering; active and external SVG resources rejected')


if __name__ == '__main__':
    {'plan': plan, 'apply': apply, 'test': test, 'render': render, 'text': extract_text}[sys.argv[1]]()
