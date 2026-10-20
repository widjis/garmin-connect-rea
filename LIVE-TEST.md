# Historical live-test status (sanitized)

Earlier authorized local research exercised two different authentication paths. A Python-library mobile SSO attempt stopped on a rate-limit error before create. A separate official Android portal → service-ticket → DI token flow succeeded, followed by authenticated read, one test workout create and GET semantic readback. These are historical outcomes, not a fresh publication-time live test or a guarantee of current server behavior.

No session, token, credential, personal identifier, workout ID/name or raw response artifact is included. Detailed local evidence is intentionally withheld. Read `ANDROID-AUTH.md` for the static/native versus desktop-browser reproduction limitations.

The publication operation runs offline checks only. It does not log in to Garmin, refresh tokens, read personal records, create/update/delete workouts, schedule workouts, queue device messages or force watch sync.
