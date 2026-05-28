# OpenClaw Release Evidence: 638dea598cd14d5bc872c2534414e3cb0c8a7ac2

Generated: 2026-05-10T12:57:29.278Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `638dea598cd14d5bc872c2534414e3cb0c8a7ac2` |
| Release ref input | `638dea598cd14d5bc872c2534414e3cb0c8a7ac2` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `638dea598cd14d5bc872c2534414e3cb0c8a7ac2` |
| Release ref SHA | `638dea598cd14d5bc872c2534414e3cb0c8a7ac2` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release/2026.5.10` | `638dea598cd1` | 40m 33s | 40m 24s | 40m 19s | [25628491878](https://github.com/openclaw/openclaw/actions/runs/25628491878) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.5.10` | `638dea598cd1` | 39m 42s | 5h 59m 15s | 39m 37s | [25628498800](https://github.com/openclaw/openclaw/actions/runs/25628498800) | 48 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 40m 2s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25628491878/job/75227761109) |
| 32m 44s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75228062348) |
| 26m 33s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75227904982) |
| 11m 34s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75228206149) |
| 10m 29s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75228233658) |
| 9m 28s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75227905144) |
| 7m 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75228233667) |
| 7m 32s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75228206182) |
| 7m 30s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75228233652) |
| 7m 14s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75227905138) |
| 7m 13s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install D) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75228206174) |
| 13s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25628491878/job/75230001427) |
| 9s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25628491878/job/75227750246) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25628491878/job/75227761229) |
| 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25628491878/job/75227761303) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 40m 19s | 13s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25628491878/job/75230001427) |
| 39m 37s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75229980265) |
| 18m 58s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75228854756) |
| 8m 28s | 4m 36s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75228233651) |
| 8m 27s | 1m 35s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75228233646) |
| 8m 27s | 7m 30s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75228233652) |
| 8m 27s | 10m 29s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75228233658) |
| 8m 26s | 1m 44s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75228233641) |
| 8m 26s | 4m 25s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75228233661) |
| 8m 25s | 2m 19s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75228233638) |
| 8m 25s | 1m 9s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75228233642) |
| 15s | 40m 2s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25628491878/job/75227761109) |
| 13s | 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25628491878/job/75227761229) |
| 13s | 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25628491878/job/75227761303) |
| 13s | 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25628491878/job/75227761305) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25628491878
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25628491878/job/75230001427
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25628498800
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-agents, Native live agents, node .release-harness/...: failure - https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75227905126
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75228206149
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25628498800/job/75229980265

## Notes

Automatically requested by Full Release Validation 25628491878 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

