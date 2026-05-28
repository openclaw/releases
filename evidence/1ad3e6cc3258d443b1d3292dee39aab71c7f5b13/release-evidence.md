# OpenClaw Release Evidence: 1ad3e6cc3258d443b1d3292dee39aab71c7f5b13

Generated: 2026-05-03T23:12:13.582Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `1ad3e6cc3258d443b1d3292dee39aab71c7f5b13` |
| Release ref input | `1ad3e6cc3258d443b1d3292dee39aab71c7f5b13` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `1ad3e6cc3258d443b1d3292dee39aab71c7f5b13` |
| Release ref SHA | `1ad3e6cc3258d443b1d3292dee39aab71c7f5b13` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/1ad3e6cc3258-1777848143328` | `1ad3e6cc3258` | 29m 27s | 49m 58s | 28m 57s | [25292941122](https://github.com/openclaw/openclaw/actions/runs/25292941122) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/1ad3e6cc3258-1777848143328` | `1ad3e6cc3258` | 4m 11s | 1h 20m 20s | 4m 8s | [25292948278](https://github.com/openclaw/openclaw/actions/runs/25292948278) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/1ad3e6cc3258-1777848143328` | `1ad3e6cc3258` | 28m 25s | 13h 18m 4s | 28m 23s | [25292948712](https://github.com/openclaw/openclaw/actions/runs/25292948712) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/1ad3e6cc3258-1777848143328` | `1ad3e6cc3258` | 1m 48s | 1m 44s | 3s | [25293006134](https://github.com/openclaw/openclaw/actions/runs/25293006134) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 28m 39s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292941122/job/74147349447) |
| 25m 50s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74147467148) |
| 23m 41s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74147467139) |
| 23m 40s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74147467127) |
| 23m 29s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74147467133) |
| 23m 16s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74147579374) |
| 22m 32s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74147467119) |
| 21m 48s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74147467121) |
| 21m 27s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74147467111) |
| 21m 8s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74147467118) |
| 20m 22s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74147467134) |
| 11m 19s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292941122/job/74147349445) |
| 4m 42s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292941122/job/74147349448) |
| 3m 46s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292948278/job/74147364279) |
| 2m 32s | `normal-ci` | checks-node-core-runtime-infra-process | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292948278/job/74147364381) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 28m 57s | 30s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292941122/job/74148787130) |
| 28m 23s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74148770979) |
| 22m 40s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74148485180) |
| 6m 38s | 10m 52s | `release-checks` | cross_os_release_checks / macOS / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74147560793) |
| 6m 16s | 1m 46s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74147673852) |
| 6m 16s | 1m 1s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74147673854) |
| 6m 16s | 1m 22s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74147673924) |
| 6m 15s | 1m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74147673849) |
| 6m 15s | 16m 24s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74147673850) |
| 6m 7s | 1m 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74147673846) |
| 6m 6s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74147673963) |
| 4m 8s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292948278/job/74147566003) |
| 2m 54s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292948278/job/74147501629) |
| 2m 51s | 2m 15s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292941122/job/74147479742) |
| 1m 59s | 4s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292948278/job/74147458127) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25292941122
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25292941122/job/74148787130
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25292948712
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74147673850
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74148485180
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25292948712/job/74148770979

## Notes

Automatically requested by Full Release Validation 25292941122 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

