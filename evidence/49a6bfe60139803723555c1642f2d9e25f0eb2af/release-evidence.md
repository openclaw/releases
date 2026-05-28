# OpenClaw Release Evidence: 49a6bfe60139803723555c1642f2d9e25f0eb2af

Generated: 2026-04-29T12:09:56.986Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `49a6bfe60139803723555c1642f2d9e25f0eb2af` |
| Release ref input | `49a6bfe60139803723555c1642f2d9e25f0eb2af` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `49a6bfe60139803723555c1642f2d9e25f0eb2af` |
| Release ref SHA | `49a6bfe60139803723555c1642f2d9e25f0eb2af` |
| Runs at release SHA | `full-release-validation` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 0 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `49a6bfe60139` | 7m 55s | 7m 45s | [25107657444](https://github.com/openclaw/openclaw/actions/runs/25107657444) | 0 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `14249827928e` | 7m 7s | 1h 43m 58s | [25107675913](https://github.com/openclaw/openclaw/actions/runs/25107675913) | 13 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 7m 23s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25107657444/job/73572974278) |
| 6m 20s | `release-checks` | Run QA Lab parity lane (baseline) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25107675913/job/73573149131) |
| 5m 36s | `release-checks` | Run QA Lab live Matrix lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/25107675913/job/73573149111) |
| 5m 32s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25107675913/job/73573269789) |
| 5m 32s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-opencode-go-smoke, Native live ga... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25107675913/job/73573270168) |
| 5m 29s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-minimax, Native live gateway prof... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25107675913/job/73573270063) |
| 5m 28s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-test, Native live test harnesses, node .release-harnes... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25107675913/job/73573270018) |
| 5m 17s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-gateway-profiles-openai, Native live gateway profi... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25107675913/job/73573270038) |
| 4m 12s | `release-checks` | install_smoke_release_checks / docker-e2e-fast | success | [job](https://github.com/openclaw/openclaw/actions/runs/25107675913/job/73573187231) |
| 4m 10s | `release-checks` | Run repo/live E2E validation / validate_live_provider_suites (native-live-src-agents, Native live agents, node .release-harness/... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25107675913/job/73573270009) |
| 3m 10s | `release-checks` | Run repo/live E2E validation / prepare_live_test_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/25107675913/job/73573269762) |
| 12s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25107657444/job/73572934850) |
| 10s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25107657444/job/73574088745) |
| 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25107657444/job/73572974651) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25107657444/job/73572974771) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25107657444
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25107657444/job/73572974278
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25107657444/job/73574088745

## Notes

Automatically requested by Full Release Validation 25107657444 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

