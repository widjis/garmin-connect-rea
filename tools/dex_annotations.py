import zipfile,struct,json
from pathlib import Path
root=Path(__file__).resolve().parents[1];results=[]
with zipfile.ZipFile(root/'apk/base.apk') as z:
 for name in z.namelist():
  if not name.endswith('.dex'):continue
  b=z.read(name)
  def u32(p):return struct.unpack_from('<I',b,p)[0]
  def uleb(p):
   v=0;s=0
   while True:
    c=b[p];p+=1;v|=(c&127)<<s;s+=7
    if c<128:return v,p
  sn,so=struct.unpack_from('<II',b,56);strings=[]
  for i in range(sn):
   p=uleb(u32(so+4*i))[1];strings.append(b[p:b.index(b'\0',p)].decode('utf8','replace'))
  tn,to=struct.unpack_from('<II',b,64);types=[strings[u32(to+4*i)] for i in range(tn)]
  mn,mo=struct.unpack_from('<II',b,88)
  def meth(i):
   c,pr,s=struct.unpack_from('<HHI',b,mo+8*i);return types[c]+'->'+strings[s]
  def val(p):
   h=b[p];p+=1;t=h&31;n=(h>>5)+1
   if t==28:
    count,p=uleb(p);vs=[]
    for _ in range(count):v,p=val(p);vs.append(v)
    return vs,p
   if t==29:return ann(p)
   if t==30:return None,p
   if t==31:return bool(h>>5),p
   v=int.from_bytes(b[p:p+n],'little');p+=n
   if t==23:v=strings[v]
   if t==24:v=types[v]
   return v,p
  def ann(p):
   ti,p=uleb(p);count,p=uleb(p);a={'annotation':types[ti]}
   for _ in range(count):si,p=uleb(p);v,p=val(p);a[strings[si]]=v
   return a,p
  cn,co=struct.unpack_from('<II',b,96)
  for i in range(cn):
   ao=u32(co+32*i+20)
   if not ao:continue
   fs,ms,ps=struct.unpack_from('<III',b,ao+4)
   for j in range(ms):
    mi,aset=struct.unpack_from('<II',b,ao+16+8*fs+8*j);anns=[]
    for k in range(u32(aset)):anns.append(ann(u32(aset+4+4*k)+1)[0])
    if any('workout-service' in str(a) or 'download' in str(a).lower() and ('device' in str(a).lower() or 'queue' in str(a).lower()) for a in anns):results.append({'dex':name,'method':meth(mi),'annotations':anns})
(root/'evidence/dex-api-annotations.json').write_text(json.dumps(results,indent=2))
for r in results:print(r['method'],r['annotations'])
