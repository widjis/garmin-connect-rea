"""Offline evidence-integrity and planner regression checks; no account access."""
import hashlib,json,subprocess,sys
from pathlib import Path
from plan import plan
ROOT=Path(__file__).resolve().parent
m=json.loads((ROOT/'manifest.json').read_text())
assert m['live_tested'] is False
assert m['apk_sha256']==hashlib.sha256((ROOT.parent/'apk/base.apk').read_bytes()).hexdigest()
assert m['route_declaration_count']==len(m['routes'])
assert m['unique_route_literal_count']==len({r['path_literal'] for r in m['routes']})
assert m['model_count']==len(m['models'])
for r in m['routes']:
    assert r['http_method']=='GET'
    lines=(ROOT.parent/r['source']).read_text().splitlines()
    assert r['path_literal'] in lines[r['line']-1]
    assert r['signature']==lines[r['line']].strip()
for model in m['models']:
    lines=(ROOT.parent/model['source']).read_text().splitlines()
    for f in model['fields']:
        assert f.get('annotation',f.get('name','')) in lines[f['line']-1]
rea=json.loads(json.loads((ROOT/'evidence/rea-package.json').read_text())['content'][0]['text'])
assert rea['evidence_id']==m['rea_evidence_id']
assert rea['subject']['digest']['sha256']==m['apk_sha256']
assert rea['normalized_result']['package_name']==m['package']
assert rea['normalized_result']['version_name']==m['version']
actual=list(plan(m))
assert len(actual)==len(set(actual))
assert all(x.startswith('GET <VERIFIED_NATIVE_BASE_HOST>/') for x in actual)
assert all('\\u200b' not in x and '\u200b' not in x for x in actual)
# Synthetic negative fixture: a mutation and malformed GET must never be planned.
synthetic={'routes':[{'http_method':'POST','path_literal':'synthetic-write','unsafe_literal':False,'parameters':[]},{'http_method':'GET','path_literal':'synthetic-bad\\u200b','unsafe_literal':True,'parameters':[]}]}
assert list(plan(synthetic))==[]
output=subprocess.check_output([sys.executable,str(ROOT/'plan.py'),'--plan'],text=True)
assert output.count('\nGET ')==len(actual)
result={'result':'PASS','checks':['APK fingerprint','REA identity/version','every GET literal/signature/source line','every model field source line','route/model counts','deduplicated offline plan','synthetic mutation/malformed-route exclusion','planner CLI execution'],'get_declarations':len(m['routes']),'distinct_get_literals':m['unique_route_literal_count'],'model_entries':len(m['models']),'planned_templates':len(actual),'live_requests':0}
(ROOT/'evidence/verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
