#!/usr/bin/env python3
"""Garmin Android SSO portal -> service ticket -> DI token -> workout POST/GET.
The UI bridge receives auth results only; it never reads login fields.
Native Play Integrity is not emulated or forged.
"""
import asyncio
import base64
import json
import os
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import urlsplit
import requests
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '.private/android-live-create'
PRIVATE = ROOT / '.private'
URL = 'https://sso.garmin.com/mobile/sso/en-US/sign-in?clientId=GCM_ANDROID_DARK'
SERVICE = 'https://mobile.integration.garmin.com/gcm/android'
CLIENT_ID = 'GARMIN_CONNECT_MOBILE_ANDROID_DI_2025Q2'
TOKEN_URL = 'https://diauth.garmin.com/di-oauth2-service/oauth/token'
GRANT = 'https://connectapi.garmin.com/di-oauth2-service/oauth/grant/service_ticket'
os.umask(0o077)
OUT.mkdir(parents=True, exist_ok=True)
PRIVATE.mkdir(mode=0o700, exist_ok=True)
STATE = OUT / 'result.json'
state = json.loads(STATE.read_text()) if STATE.exists() else {
    'run_id': datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'),
    'network': [], 'events': [],
    'flow': 'APK Android SSO portal + GMNEventHandler + DI service_ticket grant',
    'sso_client_id': 'GCM_ANDROID_DARK', 'di_client_id': CLIENT_ID,
    'limitations': ['Desktop Chrome replaces Android WebView',
                    'DI client base name corroborated by Python library; APK uses StringRetriever index 7 and _2025Q2 suffix',
                    'No native Play Integrity app-validation token; no token emulation',
                    'HTTP User-Agent is an explicit research client, not an exact app header replay'],
}
state['workout_name'] = 'REA - Android API Test ' + state['run_id']

def save(stage):
    state['stage'] = stage
    state['updated_utc'] = datetime.now(timezone.utc).isoformat()
    tmp=STATE.with_suffix('.tmp');tmp.write_text(json.dumps(state, indent=2)+'\n');tmp.replace(STATE)
    print(stage, flush=True)

def record(method, url, status):
    u=urlsplit(url)
    state['network'].append({'method':method,'host':u.hostname,'path':u.path,'status':status})

def http(sess, method, url, **kw):
    r=sess.request(method,url,timeout=30,**kw)
    record(method,url,r.status_code)
    state['last_http_status']=r.status_code
    if not 200<=r.status_code<300:
        save('http_error')
        raise RuntimeError('HTTP status '+str(r.status_code))
    return r

def create_and_verify(token):
    sess=requests.Session()
    sess.headers.update({'Authorization':'Bearer '+token,'User-Agent':'REA-Android-Flow-Test/1.0', 'Accept':'application/json'})
    base='https://connectapi.garmin.com'
    save('checking_authenticated_read')
    r=http(sess,'GET',base+'/workout-service/workouts',params={'start':0,'limit':100,'orderBy':'UPDATE_DATE','orderSeq':'DESC'})
    ws=r.json()
    if not isinstance(ws,list):raise ValueError('Unexpected list format')
    state['authenticated_read_status']=r.status_code
    save('authenticated_read_ok')
    existing=next((w for w in ws if w.get('workoutName')==state['workout_name']),None)
    if existing and not state.get('workout_id'):state['workout_id']=existing['workoutId']
    if not state.get('workout_id'):
        if state.get('post_attempted'):raise RuntimeError('Ambiguous prior POST requires reconciliation')
        body=json.loads((ROOT/'examples/create-workout.candidate.json').read_text())
        body['workoutName']=state['workout_name']
        body['description']='Android portal authentication and create/readback test. Not scheduled or sent to device.'
        (OUT/'create-request.json').write_text(json.dumps(body,indent=2)+'\n')
        state['post_attempted']=True;save('creating_workout')
        r=http(sess,'POST',base+'/workout-service/workout',json=body)
        data=r.json();state['create_status']=r.status_code;state['workout_id']=data['workoutId']
        keys=['workoutId','workoutName','sportType','description','workoutSegments']
        (OUT/'create-response.json').write_text(json.dumps({k:data[k] for k in keys if k in data},indent=2)+'\n')
        save('created')
    wid=state['workout_id'];r=http(sess,'GET',base+f'/workout-service/workout/{wid}');data=r.json()
    keys=['workoutId','workoutName','sportType','description','workoutSegments']
    (OUT/'readback.json').write_text(json.dumps({k:data[k] for k in keys if k in data},indent=2)+'\n')
    st=data['workoutSegments'][0]['workoutSteps'][0]
    state['readback_status']=r.status_code
    state['verification']={'id_matches':str(data['workoutId'])==str(wid),
        'name_matches':data['workoutName']==state['workout_name'],
        'sport_running':data['sportType']['sportTypeId']==1,
        'time_1200_seconds':st['endCondition']['conditionTypeId']==2 and float(st['endConditionValue'])==1200,
        'target_none':st['targetType']['workoutTargetTypeId']==1}
    if not all(state['verification'].values()):raise ValueError('Readback mismatch')
    save('verified');print('workoutId:',wid,flush=True)

async def main():
    if state.get('stage')=='verified':print('Already verified',state['workout_id']);return
    ticket_data={}
    try:
        save('opening_official_android_portal')
        async with async_playwright() as p:
            browser=await p.chromium.launch(executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless=False)
            context=await browser.new_context(viewport={'width':460,'height':860})
            async def bridge(source, raw):
                if urlsplit(source['frame'].url).hostname!='sso.garmin.com':return
                try:event=json.loads(raw) if isinstance(raw,str) else raw
                except (ValueError,TypeError):return
                kind=event.get('eventType')
                if kind:state['events'].append({'eventType':kind,'flowName':event.get('flowName')})
                if kind=='USER_AUTHENTICATED':
                    d=event.get('data') or {}
                    if d.get('serviceUrl')!=SERVICE:save('unexpected_service_url');return
                    if d.get('serviceTicket'):
                        ticket_data.update(d);save('android_portal_authenticated')
                else:save('waiting_for_official_login')
            await context.expose_binding('__reaGarminEvent',bridge)
            await context.add_init_script("if(location.hostname==='sso.garmin.com'){window.GMNEventHandler={handleEvent:(x)=>window.__reaGarminEvent(x)};}")
            page=await context.new_page()
            async def response(r):
                u=urlsplit(r.url)
                if u.hostname=='sso.garmin.com' and ('/api/' in u.path or '/sign-in' in u.path):
                    record(r.request.method,r.url,r.status)
                    save('waiting_for_official_login' if not ticket_data else 'android_portal_authenticated')
            page.on('response',response)
            await page.goto(URL,wait_until='domcontentloaded',timeout=60000)
            save('waiting_for_official_login')
            print('Login pada halaman resmi Garmin di Chrome. Jangan masukkan password di chat.',flush=True)
            loop=asyncio.get_running_loop();deadline=loop.time()+900
            while not ticket_data:
                if loop.time()>deadline:raise TimeoutError('Waiting for user login')
                if page.is_closed():raise RuntimeError('Login browser closed')
                await asyncio.sleep(0.5)
            await browser.close()
        save('exchanging_android_service_ticket')
        sess=requests.Session();sess.headers.update({'User-Agent':'REA-Android-Flow-Test/1.0','Accept':'application/json'})
        r=http(sess,'POST',TOKEN_URL,auth=(CLIENT_ID,''),data={
            'client_id':CLIENT_ID,'service_ticket':ticket_data['serviceTicket'],
            'grant_type':GRANT,'service_url':SERVICE})
        token=r.json();ticket_data.clear()
        if not token.get('access_token'):raise ValueError('No API access token')
        (PRIVATE/'android-token.json').write_text(json.dumps(token))
        (PRIVATE/'android-token.json').chmod(0o600)
        state['token_exchange_status']=r.status_code;save('api_token_received')
        await asyncio.to_thread(create_and_verify,token['access_token'])
    except Exception as exc:
        state['failure_stage']=state.get('stage');state['error_type']=type(exc).__name__
        save('failed');print('Error type:',type(exc).__name__,flush=True)

if __name__=='__main__':asyncio.run(main())
