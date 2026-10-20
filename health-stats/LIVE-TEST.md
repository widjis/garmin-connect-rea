# Historical daily-summary test (sanitized)

An earlier separately authorized existing-session test performed a self-profile GET and one daily-summary GET against `https://connectapi.garmin.com`. Both returned HTTP 200 JSON; the summary was an object and its calendar date matched the request. No login, refresh, mutation, schedule, device operation or forced watch sync occurred. The session file was checked unchanged.

Published contract templates:

```text
GET /userprofile-service/socialProfile/v2
GET /usersummary-service/usersummary/mobile/daily/{displayName}?calendarDate=<YYYY-MM-DD>
```

No account identifiers, record dates, field missingness/availability, metric values, payloads or session digests are bundled. This historical outcome verifies only that route for that test, not every static catalog entry, current server acceptance, units, sensor validity or watch freshness.

`live_daily_test.py --authorize-read` is an opt-in existing-session probe, not an offline regression test. It requires separate authorization and stores runtime schema metadata only beneath ignored `.private/`. No live probe was executed during publication.
