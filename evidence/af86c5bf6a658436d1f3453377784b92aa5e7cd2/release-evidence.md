# OpenClaw Release Evidence: af86c5bf6a658436d1f3453377784b92aa5e7cd2

Generated: 2026-05-11T22:41:33.053Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `af86c5bf6a658436d1f3453377784b92aa5e7cd2` |
| Release ref input | `af86c5bf6a658436d1f3453377784b92aa5e7cd2` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `af86c5bf6a658436d1f3453377784b92aa5e7cd2` |
| Release ref SHA | `af86c5bf6a658436d1f3453377784b92aa5e7cd2` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 1 | 0 | 2 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/af86c5bf6a65-1778521175357` | `af86c5bf6a65` | 5h 1m 22s | 15h 7m 13s | 5h 1m 2s | [25686775279](https://github.com/openclaw/openclaw/actions/runs/25686775279) | 1 |
| running | blocking | `normal-ci` | CI | `release-ci/af86c5bf6a65-1778521175357` | `af86c5bf6a65` | 18s | 56m 8s | 4h 56m 51s | [25686812037](https://github.com/openclaw/openclaw/actions/runs/25686812037) | 1 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/af86c5bf6a65-1778521175357` | `af86c5bf6a65` | 1m 34s | 29m 47s | 4h 58m 16s | [25686812539](https://github.com/openclaw/openclaw/actions/runs/25686812539) | 11 |
| fail | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/af86c5bf6a65-1778521175357` | `af86c5bf6a65` | 2h 0m 30s | 2h 0m 27s | 2s | [25686999176](https://github.com/openclaw/openclaw/actions/runs/25686999176) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 5h 0m 23s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25686775279/job/75412589374) |
| 4h 1m 6s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25686775279/job/75412589317) |
| 4h 1m 2s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25686775279/job/75412589360) |
| 2h 0m 45s | `full-release-validation` | Run package Telegram E2E | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25686775279/job/75413231686) |
| 2h 0m 27s | `postpublish-telegram` | Run package Telegram E2E | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25686999176/job/75413268548) |
| 4m 28s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25686812539/job/75413620307) |
| 3m 24s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25686775279/job/75412589302) |
| 3m 13s | `release-checks` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25686812539/job/75412895119) |
| 2m 53s | `release-checks` | Run QA Lab live Telegram lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/25686812539/job/75412895141) |
| 2m 43s | `release-checks` | Run QA Lab live Matrix lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/25686812539/job/75412895143) |
| 2m 30s | `release-checks` | Run QA Lab parity lane (baseline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25686812539/job/75412895193) |
| 2m 25s | `release-checks` | install_smoke_release_checks / root_dockerfile_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/25686812539/job/75412926909) |
| 2m 24s | `release-checks` | Run QA Lab parity lane (candidate) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25686812539/job/75412895190) |
| 2m 19s | `normal-ci` | checks-node-core-fast | success | [job](https://github.com/openclaw/openclaw/actions/runs/25686812037/job/75412664776) |
| 2m 7s | `normal-ci` | checks-node-core-runtime-shared | success | [job](https://github.com/openclaw/openclaw/actions/runs/25686812037/job/75412664845) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 5h 1m 2s | 19s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25686775279/job/75462635073) |
| 4h 58m 16s |  | `release-checks` | Run QA Lab parity report |  | [job](https://github.com/openclaw/openclaw/actions/runs/25686812539/job/75462378073) |
| 4h 58m 11s |  | `release-checks` | install_smoke_release_checks / root_dockerfile_smokes |  | [job](https://github.com/openclaw/openclaw/actions/runs/25686812539/job/75462367221) |
| 4h 58m 11s |  | `release-checks` | install_smoke_release_checks / bun_global_install_smoke |  | [job](https://github.com/openclaw/openclaw/actions/runs/25686812539/job/75462367224) |
| 4h 58m 11s |  | `release-checks` | install_smoke_release_checks / installer_smoke |  | [job](https://github.com/openclaw/openclaw/actions/runs/25686812539/job/75462367240) |
| 4h 56m 51s | 2s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25686812037/job/75462174048) |
| 4h 56m 40s | 2s | `normal-ci` | checks-fast-contracts-plugins | success | [job](https://github.com/openclaw/openclaw/actions/runs/25686812037/job/75462147856) |
| 4h 55m 49s | 2m 6s | `normal-ci` | check-additional-boundaries-a | success | [job](https://github.com/openclaw/openclaw/actions/runs/25686812037/job/75412664340) |
| 4h 55m 48s | 1m 5s | `normal-ci` | check-additional-extension-bundled | success | [job](https://github.com/openclaw/openclaw/actions/runs/25686812037/job/75412664327) |
| 4h 55m 48s | 49s | `normal-ci` | checks-node-core-runtime-infra-process | success | [job](https://github.com/openclaw/openclaw/actions/runs/25686812037/job/75412664809) |
| 4h 55m 47s | 29s | `normal-ci` | check-additional-boundaries-b | success | [job](https://github.com/openclaw/openclaw/actions/runs/25686812037/job/75412664272) |
| 4h 55m 47s | 1m 5s | `normal-ci` | check-additional-extension-package-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25686812037/job/75412664348) |
| 4h 55m 47s | 1m 2s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25686812037/job/75412664373) |
| 4h 55m 47s | 1m 25s | `normal-ci` | android-test-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25686812037/job/75412664409) |
| 4h 55m 47s | 51s | `normal-ci` | checks-node-agentic-control-plane-runtime | success | [job](https://github.com/openclaw/openclaw/actions/runs/25686812037/job/75412664820) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25686775279
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25686775279/job/75412589317
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25686775279/job/75412589360
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25686775279/job/75412589374
  - Run package Telegram E2E: cancelled - https://github.com/openclaw/openclaw/actions/runs/25686775279/job/75413231686
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25686775279/job/75462635073
- `postpublish-telegram`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25686999176
  - Run package Telegram E2E: cancelled - https://github.com/openclaw/openclaw/actions/runs/25686999176/job/75413268548

## Notes

Automatically requested by Full Release Validation 25686775279 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

