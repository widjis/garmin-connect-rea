"""Build a research matrix, not a list of server/device-validated combinations."""
import csv,itertools,json,math
from pathlib import Path
r=Path(__file__).resolve().parents[1];d=r/'running';d.mkdir(exist_ok=True)
steps={'warmup':1,'run':3,'walk':4,'recovery':4,'rest':5,'cooldown':2,'other':7}
ends={'time':2,'distance':3,'lap':1,'calories':4,'heart_rate_threshold':6}
targets={'none':1,'pace_range':6,'cadence_range':3,'hr_zone':4,'hr_bpm_range':4,'power_zone':2,'power_watts_range':2}
rows=[]
for step,end,target in itertools.product(steps,ends,targets):
 status='candidate_from_app_options'
 if step=='walk' and target.startswith('power'):status='not_in_running_walk_ui_branch'
 elif target.startswith('power'):status='feature_gated_candidate'
 rows.append({'step':step,'end':end,'target':target,'status':status,'live_validation':'not_tested_except_single_run_time_none_fixture','device_validation':'not_tested'})
with (d/'combination-matrix.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
catalog={'sport':{'sportTypeId':1,'sportTypeKey':'running'},'step_roles':steps,'end_conditions':ends,'primary_target_modes':targets,
 'matrix_rows':len(rows),'matrix_meaning':'Categorical research candidates, not accepted combinations. Numeric ranges, repeats, secondary targets and device constraints are separate axes.',
 'structures':['linear','repeat_fixed_count','repeat_until_time','nested_repeat_candidate','skip_last_rest_candidate','smart_repeat_candidate'],
 'secondary_target':{'fields':['secondaryTargetType','secondaryTargetValueOne','secondaryTargetValueTwo','secondaryZoneNumber','secondaryTargetValueUnit'],'status':'serializer_confirmed; specific running pairs and watch capability not verified'},
 'advanced_unverified':['hr_percent','power_percent_ftp','walk_effort_instruction','audio_notes','power_curve_for_running','sport_subtype_variants'],
 'live_fixture':{'structure':'one run step','end':'time','seconds':1200,'target':'none','created_and_read_back':True,'watch_verified':False},
 'units':{'time':'seconds','distance':'meters','pace_range':'speed in meters/second; lower is slower','hr_custom':'bpm candidate corroborated by client library','cadence':'steps/min candidate; device convention requires validation','power_custom':'watts candidate','zones':'athlete-specific zone indices, not generic bpm/watts'},
 'metadata_counts':{k:len(v) for k,v in json.loads((d/'workout-types.json').read_text()).items()}}
(d/'capabilities.json').write_text(json.dumps(catalog,indent=2)+'\n')
# Illustrative coach-intent fixtures: no Garmin POSTs and no individualized prescriptions.
def step(role,seconds=None,meters=None,target=None):
 end={'kind':'lap'} if seconds is None and meters is None else ({'kind':'time','seconds':seconds} if seconds is not None else {'kind':'distance','meters':meters})
 return {'kind':'step','role':role,'end':end,'target':target or {'kind':'none'}}
def repeat(n,*children):return {'kind':'repeat','count':n,'steps':list(children)}
examples={
 'easy_time':[step('run',seconds=1200)],
 'distance_only':[step('run',meters=5000)],
 'hr_zone':[step('run',seconds=1200,target={'kind':'hr_zone','zone':2,'zone_source':'configured_athlete_running_zones'})],
 'pace_range':[step('run',seconds=600,target={'kind':'pace_range','slow_seconds_per_km':390,'fast_seconds_per_km':360})],
 'timed_intervals':[step('warmup',seconds=600),repeat(4,step('run',seconds=60),step('recovery',seconds=90)),step('cooldown',seconds=300)],
 'distance_intervals':[step('warmup'),repeat(4,step('run',meters=400),step('recovery',seconds=90)),step('cooldown')],
 'run_walk':[repeat(4,step('run',seconds=120),step('walk',seconds=60))],
 'progression':[step('run',seconds=600,target={'kind':'effort_text','cue':'easy'}),step('run',seconds=600,target={'kind':'effort_text','cue':'steady'})],
 'fartlek':[repeat(4,step('run',seconds=45),step('recovery',seconds=75))],
 'ladder':[step('run',meters=200),step('recovery',seconds=60),step('run',meters=400),step('recovery',seconds=90),step('run',meters=200)],
 'hill_repeats':[step('warmup'),repeat(4,step('run',seconds=30,target={'kind':'effort_text','cue':'uphill; choose a suitable real hill'}),step('recovery')),step('cooldown')],
 'nested_blocks':[repeat(2,repeat(3,step('run',seconds=30),step('recovery',seconds=60)),step('recovery',seconds=180))],
}
fixtures=[]
for name,ss in examples.items():fixtures.append({'name':name,'sport':'running','status':'illustrative_intent_only_not_personalized_not_uploaded','steps':ss})
(d/'coach-intent-examples.json').write_text(json.dumps(fixtures,indent=2)+'\n')
# A pace mapping example avoids a common boundary inversion error.
lo=1000/390;hi=1000/360
assert math.isclose(lo,2.5641025641025643) and lo<hi
(d/'pace-conversion-example.json').write_text(json.dumps({'display':'6:00-6:30 min/km','slow_seconds_per_km':390,'fast_seconds_per_km':360,'candidate_api_fields':{'targetType':{'workoutTargetTypeId':6},'targetValueOne':lo,'targetValueTwo':hi},'status':'conversion_checked; server_and_watch_not_tested'},indent=2)+'\n')
print('Generated',len(rows),'research matrix cells and',len(fixtures),'intent examples; no network writes.')
