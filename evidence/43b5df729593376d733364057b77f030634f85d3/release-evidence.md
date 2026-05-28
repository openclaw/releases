# OpenClaw Release Evidence: 43b5df729593376d733364057b77f030634f85d3

Generated: 2026-05-04T22:29:10.780Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `43b5df729593376d733364057b77f030634f85d3` |
| Release ref input | `43b5df729593376d733364057b77f030634f85d3` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `43b5df729593376d733364057b77f030634f85d3` |
| Release ref SHA | `43b5df729593376d733364057b77f030634f85d3` |
| Runs at release SHA | `full-release-validation`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 0 | 0 | 0 |
| Advisory | 1 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | advisory | `full-release-validation` | Full Release Validation | `release-ci/43b5df729593-1777932096219` | `43b5df729593` | 27m 14s | 26m 51s | 27m 0s | [25345905481](https://github.com/openclaw/openclaw/actions/runs/25345905481) | 0 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/43b5df729593-1777932096219` | `43b5df729593` | 25m 59s | 4h 51m 1s | 25m 56s | [25345926285](https://github.com/openclaw/openclaw/actions/runs/25345926285) | 15 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 26m 26s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345905481/job/74314698962) |
| 20m 56s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345926285/job/74315018558) |
| 20m 16s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-smoke, native-live-src-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345926285/job/74315018544) |
| 18m 34s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-smoke, Native live ga... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345926285/job/74315018577) |
| 17m 9s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345926285/job/74315692591) |
| 16m 46s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345926285/job/74315018575) |
| 16m 40s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345926285/job/74315692598) |
| 16m 33s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345926285/job/74315692636) |
| 15m 33s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345926285/job/74315018649) |
| 15m 22s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345926285/job/74315018118) |
| 13m 29s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345926285/job/74315692576) |
| 13s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345905481/job/74318095477) |
| 12s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345905481/job/74314667486) |
| 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25345905481/job/74314699181) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25345905481/job/74314699360) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 27m 0s | 13s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345905481/job/74318095477) |
| 25m 56s | 3s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345926285/job/74318039824) |
| 8m 9s | 13m 28s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345926285/job/74315692575) |
| 8m 9s | 17m 9s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345926285/job/74315692591) |
| 8m 9s | 6s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345926285/job/74315692593) |
| 7m 18s | 12m 56s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345926285/job/74315692559) |
| 7m 18s | 7s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345926285/job/74315692574) |
| 7m 18s | 13m 29s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345926285/job/74315692576) |
| 7m 18s | 13m 15s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345926285/job/74315692580) |
| 7m 18s | 7s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345926285/job/74315692583) |
| 7m 18s | 6s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345926285/job/74315692586) |
| 25s | 26m 26s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25345905481/job/74314698962) |
| 16s | 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25345905481/job/74314699181) |
| 16s | 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25345905481/job/74314699360) |
| 16s | 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25345905481/job/74314699426) |

## Notes

Automatically requested by Full Release Validation 25345905481 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

