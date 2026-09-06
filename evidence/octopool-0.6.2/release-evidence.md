# OpenClaw Release Evidence: octopool-0.6.2

Generated: 2026-09-06T05:04:09.705Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.6.2` |
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
| pass | blocking | `ci` | CI | `codex/octopool-policy-timeout` | `595fbe34ef5f` | 5m 8s | 8m 27s | 3s | [34010701136](https://github.com/openclaw/octopool/actions/runs/34010701136) | 0 |
| pass | blocking | `release` | release | `v0.6.2` | `808daac2322c` | 1m 27s | 1m 24s | 2s | [34011551397](https://github.com/openclaw/octopool/actions/runs/34011551397) | 0 |
| pass | blocking | `homebrew` | Update octopool for v0.6.2 (request-id=299bed01-4e55-4b76-b24b-606e7fc1b4ad; source-tag-object=9e7245c20ca7ad289c5bb786b7c943777600223d; source-tag-commit=808daac2322c000f1acb92e92d6fb9a6a3ab6cba) | `main` | `45ea27650b43` | 1m 7s | 42s | 24s | [34012284472](https://github.com/openclaw/homebrew-tap/actions/runs/34012284472) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 5m 5s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/34010701136/job/101425890000) |
| 3m 22s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/34010701136/job/101425889834) |
| 1m 24s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/34011551397/job/101428157277) |
| 42s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/34012284472/job/101430057300) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 24s | 42s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/34012284472/job/101430057300) |
| 3s | 5m 5s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/34010701136/job/101425890000) |
| 2s | 3m 22s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/34010701136/job/101425889834) |
| 2s | 1m 24s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/34011551397/job/101428157277) |

## Notes

The generic release-ref and npm fields above are intentionally empty: the shared resolver supports only openclaw/openclaw refs and the openclaw npm package. The [Octopool release guide](https://github.com/openclaw/octopool/blob/808daac2322c000f1acb92e92d6fb9a6a3ab6cba/docs/releasing.md) requires Octopool tag, source, signing, and checksum provenance in these notes instead. The release workflow row records the verified Octopool source SHA.

## 0.6.2 - 2026-09-05

### Fixes

- Allow authoritative policy requests up to 30 seconds so slow connections do not prematurely block guarded GitHub commands; preserve earlier caller deadlines, cancellation, and fail-closed policy checks.
- Add opt-in final PR-merge route, policy, child-outcome, and bounded REST-header diagnostics without changing authentication, merge behavior, or retries or attributing historical failures.
- Identify successful relay `/rate_limit` output as pooled-reader quota rather than native-writer quota or permission proof, preserving JSON stdout and quiet native probes.

### Upgrade notes

- This is a CLI-only patch release; no Worker deployment or database migration is required.


Release: https://github.com/openclaw/octopool/releases/tag/v0.6.2
Source: https://github.com/openclaw/octopool/commit/808daac2322c000f1acb92e92d6fb9a6a3ab6cba
PR: https://github.com/openclaw/octopool/pull/127

GitHub verifies annotated tag object 9e7245c20ca7ad289c5bb786b7c943777600223d pointing to 808daac2322c000f1acb92e92d6fb9a6a3ab6cba. All six final public archives match checksums.txt; Linux and Windows bytes are unchanged from GoReleaser. Both Darwin executables carry the OpenClaw Foundation Developer ID, hardened runtime, accepted Apple notarization, and pass Gatekeeper as Notarized Developer ID after re-download.

Final checksums: https://github.com/openclaw/octopool/releases/download/v0.6.2/checksums.txt

```text
58fe7ea8ba7b926e5a1c9f517199b4bdbc72c26c5c8d090148c3d9047e8623c5  octopool_0.6.2_darwin_amd64.tar.gz
2a8d8de87faf4414aa4cd5911352645831958594564e71b6f56e2de3dbcb695a  octopool_0.6.2_darwin_arm64.tar.gz
5650248cf729c740d8cbbb8d0688430cca852fc74ed04548fa9cb119a57fe3d5  octopool_0.6.2_linux_amd64.tar.gz
49c62b17c94d57f6f36f062a01db0003913dcf8494948fdae8693057164fff7e  octopool_0.6.2_linux_arm64.tar.gz
4676099234c6b37ff094987856ba333fba0463f1773966bbf984194108ad7e54  octopool_0.6.2_windows_amd64.zip
991c0f3cf3125947b0cc006bd328da471df99f5cd3d86675c741aa552761c9d2  octopool_0.6.2_windows_arm64.zip
```

Darwin arm64: notarization c722e3a4-1ffe-4f14-98ad-fca0261d77f4 Accepted; binary SHA-256 07109c04ce4e74a97cb0f95c3170bead51bdaaa0e8107e0a7acc4aad39816600.

Darwin amd64: notarization 2d07276e-05ad-4b43-881b-ee2c9e15ccd6 Accepted; binary SHA-256 8b94764e6ede40685597321e690b2995cf360142dbc4e024971314233aeec8bf.

The final Homebrew formula matches independently reviewed blob 647aa8409ebdd09bc3917f334592c1eb6cf5ad7b, published at 38ae9c4802c477b286fa8deab4e4434f5840956e.

Validation: full local pnpm check passed 983 unit tests and 958 Worker integration tests, build/types, Go suite and vet; Linux and Windows CI passed. Real TCP/HTTP loopback proof used the released 0.6.1 and candidate production policy client: a six-second response failed at 5.021s before and succeeded at 7.433s after; a 31-second response still timed out at 30.024s. Earlier caller deadlines and cancellation remain covered. The public release binary passed a live relay-only repository read.

The additional CLI-to-local-Worker network smoke initially failed because GitHub anonymous quota was exhausted, producing no_identity and no cache entry. The unchanged smoke passed after the natural quota reset with fresh local state, proving a token-free miss followed by a D1/edge hit. No credential, policy, or code workaround was applied. This is a CLI-only release with no Worker deployment or database migration.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

