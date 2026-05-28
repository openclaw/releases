# OpenClaw Release Evidence: dc3c5b048e36018b2e81d72bec7e4b0b2d73158d

Generated: 2026-05-10T06:44:23.831Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `dc3c5b048e36018b2e81d72bec7e4b0b2d73158d` |
| Release ref input | `dc3c5b048e36018b2e81d72bec7e4b0b2d73158d` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `dc3c5b048e36018b2e81d72bec7e4b0b2d73158d` |
| Release ref SHA | `dc3c5b048e36018b2e81d72bec7e4b0b2d73158d` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/dc3c5b048e36-1778391814` | `dc3c5b048e36` | 1h 0m 15s | 1h 0m 7s | 1h 0m 3s | [25621045197](https://github.com/openclaw/openclaw/actions/runs/25621045197) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/dc3c5b048e36-1778391814` | `dc3c5b048e36` | 59m 37s | 4h 21m 33s | 59m 32s | [25621049871](https://github.com/openclaw/openclaw/actions/runs/25621049871) | 15 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 59m 49s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621045197/job/75207640234) |
| 52m 11s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75208013242) |
| 24m 17s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75207782326) |
| 8m 55s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75207880800) |
| 8m 23s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75207782517) |
| 7m 22s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75207782508) |
| 6m 55s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75207782510) |
| 5m 58s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75207782527) |
| 5m 57s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75207880814) |
| 4m 53s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75207782533) |
| 4m 42s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75207782511) |
| 11s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25621045197/job/75210521144) |
| 7s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621045197/job/75207633277) |
| 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25621045197/job/75207640318) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 0m 3s | 11s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25621045197/job/75210521144) |
| 59m 32s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75210511685) |
| 7m 19s | 52m 11s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75208013242) |
| 7m 19s | 1m 51s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75208013244) |
| 7m 19s | 1m 38s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75208013245) |
| 7m 19s | 1m 35s | `release-checks` | Run Docker release-path validation / Docker E2E (core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75208013248) |
| 7m 19s | 1m 51s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75208013249) |
| 7m 19s | 2m 4s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75208013250) |
| 7m 19s | 1m 22s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75208013269) |
| 7m 19s | 1m 59s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install E) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75208013271) |
| 7m 19s | 1m 50s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install H) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75208013272) |
| 12s | 59m 49s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25621045197/job/75207640234) |
| 11s |  | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25621045197/job/75207640351) |
| 11s |  | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25621045197/job/75207640376) |
| 11s |  | `full-release-validation` | Run package Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25621045197/job/75207640378) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25621045197
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25621045197/job/75210521144
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25621049871
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node .re...: failure - https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75207782512
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75208013242
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25621049871/job/75210511685

## Notes

Automatically requested by Full Release Validation 25621045197 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

