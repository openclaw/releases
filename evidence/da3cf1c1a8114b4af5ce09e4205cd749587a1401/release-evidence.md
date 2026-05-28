# OpenClaw Release Evidence: da3cf1c1a8114b4af5ce09e4205cd749587a1401

Generated: 2026-04-27T23:59:43.576Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `da3cf1c1a8114b4af5ce09e4205cd749587a1401` |
| Release ref input | `da3cf1c1a8114b4af5ce09e4205cd749587a1401` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `da3cf1c1a8114b4af5ce09e4205cd749587a1401` |
| Release ref SHA | `da3cf1c1a8114b4af5ce09e4205cd749587a1401` |
| Runs at release SHA | `full-release-validation` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `da3cf1c1a811` | 7m 52s | 7m 43s | [25025837093](https://github.com/openclaw/openclaw/actions/runs/25025837093) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `7aeb7c2a14f2` | 6m 19s | 2h 2m 1s | [25025869470](https://github.com/openclaw/openclaw/actions/runs/25025869470) | 11 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 6m 49s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025837093/job/73296734200) |
| 4m 28s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-codex-harness-docker, Docker live Codex harness, pnpm test:do... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296887114) |
| 4m 25s | `release-checks` | live_and_e2e_release_checks / Docker live models (OpenAI) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296886968) |
| 4m 19s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-cli-backend-docker, Docker live CLI backend, pnpm test:docker... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296887122) |
| 4m 12s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway-profiles-other, Native live gateway profil... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296887084) |
| 4m 11s | `release-checks` | live_and_e2e_release_checks / Docker live models (Z.ai) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296886961) |
| 4m 11s | `release-checks` | live_and_e2e_release_checks / Docker live models (xAI) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296886980) |
| 4m 10s | `release-checks` | live_and_e2e_release_checks / Docker live models (MiniMax) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296886944) |
| 4m 10s | `release-checks` | live_and_e2e_release_checks / Docker live models (OpenCode) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296886948) |
| 4m 10s | `release-checks` | live_and_e2e_release_checks / Docker live models (Fireworks) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296886979) |
| 4m 9s | `release-checks` | live_and_e2e_release_checks / Docker live models (OpenRouter) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296886938) |
| 47s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025837093/job/73296652333) |
| 7s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25025837093/job/73297395274) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25025837093/job/73296734366) |
| 0s | `full-release-validation` | Run post-publish Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25025837093/job/73296734482) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25025837093
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25025837093/job/73297395274
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470
  - live_and_e2e_release_checks / Docker live models (OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296886938
  - live_and_e2e_release_checks / Docker live models (Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296886941
  - live_and_e2e_release_checks / Docker live models (Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296886943
  - live_and_e2e_release_checks / Docker live models (MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296886944
  - live_and_e2e_release_checks / Docker live models (OpenCode): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296886948
  - live_and_e2e_release_checks / Docker live models (Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296886961
  - live_and_e2e_release_checks / Docker live models (OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296886968
  - live_and_e2e_release_checks / Docker live models (Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296886979
  - live_and_e2e_release_checks / Docker live models (xAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296886980
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-agents, Native live agents, node scripts/test-live...: failure - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296887045
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-test, Native live test harnesses, node scripts/test-li...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296887048
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296887054
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-extensions-media-audio, Native live media audio plugin...: failure - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296887057
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296887058
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296887069
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic, Native live gateway pr...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296887079
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway-profiles-other, Native live gateway profil...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296887084
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296887087
  - live_and_e2e_release_checks / validate_live_provider_suites (live-codex-harness-docker, Docker live Codex harness, pnpm test:do...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296887114
  - live_and_e2e_release_checks / validate_live_provider_suites (live-gateway-docker, Docker live gateway, pnpm test:docker:live-ga...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296887116
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-extensions-media-music, Native live media music plugin...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296887118
  - live_and_e2e_release_checks / validate_live_provider_suites (live-cli-backend-docker, Docker live CLI backend, pnpm test:docker...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296887122
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-extensions-media-video, Native live media video plugin...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296887135
  - live_and_e2e_release_checks / validate_live_provider_suites (live-acp-bind-docker, Docker live ACP bind, pnpm test:docker:live-...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73296887154
  - live_and_e2e_release_checks / Docker E2E (core): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73297212946
  - live_and_e2e_release_checks / Docker E2E (package/update OpenAI install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73297212952
  - live_and_e2e_release_checks / Docker E2E (bundled channels core): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73297212954
  - live_and_e2e_release_checks / Docker E2E (bundled channels contracts): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73297212959
  - live_and_e2e_release_checks / Docker E2E (package/update core): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73297212960
  - live_and_e2e_release_checks / Docker E2E (package/update Anthropic install): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73297212962
  - live_and_e2e_release_checks / Docker E2E (plugins/runtime install A): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73297212965
  - live_and_e2e_release_checks / Docker E2E (plugins/runtime core): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73297212969
  - live_and_e2e_release_checks / Docker E2E (plugins/runtime install B): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73297212986
  - live_and_e2e_release_checks / Docker E2E (bundled channels update B): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73297212995
  - live_and_e2e_release_checks / Docker E2E (bundled channels update A): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73297212999
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25025869470/job/73297347943

## Notes

Automatically requested by Full Release Validation 25025837093 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

