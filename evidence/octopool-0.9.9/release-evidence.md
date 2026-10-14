# OpenClaw Release Evidence: octopool-0.9.9

Generated: 2026-10-14T16:13:25.904Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.9.9` |
| Release ref input | not recorded |
| Release ref status | not-recorded |
| Release ref kind | unknown |
| Release ref name | unknown |
| Release ref SHA | not resolved |
| Runs at release SHA | none |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 4 | 0 | 0 | 0 |
| Advisory | 1 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | blocking | `ci-release-gate` | CI | `chore/release-0.9.9` | `d2271494e9ee` | 4m 50s | 11m 40s | 4m 45s | [38590921705](https://github.com/openclaw/octopool/actions/runs/38590921705) | 0 |
| pass | blocking | `ci` | CI | `main` | `cb327c6f2e37` | 5m 44s | 13m 7s | 5m 40s | [38592233631](https://github.com/openclaw/octopool/actions/runs/38592233631) | 0 |
| pass | blocking | `release` | release | `v0.9.9` | `cb327c6f2e37` | 1m 16s | 1m 12s | 3s | [38592282640](https://github.com/openclaw/octopool/actions/runs/38592282640) | 0 |
| pass | blocking | `homebrew-tap` | Update octopool for v0.9.9 (request-id=octopool-0.9.9-c552e2beebae; source-tag-object=f075ec5d15faf724c75988e21da4c894b788864b; source-tag-commit=cb327c6f2e37858636014ec9c63568651bcc777d) | `main` | `2406bd8f60cb` | 1m 21s | 1m 12s | 8s | [38593631831](https://github.com/openclaw/homebrew-tap/actions/runs/38593631831) | 0 |
| pass | advisory | `codeql` | Push on main | `main` | `cb327c6f2e37` | 1m 59s | 3m 56s | 6s | [38592232080](https://github.com/openclaw/octopool/actions/runs/38592232080) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 5m 32s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/38592233631/job/115949801794) |
| 4m 32s | `ci-release-gate` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/38590921705/job/115945260682) |
| 3m 48s | `ci-release-gate` | Linux Go suite | success | [job](https://github.com/openclaw/octopool/actions/runs/38590921705/job/115945261412) |
| 3m 42s | `ci` | Linux Go suite | success | [job](https://github.com/openclaw/octopool/actions/runs/38592233631/job/115949801865) |
| 3m 31s | `ci` | Worker checks | success | [job](https://github.com/openclaw/octopool/actions/runs/38592233631/job/115949801369) |
| 2m 50s | `ci-release-gate` | Worker checks | success | [job](https://github.com/openclaw/octopool/actions/runs/38590921705/job/115945261129) |
| 1m 53s | `codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/38592232080/job/115949803196) |
| 1m 28s | `codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/38592232080/job/115949803726) |
| 1m 12s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/38592282640/job/115949969788) |
| 1m 12s | `homebrew-tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/38593631831/job/115954626437) |
| 35s | `codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/38592232080/job/115949803464) |
| 26s | `ci-release-gate` | Release snapshot | success | [job](https://github.com/openclaw/octopool/actions/runs/38590921705/job/115945261481) |
| 18s | `ci` | Release snapshot | success | [job](https://github.com/openclaw/octopool/actions/runs/38592233631/job/115949801891) |
| 4s | `ci-release-gate` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/38590921705/job/115947523284) |
| 4s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/38592233631/job/115952651116) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 5m 40s | 4s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/38592233631/job/115952651116) |
| 4m 45s | 4s | `ci-release-gate` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/38590921705/job/115947523284) |
| 8s | 1m 12s | `homebrew-tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/38593631831/job/115954626437) |
| 6s | 1m 28s | `codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/38592232080/job/115949803726) |
| 5s | 26s | `ci-release-gate` | Release snapshot | success | [job](https://github.com/openclaw/octopool/actions/runs/38590921705/job/115945261481) |
| 5s | 5m 32s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/38592233631/job/115949801794) |
| 5s | 1m 53s | `codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/38592232080/job/115949803196) |
| 5s | 35s | `codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/38592232080/job/115949803464) |
| 4s | 4m 32s | `ci-release-gate` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/38590921705/job/115945260682) |
| 4s | 2m 50s | `ci-release-gate` | Worker checks | success | [job](https://github.com/openclaw/octopool/actions/runs/38590921705/job/115945261129) |
| 4s | 3m 48s | `ci-release-gate` | Linux Go suite | success | [job](https://github.com/openclaw/octopool/actions/runs/38590921705/job/115945261412) |
| 4s | 3m 31s | `ci` | Worker checks | success | [job](https://github.com/openclaw/octopool/actions/runs/38592233631/job/115949801369) |
| 3s | 3m 42s | `ci` | Linux Go suite | success | [job](https://github.com/openclaw/octopool/actions/runs/38592233631/job/115949801865) |
| 3s | 18s | `ci` | Release snapshot | success | [job](https://github.com/openclaw/octopool/actions/runs/38592233631/job/115949801891) |
| 3s | 1m 12s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/38592282640/job/115949969788) |

## Notes

Octopool 0.9.9 (Go CLI + Worker).
Tag: v0.9.9 (annotated, SSH-signed; tag object f075ec5d15faf724c75988e21da4c894b788864b, commit cb327c6f2e37858636014ec9c63568651bcc777d).
Release: https://github.com/openclaw/octopool/releases/tag/v0.9.9 (staged as draft by GoReleaser, published after verification; body verified identical to the CHANGELOG 0.9.9 section).
Release gate: CI workflow_dispatch on release-prep commit d227149 (tree identical to merge commit cb327c6) passed including the CLI to Worker release smoke (run 38590921705); push CI on cb327c6 green (run 38592233631).
Darwin signing: Developer ID Application: OpenClaw Foundation (FWJYW4S8P8), hardened runtime, timestamped; notarized arm64 a20c990c-02c2-438f-b0b3-590c9c6eca17 and amd64 c1af378b-a94d-487f-be63-d51ada61695c (both Accepted on first attempt, per-arch submission); codesign --check-notarization ok.
Final assets re-downloaded into a clean directory: all six archives pass shasum -c; both darwin binaries verified (strict + notarized requirement, team FWJYW4S8P8).
SHA-256: darwin_arm64 8f85f9db4fe397425149d7ac85f2e0ce9dba981a8e5a6a4ba531902b4c09c339, darwin_amd64 7ef4379aba7ed9b86a2bde1203be019f277ef3dc4da183c9c19c52fc3402e74a, linux_arm64 69a36fadf4f07309ac3d3018614bdae1a5958209d433fcc5c805960820866d95, linux_amd64 136800cfe515498a5da682b269bd27bdf86cfcce18d8dc4813e3e3aa15b0d9ad.
Homebrew: openclaw/homebrew-tap Formula/octopool.rb at 0.9.9 with the final hashes (request-id octopool-0.9.9-c552e2beebae).
Worker: no Worker deploy in this release; the Worker changes (admission headroom, batched cache reads, phase timing with D1 migration 0025_audit_timings) were already deployed from main at 5a8dc64.
Fleet: brew upgrade on 5 Macs (clawstudio, steipete-studio-sf, steipete-mbp-4, steipete-mini-sf, miniclaw) each reporting octopool 0.9.9 (cb327c6), relaying with OCTOPOOL_NO_FALLBACK=1, and serving gh pr view --json mergeStateStatus and gh issue view --json stateReason through the relay with zero new native delegations. steipete-studio-sf-worker (TCP 22 closed on the tailnet, LAN publickey refused) and megaclaw (port 22 timeout) unreachable; pending.
Includes #239, #240, #241, #242, #243, #244; release prep #245.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

