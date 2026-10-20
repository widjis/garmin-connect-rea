"""Build a static catalog from local JADX evidence, never from account data."""
import hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
SERVICE={'b22.h','iq1.a','im1.a','nz1.a','ax.a','lw.a','my.a','do0.b','hr0.a','ip0.a','rh0.a','m42.a','v31.a','p61.a','s32.a','bx1.a','jr1.a','com.garmin.android.apps.connectmobile.pulseox.data.a','com.garmin.android.apps.connectmobile.respiration.data.d'}
if not list((ROOT/'sources').glob('*.java')) or not (ROOT/'evidence/rea-package.json').is_file() or not (ROOT.parent/'apk/base.apk').is_file():
    raise SystemExit('Local APK, selected JADX sources and REA evidence are required and intentionally not bundled; see PUBLICATION.md')
routes=[]; models=[]
for p in sorted((ROOT/'sources').glob('*.java')):
    lines=p.read_text().splitlines()
    if p.stem in SERVICE:
        for i,line in enumerate(lines):
            m=re.search(r'@(?:i83\.)?f\("([^\"]+)"\)',line)
            if not m: continue
            signature=lines[i+1].strip()
            method_match=re.search(r'\s(\w+)\(',signature)
            assert method_match, (p,i,signature)
            method=method_match.group(1)
            if p.stem=='bx1.a' and method not in {'e','n'}: continue
            path=m.group(1)
            # Preserve Java annotation string exactly; no repair of malformed route.
            routes.append({'http_method':'GET','path_literal':path,'class_raw':p.stem,'method':method,'signature':signature,'source':'health-stats/sources/'+p.name,'line':i+1,'parameters':[{'annotation':a,'name':n} for a,n in re.findall(r'@(?:i83\.)?(s|t)\("([^\"]+)"\)',signature)],'confidence':'static annotation; not live tested','unsafe_literal':'\\u200b' in path})
    fields=[]
    for i,line in enumerate(lines):
        m=re.search(r'@SerializedName\((.+)\)',line)
        if m:
            j=i+1
            while j<len(lines) and (lines[j].strip().startswith('@') or not lines[j].strip()):j+=1
            fields.append({'annotation':m.group(1),'declaration':lines[j].strip(),'line':i+1,'kind':'Gson wire name'})
        m=re.search(r'\w+\.j\("([^\"]+)", (true|false)\)',line)
        if m: fields.append({'name':m.group(1),'serializer_optional':m.group(2)=='true','line':i+1,'kind':'Kotlin serializer descriptor'})
    if fields:models.append({'class_raw':p.stem,'source':'health-stats/sources/'+p.name,'fields':fields})
rea=json.loads(json.loads((ROOT/'evidence/rea-package.json').read_text())['content'][0]['text'])
manifest={'analysis_date':'2026-10-20','apk_sha256':hashlib.sha256((ROOT.parent/'apk/base.apk').read_bytes()).hexdigest(),'package':rea['normalized_result']['package_name'],'version':rea['normalized_result']['version_name'],'version_code':rea['normalized_result']['version_code'],'rea_evidence_id':rea['evidence_id'],'rea_operation':rea['operation'],'route_declaration_count':len(routes),'unique_route_literal_count':len({r['path_literal'] for r in routes}),'model_count':len(models),'routes':routes,'models':models,'live_tested':False,'credential_files_read':False}
(ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2))
rows=['# Static GET route catalog','',f"{len(routes)} declarations; {manifest['unique_route_literal_count']} distinct exact route literals. No live requests. Source locations are relative to the Garmin folder. `s` = path, `t` = query; annotation `f` = Retrofit GET. Return wrappers and aliases are kept verbatim; this is not a complete OpenAPI schema.",'','| GET route literal | Raw class.method | Parameters (s=path, t=query) | Evidence |','|---|---|---|---|']
for r in routes:
    rows.append('| `'+r['path_literal']+'` | `'+r['class_raw']+'.'+r['method']+'` | '+', '.join('`'+x['annotation']+':'+x['name']+'`' for x in r['parameters'])+' | `'+r['source']+':'+str(r['line'])+'` |')
rows+=['','## Return contracts','']
for r in routes:rows+=['- `'+r['class_raw']+'.'+r['method']+'`: `'+r['signature']+'`']
(ROOT/'ENDPOINTS.md').write_text('\n'.join(rows)+'\n')
rows=['# Wire model evidence','','Gson annotation names and Kotlin serialization descriptor names, not invented sample responses. Reference/boxed types may be nullable; confirm Kotlin metadata/defaults before enforcing required fields. A serializer optional flag describes this client serializer, not server availability. Source references are relative to the Garmin folder.','']
for m in models:
    rows+=['## '+m['class_raw'],'','Source: `'+m['source']+'`','','| Wire annotation/name | Type/declaration or serializer optional | Line |','|---|---|---|']
    for f in m['fields']:rows+=['| `'+f.get('annotation',f.get('name',''))+'` | `'+f.get('declaration','optional='+str(f.get('serializer_optional')))+'` | '+str(f['line'])+' |']
    rows+=['']
(ROOT/'MODELS.md').write_text('\n'.join(rows))
print(json.dumps({k:v for k,v in manifest.items() if k not in {'routes','models'}},indent=2))
