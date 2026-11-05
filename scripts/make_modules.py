"""Split the command index losslessly; verify all historical command expansions.

One bounded /tmp plan stores hashes and the review receipt. Historical source is
read from Git, rather than copied into another inventory. No recipe is executed
by the exhaustive dry-run check. Existing targets remain compatibility APIs.
"""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = '6f33d2ce2976d7c8b34bec43dc78e3d344c49519'
PLAN = Path('/tmp/instrumentfx-make-modules-plan.json')
SCRIPT = 'scripts/make_modules.py'
GROUPS = ('research', 'consolidation', 'comparisons', 'navigation',
          'expression', 'retirement', 'publication')
MODES = ('plan', 'apply', 'test', 'verify', 'stage', 'commit')


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True)


def guard():
    assert git('branch', '--show-current').strip() == 'main'
    assert git('remote', 'get-url', 'origin').strip() == 'git@github.com:kokizzu/instrumentfx.git'
    assert git('symbolic-ref', 'refs/remotes/origin/HEAD').strip() == 'refs/remotes/origin/main'


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def parse(text):
    rules, phony, current = {}, set(), None
    for line in text.splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        if line.startswith('.PHONY:'):
            phony.update(line.split(':', 1)[1].split())
            current = None
        elif line.startswith('\t'):
            assert current is not None, 'Recipe without target'
            rules[current].append(line)
        else:
            match = re.fullmatch(r'([A-Za-z0-9_-]+):', line)
            assert match, 'Unsupported Make syntax: ' + line
            current = match[1]
            assert current not in rules, 'Duplicate target: ' + current
            rules[current] = []
    return rules, phony


def baseline():
    return git('show', BASE + ':Makefile')


def maintenance():
    return '\n'.join('.PHONY: make-modules-' + mode + '\nmake-modules-' + mode +
                     ':\n\tpython3 ' + SCRIPT + ' ' + mode + '\n' for mode in MODES)


def group(recipe):
    assert len(recipe) == 1, 'Review multi-line recipe before splitting'
    match = re.search(r'scripts/([a-z0-9_]+)\.py', recipe[0])
    assert match, 'Non-script recipe requires review'
    name = match[1]
    if name == 'consolidation_tools':
        return 'consolidation'
    if name.startswith(('comparison_', 'creative_')) or name in ('research_gaps', 'discovery_resolution'):
        return 'comparisons'
    if name in ('brand_sort', 'brand_filename_migration', 'navigation_tools', 'canonical_links'):
        return 'navigation'
    if name.startswith(('expression_audit_', 'display_audit_')):
        return 'expression'
    if name in ('metadata_consolidation', 'source_retirement', 'technical_retirement',
                'compatibility_removal', 'archive_retirement', 'json_pointer_removal',
                'preservation_review', 'ledger_history'):
        return 'retirement'
    if name == 'research_push':
        return 'publication'
    assert name in ('research_tools', 'test_research_tools', 'research_audit_roland') or name.endswith('_catalogue'), name
    return 'research'


def outputs():
    rules, phony = parse(baseline())
    assert next(iter(rules)) == 'research-status'
    result = {'Makefile': '# Command index. Keep recipes in cohesive make/ modules.\n'
              '# The historical default is explicit so include order cannot change it.\n'
              '.DEFAULT_GOAL := research-status\n\n' +
              ''.join('include make/' + item + '.mk\n' for item in GROUPS) +
              '\n' + maintenance()}
    for item in GROUPS:
        body = '# Existing ' + item + ' command API; preserve target names and recipes.\n\n'
        for name, recipe in rules.items():
            if group(recipe) != item:
                continue
            if name in phony:
                body += '.PHONY: ' + name + '\n'
            body += name + ':\n' + '\n'.join(recipe) + '\n\n'
        # Preserve any .PHONY-only names without creating a new recipe.
        if item == 'research':
            extra = phony - rules.keys()
            if extra:
                body += '.PHONY: ' + ' '.join(sorted(extra)) + '\n'
        result['make/' + item + '.mk'] = body.rstrip() + '\n'
    return result


def save(data):
    temp = PLAN.with_suffix('.tmp')
    temp.write_text(json.dumps(data, indent=2) + '\n')
    temp.replace(PLAN)


def inspect_scope():
    allowed = set(outputs()) | {SCRIPT}
    changed = set(git('diff', '--name-only').splitlines())
    staged = set(git('diff', '--cached', '--name-only').splitlines())
    untracked = set(git('ls-files', '--others', '--exclude-standard').splitlines())
    assert (changed | staged | untracked) <= allowed, 'Unrelated work present'
    return allowed, changed, staged, untracked


def plan():
    allowed, changed, staged, untracked = inspect_scope()
    assert not staged, 'Existing staged work'
    assert (ROOT / 'Makefile').read_text() == baseline() + '\n' + maintenance(), 'Root changed since bootstrap'
    assert not any((ROOT / ('make/' + g + '.mk')).exists() for g in GROUPS), 'Module path exists'
    result = outputs()
    data = {'head': git('rev-parse', 'HEAD').strip(),
            'source_hash': digest((ROOT / 'Makefile').read_text()),
            'script_hash': digest((ROOT / SCRIPT).read_text()),
            'outputs': {p: {'sha256': digest(t), 'bytes': len(t.encode())}
                        for p, t in result.items()}}
    save(data)
    print(json.dumps(data, indent=2))
    print('Rollback: original Makefile is in Git at ' + BASE + '; no old target is removed.')


def apply():
    guard()
    data = json.loads(PLAN.read_text())
    assert data['head'] == git('rev-parse', 'HEAD').strip()
    assert data['source_hash'] == digest((ROOT / 'Makefile').read_text())
    assert data['script_hash'] == digest((ROOT / SCRIPT).read_text())
    result = outputs()
    assert {p: digest(t) for p, t in result.items()} == {p: v['sha256'] for p, v in data['outputs'].items()}
    (ROOT / 'make').mkdir(exist_ok=True)
    # Write includes first; replace the command index last.
    for p in [p for p in result if p != 'Makefile'] + ['Makefile']:
        path = ROOT / p
        temp = path.with_suffix(path.suffix + '.tmp')
        temp.write_text(result[p])
        temp.replace(path)
    print('Applied reviewed split: ' + ', '.join(result))


def verify():
    root = (ROOT / 'Makefile').read_text()
    assert len(root.splitlines()) < 100, 'Keep root a small command index'
    includes = re.findall(r'^include (.+)$', root, re.M)
    assert includes == ['make/' + g + '.mk' for g in GROUPS], 'Include order changed'
    assert '.DEFAULT_GOAL := research-status' in root.splitlines(), 'Default changed'
    old_rules, old_phony = parse(baseline())
    new_rules, new_phony = {}, set()
    for g in GROUPS:
        rules, phony = parse((ROOT / ('make/' + g + '.mk')).read_text())
        assert not (new_rules.keys() & rules.keys()), 'Duplicate included rule'
        new_rules.update(rules)
        new_phony.update(phony)
    assert all(new_rules.get(k) == v for k, v in old_rules.items()), 'Historical recipe changed'
    assert old_phony <= new_phony, 'Historical .PHONY membership lost'
    assert (new_phony & old_rules.keys()) == (old_phony & old_rules.keys()), 'Historical .PHONY behavior changed'
    source = baseline()
    for target in [None] + list(old_rules):
        args = [] if target is None else [target]
        old = subprocess.run(['make', '--no-print-directory', '-n', '-f', '-'] + args,
                             input=source, cwd=ROOT, text=True, capture_output=True, check=True)
        new = subprocess.run(['make', '--no-print-directory', '-n'] + args,
                             cwd=ROOT, text=True, capture_output=True, check=True)
        assert not old.stderr and not new.stderr, 'Make warning for ' + str(target)
        assert old.stdout == new.stdout, 'Expansion changed: ' + str(target)
    print('PASS: ' + str(len(old_rules)) + ' historical targets, default, recipes and .PHONY preserved; no warnings')


def test():
    rules, phony = parse('.PHONY: one\none:\n\tpython3 script.py\n')
    assert rules == {'one': ['\tpython3 script.py']} and phony == {'one'}
    for bad in ('one:\none:\n', 'VALUE := changed\n', '\tpython3 script.py\n'):
        try:
            parse(bad)
        except AssertionError:
            pass
        else:
            raise AssertionError('Unsafe syntax accepted')
    verify()


def publish(mode):
    guard()
    verify()
    allowed, changed, staged, untracked = inspect_scope()
    subprocess.run(['git', 'diff', '--check'], cwd=ROOT, check=True)
    data = json.loads(PLAN.read_text())
    if mode == 'stage':
        if staged:
            previous = data['review']
            assert previous['head'] == git('rev-parse', 'HEAD').strip()
            assert previous['sha256'] == digest(git('diff', '--cached')), 'Staged work changed since review'
        assert changed | staged | untracked == allowed, 'Missing/unexpected paths'
        subprocess.run(['git', 'add', '--'] + sorted(allowed), cwd=ROOT, check=True)
        subprocess.run(['git', 'diff', '--cached', '--check'], cwd=ROOT, check=True)
        data['outputs'] = {p: {'sha256': digest(text), 'bytes': len(text.encode())}
                           for p, text in outputs().items()}
        data['script_hash'] = digest((ROOT / SCRIPT).read_text())
        data['review'] = {'head': git('rev-parse', 'HEAD').strip(),
                          'sha256': digest(git('diff', '--cached'))}
        save(data)
        print(git('diff', '--cached', '--stat'))
    else:
        assert not changed and not untracked and staged == allowed
        review = data['review']
        assert review['head'] == git('rev-parse', 'HEAD').strip()
        assert review['sha256'] == digest(git('diff', '--cached'))
        subprocess.run(['git', 'diff', '--cached', '--check'], cwd=ROOT, check=True)
        subprocess.run(['git', 'commit', '-m', 'build: split Makefile into verified workflow modules'], cwd=ROOT, check=True)


if __name__ == '__main__':
    assert sys.argv[1:] and sys.argv[1] in MODES
    mode = sys.argv[1]
    if mode in ('stage', 'commit'):
        publish(mode)
    else:
        globals()[mode]()
