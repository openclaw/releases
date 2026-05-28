# OpenClaw Release Evidence: 62adabf3ce45b71591fcfceadcf746b22696bb0c

Generated: 2026-05-04T00:28:29.280Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `62adabf3ce45b71591fcfceadcf746b22696bb0c` |
| Release ref input | `62adabf3ce45b71591fcfceadcf746b22696bb0c` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `62adabf3ce45b71591fcfceadcf746b22696bb0c` |
| Release ref SHA | `62adabf3ce45b71591fcfceadcf746b22696bb0c` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/62adabf3ce45-1777852873` | `62adabf3ce45` | 26m 47s | 41m 55s | 26m 19s | [25294594665](https://github.com/openclaw/openclaw/actions/runs/25294594665) | 0 |
| pass | blocking | `normal-ci` | CI | `release-ci/62adabf3ce45-1777852873` | `62adabf3ce45` | 4m 18s | 1h 24m 54s | 4m 14s | [25294605100](https://github.com/openclaw/openclaw/actions/runs/25294605100) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/62adabf3ce45-1777852873` | `62adabf3ce45` | 25m 38s | 7h 56m 31s | 25m 34s | [25294605307](https://github.com/openclaw/openclaw/actions/runs/25294605307) | 40 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 25m 55s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294594665/job/74151284275) |
| 22m 6s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74151413510) |
| 21m 21s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74151413672) |
| 20m 41s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74151551277) |
| 20m 3s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74151551246) |
| 19m 46s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-smoke, native-live-src-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74151413667) |
| 18m 37s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-smoke, Native live ga... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74151413662) |
| 17m 59s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74151551279) |
| 17m 39s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74151551250) |
| 17m 26s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74151413678) |
| 16m 26s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74151551213) |
| 10m 43s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294594665/job/74151284294) |
| 4m 39s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294594665/job/74151284286) |
| 3m 56s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605100/job/74151309340) |
| 3m 2s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605100/job/74151309338) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 26m 19s | 27s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25294594665/job/74152805276) |
| 25m 34s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74152787926) |
| 22m 13s | 4s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74152584368) |
| 11m 4s | 1m 50s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74151897192) |
| 11m 3s | 1m 35s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74151897197) |
| 11m 0s | 1m 24s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install H) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74151897212) |
| 10m 59s | 1m 20s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74151897207) |
| 10m 52s | 2m 16s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install C) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74151897211) |
| 10m 51s | 1m 56s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74151897185) |
| 10m 51s | 1m 23s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74151897187) |
| 10m 51s | 2m 23s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74151897189) |
| 4m 14s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605100/job/74151526287) |
| 2m 48s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605100/job/74151443886) |
| 2m 43s | 2s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605100/job/74151435208) |
| 2m 39s | 3s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294605100/job/74151435478) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25294594665
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25294594665/job/74152805276
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25294605307
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74151358245
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node .re...: failure - https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74151413675
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74151698821
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74152584368
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25294605307/job/74152787926

## Notes

Automatically requested by Full Release Validation 25294594665 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

