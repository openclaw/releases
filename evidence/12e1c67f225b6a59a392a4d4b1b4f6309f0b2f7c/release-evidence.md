# OpenClaw Release Evidence: 12e1c67f225b6a59a392a4d4b1b4f6309f0b2f7c

Generated: 2026-05-05T04:00:38.392Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `12e1c67f225b6a59a392a4d4b1b4f6309f0b2f7c` |
| Release ref input | `12e1c67f225b6a59a392a4d4b1b4f6309f0b2f7c` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `12e1c67f225b6a59a392a4d4b1b4f6309f0b2f7c` |
| Release ref SHA | `12e1c67f225b6a59a392a4d4b1b4f6309f0b2f7c` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/12e1c67f225b-1777951944298` | `12e1c67f225b` | 27m 45s | 54m 42s | 27m 14s | [25356373953](https://github.com/openclaw/openclaw/actions/runs/25356373953) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/12e1c67f225b-1777951944298` | `12e1c67f225b` | 4m 29s | 1h 13m 35s | 4m 26s | [25356386660](https://github.com/openclaw/openclaw/actions/runs/25356386660) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/12e1c67f225b-1777951944298` | `12e1c67f225b` | 27m 7s | 12h 23m 28s | 27m 3s | [25356389449](https://github.com/openclaw/openclaw/actions/runs/25356389449) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/12e1c67f225b-1777951944298` | `12e1c67f225b` | 2m 11s | 1m 59s | 11s | [25356458081](https://github.com/openclaw/openclaw/actions/runs/25356458081) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 26m 45s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25356373953/job/74346435777) |
| 24m 34s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74346621985) |
| 24m 26s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74346622308) |
| 23m 17s | `release-checks` | install_smoke_release_checks / installer_smoke | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74346740929) |
| 21m 38s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74346795853) |
| 21m 22s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74346622334) |
| 21m 19s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74346622346) |
| 20m 53s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74346622344) |
| 20m 25s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74346737404) |
| 20m 8s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74346622376) |
| 19m 27s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74346737420) |
| 17m 28s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356373953/job/74346435756) |
| 4m 40s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356373953/job/74346435767) |
| 3m 59s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356386660/job/74346477367) |
| 2m 45s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356373953/job/74346632705) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 27m 14s | 31s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25356373953/job/74348470205) |
| 27m 3s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74348502109) |
| 26m 55s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74348490125) |
| 7m 53s | 18m 53s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74347050719) |
| 7m 52s | 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74347050715) |
| 7m 52s | 1m 35s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74347050716) |
| 7m 52s | 19m 2s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74347050718) |
| 7m 52s | 1m 25s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74347050721) |
| 7m 50s | 1m 36s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74347050712) |
| 7m 39s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74347050822) |
| 7m 39s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74347050876) |
| 4m 26s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356386660/job/74346797161) |
| 2m 53s | 2m 45s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356373953/job/74346632705) |
| 2m 52s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356386660/job/74346673944) |
| 2m 15s | 3s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25356386660/job/74346622851) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25356373953
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25356373953/job/74346435777
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25356373953/job/74348470205
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25356389449
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74346621985
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74346622308
  - install_smoke_release_checks / installer_smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74346740929
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74346795853
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): cancelled - https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74347050718
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): cancelled - https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74347050719
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74348490125
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25356389449/job/74348502109

## Notes

Automatically requested by Full Release Validation 25356373953 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

