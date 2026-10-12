# OpenClaw Release Evidence: octopool-0.9.8

Generated: 2026-10-12T00:01:22.349Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.9.8` |
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
| pass | blocking | `ci-release-gate` | CI | `chore/release-0.9.8` | `0f9fd4fa9d03` | 9m 14s | 14m 30s | 4s | [38176371029](https://github.com/openclaw/octopool/actions/runs/38176371029) | 0 |
| pass | blocking | `ci` | CI | `main` | `d2e57a222a9d` | 9m 13s | 14m 57s | 3s | [38178601596](https://github.com/openclaw/octopool/actions/runs/38178601596) | 0 |
| pass | blocking | `release` | release | `v0.9.8` | `d2e57a222a9d` | 1m 26s | 1m 24s | 2s | [38178619948](https://github.com/openclaw/octopool/actions/runs/38178619948) | 0 |
| pass | blocking | `homebrew-tap` | Update octopool for v0.9.8 (request-id=octopool-0.9.8-51e5fb3b0ace; source-tag-object=9dc7a7c7d591523bef923300ef2c1ceb89ab3059; source-tag-commit=d2e57a222a9d218516485b5ff0ea206651fe16a6) | `main` | `2486c5fe48da` | 1m 26s | 1m 19s | 6s | [38181611056](https://github.com/openclaw/homebrew-tap/actions/runs/38181611056) | 0 |
| pass | advisory | `codeql` | Push on main | `main` | `d2e57a222a9d` | 1m 49s | 4m 7s | 4s | [38178601536](https://github.com/openclaw/octopool/actions/runs/38178601536) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 9m 11s | `ci-release-gate` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/38176371029/job/114579515070) |
| 9m 9s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/38178601596/job/114586177790) |
| 5m 48s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/38178601596/job/114586177519) |
| 5m 19s | `ci-release-gate` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/38176371029/job/114579515351) |
| 1m 45s | `codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/38178601536/job/114586180478) |
| 1m 36s | `codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/38178601536/job/114586180357) |
| 1m 24s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/38178619948/job/114586235940) |
| 1m 19s | `homebrew-tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/38181611056/job/114595187130) |
| 46s | `codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/38178601536/job/114586180507) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 6s | 1m 19s | `homebrew-tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/38181611056/job/114595187130) |
| 4s | 5m 19s | `ci-release-gate` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/38176371029/job/114579515351) |
| 4s | 1m 36s | `codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/38178601536/job/114586180357) |
| 4s | 1m 45s | `codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/38178601536/job/114586180478) |
| 4s | 46s | `codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/38178601536/job/114586180507) |
| 3s | 9m 11s | `ci-release-gate` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/38176371029/job/114579515070) |
| 3s | 5m 48s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/38178601596/job/114586177519) |
| 3s | 9m 9s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/38178601596/job/114586177790) |
| 2s | 1m 24s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/38178619948/job/114586235940) |

## Notes

Octopool 0.9.8 (Go CLI + Worker).
Tag: v0.9.8 (annotated, SSH-signed; tag object 9dc7a7c7d591523bef923300ef2c1ceb89ab3059, commit d2e57a222a9d218516485b5ff0ea206651fe16a6).
Release: https://github.com/openclaw/octopool/releases/tag/v0.9.8 (staged as draft by GoReleaser, published after verification; body verified identical to the CHANGELOG 0.9.8 section).
Release gate: CI workflow_dispatch on release-prep commit 0f9fd4fa9d03 (tree e16c88be identical to merge commit d2e57a2) passed including the CLI to Worker release smoke (run 38176371029).
Darwin signing: Developer ID Application: OpenClaw Foundation (FWJYW4S8P8), hardened runtime, timestamped; notarized arm64 c53968b6-10c4-41fa-a240-ecb045438601 and amd64 c828a707-ff73-4470-bc1c-3ab8d6bcd75b (both Accepted); codesign --check-notarization ok. Earlier notarytool upload attempts hit HTTPClientError.deadlineExceeded (network) and were retried from the unmodified draft assets.
Final assets re-downloaded into a clean directory: all six archives pass shasum -c; both darwin binaries verified (strict + notarized requirement, team FWJYW4S8P8).
SHA-256: darwin_arm64 530a478b0cfa210481fa9b236b72a9394748c47c75287505b02d75e4485052ca, darwin_amd64 4168743f4e25565bc72670de007706ecf1dcc0547c1589d62fe51a4e07fd7b44, linux_arm64 a20c4da4c598162b490fd4c71d1a95d9ef10a914840f5a62b75a6dd56c3c8a3e, linux_amd64 016d2c3ee425638cfb2ba9658efedbcb3b2b5958beab689ec53612647f35a2f3.
Homebrew: openclaw/homebrew-tap Formula/octopool.rb at 0.9.8 with the final hashes (request-id octopool-0.9.8-51e5fb3b0ace).
Worker: deployed from d2e57a2 (octopool 713e017a-f886-4b7d-b043-63af7e4c7f76, octopool-public-proxy 141d7b58-9c90-4b5c-b9a5-fe967c24b916); no D1 migrations; relay health 3/3 identities.
Fleet: brew upgrade on 6 Macs (clawstudio, steipete-studio-sf, steipete-studio-sf-worker, steipete-mbp-4, steipete-mini-sf, miniclaw) each reporting octopool 0.9.8 (d2e57a2), relaying with OCTOPOOL_NO_FALLBACK=1 and serving gh pr diff --name-only through the relay. megaclaw unreachable over SSH (port 22 timeout); pending. Post-upgrade: zero gh pr diff native delegations on steipete-studio-sf (previously ~600-1,000/hour).
Includes #235 and #236; release prep #238.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

