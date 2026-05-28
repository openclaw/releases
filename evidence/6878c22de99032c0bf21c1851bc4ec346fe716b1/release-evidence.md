# OpenClaw Release Evidence: 6878c22de99032c0bf21c1851bc4ec346fe716b1

Generated: 2026-05-04T01:22:06.328Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `6878c22de99032c0bf21c1851bc4ec346fe716b1` |
| Release ref input | `6878c22de99032c0bf21c1851bc4ec346fe716b1` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `6878c22de99032c0bf21c1851bc4ec346fe716b1` |
| Release ref SHA | `6878c22de99032c0bf21c1851bc4ec346fe716b1` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/6878c22de990-1777855311` | `6878c22de990` | 39m 55s (+28m 0s) | 41m 35s (+22m 31s) | 39m 26s | [25295551392](https://github.com/openclaw/openclaw/actions/runs/25295551392) | 0 |
| pass | blocking | `normal-ci` | CI | `release-ci/6878c22de990-1777855311` | `6878c22de990` | 4m 10s (-2m 1s) | 1h 23m 51s (-1m 44s) | 4m 6s | [25295799846](https://github.com/openclaw/openclaw/actions/runs/25295799846) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/6878c22de990-1777855311` | `6878c22de990` | 28m 32s (+28m 13s) | 8h 4m 35s (+8h 4m 29s) | 28m 30s | [25295800268](https://github.com/openclaw/openclaw/actions/runs/25295800268) | 40 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 29m 8s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295551392/job/74154302723) |
| 22m 35s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74154438313) |
| 21m 42s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74154705219) |
| 20m 53s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74154515940) |
| 19m 52s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74154438291) |
| 19m 37s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-smoke, native-live-src-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74154438297) |
| 19m 27s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74154515937) |
| 18m 56s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74154515943) |
| 18m 24s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-smoke, Native live ga... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74154438341) |
| 17m 28s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74154515952) |
| 16m 55s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74154515942) |
| 7m 9s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295551392/job/74154302722) |
| 4m 40s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295551392/job/74154302718) |
| 3m 50s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295799846/job/74154321107) |
| 3m 3s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295799846/job/74154321079) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 39m 26s | 28s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25295551392/job/74156107748) |
| 28m 30s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74156067933) |
| 28m 16s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74156061648) |
| 10m 22s | 7m 9s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295551392/job/74154302722) |
| 10m 16s | 4m 40s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295551392/job/74154302718) |
| 10m 16s | 29m 8s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295551392/job/74154302723) |
| 10m 15s |  | `full-release-validation` | Run package Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25295551392/job/74154303077) |
| 10m 14s | 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25295551392/job/74154302988) |
| 10m 4s | 10s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295551392/job/74154291069) |
| 6m 41s | 1m 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74154705214) |
| 6m 41s | 2m 41s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74154705215) |
| 6m 41s | 57s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74154705218) |
| 6m 32s | 1m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74154705210) |
| 6m 32s | 1m 33s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74154705211) |
| 6m 32s | 21m 42s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74154705219) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `release-checks` | 19s | 28m 32s | +28m 13s | +8h 4m 29s |
| `full-release-validation` | 11m 55s | 39m 55s | +28m 0s | +22m 31s |
| `normal-ci` | 6m 11s | 4m 10s | -2m 1s | -1m 44s |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25295551392
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25295551392/job/74156107748
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25295800268
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74154376297
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74154705219
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74156061648
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25295800268/job/74156067933

## Notes

Automatically requested by Full Release Validation 25295551392 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

