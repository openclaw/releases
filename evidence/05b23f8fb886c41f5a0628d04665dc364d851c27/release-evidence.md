# OpenClaw Release Evidence: 05b23f8fb886c41f5a0628d04665dc364d851c27

Generated: 2026-05-13T06:47:02.194Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `05b23f8fb886c41f5a0628d04665dc364d851c27` |
| Release ref input | `05b23f8fb886c41f5a0628d04665dc364d851c27` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `05b23f8fb886c41f5a0628d04665dc364d851c27` |
| Release ref SHA | `05b23f8fb886c41f5a0628d04665dc364d851c27` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/05b23f8fb886-1778653371485` | `05b23f8fb886` | 23m 37s | 43m 25s | 23m 9s | [25782230301](https://github.com/openclaw/openclaw/actions/runs/25782230301) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/05b23f8fb886-1778653371485` | `05b23f8fb886` | 3m 21s | 59m 22s | 3m 18s | [25782250945](https://github.com/openclaw/openclaw/actions/runs/25782250945) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/05b23f8fb886-1778653371485` | `05b23f8fb886` | 22m 21s | 5h 6m 14s | 22m 18s | [25782251050](https://github.com/openclaw/openclaw/actions/runs/25782251050) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/05b23f8fb886-1778653371485` | `05b23f8fb886` | 3m 56s | 3m 44s | 11s | [25782376859](https://github.com/openclaw/openclaw/actions/runs/25782376859) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 22m 41s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782230301/job/75727297136) |
| 15m 56s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75727962031) |
| 8m 51s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75727645409) |
| 8m 44s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782230301/job/75727297142) |
| 8m 33s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75727889777) |
| 7m 22s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75727962006) |
| 7m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75728277349) |
| 6m 56s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75727645434) |
| 6m 40s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75728277285) |
| 6m 39s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75727645428) |
| 6m 32s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75727645396) |
| 5m 48s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-sonnet-haiku, native-li... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75727645429) |
| 4m 23s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782230301/job/75727703189) |
| 3m 44s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782376859/job/75727719457) |
| 3m 42s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782230301/job/75727297158) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 23m 9s | 27s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25782230301/job/75730094600) |
| 22m 18s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75730044306) |
| 15m 24s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75729195480) |
| 8m 5s | 4m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75728277264) |
| 8m 5s | 59s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75728277307) |
| 8m 5s | 1m 34s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75728277313) |
| 8m 5s | 7m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75728277349) |
| 8m 4s | 1m 20s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75728277248) |
| 8m 4s | 1m 3s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75728277253) |
| 8m 4s | 4m 6s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75728277257) |
| 8m 4s | 4m 21s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75728277258) |
| 3m 43s | 4m 23s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782230301/job/75727703189) |
| 3m 18s | 2s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25782250945/job/75727704384) |
| 3m 7s | 3s | `normal-ci` | checks-node-core-support-boundary | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25782250945/job/75727683249) |
| 3m 7s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25782250945/job/75727683253) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25782230301
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25782230301/job/75730094600
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25782250945
  - checks-node-core-support-boundary: failure - https://github.com/openclaw/openclaw/actions/runs/25782250945/job/75727683249
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25782250945/job/75727704384
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25782251050
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): failure - https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75728277248
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75729195480
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25782251050/job/75730044306

## Notes

Automatically requested by Full Release Validation 25782230301 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

