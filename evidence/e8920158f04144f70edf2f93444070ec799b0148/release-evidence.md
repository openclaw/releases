# OpenClaw Release Evidence: e8920158f04144f70edf2f93444070ec799b0148

Generated: 2026-05-10T10:47:56.879Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `e8920158f04144f70edf2f93444070ec799b0148` |
| Release ref input | `e8920158f04144f70edf2f93444070ec799b0148` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `e8920158f04144f70edf2f93444070ec799b0148` |
| Release ref SHA | `e8920158f04144f70edf2f93444070ec799b0148` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release/2026.5.10` | `e8920158f041` | 39m 29s | 39m 20s | 39m 12s | [25625972136](https://github.com/openclaw/openclaw/actions/runs/25625972136) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.5.10` | `e8920158f041` | 38m 21s | 6h 2m 54s | 38m 17s | [25625979113](https://github.com/openclaw/openclaw/actions/runs/25625979113) | 48 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 38m 51s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625972136/job/75221087465) |
| 32m 31s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75221342782) |
| 30m 21s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75221453191) |
| 28m 47s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75221212845) |
| 8m 30s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75221316074) |
| 7m 48s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75221316071) |
| 7m 47s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75221212943) |
| 7m 44s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75221212962) |
| 6m 59s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75221463712) |
| 6m 1s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75221212950) |
| 5m 55s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75221212977) |
| 16s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25625972136/job/75223073074) |
| 13s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625972136/job/75221076838) |
| 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25625972136/job/75221087650) |
| 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25625972136/job/75221087661) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 39m 12s | 16s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25625972136/job/75223073074) |
| 38m 17s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75223046462) |
| 14m 41s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75221815064) |
| 7m 44s | 53s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75221463708) |
| 7m 44s | 4m 3s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75221463711) |
| 7m 44s | 3m 47s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75221463718) |
| 7m 44s | 1m 31s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75221463720) |
| 7m 44s | 1m 20s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75221463722) |
| 7m 44s | 54s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75221463751) |
| 7m 43s | 4m 12s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75221463710) |
| 7m 43s | 5m 35s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75221463713) |
| 19s | 38m 51s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25625972136/job/75221087465) |
| 16s | 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25625972136/job/75221087650) |
| 16s | 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25625972136/job/75221087661) |
| 16s | 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25625972136/job/75221087674) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25625972136
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25625972136/job/75223073074
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25625979113
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75221453191
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25625979113/job/75223046462

## Notes

Automatically requested by Full Release Validation 25625972136 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

