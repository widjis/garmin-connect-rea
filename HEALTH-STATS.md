> Publication note: source/evidence references below identify local reproduction inputs, intentionally excluded from Git. Full verification requires those private local inputs; offline planning does not.

# Garmin Connect Android: health-stat retrieval methods

Static analysis, **20 October 2026**. Scope: the existing local `apk/base.apk`, Garmin Connect **5.30.1 (11657)**, package `com.garmin.android.apps.connectmobile`. No login, Garmin HTTP request, phone operation, health-record download, or workout write was performed. This is a version-specific native-client contract map, not a supported public API specification or medical interpretation.

## Authorized live follow-up

An earlier authorized existing-session test returned HTTP 200 JSON for one daily summary. No measurement values, account identifiers, record dates or response payloads are included in this publication. This verifies only that route for that test, not all catalog routes. See `health-stats/LIVE-TEST.md`.

## Result and evidence strength

- The app declares separate **GET** services for daily summary, steps, calorie history, floors, intensity minutes, resting/max HR history, sleep/stages/score, overnight HRV, Body Battery summaries/events, stress history, SpO2, respiration, weight/body composition, hydration, blood pressure, VO2/maxmet, fitness age and training readiness/status. Exact routes, parameters and return signatures: `health-stats/ENDPOINTS.md` and machine-readable `health-stats/manifest.json`.
- **63 GET declarations / 59 distinct exact route literals** in the inspected selection; **60 wire-model evidence entries**. These are catalog counts, not successful calls or a completeness claim for the whole APK. Duplicate declarations are retained to expose alternate consumers.
- Actual **REA `inspect_android_package`** succeeded on the full APK: evidence ID `ev_72dee8649034df826a44a7899a42c063a2cc790b1936adae8d52a7d983a79dd6`. Raw structured result: `health-stats/evidence/rea-package.json`. SHA-256: `5855bfffee6a1336ffefd6601b6f44e7c0dbff2554dd4b826e40747ee5107ffd`. Provider: JADX headless MCP 0.7.1, JDK 17.0.14. The default 2 GiB REA attempt failed with Java heap space; a fresh isolated MCP worker with an explicit 6 GiB heap succeeded. No global configuration was changed.
- Route/model tracing then used bounded **local JADX** extraction from four DEX members of that same APK, not REA per-method tools. Raw class identities are preserved in filenames; isolated-Dex Java package aliases can differ from full-APK aliases. `HealthExtract.java` is the extraction implementation; logs and selected sources remain under `health-stats/`. REA metadata verification does **not** independently validate every service method.
- **Known** means a literal annotation, wire-name annotation, serializer descriptor or method body in this artifact. **Inference** is called out below. **Untested** includes server acceptance, live host binding for each health service, authorization scopes, range limits, availability for this account/watch and all actual response values.

## How retrieval works

### 1. Use an authorized existing native-app session

Refer to `ANDROID-AUTH.md` for the previously documented native session/bootstrap method. This analysis deliberately does not read `.private`, token caches, credentials or historical personal health payloads. Do not copy tokens into these documents, shell history, a plan, source control or support logs. The health interfaces do not establish an OAuth scope list or prove that any existing credential is sufficient for every route. Account ownership/consent and backend authorization remain prerequisites.

The existing project's host finding is `https://connectapi.garmin.com/` (README, endpoint section). The PulseOx repository explicitly constructs its service with `ez0.c.GC`: `health-stats/sources/com.garmin.android.apps.connectmobile.pulseox.data.a.java:31–40`. Treat that as a GC-service binding, **not** a fresh verification of the production runtime hostname. Do not blindly prepend the web-client `/modern/proxy` prefix to these native paths. Interface annotations shown in the catalog contain no per-method Authorization header; interceptor/session injection must follow the existing auth research, not an invented header recipe.

### 2. Start with one calendar-day summary, not a giant history export

`UserSummaryRepo$getDailyUserSummaryAsync$2.invokeSuspend` calls its injected `b22.h.a(displayName, date)` (`health-stats/sources/b22.j.java:19–20,42–54`; construction in `b22.i.java:11–18`). The service is:

```text
GET /usersummary-service/usersummary/mobile/daily/{displayName}
query: calendarDate=<YYYY-MM-DD>
return: UserDailySummaryDTO
```

Exact contract: `health-stats/sources/b22.h.java:16–17`. `displayName` is a string path parameter, not interchangeable with numeric userProfilePK or device ID. Obtain it from the legitimate active profile/session, without inventing a profile-discovery endpoint.

This legacy/general summary has steps, distance, calories, floors, intensity minutes, resting/max HR and average stress. Its deserializer checks individual keys and uses different defaults (`UserDailySummaryDTO.java:196–308`). Do not treat zero, missing and `-1` as the same observation.

Two **different** summary contracts coexist:

- `GET mobile-gateway/usersummary/daily/{date}` → `jq1.c`, the steps feature's wrapper (`iq1.a.java:27–28`). `jq1.k`'s serializer names an inner `payload`; `jq1.b` identifies steps/calorie/distance fields (`jq1.k.java:33`, `jq1.b.java:46–55`). The outer wrapper wire key is not resolved here; do not assume this response is flat or identical to the legacy DTO.
- `GET /usersummary-service/v2/dailysummaries?startDate=...&endDate=...` → `b22.f` (`hr0.a.java:27–28`). Its serializer uses outer `data`; per-item `b22.g` includes `uuid`, `userProfilePk`, `calendarDate`, `source`, optional `intensityMinutes` and `movement` (`b22.f.java:48`, `b22.g.java:44–49`). This is **not** proof that V2 returns every legacy field.

All paths in this report are source literals. Do not “fix” leading slash differences in the evidence; a future HTTP client must deliberately resolve relative paths against its verified base URL.

### 3. Fetch feature detail only where needed

All entries below are **GET**; full argument types and range/weekly variants are in `health-stats/ENDPOINTS.md`. Source locations below refer to `health-stats/sources/`.

| Metric/detail | Exact primary route | Contract evidence / interpretation |
|---|---|---|
| Steps intraday | `wellness-service/wellness/dailySummaryChart` with query `date` | `iq1.a.java:18–19`; returns list `jq1.f`, not the daily total object |
| Steps daily total | `mobile-gateway/usersummary/daily/{date}` | `iq1.a.java:27–28`; distinct gateway wrapper |
| Calories | `/usersummary-service/stats/daily/{startDate}/{endDate}?statsType=CALORIES` | `my.a.java`; daily history, not live calorimetry |
| Floors intraday | `wellness-service/wellness/floorsChartData/daily/{calendarDate}` | `rh0.a.java`; separate daily range summaries also exist |
| Intensity minutes | `/wellness-service/wellness/daily/im/{date}` | `hr0.a.java:24–25`; also hourly and daily/weekly summary services |
| HR history | `usersummary-service/stats/heartRate/daily/{startDate}/{endDate}` | `do0.b.java:19–20`; returns list `co0.d`, not evidence of current/live HR |
| Sleep detail | `/sleep-service/sleep/dailySleepData` with queries `date`, `nonSleepBufferMinutes` | `im1.a.java:22–23`; returns `km1.c`, with sleep DTO, stages and overnight series |
| Overnight HRV | `hrv-service/hrv/{calendarDate}` | `v31.a.java:19–20`; returns `i41.b` summary + readings; range endpoint uses **fromDate/toDate**, not startDate/endDate |
| Body Battery | `/usersummary-service/stats/bodybattery/daily/{startDate}/{endDate}` | `ax.a.java:24–25`; daily low/high. Events: `wellness-service/wellness/bodyBattery/events/{calendarDate}`. MessagingToday is not a raw series endpoint |
| Stress daily history | `/usersummary-service/stats/stress/daily/{startDate}/{endDate}` | `nz1.a.java:22–23`; overnight series can additionally occur inside sleep response |
| SpO2 | `/wellness-service/wellness/daily/spo2acclimation/{date}` | `com.garmin.android.apps.connectmobile.pulseox.data.a.java:24–28`; summary, individual and hourly data in `dc1.a` |
| Respiration | `/wellness-service/wellness/daily/respiration/{date}` | `com.garmin.android.apps.connectmobile.respiration.data.d.java:20–25`; returns `be1.a`, with numeric sample arrays |
| Weight/body composition | `weight-service/weight/dayview/{date}` | `m42.a.java:27–28`; response `l42.a.dateWeightList` items `l42.c` extend `l42.j` body metrics |
| Latest weight | `weight-service/weight/latest` with queries `date`, `ignorePriority` | `m42.a.java:33–34`; do not omit or guess boolean semantics |
| Hydration | `/usersummary-service/usersummary/hydration/allData/{date}` | **GET** `ip0.a.java:26–27`; same literal also has **PUT**, which must never be used by a read-only extractor |
| Blood pressure | `bloodpressure-service/bloodpressure/dayview/{calendarDate}` | `lw.a.java:38–39`; `daily/last/{startDate}/{endDate}` returns list of `pw.a` measurements |
| VO2/maxmet | `/metrics-service/metrics/maxmet/latest/{startDate}` | `s32.a.java:21–22`; query **sport is List<String>**, generic/cycling/rowing variants in `o61.p` |
| Fitness age | `/fitnessage-service/fitnessage/v2/{calendarDate}` | `bx1.a.java:63–64`; return `yw1.k`; actual serializer wire names unresolved, so do not infer JSON names from obfuscated fields/toString |
| Training readiness | `metrics-service/metrics/trainingreadiness/{calendarDate}` | `nz1.a.java:28–29`; **list** of `oz1.b`, with deviceId, preferred tracker and timestamp fields; do not assume one item per day |
| Training status | `/mobile-gateway/usersummary/trainingstatus/latest/{startDate}` | `p61.a.java:30–31`; distinct weekly/monthly variants |

**Coverage gaps:** no source-backed full-day raw/current-HR endpoint, full-day raw stress endpoint or full-day raw Body Battery sample endpoint was established by this selected HTTP inventory. Do not import popular unofficial-library routes as if recovered from this APK. Sleep has overnight HR/stress/Body Battery series, but that does not make them full-day or live values. Fitness-age wire names, respiration serializer wire keys and several nested score/status schemas remain partly unresolved. GET interface presence does not establish feature availability or historical retention.

### 4. Decode wire fields, units and missingness conservatively

`health-stats/MODELS.md` catalogs exact annotations/descriptors with line numbers. It includes source-only fields, not vendor response examples.

| Model | Fields/structure established | Unit/null handling |
|---|---|---|
| `UserDailySummaryDTO.k` | `totalSteps`; `totalDistanceMeters`, `wellnessDistanceMeters`; calorie fields ending `Kilocalories`; `floorsAscended/Descended`; `moderateIntensityMinutes`, `vigorousIntensityMinutes`; `restingHeartRate`, `maxHeartRate`, `averageStressLevel` | meters, kcal, minutes and seconds are explicit in field names. Missing checks and `optInt` defaults differ by key; HR/stress/steps/floors use `-1` on relevant parse failures. Preserve raw missing/null/sentinel states rather than treating them as measurements. No current-HR field in this inspected deserializer. |
| `km1.c` sleep envelope | `dailySleepDTO` (`km1.v`), `sleepLevels`/`sleepMovement` lists (`km1.s`), `sleepHeartRate`, `sleepStress`, `sleepBodyBattery`, `hrvData` lists (`km1.z`), `restingHeartRate`, `hrvStatus`, `avgOvernightHrv` | `km1.z` has **object** fields `value` int, `startGMT` long; not a two-column array. `km1.s` has activityLevel and start/end GMT. Timestamp numeric unit needs conversion-chain verification, not a guess from magnitude. Many reference fields are optional/nullable. |
| `km1.v` sleep daily DTO | `calendarDate`, `sleepTimeSeconds`, `deepSleepSeconds`, `lightSleepSeconds`, `remSleepSeconds`, `awakeSleepSeconds`, `sleepStart/EndTimestampGMT/Local`, `sleepScores`, `deviceRemCapable`, `sleepFromDevice`, `sleepVersion` | durations explicitly seconds; retain original GMT vs Local timestamp distinction and capability flags. Nested score fields not fully mapped; no invented `overall.value` schema. |
| `i41.b`, `i41.f`, `i41.c` HRV | envelope `hrvSummary`, `hrvReadings`; summary `weeklyAvg`, `lastNightAvg`, `lastNight5MinHigh`, `baseline`, `status`; readings `hrvValue`, `readingTimeGMT/Local` | HRV unit not explicit in inspected annotations; expected milliseconds is a domain inference, not verified transport-unit evidence here. Preserve timestamps as provided. |
| `bx.f` → `bx.i` | calendarDate + values.lowBodyBattery/highBodyBattery; alternate JSON names `avgDailyLowBodyBattery`/`avgDailyHighBodyBattery` | nullable boxed Integer values. This is daily low/high, not instantaneous battery. Numeric bounds not established here. |
| `dc1.a` SpO2 | `averageSpO2`, `lowestSpO2`, `latestSpO2`, timestamps; `spO2SingleValues`, `spO2HourlyAverages`, sleep variants | numeric types and arrays are in source; percentage interpretation is a domain inference here, not annotation-specified unit. Do not substitute missing data with zero. |
| `be1.a` respiration | reference fields and `List<List<Double>>`/nested numeric lists | method `d()` consumes **two-element rows**, timestamp at index 0 cast to long, respiration at index 1 (`be1.a.java:174–205`). `b()` consumes four positions (`149–169`). Decompiled null-filter loop is suspicious; do not copy it as executable decoding code. Exact JSON keys and numeric timestamp units remain unverified. |
| `l42.a` → `l42.c` extends `l42.j` weight | `dateWeightList`; `calendarDate`, `date`, `samplePk`, `timestampGMT`, `weightDelta`; inherited `weight`, `bmi`, `bodyFat`, `bodyWater`, `boneMass`, `muscleMass`, `metabolicAge`, `physiqueRating`, `visceralFat`, `sourceType` | **weight/mass unit not proven by these DTOs**. Never assume kg or divide by 1000 without tracing actual unit conversion. `l42.i.value/unitKey` is the **write** DTO, not evidence that read responses use the same shape. |
| `jp0.b` hydration | `valueInML`, `goalInML`, `sweatLossInML`, `activityIntakeInML`, `baseGoalInML`, `hydrationMeasurementUnit`, `lastEntryTimestampLocal` | mL explicit in names; boxed Double values can be absent/null. Display unit does not change the explicit InML fields. |
| `pw.a` blood pressure | systolic, diastolic, pulse, version, sourceType, measurementTimestampLocal/GMT, notes, multiMeasurement, categoryName | boxed Double values; mmHg/BPM are domain expectations, not explicit unit annotations in this inspected DTO. Notes are sensitive. Avoid retaining them by default. |
| `oz1.b` readiness | score Float; calendarDate, deviceId Long, primaryActivityTracker Boolean, timestamp/timestampLocal, sleepScore, hrvWeeklyAverage, recoveryTime and factor feedback/percent fields | most fields boxed/reference types. Recovery-time unit and score range not proven. Keep per-device/time observations rather than arbitrarily taking first list entry. |

**Shape-only examples, not Garmin outputs:** sleep-series element `{ "value": <integer>, "startGMT": <long> }`; HRV reading `{ "hrvValue": <integer>, "readingTimeGMT": <string>, "readingTimeLocal": <string> }`; weight day response contains `dateWeightList: [<l42.c measurement objects>]`. These are schema sketches, intentionally not valid sample JSON or fabricated measurements.

### 5. Date, timezone and source-device handling

- `fz0.c.toString()` explicitly formats `yyyy-MM-dd` (`health-stats/sources/fz0.c.java:20–33`). It accepts a DateTime or calendar-date representation. `fz0.f` delegates to its wrapped date's `toString` (`fz0.f.java:17–18`), so that formatter's exact implementation was not independently inspected.
- Use a selected **account/calendar date**, not an implicit UTC date. GMT and Local fields coexist in HRV, sleep, weight, SpO2 and readiness DTOs. A local timestamp without offset must not be silently interpreted in the extraction machine's timezone. The exact travel/timezone-boundary rules and sleep day attribution are untested.
- Inference: cloud fetches can only expose what is already available to that cloud/account. Nothing here proves a forced watch sync/upload or guarantees freshness. The mapped Retrofit GET paths are server retrieval operations, not Connect IQ/wearable-local APIs or a BLE health-data readout. No watch-upload implementation was traced in this task.
- Preserve deviceId, source/version, timestamp and capability flags where available. Multi-device readiness and multiple daily weight/BP samples are not automatically duplicates.

## Minimal future read-only extraction sequence

This is an **unexecuted plan**, requiring separate authorization to access personal records:

1. Reuse a valid authorized session by the existing auth method. Confirm native base host/session binding without logging credentials. Do not bypass fresh-login restrictions or guess OAuth scopes.
2. Select one explicit calendar date and legitimate displayName. Read the general daily summary once.
3. Request only needed feature detail for that same date: sleep, HRV, hydration, SpO2, respiration, weight day view and BP day view; add readiness/status/maxmet only as needed. There is no requirement to fetch every metric.
4. For trends, use the explicit daily/range endpoints. The inspected interfaces provide no verified maximum range, pagination policy, rate limit, retention or inclusive/exclusive boundary contract. Start with a narrow day/range, not an unbounded export; preserve errors rather than pretending empty means healthy/zero.
5. Decode each service's actual wrapper and schema separately. Preserve missing/null/sentinel states; do not normalize units whose conversion is unresolved. Record source date, collection timestamp, device and contract version without copying identities into public reports.
6. Future implementation policy (not observed server behavior): GET-only allowlist, no body writes, conservative serialized requests, bounded retries with server guidance, stop on authorization/rate-limit errors, no automatic login loop. Status 401/403/429 meanings/handling should be confirmed for the actual endpoint before implementation claims.
7. Keep health payloads encrypted/private, outside source control and sharing bundles; minimize fields and retention. Sanitized documentation/evidence may be shared; APK and vendor decompilation have separate redistribution considerations.

The offline planner is deliberately incapable of making HTTP requests:

```sh
python3 health-stats/plan.py --plan
python3 health-stats/build_catalog.py
python3 health-stats/verify.py
```

Planner output uses placeholders, contains GET templates only and excludes the malformed weekly blood-pressure literal. It is not an authenticated client, a date-expander or a claim that the backend accepts these requests.

## Literal pitfall: do not repair a malformed route

`health-stats/sources/lw.a.java:26` literally contains `bloodpressure-service/bloodpressure/weeklyRange/{startDate}\u200b/{endDate}` (zero-width-space escape after the startDate placeholder). The existing DEX annotation inventory agrees. The catalog preserves this suspicious literal and flags it; the planner excludes it. Do not silently remove that character and advertise a corrected route as source-proven. The normal `range` and `dayview` routes are separate declarations.

## Reproduction and residual unknowns

- `health-stats/rea_probe.py`: isolated REA MCP package inspection, explicit existing engine/JDK paths, no config/token reads.
- `health-stats/HealthExtract.java`: local selected-class extraction, skip resources, one worker. The four derived DEX files were taken from the verified base APK; logs identify each extraction batch. No additional provider installation or full source export was needed.
- `health-stats/build_catalog.py`: reproducible source-to-catalog generation; `manifest.json` retains hash/version/REA ID, exact GET literals, signature/argument annotations and wire-field source lines.
- `health-stats/MODELS.md`: field evidence, **not** required-field or server response validation. Some descriptor-bearing classes contain additional unrelated fields because whole selected DTO classes were preserved.
- Known limitations: obfuscation, isolated-Dex aliasing, decompiler warnings and unresolved serializer indirections. Metadata/source evidence is not live API stability, server validation, account entitlement, watch support, clinical validity or end-to-end sync proof.
- The original analysis workspace is not this sanitized publication. APK, source files, raw evidence and private artifacts remain local; see `PUBLICATION.md` for verification boundaries.
