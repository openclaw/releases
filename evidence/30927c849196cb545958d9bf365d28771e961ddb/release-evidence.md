# OpenClaw Release Evidence: 30927c849196cb545958d9bf365d28771e961ddb

Generated: 2026-05-06T00:09:02.654Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `30927c849196cb545958d9bf365d28771e961ddb` |
| Release ref input | `30927c849196cb545958d9bf365d28771e961ddb` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `30927c849196cb545958d9bf365d28771e961ddb` |
| Release ref SHA | `30927c849196cb545958d9bf365d28771e961ddb` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/30927c849196-1778022269996` | `30927c849196` | 1h 4m 14s | 1h 21m 29s | 1h 3m 37s | [25407109310](https://github.com/openclaw/openclaw/actions/runs/25407109310) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/30927c849196-1778022269996` | `30927c849196` | 4m 2s | 1h 18m 54s | 3m 58s | [25407123358](https://github.com/openclaw/openclaw/actions/runs/25407123358) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/30927c849196-1778022269996` | `30927c849196` | 1h 2m 50s | 12h 50m 9s | 1h 2m 46s | [25407127012](https://github.com/openclaw/openclaw/actions/runs/25407127012) | 40 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/30927c849196-1778022269996` | `30927c849196` | 1m 47s | 1m 43s | 3s | [25407214544](https://github.com/openclaw/openclaw/actions/runs/25407214544) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 3m 2s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407109310/job/74520521251) |
| 1h 0m 18s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74520805622) |
| 32m 19s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74521034257) |
| 28m 40s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74521318888) |
| 25m 3s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74520805859) |
| 23m 9s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74520805833) |
| 22m 25s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74520805862) |
| 22m 3s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74520805927) |
| 20m 52s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74520806280) |
| 19m 22s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74520805897) |
| 19m 6s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74521033097) |
| 8m 43s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407109310/job/74520521276) |
| 4m 17s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407109310/job/74520521262) |
| 3m 40s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407123358/job/74520557094) |
| 2m 54s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407123358/job/74520557095) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 1h 3m 37s | 36s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25407109310/job/74526994472) |
| 1h 2m 46s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74526974186) |
| 36m 12s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74524392467) |
| 14m 9s | 39s | `release-checks` | install_smoke_release_checks / root_dockerfile_smokes | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74521675543) |
| 14m 9s | 2m 25s | `release-checks` | install_smoke_release_checks / bun_global_install_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74521675546) |
| 14m 8s | 4m 20s | `release-checks` | install_smoke_release_checks / installer_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74521675523) |
| 7m 30s | 1m 46s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74521283661) |
| 7m 30s | 1m 40s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74521283669) |
| 7m 30s | 1m 36s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74521283676) |
| 7m 30s | 1m 28s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install G) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74521283681) |
| 7m 30s | 1m 13s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74521283682) |
| 3m 58s | 3s | `normal-ci` | check-additional | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25407123358/job/74520958872) |
| 3m 2s | 4s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25407123358/job/74520848102) |
| 2m 59s | 2m 19s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407109310/job/74520797283) |
| 2m 36s | 2s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25407123358/job/74520803948) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25407109310
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25407109310/job/74526994472
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25407123358
  - check-lint: failure - https://github.com/openclaw/openclaw/actions/runs/25407123358/job/74520557024
  - check-additional-extension-bundled: failure - https://github.com/openclaw/openclaw/actions/runs/25407123358/job/74520557102
  - checks-node-core-runtime-infra-process: failure - https://github.com/openclaw/openclaw/actions/runs/25407123358/job/74520557346
  - check: failure - https://github.com/openclaw/openclaw/actions/runs/25407123358/job/74520726044
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25407123358/job/74520848102
  - check-additional: failure - https://github.com/openclaw/openclaw/actions/runs/25407123358/job/74520958872
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25407127012
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74520805622
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74521033083
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin): failure - https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74521318880
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74524392467
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25407127012/job/74526974186

## Notes

Automatically requested by Full Release Validation 25407109310 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

