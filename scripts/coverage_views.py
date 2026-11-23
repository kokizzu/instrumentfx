"""Derived coverage views and reviewable publication; no new research claims."""
import hashlib, html, json, re, subprocess, sys
from pathlib import Path
import firmware_publish as publish
import firmware_pitch as audit
import comparison_views as cv
ROOT = audit.ROOT
RECEIPT = Path('/tmp/instrumentfx-coverage-review.json')
NAV = '[Photo galleries](PHOTOS.md) · [Verification gaps](RESEARCH-GAPS.md)'

def footswitch_thumbnails(state, source):
    """Add checked top-view thumbnails below active processor names in the display tables."""
    by_link = {record['link']: key for key, record in state['comparison_model_sources'].items()}
    image_records = state.get('model_images', {}).get('models', {})
    marker = re.compile(r'<span class="model-thumbnail" data-model-key="[^"]+">.*?</span>')
    rows = []
    for line in source.splitlines():
        if line.startswith('|') and not line.startswith('|---'):
            line = marker.sub('', line)
            cells = line.split('|')
            if len(cells) >= 4:
                hrefs = re.findall(r'\]\(([^)]+)\)', line)
                keys = list(dict.fromkeys(by_link[href] for href in hrefs if href in by_link))
                thumbnails = []
                for key in keys:
                    if not image_records.get(key, {}).get('views', {}).get('top', {}).get('image_url', '').startswith('https://'):
                        continue
                    picture = cv.model_picture(state, key)
                    thumbnails.append('<span class="model-thumbnail" data-model-key="' + html.escape(key, quote=True) + '">' + picture + '</span>')
                if thumbnails:
                    cells[1] += ''.join(thumbnails)
                    line = '|'.join(cells)
        rows.append(line)
    return '\n'.join(rows) + '\n'

def footswitch_thumbnail_count(state, source):
    by_link = {record['link']: key for key, record in state['comparison_model_sources'].items()}
    image_records = state.get('model_images', {}).get('models', {})
    count = 0
    for line in source.splitlines():
        if not line.startswith('|') or line.startswith('|---'):
            continue
        hrefs = re.findall(r'\]\(([^)]+)\)', line)
        keys = set(by_link[href] for href in hrefs if href in by_link)
        count += sum(image_records.get(key, {}).get('views', {}).get('top', {}).get('image_url', '').startswith('https://') for key in keys)
    return count

def esc(value):
    return str(value or 'Unverified').replace('|', '&#124;').replace('\n', ' ')

def outputs(state):
    models = state['firmware_lifecycle']['models']
    images = state['model_images']['models']
    keys = sorted(audit.inventory(state), key=lambda k: (cv.natural_key(k), k))
    pages = {}
    gaps = ['# Verification gaps', '', '[Repository](README.md) · [Photos](PHOTOS.md) · [Firmware](FIRMWARE-UPDATES.md) · [Pitch](PITCH-SHIFTING.md)', '',
        'Generated from the authoritative research-state.json. These are evidence gaps, not negative capability claims. Checked dates belong to each model; generating this page does not refresh firmware or certify image-link availability.', '',
        '## What can close a gap', '',
        '- Release: dated manufacturer launch/shipment evidence. An available-by demo, customer review or regional retailer reference remains a proxy.',
        '- Firmware: exact-model official release notes and download index, separating device firmware from editors, USB components and drivers.',
        '- Polyphony: explicit documentation for the named algorithm, or repeatable chord-input testing on the stated firmware. Harmony voice count and stereo are insufficient.',
        '- DSP: retain processor/path denominator, firmware, algorithm settings, chain and baseline. Block ceilings are not percentages. Unstructured source notes below are not automatically classified as measurements.',
        '- Photos: actual powered control-face photo with the full enclosure perpendicular to the camera, plus a complete connector-edge view. Stock composites, unlit photos and diagrams stay qualified.', '',
        '## Hardware test procedure', '',
        '1. Record exact model/revision, firmware and editor versions; back up the owner preset before editing.',
        '2. In a spare empty preset, record the DSP meter baseline and its processor/path denominator. Keep input/output routing, sample rate and global processing fixed.',
        '3. Add only the named pitch algorithm; record interval, quality/range settings, wet/dry mix and meter. Report both total load and delta; repeat after preset recall.',
        '4. Test isolated notes, dyads, full major/minor chords and sustained overlapping notes at several intervals. Capture dry and wet audio. Distinguish chord tracking from generated harmony voices; note artifacts without inventing a numeric quality score.',
        '5. Add amp/capture, reverb and other blocks one at a time. Record rejected additions and chain-specific limits; do not extrapolate a universal effect ceiling from one preset.',
        '6. Save screenshots plus a powered overhead and connector photo with permission. Record evidence in the existing model entry and commit that model separately.', '',
        '## Per-model evidence and next action', '',
        'Every model links to its complete checked-source trail. DSP text is reproduced as evidence notes, not normalized to a comparable percentage. Photo flags concern the primary image only; supplements may provide additional coverage.', '',
        '| Model / checked sources | Release evidence needed | Firmware verification | Pitch classification | DSP evidence notes | Primary photo gaps |',
        '|---|---|---|---|---|---|']
    photo_index = ['# Product photos', '', '[Repository](README.md) · [Comparison tables](all-guitar.md) · [Verification gaps](RESEARCH-GAPS.md)', '',
        'Thumbnails are also displayed below effect names in the instrument comparison tables. These smaller brand galleries avoid loading the entire catalogue at once. Canonical brand files retain detailed image captions and source qualifications inside expandable Product pictures sections.', '',
        'All pictures are source links, not locally archived copies; a host can block or remove them. Counts mean recorded evidence, not a live HTTP availability check. Stock illumination is not independently verified powered hardware.', '',
        '| Brand | Models | Powered primary top | Strict powered top-down | Rear records |', '|---|---|---|---|---|']
    for brand in sorted(state['inventory_by_brand'], key=cv.natural_key):
        bkeys = [k for k in keys if k.split('::')[0] == brand]
        canonical = state['comparison_model_sources'][bkeys[0]]['link'].split('#')[0]
        filename = 'photos/' + Path(canonical).stem.lower() + '.md'
        page = ['# ' + brand + ' product photos', '', '[All photo galleries](../PHOTOS.md) · [Verification gaps](../RESEARCH-GAPS.md)', '',
            'Click a thumbnail for the full image. Read the linked canonical record for inspection notes; powered status and camera angle are separate requirements.', '',
            '| Model / evidence | Control face | Rear / connector edge |', '|---|---|---|']
        for key in bkeys:
            r = models[key]; im = images.get(key, {}); views = im.get('views', {})
            release = r['first_release']
            need = 'Dated first-release evidence' if not release.get('date') else ('Original launch/shipment; current basis: ' + release['kind'] if 'proxy' in release.get('kind', '') else 'Current dated basis: ' + release.get('kind', ''))
            top = views.get('top', {})
            photo_gaps = []
            if top.get('powered_on') is not True: photo_gaps.append('powered top unverified')
            if top.get('exact_top_down') is not True: photo_gaps.append('perpendicular top pending')
            if not views.get('rear'): photo_gaps.append('rear missing')
            elif not views['rear']['image_url'].startswith('https://'): photo_gaps.append('rear is local diagram; photo needed')
            link = state['comparison_model_sources'][key]['link']
            dsp = esc(r['pitch'].get('dsp'))
            gaps.append('| [' + esc(key.replace('::',' ')) + '](' + link + ') | ' + esc(need) + ' | ' + esc(r['firmware']['status']) + '; checked ' + r['checked_date'] + ' | ' + esc(r['pitch']['status']) + ' | ' + dsp + ' | ' + esc('; '.join(photo_gaps) or 'Primary flags satisfied; inspect sources') + ' |')
            cells = []
            for view in ('top','rear'):
                v = views.get(view)
                if not v:
                    cells.append('Not yet verified'); continue
                url = v['image_url']
                if not url.startswith('https://'): url = '../brand/' + url
                url = html.escape(url, quote=True)
                caption = html.escape(v['caption'], quote=True)
                label = 'Powered' if v.get('powered_on') is True else ('Unlit' if v.get('powered_on') is False else 'Power unverified / stock')
                if view == 'top': label += '; perpendicular' if v.get('exact_top_down') is True else '; angle not verified perpendicular'
                cells.append('<a href="' + url + '"><img src="' + url + '" alt="' + caption + '" title="' + caption + '" width="220" loading="lazy"></a><br>' + label)
            page.append('| [' + esc(key.replace('::',' ')) + '](../' + link + ') | ' + ' | '.join(cells) + ' |')
        pages[filename] = '\n'.join(page) + '\n'
        records = [images.get(k, {}).get('views', {}) for k in bkeys]
        photo_index.append('| [' + esc(brand) + '](' + filename + ') | ' + str(len(bkeys)) + ' | ' + str(sum(v.get('top', {}).get('powered_on') is True for v in records)) + ' | ' + str(sum(v.get('top', {}).get('powered_on') is True and v.get('top', {}).get('exact_top_down') is True for v in records)) + ' | ' + str(sum('rear' in v for v in records)) + ' |')
    summary = 'Coverage: ' + str(len(keys)) + ' models; ' + str(sum(not models[k]["first_release"].get("date") for k in keys)) + ' without a dated release reference; ' + str(sum(models[k]["pitch"]["status"] == "pitch_present_polyphony_unverified" for k in keys)) + ' with pitch present but unverified polyphony. A proxy date is still not a verified original launch.'
    gaps[4:4] = [summary, '']
    pages['RESEARCH-GAPS.md'] = '\n'.join(gaps) + '\n'
    pages['PHOTOS.md'] = '\n'.join(photo_index) + '\n'
    readme = (ROOT/'README.md').read_text()
    if NAV not in readme:
        first, rest = readme.split('\n', 1)
        readme = first + '\n\n' + NAV + '\n' + rest
    pages.update(cv.make_plan(persist=False)['outputs'])
    pages['FOOTSWITCH-DISPLAYS.md'] = footswitch_thumbnails(state, (ROOT/'FOOTSWITCH-DISPLAYS.md').read_text())
    pages['README.md'] = readme
    return pages

def state(): return json.loads((ROOT/'research-state.json').read_text())
def generate():
    publish.identity()
    for path, body in outputs(state()).items():
        dest = ROOT/path; dest.parent.mkdir(parents=True, exist_ok=True); dest.write_text(body)
    print('Generated coverage recap, brand galleries and instrument thumbnails')
def verify():
    publish.identity()
    pages = outputs(state())
    for path, body in pages.items():
        assert (ROOT/path).read_text() == body, ('Stale generated view', path)
        if path.startswith('photos/'):
            assert len(body.encode()) < 180000, ('Gallery too large', path)
            assert '<details>' not in body
    assert len([p for p in pages if p.startswith('photos/')]) == len(state()['inventory_by_brand'])
    # Thumbnail markup must preserve membership parsing and quote-safe source URLs.
    fake = {'model_images': {'models': {'Test::One': {'views': {'top': {'image_url': 'https://example.com/a?x=1&y=2', 'caption': 'a "quote"'}}}}}}
    sample = cv.model_picture(fake, 'Test::One')
    assert '&amp;' in sample and '&quot;' in sample and 'width="160"' in sample
    assert 'pending' in cv.model_picture({}, 'Missing::One')
    current = state()
    footswitch = pages['FOOTSWITCH-DISPLAYS.md']
    footswitch_source = (ROOT/'FOOTSWITCH-DISPLAYS.md').read_text()
    assert footswitch.count('class="model-thumbnail"') == footswitch_thumbnail_count(current, footswitch_source), 'Footswitch display table thumbnails changed; inspect model-link mapping'
    for key, record in current['comparison_model_sources'].items():
        link = record['link']
        if key not in current.get('model_images', {}).get('models', {}):
            continue
        view = current['model_images']['models'][key].get('views', {}).get('top', {})
        if not view.get('image_url', '').startswith('https://'):
            continue
        # Only require thumbnails for rows that link to this exact canonical model record.
        matching_rows = [line for line in footswitch.splitlines() if line.startswith('|') and link in re.findall(r'\]\(([^)]+)\)', line)]
        assert all('data-model-key="' + html.escape(key, quote=True) + '"' in line.split('|')[1] for line in matching_rows), ('Footswitch thumbnail not under model name', key)
    for filename, ids in current['comparison_membership'].items():
        text = pages[filename]
        assert text.count('<img src=') == 4 * len(ids), ('Missing table thumbnails', filename)
        for key in ids:
            link = current['comparison_model_sources'][key]['link']
            label = '[' + key.replace('::', ' ') + '](' + link + ')'
            assert text.count(label + cv.model_picture(current, key)) >= 4, ('Missing model thumbnail', filename, key)
    audit.verify()
    for target in ('comparison-verify', 'research-verify'):
        subprocess.run(['make', target], cwd=ROOT, check=True)
    subprocess.run(['git','diff','--check'], cwd=ROOT, check=True)
    print('PASS coverage freshness, all brand galleries, safe thumbnails and canonical comparisons')
def review():
    verify()
    assert not publish.git('diff','--cached','--name-only'), 'Existing staged work'
    allowed = set(outputs(state())) | {'scripts/coverage_views.py', 'scripts/comparison_views.py', 'make/coverage.mk', 'Makefile'}
    changed = set(publish.git('diff','--name-only').splitlines()) | set(publish.git('ls-files','--others','--exclude-standard').splitlines())
    assert changed <= allowed, ('Unrelated work', changed-allowed)
    subprocess.run(['git','add','--',*sorted(changed)], cwd=ROOT, check=True)
    diff = publish.git('diff','--cached')
    RECEIPT.write_text(json.dumps({'head':publish.git('rev-parse','HEAD'), 'paths':sorted(changed), 'sha256':hashlib.sha256(diff.encode()).hexdigest()}))
    print(publish.git('diff','--cached','--stat'))
def refresh():
    publish.identity(); r=json.loads(RECEIPT.read_text())
    assert r['head']==publish.git('rev-parse','HEAD')
    assert r['sha256']==hashlib.sha256(publish.git('diff','--cached').encode()).hexdigest()
    assert r['paths']==sorted(publish.git('diff','--cached','--name-only').splitlines())
    subprocess.run(['git','restore','--staged','--',*r['paths']], cwd=ROOT, check=True)
    review()

def commit():
    publish.identity(); r=json.loads(RECEIPT.read_text())
    assert r['head']==publish.git('rev-parse','HEAD')
    assert r['paths']==sorted(publish.git('diff','--cached','--name-only').splitlines())
    assert r['sha256']==hashlib.sha256(publish.git('diff','--cached').encode()).hexdigest()
    assert not publish.git('diff','--name-only')
    subprocess.run(['git','commit','-m','docs: expose model thumbnails and verification gaps'], cwd=ROOT, check=True)
    subprocess.run(['git','push','origin','main:main'], cwd=ROOT, check=True)
    assert publish.git('ls-remote','origin','refs/heads/main').split()[0]==publish.git('rev-parse','HEAD')
    print('PUSH_VERIFIED', publish.git('rev-parse','--short','HEAD'))
if __name__=='__main__':
    {'generate':generate, 'verify':verify, 'review':review, 'refresh':refresh, 'commit':commit}[sys.argv[1]]()
