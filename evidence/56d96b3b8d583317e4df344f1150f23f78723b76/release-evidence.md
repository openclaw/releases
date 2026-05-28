# OpenClaw Release Evidence: 56d96b3b8d583317e4df344f1150f23f78723b76

Generated: 2026-05-12T12:07:58.964Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `56d96b3b8d583317e4df344f1150f23f78723b76` |
| Release ref input | `56d96b3b8d583317e4df344f1150f23f78723b76` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `56d96b3b8d583317e4df344f1150f23f78723b76` |
| Release ref SHA | `56d96b3b8d583317e4df344f1150f23f78723b76` |
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
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/56d96b3b8d58-1778584074899` | `56d96b3b8d58` | 59m 45s | 1h 22m 1s | 59m 13s | [25730533795](https://github.com/openclaw/openclaw/actions/runs/25730533795) | 1 |
| pass | blocking | `normal-ci` | CI | `release-ci/56d96b3b8d58-1778584074899` | `56d96b3b8d58` | 3m 47s | 1h 7m 19s | 3m 42s | [25730554811](https://github.com/openclaw/openclaw/actions/runs/25730554811) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/56d96b3b8d58-1778584074899` | `56d96b3b8d58` | 58m 32s | 16h 34m 37s | 58m 28s | [25730557051](https://github.com/openclaw/openclaw/actions/runs/25730557051) | 48 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/56d96b3b8d58-1778584074899` | `56d96b3b8d58` | 3m 44s | 3m 0s | 43s | [25730718102](https://github.com/openclaw/openclaw/actions/runs/25730718102) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 58m 48s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25730533795/job/75554401883) |
| 50m 44s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live CLI backend) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580833) |
| 50m 43s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live ACP bind) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580811) |
| 45m 31s | `release-checks` | install_smoke_release_checks / root_dockerfile_image | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75554697413) |
| 40m 43s | `release-checks` | Run repo/live E2E validation / Docker live suites (Docker live Codex harness) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580878) |
| 35m 56s | `release-checks` | Run repo/live E2E validation / Docker live models (Z.ai) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580753) |
| 35m 54s | `release-checks` | Run repo/live E2E validation / Docker live models (Google) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580758) |
| 35m 51s | `release-checks` | Run repo/live E2E validation / Docker live models (OpenAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580765) |
| 35m 44s | `release-checks` | Run repo/live E2E validation / Docker live models (xAI) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580751) |
| 35m 43s | `release-checks` | Run repo/live E2E validation / Docker live models (Anthropic) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580769) |
| 35m 42s | `release-checks` | Run repo/live E2E validation / Docker live models (MiniMax) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580969) |
| 10m 49s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25730533795/job/75554401839) |
| 4m 18s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25730533795/job/75554938031) |
| 4m 10s | `full-release-validation` | Run normal full CI | success | [job](https://github.com/openclaw/openclaw/actions/runs/25730533795/job/75554401861) |
| 3m 15s | `normal-ci` | build-artifacts | success | [job](https://github.com/openclaw/openclaw/actions/runs/25730554811/job/75554464427) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 59m 13s | 31s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25730533795/job/75563875565) |
| 58m 28s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75563830848) |
| 47m 40s |  | `release-checks` | install_smoke_release_checks / root_dockerfile_smokes | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75562051122) |
| 47m 40s |  | `release-checks` | install_smoke_release_checks / bun_global_install_smoke | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75562051235) |
| 47m 40s |  | `release-checks` | install_smoke_release_checks / installer_smoke | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75562051630) |
| 18m 41s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75557392644) |
| 11m 24s | 1m 45s | `release-checks` | Run Docker release-path validation / Docker E2E (core) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555916950) |
| 11m 24s | 1m 13s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75556015834) |
| 11m 24s | 5m 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.2) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75556015841) |
| 11m 24s | 57s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (skill-install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75556015843) |
| 11m 24s | 7m 4s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75556015844) |
| 3m 48s | 4m 18s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25730533795/job/75554938031) |
| 3m 42s | 3s | `normal-ci` | build-smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25730554811/job/75554989522) |
| 3m 42s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25730554811/job/75555004395) |
| 3m 36s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25730554811/job/75554989508) |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/25730533795
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25730533795/job/75563875565
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/25730557051
  - install_smoke_release_checks / root_dockerfile_image: failure - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75554697413
  - Run repo/live E2E validation / Docker live models (xAI): failure - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580751
  - Run repo/live E2E validation / Docker live models (Z.ai): failure - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580753
  - Run repo/live E2E validation / Docker live models (OpenCode): failure - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580756
  - Run repo/live E2E validation / Docker live models (Google): failure - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580758
  - Run repo/live E2E validation / Docker live models (OpenAI): failure - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580765
  - Run repo/live E2E validation / Docker live models (Anthropic): failure - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580769
  - Run repo/live E2E validation / Docker live suites (Docker live ACP bind): cancelled - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580811
  - Run repo/live E2E validation / Docker live suites (Docker live CLI backend): cancelled - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580833
  - Run repo/live E2E validation / Docker live models (Fireworks): failure - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580844
  - Run repo/live E2E validation / Docker live suites (Docker live gateway MiniMax): cancelled - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580847
  - Run repo/live E2E validation / Docker live models (OpenRouter): failure - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580849
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory DeepSeek/Fireworks): cancelled - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580853
  - Run repo/live E2E validation / Docker live suites (Docker live Codex harness): cancelled - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580878
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Anthropic): cancelled - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580894
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory xAI/Z.ai): cancelled - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580910
  - Run repo/live E2E validation / Docker live suites (Docker live gateway advisory OpenCode/OpenRouter): cancelled - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580920
  - Run repo/live E2E validation / Docker live suites (Docker live gateway OpenAI): cancelled - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580943
  - Run repo/live E2E validation / Docker live models (MiniMax): failure - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555580969
  - Run repo/live E2E validation / Docker live suites (Docker live gateway Google): cancelled - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555581003
  - Run Docker release-path validation / Docker E2E (package/update core): failure - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75555916807
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor): failure - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75556015834
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-restart-auth): failure - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75556015853
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch): failure - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75556015862
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75557392644
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25730557051/job/75563830848

## Notes

Automatically requested by Full Release Validation 25730533795 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

