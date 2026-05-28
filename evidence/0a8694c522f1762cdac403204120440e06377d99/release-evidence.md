# OpenClaw Release Evidence: 0a8694c522f1762cdac403204120440e06377d99

Generated: 2026-05-03T23:52:08.622Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `0a8694c522f1762cdac403204120440e06377d99` |
| Release ref input | `0a8694c522f1762cdac403204120440e06377d99` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `0a8694c522f1762cdac403204120440e06377d99` |
| Release ref SHA | `0a8694c522f1762cdac403204120440e06377d99` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/0a8694c522f1-1777850581207` | `0a8694c522f1` | 28m 45s | 44m 23s | 28m 14s | [25293809107](https://github.com/openclaw/openclaw/actions/runs/25293809107) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/0a8694c522f1-1777850581207` | `0a8694c522f1` | 3m 57s | 1h 13m 30s | 3m 53s | [25293815361](https://github.com/openclaw/openclaw/actions/runs/25293815361) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/0a8694c522f1-1777850581207` | `0a8694c522f1` | 27m 19s | 13h 9m 38s | 27m 15s | [25293815503](https://github.com/openclaw/openclaw/actions/runs/25293815503) | 40 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/f0bb00f54ba3-1777850563426` | `f0bb00f54ba3` | 1m 44s | 1m 40s | 3s | [25293862699](https://github.com/openclaw/openclaw/actions/runs/25293862699) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 27m 59s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809107/job/74149421176) |
| 25m 7s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74149533710) |
| 24m 35s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74149533746) |
| 22m 58s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74149533722) |
| 21m 17s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74149533708) |
| 20m 57s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74149533721) |
| 20m 9s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74149533736) |
| 19m 56s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74149591912) |
| 19m 52s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74149591915) |
| 19m 39s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74149533695) |
| 18m 53s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74149591908) |
| 7m 13s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809107/job/74149421179) |
| 4m 12s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809107/job/74149421177) |
| 3m 34s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815361/job/74149439399) |
| 2m 23s | `normal-ci` | checks-node-core-runtime-infra-process | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815361/job/74149439463) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 28m 14s | 30s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25293809107/job/74150790649) |
| 27m 15s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74150758213) |
| 23m 58s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74150598605) |
| 16m 8s | 1m 43s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74150225129) |
| 16m 8s | 2m 23s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74150225134) |
| 16m 8s | 1m 43s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74150225136) |
| 16m 8s | 1m 51s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74150225142) |
| 16m 8s | 1m 25s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74150225147) |
| 16m 8s | 1m 37s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74150225149) |
| 16m 8s | 1m 0s | `release-checks` | Run Docker release-path validation / Docker E2E (core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74150225150) |
| 16m 8s | 1m 21s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74150225151) |
| 3m 53s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815361/job/74149624263) |
| 2m 42s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815361/job/74149563016) |
| 2m 29s | 2m 12s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809107/job/74149538467) |
| 2m 8s | 3s | `normal-ci` | checks-fast-contracts-plugins | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293815361/job/74149529734) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25293809107
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25293809107/job/74150790649
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25293815361
  - check-lint: failure - https://github.com/openclaw/openclaw/actions/runs/25293815361/job/74149439386
  - check: failure - https://github.com/openclaw/openclaw/actions/runs/25293815361/job/74149517186
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25293815503
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74149483304
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node .re...: failure - https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74149533770
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25293815503/job/74150758213

## Notes

Automatically requested by Full Release Validation 25293809107 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

