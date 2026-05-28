# OpenClaw Release Evidence: fc055e2393cd6fa9730e31f57597c1ac8ea3dad1

Generated: 2026-04-27T23:38:54.039Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `fc055e2393cd6fa9730e31f57597c1ac8ea3dad1` |
| Release ref input | `fc055e2393cd6fa9730e31f57597c1ac8ea3dad1` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `fc055e2393cd6fa9730e31f57597c1ac8ea3dad1` |
| Release ref SHA | `fc055e2393cd6fa9730e31f57597c1ac8ea3dad1` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 1 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `fc055e2393cd` | 9m 13s | 12m 16s | [25025094613](https://github.com/openclaw/openclaw/actions/runs/25025094613) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `fc055e2393cd` | 2m 53s | 54m 32s | [25025126092](https://github.com/openclaw/openclaw/actions/runs/25025126092) | 3 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `fc055e2393cd` | 7m 59s | 3h 0m 6s | [25025126426](https://github.com/openclaw/openclaw/actions/runs/25025126426) | 22 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 8m 8s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025094613/job/73294424434) |
| 6m 18s | `release-checks` | live_and_e2e_release_checks / Docker live models (OpenRouter) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025126426/job/73294627041) |
| 6m 17s | `release-checks` | live_and_e2e_release_checks / Docker live models (Z.ai) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025126426/job/73294627044) |
| 6m 17s | `release-checks` | live_and_e2e_release_checks / Docker live models (Fireworks) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025126426/job/73294627046) |
| 6m 17s | `release-checks` | live_and_e2e_release_checks / Docker live models (OpenCode) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025126426/job/73294627047) |
| 6m 17s | `release-checks` | live_and_e2e_release_checks / Docker live models (xAI) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025126426/job/73294627055) |
| 6m 17s | `release-checks` | live_and_e2e_release_checks / Docker live models (OpenAI) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025126426/job/73294627056) |
| 6m 16s | `release-checks` | live_and_e2e_release_checks / Docker live models (MiniMax) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025126426/job/73294627042) |
| 6m 16s | `release-checks` | live_and_e2e_release_checks / Docker live models (Anthropic) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025126426/job/73294627045) |
| 5m 56s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway-core, Native live gateway core, node scrip... | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25025126426/job/73294627057) |
| 5m 13s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-extensions-media, Native live media plugins, node scri... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025126426/job/73294627060) |
| 3m 13s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025094613/job/73294424425) |
| 2m 35s | `normal-ci` | checks-node-agentic-agents | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025126092/job/73294457109) |
| 2m 3s | `normal-ci` | checks-node-agentic-plugin-sdk | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025126092/job/73294457077) |
| 1m 59s | `normal-ci` | macos-swift | success | [job](https://github.com/openclaw/openclaw/actions/runs/25025126092/job/73294456912) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025094613
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25025094613/job/73294424434
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25025094613/job/73295273754
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25025126092
  - checks-fast-contracts-plugins: failure - https://github.com/openclaw/openclaw/actions/runs/25025126092/job/73294456836
  - check-additional-boundaries: failure - https://github.com/openclaw/openclaw/actions/runs/25025126092/job/73294456994
  - check-additional: failure - https://github.com/openclaw/openclaw/actions/runs/25025126092/job/73294642874

## Notes

Automatically requested by Full Release Validation 25025094613 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

