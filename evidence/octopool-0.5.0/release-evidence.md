# OpenClaw Release Evidence: octopool-0.5.0

Generated: 2026-07-18T17:04:09.095Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.5.0` |
| Release ref input | `v0.5.0` |
| Release ref status | not-found |
| Release ref kind | unknown |
| Release ref name | unknown |
| Release ref SHA | not resolved |
| Runs at release SHA | none |
| Package spec | `octopool@0.5.0` |
| npm status | invalid |
| npm error | only openclaw package specs are supported |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 0 | 0 | 0 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | blocking | `release` | release | `v0.5.0` | `ae40820d7e89` | 1m 12s | 1m 9s | 2s | [29652691829](https://github.com/openclaw/octopool/actions/runs/29652691829) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1m 9s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/29652691829/job/88101597582) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 2s | 1m 9s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/29652691829/job/88101597582) |

## Notes

octopool 0.5.0: quota program (token-free-first, human-format reads, conditional revalidation, R2 log cache + run_list superset). Darwin binaries signed with OpenClaw Foundation Developer ID (FWJYW4S8P8) and notarized (submissions 7cb9c310-add3-4cf5-bf44-f90ce624119a, 6177342a-0418-4891-b3b5-93f76324e12b); Gatekeeper assesses Notarized Developer ID. Worker deployed b93c4daf/eb56bc3c; fleet on 0.5.0.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

