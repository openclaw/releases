# OpenClaw Release Evidence: f0bb00f54ba3fcafd2e988653626020f19db70f4

Generated: 2026-05-03T23:53:52.877Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `f0bb00f54ba3fcafd2e988653626020f19db70f4` |
| Release ref input | `f0bb00f54ba3fcafd2e988653626020f19db70f4` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `f0bb00f54ba3fcafd2e988653626020f19db70f4` |
| Release ref SHA | `f0bb00f54ba3fcafd2e988653626020f19db70f4` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/f0bb00f54ba3-1777850563426` | `f0bb00f54ba3` | 30m 40s | 46m 39s | 30m 14s | [25293802042](https://github.com/openclaw/openclaw/actions/runs/25293802042) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/f0bb00f54ba3-1777850563426` | `f0bb00f54ba3` | 4m 3s | 1h 21m 39s | 3m 59s | [25293809176](https://github.com/openclaw/openclaw/actions/runs/25293809176) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/f0bb00f54ba3-1777850563426` | `f0bb00f54ba3` | 29m 16s | 13h 15m 51s | 29m 12s | [25293809356](https://github.com/openclaw/openclaw/actions/runs/25293809356) | 40 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/f0bb00f54ba3-1777850563426` | `f0bb00f54ba3` | 1m 44s | 1m 40s | 3s | [25293862699](https://github.com/openclaw/openclaw/actions/runs/25293862699) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 29m 57s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293802042/job/74149406165) |
| 27m 2s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74149520246) |
| 25m 0s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74149520264) |
| 22m 30s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74149520250) |
| 21m 32s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74149625792) |
| 21m 23s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74149625789) |
| 21m 9s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74149520234) |
| 20m 42s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74149520254) |
| 20m 19s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74149520245) |
| 20m 19s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74149625786) |
| 19m 42s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74149520233) |
| 6m 43s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293802042/job/74149406146) |
| 4m 41s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293802042/job/74149406144) |
| 3m 43s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809176/job/74149421938) |
| 2m 44s | `normal-ci` | checks-node-core-runtime-infra-process | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809176/job/74149422038) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 30m 14s | 25s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25293802042/job/74150869185) |
| 29m 12s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74150836159) |
| 26m 37s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74150712309) |
| 11m 18s | 1m 36s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74149987959) |
| 11m 18s | 15m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74149987965) |
| 11m 18s | 2m 2s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74149987966) |
| 11m 18s | 53s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74149987968) |
| 11m 18s | 1m 18s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74149987969) |
| 11m 18s | 1m 34s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74149987973) |
| 11m 17s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74149988099) |
| 11m 17s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74149988112) |
| 3m 59s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809176/job/74149614248) |
| 2m 58s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809176/job/74149562603) |
| 2m 46s | 2m 14s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293802042/job/74149535795) |
| 2m 0s | 3s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25293809176/job/74149512645) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25293802042
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25293802042/job/74150869185
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25293809356
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74149466888
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node .re...: failure - https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74149520247
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74149987965
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74150712309
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25293809356/job/74150836159

## Notes

Automatically requested by Full Release Validation 25293802042 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

