# AI Base development tooling

IntraPilot uses AI Base 0.2.2 in project-owned workflow mode with the Codex
adapter and lightweight workflow. The existing design, implementation plan,
status, and product security contract remain authoritative. No Claude adapter
or additional model service is installed.

AI Base adds local lifecycle callbacks and compact handoff routing. It is
development tooling and is not bundled into the JetBrains plugin.

## Maintenance

From the project root:

```powershell
.\.ai\commands\ai-base.ps1 doctor
.\.ai\commands\ai-base.ps1 diff
.\.ai\commands\ai-base.ps1 sync
.\.ai\commands\ai-base.ps1 explain --rule single-writer
python scripts/verify-bootstrap.py
```

The helper locates the shared source from local `.ai/integration.json`.
`--source C:\Tools\ai-base` or `AI_BASE_SOURCE` explicitly overrides that
location. Keep source/profile changes and inspect `diff` before `sync`.
The current profile lists no allowed plugin build command while startup is
blocked. Discovery suggestions are not execution authorization.

Use the `intrapilot-handoff` skill at meaningful task boundaries or before
manual compaction. It updates the durable status and a local routing pair;
the implementation plan remains the only roadmap.

## Ownership and fresh checkouts

The original contributor instructions are preserved outside a marked AI Base
section in `AGENTS.md`. Only that section and recorded callback/runtime files
are managed. Runtime/profile/manifest files and checkpoints are machine-local
and ignored; rules, commands, skill, and this guide are tracked.

A fresh checkout needs a reviewed integration from a local AI Base source.
Inspect the source README and discovery report first. Preserve the existing
AGENTS content and project handoff skill; resolve their ownership explicitly
before initialization. Select only `codex`, `lightweight`, workflow owner
`project`, handoff skill `intrapilot-handoff`, and these handoff sources:
`.ai/rules/workspace.md`, `docs/STATUS.md`, `docs/IMPLEMENTATION_PLAN.md`.
Back up existing instructions before merging only the generated managed section.
Do not fabricate ownership hashes or overwrite existing user configuration.

## Verification boundary

Doctor/diff and idempotent synchronization verify local configuration ownership.
Native Codex callback execution still requires the host's own trust review and
live event evidence. AI Base does not auto-approve trust or change global model
settings. No LSP/agent runtime acceptance is inferred from configuration checks.
Product build/startup and Marketplace publication remain separately blocked.

Integration checks on 2026-10-13: doctor and diff reported no conflicts/changes;
repeat initialization and sync preserved managed contents and timestamps;
original contributor instructions and 816 plugin/source/blocker files remained
byte-identical. Synthetic callback checks verified nonblocking automatic
compaction, rejection of missing manual checkpoints, routing of unapproved
restores to project documents, and the Windows launcher. These are offline
callback checks, not native Codex event acceptance.
