# OpenClaw Release Evidence: 29d7376ff8fc9e72114a89d289ef4ae1ca770592

Generated: 2026-05-04T00:12:47.957Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `29d7376ff8fc9e72114a89d289ef4ae1ca770592` |
| Release ref input | `29d7376ff8fc9e72114a89d289ef4ae1ca770592` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `29d7376ff8fc9e72114a89d289ef4ae1ca770592` |
| Release ref SHA | `29d7376ff8fc9e72114a89d289ef4ae1ca770592` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/29d7376ff8fc-1777851973` | `29d7376ff8fc` | 26m 5s | 40m 53s | 25m 42s | [25294286154](https://github.com/openclaw/openclaw/actions/runs/25294286154) | 0 |
| pass | blocking | `normal-ci` | CI | `release-ci/29d7376ff8fc-1777851973` | `29d7376ff8fc` | 4m 15s | 1h 21m 57s | 4m 13s | [25294291335](https://github.com/openclaw/openclaw/actions/runs/25294291335) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/29d7376ff8fc-1777851973` | `29d7376ff8fc` | 24m 57s | 7h 50m 14s | 24m 53s | [25294291687](https://github.com/openclaw/openclaw/actions/runs/25294291687) | 40 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 25m 29s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294286154/job/74150556545) |
| 22m 25s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150669321) |
| 22m 8s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150669173) |
| 20m 42s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-smoke, native-live-src-... | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150669330) |
| 20m 19s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150768769) |
| 18m 54s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-smoke, Native live ga... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150669348) |
| 17m 49s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150669329) |
| 17m 29s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150768760) |
| 17m 25s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150669326) |
| 17m 19s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150768764) |
| 16m 53s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150768741) |
| 10m 15s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294286154/job/74150556552) |
| 4m 38s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294286154/job/74150556551) |
| 3m 51s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294291335/job/74150570494) |
| 2m 19s | `normal-ci` | checks-node-core-fast | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294291335/job/74150570607) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 25m 42s | 23s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25294286154/job/74151865262) |
| 24m 53s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74151833613) |
| 21m 10s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74151627961) |
| 6m 32s | 1m 57s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150875012) |
| 6m 32s | 1m 31s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150875017) |
| 6m 32s | 1m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150875018) |
| 6m 32s | 14m 36s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150875019) |
| 6m 32s | 52s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150875021) |
| 6m 32s | 1m 37s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150875025) |
| 6m 31s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150875205) |
| 6m 31s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150875209) |
| 4m 13s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294291335/job/74150758923) |
| 2m 40s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294291335/job/74150688546) |
| 2m 9s | 2s | `normal-ci` | checks-fast-contracts-plugins | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294291335/job/74150659972) |
| 2m 4s | 3s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25294291335/job/74150660448) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25294286154
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25294286154/job/74151865262
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25294291687
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150615235
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node .re...: failure - https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150669327
  - Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-smoke, native-live-src-...: failure - https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150669330
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74150875019
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74151627961
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25294291687/job/74151833613

## Notes

Automatically requested by Full Release Validation 25294286154 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

