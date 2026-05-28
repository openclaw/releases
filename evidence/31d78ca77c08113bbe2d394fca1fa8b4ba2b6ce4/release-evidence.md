# OpenClaw Release Evidence: 31d78ca77c08113bbe2d394fca1fa8b4ba2b6ce4

Generated: 2026-05-10T11:37:01.531Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `31d78ca77c08113bbe2d394fca1fa8b4ba2b6ce4` |
| Release ref input | `31d78ca77c08113bbe2d394fca1fa8b4ba2b6ce4` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `31d78ca77c08113bbe2d394fca1fa8b4ba2b6ce4` |
| Release ref SHA | `31d78ca77c08113bbe2d394fca1fa8b4ba2b6ce4` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release/2026.5.10` | `31d78ca77c08` | 40m 23s | 40m 9s | 40m 10s | [25626898259](https://github.com/openclaw/openclaw/actions/runs/25626898259) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.5.10` | `31d78ca77c08` | 39m 7s | 6h 19m 46s | 39m 5s | [25626907130](https://github.com/openclaw/openclaw/actions/runs/25626907130) | 48 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 39m 47s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25626898259/job/75223554142) |
| 33m 14s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75223836698) |
| 30m 39s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75223950880) |
| 30m 28s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75223688630) |
| 8m 59s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75223688728) |
| 8m 26s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75223788825) |
| 7m 20s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75223788811) |
| 7m 20s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75223950902) |
| 7m 18s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75223959683) |
| 7m 12s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75223688758) |
| 7m 7s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75223959692) |
| 12s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25626898259/job/75225653643) |
| 10s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25626898259/job/75223539188) |
| 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25626898259/job/75223554301) |
| 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25626898259/job/75223554346) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 40m 10s | 12s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25626898259/job/75225653643) |
| 39m 5s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75225620753) |
| 15m 7s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75224342831) |
| 7m 50s | 5m 42s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.7) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75223959675) |
| 7m 50s | 1m 37s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75223959690) |
| 7m 49s | 1m 7s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75223959671) |
| 7m 49s | 59s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75223959674) |
| 7m 49s | 1m 19s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75223959681) |
| 7m 49s | 2m 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75223959682) |
| 7m 49s | 4m 55s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75223959686) |
| 7m 49s | 5m 43s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.6) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75223959689) |
| 21s | 39m 47s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25626898259/job/75223554142) |
| 19s | 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25626898259/job/75223554301) |
| 19s | 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25626898259/job/75223554346) |
| 19s | 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25626898259/job/75223554352) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25626898259
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25626898259/job/75225653643
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25626907130
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75223950880
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25626907130/job/75225620753

## Notes

Automatically requested by Full Release Validation 25626898259 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

