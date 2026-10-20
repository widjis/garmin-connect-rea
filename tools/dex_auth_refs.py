import zipfile,struct,json
from pathlib import Path
root=Path(__file__).resolve().parents[1];out=[]
with zipfile.ZipFile(root/'apk/base.apk') as z:
 for name in z.namelist():
  if not name.endswith('.dex'):continue
  b=z.read(name)
  def u32(p):return struct.unpack_from('<I',b,p)[0]
  def ul(p):
   v=0;s=0
   while True:
    c=b[p];p+=1;v|=(c&127)<<s;s+=7
    if c<128:return v,p
  sn,so=struct.unpack_from('<II',b,56);ss=[]
  for i in range(sn):
   p=ul(u32(so+4*i))[1];ss.append(b[p:b.index(b'\0',p)].decode('utf8','replace'))
  targets={i:s for i,s in enumerate(ss) if any(k in s for k in ['GCM_ANDROID_DARK','SSO_PORTAL_CLIENT_ID_DARK','service_ticket=','/di-oauth2-service/oauth/grant/service_ticket','/portal/signin','/signin?']) and len(s)<200}
  if not targets:continue
  tn,to=struct.unpack_from('<II',b,64);ts=[ss[u32(to+4*i)] for i in range(tn)];mn,mo=struct.unpack_from('<II',b,88)
  cn,co=struct.unpack_from('<II',b,96)
  for c in range(cn):
   p=u32(co+32*c+24)
   if not p:continue
   sizes=[]
   for _ in range(4):v,p=ul(p);sizes.append(v)
   for _ in range(sizes[0]+sizes[1]):_,p=ul(p);_,p=ul(p)
   for count in sizes[2:]:
    idx=0
    for _ in range(count):
     delta,p=ul(p);idx+=delta;_,p=ul(p);code,p=ul(p)
     if not code:continue
     n=u32(code+12);start=code+16
     for k in range(n-1):
      off=start+2*k;op=b[off]
      if op not in (26,27):continue
      si=struct.unpack_from('<H',b,off+2)[0] if op==26 else (u32(off+2) if k+2<n else -1)
      if si in targets:
       ci,pr,ni=struct.unpack_from('<HHI',b,mo+8*idx)
       out.append({'dex':name,'class':ts[ci][1:-1].replace('/','.'),'method':ss[ni],'value':targets[si],'code_unit_candidate':k})
(root/'evidence/auth-string-ref-candidates.json').write_text(json.dumps(out,indent=2))
for r in out:print(r)
