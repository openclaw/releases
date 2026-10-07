# OpenClaw Release Evidence: octopool-0.9.7

Generated: 2026-10-07T05:10:00.078Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.9.7` |
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
| pass | blocking | `ci-release-gate` | CI | `chore/release-0.9.7` | `e5e3a700d1f4` | 9m 12s | 14m 40s | 4s | [37573101653](https://github.com/openclaw/octopool/actions/runs/37573101653) | 0 |
| pass | blocking | `ci` | CI | `main` | `8cf959361f8f` | 9m 9s | 13m 17s | 3s | [37573919635](https://github.com/openclaw/octopool/actions/runs/37573919635) | 0 |
| pass | blocking | `release` | release | `v0.9.7` | `8cf959361f8f` | 1m 17s | 1m 15s | 2s | [37573944913](https://github.com/openclaw/octopool/actions/runs/37573944913) | 0 |
| pass | blocking | `homebrew-tap` | Update octopool for v0.9.7 (request-id=octopool-0.9.7-78dd3d3d947d; source-tag-object=35fbe27a55dfc08b70c5a2165e984ce6a5224f81; source-tag-commit=8cf959361f8f69aef82d169f816d41a2e8974193) | `main` | `b9b890be1ac7` | 1m 25s | 1m 16s | 8s | [37574608095](https://github.com/openclaw/homebrew-tap/actions/runs/37574608095) | 0 |
| pass | advisory | `codeql` | Push on main | `main` | `8cf959361f8f` | 1m 51s | 3m 43s | 4s | [37573919050](https://github.com/openclaw/octopool/actions/runs/37573919050) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 9m 7s | `ci-release-gate` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/37573101653/job/112635921322) |
| 9m 5s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/37573919635/job/112638451871) |
| 5m 33s | `ci-release-gate` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/37573101653/job/112635921655) |
| 4m 12s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/37573919635/job/112638451576) |
| 1m 46s | `codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/37573919050/job/112638453769) |
| 1m 16s | `homebrew-tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/37574608095/job/112640587680) |
| 1m 15s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/37573944913/job/112638529329) |
| 1m 9s | `codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/37573919050/job/112638453613) |
| 48s | `codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/37573919050/job/112638453332) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 8s | 1m 16s | `homebrew-tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/37574608095/job/112640587680) |
| 4s | 9m 7s | `ci-release-gate` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/37573101653/job/112635921322) |
| 4s | 5m 33s | `ci-release-gate` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/37573101653/job/112635921655) |
| 4s | 48s | `codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/37573919050/job/112638453332) |
| 4s | 1m 46s | `codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/37573919050/job/112638453769) |
| 3s | 4m 12s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/37573919635/job/112638451576) |
| 3s | 9m 5s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/37573919635/job/112638451871) |
| 3s | 1m 9s | `codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/37573919050/job/112638453613) |
| 2s | 1m 15s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/37573944913/job/112638529329) |

## Notes

Octopool 0.9.7 (Go CLI; Worker change already deployed from main fb72d9f).
Tag: v0.9.7 (annotated, SSH-signed; tag object 35fbe27a55dfc08b70c5a2165e984ce6a5224f81, commit 8cf959361f8f69aef82d169f816d41a2e8974193).
Release: https://github.com/openclaw/octopool/releases/tag/v0.9.7 (staged as draft by GoReleaser, published after verification; body verified identical to the CHANGELOG 0.9.7 section).
Release gate: CI workflow_dispatch on release-prep commit e5e3a700d1f4 (tree identical to the merge commit) passed including the CLI to Worker release smoke (run 37573101653).
Darwin signing: Developer ID Application: OpenClaw Foundation (FWJYW4S8P8), hardened runtime, timestamped; notarized arm64 2e38df11-e50a-418b-a7d1-e8618146f229 and amd64 b396ebd2-c396-4a26-82c0-432231e6e245 (both Accepted); codesign --check-notarization ok; spctl: Notarized Developer ID.
Final assets re-downloaded into a clean directory: all six archives pass shasum -c; both darwin binaries verified (strict + notarized requirement).
SHA-256: darwin_arm64 9c7c1d411d21a5c67d935f789821ebe0dab5c9e6780cd447afaca4e533a3ab44, darwin_amd64 da340e0e00d8db329ec5bf4cb5fe8b8f6005c0eacb01f301b0622feb976d0903, linux_arm64 d44833783161b0655240ed650961c53351faf5d518ab388c97a147aa7317315a, linux_amd64 35f1501739757358a8283119dbdafc8e456618ec5d1fdcc6d21f422d03531f19.
Homebrew: openclaw/homebrew-tap Formula/octopool.rb at 0.9.7 with the final hashes (request-id octopool-0.9.7-78dd3d3d947d).
Fleet: brew upgrade on 6 Macs (clawstudio, steipete-studio-sf, steipete-mini-sf, steipete-studio-sf-worker, miniclaw, steipete-mbp-4) each reporting octopool 0.9.7 (8cf9593) and relaying with OCTOPOOL_NO_FALLBACK=1. megaclaw unreachable over SSH (port 22 timeout); pending.
Includes #228 and #229 by @SebTardif; release prep #233.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

