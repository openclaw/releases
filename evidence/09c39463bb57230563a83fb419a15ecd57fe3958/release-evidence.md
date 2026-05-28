# OpenClaw Release Evidence: 09c39463bb57230563a83fb419a15ecd57fe3958

Generated: 2026-04-27T23:50:09.436Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `09c39463bb57230563a83fb419a15ecd57fe3958` |
| Release ref input | `09c39463bb57230563a83fb419a15ecd57fe3958` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `09c39463bb57230563a83fb419a15ecd57fe3958` |
| Release ref SHA | `09c39463bb57230563a83fb419a15ecd57fe3958` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `09c39463bb57` | 4m 34s | 4m 27s | [25025627562](https://github.com/openclaw/openclaw/actions/runs/25025627562) | 0 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `3f94f25a3c7a` | 3m 0s | 45m 47s | [25025658762](https://github.com/openclaw/openclaw/actions/runs/25025658762) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 3m 35s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025627562/job/73296083924) |
| 2m 17s | `release-checks` | live_and_e2e_release_checks / prepare_docker_e2e_image | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025658762/job/73296245392) |
| 2m 9s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-codex-harness-docker, Docker live Codex harness, pnpm test:do... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025658762/job/73296245559) |
| 2m 5s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-acp-bind-docker, Docker live ACP bind, pnpm test:docker:live-... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025658762/job/73296245542) |
| 2m 3s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (live-cli-backend-docker, Docker live CLI backend, pnpm test:docker... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025658762/job/73296245549) |
| 1m 52s | `release-checks` | live_and_e2e_release_checks / validate_repo_e2e | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025658762/job/73296245402) |
| 1m 52s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-extensions-a-k, Native live plugins A-K, node scripts/... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025658762/job/73296245527) |
| 1m 52s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-agents, Native live agents, node scripts/test-live... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025658762/job/73296245543) |
| 1m 52s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-extensions-openai, Native live OpenAI plugin, node scr... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025658762/job/73296245551) |
| 1m 52s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-extensions-media, Native live media plugins, node scri... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025658762/job/73296245552) |
| 1m 51s | `release-checks` | live_and_e2e_release_checks / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025658762/job/73296245375) |
| 44s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025627562/job/73296001445) |
| 8s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25025627562/job/73296464597) |
| 0s | `full-release-validation` | Run post-publish Telegram E2E | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25025627562/job/73296084164) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25025627562/job/73296084359) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025627562
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025627562/job/73296083924
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25025627562/job/73296464597

## Notes

Automatically requested by Full Release Validation 25025627562 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

