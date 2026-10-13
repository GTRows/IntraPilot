# Security contract

IntraPilot is an internal-model-only JetBrains assistant under development.
The inherited ProxyAI runtime still contains public-network paths. It is not
approved for installation or use with confidential projects.

## Required product boundary

Only administrator-approved organization-hosted model endpoints may receive
model requests. All other network destinations must be denied. No inference
engine runs on the workstation. No telemetry, analytics, cloud provider,
remote crash reporting, external agent, account service, or fallback is shipped.

A private IP address alone does not prove an approved or internal service.
The deployment supplies exact approved destinations and model IDs, plus an
outbound network policy. The model gateway must independently be confirmed to
serve approved internal models without forwarding requests to public services.

The plugin cannot sandbox the complete IDE process or arbitrary subprocesses.
The first release excludes arbitrary shell execution, external agents, remote
MCP, web fetching/search, automatic model downloads, and plugin-owned update
requests. IDE run/debug tools that execute project code stay excluded unless an
independent process/network isolation boundary is introduced and verified.

Marketplace installation/update traffic belongs to the host IDE. Public source
hosting, build dependencies, and Marketplace upload belong to the development
and distribution environment; they are not permitted product runtime egress.
Offline deployments install an independently reviewed ZIP with host-IDE
outbound traffic restricted separately.

## Release blocker

`config/security/STARTUP_BLOCKED` causes Gradle settings evaluation to fail
before project tasks, dependency setup, packaging, signing, sandbox startup,
or publishing. There is no skip flag. After source/dependency conversion and
read-only source-boundary review, clear only `STARTUP_BLOCKED` to allow synthetic
tests, sandbox validation, and an unsigned validation ZIP. `RELEASE_BLOCKED`
continues blocking signing and publishing until complete runtime acceptance.
This allows acceptance evidence to be collected without permitting publication.
GitHub Actions is disabled for this fork.

Remove `RELEASE_BLOCKED` only after all of the following have evidence and review:

1. All runtime network call sites and transitive libraries are inventoried.
2. Public providers, telemetry, updater, downloads, and external tooling are
   removed from registration, source shipping, and the built distribution.
3. One approved internal-model client enforces destination/model policy with
   no redirects, external DNS/proxy path, or provider fallback.
4. Fresh installs, old settings, endpoint changes, missing/deleted models,
   network failures, and agent/subagent routing all fail closed.
5. Local tools enforce project boundaries and do not execute arbitrary code.
6. Tests use synthetic repositories and synthetic model traffic only.
7. A real IntelliJ sandbox is observed during startup, idle, chat, edit, agent
   tools, retries, configuration migration, and delayed activity. No plugin
   connection targets an unapproved destination, including DNS and subprocesses.
8. A representative deployment enforces outbound denial independently of the
   plugin and verifies the internal gateway does not forward requests externally.
9. The reviewed package passes license review and JetBrains Plugin Verifier.

Passing `scripts/verify-bootstrap.py` proves only the repository foundation.
It does not prove any item in the runtime release checklist.
