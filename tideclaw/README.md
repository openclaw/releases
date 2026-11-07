# Tideclaw operational instructions

Reviewed, sanitized snapshot of the reusable instructions from the Tideclaw OpenClaw instance, captured November 7, 2026. This is documentation, not a runnable backup, installer, scheduler export, or source of release authorization. Nothing here activates an automation or changes a live instance.

## Contents

| Location | Contents |
| --- | --- |
| `automations/index.json` | Reference inventory: recurring schedules, execution modes, timeouts, tool lists, and prompt paths |
| `automations/hourly-main-hotfix-audit.md` | Current replacement hourly job prompt |
| `automations/hotfix-audit/AUTOMATION.md` | Complete audit procedure, including triage-first eligibility and full-range completion |
| `automations/daily-hotfix-quality-review.md` | Current replacement daily review prompt |
| `automations/hotfix-audit/DAILY-REVIEW.md` | Detailed review procedure |
| `automations/daily-release-skills-automation-review.md` | Daily local-skill and general-automation hygiene prompt |
| `automations/hourly-ubuntu-kernel-status.md` | Sanitized advisory-monitoring prompt |
| `automations/hourly-ubuntu-kernel-status.trigger.mjs` | Existing deterministic advisory-change trigger; requires scheduler-provided globals |
| `skills/hotfix-ledger/SKILL.md` | Instance-local hotfix-ledger API skill |
| `workspace/` | Workspace AGENTS, SOUL, and IDENTITY instruction snapshots |

The hourly instructions exclude new features and feature-only repairs before expensive review, explicitly exclude the OpenClaw ID feature squash, and require every commit in the pinned range to be accounted for. Only an actual hard limit or concrete external blocker permits unresolved work.

## Reuse and authority

1. Review the instructions against the current OpenClaw documentation and your own repository policy. Workspace files are source snapshots, not universal product documentation; IDENTITY.md is an unfilled template. The current runtime/tool contract takes precedence over historical command examples in workspace instructions.
2. Provision the supported skills and explicitly authorize each task. References to prior user authorization are not transferable grants. The exported tool lists describe the source configuration and do not grant tool access.
3. Replace `<AUDIT_WORKSPACE>`, `<HOURLY_HOTFIX_AUDIT_JOB>`, `<DAILY_HOTFIX_REVIEW_JOB>`, and `<BACKPORT_MANAGER_SESSION>` with operator-selected local bindings. Paths beginning `.openclaw/hotfix-audit/` are relative to the audit workspace. Deploy the two files from `automations/hotfix-audit/` there before scheduling either hotfix job.
4. Bind a local owner, workspace, credentials, session, and delivery destination through supported tools. The inventory deliberately omits those bindings and is not accepted as a scheduler import. Existing-session jobs need an explicitly selected session. Keep jobs inactive until reviewed.
5. Preserve the real audit checkpoint and append-only log when migrating an existing audit. This repository includes neither; never infer a reviewed checkpoint from this snapshot. A new deployment needs an explicitly chosen baseline, not a silent reset.
6. The kernel monitor is a point-in-time example for the named CVE, not a current security assessment. Its trigger expects `web_fetch`, `trigger`, and `json` globals supplied by the scheduler; it is not a standalone Node.js program. Recheck advisory format and the initial comparison baseline before activation. Host names and installed kernel versions have been removed.

The hygiene prompt references a historical skill-consolidation PR and the source job uses a persistent review session. Those are context, not proof that work is complete or that the same session exists elsewhere. Job UUID references in prompts were replaced with logical bindings, including references to the superseded hotfix jobs.

## Shared skills stay upstream

Tideclaw discovers OpenClaw repository and bundled skills as well as the instance-local skill above. Release workflows remain canonical in [openclaw/openclaw `.agents/skills`](https://github.com/openclaw/openclaw/tree/main/.agents/skills), notably `release-openclaw-maintainer`, `release-openclaw-ci`, `release-openclaw-mac`, `release-openclaw-plugin-testing`, and `verify-release`. They are not duplicated here.

The separately installed `autoreview` skill comes from [openclaw/agent-skills](https://github.com/openclaw/agent-skills), observed at commit `1444c91f6b455227993bc780d0933f78ae54f5b4`, under `skills/autoreview`. It remains an external dependency rather than another local copy.

## Snapshot boundary

Included: four custom recurring automation prompts, their two audit instruction files, the existing advisory trigger, one local skill, and three workspace instruction files. Only host paths, private routing/job identifiers, personal attribution, and host-specific security baseline details were normalized or removed. Operational policy is otherwise retained; this snapshot does not silently rewrite the live instance.

Excluded: one-shot release/PR continuations; disabled historical jobs; the built-in memory-maintenance automation; USER.md, MEMORY.md, daily notes, dreams, transcripts and raw logs; scheduler scratch/history/checkpoints/locks; provider/system prompts and responses; live configuration; credentials and skill-manager metadata; build artifacts and installed dependencies. The built-in maintenance job and shared skills are not custom Tideclaw procedures.

Future refreshes should read the current automation inventory and source files, preserve this boundary, inspect the outgoing diff, and verify references and privacy before opening a PR. Do not bulk-copy the instance directory.
