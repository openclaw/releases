# OpenClaw Release Evidence: 681b56fc0af9653010446a6004639e5de191b4fb

Generated: 2026-05-10T06:55:41.999Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `681b56fc0af9653010446a6004639e5de191b4fb` |
| Release ref input | `681b56fc0af9653010446a6004639e5de191b4fb` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `681b56fc0af9653010446a6004639e5de191b4fb` |
| Release ref SHA | `681b56fc0af9653010446a6004639e5de191b4fb` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/681b56fc0af9-1778392428` | `681b56fc0af9` | 1h 1m 42s | 1h 1m 27s | 1h 1m 30s | [25621220604](https://github.com/openclaw/openclaw/actions/runs/25621220604) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/681b56fc0af9-1778392428` | `681b56fc0af9` | 1h 0m 34s | 4h 35m 5s | 1h 0m 31s | [25621228190](https://github.com/openclaw/openclaw/actions/runs/25621228190) | 15 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 1m 9s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621220604/job/75208163011) |
| 52m 15s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75208555684) |
| 25m 9s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75208287866) |
| 9m 31s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75208375976) |
| 9m 1s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75208375972) |
| 8m 18s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75208287993) |
| 7m 16s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75208288003) |
| 7m 11s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75208555696) |
| 7m 1s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75208375962) |
| 6m 3s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75208287994) |
| 5m 45s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75208287964) |
| 11s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25621220604/job/75211080762) |
| 7s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621220604/job/75208150998) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25621220604/job/75208163089) |
| 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25621220604/job/75208163171) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 1m 30s | 11s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25621220604/job/75211080762) |
| 1h 0m 31s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75211050738) |
| 8m 15s | 2m 4s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75208555695) |
| 8m 15s | 1m 18s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install F) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75208555716) |
| 8m 15s | 1m 23s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75208555720) |
| 8m 14s | 52m 15s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75208555684) |
| 8m 14s | 2m 35s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75208555698) |
| 8m 14s | 1m 21s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install H) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75208555712) |
| 8m 13s | 1m 45s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install C) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75208555709) |
| 8m 13s | 1m 12s | `release-checks` | Run Docker release-path validation / Docker E2E (core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75208555715) |
| 8m 13s | 1m 39s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install G) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75208555719) |
| 19s | 1h 1m 9s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621220604/job/75208163011) |
| 17s | 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25621220604/job/75208163089) |
| 17s | 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25621220604/job/75208163171) |
| 17s | 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25621220604/job/75208163183) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25621220604
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25621220604/job/75211080762
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25621228190
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75208555684
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25621228190/job/75211050738

## Notes

Automatically requested by Full Release Validation 25621220604 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

