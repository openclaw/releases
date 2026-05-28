# OpenClaw Release Evidence: f9a106fb28674b00b5c09fe793448f3f939fbbe0

Generated: 2026-05-10T07:15:15.673Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `f9a106fb28674b00b5c09fe793448f3f939fbbe0` |
| Release ref input | `f9a106fb28674b00b5c09fe793448f3f939fbbe0` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `f9a106fb28674b00b5c09fe793448f3f939fbbe0` |
| Release ref SHA | `f9a106fb28674b00b5c09fe793448f3f939fbbe0` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 2 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/f9a106fb2867-1778395297` | `f9a106fb2867` | 33m 15s | 53m 1s | 32m 47s | [25622065192](https://github.com/openclaw/openclaw/actions/runs/25622065192) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/f9a106fb2867-1778395297` | `f9a106fb2867` | 4m 6s | 1h 15m 10s | 3m 28s | [25622071403](https://github.com/openclaw/openclaw/actions/runs/25622071403) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/f9a106fb2867-1778395297` | `f9a106fb2867` | 31m 51s | 7h 45m 28s | 31m 47s | [25622071771](https://github.com/openclaw/openclaw/actions/runs/25622071771) | 48 |
| fail | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/f9a106fb2867-1778395297` | `f9a106fb2867` | 2m 56s | 2m 45s | 11s | [25622130403](https://github.com/openclaw/openclaw/actions/runs/25622130403) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 32m 23s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622065192/job/75210443634) |
| 25m 51s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75210570929) |
| 25m 13s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75210697720) |
| 23m 45s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75210803373) |
| 13m 41s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75210697713) |
| 13m 1s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75210571060) |
| 12m 40s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75210697719) |
| 12m 39s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install G) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75210803394) |
| 11m 51s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75210697712) |
| 11m 40s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75210697715) |
| 11m 34s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75210697722) |
| 8m 46s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622065192/job/75210443635) |
| 4m 41s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622065192/job/75210443629) |
| 3m 28s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622071403/job/75210475048) |
| 3m 17s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622065192/job/75210443628) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 32m 47s | 28s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25622065192/job/75212049457) |
| 31m 47s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75212023358) |
| 19m 5s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75211383113) |
| 8m 16s | 5m 7s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75210814383) |
| 8m 16s | 4m 47s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75210814396) |
| 8m 15s | 7m 9s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75210814385) |
| 8m 15s | 2m 25s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75210814389) |
| 8m 15s | 5m 25s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75210814391) |
| 8m 14s | 1m 6s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75210814374) |
| 8m 14s | 10m 50s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75210814381) |
| 8m 14s | 5m 24s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75210814388) |
| 3m 34s | 3m 17s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622065192/job/75210592445) |
| 3m 28s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622071403/job/75210603116) |
| 3m 13s | 3s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622071403/job/75210589656) |
| 3m 12s | 4s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25622071403/job/75210589639) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25622065192
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25622065192/job/75212049457
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25622071771
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75210697720
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75210803373
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25622071771/job/75212023358
- `postpublish-telegram`: failure - https://github.com/openclaw/openclaw/actions/runs/25622130403
  - Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25622130403/job/75210598540

## Notes

Automatically requested by Full Release Validation 25622065192 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

