# OpenClaw Release Evidence: 695d3693499cc4224ac9466155c548ee7090b5b2

Generated: 2026-05-09T21:38:17.399Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `695d3693499cc4224ac9466155c548ee7090b5b2` |
| Release ref input | `695d3693499cc4224ac9466155c548ee7090b5b2` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `695d3693499cc4224ac9466155c548ee7090b5b2` |
| Release ref SHA | `695d3693499cc4224ac9466155c548ee7090b5b2` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 0 | 0 | 2 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/695d3693499c-1778361880280` | `695d3693499c` | 13m 9s | 43m 1s | 12m 42s | [25612175739](https://github.com/openclaw/openclaw/actions/runs/25612175739) | 1 |
| running | blocking | `normal-ci` | CI | `release-ci/695d3693499c-1778361880280` | `695d3693499c` | 13s | 1h 8m 21s | 2m 40s | [25612185480](https://github.com/openclaw/openclaw/actions/runs/25612185480) | 4 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/695d3693499c-1778361880280` | `695d3693499c` | 4m 8s | 3h 35m 41s | 7m 6s | [25612183326](https://github.com/openclaw/openclaw/actions/runs/25612183326) | 34 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/695d3693499c-1778361880280` | `695d3693499c` | 3m 14s | 2m 53s | 20s | [25612239500](https://github.com/openclaw/openclaw/actions/runs/25612239500) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 12m 17s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25612175739/job/75184153220) |
| 12m 11s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25612175739/job/75184153230) |
| 11m 22s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612175739/job/75184153228) |
| 7m 46s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612183326/job/75184278380) |
| 7m 39s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612183326/job/75184360466) |
| 6m 51s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612183326/job/75184278460) |
| 5m 42s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612183326/job/75184360501) |
| 5m 18s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612183326/job/75184498686) |
| 5m 7s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612183326/job/75184278396) |
| 4m 41s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612183326/job/75184278381) |
| 4m 36s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612183326/job/75184278415) |
| 4m 25s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612183326/job/75184278400) |
| 4m 24s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612183326/job/75184485840) |
| 3m 46s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612175739/job/75184290307) |
| 3m 1s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612185480/job/75184175498) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 12m 42s | 27s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25612175739/job/75184766733) |
| 7m 6s | 4m 3s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612183326/job/75184498660) |
| 7m 6s | 3m 59s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612183326/job/75184498680) |
| 7m 6s | 3m 53s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612183326/job/75184498683) |
| 7m 5s | 1m 26s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612183326/job/75184498670) |
| 7m 5s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25612183326/job/75184498675) |
| 7m 5s | 1m 37s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612183326/job/75184498682) |
| 7m 5s | 57s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612183326/job/75184498684) |
| 7m 5s | 5m 18s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612183326/job/75184498686) |
| 7m 5s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25612183326/job/75184498688) |
| 7m 5s | 52s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612183326/job/75184498691) |
| 3m 11s | 3m 46s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612175739/job/75184290307) |
| 2m 40s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612185480/job/75184292804) |
| 2m 12s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612185480/job/75184269710) |
| 2m 1s | 2s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25612185480/job/75184261255) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612175739
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612175739/job/75184153220
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25612175739/job/75184153230
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25612175739/job/75184766733

## Notes

Automatically requested by Full Release Validation 25612175739 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

