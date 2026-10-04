# OpenClaw Release Evidence: octopool-0.9.5

Generated: 2026-10-04T00:24:06.926Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.9.5` |
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
| Advisory | 1 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | blocking | `ci` | CI | `main` | `f1824df9d8ec` | 8m 49s | 14m 8s | 3s | [37163967837](https://github.com/openclaw/octopool/actions/runs/37163967837) | 0 |
| pass | blocking | `release` | release | `v0.9.5` | `f1824df9d8ec` | 1m 17s | 1m 13s | 3s | [37163988667](https://github.com/openclaw/octopool/actions/runs/37163988667) | 0 |
| pass | blocking | `homebrew-tap` | Update octopool for v0.9.5 (request-id=octopool-0.9.5-4da97c46102f; source-tag-object=dc088b074e55376ac82bc8cb009ce297cc5b4431; source-tag-commit=f1824df9d8eccd29c4caea969469a8d259082221) | `main` | `b0e5bd0d380c` | 1m 23s | 1m 14s | 8s | [37164462948](https://github.com/openclaw/homebrew-tap/actions/runs/37164462948) | 0 |
| pass | advisory | `codeql` | Push on main | `main` | `f1824df9d8ec` | 1m 51s | 3m 43s | 4s | [37163967361](https://github.com/openclaw/octopool/actions/runs/37163967361) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 8m 46s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/37163967837/job/111322984708) |
| 5m 22s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/37163967837/job/111322984834) |
| 1m 48s | `codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/37163967361/job/111322985325) |
| 1m 17s | `codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/37163967361/job/111322985219) |
| 1m 14s | `homebrew-tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/37164462948/job/111324435131) |
| 1m 13s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/37163988667/job/111323047265) |
| 38s | `codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/37163967361/job/111322985350) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 8s | 1m 14s | `homebrew-tap` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/37164462948/job/111324435131) |
| 4s | 38s | `codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/37163967361/job/111322985350) |
| 3s | 8m 46s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/37163967837/job/111322984708) |
| 3s | 1m 13s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/37163988667/job/111323047265) |
| 3s | 1m 17s | `codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/37163967361/job/111322985219) |
| 3s | 1m 48s | `codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/37163967361/job/111322985325) |
| 2s | 5m 22s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/37163967837/job/111322984834) |

## Notes

Octopool 0.9.5 (Go CLI; Worker changes already deployed from main b6e5a35; maintainers pool allow_search enabled).
Tag: v0.9.5 (annotated, SSH-signed; tag object dc088b074e55376ac82bc8cb009ce297cc5b4431, commit f1824df9d8eccd29c4caea969469a8d259082221).
Release: https://github.com/openclaw/octopool/releases/tag/v0.9.5 (body verified identical to the CHANGELOG 0.9.5 section).
Darwin signing: Developer ID Application: OpenClaw Foundation (FWJYW4S8P8), hardened runtime, timestamped; notarized arm64 f1272e09-2d6a-4b38-b33c-2f0bc66bf5fc and amd64 23484839-8510-449f-9a6a-2f16dabf1a6b (both Accepted); spctl: Notarized Developer ID.
Signed darwin archives re-uploaded with updated checksums.txt; downloaded copies verified with shasum -c.
SHA-256: darwin_arm64 c597d52dd4a41e9b650a3b12d796edf685674bfec904b812e7c8e73e3cb7deb5, darwin_amd64 df4d542e17578f2660c7a4ccfb83fa897fce98ed7419a8e77d87fed904cad250, linux_arm64 84aabc2ad6ea392d2e65b4ea3f3552edbb288c25953590aa99545f0a8b712530, linux_amd64 f8e51a724ad3fb84dca2b46f3c8988a8a710790ff9dd7cde9524d967435c8507.
Homebrew: openclaw/homebrew-tap Formula/octopool.rb at version 0.9.5 with the signed hashes (request-id octopool-0.9.5-4da97c46102f).
Fleet: brew upgrade on 6 Macs, each reporting octopool 0.9.5 (f1824df). steipete-mbp unreachable over SSH (port 22 timeout); still pending.
Includes #222, #223, #224, #225, #226; release prep #227.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

