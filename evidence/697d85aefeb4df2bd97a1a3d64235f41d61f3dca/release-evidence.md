# OpenClaw Release Evidence: 697d85aefeb4df2bd97a1a3d64235f41d61f3dca

Generated: 2026-04-28T00:53:12.399Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `697d85aefeb4df2bd97a1a3d64235f41d61f3dca` |
| Release ref input | `697d85aefeb4df2bd97a1a3d64235f41d61f3dca` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `697d85aefeb4df2bd97a1a3d64235f41d61f3dca` |
| Release ref SHA | `697d85aefeb4df2bd97a1a3d64235f41d61f3dca` |
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

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `697d85aefeb4` | 1h 14m 49s | 1h 14m 42s | [25025387676](https://github.com/openclaw/openclaw/actions/runs/25025387676) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `697d85aefeb4` | 1h 13m 16s | 7h 41m 57s | [25025417185](https://github.com/openclaw/openclaw/actions/runs/25025417185) | 31 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1h 13m 52s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025387676/job/73295332587) |
| 1h 9m 9s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25025417185/job/73295692799) |
| 21m 46s | `release-checks` | live_and_e2e_release_checks / Docker E2E (bundled channels update B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025417185/job/73295853300) |
| 17m 28s | `release-checks` | cross_os_release_checks / Windows / installer fresh | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25025417185/job/73295692823) |
| 15m 56s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway-core, Native live gateway core, node scrip... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025417185/job/73295499797) |
| 13m 33s | `release-checks` | live_and_e2e_release_checks / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025417185/job/73295853312) |
| 13m 30s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-gateway-docker, Docker live gateway, pnpm test:docker:live-ga... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025417185/job/73295499823) |
| 13m 30s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025417185/job/73295692808) |
| 13m 2s | `release-checks` | live_and_e2e_release_checks / Docker E2E (plugins/runtime install A) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025417185/job/73295853246) |
| 12m 17s | `release-checks` | install_smoke_release_checks / install-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025417185/job/73295434648) |
| 12m 10s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-acp-bind-docker, Docker live ACP bind, pnpm test:docker:live-... | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25025417185/job/73295499804) |
| 44s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025387676/job/73295252746) |
| 6s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25025387676/job/73302709965) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25025387676/job/73295332697) |
| 0s | `full-release-validation` | Run post-publish Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25025387676/job/73295332709) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25025387676
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25025387676/job/73302709965
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25025417185
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-extensions-o-z, Native live plugins O-Z, node scripts/...: failure - https://github.com/openclaw/openclaw/actions/runs/25025417185/job/73295499795
  - live_and_e2e_release_checks / validate_live_provider_suites (live-cli-backend-docker, Docker live CLI backend, pnpm test:docker...: failure - https://github.com/openclaw/openclaw/actions/runs/25025417185/job/73295499800
  - live_and_e2e_release_checks / validate_live_provider_suites (live-acp-bind-docker, Docker live ACP bind, pnpm test:docker:live-...: failure - https://github.com/openclaw/openclaw/actions/runs/25025417185/job/73295499804
  - Run package acceptance / Telegram package acceptance / Run package Telegram E2E: failure - https://github.com/openclaw/openclaw/actions/runs/25025417185/job/73295664457
  - cross_os_release_checks / Windows / packaged upgrade: failure - https://github.com/openclaw/openclaw/actions/runs/25025417185/job/73295692799
  - cross_os_release_checks / Windows / installer fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25025417185/job/73295692823
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25025417185/job/73296739092
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25025417185/job/73302653640

## Notes

Automatically requested by Full Release Validation 25025387676 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

