# OpenClaw Release Evidence: b90f29d3133336bb896d7ccdb096f998da4ef635

Generated: 2026-04-27T23:52:01.898Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `b90f29d3133336bb896d7ccdb096f998da4ef635` |
| Release ref input | `b90f29d3133336bb896d7ccdb096f998da4ef635` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `b90f29d3133336bb896d7ccdb096f998da4ef635` |
| Release ref SHA | `b90f29d3133336bb896d7ccdb096f998da4ef635` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `b90f29d31333` | 2m 32s | 2m 24s | [25025758311](https://github.com/openclaw/openclaw/actions/runs/25025758311) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `b90f29d31333` | 1m 24s | 1m 15s | [25025789554](https://github.com/openclaw/openclaw/actions/runs/25025789554) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 1m 34s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025758311/job/73296492617) |
| 43s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025758311/job/73296415463) |
| 37s | `release-checks` | resolve_target | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296510564) |
| 35s | `release-checks` | live_and_e2e_release_checks / validate_selected_ref | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296577123) |
| 7s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25025758311/job/73296659701) |
| 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296639957) |
| 0s | `full-release-validation` | Run post-publish Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25025758311/job/73296492781) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25025758311/job/73296492955) |
| 0s | `release-checks` | Run QA Lab live Matrix lane | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296577278) |
| 0s | `release-checks` | Run QA Lab parity lane (${{ matrix.lane }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296577289) |
| 0s | `release-checks` | Run package acceptance | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296577327) |
| 0s | `release-checks` | cross_os_release_checks | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296577388) |
| 0s | `release-checks` | Run QA Lab live Telegram lane | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296577403) |
| 0s | `release-checks` | install_smoke_release_checks | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296577455) |
| 0s | `release-checks` | live_and_e2e_release_checks / validate_special_e2e | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296639500) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025758311
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025758311/job/73296492617
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25025758311/job/73296659701
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025789554
  - live_and_e2e_release_checks / validate_selected_ref: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296577123
  - live_and_e2e_release_checks / validate_special_e2e: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296639500
  - live_and_e2e_release_checks / validate_repo_e2e: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296639520
  - live_and_e2e_release_checks / Docker live models (selected providers): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296639570
  - live_and_e2e_release_checks / Docker live models (${{ matrix.provider_label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296639591
  - live_and_e2e_release_checks / validate_live_provider_suites: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296639685
  - live_and_e2e_release_checks / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296639710
  - live_and_e2e_release_checks / plan_docker_lane_groups: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296639742
  - live_and_e2e_release_checks / Docker E2E targeted lanes (${{ matrix.group.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296639745
  - live_and_e2e_release_checks / Docker E2E (openwebui): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296639769
  - live_and_e2e_release_checks / prepare_docker_e2e_image: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296639784
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296639957
  - live_and_e2e_release_checks / Docker E2E (${{ matrix.label }}): cancelled - https://github.com/openclaw/openclaw/actions/runs/25025789554/job/73296640029

## Notes

Automatically requested by Full Release Validation 25025758311 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

