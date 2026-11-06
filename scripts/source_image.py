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
HOSTS = {'www.valeton.net', 'res.diversitone.com', 'images.ctfassets.net', 'mod.audio', 'zoomcorp.com', 'static.roland.com', 'cdn.roland.com',
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


RELEASE_NOTE_URLS = frozenset({
    'https://yms-file-store.oss-cn-hongkong.aliyuncs.com/software/releaseNote/firmware/MK20.txt',
    'https://yms-file-store.oss-cn-hongkong.aliyuncs.com/software/releaseNote/firmware/MK300.txt',
})


def decode_release_note(data):
    """Decode inert manufacturer text without replacement of invalid bytes."""
    if data.startswith((b'\xff\xfe', b'\xfe\xff')):
        return data.decode('utf-16'), 'utf-16-bom'
    try:
        return data.decode('utf-8-sig'), 'utf-8-sig'
    except UnicodeDecodeError:
        return data.decode('gb18030'), 'gb18030'


def check_index_url(url):
    parsed = urllib.parse.urlsplit(url)
    assert parsed.scheme == 'https' and (parsed.hostname in ('www.valeton.net', 'www.mooeraudio.com') or url in RELEASE_NOTE_URLS)
    assert not parsed.username and not parsed.password and parsed.port in (None, 443)
    if parsed.path == '/wp-admin/admin-ajax.php':
        assert parsed.hostname == 'www.valeton.net'
        query = urllib.parse.parse_qs(parsed.query)
        assert query.get('action') == ['wpfd']
        assert query.get('task') in (['categories.display'], ['files.display'])
        assert (query.get('task'), query.get('view')) in ((['categories.display'], ['categories']), (['files.display'], ['files']))
        assert set(query) <= {'juwpfisadmin', 'action', 'task', 'view', 'id', 'top', 'page', 'limit', 'rootcat', 'page_limit', 'orderCol', 'orderDir'}
    return url


class IndexRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        check_index_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def inspect_index():
    """Inspect bounded public HTML/JSON/JS as text; never execute page scripts."""
    identity()
    state = json.loads((ROOT / 'research-state.json').read_text())['source_image_inspection']
    url = state['index_url']
    check_index_url(url)
    needle = state.get('index_needle', 'GP-150')
    assert isinstance(needle, str) and 2 <= len(needle) <= 64
    request = urllib.request.Request(url, headers={'User-Agent': 'InstrumentFX-source-review/1.0'})
    opener = urllib.request.build_opener(IndexRedirect())
    with opener.open(request, timeout=30) as response:
        check_index_url(response.geturl())
        limit = 65536 if url in RELEASE_NOTE_URLS else 4 * 1024 * 1024
        data = response.read(limit + 1)
    assert len(data) <= limit, 'Static manufacturer source exceeds selected size limit'
    if url in RELEASE_NOTE_URLS:
        body, encoding = decode_release_note(data)
        print(json.dumps({'url': url, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'encoding': encoding}))
        print(body)
        return
    body = data.decode('utf-8')
    if body.lstrip().startswith('{'):
        decoded = json.loads(body)
        if 'files' in decoded:
            assert len(decoded['files']) <= 100, 'Select a smaller catalogue page'
            print(json.dumps({'url': url, 'sha256': hashlib.sha256(data).hexdigest(),
                              'keys': list(decoded), 'files': decoded['files']}))
            return
        if 'categories' in decoded:
            print(json.dumps({'url': url, 'sha256': hashlib.sha256(data).hexdigest(),
                              'keys': list(decoded), 'files': decoded.get('files'), 'categories': [{'id': row.get('term_id'), 'name': row.get('name')}
                                             for row in decoded['categories']]}))
            return
    import re
    positions = [match.start() for match in re.finditer(re.escape(needle), body, re.I)]
    skip = state.get('index_skip', 0)
    assert isinstance(skip, int) and 0 <= skip <= 1000
    print(json.dumps({'url': url, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                      'needle': needle, 'matches': len(positions), 'skip': skip}))
    previous_end = 0
    for position in positions[skip:skip + 25]:
        start, end = max(previous_end, position - 250), position + 1000
        if end > start:
            print(body[start:end])
            previous_end = end


def test():
    for note_url in RELEASE_NOTE_URLS:
        check_index_url(note_url)
    fixture_text = 'V086 更新说明'
    for codec in ('utf-8-sig', 'utf-16', 'gb18030'):
        assert decode_release_note(fixture_text.encode(codec))[0] == fixture_text
    check_index_url('https://www.valeton.net/user-manual/')
    check_index_url('https://www.mooeraudio.com/companyfile/GE300-Downloads-145.html')
    check_index_url('https://www.valeton.net/wp-admin/admin-ajax.php?action=wpfd&task=files.display&view=files&id=320')
    for bad in ('https://yms-file-store.oss-cn-hongkong.aliyuncs.com/software/releaseNote/firmware/MK20.zip',
                'https://yms-file-store.oss-cn-hongkong.aliyuncs.com/software/releaseNote/firmware/MK300.zip',
                'https://yms-file-store.oss-cn-hongkong.aliyuncs.com/software/releaseNote/firmware/MK300.txt?download=1',
                'https://yms-file-store.oss-cn-hongkong.aliyuncs.com/software/other.txt',
                'https://example.com/user-manual/',
                'http://www.valeton.net/user-manual/',
                'https://user:secret@www.valeton.net/user-manual/',
                'https://www.valeton.net/wp-admin/admin-ajax.php?action=wpfd&task=files.upload&view=files',
                'https://www.valeton.net/wp-admin/admin-ajax.php?action=wpfd&task=categories.display&view=files'):
        try:
            check_index_url(bad)
        except AssertionError:
            pass
        else:
            raise AssertionError('Unsafe catalogue request accepted')
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
    {'plan': plan, 'apply': apply, 'test': test, 'render': render, 'text': extract_text, 'index': inspect_index}[sys.argv[1]]()
