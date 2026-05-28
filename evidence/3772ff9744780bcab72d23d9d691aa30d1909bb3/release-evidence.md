# OpenClaw Release Evidence: 3772ff9744780bcab72d23d9d691aa30d1909bb3

Generated: 2026-05-09T17:57:14.763Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `3772ff9744780bcab72d23d9d691aa30d1909bb3` |
| Release ref input | `3772ff9744780bcab72d23d9d691aa30d1909bb3` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `3772ff9744780bcab72d23d9d691aa30d1909bb3` |
| Release ref SHA | `3772ff9744780bcab72d23d9d691aa30d1909bb3` |
| Runs at release SHA | `full-release-validation`, `normal-ci`, `release-checks`, `postpublish-telegram` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 1 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `release-ci/3772ff974478-1778348032273` | `3772ff974478` | 22m 54s | 1h 5m 7s | 22m 26s | [25607388639](https://github.com/openclaw/openclaw/actions/runs/25607388639) | 1 |
| running | blocking | `normal-ci` | CI | `release-ci/3772ff974478-1778348032273` | `3772ff974478` | 19s | 1h 10m 32s | 2m 47s | [25607395371](https://github.com/openclaw/openclaw/actions/runs/25607395371) | 4 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `release-ci/3772ff974478-1778348032273` | `3772ff974478` | 22m 14s | 6h 53m 50s | 22m 10s | [25607397201](https://github.com/openclaw/openclaw/actions/runs/25607397201) | 47 |
| pass | blocking | `postpublish-telegram` | NPM Telegram Beta E2E | `release-ci/3772ff974478-1778348032273` | `3772ff974478` | 3m 15s | 2m 59s | 15s | [25607453826](https://github.com/openclaw/openclaw/actions/runs/25607453826) | 1 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 22m 9s | `full-release-validation` | Run normal full CI | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607388639/job/75171558834) |
| 22m 1s | `full-release-validation` | Run release/live/Docker/QA validation | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607388639/job/75171558839) |
| 19m 38s | `release-checks` | Run repo/live E2E validation / validate_release_live_cache | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171703669) |
| 16m 54s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171808802) |
| 15m 6s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15) | cancelled | [job](https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171948954) |
| 14m 56s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171808793) |
| 14m 3s | `release-checks` | cross_os_release_checks / Linux / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171808792) |
| 13m 49s | `full-release-validation` | Run plugin prerelease validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607388639/job/75171558840) |
| 12m 40s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171949775) |
| 11m 51s | `release-checks` | cross_os_release_checks / Windows / packaged fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171808788) |
| 11m 42s | `release-checks` | cross_os_release_checks / Linux / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171808795) |
| 11m 30s | `release-checks` | cross_os_release_checks / macOS / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171808807) |
| 11m 28s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171949781) |
| 3m 48s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607388639/job/75171713624) |
| 3m 5s | `normal-ci` | android-test-third-party | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607395371/job/75171583406) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 22m 26s | 27s | `full-release-validation` | Verify full validation | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25607388639/job/75172879962) |
| 22m 10s | 3s | `release-checks` | Verify release checks | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75172889344) |
| 22m 2s | 6s | `release-checks` | Run package acceptance / Verify package acceptance | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75172882569) |
| 6m 56s | 4m 6s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.4) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171948951) |
| 6m 56s | 4m 44s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.5.5) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171948968) |
| 6m 56s | 1m 43s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update Anthropic install) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171949771) |
| 6m 56s | 12m 40s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime services) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171949775) |
| 6m 56s | 11m 28s | `release-checks` | Run Docker release-path validation / Docker E2E (package/update OpenAI install) | failure | [job](https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171949781) |
| 6m 56s | 1m 52s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install B) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171949784) |
| 6m 56s | 1m 33s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime plugins) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171949785) |
| 6m 56s | 1m 28s | `release-checks` | Run Docker release-path validation / Docker E2E (plugins/runtime install E) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171949786) |
| 2m 59s | 3m 48s | `full-release-validation` | Run package Telegram E2E | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607388639/job/75171713624) |
| 2m 47s | 4s | `normal-ci` | checks-node-core | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607395371/job/75171720322) |
| 2m 8s | 2s | `normal-ci` | check-additional | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607395371/job/75171685307) |
| 2m 3s | 4s | `normal-ci` | check | success | [job](https://github.com/openclaw/openclaw/actions/runs/25607395371/job/75171681008) |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607388639
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607388639/job/75171558834
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607388639/job/75171558839
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25607388639/job/75172879962
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607397201
  - Run repo/live E2E validation / validate_release_live_cache: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171703669
  - cross_os_release_checks / Windows / packaged upgrade: cancelled - https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171808802
  - Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor-2026.4.15): cancelled - https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171948954
  - Run Docker release-path validation / Docker E2E (plugins/runtime services): failure - https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171949775
  - Run Docker release-path validation / Docker E2E (package/update OpenAI install): failure - https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75171949781
  - Run package acceptance / Verify package acceptance: failure - https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75172882569
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25607397201/job/75172889344

## Notes

Automatically requested by Full Release Validation 25607388639 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

