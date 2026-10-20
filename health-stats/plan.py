"""Offline GET-template planner. Never reads credentials or imports HTTP clients."""
import argparse,json
from pathlib import Path

def plan(manifest):
    seen=set()
    for r in manifest['routes']:
        if r['http_method']!='GET' or r['unsafe_literal'] or r['path_literal'] in seen:
            continue
        seen.add(r['path_literal'])
        path=r['path_literal']
        query=[x['name']+'=<'+x['name']+'>' for x in r['parameters'] if x['annotation']=='t']
        if query:path+=('&' if '?' in path else '?')+'&'.join(query)
        yield 'GET <VERIFIED_NATIVE_BASE_HOST>/'+path.lstrip('/')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan',action='store_true',required=True)
    parser.parse_args()
    manifest=json.loads(Path(__file__).with_name('manifest.json').read_text())
    print('# OFFLINE ONLY. Placeholders; not executable HTTP requests.')
    print('\n'.join(plan(manifest)))

if __name__=='__main__':main()
