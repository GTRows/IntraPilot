import json
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ID = "io.github.gtrows.intrapilot"
LOGOS = [
    "META-INF/pluginIcon.svg",
    "META-INF/pluginIcon_dark.svg",
    "icons/codegpt.svg",
    "icons/codegpt_dark.svg",
    "icons/codegpt-small.svg",
    "icons/codegpt-small_dark.svg",
    "icons/codegpt-model.svg",
    "icons/codegpt-model_dark.svg",
    "icons/proxyRounded.svg",
    "icons/proxyRounded_dark.svg",
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    properties = dict(
        line.split("=", 1)
        for raw_line in (ROOT / "gradle.properties").read_text().splitlines()
        if (line := raw_line.strip()) and not line.startswith("#") and "=" in line
    )
    properties = {key.strip(): value.strip() for key, value in properties.items()}
    require(properties["pluginName"] == "IntraPilot", "Incorrect product name")
    require(properties["pluginGroup"] == "io.github.gtrows", "Incorrect plugin group")
    require(
        properties["pluginRepositoryUrl"] == "https://github.com/GTRows/IntraPilot",
        "Incorrect fork URL",
    )
    require(properties["org.gradle.configuration-cache"] == "false", "Release gate requires configuration cache off")

    descriptor = ET.parse(ROOT / "src/main/resources/META-INF/plugin.xml").getroot()
    require(descriptor.findtext("id") == PLUGIN_ID, "Incorrect plugin ID")
    require(descriptor.findtext("name") == "IntraPilot", "Incorrect descriptor name")
    require(descriptor.findtext("vendor") == "GTRows", "Incorrect vendor")
    require(descriptor.find("extensions/toolWindow").attrib["id"] == "IntraPilot", "Incorrect tool window ID")
    plugin_class = (ROOT / "src/main/java/ee/carlrobert/codegpt/CodeGPTPlugin.java").read_text()
    require(f'PluginId.getId("{PLUGIN_ID}")' in plugin_class, "Runtime plugin ID mismatch")

    settings = (ROOT / "settings.gradle.kts").read_text()
    require('rootProject.name = "IntraPilot"' in settings, "Incorrect Gradle project name")
    for marker in ("STARTUP_BLOCKED", "RELEASE_BLOCKED"):
        require((ROOT / "config/security" / marker).is_file(), f"Missing {marker}")
        require(f'file("config/security/{marker}")' in settings, f"Missing {marker} gate")
    require(settings.index("STARTUP_BLOCKED") < settings.index("rootProject.name"), "Startup blocker is too late")
    require('throw GradleException(' in settings, "Missing startup refusal")
    require('it.name == "publishPlugin"' in settings and 'it.name == "signPlugin"' in settings, "Missing publication gate")

    policy = json.loads((ROOT / "config/internal-model-policy.example.json").read_text())
    require(policy["approvedDestinations"] == [] and policy["approvedModelIds"] == [], "Example must contain no deployment values")
    require(policy["approvedBitbucketDestinations"] == [], "Example must contain no internal Bitbucket address")
    require(all(value is False for key, value in policy.items() if key.startswith("allow")), "Example allows a forbidden surface")
    expected_features = {
        "chatEnabled", "agentEnabled", "inlineEditEnabled", "inlineCompletionEnabled",
        "fileContextEnabled", "projectSearchEnabled", "diagnosticsEnabled",
        "editActionsEnabled", "writeActionsEnabled", "taskTrackingEnabled",
        "nextEditEnabled", "autoApplyEnabled", "commitMessageEnabled", "nameSuggestionsEnabled",
        "skillsEnabled", "subagentsEnabled", "bitbucketEnabled", "projectRulesEnabled",
        "taskMemoryEnabled", "reviewModeEnabled", "connectionCheckEnabled", "usageTrackingEnabled",
    }
    require(set(policy["features"]) == expected_features, "Missing independent feature controls")
    require(all(value is False for value in policy["features"].values()), "Example features must start disabled")

    resources = ROOT / "src/main/resources"
    for logo in LOGOS:
        svg = ET.parse(resources / logo).getroot()
        require(svg.tag == "{http://www.w3.org/2000/svg}svg", f"Invalid SVG: {logo}")
        expected_size = "13" if "small" in logo or "model" in logo else "128" if "proxyRounded" in logo else "20" if logo.startswith("icons/") else "40"
        require(svg.attrib.get("width") == expected_size and svg.attrib.get("height") == expected_size, f"Incorrect icon size: {logo}")
        for element in svg.iter():
            require(not element.tag.endswith("script"), f"Script in SVG: {logo}")
            require(not any(key.endswith("href") for key in element.attrib), f"External resource in SVG: {logo}")

    require("Apache License" in (ROOT / "LICENSE").read_text(), "Original license missing")
    require("Carl-Robert Linnupuu" in (ROOT / "NOTICE").read_text(), "Upstream attribution missing")
    for document in ("AGENTS.md", "SECURITY.md", "docs/INTERNAL_ONLY_DESIGN.md", "docs/IMPLEMENTATION_PLAN.md", "docs/STATUS.md"):
        require((ROOT / document).is_file(), f"Missing document: {document}")
    require("must not be installed or launched" in (ROOT / "README.md").read_text(), "Missing development warning")
    branch = subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, text=True).strip()
    require(branch == "development", "Foundation work must be on development")
    subprocess.run(["git", "-c", "core.autocrlf=false", "diff", "--check"], cwd=ROOT, check=True)
    print("PASS: identity, metadata, 10 SVG variants, empty policy, notices, branch, and bootstrap gates.")
    print("Runtime conversion, packaging, network confinement, and Marketplace publication remain pending.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError, ET.ParseError, subprocess.CalledProcessError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
