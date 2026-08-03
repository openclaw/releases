# OpenClaw Release Evidence: octopool-0.5.1

Generated: 2026-08-03T08:31:36.581Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.5.1` |
| Release ref input | `v0.5.1` |
| Release ref status | not-found |
| Release ref kind | unknown |
| Release ref name | unknown |
| Release ref SHA | not resolved |
| Runs at release SHA | none |
| Package spec | `octopool@0.5.1` |
| npm status | invalid |
| npm error | only openclaw package specs are supported |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 2 | 0 | 0 | 0 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | blocking | `ci` | CI | `main` | `e5008263d2fd` | 3m 30s | 3m 21s | 9s | [30796885179](https://github.com/openclaw/octopool/actions/runs/30796885179) | 0 |
| pass | blocking | `release` | release | `v0.5.1` | `e5008263d2fd` | 2m 18s | 2m 15s | 2s | [30797128926](https://github.com/openclaw/octopool/actions/runs/30797128926) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 3m 21s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/30796885179/job/91632391139) |
| 2m 15s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/30797128926/job/91633146166) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 9s | 3m 21s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/30796885179/job/91632391139) |
| 2s | 2m 15s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/30797128926/job/91633146166) |

## Notes

GitHub release assets were checksum-verified after both Darwin archives were signed and notarized with the OpenClaw Foundation Developer ID. Homebrew formula 0.5.1 was published and the OpenClaw Worker was deployed from the release commit.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

