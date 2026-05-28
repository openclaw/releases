# OpenClaw Release Evidence: 8541f69f892d57bb261a1694f0f5b0cb24ded1d1

Generated: 2026-05-10T09:47:23.721Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `8541f69f892d57bb261a1694f0f5b0cb24ded1d1` |
| Release ref input | `8541f69f892d57bb261a1694f0f5b0cb24ded1d1` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `8541f69f892d57bb261a1694f0f5b0cb24ded1d1` |
| Release ref SHA | `8541f69f892d57bb261a1694f0f5b0cb24ded1d1` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release/2026.5.10` | `8541f69f892d` | 43m 36s | 43m 28s | 43m 19s | [25624728445](https://github.com/openclaw/openclaw/actions/runs/25624728445) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.5.10` | `8541f69f892d` | 42m 42s | 7h 23m 16s | 42m 38s | [25624735372](https://github.com/openclaw/openclaw/actions/runs/25624735372) | 48 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 43m 3s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25624728445/job/75217673766) |
| 36m 13s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75217974883) |
| 30m 20s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75218098916) |
| 26m 50s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75217814868) |
| 22m 11s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75218098908) |
| 11m 2s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75217974878) |
| 9m 54s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75218111487) |
| 9m 23s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75217974886) |
| 8m 12s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75217815061) |
| 7m 56s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install C) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75218098917) |
| 7m 42s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75218111520) |
| 16s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25624728445/job/75219954980) |
| 9s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25624728445/job/75217663840) |
| 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25624728445/job/75217673865) |
| 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25624728445/job/75217673868) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 43m 19s | 16s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25624728445/job/75219954980) |
| 42m 38s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75219936570) |
| 18m 14s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75218631295) |
| 8m 25s | 7m 7s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75218111496) |
| 8m 19s | 1m 1s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75218111537) |
| 8m 18s | 1m 49s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75218111475) |
| 8m 18s | 1m 5s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75218111481) |
| 8m 18s | 9m 54s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75218111487) |
| 8m 18s | 1m 40s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75218111489) |
| 8m 18s | 4m 5s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75218111493) |
| 8m 18s | 4m 5s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75218111503) |
| 14s | 43m 3s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25624728445/job/75217673766) |
| 12s | 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25624728445/job/75217673865) |
| 12s | 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25624728445/job/75217673868) |
| 12s | 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25624728445/job/75217673917) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25624728445
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25624728445/job/75219954980
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25624735372
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): failure - https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75217923225
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75218098916
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25624735372/job/75219936570

## Notes

Automatically requested by Full Release Validation 25624728445 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

