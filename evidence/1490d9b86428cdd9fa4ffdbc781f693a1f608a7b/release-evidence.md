# OpenClaw Release Evidence: 1490d9b86428cdd9fa4ffdbc781f693a1f608a7b

Generated: 2026-05-04T20:27:06.013Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `1490d9b86428cdd9fa4ffdbc781f693a1f608a7b` |
| Release ref input | `1490d9b86428cdd9fa4ffdbc781f693a1f608a7b` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `1490d9b86428cdd9fa4ffdbc781f693a1f608a7b` |
| Release ref SHA | `1490d9b86428cdd9fa4ffdbc781f693a1f608a7b` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/1490d9b86428-1777923265660` | `1490d9b86428` | 52m 15s | 1h 18m 44s | 51m 43s | [25339178545](https://github.com/openclaw/openclaw/actions/runs/25339178545) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/1490d9b86428-1777923265660` | `1490d9b86428` | 9m 22s | 1h 21m 49s | 7m 49s | [25339204789](https://github.com/openclaw/openclaw/actions/runs/25339204789) | 1 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/1490d9b86428-1777923265660` | `1490d9b86428` | 50m 46s | 13h 58m 41s | 50m 41s | [25339210748](https://github.com/openclaw/openclaw/actions/runs/25339210748) | 40 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/1490d9b86428-1777923265660` | `1490d9b86428` | 1m 53s | 1m 48s | 5s | [25339325314](https://github.com/openclaw/openclaw/actions/runs/25339325314) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 51m 9s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339178545/job/74292134965) |
| 44m 38s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74292860431) |
| 28m 30s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74293677987) |
| 23m 31s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74292542625) |
| 22m 30s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74292542592) |
| 21m 38s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74292542605) |
| 20m 47s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74292542626) |
| 19m 10s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74292767055) |
| 18m 59s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74292542584) |
| 18m 58s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74292542604) |
| 18m 51s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74292542643) |
| 12m 19s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339178545/job/74292134908) |
| 9m 51s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339178545/job/74292134970) |
| 3m 51s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339204789/job/74292225391) |
| 3m 45s | `normal-ci` | checks-windows-node-test | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339204789/job/74292225402) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 51m 43s | 31s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25339178545/job/74300299049) |
| 50m 41s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74300237833) |
| 37m 57s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74298254074) |
| 9m 24s | 1m 25s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74293677976) |
| 9m 24s | 2m 6s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74293677977) |
| 9m 24s | 28m 30s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74293677987) |
| 9m 23s | 1m 52s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74293677958) |
| 9m 23s | 1m 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74293677986) |
| 9m 23s | 1m 42s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74293678114) |
| 9m 21s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74293678390) |
| 9m 21s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74293678715) |
| 7m 49s | 3s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25339204789/job/74293382899) |
| 6m 35s | 3s | `normal-ci` | checks-fast-contracts-plugins | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339204789/job/74293203395) |
| 6m 12s | 2s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25339204789/job/74293129409) |
| 6m 8s | 3s | `normal-ci` | build-smoke | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25339204789/job/74293119327) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25339178545
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25339178545/job/74300299049
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25339204789
  - build-artifacts: failure - https://github.com/openclaw/openclaw/actions/runs/25339204789/job/74292225255
  - checks-node-agentic-control-plane-auth-node: failure - https://github.com/openclaw/openclaw/actions/runs/25339204789/job/74292225833
  - build-smoke: failure - https://github.com/openclaw/openclaw/actions/runs/25339204789/job/74293119327
  - check-additional: failure - https://github.com/openclaw/openclaw/actions/runs/25339204789/job/74293119370
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25339204789/job/74293382899
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25339210748
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74292373745
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74293677987
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74298254074
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25339210748/job/74300237833

## Notes

Automatically requested by Full Release Validation 25339178545 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

