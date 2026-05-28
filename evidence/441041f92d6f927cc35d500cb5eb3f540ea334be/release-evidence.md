# OpenClaw Release Evidence: 441041f92d6f927cc35d500cb5eb3f540ea334be

Generated: 2026-05-12T13:30:45.532Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `441041f92d6f927cc35d500cb5eb3f540ea334be` |
| Release ref input | `441041f92d6f927cc35d500cb5eb3f540ea334be` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `441041f92d6f927cc35d500cb5eb3f540ea334be` |
| Release ref SHA | `441041f92d6f927cc35d500cb5eb3f540ea334be` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/441041f92d6f-1778588752362` | `441041f92d6f` | 1h 4m 12s | 1h 37m 23s | 1h 3m 8s | [25734280121](https://github.com/openclaw/openclaw/actions/runs/25734280121) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/441041f92d6f-1778588752362` | `441041f92d6f` | 4m 36s | 1h 13m 40s | 4m 22s | [25734328336](https://github.com/openclaw/openclaw/actions/runs/25734328336) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/441041f92d6f-1778588752362` | `441041f92d6f` | 1h 1m 20s | 17h 4m 54s | 1h 1m 17s | [25734324948](https://github.com/openclaw/openclaw/actions/runs/25734324948) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/441041f92d6f-1778588752362` | `441041f92d6f` | 7m 19s | 2m 56s | 4m 21s | [25734622865](https://github.com/openclaw/openclaw/actions/runs/25734622865) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 2m 2s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25734280121/job/75567157880) |
| 50m 54s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156412) |
| 50m 49s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156335) |
| 45m 31s | `release-checks` | install_smoke_release_checks / root_dockerfile_image | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75567473602) |
| 40m 45s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156358) |
| 35m 59s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156283) |
| 35m 52s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156251) |
| 35m 51s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156275) |
| 35m 49s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156386) |
| 35m 45s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156241) |
| 35m 43s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156219) |
| 15m 4s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25734280121/job/75567157795) |
| 7m 55s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25734280121/job/75568163753) |
| 5m 37s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25734280121/job/75567157786) |
| 5m 15s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25734280121/job/75567157834) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 3m 8s | 1m 2s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25734280121/job/75578816938) |
| 1h 1m 17s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75578654941) |
| 47m 15s | 0s | `release-checks` | install_smoke_release_checks / installer_smoke | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75575938729) |
| 47m 15s | 0s | `release-checks` | install_smoke_release_checks / root_dockerfile_smokes | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75575938960) |
| 47m 15s | 0s | `release-checks` | install_smoke_release_checks / bun_global_install_smoke | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75575939156) |
| 20m 37s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75570823067) |
| 12m 41s | 55s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75569309161) |
| 12m 41s | 4m 51s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75569309292) |
| 12m 40s | 32m 12s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75569308729) |
| 12m 40s | 4m 52s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75569309139) |
| 12m 40s | 7m 41s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75569309143) |
| 6m 39s | 7m 55s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25734280121/job/75568163753) |
| 4m 22s | 11s | `normal-ci` | security-fast | success | [job](https://github.com/openclaw/openclaw/actions/runs/25734328336/job/75567874540) |
| 4m 21s | 2m 56s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25734622865/job/75568210329) |
| 3m 50s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25734328336/job/75567852675) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25734280121
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25734280121/job/75578816938
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25734324948
  - install_smoke_release_checks / root_dockerfile_image: failure - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75567473602
  - Run repo/live E2E validation / Docker live models (OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156209
  - Run repo/live E2E validation / Docker live models (OpenCode): failure - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156219
  - Run repo/live E2E validation / Docker live models (OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156237
  - Run repo/live E2E validation / Docker live models (Google): failure - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156241
  - Run repo/live E2E validation / Docker live models (MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156251
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156270
  - Run repo/live E2E validation / Docker live models (Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156275
  - Run repo/live E2E validation / Docker live models (Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156283
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156284
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156302
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156307
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156335
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156344
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156354
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156358
  - Run repo/live E2E validation / Docker live models (Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156386
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156405
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156412
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75568156463
  - Run Docker release-path validation / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75569308729
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25734324948/job/75578654941

## Notes

Automatically requested by Full Release Validation 25734280121 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

