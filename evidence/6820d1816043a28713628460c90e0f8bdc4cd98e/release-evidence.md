# OpenClaw Release Evidence: 6820d1816043a28713628460c90e0f8bdc4cd98e

Generated: 2026-05-12T11:15:19.262Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `6820d1816043a28713628460c90e0f8bdc4cd98e` |
| Release ref input | `6820d1816043a28713628460c90e0f8bdc4cd98e` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `6820d1816043a28713628460c90e0f8bdc4cd98e` |
| Release ref SHA | `6820d1816043a28713628460c90e0f8bdc4cd98e` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/6820d1816043-1778580937603` | `6820d1816043` | 59m 21s | 1h 19m 8s | 58m 45s | [25728084036](https://github.com/openclaw/openclaw/actions/runs/25728084036) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/6820d1816043-1778580937603` | `6820d1816043` | 3m 25s | 1h 7m 31s | 3m 22s | [25728110633](https://github.com/openclaw/openclaw/actions/runs/25728110633) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/6820d1816043-1778580937603` | `6820d1816043` | 57m 42s | 16h 8m 3s | 57m 39s | [25728111522](https://github.com/openclaw/openclaw/actions/runs/25728111522) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/6820d1816043-1778580937603` | `6820d1816043` | 3m 54s | 2m 58s | 55s | [25728266978](https://github.com/openclaw/openclaw/actions/runs/25728266978) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 58m 8s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728084036/job/75546009851) |
| 50m 42s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002073) |
| 50m 28s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002069) |
| 45m 52s | `release-checks` | install_smoke_release_checks / root_dockerfile_image | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75546338768) |
| 40m 42s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002080) |
| 36m 11s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002031) |
| 35m 57s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002000) |
| 35m 53s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenRouter) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002007) |
| 35m 46s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002018) |
| 35m 44s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002006) |
| 35m 43s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenCode) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547001998) |
| 8m 46s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728084036/job/75546009822) |
| 4m 25s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728084036/job/75546541788) |
| 3m 44s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728084036/job/75546009818) |
| 3m 17s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728084036/job/75546009918) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 58m 45s | 35s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728084036/job/75555361132) |
| 57m 39s | 2s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75555271450) |
| 47m 43s |  | `release-checks` | install_smoke_release_checks / bun_global_install_smoke | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75553704028) |
| 47m 43s |  | `release-checks` | install_smoke_release_checks / root_dockerfile_smokes | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75553704191) |
| 47m 43s |  | `release-checks` | install_smoke_release_checks / installer_smoke | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75553704720) |
| 23m 24s | 11s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75549746000) |
| 12m 39s | 1m 23s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547928294) |
| 12m 29s | 1m 17s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547928285) |
| 12m 29s | 1m 27s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547928303) |
| 12m 29s | 1m 29s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547928309) |
| 12m 29s | 5m 9s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547928346) |
| 3m 48s | 4m 25s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728084036/job/75546541788) |
| 3m 22s | 2s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728110633/job/75546558557) |
| 3m 16s | 4s | `normal-ci` | checks-node-channels | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728110633/job/75546540027) |
| 3m 9s | 4s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25728110633/job/75546540060) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25728084036
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25728084036/job/75555361132
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25728111522
  - install_smoke_release_checks / root_dockerfile_image: failure - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75546338768
  - Run repo/live E2E validation / Docker live models (Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547001991
  - Run repo/live E2E validation / Docker live models (OpenCode): failure - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547001998
  - Run repo/live E2E validation / Docker live models (Google): failure - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002000
  - Run repo/live E2E validation / Docker live models (MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002006
  - Run repo/live E2E validation / Docker live models (OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002007
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002018
  - Run repo/live E2E validation / Docker live models (OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002031
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002037
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002047
  - Run repo/live E2E validation / Docker live models (Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002048
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002051
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002056
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002069
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002070
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002073
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002080
  - Run repo/live E2E validation / Docker live models (Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002095
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002154
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547002274
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547452051
  - Run Docker release-path validation / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547452060
  - Run Docker release-path validation / Docker E2E (core): failure - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547452101
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): failure - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547928263
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547928294
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth): failure - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75547928303
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75549746000
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25728111522/job/75555271450

## Notes

Automatically requested by Full Release Validation 25728084036 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

