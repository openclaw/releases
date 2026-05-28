# OpenClaw Release Evidence: 85a0f1c018ea7ee2b894a1ddcbbd396c8d28c105

Generated: 2026-05-10T10:33:24.336Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `85a0f1c018ea7ee2b894a1ddcbbd396c8d28c105` |
| Release ref input | `85a0f1c018ea7ee2b894a1ddcbbd396c8d28c105` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `85a0f1c018ea7ee2b894a1ddcbbd396c8d28c105` |
| Release ref SHA | `85a0f1c018ea7ee2b894a1ddcbbd396c8d28c105` |
| Runs at release SHA | `full-release-validation`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release/2026.5.10` | `85a0f1c018ea` | 48m 17s | 48m 1s | 48m 2s | [25625524976](https://github.com/openclaw/openclaw/actions/runs/25625524976) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.5.10` | `85a0f1c018ea` | 47m 17s | 6h 53m 7s | 47m 14s | [25625532588](https://github.com/openclaw/openclaw/actions/runs/25625532588) | 48 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 47m 35s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625524976/job/75219864869) |
| 41m 28s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75220146071) |
| 30m 20s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75220289204) |
| 24m 18s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75219998599) |
| 13m 57s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75220146069) |
| 9m 42s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75219998736) |
| 8m 50s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75219998755) |
| 8m 21s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75220307099) |
| 7m 50s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75220289209) |
| 7m 47s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75219998750) |
| 7m 24s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75220146073) |
| 14s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25625524976/job/75222324433) |
| 12s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625524976/job/75219852693) |
| 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25625524976/job/75219864996) |
| 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25625524976/job/75219865051) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 48m 2s | 14s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25625524976/job/75222324433) |
| 47m 14s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75222308551) |
| 16m 32s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75220750614) |
| 8m 9s | 8m 21s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75220307099) |
| 8m 8s | 1m 46s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75220307086) |
| 8m 8s | 2m 41s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75220307089) |
| 8m 8s | 5m 18s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75220307101) |
| 8m 7s | 1m 6s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75220307087) |
| 8m 7s | 5m 12s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75220307092) |
| 8m 7s | 4m 2s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75220307093) |
| 8m 7s | 4m 18s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75220307095) |
| 18s | 47m 35s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625524976/job/75219864869) |
| 17s |  | `full-release-validation` | Run package Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25625524976/job/75219865118) |
| 16s | 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25625524976/job/75219864996) |
| 16s | 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25625524976/job/75219865051) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25625524976
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25625524976/job/75222324433
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25625532588
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75220289204
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25625532588/job/75222308551

## Notes

Automatically requested by Full Release Validation 25625524976 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

