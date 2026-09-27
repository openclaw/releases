# OpenClaw Release Evidence: octopool-0.9.0

Generated: 2026-09-27T19:05:04.067Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.9.0` |
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
| Blocking | 3 | 0 | 0 | 0 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | blocking | `ci` | CI | `main` | `425f2f278514` | 7m 55s | 13m 16s | 2s | [36341596743](https://github.com/openclaw/octopool/actions/runs/36341596743) | 0 |
| pass | blocking | `release` | release | `v0.9.0` | `425f2f278514` | 1m 11s | 1m 8s | 2s | [36341609712](https://github.com/openclaw/octopool/actions/runs/36341609712) | 0 |
| pass | blocking | `tap` | Update octopool for v0.9.0 (request-id=octopool-0.9.0-e31d60cc4928; source-tag-object=a95714ccef730b9d6254415faf1036df6d8bedc1; source-tag-commit=425f2f278514974cf35bf1bf51f24985eb9c316d) | `main` | `180f773f9507` | 1m 37s | 1m 29s | 7s | [36342397284](https://github.com/openclaw/homebrew-tap/actions/runs/36342397284) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 7m 52s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/36341596743/job/108682641684) |
| 5m 24s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/36341596743/job/108682641449) |
| 1m 29s | `tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/36342397284/job/108684905291) |
| 1m 8s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/36341609712/job/108682676061) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 7s | 1m 29s | `tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/36342397284/job/108684905291) |
| 2s | 5m 24s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/36341596743/job/108682641449) |
| 2s | 7m 52s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/36341596743/job/108682641684) |
| 2s | 1m 8s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/36341609712/job/108682676061) |

## Notes

Octopool 0.9.0 (Go CLI + Cloudflare Worker).
Tag: v0.9.0 (annotated, SSH-signed; tag object a95714ccef730b9d6254415faf1036df6d8bedc1, commit 425f2f278514974cf35bf1bf51f24985eb9c316d).
Release: https://github.com/openclaw/octopool/releases/tag/v0.9.0 (body verified identical to the CHANGELOG 0.9.0 section).
Darwin signing: Developer ID Application: OpenClaw Foundation (FWJYW4S8P8), hardened runtime, secure timestamp; notarization Accepted (arm64 9dfbbea5-fb5c-4b5e-ab10-8b3da30513ee, amd64 c6e21f01-71eb-4fc3-9d0a-c75420c238c9); spctl: Notarized Developer ID on the re-downloaded release asset.
Final checksums.txt (post-signing): darwin_arm64 a2b7786aa6cc03a9d7911a41bbd8bcc579ffc9f179d15a616c788f66354000d6, darwin_amd64 1f052cf3e153ff1de1d3993e21fa99060f05ebea5942aacbce38096b68b567fc; all six assets re-verified with shasum -c after upload.
Homebrew: openclaw/homebrew-tap Formula/octopool.rb 0.9.0 (commit 742a697) with the final hashes (all four platform sha256 values verified).
Worker: octopool + octopool-public-proxy already deployed from main 22ea31a (versions 83a0e678-e2cc-44a4-a9c7-942126893d56, 7bb2fcf3-08e6-4695-8255-a83b188ca7fc); D1 migrations 0021/0022 and Durable Object migrations v2/v3 applied; the release commit changes only CHANGELOG.md.
Fleet: clawstudio, steipete-studio-sf, steipete-mbp-4, steipete-mini-sf, megaclaw, miniclaw, steipete-studio-sf-worker all report octopool 0.9.0 (425f2f2) and relay with OCTOPOOL_NO_FALLBACK=1.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

