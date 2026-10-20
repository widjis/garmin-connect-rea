# Garmin Connect REA research

Sanitized, version-specific research into Garmin Connect Android **5.30.1 (11657)**, package `com.garmin.android.apps.connectmobile`. This repository contains authored research, selected interface/model contract excerpts, offline catalogs/planners and research tooling—not Garmin's application or bulk decompiled source.

## Contents

- `HEALTH-STATS.md`: native health-summary/detail retrieval contracts, units/null/timezone caveats and evidence boundaries.
- `health-stats/ENDPOINTS.md`, `MODELS.md`, `manifest.json`: 63 GET declarations, 59 distinct route literals and 60 model entries from the inspected selection. These are static inventory counts, not successful-call counts.
- `ANDROID-AUTH.md`, `LIVE-TEST.md`: portal/grant research and sanitized historical test outcomes; no sessions or account artifacts.
- `running/`: running capabilities, candidate matrix and illustrative CoachIntent structures—not personalized prescriptions or blanket server/device compatibility.
- `strength/STRENGTH-CAPABILITIES.md`, `calendar/CALENDAR-SCHEDULING.md`: contract notes with personal examples removed.
- `tools/`: selected extraction and interactive reproduction scripts. Live scripts are not a test suite and must not be batch-executed.
- `activity-analysis/README.md`: privacy boundary for activity analysis; no activity records are bundled.

## Offline checks (Python 3.10+; standard library)

```sh
python3 health-stats/plan.py --plan
python3 health-stats/verify_offline.py
python3 tools/build_running_catalog.py
python3 tools/publication_check.py
```

The offline plan prints placeholder GET templates only. The malformed weekly blood-pressure literal is preserved in the manifest and excluded from the plan. No token, login or network access is needed.

## Full local evidence reproduction

`health-stats/verify.py` deliberately requires the exact APK, extracted source lines and REA package evidence. Those inputs are **not bundled**; it must not be described as passing on a clean clone. Obtain your own authorized local input at `apk/base.apk`, run the extraction tooling, and restore local `health-stats/sources/` and `health-stats/evidence/rea-package.json` before running it. See `PUBLICATION.md`. `build_catalog.py` likewise requires local source/evidence inputs; do not run it against an empty extraction directory.

JADX Java helpers require a separately supplied compatible JADX JAR and JDK. `health-stats/rea_probe.py` requires environment-provided engine/JDK/JAR paths and the Python `mcp` package. None is redistributed here.

## Live tooling: explicit authorization required

Publication does **not** authorize accessing Garmin or creating workouts. Never run every `.py` file as a test: several historical helpers authenticate/create at execution time. `tools/android_portal_create.py` uses the official browser portal and creates a single test workout; `tools/live_create.py` uses a separate Python-library SSO flow. Their runtime outputs and sessions are now under ignored `.private/`. They do not schedule/send to a watch.

The GET-only daily-summary probe requires `python3 health-stats/live_daily_test.py --authorize-read`, an existing authorized `.private/android-token.json` and renewed consent for profile/health reads. It uses the **machine-local** previous calendar date, not a proven account timezone. No automatic login/refresh occurs. Never provide passwords/tokens through chat. The live requirements files preserve the original workspace's recorded dependency snapshot; installation and fresh live compatibility were not tested for this publication. Do not interpret the pinned snapshot as a current dependency recommendation.

## Boundaries

API acceptance ≠ valid FIT ≠ watch receipt ≠ completed activity. No device delivery was verified by this publication. This is unsupported research, not a public API guarantee, clinical interpretation or medical advice. Garmin names, formats and extracted contract material remain subject to their respective owners' rights; no blanket license over vendor material is granted.

All private sessions, personal health/activity/calendar payloads, APK/DEX/JAR binaries, bulk source and raw evidence are excluded even though the destination repository is private. Original local research remains untouched. See `PUBLICATION.md` for the publication checkpoint and exclusions.
