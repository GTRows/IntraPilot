# IntraPilot

![IntraPilot](src/main/resources/META-INF/pluginIcon.svg)

An independent JetBrains assistant fork targeting approved organization-hosted
model servers. Based on [ProxyAI](https://github.com/carlrobertoh/ProxyAI).

**Development foundation only. The inherited runtime is not yet converted and
must not be installed or launched on confidential projects.**

## Required product behavior

- Connect only to explicitly approved internal model servers, including Qwen.
- Free distribution; no paid-plugin licensing calls.
- Optional token-authenticated read-only internal Bitbucket connection; no Bitbucket Cloud.
- Separate inline edit/completion/next-edit switches, initially disabled.
- Independent controls for all user features; mandatory security rules remain enforced.
- Local recorded token totals, input/output summaries, daily Usage charts, and model/feature breakdown with explicit missing-data coverage.
- No public cloud/free-model providers or fallback.
- No model inference, model weights, or model server running on the workstation.
- No telemetry, analytics, remote crash reports, account sync, or plugin-owned
  update requests.
- Retain project file reading/search, approved edits/diff previews, IDE
  diagnostics, chat, agents, and task tracking.
- Exclude web search/fetch, Context7, remote MCP, external agents, arbitrary shell
  execution, and project run/debug execution from the first release.
- Invalid policy, server, or model configuration stops the action.

These are acceptance requirements, not claims about the inherited code.
Deployment network restrictions and verification of the internal model gateway
are required independently of the plugin.

## Project documents

- [Design](docs/INTERNAL_ONLY_DESIGN.md)
- [Implementation plan](docs/IMPLEMENTATION_PLAN.md)
- [Current status](docs/STATUS.md)
- [Security and release acceptance](SECURITY.md)
- [Contributor instructions](AGENTS.md)
- [AI Base development tooling](docs/DEVELOPMENT.md)
- [Empty example deployment policy](config/internal-model-policy.example.json)

## Verify the foundation

Run `python scripts/verify-bootstrap.py` and `git diff --check`.
This verifies project metadata, icons, documentation, and the initial blocker;
it does not build or launch the inherited plugin or prove network confinement.

`STARTUP_BLOCKED` initially stops all Gradle execution. After source conversion
and review, validation builds may proceed while `RELEASE_BLOCKED` still prevents
signing/publication. No bypass flag is provided. Fork GitHub Actions is disabled.

## Distribution target

JetBrains Marketplace publication and a reviewed offline ZIP, after complete
security conversion, runtime observation, package review, and Plugin Verifier.
Host-IDE Marketplace installation/update traffic is separate from plugin runtime
traffic and must be controlled separately in restricted deployments.

## License and origin

Apache-2.0. ProxyAI Copyright 2023 Carl-Robert Linnupuu.
See [LICENSE](LICENSE), [NOTICE](NOTICE), and notices in inherited source.
This is an independent fork, not an upstream-endorsed ProxyAI release.
