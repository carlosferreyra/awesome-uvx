# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""
Test that tools in the list are installable and executable via uvx.

Usage:
    uv run scripts/test-clients.py --tools '<json>'

The --tools argument accepts a JSON array of tool objects matching the
tools.json schema. Each object must have at minimum:
    {"package": "<name>", "execs": ["<binary>", ...]}

Examples:
    # Test a single tool (e.g. from a PR diff):
    uv run scripts/test-clients.py --tools '[{"package":"ruff","execs":["ruff"]}]'

    # Test all tools from tools.json (e.g. monthly run):
    uv run scripts/test-clients.py --tools "$(python -c "
    import json
    with open('tools.json') as f:
        cats = json.load(f)['categories']
    tools = [{'package': k, 'execs': v['execs']} for c in cats for k, v in c['tools'].items()]
    print(json.dumps(tools))
    ")"
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


def main():
    parser = ArgumentParser(description="Test uvx tool installations.")
    parser.add_argument(
        "--tools",
        required=True,
        help='JSON array of {"package": str, "execs": [str, ...]} objects',
    )
    parser.add_argument(
        "--output",
        default="output.log",
        help="Path to write failure log (default: output.log)",
    )
    args = parser.parse_args()

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
            print(f"    ✓ ok")
            results.append({"package": package, "success": True})
        else:
            print(f"    ✗ failed ({failure_type})")
            results.append({"package": package, "success": False, "reason": failure_type})

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
