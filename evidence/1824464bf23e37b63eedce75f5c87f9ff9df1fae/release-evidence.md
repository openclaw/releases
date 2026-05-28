# OpenClaw Release Evidence: 1824464bf23e37b63eedce75f5c87f9ff9df1fae

Generated: 2026-05-12T17:45:30.890Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `1824464bf23e37b63eedce75f5c87f9ff9df1fae` |
| Release ref input | `1824464bf23e37b63eedce75f5c87f9ff9df1fae` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `1824464bf23e37b63eedce75f5c87f9ff9df1fae` |
| Release ref SHA | `1824464bf23e37b63eedce75f5c87f9ff9df1fae` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 2 | 0 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/1824464bf23e-1778598997209` | `1824464bf23e` | 2h 28m 2s | 6h 20m 41s | 2h 27m 7s | [25743872489](https://github.com/openclaw/openclaw/actions/runs/25743872489) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/1824464bf23e-1778598997209` | `1824464bf23e` | 1m 22s | 1h 15m 26s | 2h 0m 24s | [25743900011](https://github.com/openclaw/openclaw/actions/runs/25743900011) | 4 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/1824464bf23e-1778598997209` | `1824464bf23e` | 5s | 4h 18m 21s | 2h 27m 29s | [25743904575](https://github.com/openclaw/openclaw/actions/runs/25743904575) | 34 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/1824464bf23e-1778598997209` | `1824464bf23e` | 1h 1m 6s | 3m 14s | 57m 51s | [25744087899](https://github.com/openclaw/openclaw/actions/runs/25744087899) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 2h 26m 37s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25743872489/job/75601642940) |
| 1h 24m 37s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25743872489/job/75601642862) |
| 1h 23m 30s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25743872489/job/75601643013) |
| 1h 1m 38s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25743872489/job/75602325515) |
| 16m 47s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25743904575/job/75629995784) |
| 8m 41s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-deepseek-glm, native-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25743904575/job/75629994488) |
| 7m 54s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25743904575/job/75629998867) |
| 7m 39s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openrouter, Native live gateway p... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25743904575/job/75629995225) |
| 7m 27s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25743904575/job/75629998300) |
| 6m 28s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25743904575/job/75629995713) |
| 6m 10s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25743904575/job/75629995172) |
| 5m 35s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-anthropic-opus, native-live-src-g... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25743904575/job/75629993919) |
| 5m 20s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-kimi, native-live-src... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25743904575/job/75629994793) |
| 5m 18s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-google, Native live gateway profi... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25743904575/job/75629994013) |
| 3m 56s | `normal-ci` | android-test-third-party | success | [job](https://github.com/openclaw/openclaw/actions/runs/25743900011/job/75624815450) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 2h 27m 29s |  | `release-checks` | Run package acceptance / Docker product acceptance / validate_special_e2e | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25743904575/job/75629995894) |
| 2h 27m 29s |  | `release-checks` | Run package acceptance / Docker product acceptance / validate_repo_e2e | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25743904575/job/75629995905) |
| 2h 27m 29s |  | `release-checks` | Run package acceptance / Docker product acceptance / prepare_live_test_image | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25743904575/job/75629996123) |
| 2h 27m 29s |  | `release-checks` | Run package acceptance / Docker product acceptance / Live media suites (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25743904575/job/75629996149) |
| 2h 27m 29s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker live models (selected providers) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25743904575/job/75629996358) |
| 2h 27m 29s |  | `release-checks` | Run package acceptance / Docker product acceptance / validate_release_live_cache | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25743904575/job/75629996696) |
| 2h 27m 29s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker live models (${{ matrix.provider_label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25743904575/job/75629996740) |
| 2h 27m 29s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker live suites (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25743904575/job/75629996834) |
| 2h 27m 29s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25743904575/job/75629997595) |
| 2h 27m 29s |  | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25743904575/job/75629997900) |
| 2h 27m 7s | 54s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25743872489/job/75629822622) |
| 2h 0m 24s | 3s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25743900011/job/75625022126) |
| 2h 0m 10s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25743900011/job/75624992397) |
| 1h 59m 12s | 54s | `normal-ci` | checks-node-agentic-control-plane-agent-chat | success | [job](https://github.com/openclaw/openclaw/actions/runs/25743900011/job/75624818439) |
| 1h 59m 12s | 42s | `normal-ci` | checks-node-agentic-control-plane-auth-node | success | [job](https://github.com/openclaw/openclaw/actions/runs/25743900011/job/75624818884) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25743872489
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25743872489/job/75629822622

## Notes

Automatically requested by Full Release Validation 25743872489 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

