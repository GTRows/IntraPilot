---
name: intrapilot-handoff
description: Save or resume IntraPilot development state at task boundaries, on handoff requests, or before compaction while preserving the project plan and security blockers.
---

# IntraPilot handoff

Read `AGENTS.md`, `.ai/rules/workspace.md`, `docs/STATUS.md`, and
`docs/IMPLEMENTATION_PLAN.md`, then inspect the current branch, files, and
existing `.ai/task-state.json` / `.ai/memory/HANDOFF.md` if present.

For saving, update the durable status document with actual progress and
verification. Keep the existing plan as the sole implementation sequence.
Save a compact routing checkpoint in both local AI Base artifacts with the
active goal, accepted decisions, constraints, completed work, changed files,
actual evidence, remaining uncertainty, and next executable step. Link the
project documents instead of copying a second roadmap. Keep startup/publication
blockers explicit and never mark runtime conversion or network confinement
complete without the evidence required by `SECURITY.md`.

Use `references/handoff-template.md`. Verification entries include `layer`,
`result`, `command`, `verified_at` in UTC, and a reviewed revision/file digests
where available. Keep static, tests, integration, host-runtime, and review
evidence separate. Preserve old evidence and mark stale/incomplete claims
unverified. Never include credentials or confidential deployment context.

When a hook provides `handoff_context`, copy its exact adapter, session_id,
and cycle_id into the task-state and handoff artifacts. Save both after the
request with current UTC verification time. Do not invent or reuse a binding.
An unbound manual handoff is allowed but is not precompact approval.
Automatic compaction must continue without a missing checkpoint becoming a gate.

For resuming, compare the checkpoint's revision/file identity with current
files and tools. Continue the recorded next step only after its preconditions
are satisfied. Handoff is local development state, never plugin runtime state.
