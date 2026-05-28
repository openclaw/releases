# OpenClaw Release Evidence: 31633bc0ec80e6e314b1eeed3d9e1196a8ac0eef

Generated: 2026-05-06T01:11:23.651Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `31633bc0ec80e6e314b1eeed3d9e1196a8ac0eef` |
| Release ref input | `31633bc0ec80e6e314b1eeed3d9e1196a8ac0eef` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `31633bc0ec80e6e314b1eeed3d9e1196a8ac0eef` |
| Release ref SHA | `31633bc0ec80e6e314b1eeed3d9e1196a8ac0eef` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/31633bc0ec80-1778026034939` | `31633bc0ec80` | 1h 3m 52s | 1h 21m 32s | 1h 3m 15s | [25409217151](https://github.com/openclaw/openclaw/actions/runs/25409217151) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/31633bc0ec80-1778026034939` | `31633bc0ec80` | 4m 25s | 1h 21m 46s | 4m 22s | [25409229355](https://github.com/openclaw/openclaw/actions/runs/25409229355) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/31633bc0ec80-1778026034939` | `31633bc0ec80` | 1h 2m 42s | 12h 48m 47s | 1h 2m 37s | [25409226686](https://github.com/openclaw/openclaw/actions/runs/25409226686) | 40 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/31633bc0ec80-1778026034939` | `31633bc0ec80` | 1m 37s | 1m 34s | 3s | [25409315214](https://github.com/openclaw/openclaw/actions/runs/25409315214) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 3m 0s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409217151/job/74526943285) |
| 1h 0m 19s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74527162597) |
| 33m 24s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74527773613) |
| 32m 6s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74527363112) |
| 21m 40s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74527162995) |
| 21m 35s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74527163030) |
| 21m 34s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74527163009) |
| 21m 15s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74527163013) |
| 20m 7s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74527163017) |
| 19m 31s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74527983035) |
| 19m 17s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74527163035) |
| 8m 43s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409217151/job/74526943278) |
| 4m 43s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409217151/job/74526943287) |
| 3m 58s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409229355/job/74526985851) |
| 2m 42s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409229355/job/74526985799) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 3m 15s | 36s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25409217151/job/74532833233) |
| 1h 2m 37s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74532804611) |
| 42m 36s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74531014449) |
| 11m 2s | 12m 54s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74527982991) |
| 11m 2s | 13m 19s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74527983004) |
| 11m 2s | 12m 43s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74527983005) |
| 11m 2s | 19m 31s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74527983035) |
| 11m 2s | 8m 28s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74527983048) |
| 11m 2s | 16m 36s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74527983066) |
| 11m 1s | 13m 0s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74527982952) |
| 11m 1s | 14m 5s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74527982954) |
| 4m 22s | 3s | `normal-ci` | check-additional | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25409229355/job/74527370223) |
| 3m 5s | 1m 47s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25409217151/job/74527204613) |
| 2m 51s | 2s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25409229355/job/74527221800) |
| 2m 4s | 4s | `normal-ci` | check | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25409229355/job/74527154439) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25409217151
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25409217151/job/74532833233
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25409229355
  - check-lint: failure - https://github.com/openclaw/openclaw/actions/runs/25409229355/job/74526985760
  - check-additional-extension-bundled: failure - https://github.com/openclaw/openclaw/actions/runs/25409229355/job/74526985820
  - checks-node-core-runtime-infra-process: failure - https://github.com/openclaw/openclaw/actions/runs/25409229355/job/74526986010
  - check: failure - https://github.com/openclaw/openclaw/actions/runs/25409229355/job/74527154439
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25409229355/job/74527221800
  - check-additional: failure - https://github.com/openclaw/openclaw/actions/runs/25409229355/job/74527370223
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25409226686
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74527162597
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74527982978
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25409226686/job/74532804611

## Notes

Automatically requested by Full Release Validation 25409217151 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

