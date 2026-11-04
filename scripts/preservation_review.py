"""Read-only review of a registered original body against its canonical copy."""
import difflib
import json
from pathlib import Path
import re
import sys
sys.dont_write_bytecode = True
import research_tools
from canonical_links import preservation_text

research_tools.identity()
assert len(sys.argv) == 2, 'Pass one registered source path'
state = json.loads((research_tools.ROOT / 'research-state.json').read_text())
entries = [x for x in state['consolidation_and_price_findings'] if x.get('source') == sys.argv[1] and x.get('verification_kind') == 'complete-source-body-v1']
assert len(entries) == 1, 'Source must identify one complete body'
e = entries[0]
source = research_tools.read_preserved_source(e['source'])
if e.get('source_section'):
    fragment = source.split('\n## ' + e['source_section'] + '\n', 1)[1].split('\n## ', 1)[0]
    source = '# ' + e['model_name'] + '\n' + fragment
text = preservation_text(e['destination'].split('#')[0])
prefix = e['marker']
body = text.split('<!-- ' + prefix + ' source begins -->\n', 1)[1].split('<!-- ' + prefix + ' source ends -->', 1)[0]
normalized = body
for old, new in e.get('link_normalizations', {}).items():
    normalized = normalized.replace(new, old)
for ref in e['renamed_references']:
    normalized = normalized.replace('[' + prefix + '-' + ref + ']', '[' + ref + ']')
normalized = re.sub(r'^### ', '## ', normalized, flags=re.M)
expected = source.split('\n', 1)[1]
plan = {'head': research_tools.git('rev-parse', 'HEAD').strip(), 'source': e['source'], 'destination': e['destination'], 'marker': prefix, 'expected_original_body': expected, 'current_normalized_body': normalized, 'equal': normalized == expected}
Path('/tmp/instrumentfx-preservation-review.json').write_text(json.dumps(plan, indent=2) + '\n')
print(''.join(difflib.unified_diff(expected.splitlines(True), normalized.splitlines(True), fromfile='registered original', tofile='current canonical copy')) or 'PASS: exact original body retained')
print('Read-only review: /tmp/instrumentfx-preservation-review.json')
