#!/usr/bin/env python3
"""Interactive local authentication, one test workout, then API readback."""
import getpass
import importlib.metadata
import json
import logging
import os
import sys
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import urlsplit
from garminconnect.client import Client

ROOT = Path(__file__).resolve().parents[1]
PRIVATE = ROOT / '.private'
OUT = ROOT / '.private/live-create'
os.umask(0o077)
PRIVATE.mkdir(exist_ok=True, mode=0o700)
OUT.mkdir(parents=True, exist_ok=True)
logging.disable(logging.CRITICAL)
STATE = OUT / 'result.json'
state = json.loads(STATE.read_text()) if STATE.exists() else {
    'run_id': datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'),
    'stage': 'prepared', 'network': [],
    'library': 'garminconnect ' + importlib.metadata.version('garminconnect'),
    'auth_strategy': 'mobile+requests (library iOS SSO identity)',
}
state['workout_name'] = 'REA - API Test ' + state['run_id']

def save(stage):
    state['stage'] = stage
    state['updated_utc'] = datetime.now(timezone.utc).isoformat()
    tmp = STATE.with_suffix('.tmp')
    tmp.write_text(json.dumps(state, indent=2) + '\n')
    tmp.replace(STATE)
    print(stage, flush=True)

def hook(response, *args, **kwargs):
    u = urlsplit(response.url)
    # No headers, bodies, query strings, credentials or tokens in evidence.
    state['network'].append({'method': response.request.method,
                             'host': u.hostname, 'path': u.path,
                             'status': response.status_code})

class ObservedClient(Client):
    def _post_credentials(self, sess, *args, **kwargs):
        if hook not in sess.hooks.get('response', []):
            sess.hooks.setdefault('response', []).append(hook)
        return super()._post_credentials(sess, *args, **kwargs)

if state.get('error_type') == 'GarminConnectTooManyRequestsError' and '--retry-auth' not in sys.argv:
    print('Percobaan sebelumnya terkena rate limit. Tidak ada login ulang otomatis.')
    print('Setelah masalah rate limit selesai, jalankan manual dengan --retry-auth.')
    raise SystemExit(2)

client = ObservedClient()
client.skip_strategies = {'mobile+cffi', 'widget+cffi', 'portal+cffi', 'portal+requests'}
client.cs.hooks['response'].append(hook)
client._api_session.hooks['response'].append(hook)
try:
    if state['stage'] == 'verified':
        print('Sudah berhasil. workoutId:', state['workout_id'])
        raise SystemExit(0)
    print('Uji: login Garmin, create satu workout lari 20 menit, lalu GET verifikasi.')
    print('Password/kode MFA tidak disimpan. Token sesi disimpan lokal di .private (mode 600).')
    save('waiting_for_local_login')
    session_dir = PRIVATE / 'session'
    if session_dir.exists():
        client.load(str(session_dir))
        save('session_loaded')
    else:
        email = getpass.getpass('Email Garmin (tersembunyi): ').strip()
        password = getpass.getpass('Password Garmin: ')
        save('authenticating')
        client.login(email, password, prompt_mfa=lambda: getpass.getpass('Kode MFA Garmin: ').strip())
        del email, password
        session_dir.mkdir(mode=0o700, exist_ok=True)
        client.dump(str(session_dir))
        for p in session_dir.iterdir():
            if p.is_file():p.chmod(0o600)
        save('authenticated')
    # A successful authenticated read must precede the write.
    resp = client.request('GET', 'connectapi', '/workout-service/workouts',
                          params={'start': 0, 'limit': 100, 'orderBy': 'UPDATE_DATE', 'orderSeq': 'DESC'})
    workouts = resp.json()
    if not isinstance(workouts, list):raise ValueError('Unexpected workout list structure')
    state['authenticated_read_status'] = resp.status_code
    save('authenticated_read_ok')
    existing = next((w for w in workouts if w.get('workoutName') == state['workout_name']), None)
    if not state.get('workout_id') and existing:
        state['workout_id'] = existing['workoutId']
        save('existing_test_workout_recovered')
    if not state.get('workout_id'):
        # An earlier ambiguous POST requires explicit reconciliation; never blindly repeat it.
        if state.get('post_attempted'):
            raise RuntimeError('Earlier POST outcome unresolved; reconcile before retry')
        body = json.loads((ROOT / 'examples/create-workout.candidate.json').read_text())
        body['workoutName'] = state['workout_name']
        body['description'] = 'API authentication and create/readback test. Not scheduled or sent to a watch.'
        (OUT / 'create-request.json').write_text(json.dumps(body, indent=2) + '\n')
        state['post_attempted'] = True
        save('creating_workout')
        resp = client.request('POST', 'connectapi', '/workout-service/workout', json=body)
        created = resp.json()
        state['create_status'] = resp.status_code
        state['workout_id'] = created['workoutId']
        # Keep only workout-specific fields; omit returned owner/account identifiers.
        fields = ['workoutId', 'workoutName', 'sportType', 'description', 'workoutSegments']
        (OUT / 'create-response.json').write_text(json.dumps({k:created[k] for k in fields if k in created}, indent=2) + '\n')
        save('created')
    wid = state['workout_id']
    resp = client.request('GET', 'connectapi', f'/workout-service/workout/{wid}')
    readback = resp.json()
    fields = ['workoutId', 'workoutName', 'sportType', 'description', 'workoutSegments']
    (OUT / 'readback.json').write_text(json.dumps({k:readback[k] for k in fields if k in readback}, indent=2) + '\n')
    step = readback['workoutSegments'][0]['workoutSteps'][0]
    state['verification'] = {
        'id_matches': str(readback['workoutId']) == str(wid),
        'name_matches': readback['workoutName'] == state['workout_name'],
        'running_sport': readback['sportType']['sportTypeId'] == 1,
        'duration_1200_seconds': step['endCondition']['conditionTypeId'] == 2 and float(step['endConditionValue']) == 1200,
        'target_none': step['targetType']['workoutTargetTypeId'] == 1,
    }
    state['readback_status'] = resp.status_code
    if not all(state['verification'].values()):raise ValueError('Readback does not match planned workout')
    save('verified')
    print('BERHASIL. workoutId:', wid)
    print('Workout:', state['workout_name'])
    print('Bukti:', OUT)
except (KeyboardInterrupt, EOFError):
    save('cancelled')
except Exception as exc:
    state['error_type'] = type(exc).__name__
    state['failure_stage'] = state['stage']
    # Deliberately do not serialize exception text; upstream errors may include secrets.
    save('failed')
    print('Uji berhenti:', state['error_type'])
    print('Status HTTP yang aman ada di', STATE)
    raise SystemExit(1)
