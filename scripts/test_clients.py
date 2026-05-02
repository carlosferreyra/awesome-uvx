# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""
Test that tools in the list are installable and executable via uvx.

Usage:
    uv run scripts/test_clients.py --all
    uv run scripts/test_clients.py --diff origin/main
    uv run scripts/test_clients.py --tools '<json>'

Modes (mutually exclusive):
    --all              Test every tool in tools.json.
    --diff <ref>       Test only tools added vs. <ref> (uses diff_tools.py).
    --tools '<json>'   Explicit JSON array of {"package", "execs"} objects.

Exit codes:
    0  all tested tools passed (or nothing to test in --diff mode)
    1  one or more tools failed, or invalid input
"""

import json
import re
import subprocess
import sys
from argparse import ArgumentParser
from pathlib import Path

# --- failure classification patterns ---

NETWORK_PATTERNS = re.compile(
    r"(failed to fetch|connection error|could not connect|network|timeout|timed out|"
    r"ssl error|certificate|http 5\d\d|503|502|504)",
    re.IGNORECASE,
)
NOT_FOUND_PATTERNS = re.compile(
    r"(no solution found|not found|package .* doesn't exist|"
    r"404|packagenotfound|no matching distribution)",
    re.IGNORECASE,
)
BINARY_PATTERNS = re.compile(
    r"(executable .* not found|no such file|command not found|"
    r"which: no|not in.*path)",
    re.IGNORECASE,
)


def classify_failure(stdout: str, stderr: str) -> str:
    combined = stdout + stderr
    if NETWORK_PATTERNS.search(combined):
        return "network"
    if NOT_FOUND_PATTERNS.search(combined):
        return "not_found"
    if BINARY_PATTERNS.search(combined):
        return "wrong_binary"
    return "execution_error"


def run(command: str) -> tuple[bool, str, str]:
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    return result.returncode == 0, result.stdout.strip(), result.stderr.strip()


def test_tool(package: str, exec_name: str) -> tuple[bool, str]:
    """
    Try two methods. Returns (success, failure_type).
    failure_type is one of: network, not_found, wrong_binary, execution_error
    On success, failure_type is empty string.
    """
    # Method 1: uv tool install
    ok, out, err = run(f"uv tool install --force {package}")
    if ok:
        return True, ""

    # Retry once on network errors before giving up
    if NETWORK_PATTERNS.search(out + err):
        ok, out, err = run(f"uv tool install --force {package}")
        if ok:
            return True, ""
        return False, "network"

    # Method 2: uvx --from
    ok2, out2, err2 = run(f"uvx --from {package} {exec_name} --help")
    if ok2:
        return True, ""

    # Classify based on combined output of both attempts
    return False, classify_failure(out + out2, err + err2)


def load_all_tools(tools_path: Path) -> list[dict]:
    with open(tools_path) as f:
        cats = json.load(f)["categories"]
    return [
        {"package": pkg, "execs": data["execs"]}
        for cat in cats
        for pkg, data in cat["tools"].items()
    ]


def load_diff_tools(base_ref: str) -> list[dict]:
    """Delegate to diff_tools.py to extract added tools vs. base_ref."""
    script = Path(__file__).parent / "diff_tools.py"
    result = subprocess.run(
        ["uv", "run", str(script), "--base", base_ref],
        capture_output=True,
        text=True,
    )
    if result.returncode == 2:
        return []
    if result.returncode != 0:
        print(f"diff_tools.py failed: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    return json.loads(result.stdout)


def main():
    parser = ArgumentParser(description="Test uvx tool installations.")
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument("--all", action="store_true", help="Test every tool in tools.json")
    src.add_argument("--diff", metavar="REF", help="Test only tools added vs. REF")
    src.add_argument("--tools", help='JSON array of {"package", "execs"} objects')
    parser.add_argument(
        "--output",
        default="output.log",
        help="Path to write failure log (default: output.log)",
    )
    parser.add_argument(
        "--tools-path",
        default="tools.json",
        help="Path to tools.json (default: tools.json)",
    )
    args = parser.parse_args()

    if args.all:
        tools = load_all_tools(Path(args.tools_path))
    elif args.diff:
        tools = load_diff_tools(args.diff)
        if not tools:
            print("No new tools to test.")
            return
    else:
        try:
            tools = json.loads(args.tools)
        except json.JSONDecodeError as e:
            print(f"Error: --tools is not valid JSON: {e}", file=sys.stderr)
            sys.exit(1)

    # Ensure uv is available
    ok, version, _ = run("uv --version")
    if not ok:
        print("uv not found. Installing...")
        run("curl -LsSf https://astral.sh/uv/install.sh | sh")
    else:
        print(f"uv {version}")

    print(f"Testing {len(tools)} tool(s)...\n")

    results: list[dict] = []

    for tool in tools:
        package = tool["package"]
        exec_name = tool["execs"][0] if tool.get("execs") else package.split("[")[0]
        print(f"  Testing: {package} ({exec_name})")

        success, failure_type = test_tool(package, exec_name)

        if success:
            print("    ✓ ok")
            results.append({"package": package, "success": True})
        else:
            print(f"    ✗ failed ({failure_type})")
            results.append(
                {"package": package, "success": False, "reason": failure_type}
            )

    # Summary
    passed = [r for r in results if r["success"]]
    failed = [r for r in results if not r["success"]]

    print(f"\nResults: {len(passed)} passed, {len(failed)} failed")

    if failed:
        log_path = Path(args.output)
        with open(log_path, "w") as f:
            json.dump(failed, f, indent=2)
        print(f"Failures written to {log_path}")
        sys.exit(1)


if __name__ == "__main__":
    main()
