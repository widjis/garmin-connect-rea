import json,requests
from pathlib import Path
from datetime import datetime,timezone
r=Path(__file__).resolve().parents[1];out=r/'.private/running';out.mkdir(parents=True, exist_ok=True)
t=json.loads((r/'.private/android-token.json').read_text());s=requests.Session();s.headers.update({'Authorization':'Bearer '+t['access_token'],'User-Agent':'REA-Android-Flow-Test/1.0'})
results=[]
for name,path in [('workout-types','/workout-service/workout/types'),('workout-sports','/workout-service/workout/types/sport')]:
 x=s.get('https://connectapi.garmin.com'+path,timeout=30)
 results.append({'path':path,'status':x.status_code,'time_utc':datetime.now(timezone.utc).isoformat()})
 print(name,x.status_code)
 if x.ok:
  j=x.json();(out/(name+'.json')).write_text(json.dumps(j,indent=2)+'\n');print('keys:',list(j)[:30] if isinstance(j,dict) else 'list length '+str(len(j)))
 else:break
(out/'metadata-status.json').write_text(json.dumps(results,indent=2)+'\n')
