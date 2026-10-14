# IntraPilot internal-only design

Date: 2026-10-14
Status: project foundation; runtime conversion not implemented
Upstream baseline: `carlrobertoh/ProxyAI@1c7a8569fe5e34bb64cbc10fa32e6918e8358d98`

## Intent

Create a JetBrains plugin based on ProxyAI that preserves useful IDE tools and
connects only to an organization's own approved model servers, including Qwen.
The user explicitly requires a new name/logo, eventual JetBrains Marketplace
publication, no cloud/free-provider catalog, no workstation inference, no
telemetry, and no internet data output.
The user also requires free distribution, independent inline-feature toggles,
and token-authenticated Bitbucket integration. The user confirmed organization-
hosted Bitbucket Data Center/Server on 2026-10-14. Exact version, endpoint,
authentication permissions, and actual connectivity remain deployment checks.

Product identity: IntraPilot. Plugin ID: `io.github.gtrows.intrapilot`.
Source: `https://github.com/GTRows/IntraPilot`.
Project location: `D:\Workspace\Self\OpenSource\IntraPilot`.
The user confirmed the name and location. Retaining Java/Kotlin and the
JetBrains plugin structure is an implementation choice inherited from upstream.
The original vector logo uses enclosed code brackets and an internal node.

## Network and model boundary

- The workstation runs the IDE and plugin only; inference runs on an approved
  organization-hosted server. Do not embed or launch llama.cpp, Ollama, local
  model weights, or an external model-serving process.
- Begin with the OpenAI-compatible chat-completions API and native function
  calling. Actual server API/tool support must be verified with synthetic data.
- All features and subagents use approved internal model IDs. There is no
  public-model discovery, provider account, subscription, or free-model picker.
- Empty policy denies all requests. Deployment-specific policy is installed
  locally, outside tracked/public project content, and maintained by deployment
  administrators. The example file is a proposed schema, not a working control.
- Approved destinations are exact scheme/host/port and permitted API paths,
  not a blanket private-address range. User/provider configuration cannot widen
  the policy. Old ProxyAI settings are not imported as trusted policy.
- DNS, resolved addresses, redirects, proxy routing, and secondary connections
  must stay within the approved boundary. Deny redirects and uncontrolled proxy
  discovery; support internal names only with a controlled internal resolver.
- Missing endpoint, missing/deleted model, policy mismatch, request failure,
  migration, or unavailable server stops the action. Never choose a default
  public provider or silently switch destination/model.
- The organization verifies that the gateway serves its internal models and
  does not forward traffic to a public inference service.
- The only additional network service is optional, separately approved internal
  Bitbucket. No Bitbucket Cloud, public REST API, public Git remote, or generic
  URL/network tool is introduced. Token auth does not waive destination policy.
- No code/context leaves the organization. Requests to the approved internal
  model server necessarily transmit selected context from the workstation.
- Enforce outbound denial on the deployment independently of plugin code.
  A plugin in a shared IDE process cannot guarantee all host traffic is local.

## Feature scope

Keep chat, agent iteration, project-scoped file reading/search, diff previews,
approved edits/writes, IDE diagnostics, and task tracking. Models receive only
the context selected for those actions. No background screen/file upload,
automatic screenshot watching, remote sync, or prompt/body logging.

Exclude internet search/fetch, Context7 access, remote MCP, external agents/ACP,
arbitrary shell commands, and run/debug execution of project programs from the
first release. Process execution can bypass an HTTP-client policy. A future
request to restore it needs a separate independently enforced sandbox design.
This exclusion is an implementation choice required to enforce the user's
network restriction; it is not a claim that the user explicitly rejected shell.

Edits require a diff and explicit approval. A failed/cancelled approval or
security hook denies the operation. Reads/searches/edits stay inside approved
project roots, including symlink/junction resolution. Treat source-file
instructions and model tool arguments as untrusted input.

## Inline controls and internal Bitbucket

Provide separate persistent switches for inline edit, inline completion, and
next edit. Start all three disabled. Disabling a switch cancels/suppresses its
requests, context collection, scheduling, and pending result application without
disabling chat/agent. Completion/next edit require a compatible approved
internal model; otherwise show the unavailable capability and keep them off.

Bitbucket scope begins with read-only repositories, branches, commits, PRs and
diffs. Token storage uses IntelliJ PasswordSafe; neither the token nor auth
headers are given to the model or persisted in project/config/log/export data.
Attach selected Bitbucket context to the internal model only through the same
reviewed context-selection rules as local files. No write/merge/push/comments
or external code hosting are implied by connecting an account.

The approved deployment supplies the Bitbucket service and token locally.
Version/auth compatibility is verified with synthetic fixtures before any real
connection. Policy validates every request and pagination/redirect destination.
The user confirmed internal hosting; verify its exact deployment locally. Never enable a public
fallback or ask for production credentials in the public development project.

## Source conversion

Replace the provider catalog/routing rather than hiding cloud options in UI.
Remove the telemetry module/SDK from dependencies, registration, and packaging.
Remove native inference submodules and provisioning, updater activity, cloud
identity/credit flows, external-agent runners, remote tools, and every default
cloud fallback. Refactor only where necessary to separate retained IDE tools
from forbidden features. Maintain upstream history, LICENSE, and notices.
Isolate global extension/action/configurable/notification IDs and persistent
state names/storage files from ProxyAI. Verify coexistence and prevent inherited
settings from becoming trusted internal configuration.

Current evidence pointers:

- `settings/models/ModelSettings.kt`: unresolved selections use defaults.
- `settings/models/ModelCatalog.kt`: defaults point to the ProxyAI provider.
- `agent/clients/ProxyAILLMClient.kt`: public ProxyAI endpoint.
- `proxyai-telemetry/`: analytics module and RudderStack dependency.
- `agent/tools/WebSearchTool.kt`, `WebFetchTool.kt`, `GetLibraryDocsTool.kt`,
  `ResolveLibraryIdTool.kt`: public-network tools.
- `CodeGPTProjectActivity.kt`: automatic cloud account synchronization.
- `CodeGPTUpdateActivity.kt`: scheduled update-check path.
- `agent/BuiltInToolRegistry.kt`: shell approval exceptions approve execution.
- `agent/external/`, `mcp/`, `services/llama/`: additional execution/network paths.

These pointers are an initial inventory, not a complete audit.

## Distribution and acceptance

Fork foundation is publishable source, not an installable secure plugin.
Gradle execution is initially blocked by `STARTUP_BLOCKED`. Source-boundary
review permits clearing that marker for synthetic tests and an unsigned
validation ZIP; `RELEASE_BLOCKED` keeps signing/publication blocked until the
complete runtime acceptance in `SECURITY.md`. This separates validation access
from release approval without bypassing either boundary.
Marketplace publication requires a reviewed package, compatible IDE range,
Plugin Verifier results, license/attribution checks, listing assets, privacy
statement, and signing configuration. Tokens/certificates stay outside source.
The first release is uploaded only after the package is concrete and reviewed.
Marketplace approval is external and cannot be promised.
Choose free distribution. No paid-plugin purchase, subscription, or license-
verification network flow belongs in the product.

Runtime no-egress does not mean an IDE can download/update a Marketplace plugin
without network access. Restricted deployments use an offline reviewed ZIP and
separate IDE/network restrictions. Public development/build infrastructure is
distinct from the plugin's internal-only runtime.

No corporate deployment endpoint/model identifier/token/source is available in
this public project. Use synthetic fixtures, then verify actual server tool
calling and real network confinement on the approved deployment environment.
Do not claim deployment approval based on technical feasibility alone.
