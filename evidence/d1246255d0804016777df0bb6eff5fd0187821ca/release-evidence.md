# OpenClaw Release Evidence: d1246255d0804016777df0bb6eff5fd0187821ca

Generated: 2026-05-13T05:43:45.749Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `d1246255d0804016777df0bb6eff5fd0187821ca` |
| Release ref input | `d1246255d0804016777df0bb6eff5fd0187821ca` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `d1246255d0804016777df0bb6eff5fd0187821ca` |
| Release ref SHA | `d1246255d0804016777df0bb6eff5fd0187821ca` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 3 | 0 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/d1246255d080-1778649648605` | `d1246255d080` | 22m 25s | 43m 19s | 21m 56s | [25780009082](https://github.com/openclaw/openclaw/actions/runs/25780009082) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/d1246255d080-1778649648605` | `d1246255d080` | 3m 47s | 59m 3s | 3m 44s | [25780022578](https://github.com/openclaw/openclaw/actions/runs/25780022578) | 4 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/d1246255d080-1778649648605` | `d1246255d080` | 21m 29s | 5h 5m 2s | 21m 26s | [25780022064](https://github.com/openclaw/openclaw/actions/runs/25780022064) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/d1246255d080-1778649648605` | `d1246255d080` | 3m 41s | 3m 29s | 12s | [25780135027](https://github.com/openclaw/openclaw/actions/runs/25780135027) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 21m 38s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780009082/job/75720414662) |
| 15m 15s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022064/job/75721004980) |
| 9m 44s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780009082/job/75720414646) |
| 8m 44s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022064/job/75721001396) |
| 7m 50s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022064/job/75720693695) |
| 7m 26s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022064/job/75721547966) |
| 7m 1s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022064/job/75720693779) |
| 6m 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022064/job/75721547955) |
| 6m 2s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022064/job/75720693782) |
| 5m 50s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022064/job/75720693687) |
| 5m 38s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022064/job/75720693691) |
| 4m 47s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022064/job/75721005015) |
| 4m 13s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780009082/job/75720414647) |
| 3m 51s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780009082/job/75720752635) |
| 3m 29s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780135027/job/75720767502) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 21m 56s | 28s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25780009082/job/75722670928) |
| 21m 26s | 2s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022064/job/75722655776) |
| 18m 36s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022064/job/75722343774) |
| 12m 8s | 4m 31s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022064/job/75721547969) |
| 11m 33s | 4m 19s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022064/job/75721547968) |
| 11m 13s | 4m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022064/job/75721547944) |
| 11m 10s | 6m 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022064/job/75721547955) |
| 11m 10s | 1m 44s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022064/job/75721547967) |
| 11m 9s | 1m 33s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022064/job/75721547931) |
| 11m 9s | 58s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022064/job/75721547932) |
| 11m 9s | 1m 42s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022064/job/75721547936) |
| 3m 44s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022578/job/75720809459) |
| 3m 40s | 2s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022578/job/75720793020) |
| 3m 34s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022578/job/75720793014) |
| 3m 34s | 2s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25780022578/job/75720793023) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25780009082
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25780009082/job/75722670928

## Notes

Automatically requested by Full Release Validation 25780009082 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

