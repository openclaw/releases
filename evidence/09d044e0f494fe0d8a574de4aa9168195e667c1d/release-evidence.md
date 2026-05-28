# OpenClaw Release Evidence: 09d044e0f494fe0d8a574de4aa9168195e667c1d

Generated: 2026-04-28T00:28:31.739Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `09d044e0f494fe0d8a574de4aa9168195e667c1d` |
| Release ref input | `09d044e0f494fe0d8a574de4aa9168195e667c1d` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `09d044e0f494fe0d8a574de4aa9168195e667c1d` |
| Release ref SHA | `09d044e0f494fe0d8a574de4aa9168195e667c1d` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 2 | 0 | 0 | 0 |
| Advisory | 1 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| pass | advisory | `full-release-validation` | Full Release Validation | `release/2026.4.26` | `09d044e0f494` | 21m 52s | 24m 55s | [25026336221](https://github.com/openclaw/openclaw/actions/runs/25026336221) | 0 |
| pass | blocking | `normal-ci` | CI | `release/2026.4.26` | `09d044e0f494` | 2m 35s | 53m 37s | [25026363590](https://github.com/openclaw/openclaw/actions/runs/25026363590) | 3 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.4.26` | `09d044e0f494` | 20m 31s | 4h 21m 40s | [25026364512](https://github.com/openclaw/openclaw/actions/runs/25026364512) | 22 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 21m 0s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026336221/job/73298215533) |
| 16m 59s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway, Native live gateway, node scripts/test-li... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026364512/job/73298365114) |
| 15m 44s | `release-checks` | live_and_e2e_release_checks / Docker E2E (plugins/runtime) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026364512/job/73298684881) |
| 13m 3s | `release-checks` | live_and_e2e_release_checks / Docker E2E (package/update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026364512/job/73298684888) |
| 9m 38s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-acp-bind-docker, Docker live ACP bind, pnpm test:docker:live-... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026364512/job/73298365142) |
| 9m 35s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-extensions-l-z, Native live plugins L-Z, node scripts/... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026364512/job/73298365133) |
| 9m 18s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026364512/job/73298567065) |
| 9m 12s | `release-checks` | install_smoke_release_checks / install-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026364512/job/73298309673) |
| 8m 47s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-cli-backend-docker, Docker live CLI backend, pnpm test:docker... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026364512/job/73298365183) |
| 8m 22s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026364512/job/73298567121) |
| 7m 37s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-gateway-docker, Docker live gateway, pnpm test:docker:live-ga... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026364512/job/73298365120) |
| 3m 10s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026336221/job/73298215548) |
| 2m 10s | `normal-ci` | checks-node-agentic-plugin-sdk | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026363590/job/73298250715) |
| 1m 56s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026363590/job/73298250488) |
| 1m 55s | `normal-ci` | checks-node-agentic-agents | success | [job](https://github.com/openclaw/openclaw/actions/runs/25026363590/job/73298250721) |

## Notes

Automatically requested by Full Release Validation 25026336221 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

