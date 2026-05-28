# OpenClaw Release Evidence: 13327dbaef0962223dd6aa33b64cff9abc100785

Generated: 2026-04-28T14:39:17.370Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `13327dbaef0962223dd6aa33b64cff9abc100785` |
| Release ref input | `13327dbaef0962223dd6aa33b64cff9abc100785` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `13327dbaef0962223dd6aa33b64cff9abc100785` |
| Release ref SHA | `13327dbaef0962223dd6aa33b64cff9abc100785` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release/2026.4.27` | `13327dbaef09` | 21m 5s | 25m 37s | [25058289497](https://github.com/openclaw/openclaw/actions/runs/25058289497) | 0 |
| fail | blocking | `normal-ci` | CI | `release/2026.4.27` | `13327dbaef09` | 4m 21s | 1h 3m 51s | [25058318413](https://github.com/openclaw/openclaw/actions/runs/25058318413) | 3 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `release/2026.4.27` | `13327dbaef09` | 17m 47s | 3h 22m 46s | [25058318907](https://github.com/openclaw/openclaw/actions/runs/25058318907) | 19 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 20m 20s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25058289497/job/73404823802) |
| 11m 41s | `release-checks` | install_smoke_release_checks / install-smoke | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25058318907/job/73405449983) |
| 7m 49s | `release-checks` | live_and_e2e_release_checks / Docker live models (Google) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25058318907/job/73405940047) |
| 7m 41s | `release-checks` | live_and_e2e_release_checks / Docker live models (Z.ai) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25058318907/job/73405940090) |
| 7m 32s | `release-checks` | live_and_e2e_release_checks / Docker live models (OpenCode) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25058318907/job/73405940080) |
| 7m 16s | `release-checks` | live_and_e2e_release_checks / Docker live models (OpenAI) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25058318907/job/73405940399) |
| 6m 45s | `release-checks` | live_and_e2e_release_checks / Docker live models (Fireworks) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25058318907/job/73405940322) |
| 6m 23s | `release-checks` | live_and_e2e_release_checks / Docker live models (Anthropic) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25058318907/job/73405940100) |
| 6m 21s | `release-checks` | live_and_e2e_release_checks / Docker live models (OpenRouter) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25058318907/job/73405940214) |
| 6m 15s | `release-checks` | live_and_e2e_release_checks / Docker live models (MiniMax) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25058318907/job/73405940523) |
| 6m 3s | `release-checks` | live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway-profiles-zai, Native live gateway profiles... | success | [job](https://github.com/openclaw/openclaw/actions/runs/25058318907/job/73405940843) |
| 4m 50s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25058289497/job/73404823643) |
| 2m 47s | `normal-ci` | checks-node-agentic-plugin-sdk | success | [job](https://github.com/openclaw/openclaw/actions/runs/25058318413/job/73404948544) |
| 2m 24s | `normal-ci` | checks-node-auto-reply-reply-commands-state-routing | success | [job](https://github.com/openclaw/openclaw/actions/runs/25058318413/job/73404948681) |
| 2m 15s | `normal-ci` | checks-fast-contracts-plugins | success | [job](https://github.com/openclaw/openclaw/actions/runs/25058318413/job/73404948124) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25058289497
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25058289497/job/73404823802
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25058289497/job/73408908268
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25058318413
  - checks-node-extensions-shard-5: failure - https://github.com/openclaw/openclaw/actions/runs/25058318413/job/73404948540
  - checks-node-extensions: failure - https://github.com/openclaw/openclaw/actions/runs/25058318413/job/73405632786

## Notes

Automatically requested by Full Release Validation 25058289497 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

