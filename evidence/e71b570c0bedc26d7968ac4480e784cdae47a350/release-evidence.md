# OpenClaw Release Evidence: e71b570c0bedc26d7968ac4480e784cdae47a350

Generated: 2026-05-03T17:13:43.440Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `e71b570c0bedc26d7968ac4480e784cdae47a350` |
| Release ref input | `e71b570c0bedc26d7968ac4480e784cdae47a350` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `e71b570c0bedc26d7968ac4480e784cdae47a350` |
| Release ref SHA | `e71b570c0bedc26d7968ac4480e784cdae47a350` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 2 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/e71b570c0bed-1777826700363` | `e71b570c0bed` | 28m 12s | 53m 0s | 27m 46s | [25284892803](https://github.com/openclaw/openclaw/actions/runs/25284892803) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/e71b570c0bed-1777826700363` | `e71b570c0bed` | 4m 1s | 1h 13m 51s | 3m 56s | [25284902457](https://github.com/openclaw/openclaw/actions/runs/25284902457) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/e71b570c0bed-1777826700363` | `e71b570c0bed` | 27m 5s | 13h 36m 53s | 27m 1s | [25284901048](https://github.com/openclaw/openclaw/actions/runs/25284901048) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/e71b570c0bed-1777826700363` | `e71b570c0bed` | 1m 53s | 1m 36s | 16s | [25284949375](https://github.com/openclaw/openclaw/actions/runs/25284949375) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 27m 28s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284892803/job/74127759888) |
| 24m 35s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74127885741) |
| 22m 50s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74127885727) |
| 22m 27s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74127885726) |
| 21m 53s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74127885750) |
| 21m 38s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74127885728) |
| 21m 21s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74127885769) |
| 21m 6s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74127885721) |
| 19m 44s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74127885706) |
| 19m 41s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74128010763) |
| 19m 27s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74127885749) |
| 16m 18s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284892803/job/74127759882) |
| 4m 8s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284892803/job/74127759889) |
| 3m 38s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284902457/job/74127782265) |
| 2m 27s | `normal-ci` | checks-node-core-runtime-infra-process | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284902457/job/74127782359) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 27m 46s | 26s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25284892803/job/74129268715) |
| 27m 1s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74129246769) |
| 23m 42s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74129066712) |
| 6m 21s | 1m 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74128104750) |
| 6m 20s | 1m 51s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74128104732) |
| 6m 20s | 2m 5s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74128104737) |
| 6m 20s | 1m 20s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74128104739) |
| 6m 20s | 2m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74128104743) |
| 6m 19s | 17m 21s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74128104735) |
| 6m 18s | 1m 32s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74128099086) |
| 6m 17s | 6m 31s | `release-checks` | Run Docker release-path validation / Docker E2E (core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74128099067) |
| 3m 56s | 4s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284902457/job/74127986989) |
| 2m 51s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284902457/job/74127921339) |
| 2m 38s | 2m 15s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284892803/job/74127883296) |
| 2m 21s | 2s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25284902457/job/74127897703) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25284892803
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25284892803/job/74129268715
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25284901048
  - Run repo/live E2E validation / validate_release_live_cache: failure - https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74127885588
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74128104735
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74129066712
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25284901048/job/74129246769

## Notes

Automatically requested by Full Release Validation 25284892803 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

