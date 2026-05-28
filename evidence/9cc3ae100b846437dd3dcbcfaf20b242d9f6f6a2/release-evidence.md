# OpenClaw Release Evidence: 9cc3ae100b846437dd3dcbcfaf20b242d9f6f6a2

Generated: 2026-05-04T16:42:37.742Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `9cc3ae100b846437dd3dcbcfaf20b242d9f6f6a2` |
| Release ref input | `9cc3ae100b846437dd3dcbcfaf20b242d9f6f6a2` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `9cc3ae100b846437dd3dcbcfaf20b242d9f6f6a2` |
| Release ref SHA | `9cc3ae100b846437dd3dcbcfaf20b242d9f6f6a2` |
| Runs at release SHA | none |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release/2026.5.4` | `8f7399e9e9de` | 2h 34m 41s (+19m 37s) | 1h 35m 54s (-50m 51s) | 2h 34m 5s | [25323724103](https://github.com/openclaw/openclaw/actions/runs/25323724103) | 0 |
| fail | blocking | `normal-ci` | CI | `release/2026.5.4` | `b70dbe32d031` | 6m 22s (+2m 7s) | 1h 19m 20s (-3m 1s) | 6m 19s | [25327866761](https://github.com/openclaw/openclaw/actions/runs/25327866761) | 1 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.5.4` | `b70dbe32d031` | 1h 12m 8s (-1h 1m 13s) | 8h 33m 8s (-1h 53m 16s) | 1h 12m 3s | [25327861937](https://github.com/openclaw/openclaw/actions/runs/25327861937) | 40 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 12m 28s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25323724103/job/74253276169) |
| 42m 17s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25327861937/job/74254234937) |
| 23m 16s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25327861937/job/74255368565) |
| 23m 6s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25327861937/job/74253709974) |
| 20m 29s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25327861937/job/74254121438) |
| 19m 46s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25327861937/job/74253709983) |
| 19m 40s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25327861937/job/74254122725) |
| 19m 15s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-smoke, Native live ga... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25327861937/job/74253709951) |
| 18m 19s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-smoke, native-live-src-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25327861937/job/74253709921) |
| 17m 53s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25327861937/job/74253709925) |
| 16m 31s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25327861937/job/74254121422) |
| 15m 58s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25323724103/job/74253276012) |
| 6m 43s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25323724103/job/74253275984) |
| 3m 44s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25327866761/job/74253363574) |
| 2m 52s | `normal-ci` | checks-node-core-runtime-infra-state | success | [job](https://github.com/openclaw/openclaw/actions/runs/25327866761/job/74253364053) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 2h 34m 5s | 35s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25323724103/job/74264493995) |
| 1h 21m 41s | 6m 43s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25323724103/job/74253275984) |
| 1h 21m 34s | 15m 58s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25323724103/job/74253276012) |
| 1h 21m 34s | 1h 12m 28s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25323724103/job/74253276169) |
| 1h 21m 32s |  | `full-release-validation` | Run package Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25323724103/job/74253277050) |
| 1h 21m 31s | 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25323724103/job/74253276471) |
| 1h 21m 21s | 10s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25323724103/job/74253240982) |
| 1h 12m 3s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25327861937/job/74264417203) |
| 1h 11m 47s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25327861937/job/74264392561) |
| 48m 28s | 1m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25327861937/job/74255372581) |
| 48m 27s | 2m 27s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install F) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25327861937/job/74255219660) |
| 48m 27s | 23m 16s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25327861937/job/74255368565) |
| 48m 27s | 1m 55s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25327861937/job/74255368590) |
| 48m 27s | 2m 22s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25327861937/job/74255368694) |
| 48m 27s | 1m 55s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25327861937/job/74255375123) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `release-checks` | 2h 13m 21s | 1h 12m 8s | -1h 1m 13s | -1h 53m 16s |
| `full-release-validation` | 2h 15m 4s | 2h 34m 41s | +19m 37s | -50m 51s |
| `normal-ci` | 4m 15s | 6m 22s | +2m 7s | -3m 1s |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25323724103
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25323724103/job/74264493995
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25327866761
  - build-artifacts: failure - https://github.com/openclaw/openclaw/actions/runs/25327866761/job/74253363301
  - build-smoke: failure - https://github.com/openclaw/openclaw/actions/runs/25327866761/job/74253513551
  - check-additional: failure - https://github.com/openclaw/openclaw/actions/runs/25327866761/job/74254021823
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25327866761/job/74254317612
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25327861937
  - Run QA Lab live Slack lane: failure - https://github.com/openclaw/openclaw/actions/runs/25327861937/job/74253521964
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25327861937/job/74264417203

## Notes

Automatically requested by Full Release Validation 25323724103 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

