# OpenClaw Release Evidence: octopool-0.9.10

Generated: 2026-10-25T01:21:42.289Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.9.10` |
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
| pass | blocking | `ci-release-gate` | CI | `chore/release-0.9.10` | `0ab7ab4138e0` | 4m 24s | 11m 13s | 4m 20s | [40140423847](https://github.com/openclaw/octopool/actions/runs/40140423847) | 0 |
| pass | blocking | `ci` | CI | `main` | `78b159d4be4e` | 4m 57s | 12m 36s | 4m 53s | [40141189469](https://github.com/openclaw/octopool/actions/runs/40141189469) | 0 |
| pass | blocking | `release` | release | `v0.9.10` | `78b159d4be4e` | 1m 46s | 1m 43s | 2s | [40141628119](https://github.com/openclaw/octopool/actions/runs/40141628119) | 0 |
| pass | blocking | `homebrew-tap` | Update octopool for v0.9.10 (request-id=octopool-0.9.10-57746e17c5c5; source-tag-object=9c182db080fe31bdd13ff757a36363db3d655f4b; source-tag-commit=78b159d4be4ea35df72455aee29d4a9155653c3c) | `main` | `ac22b58555b8` | 50s | 45s | 4s | [40149734007](https://github.com/openclaw/homebrew-tap/actions/runs/40149734007) | 0 |
| pass | advisory | `codeql` | Push on main | `main` | `78b159d4be4e` | 2m 2s | 4m 3s | 3s | [40141188988](https://github.com/openclaw/octopool/actions/runs/40141188988) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 4m 48s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/40141189469/job/121013097006) |
| 4m 15s | `ci-release-gate` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/40140423847/job/121010814428) |
| 3m 45s | `ci` | Worker checks | success | [job](https://github.com/openclaw/octopool/actions/runs/40141189469/job/121013097203) |
| 3m 37s | `ci` | Linux Go suite | success | [job](https://github.com/openclaw/octopool/actions/runs/40141189469/job/121013097249) |
| 3m 23s | `ci-release-gate` | Linux Go suite | success | [job](https://github.com/openclaw/octopool/actions/runs/40140423847/job/121010814406) |
| 3m 5s | `ci-release-gate` | Worker checks | success | [job](https://github.com/openclaw/octopool/actions/runs/40140423847/job/121010814395) |
| 1m 58s | `codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/40141188988/job/121013098420) |
| 1m 43s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/40141628119/job/121014396340) |
| 1m 18s | `codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/40141188988/job/121013098245) |
| 47s | `codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/40141188988/job/121013098428) |
| 45s | `homebrew-tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/40149734007/job/121038548714) |
| 27s | `ci-release-gate` | Release snapshot | success | [job](https://github.com/openclaw/octopool/actions/runs/40140423847/job/121010814246) |
| 22s | `ci` | Release snapshot | success | [job](https://github.com/openclaw/octopool/actions/runs/40141189469/job/121013097182) |
| 4s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/40141189469/job/121014101451) |
| 3s | `ci-release-gate` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/40140423847/job/121011668570) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 4m 53s | 4s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/40141189469/job/121014101451) |
| 4m 20s | 3s | `ci-release-gate` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/40140423847/job/121011668570) |
| 4s | 45s | `homebrew-tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/40149734007/job/121038548714) |
| 3s | 27s | `ci-release-gate` | Release snapshot | success | [job](https://github.com/openclaw/octopool/actions/runs/40140423847/job/121010814246) |
| 3s | 3m 5s | `ci-release-gate` | Worker checks | success | [job](https://github.com/openclaw/octopool/actions/runs/40140423847/job/121010814395) |
| 3s | 3m 23s | `ci-release-gate` | Linux Go suite | success | [job](https://github.com/openclaw/octopool/actions/runs/40140423847/job/121010814406) |
| 3s | 4m 15s | `ci-release-gate` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/40140423847/job/121010814428) |
| 3s | 22s | `ci` | Release snapshot | success | [job](https://github.com/openclaw/octopool/actions/runs/40141189469/job/121013097182) |
| 3s | 3m 45s | `ci` | Worker checks | success | [job](https://github.com/openclaw/octopool/actions/runs/40141189469/job/121013097203) |
| 3s | 1m 18s | `codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/40141188988/job/121013098245) |
| 3s | 1m 58s | `codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/40141188988/job/121013098420) |
| 3s | 47s | `codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/40141188988/job/121013098428) |
| 2s | 4m 48s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/40141189469/job/121013097006) |
| 2s | 3m 37s | `ci` | Linux Go suite | success | [job](https://github.com/openclaw/octopool/actions/runs/40141189469/job/121013097249) |
| 2s | 1m 43s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/40141628119/job/121014396340) |

## Notes

Octopool 0.9.10 (Go CLI + Worker).
Tag: v0.9.10 (annotated, SSH-signed; tag object 9c182db080fe31bdd13ff757a36363db3d655f4b, commit 78b159d4be4ea35df72455aee29d4a9155653c3c).
Release: https://github.com/openclaw/octopool/releases/tag/v0.9.10 (staged as draft by GoReleaser, published after verification; body verified identical to the CHANGELOG 0.9.10 section).
Release gate: CI workflow_dispatch on release-prep commit 0ab7ab4 (tree identical to merge commit 78b159d) passed including the CLI to Worker release smoke (run 40140423847); push CI on 78b159d green (run 40141189469).
Darwin signing: Developer ID Application: OpenClaw Foundation (FWJYW4S8P8), hardened runtime, timestamped; notarized arm64 b0c6b770-a42f-4a72-8d36-4209f0251b89 and amd64 d4092213-abfb-45e4-9967-7dbf7c5bae69 (both Accepted on first attempt, per-arch submission); codesign --check-notarization ok.
Final assets re-downloaded into a clean directory: all six archives pass shasum -c; both darwin binaries verified (strict + notarized requirement, team FWJYW4S8P8) and report octopool 0.9.10 (78b159d), built with Go 1.26.10.
SHA-256: darwin_arm64 efa83f2a6103f0e0e0f20cb341b24d9519f358f806f1a7bfe69a25894f5169a9, darwin_amd64 581fadf4f36a6fa02bc0aa35b348e3c2c3746160466e96f6244bca315b4e6158, linux_arm64 9d42ca259bbbf6bb080c469389d8dba5af86cfb4cb514f4101f24bec7058c1b0, linux_amd64 52c9e58d025bd36184d087ef437126165ecf934483f0f31d5249c29b90d1dc9f.
Homebrew: openclaw/homebrew-tap Formula/octopool.rb at 0.9.10 with the final hashes (commit 546403e1b574, request-id octopool-0.9.10-57746e17c5c5).
Worker: no Worker deploy in this release; the Worker changes from #247, #248, #251 and #253 need no D1 migrations and are not yet deployed (latest Worker deployment 2026-10-14T03:43Z).
Fleet: brew upgrade on 6 Macs (steipete-studio-sf, clawstudio, steipete-mbp-4, steipete-mini-sf, steipete-studio-sf-worker, miniclaw) each reporting octopool 0.9.10 (78b159d), Foundation-signed and notarized, gh resolving through the shim in zsh -c and zsh -lc, relaying with OCTOPOOL_NO_FALLBACK=1, pool health 3/3. megaclaw (port 22 timeout), clawmac and the London Mac Studio (tailnet offline) unreachable; pending.
Includes #246, #247, #248, #249, #251, #253, #254, #255, #256, #257, #258, #259, #260, #261; release prep #262.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

