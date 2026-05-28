# OpenClaw Release Evidence: e6fb7aa1a86bab4cc6c9a8201061d3560098018c

Generated: 2026-05-12T11:06:55.476Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `e6fb7aa1a86bab4cc6c9a8201061d3560098018c` |
| Release ref input | `e6fb7aa1a86bab4cc6c9a8201061d3560098018c` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `e6fb7aa1a86bab4cc6c9a8201061d3560098018c` |
| Release ref SHA | `e6fb7aa1a86bab4cc6c9a8201061d3560098018c` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 2 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/e6fb7aa1a86b-1778580425630` | `e6fb7aa1a86b` | 59m 17s | 1h 23m 57s | 58m 40s | [25727681793](https://github.com/openclaw/openclaw/actions/runs/25727681793) | 1 |
| fail | blocking | `normal-ci` | CI | `release-ci/e6fb7aa1a86b-1778580425630` | `e6fb7aa1a86b` | 3m 24s | 1h 5m 56s | 3m 21s | [25727709659](https://github.com/openclaw/openclaw/actions/runs/25727709659) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/e6fb7aa1a86b-1778580425630` | `e6fb7aa1a86b` | 57m 24s | 14h 25m 26s | 57m 12s | [25727711525](https://github.com/openclaw/openclaw/actions/runs/25727711525) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/e6fb7aa1a86b-1778580425630` | `e6fb7aa1a86b` | 5m 46s | 3m 6s | 2m 39s | [25727879864](https://github.com/openclaw/openclaw/actions/runs/25727879864) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 58m 6s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25727681793/job/75544663622) |
| 50m 43s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552691) |
| 45m 31s | `release-checks` | install_smoke_release_checks / root_dockerfile_image | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75544993266) |
| 40m 41s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552647) |
| 36m 5s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552653) |
| 35m 58s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552597) |
| 35m 51s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552545) |
| 35m 51s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552577) |
| 35m 43s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552697) |
| 35m 42s | `release-checks` | Run repo/live E2E validation / Docker live models (Fireworks) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552661) |
| 35m 42s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552666) |
| 11m 21s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25727681793/job/75544663552) |
| 6m 25s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25727681793/job/75545246483) |
| 3m 45s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25727681793/job/75544663548) |
| 3m 29s | `full-release-validation` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25727681793/job/75544663541) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 58m 40s | 36s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25727681793/job/75553998023) |
| 57m 12s | 11s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75553834487) |
| 47m 26s | 0s | `release-checks` | install_smoke_release_checks / installer_smoke | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75552263960) |
| 47m 26s | 0s | `release-checks` | install_smoke_release_checks / bun_global_install_smoke | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75552264225) |
| 47m 26s | 0s | `release-checks` | install_smoke_release_checks / root_dockerfile_smokes | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75552264501) |
| 18m 35s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75547619650) |
| 10m 48s | 6m 34s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75546280283) |
| 10m 21s | 8m 11s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75546280353) |
| 10m 20s | 1m 36s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75546280284) |
| 10m 20s | 1m 27s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75546280291) |
| 10m 20s | 1m 8s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-corrupt-plugin) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75546280305) |
| 4m 7s | 6m 25s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25727681793/job/75545246483) |
| 3m 21s | 2s | `normal-ci` | checks-node-core | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25727709659/job/75545216357) |
| 3m 15s | 3s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25727709659/job/75545198081) |
| 3m 15s | 3s | `normal-ci` | checks-node-core-support-boundary | success | [job](https://github.com/openclaw/openclaw/actions/runs/25727709659/job/75545198117) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25727681793
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25727681793/job/75553998023
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25727709659
  - checks-node-core-fast: failure - https://github.com/openclaw/openclaw/actions/runs/25727709659/job/75544735197
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25727709659/job/75545216357
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25727711525
  - install_smoke_release_checks / root_dockerfile_image: failure - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75544993266
  - Run repo/live E2E validation / Docker live models (Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552545
  - Run repo/live E2E validation / Docker live models (OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552563
  - Run repo/live E2E validation / Docker live models (OpenCode): failure - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552567
  - Run repo/live E2E validation / Docker live models (Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552577
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552596
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552597
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): failure - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552600
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552608
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552634
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552636
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552644
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552647
  - Run repo/live E2E validation / Docker live models (MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552653
  - Run repo/live E2E validation / Docker live models (Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552661
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): failure - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552663
  - Run repo/live E2E validation / Docker live models (OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552666
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552691
  - Run repo/live E2E validation / Docker live models (Google): failure - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552697
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75545552743
  - Run Docker release-path validation / Docker E2E (core): failure - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75546044742
  - Run Docker release-path validation / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75546044751
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): failure - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75546280284
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75546280291
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth): failure - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75546280326
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75547619650
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25727711525/job/75553834487

## Notes

Automatically requested by Full Release Validation 25727681793 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

