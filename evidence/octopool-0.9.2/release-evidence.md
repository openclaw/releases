# OpenClaw Release Evidence: octopool-0.9.2

Generated: 2026-09-29T05:08:04.427Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.9.2` |
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
| pass | blocking | `ci` | CI | `main` | `1940d9bc05a1` | 8m 36s | 14m 18s | 2s | [36523449664](https://github.com/openclaw/octopool/actions/runs/36523449664) | 0 |
| pass | blocking | `release` | release | `v0.9.2` | `1940d9bc05a1` | 1m 36s | 1m 33s | 2s | [36523462920](https://github.com/openclaw/octopool/actions/runs/36523462920) | 0 |
| pass | blocking | `tap` | Update octopool for v0.9.2 (request-id=octopool-0.9.2-d5e9575e9dae; source-tag-object=833fc1e62769e6c27c300f5ff841fbf9551717ad; source-tag-commit=1940d9bc05a1276d1cd5ecb6d65a58356dd679c2) | `main` | `eb46e681cbb6` | 1m 30s | 1m 22s | 7s | [36524146210](https://github.com/openclaw/homebrew-tap/actions/runs/36524146210) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 8m 33s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/36523449664/job/109261170517) |
| 5m 45s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/36523449664/job/109261170363) |
| 1m 33s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/36523462920/job/109261210410) |
| 1m 22s | `tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/36524146210/job/109263335453) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 7s | 1m 22s | `tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/36524146210/job/109263335453) |
| 2s | 5m 45s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/36523449664/job/109261170363) |
| 2s | 8m 33s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/36523449664/job/109261170517) |
| 2s | 1m 33s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/36523462920/job/109261210410) |

## Notes

Octopool 0.9.2 (Go CLI; Worker changes already deployed).
Tag: v0.9.2 (annotated, SSH-signed; tag object 833fc1e62769e6c27c300f5ff841fbf9551717ad, commit 1940d9bc05a1276d1cd5ecb6d65a58356dd679c2).
Release: https://github.com/openclaw/octopool/releases/tag/v0.9.2 (body verified identical to the CHANGELOG 0.9.2 section).
Darwin signing: Developer ID Application: OpenClaw Foundation (FWJYW4S8P8), hardened runtime, secure timestamp; notarization Accepted (arm64 1e936c21-57a9-4b6a-8cbc-74b6fc97d360, amd64 e376d0ab-c860-452c-a976-bbfd27f55557); spctl: Notarized Developer ID on the re-downloaded asset.
Final checksums (post-signing): darwin_arm64 c79d826b643f022e382938c2563b0d1ab92b19a63cf4cfad90a806c3c8dbea64, darwin_amd64 716ac8b85be2b78fdc7d8da4351a900dff1d4979b54e948b53bdc33d9a2850f8; all six assets re-verified with shasum -c.
Homebrew: openclaw/homebrew-tap Formula/octopool.rb 0.9.2 (commit d0b0f50), all four platform sha256 values verified.
Worker: deployed from main ec12442 (version f348b26c-2991-4519-9021-12217fa01d6f) with D1 migrations 0023 and 0024 applied; the release commit changes only CHANGELOG.md. Live proof: run_list_superset, run_jobs_superset, and stale_while_revalidate audit markers observed on real reads.
Fleet: clawstudio, steipete-studio-sf, steipete-mbp-4, steipete-mini-sf, megaclaw, miniclaw, steipete-studio-sf-worker report octopool 0.9.2 (1940d9b) and relay with OCTOPOOL_NO_FALLBACK=1.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

