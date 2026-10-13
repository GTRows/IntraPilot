# Project status

Date: 2026-10-13
Branch: development

## Foundation

- GitHub fork: https://github.com/GTRows/IntraPilot
- Upstream baseline: 1c7a8569fe5e34bb64cbc10fa32e6918e8358d98
- New identity: IntraPilot / io.github.gtrows.intrapilot.
- Original SVG icons for light/dark IDE themes.
- Internal-only design, security contract, empty example deployment policy.
- Separate Gradle startup/publication blockers and disabled fork Actions.

## Not yet delivered

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
