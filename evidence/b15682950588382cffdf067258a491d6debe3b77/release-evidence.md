# OpenClaw Release Evidence: b15682950588382cffdf067258a491d6debe3b77

Generated: 2026-05-05T01:00:56.431Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `b15682950588382cffdf067258a491d6debe3b77` |
| Release ref input | `b15682950588382cffdf067258a491d6debe3b77` |
| Release ref status | resolved |
| Release ref kind | `sha` |
| Release ref name | `b15682950588382cffdf067258a491d6debe3b77` |
| Release ref SHA | `b15682950588382cffdf067258a491d6debe3b77` |
| Runs at release SHA | `full-release-validation`, `release-checks` |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 0 | 0 | 0 |
| Advisory | 1 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | advisory | `full-release-validation` | Full Release Validation | `main` | `b15682950588` | 38m 37s | 38m 25s | 38m 29s | [25350970693](https://github.com/openclaw/openclaw/actions/runs/25350970693) | 0 |
| pass | blocking | `release-checks` | OpenClaw Release Checks | `main` | `b15682950588` | 37m 39s | 1h 19m 1s | 37m 35s | [25350983142](https://github.com/openclaw/openclaw/actions/runs/25350983142) | 25 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 38m 9s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350970693/job/74330250457) |
| 32m 18s | `release-checks` | cross_os_release_checks / Windows / packaged upgrade | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350983142/job/74330665870) |
| 2m 47s | `release-checks` | install_smoke_release_checks / installer_smoke | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350983142/job/74330621015) |
| 2m 47s | `release-checks` | cross_os_release_checks / Windows / installer fresh | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350983142/job/74330665859) |
| 2m 23s | `release-checks` | Prepare release package artifact | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350983142/job/74330382029) |
| 2m 16s | `release-checks` | Run QA Lab live Matrix lane | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350983142/job/74330382028) |
| 2m 14s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350983142/job/74330995280) |
| 2m 12s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350983142/job/74330995279) |
| 2m 4s | `release-checks` | install_smoke_release_checks / root_dockerfile_image | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350983142/job/74330400673) |
| 1m 58s | `release-checks` | Run QA Lab parity lane (baseline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350983142/job/74330382041) |
| 1m 51s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350983142/job/74330995288) |
| 8s | `full-release-validation` | Resolve target ref | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350970693/job/74330235173) |
| 8s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350970693/job/74333961327) |
| 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25350970693/job/74330250573) |
| 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25350970693/job/74330250680) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 38m 29s | 8s | `full-release-validation` | Verify full validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350970693/job/74333961327) |
| 37m 35s | 3s | `release-checks` | Verify release checks | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350983142/job/74333896236) |
| 9m 43s | 5s | `release-checks` | Run package acceptance / Verify package acceptance | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350983142/job/74331248581) |
| 7m 29s | 2m 12s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugins-offline) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350983142/job/74330995279) |
| 7m 29s | 1m 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (plugin-update) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350983142/job/74330995282) |
| 7m 28s | 1m 37s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (published-upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350983142/job/74330995271) |
| 7m 19s | 1m 41s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (upgrade-survivor) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350983142/job/74330995275) |
| 7m 19s | 2m 14s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (update-channel-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350983142/job/74330995280) |
| 7m 19s | 1m 51s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E targeted lanes (doctor-switch) | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350983142/job/74330995288) |
| 7m 18s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (${{ matrix.label }}) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25350983142/job/74330995390) |
| 7m 18s | 0s | `release-checks` | Run package acceptance / Docker product acceptance / Docker E2E (openwebui) | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25350983142/job/74330995440) |
| 19s | 38m 9s | `full-release-validation` | Run release/live/Docker/QA validation | success | [job](https://github.com/openclaw/openclaw/actions/runs/25350970693/job/74330250457) |
| 11s | 0s | `full-release-validation` | Run normal full CI | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25350970693/job/74330250573) |
| 11s | 0s | `full-release-validation` | Prepare release package artifact | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25350970693/job/74330250680) |
| 11s | 0s | `full-release-validation` | Run plugin prerelease validation | skipped | [job](https://github.com/openclaw/openclaw/actions/runs/25350970693/job/74330250738) |

## Notes

Automatically requested by Full Release Validation 25350970693 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

