# Sanitized publication checkpoint

Prepared for the explicitly requested private GitHub repository `widjis/garmin-connect-rea`. A separate clean repository is used; the original analysis workspace and its unrelated parent Git repository are not initialized, staged, modified or published.

## Included

Authored reports and selected contract/model excerpts; exact health route/model manifest; source references and APK hash for provenance; offline planner and separate offline-only verifier; extraction scripts; running metadata enum snapshot and reproducible candidate matrix/intent examples; sanitized historical transport outcomes. No blanket redistribution license for Garmin material is asserted.

`publication-manifest.json` is the reviewed file allowlist with SHA-256/byte counts (excluding itself). `tools/publication_check.py` checks that allowlist, content hashes, forbidden paths/extensions and common secret patterns. The manifest is a review checkpoint, not a signature or an exhaustive privacy guarantee. Future additions require deliberate review and a new checkpoint.

## Excluded

- All `.private/` contents, sessions, cookies, credentials, tokens, portal snapshots and authentication exchanges.
- Personal health values, activity/calendar dates and records, sensor series, laps, zones, GPS, owner/profile/device IDs, workout IDs/names and personalized activity reports.
- APK/DEX/JAR binaries, environments and installed dependencies.
- Bulk proprietary decompiled `sources/`, `auth-sources/`, nested source trees, raw REA results and extraction/network logs.
- Account-specific activity/strength/calendar scripts that embed real records, personal interpretation or an unavailable local adapter. These are not disguised as synthetic examples or published in a broken state.
- Unrelated sibling skills and files from the original parent repository.

Static schema identifiers such as `userId`, `deviceId` and `displayName` remain in contract documentation; these are field names/placeholders, not account values. Public native client identifiers and the app's Play Integrity project number describe protocol configuration, not personal credentials. Historical transport outcomes do not include measurement values or field-availability reports.

## Verification actually exercised before publication

1. The original `health-stats/verify.py` was run in an isolated scratch directory with read-only symlinks to the original APK/extracted sources and a copied REA package result. It returned **PASS**: APK fingerprint; REA package/version; every GET literal/signature/source line; every model field source line; route/model counts; deduplicated planner; synthetic mutation/malformed-route exclusions; planner CLI. Its output was written only to scratch, not the original workspace. Counts: 63 GET declarations, 59 distinct literals, 60 model entries, 58 planned templates; zero live requests.
2. `python3 health-stats/verify_offline.py` passed on the sanitized publication. It verifies catalog consistency, planner CLI and synthetic negative cases only—not absent APK/source/REA evidence.
3. `python3 tools/build_running_catalog.py` ran offline and generated 245 candidate cells and 12 illustrative intents, without network calls. The illustrative dose/pace constants are examples, not observed personal measurements or prescriptions.
4. All published Python scripts passed compile checks without executing live helper bodies.
5. Publication allowlist/hash/secret-pattern checks and staged diff review are required before commit. No independent reviewer tool is available in this focused one-shot publication task; manual review is not represented as independent approval.

Full `verify.py` and `build_catalog.py` require the deliberately omitted local inputs. A clean clone can run the offline verifier but cannot reproduce full source integrity until those separately authorized inputs are obtained. No live Garmin calls, dependency installation, Java extraction or watch/device validation were performed for this publication. No CI result is implied.

## Runtime safety

Historical create helpers require separately authorized interactive use; executing a script is not a harmless test discovery operation. Their state/readback artifacts now go beneath ignored `.private/`; raw historical artifact files were not copied. The daily-summary probe requires `--authorize-read`; it is GET-only and has no automatic login/refresh. Its previous-day selection is machine-local, not a confirmed account timezone.

Before any future local extraction, create output directories (for example `mkdir -p evidence health-stats/evidence health-stats/sources`). DEX inventory helpers read `apk/base.apk`. Java helpers accept local input/output/class-selection arguments and require a separately supplied compatible JADX classpath. The REA probe requires `JAVA_HOME`, `REA_JADX_MCP_JAR`, `REA_ENTRYPOINT` and optionally `REA_NODE`; Python `mcp` is an additional optional dependency, not needed for offline catalog checks.

After push, read back `refs/heads/main` via `git ls-remote` and compare it with local HEAD, then read GitHub repository privacy/default branch. Those remote results are reported in the completion response rather than writing a self-referential commit hash into this file.
