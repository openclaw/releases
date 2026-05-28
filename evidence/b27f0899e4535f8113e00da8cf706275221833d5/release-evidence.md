# OpenClaw Release Evidence: b27f0899e4535f8113e00da8cf706275221833d5

Generated: 2026-05-13T07:15:28.119Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `b27f0899e4535f8113e00da8cf706275221833d5` |
| Release ref input | `b27f0899e4535f8113e00da8cf706275221833d5` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `b27f0899e4535f8113e00da8cf706275221833d5` |
| Release ref SHA | `b27f0899e4535f8113e00da8cf706275221833d5` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/b27f0899e453-1778652283721` | `b27f0899e453` | 1h 10m 21s | 1h 30m 3s | 1h 9m 43s | [25781558113](https://github.com/openclaw/openclaw/actions/runs/25781558113) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/b27f0899e453-1778652283721` | `b27f0899e453` | 3m 25s | 1h 1m 50s | 3m 23s | [25781571399](https://github.com/openclaw/openclaw/actions/runs/25781571399) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/b27f0899e453-1778652283721` | `b27f0899e453` | 1h 8m 55s | 6h 34m 55s | 1h 8m 51s | [25781575402](https://github.com/openclaw/openclaw/actions/runs/25781575402) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/b27f0899e453-1778652283721` | `b27f0899e453` | 3m 37s | 3m 26s | 10s | [25781704175](https://github.com/openclaw/openclaw/actions/runs/25781704175) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 9m 19s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781558113/job/75725199700) |
| 1h 0m 32s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75726150122) |
| 15m 14s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75725848500) |
| 10m 11s | `release-checks` | install_smoke_release_checks / installer_smoke | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75725721173) |
| 10m 10s | `release-checks` | install_smoke_release_checks / root_dockerfile_smokes | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75725721177) |
| 10m 9s | `release-checks` | install_smoke_release_checks / bun_global_install_smoke | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75725721206) |
| 9m 41s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75725848158) |
| 8m 51s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781558113/job/75725199672) |
| 8m 46s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75725533401) |
| 7m 48s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75726172147) |
| 7m 5s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75725533411) |
| 7m 5s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75726172155) |
| 3m 52s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781558113/job/75725611821) |
| 3m 40s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781558113/job/75725199655) |
| 3m 32s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781558113/job/75725199684) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 9m 43s | 38s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25781558113/job/75733866790) |
| 1h 8m 51s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75733797298) |
| 16m 11s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75727088485) |
| 8m 22s | 4m 33s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75726172149) |
| 8m 22s | 4m 8s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75726172174) |
| 8m 22s | 1m 40s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75726172211) |
| 8m 21s | 51s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75726172138) |
| 8m 21s | 1m 41s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75726172145) |
| 8m 21s | 7m 48s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75726172147) |
| 8m 21s | 7m 5s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75726172155) |
| 8m 21s | 4m 15s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75726172158) |
| 3m 52s | 3m 52s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781558113/job/75725611821) |
| 3m 23s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781571399/job/75725600606) |
| 3m 18s | 2s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781571399/job/75725578444) |
| 3m 18s | 2s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25781571399/job/75725578478) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25781558113
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25781558113/job/75733866790
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25781575402
  - install_smoke_release_checks / installer_smoke: failure - https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75725721173
  - install_smoke_release_checks / root_dockerfile_smokes: failure - https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75725721177
  - install_smoke_release_checks / bun_global_install_smoke: failure - https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75725721206
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): cancelled - https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75726150122
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25781575402/job/75733797298

## Notes

Automatically requested by Full Release Validation 25781558113 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

