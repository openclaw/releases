# OpenClaw Release Evidence: release-2026.4.30

Generated: 2026-05-02T15:21:16.896Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `release-2026.4.30` |
| Release ref input | `release/2026.4.30` |
| Release ref status | resolved |
| Release ref kind | `branch` |
| Release ref name | `release/2026.4.30` |
| Release ref SHA | `68db30b8ef2d765a1d58200175da58d42517b5f7` |
| Runs at release SHA | `full-release-validation`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 0 | 0 | 0 |
| Advisory | 1 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | advisory | `full-release-validation` | Full Release Validation | `release/2026.4.30` | `68db30b8ef2d` | 10m 6s (-18m 47s) | 9m 58s (-18m 47s) | 9m 59s | [25254953253](https://github.com/openclaw/openclaw/actions/runs/25254953253) | 0 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.4.30` | `68db30b8ef2d` | 9m 7s (-18m 44s) | 11m 57s (-25m 22s) | 9m 3s | [25254959456](https://github.com/openclaw/openclaw/actions/runs/25254959456) | 5 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 9m 43s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25254953253/job/74052729032) |
| 2m 49s | `release-checks` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25254959456/job/74052785744) |
| 2m 12s | `release-checks` | Run package acceptance / Telegram package acceptance / Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25254959456/job/74052990697) |
| 1m 29s | `release-checks` | Run package acceptance / Docker product acceptance / prepare_docker_e2e_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/25254959456/job/74053039198) |
| 1m 20s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25254959456/job/74053119040) |
| 1m 11s | `release-checks` | Run package acceptance / Resolve package candidate | success | [job](https://github.com/openclaw/openclaw/actions/runs/25254959456/job/74052928515) |
| 59s | `release-checks` | resolve_target | success | [job](https://github.com/openclaw/openclaw/actions/runs/25254959456/job/74052736295) |
| 54s | `release-checks` | Run package acceptance / Docker product acceptance / validate_selected_ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25254959456/job/74052990620) |
| 51s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25254959456/job/74053119047) |
| 9s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25254953253/job/74052720629) |
| 6s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25254953253/job/74053227329) |
| 5s | `release-checks` | Run package acceptance / Docker product acceptance / plan_docker_lane_groups | success | [job](https://github.com/openclaw/openclaw/actions/runs/25254959456/job/74053039204) |
| 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25254959456/job/74053190098) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25254953253/job/74052729176) |
| 0s | `full-release-validation` | Run post-publish Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25254953253/job/74052729244) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 9m 59s | 6s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25254953253/job/74053227329) |
| 9m 3s | 2s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/25254959456/job/74053196095) |
| 8m 56s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25254959456/job/74053190098) |
| 7m 43s | 51s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25254959456/job/74053119047) |
| 7m 34s | 1m 20s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25254959456/job/74053119040) |
| 7m 33s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25254959456/job/74053119106) |
| 7m 33s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25254959456/job/74053119162) |
| 6m 4s | 1m 29s | `release-checks` | Run package acceptance / Docker product acceptance / prepare_docker_e2e_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/25254959456/job/74053039198) |
| 6m 4s | 5s | `release-checks` | Run package acceptance / Docker product acceptance / plan_docker_lane_groups | success | [job](https://github.com/openclaw/openclaw/actions/runs/25254959456/job/74053039204) |
| 6m 3s |  | `release-checks` | Run package acceptance / Docker product acceptance / Live media suites (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25254959456/job/74053039293) |
| 6m 3s |  | `release-checks` | Run package acceptance / Docker product acceptance / validate_special_e2e | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25254959456/job/74053039302) |
| 14s | 9m 43s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25254953253/job/74052729032) |
| 12s | 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25254953253/job/74052729176) |
| 12s | 0s | `full-release-validation` | Run post-publish Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25254953253/job/74052729244) |
| 12s | 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25254953253/job/74052729262) |

## Timing Changes

| Run | Previous | Current | Delta | Job Time Delta |
| --- | ---: | ---: | ---: | ---: |
| `full-release-validation` | 28m 53s | 10m 6s | -18m 47s | -18m 47s |
| `release-checks` | 27m 51s | 9m 7s | -18m 44s | -25m 22s |

## Notes

Automatically requested by Full Release Validation 25254953253 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

