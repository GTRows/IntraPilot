# IntraPilot development integration

AI Base is development tooling only. It is not part of the plugin runtime,
provider catalog, model gateway, native payloads, or distribution resources.
The product security contract in `AGENTS.md` and `SECURITY.md` stays authoritative.

Read `docs/INTERNAL_ONLY_DESIGN.md`, `docs/IMPLEMENTATION_PLAN.md`, and
`docs/STATUS.md` before work. The existing plan owns implementation order and
the status document owns durable progress; do not create a competing roadmap.
Use a lightweight inspect, implement, verify, update-state workflow with one
writer and read-only review. Work and commit on `development`.

`STARTUP_BLOCKED` and `RELEASE_BLOCKED` are product acceptance boundaries.
AI Base discovery can list inherited build/test commands; these are candidates,
not permission to execute them. The current approved project check is
`python scripts/verify-bootstrap.py`; plugin builds/startup remain blocked.
Keep actual static, test, runtime, and review evidence separate.

Only the Codex adapter is installed. Do not install a Claude adapter, change
global model/provider settings, approve native hook trust automatically, or
add network services as part of this development integration. AI Base lifecycle
callbacks keep task routing locally and do not contact model providers.

Use `intrapilot-handoff` before manual compaction, with the hook's exact native
binding when supplied. Update `docs/STATUS.md` first, then the small local
`.ai/task-state.json` / `.ai/memory/HANDOFF.md` routing pair. Without a supplied
binding, a manual checkpoint is unbound and cannot claim precompact approval.
Automatic compaction remains nonblocking. Compare current files/revision before
resuming; do not infer success from old handoff text.

Use `.ai/commands/ai-base.ps1 doctor`, `diff`, `sync`, or `explain` to maintain
the integration. AI Base manages only its marked AGENTS section and recorded
runtime/hook fragments. Preserve all other instructions and configuration.
Change managed outputs through source/profile changes and reviewed sync, never
by forging manifest hashes or editing generated callbacks in place.

Machine profiles, ownership manifests, hooks, runtime copies, backups, reports,
and checkpoints are ignored. Durable rules, maintenance commands, this skill,
and documentation are tracked. A fresh checkout needs an explicit reviewed
integration using the local shared AI Base source; it does not inherit this
machine's paths or native trust. No confidential project data belongs in the
public repository or development prompts.
