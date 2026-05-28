# OpenClaw Release Evidence: 4047f4d0b4207a475d5380ba46a50d6294bd909c

Generated: 2026-05-03T22:21:41.161Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `4047f4d0b4207a475d5380ba46a50d6294bd909c` |
| Release ref input | `4047f4d0b4207a475d5380ba46a50d6294bd909c` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `4047f4d0b4207a475d5380ba46a50d6294bd909c` |
| Release ref SHA | `4047f4d0b4207a475d5380ba46a50d6294bd909c` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 0 | 0 | 2 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/4047f4d0b420-1777846726873` | `4047f4d0b420` | 2m 20s | 6m 30s | 2m 5s | [25292433817](https://github.com/openclaw/openclaw/actions/runs/25292433817) | 0 |
| running | blocking | `normal-ci` | CI | `release-ci/4047f4d0b420-1777846726873` | `4047f4d0b420` | 2m 18s | 1h 0m 10s | 2m 17s | [25292441773](https://github.com/openclaw/openclaw/actions/runs/25292441773) | 4 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/4047f4d0b420-1777846726873` | `4047f4d0b420` | 2m 17s | 4m 10s | 2m 16s | [25292440270](https://github.com/openclaw/openclaw/actions/runs/25292440270) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1m 59s | `normal-ci` | checks-node-core-runtime-shared | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292441773/job/74146154638) |
| 1m 53s | `normal-ci` | build-artifacts | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292441773/job/74146154511) |
| 1m 51s | `normal-ci` | checks-fast-contracts-channels-c | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292441773/job/74146154448) |
| 1m 36s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292433817/job/74146129019) |
| 1m 35s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292433817/job/74146129015) |
| 1m 33s | `normal-ci` | checks-node-agentic-gateway-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292441773/job/74146154662) |
| 1m 29s | `normal-ci` | checks-fast-contracts-plugins-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292441773/job/74146154531) |
| 1m 29s | `normal-ci` | checks-node-agentic-commands-status-tools | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292441773/job/74146154670) |
| 1m 28s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292433817/job/74146129024) |
| 1m 24s | `normal-ci` | check-dependencies | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292441773/job/74146154519) |
| 1m 23s | `normal-ci` | checks-fast-contracts-channels-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292441773/job/74146154463) |
| 1m 23s | `normal-ci` | check-additional-extension-bundled | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292441773/job/74146154557) |
| 1m 23s | `normal-ci` | checks-node-core-runtime-media-ui | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292441773/job/74146154681) |
| 1m 21s | `full-release-validation` | Prepare release package artifact | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25292433817/job/74146129023) |
| 1m 7s | `release-checks` | Run QA Lab live Telegram lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292440270/job/74146195026) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 2m 17s | 2s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292441773/job/74146262695) |
| 2m 17s | 2s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292441773/job/74146262696) |
| 2m 16s | 4s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292441773/job/74146262699) |
| 2m 16s |  | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li... |  | [job](https://github.com/openclaw/openclaw/actions/runs/25292440270/job/74146246230) |
| 2m 16s |  | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... |  | [job](https://github.com/openclaw/openclaw/actions/runs/25292440270/job/74146246238) |
| 2m 16s |  | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro... |  | [job](https://github.com/openclaw/openclaw/actions/runs/25292440270/job/74146246239) |
| 2m 16s |  | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi... |  | [job](https://github.com/openclaw/openclaw/actions/runs/25292440270/job/74146246240) |
| 2m 16s |  | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... |  | [job](https://github.com/openclaw/openclaw/actions/runs/25292440270/job/74146246241) |
| 2m 16s |  | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... |  | [job](https://github.com/openclaw/openclaw/actions/runs/25292440270/job/74146246242) |
| 2m 16s |  | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-backends, Native live gateway backends, no... |  | [job](https://github.com/openclaw/openclaw/actions/runs/25292440270/job/74146246246) |
| 2m 16s |  | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-agents, Native live agents, node .release-harness/... |  | [job](https://github.com/openclaw/openclaw/actions/runs/25292440270/job/74146246250) |
| 2m 16s |  | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-xai, Native live xAI plugin, node .release-... |  | [job](https://github.com/openclaw/openclaw/actions/runs/25292440270/job/74146246261) |
| 2m 16s |  | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node .re... |  | [job](https://github.com/openclaw/openclaw/actions/runs/25292440270/job/74146246263) |
| 2m 13s | 3s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292441773/job/74146260089) |
| 2m 5s | 15s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292433817/job/74146221973) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292433817
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292433817/job/74146129015
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292433817/job/74146129019
  - Prepare release package artifact: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292433817/job/74146129023
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25292433817/job/74146129024
  - Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25292433817/job/74146204014
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25292433817/job/74146221973

## Notes

Automatically requested by Full Release Validation 25292433817 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

