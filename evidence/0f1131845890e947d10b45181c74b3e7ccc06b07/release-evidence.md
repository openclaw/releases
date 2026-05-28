# OpenClaw Release Evidence: 0f1131845890e947d10b45181c74b3e7ccc06b07

Generated: 2026-05-09T23:11:14.442Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `0f1131845890e947d10b45181c74b3e7ccc06b07` |
| Release ref input | `0f1131845890e947d10b45181c74b3e7ccc06b07` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `0f1131845890e947d10b45181c74b3e7ccc06b07` |
| Release ref SHA | `0f1131845890e947d10b45181c74b3e7ccc06b07` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/0f1131845890-1778367619312` | `0f1131845890` | 10m 28s | 28m 8s | 9m 56s | [25614001525](https://github.com/openclaw/openclaw/actions/runs/25614001525) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/0f1131845890-1778367619312` | `0f1131845890` | 2m 58s | 1h 11m 30s | 2m 44s | [25614008648](https://github.com/openclaw/openclaw/actions/runs/25614008648) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/0f1131845890-1778367619312` | `0f1131845890` | 9m 49s | 4h 2m 48s | 9m 46s | [25614008688](https://github.com/openclaw/openclaw/actions/runs/25614008688) | 33 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/0f1131845890-1778367619312` | `0f1131845890` | 2m 56s | 2m 45s | 11s | [25614055236](https://github.com/openclaw/openclaw/actions/runs/25614055236) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 9m 37s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614001525/job/75188827727) |
| 8m 44s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614001525/job/75188827728) |
| 6m 56s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75188946907) |
| 6m 52s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75188946998) |
| 6m 19s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75188947013) |
| 5m 14s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75188947018) |
| 5m 6s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189033641) |
| 5m 5s | `release-checks` | cross_os_release_checks / Linux / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189033627) |
| 5m 5s | `release-checks` | cross_os_release_checks / Linux / packaged fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189033637) |
| 4m 50s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75188946991) |
| 4m 48s | `release-checks` | cross_os_release_checks / macOS / installer fresh | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189033654) |
| 4m 47s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189036496) |
| 3m 20s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614001525/job/75188945982) |
| 3m 15s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614001525/job/75188827734) |
| 2m 45s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614055236/job/75188952691) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 9m 56s | 31s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25614001525/job/75189250582) |
| 9m 46s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189260010) |
| 9m 22s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189238417) |
| 9m 21s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189238410) |
| 9m 21s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189238467) |
| 9m 21s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (${{ matrix.group.label }}) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189238542) |
| 6m 49s | 1m 31s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189124610) |
| 6m 49s | 2m 47s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189124617) |
| 6m 49s | 1m 25s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install E) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189124632) |
| 6m 49s | 1m 24s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install H) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189124633) |
| 6m 49s | 1m 34s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install F) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189124637) |
| 2m 49s | 3m 20s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614001525/job/75188945982) |
| 2m 44s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614008648/job/75188958028) |
| 2m 15s | 4s | `normal-ci` | check-additional | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25614008648/job/75188935018) |
| 1m 54s | 2s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25614008648/job/75188920141) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614001525
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614001525/job/75188827727
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25614001525/job/75189250582
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25614008648
  - check-additional-boundaries-d: failure - https://github.com/openclaw/openclaw/actions/runs/25614008648/job/75188844580
  - check-additional: failure - https://github.com/openclaw/openclaw/actions/runs/25614008648/job/75188935018
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75188946907
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75188946998
  - cross_os_release_checks / Linux / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189033627
  - cross_os_release_checks / Windows / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189033635
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189033636
  - cross_os_release_checks / Linux / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189033637
  - cross_os_release_checks / Windows / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189033638
  - cross_os_release_checks / Linux / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189033641
  - cross_os_release_checks / macOS / packaged fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189033642
  - cross_os_release_checks / macOS / installer fresh: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189033654
  - cross_os_release_checks / macOS / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189033664
  - Run repo/live E2E validation / Docker live models (Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189036435
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189036441
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189036443
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): failure - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189036444
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189036496
  - Run package acceptance / Docker product acceptance / prepare_docker_e2e_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189114585
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189124600
  - Run Docker release-path validation / Docker E2E (core): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189124602
  - Run Docker release-path validation / Docker E2E (package/update core): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189124606
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189124617
  - Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189238410
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189238417
  - Run package acceptance / Docker product acceptance / Docker E2E (openwebui): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189238467
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (${{ matrix.group.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189238542
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25614008688/job/75189260010

## Notes

Automatically requested by Full Release Validation 25614001525 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

