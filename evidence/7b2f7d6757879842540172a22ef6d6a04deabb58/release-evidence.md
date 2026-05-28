# OpenClaw Release Evidence: 7b2f7d6757879842540172a22ef6d6a04deabb58

Generated: 2026-05-09T17:18:30.295Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `7b2f7d6757879842540172a22ef6d6a04deabb58` |
| Release ref input | `7b2f7d6757879842540172a22ef6d6a04deabb58` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `7b2f7d6757879842540172a22ef6d6a04deabb58` |
| Release ref SHA | `7b2f7d6757879842540172a22ef6d6a04deabb58` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 2 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/7b2f7d675787-1778346241088` | `7b2f7d675787` | 14m 8s | 40m 28s | 13m 34s | [25606740802](https://github.com/openclaw/openclaw/actions/runs/25606740802) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/7b2f7d675787-1778346241088` | `7b2f7d675787` | 12m 43s | 1h 39m 9s | 2m 45s | [25606749619](https://github.com/openclaw/openclaw/actions/runs/25606749619) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/7b2f7d675787-1778346241088` | `7b2f7d675787` | 13m 13s | 5h 13m 42s | 13m 10s | [25606749814](https://github.com/openclaw/openclaw/actions/runs/25606749814) | 46 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/7b2f7d675787-1778346241088` | `7b2f7d675787` | 3m 4s | 2m 52s | 12s | [25606806515](https://github.com/openclaw/openclaw/actions/runs/25606806515) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 13m 2s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606740802/job/75169875623) |
| 12m 51s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606740802/job/75169875600) |
| 12m 28s | `normal-ci` | macos-node | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606749619/job/75169899866) |
| 12m 0s | `normal-ci` | macos-swift | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25606749619/job/75169899869) |
| 10m 37s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170018340) |
| 8m 40s | `release-checks` | cross_os_release_checks / Linux / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170126417) |
| 8m 35s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170126413) |
| 8m 34s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170126418) |
| 8m 16s | `release-checks` | cross_os_release_checks / macOS / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170126424) |
| 7m 50s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170126411) |
| 7m 50s | `release-checks` | cross_os_release_checks / Windows / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170126422) |
| 7m 48s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606740802/job/75169875598) |
| 7m 42s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170126430) |
| 7m 7s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170018410) |
| 6m 32s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170018435) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 13m 34s | 33s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25606740802/job/75170592978) |
| 13m 10s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170603368) |
| 13m 3s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170597112) |
| 12m 18s | 40s | `release-checks` | cross_os_release_checks / macOS / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170126414) |
| 9m 12s | 3m 46s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170126420) |
| 7m 22s | 1m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170269930) |
| 7m 21s | 4m 55s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170269934) |
| 7m 21s | 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170269937) |
| 7m 21s | 1m 38s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170269940) |
| 7m 21s | 4m 44s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170269941) |
| 7m 20s | 5m 42s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170269929) |
| 3m 2s | 3m 20s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606740802/job/75170025772) |
| 2m 45s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606749619/job/75170033652) |
| 2m 28s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606749619/job/75170020181) |
| 1m 52s | 2s | `normal-ci` | checks-fast-contracts-plugins | success | [job](https://github.com/openclaw/openclaw/actions/runs/25606749619/job/75169987581) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606740802
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606740802/job/75169875600
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606740802/job/75169875623
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25606740802/job/75170592978
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606749619
  - macos-node: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606749619/job/75169899866
  - macos-swift: failure - https://github.com/openclaw/openclaw/actions/runs/25606749619/job/75169899869
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606749814
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170018340
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-...: failure - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170018435
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170126411
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170126413
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170126414
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170126417
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170126418
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170126420
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170126422
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170126424
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170126430
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170248712
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): cancelled - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170248757
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6): failure - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170269926
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15): cancelled - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170269929
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7): failure - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170269932
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5): failure - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170269933
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2): failure - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170269934
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.23): failure - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170269941
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4): failure - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170269943
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170597112
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25606749814/job/75170603368

## Notes

Automatically requested by Full Release Validation 25606740802 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

