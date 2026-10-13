// Modified for IntraPilot; see NOTICE.
if (file("config/security/STARTUP_BLOCKED").exists()) {
    throw GradleException(
        "IntraPilot inherited runtime is blocked. Complete source-boundary review before validation; see SECURITY.md."
    )
}

gradle.taskGraph.whenReady {
    if (file("config/security/RELEASE_BLOCKED").exists() &&
        allTasks.any { it.name == "publishPlugin" || it.name == "signPlugin" }
    ) {
        throw GradleException(
            "IntraPilot signing and publication are blocked until runtime acceptance; see SECURITY.md."
        )
    }
}

rootProject.name = "IntraPilot"
include(":proxyai-treesitter")
include(":proxyai-telemetry")
