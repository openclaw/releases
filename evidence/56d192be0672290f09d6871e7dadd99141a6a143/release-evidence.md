# OpenClaw Release Evidence: 56d192be0672290f09d6871e7dadd99141a6a143

Generated: 2026-05-10T12:24:18.796Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `56d192be0672290f09d6871e7dadd99141a6a143` |
| Release ref input | `56d192be0672290f09d6871e7dadd99141a6a143` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `56d192be0672290f09d6871e7dadd99141a6a143` |
| Release ref SHA | `56d192be0672290f09d6871e7dadd99141a6a143` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release/2026.5.10` | `56d192be0672` | 39m 6s | 38m 52s | 38m 51s | [25627858042](https://github.com/openclaw/openclaw/actions/runs/25627858042) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.5.10` | `56d192be0672` | 38m 0s | 5h 39m 25s | 37m 57s | [25627866233](https://github.com/openclaw/openclaw/actions/runs/25627866233) | 48 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 38m 28s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25627858042/job/75226089159) |
| 32m 27s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75226361909) |
| 24m 18s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75226227706) |
| 12m 9s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75226482263) |
| 10m 14s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75226514903) |
| 10m 3s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75226514909) |
| 7m 38s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75226227878) |
| 7m 10s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75226227877) |
| 7m 9s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75226514913) |
| 7m 5s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75226227881) |
| 6m 4s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75226227847) |
| 14s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25627858042/job/75228148435) |
| 10s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25627858042/job/75226080349) |
| 0s | `full-release-validation` | Run package Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25627858042/job/75226089469) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 38m 51s | 14s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25627858042/job/75228148435) |
| 37m 57s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75228122441) |
| 18m 31s | 7s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75227069642) |
| 8m 18s | 1m 30s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75226514914) |
| 8m 17s | 4m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75226514912) |
| 8m 17s | 7m 9s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75226514913) |
| 8m 17s | 1m 57s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75226514915) |
| 8m 17s | 1m 35s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75226514919) |
| 8m 16s | 10m 14s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75226514903) |
| 8m 16s | 1m 6s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75226514905) |
| 8m 16s | 4m 10s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75226514907) |
| 21s | 38m 28s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25627858042/job/75226089159) |
| 14s |  | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25627858042/job/75226089222) |
| 14s |  | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25627858042/job/75226089270) |
| 14s |  | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25627858042/job/75226089374) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25627858042
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25627858042/job/75228148435
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25627866233
  - Run package acceptance / Telegram package acceptance / Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75226416929
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75226482263
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75227069642
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25627866233/job/75228122441

## Notes

Automatically requested by Full Release Validation 25627858042 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

