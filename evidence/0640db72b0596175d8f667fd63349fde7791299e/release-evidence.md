# OpenClaw Release Evidence: 0640db72b0596175d8f667fd63349fde7791299e

Generated: 2026-05-01T21:53:31.884Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `0640db72b0596175d8f667fd63349fde7791299e` |
| Release ref input | `0640db72b0596175d8f667fd63349fde7791299e` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `0640db72b0596175d8f667fd63349fde7791299e` |
| Release ref SHA | `0640db72b0596175d8f667fd63349fde7791299e` |
| Runs at release SHA | `full-release-validation` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `0640db72b059` | 34m 11s | 40m 41s | 33m 55s | [25233625542](https://github.com/openclaw/openclaw/actions/runs/25233625542) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `deeec3117c0d` | 3m 28s | 1h 4m 7s | 3m 23s | [25233639151](https://github.com/openclaw/openclaw/actions/runs/25233639151) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `deeec3117c0d` | 33m 6s | 6h 19m 10s | 33m 4s | [25233639851](https://github.com/openclaw/openclaw/actions/runs/25233639851) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 33m 28s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25233625542/job/73994801327) |
| 29m 55s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995060737) |
| 27m 31s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995060766) |
| 26m 21s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995060723) |
| 26m 13s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995060763) |
| 25m 56s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995060721) |
| 24m 31s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995060735) |
| 24m 7s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-minimax-qwen, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995060768) |
| 23m 36s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-mimo, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995060830) |
| 23m 27s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995060772) |
| 21m 20s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | success | [job](https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995060402) |
| 3m 40s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25233625542/job/73994801352) |
| 3m 10s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25233625542/job/73994801356) |
| 3m 5s | `normal-ci` | checks-node-auto-reply-reply-dispatch | success | [job](https://github.com/openclaw/openclaw/actions/runs/25233639151/job/73994849145) |
| 2m 42s | `normal-ci` | checks-node-core-runtime-infra | success | [job](https://github.com/openclaw/openclaw/actions/runs/25233639151/job/73994849098) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 33m 55s | 15s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25233625542/job/73998429497) |
| 33m 4s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73998384163) |
| 5m 46s | 0s | `release-checks` | Run repo/live E2E validation / Docker live models (${{ matrix.provider_label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995476449) |
| 5m 46s | 0s | `release-checks` | Run repo/live E2E validation / Docker live models (selected providers) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995476624) |
| 5m 46s | 0s | `release-checks` | Run repo/live E2E validation / Docker live suites (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995476829) |
| 5m 43s |  | `release-checks` | install_smoke_release_checks / installer_smoke | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995470638) |
| 5m 43s |  | `release-checks` | install_smoke_release_checks / root_dockerfile_smokes | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995470703) |
| 5m 43s |  | `release-checks` | install_smoke_release_checks / bun_global_install_smoke | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995470837) |
| 3m 23s | 4s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25233639151/job/73995202385) |
| 3m 20s | 0s | `release-checks` | cross_os_release_checks | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995204797) |
| 3m 20s | 0s | `release-checks` | Run package acceptance | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995204963) |
| 3m 20s | 0s | `release-checks` | Run Docker release-path validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995205032) |
| 2m 16s | 3s | `normal-ci` | check-additional | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25233639151/job/73995065859) |
| 1m 49s | 4s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25233639151/job/73995023298) |
| 1m 21s | 1m 41s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25233639151/job/73994848970) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25233625542
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25233625542/job/73998429497
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25233639151
  - build-artifacts: failure - https://github.com/openclaw/openclaw/actions/runs/25233639151/job/73994848908
  - checks-fast-contracts-plugins-c: failure - https://github.com/openclaw/openclaw/actions/runs/25233639151/job/73994848922
  - checks-node-compat-node22: failure - https://github.com/openclaw/openclaw/actions/runs/25233639151/job/73994848969
  - build-smoke: failure - https://github.com/openclaw/openclaw/actions/runs/25233639151/job/73994924054
  - checks-fast-contracts-plugins: failure - https://github.com/openclaw/openclaw/actions/runs/25233639151/job/73994955547
  - check-additional: failure - https://github.com/openclaw/openclaw/actions/runs/25233639151/job/73995065859
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25233639151/job/73995202385
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25233639851
  - Run QA Lab live Telegram lane: failure - https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73994953980
  - Run QA Lab live Matrix lane: failure - https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73994954001
  - Run QA Lab parity lane (baseline): failure - https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73994954005
  - Prepare release package artifact: failure - https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73994954034
  - Run QA Lab parity lane (candidate): failure - https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73994954042
  - install_smoke_release_checks / root_dockerfile_image: failure - https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73994971451
  - Run repo/live E2E validation / validate_repo_e2e: failure - https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995060358
  - Run repo/live E2E validation / validate_special_e2e (openshell-e2e, OpenShell repo E2E, pnpm test:e2e:openshell, 120, true, false): failure - https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995060366
  - Run repo/live E2E validation / validate_special_e2e (openai-ws-stream-live-e2e, OpenAI WebSocket live E2E, pnpm test:e2e src/age...: failure - https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995060371
  - Run repo/live E2E validation / prepare_live_test_image: failure - https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73995060382
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25233639851/job/73998384163

## Notes

Automatically requested by Full Release Validation 25233625542 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

