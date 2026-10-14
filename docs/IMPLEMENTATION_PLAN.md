# IntraPilot Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans for implementation with one writer and read-only review. Steps use checkbox syntax for tracking.

**Goal:** Deliver a reviewed JetBrains plugin that uses only approved organization-hosted models, with no public-network runtime paths or workstation inference.

**Architecture:** Retain useful ProxyAI IDE tools and replace its provider/network/execution surfaces. One internal client enforces administrator-approved destinations and model IDs; independent deployment egress controls complete the boundary.

**Tech Stack:** Existing Java/Kotlin, JetBrains Platform, and Gradle; minimize retained runtime dependencies.

**Spec:** `docs/INTERNAL_ONLY_DESIGN.md`

## Global constraints

- Product: IntraPilot; plugin ID: `io.github.gtrows.intrapilot`.
- Work on `development`; no confidential deployment information in public source.
- No public providers, free-model catalogs, telemetry, cloud fallback, account sync, updater requests, external agents, remote MCP, arbitrary process execution, or workstation inference.
- Unconfigured or invalid policy denies requests. Never migrate upstream settings into trusted policy.
- Preserve original licenses and relevant notices. Mark changes to inherited files.
- The project foundation is not a secure product release. Keep publication blocked until complete acceptance.
- Distribution is free. Source/context must never leave the organization; only approved internal model requests and optional read-only internal Bitbucket requests are permitted.
- Bitbucket Cloud is excluded. The user confirmed internal Data Center/Server hosting; exact version/endpoint/auth are verified locally. Credentials stay in PasswordSafe, never prompts/config/logs.
- Inline edit, completion, and next edit have independent persistent controls, initially off. Disabled features may not collect context, request, schedule, or apply results.

## Review focus

1. Deleted/renamed/missing model selection must stop every feature and subagent.
2. DNS/proxy/redirect resolution must not widen exact approved destinations.
3. Old settings and feature-specific clients must not restore a cloud route.
4. Symlinks/junctions, source instructions, and shell/run tools must not bypass tool boundaries.
5. Delayed startup/update/background behavior and libraries must not send telemetry or project content.

## Task 1: Source and artifact boundary

**Files:** `build.gradle.kts`, `settings.gradle.kts`, `gradle/libs.versions.toml`, `.gitmodules`, `src/main/resources/META-INF/plugin.xml`, `src/main/kotlin/ee/carlrobert/codegpt/CodeGPTProjectActivity.kt`, `CodeGPTUpdateActivity.kt`, and discovered dependency/registration callers.

**Produces:** a reviewed source/dependency inventory in `docs/security/NETWORK_INVENTORY.md`; removal of public-network and local-inference registrations/dependencies; validation-only build access while publication remains blocked.

- [ ] Inventory all HTTP, socket, DNS, browser, subprocess, telemetry, updater, download, and remote-resource call sites, including transitives and native code.
- [ ] Trace each retained IDE tool's dependencies before removing any runtime source.
- [ ] Remove telemetry and analytics completely; remove llama.cpp/native serving/provisioning and public account/provider/client flows from the distribution.
- [ ] Remove web/Context7/remote MCP/external-agent tools and unrestricted process/run/debug execution from tool registration.
- [ ] Replace inherited startup/cloud synchronization and update scheduling with internal-only startup.
- [ ] Add source/artifact checks that reject forbidden modules, SDKs, provider catalogs, endpoints, and external-process registrations.
- [ ] Request read-only source-boundary review. After it passes, remove only `STARTUP_BLOCKED` to permit synthetic tests and sandbox validation. Keep `RELEASE_BLOCKED` until Task 5 acceptance.

## Task 2: Approved internal connection and model routing

**Files:** create `src/main/kotlin/ee/carlrobert/codegpt/security/InternalNetworkPolicy.kt`; modify `agent/clients/HttpClientProvider.kt`, `agent/clients/CustomOpenAILLMClient.kt`, `settings/models/LLMClientFactory.kt`, `ModelCatalog.kt`, `ModelProvider.kt`, `ModelSettings.kt`, `settings/service/ServiceType.java`, and affected settings/UI callers.

**Consumes:** reviewed dependency inventory. **Produces:** one approved internal-provider path and feature/subagent routing with no fallback.

- [ ] Resolve the deployment policy location/ownership mechanism with the deployment administrator; no ordinary user/project config may widen it. Verify gateway protocol using synthetic requests.
- [ ] Define `InternalNetworkPolicy.validateRequest(uri: java.net.URI, modelId: String)` and controlled DNS/proxy handling; deny empty policy, unsupported scheme/path, public/unapproved address, redirects, and proxy escape.
- [ ] Test exact origins/paths/model IDs, IPv4/IPv6 representations, DNS changes, userinfo, redirects, proxy configuration, missing policy, and policy-file replacement.
- [ ] Replace provider selection/catalog with administrator-approved internal models only; reuse no upstream defaults.
- [ ] Test `ModelSettings` across fresh install, missing/deleted/renamed models, old settings, feature routing, subagent routing, and network failure. Every invalid case must stop rather than choose another provider/model.
- [ ] Verify mock chat-completions streaming, tool calls, authentication, cancellation, retries, and server error handling. Log no request bodies, prompt text, source content, or credentials.
- [ ] Inventory every literal/dynamic destination in source, generated code, libraries/native payloads, and final distribution. Test policy against redirects, proxy/DNS changes, response-supplied paging links, and background requests.

## Task 3: Retained tools and approval boundary

**Files:** `agent/BuiltInToolRegistry.kt`, `agent/ToolSpecs.kt`, `agent/AgentFactory.kt`, `agent/tools/ReadTool.kt`, `IntelliJSearchTool.kt`, `EditTool.kt`, `WriteTool.kt`, `DiagnosticsTool.kt`, `ConfirmingTools.kt`, `settings/hooks/HookManager.kt`, and discovered callers/tests.

**Consumes:** internal model client/policy. **Produces:** project-scoped read/search/diagnostic/edit tools and task tracking.

- [ ] Preserve native IDE navigation/search and reviewed diff approval flows; reconcile prompts/tool schemas with the reduced tool catalog.
- [ ] Enforce project-root confinement after path and symlink/junction resolution, including non-existing write targets.
- [ ] Test outside-project reads/writes, traversal, junctions, model-generated unsafe paths, denied edits, cancellation, hook failure, and approval exceptions.
- [ ] Verify no arbitrary command, external agent, run/debug process, remote MCP, URL fetch, or model download tool is registered or reachable.
- [ ] Verify agent/subagent iterations with the internal client's synthetic tool-capable server.

## Task 3a: Independent inline-feature controls

**Files:** `settings/configuration/ConfigurationSettings.kt`, `settings/configuration/ConfigurationComponent.java`, `settings/configuration/CodeCompletionConfigurationForm.kt`, `inlineedit/`, `codecompletions/`, `nextedit/`, and their actual registered provider/listener callers (resolve callers before editing).

**Consumes:** approved internal feature/model routing. **Produces:** persistent independent inline-edit, completion, and next-edit switches, all defaulting off.

- [ ] Trace each feature's invocation, context collection, scheduling, request, cancellation, and result application before edits.
- [ ] Add independent switches and capability validation; no unsupported model fallback.
- [ ] Test fresh install, restart, toggling one feature independently, disabling during in-flight work, and configuration/capability changes. Assert no network/context collection or delayed application while disabled.

## Task 3b: Optional internal Bitbucket connection

**Files:** create a scoped Bitbucket service/settings module and synthetic integration tests under `src/main/kotlin/ee/carlrobert/codegpt/` and `src/test/kotlin/ee/carlrobert/codegpt/`; extend the internal destination policy and context selection UI.

**Consumes:** approved destination/path/method enforcement. **Produces:** token-authenticated read-only internal Bitbucket repositories/branches/commits/PRs/diffs.

- [ ] Verify the user-confirmed internal Data Center/Server deployment's exact endpoint and API/auth version locally; Bitbucket Cloud cannot satisfy this contract.
- [ ] Store/remove the service-scoped token using PasswordSafe. Reject unapproved/public service URLs before attaching credentials or sending requests.
- [ ] Implement read-only API operations and explicit context selection. Include no git push, merge, PR/comment write, webhook, external browser login, public API, or MCP dependency.
- [ ] Test expired/revoked/missing tokens, redaction, service switching, malicious paging URLs, redirects, outside-policy origins/paths/methods, and public-host denial using synthetic fixtures.
- [ ] Assert auth secrets never appear in model messages, plain config, logs, exports, or redirected requests.

## Task 4: Branding, settings, and package checks

**Files:** `src/main/resources/META-INF/plugin*.xml`, `src/main/resources/messages/codegpt*.properties`, `src/main/java/ee/carlrobert/codegpt/CodeGPTPlugin.java`, provider/model settings panels, `DESCRIPTION.md`, `README.md`, `NOTICE`, and remaining branding references.

**Produces:** IntraPilot UI with only internal connection/model choices and an unsigned validation ZIP.

- [ ] Complete visible UI identity; retain upstream provenance and notices without implying upstream endorsement.
- [ ] Isolate global action/configurable/notification IDs and persistent state names/files from upstream. Test coexistence with ProxyAI and prove old cloud settings cannot be imported as internal policy.
- [ ] Remove forbidden settings/actions and account/credits/free-model screens; no first-run connection until approved policy is present.
- [ ] Build an unsigned validation ZIP. Inspect its registration, classpath, libraries, native payloads, and endpoints against the inventory.
- [ ] Run relevant unit/integration tests and JetBrains Plugin Verifier against the chosen supported IDE range. Compatibility changes require actual verifier evidence.

## Task 5: Runtime acceptance and publication

**Files:** create `docs/security/RUNTIME_ACCEPTANCE.md`, `docs/PRIVACY.md`, `docs/RELEASE.md`; update `docs/STATUS.md`, `.github/workflows/build.yml`, and deployment packaging as needed.

**Produces:** evidence-backed release candidate and Marketplace submission assets.

- [ ] Obtain administrator-managed policy/egress deployment details locally, without placing them in the public repository.
- [ ] Verify the internal gateway serves only approved internal models and native tools, with no external forwarding.
- [ ] Observe actual IntelliJ DNS/network/process activity across startup, idle, chat, edit, tools, cancellation, errors, migration, and delayed background behavior using synthetic data. Test blocked public destinations independently.
- [ ] Exercise real IntelliJ Bitbucket reads/paging, token rotation/removal, and service switching against an approved internal test service with synthetic content/test credentials. Observe request origins and confirm auth headers never reach the model or another origin. Exercise inline toggles during active requests in the same runtime observation.
- [ ] Review the built artifact, transitive licenses, test evidence, compatible IDE range, privacy text, and release listing.
- [ ] Choose free Marketplace distribution; include no paid licensing callbacks. Complete inline-control and internal Bitbucket acceptance before claiming those features work.
- [ ] Remove `RELEASE_BLOCKED` only after completed runtime acceptance and review; enable only the reviewed CI workflow.
- [ ] Configure signing and publishing credentials outside the repository; prepare the final reviewed ZIP and Marketplace submission. First upload is manual and Marketplace approval is external.

## Current verification

Only bootstrap verification is available. No task above is marked complete.
This plan does not authorize uploading company context or inventing actual
deployment endpoint values. Marketplace publishing follows a concrete reviewed
release artifact; the inherited fork must never be presented as that artifact.
