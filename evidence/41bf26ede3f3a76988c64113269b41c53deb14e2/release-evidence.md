# OpenClaw Release Evidence: 41bf26ede3f3a76988c64113269b41c53deb14e2

Generated: 2026-05-12T11:34:47.154Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `41bf26ede3f3a76988c64113269b41c53deb14e2` |
| Release ref input | `41bf26ede3f3a76988c64113269b41c53deb14e2` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `41bf26ede3f3a76988c64113269b41c53deb14e2` |
| Release ref SHA | `41bf26ede3f3a76988c64113269b41c53deb14e2` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 2 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/41bf26ede3f3-1778582026883` | `41bf26ede3f3` | 1h 0m 30s | 1h 23m 42s | 59m 59s | [25728926292](https://github.com/openclaw/openclaw/actions/runs/25728926292) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/41bf26ede3f3-1778582026883` | `41bf26ede3f3` | 3m 22s | 1h 4m 21s | 3m 18s | [25728959717](https://github.com/openclaw/openclaw/actions/runs/25728959717) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/41bf26ede3f3-1778582026883` | `41bf26ede3f3` | 58m 29s | 16h 20m 42s | 58m 26s | [25728959820](https://github.com/openclaw/openclaw/actions/runs/25728959820) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/41bf26ede3f3-1778582026883` | `41bf26ede3f3` | 4m 28s | 4m 1s | 26s | [25729115995](https://github.com/openclaw/openclaw/actions/runs/25729115995) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 59m 13s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728926292/job/75548895711) |
| 50m 31s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141969) |
| 50m 31s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141973) |
| 45m 24s | `release-checks` | install_smoke_release_checks / root_dockerfile_image | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75549223402) |
| 40m 42s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550142031) |
| 35m 53s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141908) |
| 35m 52s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141985) |
| 35m 48s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141939) |
| 35m 46s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141934) |
| 35m 44s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141949) |
| 35m 42s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141938) |
| 11m 40s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728926292/job/75548895682) |
| 4m 50s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728926292/job/75549456367) |
| 4m 1s | `postpublish-telegram` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25729115995/job/75549479928) |
| 3m 51s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728926292/job/75548895705) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 59m 59s | 30s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728926292/job/75558438590) |
| 58m 26s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75558328287) |
| 47m 12s |  | `release-checks` | install_smoke_release_checks / root_dockerfile_smokes | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75556545359) |
| 47m 11s | 0s | `release-checks` | install_smoke_release_checks / installer_smoke | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75556545030) |
| 47m 11s | 0s | `release-checks` | install_smoke_release_checks / bun_global_install_smoke | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75556545102) |
| 18m 7s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75551840446) |
| 13m 24s | 1m 17s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550554776) |
| 13m 23s | 1m 56s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550554763) |
| 13m 23s | 2m 46s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install C) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550554774) |
| 13m 23s | 4m 18s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update core) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550554786) |
| 13m 23s | 1m 48s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550554789) |
| 3m 58s | 4m 50s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728926292/job/75549456367) |
| 3m 18s | 3s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728959717/job/75549464600) |
| 3m 14s | 3s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728959717/job/75549436757) |
| 3m 14s | 2s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728959717/job/75549436804) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25728926292
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25728926292/job/75558438590
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25728959820
  - install_smoke_release_checks / root_dockerfile_image: failure - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75549223402
  - Run repo/live E2E validation / Docker live models (Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141908
  - Run repo/live E2E validation / Docker live models (OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141934
  - Run repo/live E2E validation / Docker live models (OpenCode): failure - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141936
  - Run repo/live E2E validation / Docker live models (Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141938
  - Run repo/live E2E validation / Docker live models (MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141939
  - Run repo/live E2E validation / Docker live models (Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141949
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141951
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141958
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141969
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141973
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141979
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141984
  - Run repo/live E2E validation / Docker live models (Google): failure - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141985
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550141989
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550142003
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550142031
  - Run repo/live E2E validation / Docker live models (OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550142036
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550142055
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550142138
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): failure - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550501493
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth): failure - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550501494
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550501519
  - Run Docker release-path validation / Docker E2E (core): failure - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550554760
  - Run Docker release-path validation / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75550554786
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75551840446
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25728959820/job/75558328287

## Notes

Automatically requested by Full Release Validation 25728926292 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

