# Project status

Date: 2026-10-14
Branch: development

## Foundation

- GitHub fork: https://github.com/GTRows/IntraPilot
- Upstream baseline: 1c7a8569fe5e34bb64cbc10fa32e6918e8358d98
- New identity: IntraPilot / io.github.gtrows.intrapilot.
- Original SVG icons for light/dark IDE themes.
- Internal-only design, security contract, empty example deployment policy.
- Separate Gradle startup/publication blockers and disabled fork Actions.
- AI Base 0.2.2 development integration: Codex only, lightweight project-owned
  workflow, local lifecycle callbacks, and `intrapilot-handoff`. See
  `docs/DEVELOPMENT.md`; this is not plugin runtime functionality.

## Not yet delivered

- Added requirements: free distribution, complete destination/source/package
  inspection, independent inline-feature switches, and optional token-based
  read-only internal Bitbucket. Internal Data Center/Server hosting was confirmed
  by the user on 2026-10-14; exact deployment/version/auth remains unverified. These are
  accepted design requirements, not implemented runtime features.
- Requirements review added actual IntelliJ Bitbucket/token/service-switching
  observation and inline-toggle runtime scenarios to release acceptance.

- Cloud providers, telemetry, external tools, local inference, and network
  fallbacks still exist in inherited source. They have not been removed.
- The internal-only client, approved model catalog, and confinement tests
  are not implemented.
- No built ZIP, real IntelliJ runtime verification, internal-server test,
  corporate installation approval, or Marketplace publication exists.

## Next work

Execute `docs/IMPLEMENTATION_PLAN.md` in dependency order. Keep `STARTUP_BLOCKED`
until source-boundary conversion/review permits validation; keep `RELEASE_BLOCKED`
until the complete runtime acceptance and release evidence are reviewed.
Do not use inherited runtime settings as trusted deployment policy.

## Foundation verification

- `python scripts/verify-bootstrap.py`: identity, metadata, ten SVG variants,
  empty policy, notices, branch, and bootstrap gate checks passed.
- `git diff --check`: passed.
- SVG preview rendered and visually inspected for light/dark themes.
- Cached Gradle 8.2 `help --offline --no-daemon --console=plain` refused at
  `settings.gradle.kts` line 3 with the expected startup-blocker message before
  project task execution. This proves initial refusal, not a build or the full
  Gradle 8.13/IntelliJ compatibility of the project.
- Fork Actions permissions were queried and `enabled` was `false`.
- Read-only design review identified and corrected the circular validation/
  publication gate. Foundation review also corrected intrinsic UI icon sizes,
  clarified the two-gate procedure, and added identity/state isolation plus
  coexistence checks to the implementation plan.
- AI Base doctor/diff/repeat-init/sync passed without conflicts or managed
  changes. Original contributor instructions and 816 source/blocker files were
  preserved. Four offline callback checks passed; native Codex trust/execution
  remains unverified and was not changed. Development tooling is outside the
  plugin runtime and does not establish product network confinement.
- Read-only review of the AI Base integration found no actionable defects and
  independently checked ownership, preservation, ignore rules, and doctor/diff.
