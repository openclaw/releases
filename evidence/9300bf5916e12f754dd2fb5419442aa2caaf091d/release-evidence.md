# OpenClaw Release Evidence: 9300bf5916e12f754dd2fb5419442aa2caaf091d

Generated: 2026-05-09T23:00:42.961Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `9300bf5916e12f754dd2fb5419442aa2caaf091d` |
| Release ref input | `9300bf5916e12f754dd2fb5419442aa2caaf091d` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `9300bf5916e12f754dd2fb5419442aa2caaf091d` |
| Release ref SHA | `9300bf5916e12f754dd2fb5419442aa2caaf091d` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/9300bf5916e1-1778366748200` | `9300bf5916e1` | 14m 28s | 34m 58s | 13m 57s | [25613737012](https://github.com/openclaw/openclaw/actions/runs/25613737012) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/9300bf5916e1-1778366748200` | `9300bf5916e1` | 3m 52s | 1h 13m 24s | 2m 44s | [25613743350](https://github.com/openclaw/openclaw/actions/runs/25613743350) | 4 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/9300bf5916e1-1778366748200` | `9300bf5916e1` | 7m 35s | 3h 58m 58s | 7m 34s | [25613743370](https://github.com/openclaw/openclaw/actions/runs/25613743370) | 33 |
| fail | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/9300bf5916e1-1778366748200` | `9300bf5916e1` | 3m 46s | 3m 27s | 18s | [25613793875](https://github.com/openclaw/openclaw/actions/runs/25613793875) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 13m 40s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25613737012/job/75188166742) |
| 9m 21s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613737012/job/75188166730) |
| 8m 38s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613743370/job/75188416700) |
| 8m 5s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613743370/job/75188288328) |
| 7m 41s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613743370/job/75188416674) |
| 7m 31s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613743370/job/75188288326) |
| 5m 20s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613743370/job/75188288349) |
| 5m 5s | `release-checks` | Run QA Lab live Telegram lane | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25613743370/job/75188235435) |
| 5m 4s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613743370/job/75188288298) |
| 4m 59s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613743370/job/75188288294) |
| 4m 56s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613743370/job/75188288297) |
| 4m 49s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613743370/job/75188288299) |
| 4m 16s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613737012/job/75188301812) |
| 4m 15s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613737012/job/75188166736) |
| 3m 27s | `postpublish-telegram` | Run package Telegram E2E | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25613793875/job/75188307326) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 13m 57s | 30s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25613737012/job/75188784321) |
| 7m 34s | 1m 41s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613743370/job/75188518114) |
| 7m 34s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25613743370/job/75188518122) |
| 7m 34s | 4m 38s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613743370/job/75188518124) |
| 7m 34s | 1m 37s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613743370/job/75188518125) |
| 7m 34s | 1m 10s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613743370/job/75188518126) |
| 7m 34s | 4m 39s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613743370/job/75188518129) |
| 7m 34s | 4m 13s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613743370/job/75188518130) |
| 7m 33s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) |  | [job](https://github.com/openclaw/openclaw/actions/runs/25613743370/job/75188518115) |
| 7m 33s | 1m 30s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613743370/job/75188518116) |
| 7m 33s | 4m 8s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613743370/job/75188518117) |
| 3m 4s | 4m 16s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613737012/job/75188301812) |
| 2m 44s | 2s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25613743350/job/75188301987) |
| 2m 34s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613743350/job/75188289513) |
| 2m 6s | 2s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25613743350/job/75188268442) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25613737012
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25613737012/job/75188166742
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25613737012/job/75188784321
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25613743350
  - checks-node-agentic-commands-onboard-config: failure - https://github.com/openclaw/openclaw/actions/runs/25613743350/job/75188185659
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25613743350/job/75188301987
- `postpublish-telegram`: failure - https://github.com/openclaw/openclaw/actions/runs/25613793875
  - Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25613793875/job/75188307326

## Notes

Automatically requested by Full Release Validation 25613737012 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

