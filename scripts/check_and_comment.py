# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx"]
# ///
"""Comment on or approve a pull request after tool validation."""

import json
import os
from pathlib import Path

import httpx  # type: ignore[ty:unresolved-import]

REASON_MESSAGES = {
    "network": "\n".join(
        [
            "> ⚠️ This may be a transient PyPI outage.",
            "> Please re-run the workflow before amending your PR.",
        ]
    ),
    "not_found": "\n".join(
        [
            "> ❌ The package name does not exist on PyPI.",
            "> Please double-check the package name and try again.",
        ]
    ),
    "wrong_binary": "\n".join(
        [
            "> ❌ The package installed but the declared binary was not found.",
            "> Please verify the `execs` field matches the actual binary name.",
        ]
    ),
    "execution_error": "\n".join(
        [
            "> ❌ The tool ran but exited with an error.",
            "> Please verify the package works with `uvx --from <package> <binary> --help`.",
        ]
    ),
}


def github_config() -> tuple[str, int, dict[str, str]]:
    owner = os.environ.get("GITHUB_REPOSITORY_OWNER", "")
    repo = os.environ.get("GITHUB_REPOSITORY", "").partition("/")[2]
    token = os.environ.get("GITHUB_TOKEN", "")
    issue_number = int(os.environ.get("PR_NUMBER", "0"))
    base_url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    return base_url, issue_number, headers


def failure_comment(log_path: Path = Path("output.log")) -> str:
    try:
        failures = json.loads(log_path.read_text())
    except Exception:
        failures = [{"package": "unknown", "reason": "execution_error"}]

    lines = []
    for failure in failures:
        reason = failure["reason"]
        hint = REASON_MESSAGES.get(reason, REASON_MESSAGES["execution_error"])
        lines.append(
            f"### `{failure['package']}` — {reason.replace('_', ' ', 1)}\n{hint}"
        )

    return "\n".join(
        [
            "## ❌ Tool validation failed",
            "",
            "The following tool(s) proposed in this PR could not be validated:",
            "",
            "\n\n".join(lines),
            "",
            "---",
            "_Please amend your PR and push again. The workflow will re-run automatically._",
        ]
    )


def post_to_github(url: str, headers: dict[str, str], body: dict[str, str]) -> None:
    response = httpx.post(url, headers=headers, json=body)
    if not response.is_success:
        raise RuntimeError(f"GitHub API error: {response.status_code} {response.text}")


def comment_failure(base_url: str, issue_number: int, headers: dict[str, str]) -> None:
    post_to_github(
        f"{base_url}/issues/{issue_number}/comments",
        headers,
        {"body": failure_comment()},
    )


def approve(base_url: str, issue_number: int, headers: dict[str, str]) -> None:
    post_to_github(
        f"{base_url}/pulls/{issue_number}/reviews",
        headers,
        {
            "event": "APPROVE",
            "body": "✅ All proposed tools validated successfully via `uvx`. Ready for merge.",
        },
    )


def main() -> None:
    base_url, issue_number, headers = github_config()
    action = os.environ.get("ACTION", "")

    if action == "comment_failure":
        comment_failure(base_url, issue_number, headers)
    elif action == "approve":
        approve(base_url, issue_number, headers)
    else:
        raise ValueError(f"Unknown ACTION: {action}")


if __name__ == "__main__":
    main()
