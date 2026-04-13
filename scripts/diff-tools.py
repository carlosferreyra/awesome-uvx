# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""
Extract newly added tools from a git diff of tools.json.

Compares the current branch against a base ref (default: origin/main) and
outputs a JSON array of added tool objects suitable for passing to test-clients.py.

Usage:
    uv run scripts/diff-tools.py                    # diff against origin/main
    uv run scripts/diff-tools.py --base origin/main # explicit base ref

Output (stdout):
    [{"package": "ruff", "execs": ["ruff"]}, ...]

Exit codes:
    0  added tools found, JSON written to stdout
    1  error
    2  no added tools detected (e.g. only removals or metadata changes)
"""

import json
import subprocess
import sys
from argparse import ArgumentParser


def run(command: str) -> tuple[bool, str, str]:
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    return result.returncode == 0, result.stdout.strip(), result.stderr.strip()


def get_json_at_ref(ref: str, path: str) -> dict | None:
    ok, out, err = run(f"git show {ref}:{path}")
    if not ok:
        return None
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        return None


def extract_tools(data: dict) -> dict[str, dict]:
    """Flatten categories into {package_name: tool_data} mapping."""
    tools = {}
    for category in data.get("categories", []):
        for pkg_name, pkg_data in category.get("tools", {}).items():
            tools[pkg_name] = pkg_data
    return tools


def main():
    parser = ArgumentParser(description="Extract newly added tools from git diff.")
    parser.add_argument(
        "--base",
        default="origin/main",
        help="Base ref to diff against (default: origin/main)",
    )
    parser.add_argument(
        "--path",
        default="tools.json",
        help="Path to tools.json relative to repo root (default: tools.json)",
    )
    args = parser.parse_args()

    # Load base version of tools.json
    base_data = get_json_at_ref(args.base, args.path)
    if base_data is None:
        print(f"Error: could not read {args.path} at {args.base}", file=sys.stderr)
        sys.exit(1)

    # Load current (HEAD) version
    try:
        with open(args.path) as f:
            head_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: could not read {args.path}: {e}", file=sys.stderr)
        sys.exit(1)

    base_tools = extract_tools(base_data)
    head_tools = extract_tools(head_data)

    # Only newly added keys — not modified, not removed
    added = {
        pkg: data
        for pkg, data in head_tools.items()
        if pkg not in base_tools
    }

    if not added:
        print("No new tools detected.", file=sys.stderr)
        sys.exit(2)

    output = [
        {"package": pkg, "execs": data.get("execs", [])}
        for pkg, data in added.items()
    ]

    print(json.dumps(output))


if __name__ == "__main__":
    main()
