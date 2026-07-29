# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Comment on or approve a pull request after tool validation."""

import json
import os
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

OWNER = os.environ.get("GITHUB_REPOSITORY_OWNER", "")
REPOSITORY = os.environ.get("GITHUB_REPOSITORY", "").partition("/")[2]
TOKEN = os.environ.get("GITHUB_TOKEN", "")
PR_NUMBER = int(os.environ.get("PR_NUMBER", "0"))
ACTION = os.environ.get("ACTION", "")

BASE_URL = f"https://api.github.com/repos/{OWNER}/{REPOSITORY}"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "Content-Type": "application/json",
    "X-GitHub-Api-Version": "2022-11-28",
}


def post(path: str, payload: dict) -> None:
    request = Request(
        f"{BASE_URL}{path}",
        data=json.dumps(payload).encode(),
        headers=HEADERS,
        method="POST",
    )
    try:
        with urlopen(request):
            pass
    except HTTPError as error:
        response = error.read().decode()
        raise RuntimeError(f"GitHub API error: {error.code} {response}") from error


def comment_failure() -> None:
    try:
        failures = json.loads(Path("output.log").read_text())
    except (OSError, json.JSONDecodeError):
        failures = [{"package": "unknown", "reason": "execution_error"}]

    reason_messages = {
        "network": (
            "> ⚠️ This may be a transient PyPI outage.\n"
            "> Please re-run the workflow before amending your PR."
        ),
        "not_found": (
            "> ❌ The package name does not exist on PyPI.\n"
            "> Please double-check the package name and try again."
        ),
        "wrong_binary": (
            "> ❌ The package installed but the declared binary was not found.\n"
            "> Please verify the `execs` field matches the actual binary name."
        ),
        "execution_error": (
            "> ❌ The tool ran but exited with an error.\n"
            "> Please verify the package works with "
            "`uvx --from <package> <binary> --help`."
        ),
    }

    lines = []
    for failure in failures:
        reason = failure["reason"]
        hint = reason_messages.get(reason, reason_messages["execution_error"])
        lines.append(f"### `{failure['package']}` — {reason.replace('_', ' ')}\n{hint}")

    body = "\n".join(
        [
            "## ❌ Tool validation failed",
            "",
            "The following tool(s) proposed in this PR could not be validated:",
            "",
            "\n\n".join(lines),
            "",
            "---",
            (
                "_Please amend your PR and push again. "
                "The workflow will re-run automatically._"
            ),
        ]
    )
    post(f"/issues/{PR_NUMBER}/comments", {"body": body})


def approve() -> None:
    post(
        f"/pulls/{PR_NUMBER}/reviews",
        {
            "event": "APPROVE",
            "body": "✅ All proposed tools validated successfully via `uvx`. "
            "Ready for merge.",
        },
    )


if ACTION == "comment_failure":
    comment_failure()
elif ACTION == "approve":
    approve()
else:
    raise ValueError(f"Unknown ACTION: {ACTION}")
