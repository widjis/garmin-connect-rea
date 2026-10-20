import zipfile,struct,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
out=[]
with zipfile.ZipFile(root/'apk/base.apk') as z:
 for name in z.namelist():
  if not name.endswith('.dex'):continue
  b=z.read(name); n,off=struct.unpack_from('<II',b,56)
  for i in range(n):
   p=struct.unpack_from('<I',b,off+4*i)[0]
   while b[p]&128:p+=1
   p+=1;s=b[p:b.index(b'\0',p)].decode('utf8','replace')
   if any(k in s.lower() for k in ['workout-service','workout/','workouts/','download-service','device/','sendto','send_to','workoutsegment','workoutstep']):out.append({'dex':name,'index':i,'value':s})
(root/'evidence/dex-strings.json').write_text(json.dumps(out,indent=2))
for x in out:
 if '/' in x['value'] and len(x['value'])<300:print(x['value'])
