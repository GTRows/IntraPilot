import argparse
import json
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def main():
    parser = argparse.ArgumentParser(description="Maintain IntraPilot development tooling.")
    parser.add_argument("command", choices=("doctor", "diff", "sync", "explain"))
    parser.add_argument("--source", help="Local shared AI Base source directory")
    parser.add_argument("--rule")
    args = parser.parse_args()
    source = args.source or os.environ.get("AI_BASE_SOURCE")
    if not source:
        integration_path = ROOT / ".ai/integration.json"
        if not integration_path.is_file():
            parser.error("No local integration metadata; supply --source or AI_BASE_SOURCE after reviewed initialization.")
        source = json.loads(integration_path.read_text(encoding="utf-8"))["base_source"]
    source_path = Path(source).resolve()
    if not (source_path / "scripts/ai_base/cli.py").is_file():
        parser.error("AI Base source directory is unavailable.")
    if args.rule and args.command != "explain":
        parser.error("--rule is supported only by explain")
    sys.path.insert(0, str(source_path / "scripts"))
    from ai_base.cli import main as run
    arguments = [args.command, str(ROOT)]
    if args.rule:
        arguments.extend(["--rule", args.rule])
    return run(arguments)


if __name__ == "__main__":
    raise SystemExit(main())
