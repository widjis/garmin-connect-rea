#!/usr/bin/env python3
"""Explicit single-day test; existing session only, GET only, no refresh/login.
Saves schema-only metadata, never raw response/identity/measurement values.
"""
import hashlib
import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import quote, urlencode
from urllib.request import HTTPRedirectHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://connectapi.garmin.com'
TEMPLATE = '/usersummary-service/usersummary/mobile/daily/{displayName}'

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--authorize-read", action="store_true", required=True, help="Explicitly authorize the existing-session profile and daily-summary GETs")
    parser.parse_args()
    os.umask(0o077)
    now = datetime.now().astimezone()
    day = (now.date() - timedelta(days=1)).isoformat()
    result = {'collected_at': now.isoformat(), 'calendarDate': day,
              'date_basis': 'Last completed machine-local calendar day; account timezone not established',
              'base_host': BASE, 'endpoint_template': TEMPLATE, 'requests': [],
              'login_attempts': 0, 'refresh_attempts': 0, 'health_request_count': 0,
              'raw_response_retained': False}
    path = ROOT / '.private/android-token.json'
    before = None
    try:
        if path.is_symlink():
            raise ValueError('Refuse symlink session')
        raw = path.read_bytes()
        before = hashlib.sha256(raw).digest()
        token = json.loads(raw)
        if not isinstance(token.get('access_token'), str) or not token['access_token']:
            raise ValueError('No existing access token')
        opener = build_opener(NoRedirect())
        def get(route, label, params=None):
            assert route == '/userprofile-service/socialProfile/v2' or route.startswith('/usersummary-service/usersummary/mobile/daily/')
            request = Request(BASE + route + ('?' + urlencode(params) if params else ''),
                              headers={'Authorization': 'Bearer ' + token['access_token'],
                                       'User-Agent': 'REA-Android-Flow-Test/1.0', 'Accept': 'application/json'}, method='GET')
            try:
                response = opener.open(request, timeout=30)
            except HTTPError as error:
                response = error
            with response:
                status = response.code
                content_type = response.headers.get_content_type()
                body = response.read(4 * 1024 * 1024)
            entry = {'method': 'GET', 'path_template': label, 'status': status, 'content_type': content_type}
            result['requests'].append(entry)
            try:
                data = json.loads(body)
                entry['json_valid'] = True
            except (ValueError, UnicodeError):
                data = None
                entry['json_valid'] = False
            if status != 200 or not entry['json_valid']:
                result['verdict'] = 'blocked_http_or_non_json'
                raise RuntimeError('HTTP or JSON blocker')
            return data
        # Source-proven self-profile GET: evidence/dex-all-http-annotations.json
        # Leo1/a;->a, Li83/f; annotation, lines 1312-1332. No identity path supplied.
        profile = get('/userprofile-service/socialProfile/v2', '/userprofile-service/socialProfile/v2')
        display = profile.get('displayName') if isinstance(profile, dict) else None
        if not isinstance(display, str) or not display:
            result['verdict'] = 'blocked_self_profile_missing_displayName'
            raise RuntimeError('No active self-profile displayName')
        result['health_request_count'] = 1
        data = get(TEMPLATE.replace('{displayName}', quote(display, safe='')), TEMPLATE, {'calendarDate': day})
        if not isinstance(data, dict):
            result['verdict'] = 'blocked_unexpected_summary_shape'
            raise RuntimeError('Unexpected summary shape')
        keys = ['totalSteps', 'totalDistanceMeters', 'wellnessDistanceMeters', 'totalKilocalories',
                'activeKilocalories', 'bmrKilocalories', 'floorsAscended', 'floorsDescended',
                'moderateIntensityMinutes', 'vigorousIntensityMinutes', 'restingHeartRate',
                'maxHeartRate', 'averageStressLevel']
        result['fields'] = {key: {'present': key in data, 'type': type(data[key]).__name__ if key in data else None,
                                  'null': data[key] is None if key in data else None} for key in keys}
        result['top_level_field_names'] = sorted(data)
        result['calendar_date_matches'] = data.get('calendarDate') == day
        result['non_null_metric_fields'] = sum(key in data and data[key] is not None for key in keys)
        valid = result['calendar_date_matches'] and result['non_null_metric_fields'] > 0
        result['verdict'] = 'live_daily_summary_verified' if valid else 'summary_json_unverified_or_empty'
    except Exception as error:
        result.setdefault('verdict', 'blocked_local_or_transport')
        result['error_type'] = type(error).__name__
    finally:
        try:
            result['session_file_unchanged'] = before is not None and hashlib.sha256(path.read_bytes()).digest() == before
        except OSError:
            result['session_file_unchanged'] = False
    out = ROOT / '.private/live-health-test' / (now.strftime('%Y%m%dT%H%M%S%z') + '.json')
    out.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + '\n')
    out.chmod(0o600)
    print(json.dumps({'metadata_path': str(out), **result}, indent=2))

if __name__ == '__main__':
    main()
