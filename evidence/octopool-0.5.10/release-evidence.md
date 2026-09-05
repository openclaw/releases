# OpenClaw Release Evidence: octopool-0.5.10

Generated: 2026-08-29T07:02:33.985Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.5.10` |
| Release ref input | `v0.5.10` |
| Release ref status | not-found |
| Release ref kind | unknown |
| Release ref name | unknown |
| Release ref SHA | not resolved |
| Runs at release SHA | none |
| Package spec | `octopool@0.5.10` |
| npm status | invalid |
| npm error | only openclaw package specs are supported |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 4 | 0 | 0 | 0 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | blocking | `pr-ci` | CI | `fix/rewrite-egress-hardening` | `b91bacf15490` | 2m 54s | 2m 52s | 2s | [33238404239](https://github.com/openclaw/octopool/actions/runs/33238404239) | 0 |
| pass | blocking | `release-ci` | CI | `main` | `0fefcffe638f` | 2m 32s | 2m 28s | 3s | [33239143389](https://github.com/openclaw/octopool/actions/runs/33239143389) | 0 |
| pass | blocking | `release-build` | release | `v0.5.10` | `0fefcffe638f` | 1m 25s | 1m 22s | 2s | [33239144158](https://github.com/openclaw/octopool/actions/runs/33239144158) | 0 |
| pass | blocking | `homebrew` | Update octopool for v0.5.10 (request-id=octopool-0.5.10-fqkdrc; source-tag-object=d40cde7f310cd5558e7f449a1adc8bb09244e3de; source-tag-commit=0fefcffe638fbb0ac3b9c0388ccd9ec323e43845) | `main` | `e102f010f618` | 38s | 34s | 3s | [33239582215](https://github.com/openclaw/homebrew-tap/actions/runs/33239582215) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 2m 52s | `pr-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/33238404239/job/99063379298) |
| 2m 28s | `release-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/33239143389/job/99065334283) |
| 1m 22s | `release-build` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/33239144158/job/99065336279) |
| 34s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/33239582215/job/99066490982) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 3s | 2m 28s | `release-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/33239143389/job/99065334283) |
| 3s | 34s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/33239582215/job/99066490982) |
| 2s | 2m 52s | `pr-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/33238404239/job/99063379298) |
| 2s | 1m 22s | `release-build` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/33239144158/job/99065336279) |

## Notes

## Octopool 0.5.10 verification

Release: https://github.com/openclaw/octopool/releases/tag/v0.5.10

Source commit: `0fefcffe638fbb0ac3b9c0388ccd9ec323e43845`. Annotated SSH-signed tag object: `d40cde7f310cd5558e7f449a1adc8bb09244e3de`; GitHub reports the signature verified/valid. The merged hardening PR is https://github.com/openclaw/octopool/pull/68 and its real isolated Cloudflare/GitHub proof is https://github.com/openclaw/octopool/pull/68#issuecomment-5460854970.

Both Darwin binaries are signed by `Developer ID Application: OpenClaw Foundation (FWJYW4S8P8)`, notarization was Accepted, and Gatekeeper reports Notarized Developer ID. All six final archives and the checksum manifest were redownloaded after signing/publication and matched their GitHub SHA-256 digests. Final checksum-manifest SHA-256: `ece387fc0e198a60b8271cdba69ad025f256db0ce382cf36db1c4e5c7c5151a0`.

| Platform | Final archive SHA-256 |
|---|---|
| darwin_arm64 | `db691bf06fed777578ad4419e0d1a7bc70ffff1b946a552ba85533d390d63280` |
| darwin_amd64 | `508a3ec4d273074bfb301589886ccf7e7e153868d3926a6fac30d9da479fbb74` |
| linux_arm64 | `9ec3d4fa20a68f7be052c0711ed221434cfa6a375a35bece328ae87230e2661a` |
| linux_amd64 | `c54acc9c7bd60ee3e7188bc1756dfdfe5c5dcee7f74729ecd87928b345321340` |
| windows_arm64 | `f926397ff31072488f78dda25180b5307ddd9dbf8a816136c1d829c5976c546b` |
| windows_amd64 | `ccb726c5b51eb36ae1dccef67d28520c44f4c8b770b10cfabd1e736846a517b2` |

The verified-hash Homebrew update produced commit `4ddb88877205b012276afcfbd2239f0f6f276ae8` in openclaw/homebrew-tap. Its four archive hashes match the final signed/publication inventory. The authoritative Worker was deployed from the release commit; both public hosts passed discovery, and production normal-relay and literal-tab-denial checks passed without changing policy configuration. The unchanged forwarding proxy did not require redeployment.

Local validation passed 501 unit tests, 180 Worker integration tests, Go tests/vet/race, documentation generation and blocking-priority independent review. Seven live-observable contract groups passed against a real isolated Worker and real GitHub publications/readbacks. Instrumented subprocess/Worker tests separately establish zero-child/zero-fetch properties; an HTTP denial alone is not claimed to be a live packet trace.

Octopool is a Go CLI, not an npm publication. The generic evidence collector resolves release refs against openclaw/openclaw and package specs through npm; any not-found/unsupported result for those optional Octopool inputs is a collector scope limitation, not a failed Octopool release. The repository-specific tag, Release, artifacts and workflow proof above are authoritative.

## 0.5.10 - 2026-08-28

### Fixes

- Reject native-gh endpoint placeholders under active rewrite policy, guard canonical relay egress and derived probes, and block recognizable active rule JSON in supported submissions while preserving ordinary prose rewrites; existing broad rules matching fixed transport text can now deny additional requests, so review them before upgrading.
- Normalize `gh pr view --json mergeable` to `MERGEABLE`, `CONFLICTING`, or `UNKNOWN` before filtering and `--jq`, preserving raw `gh api` REST values and unsupported-field delegation; scripts relying on older boolean/null output must migrate to explicit enum comparisons.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

