# OpenClaw Release Evidence: 4556707cb7d844df26da2d7ab2d3697d0da946c6

Generated: 2026-05-04T22:37:14.565Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `4556707cb7d844df26da2d7ab2d3697d0da946c6` |
| Release ref input | `4556707cb7d844df26da2d7ab2d3697d0da946c6` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `4556707cb7d844df26da2d7ab2d3697d0da946c6` |
| Release ref SHA | `4556707cb7d844df26da2d7ab2d3697d0da946c6` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/4556707cb7d8-1777930170764` | `4556707cb7d8` | 1h 7m 16s | 1h 34m 10s | 1h 6m 44s | [25344560552](https://github.com/openclaw/openclaw/actions/runs/25344560552) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/4556707cb7d8-1777930170764` | `4556707cb7d8` | 4m 16s | 1h 16m 49s | 4m 13s | [25344581071](https://github.com/openclaw/openclaw/actions/runs/25344581071) | 4 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/4556707cb7d8-1777930170764` | `4556707cb7d8` | 1h 5m 46s | 14h 11m 49s | 1h 5m 43s | [25344578112](https://github.com/openclaw/openclaw/actions/runs/25344578112) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/4556707cb7d8-1777930170764` | `4556707cb7d8` | 4m 38s | 1m 43s | 2m 54s | [25344689467](https://github.com/openclaw/openclaw/actions/runs/25344689467) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 6m 17s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344560552/job/74310274971) |
| 53m 25s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344578112/job/74311991510) |
| 42m 8s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344578112/job/74310925550) |
| 22m 31s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344578112/job/74310644114) |
| 21m 19s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344578112/job/74310644004) |
| 21m 12s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344578112/job/74310644099) |
| 21m 4s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344578112/job/74311398189) |
| 20m 54s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344578112/job/74310644240) |
| 20m 0s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344578112/job/74311398159) |
| 19m 14s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344578112/job/74310644110) |
| 19m 8s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344578112/job/74310644132) |
| 15m 20s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344560552/job/74310274908) |
| 4m 54s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344560552/job/74310635432) |
| 4m 42s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344560552/job/74310274910) |
| 3m 43s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344581071/job/74310361067) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 6m 44s | 31s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25344560552/job/74319038260) |
| 1h 5m 43s | 2s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344578112/job/74318964784) |
| 1h 5m 29s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344578112/job/74318950993) |
| 12m 48s | 2m 1s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344578112/job/74311991500) |
| 12m 47s | 1m 33s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344578112/job/74311991513) |
| 12m 46s | 1m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344578112/job/74311991499) |
| 12m 5s | 2m 1s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344578112/job/74311991522) |
| 12m 2s | 53m 25s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344578112/job/74311991510) |
| 11m 58s | 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344578112/job/74311991496) |
| 11m 56s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25344578112/job/74311991791) |
| 11m 56s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25344578112/job/74311991985) |
| 4m 13s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344581071/job/74310915105) |
| 2m 55s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344581071/job/74310720777) |
| 2m 54s | 1m 43s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344689467/job/74310677484) |
| 2m 48s | 4m 54s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25344560552/job/74310635432) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25344560552
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25344560552/job/74319038260
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25344581071
  - checks-windows-node-test: failure - https://github.com/openclaw/openclaw/actions/runs/25344581071/job/74310361006

## Notes

Automatically requested by Full Release Validation 25344560552 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

