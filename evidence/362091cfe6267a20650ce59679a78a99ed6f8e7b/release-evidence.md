# OpenClaw Release Evidence: 362091cfe6267a20650ce59679a78a99ed6f8e7b

Generated: 2026-05-04T00:07:53.258Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `362091cfe6267a20650ce59679a78a99ed6f8e7b` |
| Release ref input | `362091cfe6267a20650ce59679a78a99ed6f8e7b` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `362091cfe6267a20650ce59679a78a99ed6f8e7b` |
| Release ref SHA | `362091cfe6267a20650ce59679a78a99ed6f8e7b` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/362091cfe626-1777851183640` | `362091cfe626` | 34m 27s | 53m 31s | 33m 58s | [25294024194](https://github.com/openclaw/openclaw/actions/runs/25294024194) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/362091cfe626-1777851183640` | `362091cfe626` | 7m 24s | 1h 25m 7s | 6m 27s | [25294030513](https://github.com/openclaw/openclaw/actions/runs/25294030513) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/362091cfe626-1777851183640` | `362091cfe626` | 33m 13s | 13h 20m 33s | 33m 8s | [25294030662](https://github.com/openclaw/openclaw/actions/runs/25294030662) | 40 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/362091cfe626-1777851183640` | `362091cfe626` | 1m 46s | 1m 42s | 3s | [25294082507](https://github.com/openclaw/openclaw/actions/runs/25294082507) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 33m 43s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294024194/job/74149930970) |
| 26m 52s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74150223722) |
| 25m 17s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74150040930) |
| 22m 25s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74150040928) |
| 21m 43s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74150040921) |
| 21m 36s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74150040933) |
| 20m 50s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74150131747) |
| 19m 51s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74150040947) |
| 19m 39s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74150040948) |
| 19m 29s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74150040950) |
| 18m 45s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74150131773) |
| 7m 46s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294024194/job/74149930980) |
| 6m 40s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294024194/job/74149930987) |
| 6m 12s | `normal-ci` | checks-node-agentic-control-plane-runtime | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294030513/job/74149948735) |
| 3m 41s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294030513/job/74149948589) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 33m 58s | 28s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25294024194/job/74151589694) |
| 33m 8s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74151559716) |
| 33m 0s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74151552530) |
| 7m 42s | 11m 18s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74150136967) |
| 7m 41s | 10m 57s | `release-checks` | cross_os_release_checks / macOS / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74150136971) |
| 6m 27s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294030513/job/74150240406) |
| 6m 6s | 1m 31s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74150223716) |
| 6m 6s | 1m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74150223719) |
| 6m 6s | 7m 14s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74150223720) |
| 6m 6s | 26m 52s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74150223722) |
| 6m 6s | 50s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74150223724) |
| 6m 6s | 2m 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74150223733) |
| 5m 19s | 2m 4s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294030513/job/74149948538) |
| 3m 56s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294030513/job/74150124058) |
| 2m 42s | 2m 18s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294024194/job/74150053827) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25294024194
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25294024194/job/74151589694
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25294030662
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74149996850
  - Run repo/live E2E validation / validate_release_live_cache: failure - https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74150040813
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node .re...: failure - https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74150040940
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74150223722
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74151552530
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25294030662/job/74151559716

## Notes

Automatically requested by Full Release Validation 25294024194 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

