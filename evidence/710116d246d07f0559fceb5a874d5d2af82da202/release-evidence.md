# OpenClaw Release Evidence: 710116d246d07f0559fceb5a874d5d2af82da202

Generated: 2026-05-03T22:51:29.396Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `710116d246d07f0559fceb5a874d5d2af82da202` |
| Release ref input | `710116d246d07f0559fceb5a874d5d2af82da202` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `710116d246d07f0559fceb5a874d5d2af82da202` |
| Release ref SHA | `710116d246d07f0559fceb5a874d5d2af82da202` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/710116d246d0-1777846870312` | `710116d246d0` | 29m 58s | 47m 54s | 29m 29s | [25292484737](https://github.com/openclaw/openclaw/actions/runs/25292484737) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/710116d246d0-1777846870312` | `710116d246d0` | 6m 18s | 1h 30m 54s | 6m 14s | [25292492724](https://github.com/openclaw/openclaw/actions/runs/25292492724) | 3 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/710116d246d0-1777846870312` | `710116d246d0` | 28m 31s | 13h 27m 6s | 28m 27s | [25292492563](https://github.com/openclaw/openclaw/actions/runs/25292492563) | 39 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/710116d246d0-1777846870312` | `710116d246d0` | 1m 56s | 1m 48s | 7s | [25292547389](https://github.com/openclaw/openclaw/actions/runs/25292547389) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 29m 9s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292484737/job/74146260203) |
| 24m 20s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74146389147) |
| 24m 12s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-xai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74146389171) |
| 23m 51s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74146492470) |
| 23m 13s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74146389177) |
| 21m 34s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74146389156) |
| 21m 34s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-fireworks, Native live gateway pr... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74146389157) |
| 21m 9s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74146492487) |
| 21m 6s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live gateway Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74146492467) |
| 20m 44s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-deepseek, Native live gateway pro... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74146389160) |
| 20m 30s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74146389188) |
| 6m 44s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292484737/job/74146260201) |
| 6m 43s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292484737/job/74146260192) |
| 5m 51s | `normal-ci` | checks-node-agentic-control-plane-agent-chat | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292492724/job/74146278783) |
| 5m 51s | `normal-ci` | checks-node-agentic-control-plane-runtime | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292492724/job/74146278790) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 29m 29s | 29s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292484737/job/74147762482) |
| 28m 27s | 4s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74147728623) |
| 23m 22s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74147468599) |
| 6m 35s | 1m 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74146596884) |
| 6m 35s | 56s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74146596888) |
| 6m 35s | 1m 31s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74146596889) |
| 6m 35s | 2m 26s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74146596892) |
| 6m 34s | 16m 47s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74146596886) |
| 6m 27s | 1m 22s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74146596883) |
| 6m 25s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74146597016) |
| 6m 25s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74146597073) |
| 6m 14s | 3s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25292492724/job/74146582232) |
| 3m 56s | 3s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292492724/job/74146474000) |
| 2m 49s | 2m 15s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292484737/job/74146390885) |
| 2m 9s | 4s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25292492724/job/74146379492) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25292484737
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25292484737/job/74147762482
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25292492724
  - checks-fast-contracts-plugins-c: failure - https://github.com/openclaw/openclaw/actions/runs/25292492724/job/74146278656
  - check-dependencies: failure - https://github.com/openclaw/openclaw/actions/runs/25292492724/job/74146278680
  - checks-node-core-runtime-infra-process: failure - https://github.com/openclaw/openclaw/actions/runs/25292492724/job/74146278770
  - check: failure - https://github.com/openclaw/openclaw/actions/runs/25292492724/job/74146350797
  - checks-fast-contracts-plugins: failure - https://github.com/openclaw/openclaw/actions/runs/25292492724/job/74146359266
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25292492724/job/74146582232
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25292492563
  - Run repo/live E2E validation / validate_repo_e2e: failure - https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74146389020
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74146492487
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74146596886
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74147468599
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25292492563/job/74147728623

## Notes

Automatically requested by Full Release Validation 25292484737 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

