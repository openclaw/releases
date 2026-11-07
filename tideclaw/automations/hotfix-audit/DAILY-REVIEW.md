# Daily hourly-audit quality review

Review and improve the hourly hotfix audit, not product code.

Workspace: <AUDIT_WORKSPACE>
Hourly job: <HOURLY_HOTFIX_AUDIT_JOB>
Instructions: .openclaw/hotfix-audit/AUTOMATION.md
Audit log: .openclaw/hotfix-audit/main-hotfix-audit.log
Review log: .openclaw/hotfix-audit/main-hotfix-audit-review.log

## Review
- Read scoped instructions and the previous review. Analyze new hourly runs since the last completed review, plus unresolved findings and a small comparison sample from earlier runs. Record exact log bounds, source SHAs and instruction hashes. If no new evidence exists, record that without inventing improvements.
- Inspect scheduler configuration, run outcomes, duration, failures and delivery receipts through supported tools when available. Distinguish successful execution from successful delivery. Use audit artifacts if scheduler access is unavailable and name that evidence gap.
- Assess throughput, backlog age, time to discovery, redundant reads/fetches, stalled large-PR reviews, recoverability and tool/token cost where actually recorded. Do not invent cost metrics or optimize throughput at the expense of coverage.
- Independently inspect pinned source diffs/owners/callers for a bounded, representative sample of both inclusions and exclusions: high-risk changes, significant P2/UX cases, mixed squash PRs and routine exclusions. Read more where discrepancies warrant it. Do not accept the hourly audit's own reasoning as ground truth. Report sample size and uncertainty; do not claim population precision/recall from a small sample.
- Check missed hotfix opportunities, unsupported inclusions, severity/urgency calibration, evidence quality, fix-level extraction scope/dependencies, canonical identity/deduplication, checkpoint continuity and verified ledger effects. Ledger reads follow the installed hotfix-ledger skill; secrets remain protected. Review judgments are not release approvals.

## Improve
- The user authorizes evidence-backed improvements to the hourly audit's instructions and workflow without asking again. Prefer small edits to AUTOMATION.md, which the hourly job reads each run. Remove redundant instructions rather than adding unbounded prompt history. Keep incident details and examples in the review log.
- Preserve the user's objective: only supported hotfix opportunities in the ledger; all P0s, most P1s and significant P2s judged by actual user harm; isolate actual fixes within squash PRs. Preserve append-only history, contiguous checkpoints, static-only inspection, credential protection, and no product edits/releases/deployments. Do not widen tool permissions, change models, add paid services or alter unrelated jobs. Keep hourly cadence and scheduler delivery to the Backport manager conversation.
- Supported scheduler edits to this hourly job's payload/timeout may be made if needed and authorized by the tool. Read current state first, preserve unrelated fields, then read back. Runtime restrictions remain binding: if cross-job mutation is denied, record the proposed scheduler change as blocked; never use shell/direct database access, privilege changes or another session to bypass it. Local instruction-file improvements are a separate authorized effect, not a way to bypass a denied scheduler operation.
- Never rewrite or advance the hourly audit checkpoint or amend old log entries. Record discovered classification errors/missed candidates as bounded correction requests for the hourly audit, with source evidence; do not mutate ledger records from this reviewer.
- Preserve current file contents before editing; use expected-text edits and verify the resulting diff. Do not interrupt an active audit or change instructions mid-run; defer the edit if safe application cannot be established. Preserve an exact before/after diff in the review log for rollback.
- Test proposed reasoning changes against the reviewed sample and at least one contrasting case. Record whether the change fixes the observed issue without weakening other requirements. Prompt replay is static review, not proof of future model behavior. On later days assess whether earlier improvements helped; revert only your own ineffective changes with evidence, preserving unrelated edits. No forced daily changes.

## Finish
Append a concise review entry with UTC time, reviewed interval and sample, measured outcomes, concrete findings, applied changes and verification, deferred/blocked items, and next evaluation criteria. Complete the review within this session or name the concrete blocker. Provide a concise final report in this review session; the scheduler owns delivery to the Backport manager conversation (<BACKPORT_MANAGER_SESSION>). Do not send a manual duplicate notification. No recursive review jobs or helper sessions.
