# IntraPilot contributor instructions

- Read `docs/INTERNAL_ONLY_DESIGN.md`, `docs/IMPLEMENTATION_PLAN.md`, and `docs/STATUS.md` before edits.
- This is a public fork. Never add employer names, internal hostnames, IP addresses, tokens, source code, logs, prompts, or conversations from a real deployment.
- Use English for code, comments, and repository documents. Use no emojis.
- Work and commit on `development`. Keep the upstream remote for provenance; never push to upstream.
- Preserve the Apache-2.0 license and applicable third-party notices. Record changes to inherited files.
- The product connects to explicitly approved organization-hosted model servers. It never runs inference on the workstation.
- No public model providers, free-model catalogs, telemetry, analytics, remote crash reporting, account sync, plugin-owned update requests, external agents, remote MCP, model downloads, or internet tools.
- Missing or invalid policy/model configuration must stop the request. Never fall back to another provider or endpoint.
- Do not launch the inherited plugin. `config/security/STARTUP_BLOCKED` blocks Gradle execution until source-boundary review permits synthetic validation. `RELEASE_BLOCKED` separately blocks signing/publication until runtime acceptance.
- Never remove or bypass either blocker merely to make a build pass. `STARTUP_BLOCKED` requires source-boundary review; `RELEASE_BLOCKED` requires the complete runtime evidence listed in `SECURITY.md`.
- Preserve one writer. Read-only reviewers may inspect the design and changes.
- Run `python scripts/verify-bootstrap.py` to verify the project foundation. This is not runtime or network-safety verification.
- Claim no-egress only with built-artifact review and observed runtime evidence. The host IDE, model gateway, and network policy have separate boundaries.
