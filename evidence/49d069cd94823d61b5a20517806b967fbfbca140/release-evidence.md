# OpenClaw Release Evidence: 49d069cd94823d61b5a20517806b967fbfbca140

Generated: 2026-04-27T23:58:30.191Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `49d069cd94823d61b5a20517806b967fbfbca140` |
| Release ref input | `49d069cd94823d61b5a20517806b967fbfbca140` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `49d069cd94823d61b5a20517806b967fbfbca140` |
| Release ref SHA | `49d069cd94823d61b5a20517806b967fbfbca140` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `49d069cd9482` | 3m 24s | 3m 16s | [25025948656](https://github.com/openclaw/openclaw/actions/runs/25025948656) | 0 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `7f77ecff77aa` | 2m 29s | 8m 42s | [25025977989](https://github.com/openclaw/openclaw/actions/runs/25025977989) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 2m 26s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025948656/job/73297052489) |
| 1m 9s | `release-checks` | live_and_e2e_release_checks / prepare_docker_e2e_image | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025977989/job/73297195224) |
| 1m 9s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-extensions-media-music, Native live media music plugin... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025977989/job/73297195510) |
| 1m 5s | `release-checks` | live_and_e2e_release_checks / validate_special_e2e (openshell-e2e, OpenShell repo E2E, pnpm test:e2e:openshell, 120, true, false) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025977989/job/73297195198) |
| 1m 1s | `release-checks` | live_and_e2e_release_checks / validate_special_e2e (openai-ws-stream-live-e2e, OpenAI WebSocket live E2E, pnpm test:e2e src/age... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025977989/job/73297195200) |
| 46s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-extensions-l-n, Native live plugins L-N, node scripts/... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025977989/job/73297195536) |
| 44s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025948656/job/73296978579) |
| 43s | `release-checks` | live_and_e2e_release_checks / validate_selected_ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025977989/job/73297128217) |
| 40s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway-backends, Native live gateway backends, no... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025977989/job/73297195521) |
| 36s | `release-checks` | resolve_target | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025977989/job/73297067637) |
| 35s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-extensions-media-audio, Native live media audio plugin... | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25025977989/job/73297195548) |
| 30s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-extensions-o-z-other, Native live plugins O-Z other, n... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025977989/job/73297195539) |
| 6s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25025948656/job/73297285074) |
| 0s | `full-release-validation` | Run post-publish Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25025948656/job/73297052643) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25025948656/job/73297052715) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025948656
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025948656/job/73297052489
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25025948656/job/73297285074

## Notes

Automatically requested by Full Release Validation 25025948656 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

