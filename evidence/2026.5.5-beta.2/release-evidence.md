# OpenClaw Release Evidence: 2026.5.5-beta.2

Generated: 2026-05-06T01:49:49.768Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `2026.5.5-beta.2` |
| Release ref input | `v2026.5.5-beta.2` |
| Release ref status | resolved |
| Release ref kind | `tag` |
| Release ref name | `v2026.5.5-beta.2` |
| Release ref SHA | `e82082195026515a4c1404f35c2dce991f995314` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 0 | 0 | 2 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release/2026.5.5` | `e82082195026` | 2m 57s | 6m 25s | 2m 38s | [25412078910](https://github.com/openclaw/openclaw/actions/runs/25412078910) | 0 |
| running | blocking | `normal-ci` | CI | `release/2026.5.5` | `e82082195026` | 2m 54s | 1h 9m 37s | 2m 54s | [25412092460](https://github.com/openclaw/openclaw/actions/runs/25412092460) | 4 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.5.5` | `e82082195026` | 1m 45s | 4m 37s | 1m 45s | [25412095596](https://github.com/openclaw/openclaw/actions/runs/25412095596) | 2 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 2m 34s | `normal-ci` | checks-node-core-runtime-infra-state | success | [job](https://github.com/openclaw/openclaw/actions/runs/25412092460/job/74535886713) |
| 2m 3s | `normal-ci` | checks-node-core-runtime-infra-process | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25412092460/job/74535886704) |
| 2m 2s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25412078910/job/74535854181) |
| 2m 1s | `normal-ci` | checks-node-core-runtime-shared | success | [job](https://github.com/openclaw/openclaw/actions/runs/25412092460/job/74535886730) |
| 1m 59s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25412092460/job/74535886475) |
| 1m 57s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25412078910/job/74535854187) |
| 1m 56s | `full-release-validation` | Run plugin prerelease validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25412078910/job/74535854182) |
| 1m 49s | `normal-ci` | android-build-play | success | [job](https://github.com/openclaw/openclaw/actions/runs/25412092460/job/74535886495) |
| 1m 42s | `normal-ci` | checks-node-agentic-commands-status-tools | success | [job](https://github.com/openclaw/openclaw/actions/runs/25412092460/job/74535886758) |
| 1m 41s | `normal-ci` | checks-node-auto-reply-reply-agent-runner | success | [job](https://github.com/openclaw/openclaw/actions/runs/25412092460/job/74535886745) |
| 1m 33s | `release-checks` | Run QA Lab parity lane (candidate) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25412095596/job/74535963410) |
| 1m 30s | `normal-ci` | check-additional-extension-package-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25412092460/job/74535886568) |
| 1m 29s | `normal-ci` | checks-fast-contracts-channels-b | success | [job](https://github.com/openclaw/openclaw/actions/runs/25412092460/job/74535886418) |
| 1m 29s | `normal-ci` | check-additional-extension-bundled | success | [job](https://github.com/openclaw/openclaw/actions/runs/25412092460/job/74535886557) |
| 1m 4s | `release-checks` | resolve_target | success | [job](https://github.com/openclaw/openclaw/actions/runs/25412095596/job/74535875127) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 2m 54s |  | `normal-ci` | checks-node-core |  | [job](https://github.com/openclaw/openclaw/actions/runs/25412092460/job/74536090625) |
| 2m 38s | 18s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25412078910/job/74536019687) |
| 1m 57s | 2s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25412092460/job/74536006053) |
| 1m 57s | 2s | `normal-ci` | checks-fast-contracts-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25412092460/job/74536014398) |
| 1m 53s | 3s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25412092460/job/74536001826) |
| 1m 53s | 2s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25412092460/job/74536001853) |
| 1m 53s | 3s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25412092460/job/74536001863) |
| 1m 45s |  | `release-checks` | install_smoke_release_checks / root_dockerfile_image |  | [job](https://github.com/openclaw/openclaw/actions/runs/25412095596/job/74535982480) |
| 1m 42s | 2s | `normal-ci` | checks-fast-contracts-plugins | success | [job](https://github.com/openclaw/openclaw/actions/runs/25412092460/job/74535995686) |
| 1m 24s | 25s | `release-checks` | install_smoke_release_checks / docker-e2e-fast | success | [job](https://github.com/openclaw/openclaw/actions/runs/25412095596/job/74535982458) |
| 1m 24s | 27s | `release-checks` | install_smoke_release_checks / qr_package_install_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25412095596/job/74535982461) |
| 1m 23s | 0s | `release-checks` | install_smoke_release_checks / install-smoke-fast | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25412095596/job/74535982742) |
| 1m 16s |  | `release-checks` | Prepare release package artifact |  | [job](https://github.com/openclaw/openclaw/actions/runs/25412095596/job/74535963399) |
| 1m 16s | 7s | `release-checks` | install_smoke_release_checks / preflight | success | [job](https://github.com/openclaw/openclaw/actions/runs/25412095596/job/74535963537) |
| 1m 10s |  | `release-checks` | Run QA Lab live Matrix lane |  | [job](https://github.com/openclaw/openclaw/actions/runs/25412095596/job/74535963398) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25412078910
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25412078910/job/74535854181
  - Run plugin prerelease validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25412078910/job/74535854182
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25412078910/job/74535854187
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25412078910/job/74536019687

## Notes

Automatically requested by Full Release Validation 25412078910 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

