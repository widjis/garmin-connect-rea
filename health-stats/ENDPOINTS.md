# Static GET route catalog

63 declarations; 59 distinct exact route literals. No live requests. Source locations are relative to the Garmin folder. `s` = path, `t` = query; annotation `f` = Retrofit GET. Return wrappers and aliases are kept verbatim; this is not a complete OpenAPI schema.

| GET route literal | Raw class.method | Parameters (s=path, t=query) | Evidence |
|---|---|---|---|
| `wellness-service/wellness/bodyBattery/messagingToday` | `ax.a.a` |  | `health-stats/sources/ax.a.java:18` |
| `wellness-service/wellness/bodyBattery/events/{calendarDate}` | `ax.a.b` | `s:calendarDate` | `health-stats/sources/ax.a.java:21` |
| `/usersummary-service/stats/bodybattery/daily/{startDate}/{endDate}` | `ax.a.c` | `s:startDate`, `s:endDate` | `health-stats/sources/ax.a.java:24` |
| `/usersummary-service/usersummary/mobile/daily/{displayName}` | `b22.h.a` | `s:displayName`, `t:calendarDate` | `health-stats/sources/b22.h.java:16` |
| `/metrics-service/metrics/maxmet/latest/hbase/{date}` | `bx1.a.e` | `s:date`, `t:sport` | `health-stats/sources/bx1.a.java:36` |
| `/fitnessage-service/fitnessage/v2/{calendarDate}` | `bx1.a.n` | `s:calendarDate` | `health-stats/sources/bx1.a.java:63` |
| `/wellness-service/wellness/daily/spo2acclimation/{date}` | `com.garmin.android.apps.connectmobile.pulseox.data.a.a` | `s:date` | `health-stats/sources/com.garmin.android.apps.connectmobile.pulseox.data.a.java:24` |
| `/wellness-service/stats/daily/acclimation?` | `com.garmin.android.apps.connectmobile.pulseox.data.a.b` | `t:fromDate`, `t:untilDate` | `health-stats/sources/com.garmin.android.apps.connectmobile.pulseox.data.a.java:27` |
| `/wellness-service/wellness/daily/respiration/{date}` | `com.garmin.android.apps.connectmobile.respiration.data.d.a` | `s:date` | `health-stats/sources/com.garmin.android.apps.connectmobile.respiration.data.d.java:21` |
| `/usersummary-service/stats/respiration/daily/{startDate}/{endDate}` | `com.garmin.android.apps.connectmobile.respiration.data.d.b` | `s:startDate`, `s:endDate` | `health-stats/sources/com.garmin.android.apps.connectmobile.respiration.data.d.java:24` |
| `usersummary-service/stats/heartRate/weekly/{endDate}/{numWeeks}` | `do0.b.a` | `s:endDate`, `s:numWeeks` | `health-stats/sources/do0.b.java:16` |
| `usersummary-service/stats/heartRate/daily/{startDate}/{endDate}` | `do0.b.b` | `s:startDate`, `s:endDate` | `health-stats/sources/do0.b.java:19` |
| `/mobile-gateway/snapshot/timeline/v2/forDate/{date}` | `hr0.a.a` | `s:date` | `health-stats/sources/hr0.a.java:15` |
| `/usersummary-service/stats/im/weekly/{startDate}/{endDate}` | `hr0.a.b` | `s:startDate`, `s:endDate` | `health-stats/sources/hr0.a.java:18` |
| `/wellness-service/stats/hourly/im/{endDate}/{days}` | `hr0.a.c` | `s:endDate`, `s:days` | `health-stats/sources/hr0.a.java:21` |
| `/wellness-service/wellness/daily/im/{date}` | `hr0.a.d` | `s:date` | `health-stats/sources/hr0.a.java:24` |
| `/usersummary-service/v2/dailysummaries` | `hr0.a.e` | `t:startDate`, `t:endDate` | `health-stats/sources/hr0.a.java:27` |
| `/usersummary-service/stats/im/daily/{startDate}/{endDate}` | `hr0.a.f` | `s:startDate`, `s:endDate` | `health-stats/sources/hr0.a.java:30` |
| `/sleep-service/sleep/dailySleepData` | `im1.a.c` | `t:date`, `t:nonSleepBufferMinutes` | `health-stats/sources/im1.a.java:22` |
| `/sleep-service/stats/sleep/daily/{startDate}/{endDate}` | `im1.a.e` | `s:startDate`, `s:endDate` | `health-stats/sources/im1.a.java:25` |
| `/sleep-service/stats/sleep/weekly/{endDate}/{weekCount}` | `im1.a.m` | `s:endDate`, `s:weekCount` | `health-stats/sources/im1.a.java:51` |
| `usersummary-service/stats/hydration/daily/{startDate}/{endDate}` | `ip0.a.c` | `s:startDate`, `s:endDate` | `health-stats/sources/ip0.a.java:23` |
| `/usersummary-service/usersummary/hydration/allData/{date}` | `ip0.a.d` | `s:date` | `health-stats/sources/ip0.a.java:26` |
| `usersummary-service/stats/hydration/weekly/{endDate}/{numOfWeeks}` | `ip0.a.e` | `s:endDate`, `s:numOfWeeks` | `health-stats/sources/ip0.a.java:29` |
| `wellness-service/wellness/dailySummaryChart` | `iq1.a.a` | `t:date` | `health-stats/sources/iq1.a.java:18` |
| `/usersummary-service/stats/daily/{startDate}/{endDate}?statsType=STEPS` | `iq1.a.b` | `s:startDate`, `s:endDate`, `t:currentDate` | `health-stats/sources/iq1.a.java:21` |
| `/usersummary-service/stats/steps/monthly/{startDate}/{numOfMonths}` | `iq1.a.c` | `s:startDate`, `s:numOfMonths` | `health-stats/sources/iq1.a.java:24` |
| `mobile-gateway/usersummary/daily/{date}` | `iq1.a.d` | `s:date` | `health-stats/sources/iq1.a.java:27` |
| `/usersummary-service/stats/steps/weekly/{endDate}/{numOfWeeks}` | `iq1.a.e` | `s:endDate`, `s:numOfWeeks` | `health-stats/sources/iq1.a.java:30` |
| `/usersummary-service/stats/stress/daily/{startDate}/{endDate}` | `jr1.a.b` | `s:startDate`, `s:endDate` | `health-stats/sources/jr1.a.java:16` |
| `/usersummary-service/stats/stress/weekly/{endDate}/{numOfWeeks}` | `jr1.a.c` | `s:endDate`, `s:numOfWeeks` | `health-stats/sources/jr1.a.java:19` |
| `bloodpressure-service/bloodpressure/category/level` | `lw.a.a` |  | `health-stats/sources/lw.a.java:23` |
| `bloodpressure-service/bloodpressure/weeklyRange/{startDate}\u200b/{endDate}` | `lw.a.b` | `s:startDate`, `s:endDate` | `health-stats/sources/lw.a.java:26` |
| `bloodpressure-service/bloodpressure/dayview/{calendarDate}` | `lw.a.f` | `s:calendarDate` | `health-stats/sources/lw.a.java:38` |
| `bloodpressure-service/bloodpressure/range/{startDate}/{endDate}` | `lw.a.g` | `s:startDate`, `s:endDate` | `health-stats/sources/lw.a.java:41` |
| `bloodpressure-service/bloodpressure/daily/last/{startDate}/{endDate}` | `lw.a.h` | `s:startDate`, `s:endDate` | `health-stats/sources/lw.a.java:44` |
| `weight-service/weight/dayview/{date}` | `m42.a.b` | `s:date` | `health-stats/sources/m42.a.java:27` |
| `weight-service/weight/weeklyRange/{startDate}/{endDate}` | `m42.a.c` | `s:startDate`, `s:endDate` | `health-stats/sources/m42.a.java:30` |
| `weight-service/weight/latest` | `m42.a.d` | `t:date`, `t:ignorePriority` | `health-stats/sources/m42.a.java:33` |
| `weight-service/weight/range/{startDate}/{endDate}` | `m42.a.f` | `s:startDate`, `s:endDate` | `health-stats/sources/m42.a.java:39` |
| `weight-service/weight/checkAllRecentWeightsFromIndexS1/{calendarDate}` | `m42.a.h` | `s:calendarDate` | `health-stats/sources/m42.a.java:45` |
| `weight-service/weight/checkWeightHistory` | `m42.a.i` | `t:minWeight`, `t:maxWeight`, `t:startDate`, `t:endDate`, `t:hasBodyMetrics` | `health-stats/sources/m42.a.java:48` |
| `/usersummary-service/stats/daily/{startDate}/{endDate}?statsType=CALORIES` | `my.a.a` | `s:startDate`, `s:endDate`, `t:currentDate` | `health-stats/sources/my.a.java:19` |
| `/usersummary-service/stats/calories/weekly/{endDate}/{numWeeks}` | `my.a.b` | `s:endDate`, `s:numWeeks` | `health-stats/sources/my.a.java:22` |
| `/activitylist-service/activities/list/{displayName}` | `nz1.a.a` | `s:displayName`, `t:activityTypeId`, `t:startTimestampLocal`, `t:endTimestampLocal` | `health-stats/sources/nz1.a.java:19` |
| `/usersummary-service/stats/stress/daily/{startDate}/{endDate}` | `nz1.a.b` | `s:startDate`, `s:endDate` | `health-stats/sources/nz1.a.java:22` |
| `/sleep-service/sleep/dailySleepData` | `nz1.a.c` | `t:date`, `t:nonSleepBufferMinutes` | `health-stats/sources/nz1.a.java:25` |
| `metrics-service/metrics/trainingreadiness/{calendarDate}` | `nz1.a.d` | `s:calendarDate` | `health-stats/sources/nz1.a.java:28` |
| `/sleep-service/stats/sleep/daily/{startDate}/{endDate}` | `nz1.a.e` | `s:startDate`, `s:endDate` | `health-stats/sources/nz1.a.java:31` |
| `hrv-service/hrv/{calendarDate}` | `nz1.a.f` | `s:calendarDate` | `health-stats/sources/nz1.a.java:34` |
| `/mobile-gateway/usersummary/trainingstatus/weekly/{startDate}/{endDate}` | `p61.a.a` | `s:startDate`, `s:endDate` | `health-stats/sources/p61.a.java:18` |
| `/metrics-service/metrics/manualstresslevel/daily/{startDate}/{endDate}` | `p61.a.b` | `s:startDate`, `s:endDate` | `health-stats/sources/p61.a.java:21` |
| `/metrics-service/metrics/heataltitudeacclimation/daily/{startDate}/{endDate}` | `p61.a.c` | `s:startDate`, `s:endDate` | `health-stats/sources/p61.a.java:24` |
| `/mobile-gateway/usersummary/trainingstatus/monthly/{startDate}/{endDate}` | `p61.a.d` | `s:startDate`, `s:endDate` | `health-stats/sources/p61.a.java:27` |
| `/mobile-gateway/usersummary/trainingstatus/latest/{startDate}` | `p61.a.e` | `s:startDate` | `health-stats/sources/p61.a.java:30` |
| `/usersummary-service/stats/floors/daily/{startDate}/{endDate}` | `rh0.a.a` | `s:startDate`, `s:endDate` | `health-stats/sources/rh0.a.java:15` |
| `wellness-service/wellness/floorsChartData/daily/{calendarDate}` | `rh0.a.b` | `s:calendarDate` | `health-stats/sources/rh0.a.java:18` |
| `/usersummary-service/stats/floors/weekly/{endDate}/{numOfWeeks}` | `rh0.a.c` | `s:endDate`, `s:numOfWeeks` | `health-stats/sources/rh0.a.java:21` |
| `/metrics-service/metrics/maxmet/weekly/{startDate}/{endDate}` | `s32.a.a` | `s:startDate`, `s:endDate`, `t:sport` | `health-stats/sources/s32.a.java:18` |
| `/metrics-service/metrics/maxmet/latest/{startDate}` | `s32.a.b` | `s:startDate`, `t:sport` | `health-stats/sources/s32.a.java:21` |
| `/metrics-service/metrics/maxmet/daily/{startDate}/{endDate}` | `s32.a.c` | `s:startDate`, `s:endDate`, `t:sport` | `health-stats/sources/s32.a.java:24` |
| `hrv-service/hrv/daily/{fromDate}/{toDate}` | `v31.a.a` | `s:fromDate`, `s:toDate` | `health-stats/sources/v31.a.java:16` |
| `hrv-service/hrv/{calendarDate}` | `v31.a.d` | `s:calendarDate` | `health-stats/sources/v31.a.java:19` |

## Return contracts

- `ax.a.a`: `i0<a0<e>> a();`
- `ax.a.b`: `i0<a0<List<b>>> b(@s("calendarDate") c calendarDate);`
- `ax.a.c`: `i0<a0<List<bx.f>>> c(@s("startDate") c startDate, @s("endDate") c endDate);`
- `b22.h.a`: `i0<a0<UserDailySummaryDTO>> a(@s("displayName") String displayName, @t("calendarDate") String date);`
- `bx1.a.e`: `i0<a0<j>> e(@i83.s("date") c date, @t("sport") String sport);`
- `bx1.a.n`: `i0<a0<k>> n(@i83.s("calendarDate") String calendarDate);`
- `com.garmin.android.apps.connectmobile.pulseox.data.a.a`: `i0<dc1.a> a(@s("date") c date);`
- `com.garmin.android.apps.connectmobile.pulseox.data.a.b`: `i0<nl.a> b(@t("fromDate") c startDate, @t("untilDate") c endDate);`
- `com.garmin.android.apps.connectmobile.respiration.data.d.a`: `i0<a0<be1.a>> a(@s("date") fz0.f date);`
- `com.garmin.android.apps.connectmobile.respiration.data.d.b`: `i0<a0<List<be1.b>>> b(@s("startDate") fz0.f startDate, @s("endDate") fz0.f endDate);`
- `do0.b.a`: `i0<a0<List<d>>> a(@s("endDate") c endDate, @s("numWeeks") int numWeeks);`
- `do0.b.b`: `i0<a0<List<d>>> b(@s("startDate") c startDate, @s("endDate") c endDate);`
- `hr0.a.a`: `i0<a0<String>> a(@s("date") c date);`
- `hr0.a.b`: `i0<a0<List<ir0.f>>> b(@s("startDate") c startDate, @s("endDate") c endDate);`
- `hr0.a.c`: `i0<a0<ir0.c>> c(@s("endDate") c date, @s("days") int days);`
- `hr0.a.d`: `i0<a0<ir0.a>> d(@s("date") c date);`
- `hr0.a.e`: `i0<a0<b22.f>> e(@t("startDate") String startDate, @t("endDate") String endDate);`
- `hr0.a.f`: `i0<a0<List<ir0.f>>> f(@s("startDate") c startDate, @s("endDate") c endDate);`
- `im1.a.c`: `i0<a0<c>> c(@t("date") fz0.c date, @t("nonSleepBufferMinutes") int nonSleepBufferMinutes);`
- `im1.a.e`: `i0<a0<b>> e(@s("startDate") fz0.c startDate, @s("endDate") fz0.c endDate);`
- `im1.a.m`: `i0<a0<mm1.f>> m(@s("endDate") fz0.c endDate, @s("weekCount") int weekCount);`
- `ip0.a.c`: `i0<a0<List<jp0.a>>> c(@s("startDate") String startDate, @s("endDate") String endDate);`
- `ip0.a.d`: `i0<a0<b>> d(@s("date") c date);`
- `ip0.a.e`: `i0<a0<List<jp0.f>>> e(@s("endDate") String endDate, @s("numOfWeeks") int numOfWeeks);`
- `iq1.a.a`: `i0<a0<List<jq1.f>>> a(@t("date") c date);`
- `iq1.a.b`: `i0<a0<jq1.a>> b(@s("startDate") c startDate, @s("endDate") c endDate, @t("currentDate") c currentDate);`
- `iq1.a.c`: `i0<a0<List<j>>> c(@s("startDate") c startDate, @s("numOfMonths") int numOfMonths);`
- `iq1.a.d`: `i0<a0<jq1.c>> d(@s("date") c date);`
- `iq1.a.e`: `i0<a0<List<j>>> e(@s("endDate") c endDate, @s("numOfWeeks") int numOfWeeks);`
- `jr1.a.b`: `i0<a0<List<kr1.a>>> b(@s("startDate") c startDate, @s("endDate") c endDate);`
- `jr1.a.c`: `i0<a0<List<kr1.c>>> c(@s("endDate") c endDate, @s("numOfWeeks") int numOfWeeks);`
- `lw.a.a`: `d<String> a();`
- `lw.a.b`: `i0<h> b(@s("startDate") c startDate, @s("endDate") c endDate);`
- `lw.a.f`: `i0<kw.o> f(@s("calendarDate") c calendarDate);`
- `lw.a.g`: `i0<h> g(@s("startDate") c startDate, @s("endDate") c endDate);`
- `lw.a.h`: `i0<a0<List<pw.a>>> h(@s("startDate") c startDate, @s("endDate") c endDate);`
- `m42.a.b`: `i0<a0<l42.a>> b(@s("date") c date);`
- `m42.a.c`: `i0<a0<e>> c(@s("startDate") c startDate, @s("endDate") c endDate);`
- `m42.a.d`: `i0<a0<h>> d(@t("date") c date, @t("ignorePriority") boolean ignorePriority);`
- `m42.a.f`: `i0<a0<k>> f(@s("startDate") c startDate, @s("endDate") c endDate);`
- `m42.a.h`: `Object h(@s("calendarDate") c cVar, d<? super a0<Boolean>> dVar);`
- `m42.a.i`: `Object i(@t("minWeight") Integer num, @t("maxWeight") Integer num2, @t("startDate") String str, @t("endDate") String str2, @t("hasBodyMetrics") Boolean bool, d<? super a0<Boolean>> dVar);`
- `my.a.a`: `Object a(@s("startDate") c cVar, @s("endDate") c cVar2, @t("currentDate") c cVar3, d<? super a0<b>> dVar);`
- `my.a.b`: `Object b(@s("endDate") c cVar, @s("numWeeks") int i, d<? super a0<List<e>>> dVar);`
- `nz1.a.a`: `Object a(@s("displayName") String str, @t("activityTypeId") String str2, @t("startTimestampLocal") String str3, @t("endTimestampLocal") String str4, d<? super a0<c>> dVar);`
- `nz1.a.b`: `i0<a0<List<kr1.a>>> b(@s("startDate") fz0.c startDate, @s("endDate") fz0.c endDate);`
- `nz1.a.c`: `i0<a0<km1.c>> c(@t("date") fz0.c date, @t("nonSleepBufferMinutes") int nonSleepBufferMinutes);`
- `nz1.a.d`: `i0<a0<List<b>>> d(@s("calendarDate") fz0.c date);`
- `nz1.a.e`: `i0<a0<mm1.b>> e(@s("startDate") fz0.c startDate, @s("endDate") fz0.c endDate);`
- `nz1.a.f`: `i0<a0<i41.b>> f(@s("calendarDate") fz0.c date);`
- `p61.a.a`: `i0<a0<TrainingStatusReportDTO>> a(@s("startDate") String startDate, @s("endDate") String endDate);`
- `p61.a.b`: `i0<a0<StressScoresSummaryDTO>> b(@s("startDate") String startDate, @s("endDate") String endDate);`
- `p61.a.c`: `i0<a0<List<e>>> c(@s("startDate") String startDate, @s("endDate") String endDate);`
- `p61.a.d`: `i0<a0<TrainingStatusReportDTO>> d(@s("startDate") String startDate, @s("endDate") String endDate);`
- `p61.a.e`: `i0<a0<CurrentTrainingStatusDTO>> e(@s("startDate") String startDate);`
- `rh0.a.a`: `i0<a0<List<b>>> a(@s("startDate") c startDate, @s("endDate") c endDate);`
- `rh0.a.b`: `i0<a0<sh0.c>> b(@s("calendarDate") c date);`
- `rh0.a.c`: `i0<a0<List<sh0.f>>> c(@s("endDate") c endDate, @s("numOfWeeks") int numOfWeeks);`
- `s32.a.a`: `Object a(@s("startDate") c cVar, @s("endDate") c cVar2, @t("sport") List<String> list, d<? super a0<List<p>>> dVar);`
- `s32.a.b`: `Object b(@s("startDate") c cVar, @t("sport") List<String> list, d<? super a0<p>> dVar);`
- `s32.a.c`: `Object c(@s("startDate") c cVar, @s("endDate") c cVar2, @t("sport") List<String> list, d<? super a0<List<p>>> dVar);`
- `v31.a.a`: `i0<a0<e>> a(@s("fromDate") c fromDate, @s("toDate") c toDate);`
- `v31.a.d`: `i0<a0<b>> d(@s("calendarDate") c date);`
