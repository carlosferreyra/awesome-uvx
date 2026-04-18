import { readFileSync } from "fs";

const github = {
  owner: process.env.GITHUB_REPOSITORY_OWNER ?? "",
  repo: process.env.GITHUB_REPOSITORY?.split("/")[1] ?? "",
  token: process.env.GITHUB_TOKEN ?? "",
  issueNumber: Number(process.env.PR_NUMBER ?? "0"),
  action: process.env.ACTION as "comment_failure" | "approve",
};

const headers = {
  Authorization: `Bearer ${github.token}`,
  Accept: "application/vnd.github+json",
  "Content-Type": "application/json",
  "X-GitHub-Api-Version": "2022-11-28",
};

const base = `https://api.github.com/repos/${github.owner}/${github.repo}`;

async function commentFailure() {
  type Failure = { package: string; reason: string };
  let failures: Failure[] = [];
  try {
    failures = JSON.parse(readFileSync("output.log", "utf8"));
  } catch {
    failures = [{ package: "unknown", reason: "execution_error" }];
  }

  const reasonMessages: Record<string, string> = {
    network: [
      "> ⚠️ This may be a transient PyPI outage.",
      "> Please re-run the workflow before amending your PR.",
    ].join("\n"),
    not_found: [
      "> ❌ The package name does not exist on PyPI.",
      "> Please double-check the package name and try again.",
    ].join("\n"),
    wrong_binary: [
      "> ❌ The package installed but the declared binary was not found.",
      "> Please verify the `execs` field matches the actual binary name.",
    ].join("\n"),
    execution_error: [
      "> ❌ The tool ran but exited with an error.",
      "> Please verify the package works with `uvx --from <package> <binary> --help`.",
    ].join("\n"),
  };

  const lines = failures
    .map((f) => {
      const hint = reasonMessages[f.reason] ?? reasonMessages.execution_error;
      return `### \`${f.package}\` — ${f.reason.replace("_", " ")}\n${hint}`;
    })
    .join("\n\n");

  const body = [
    "## ❌ Tool validation failed",
    "",
    "The following tool(s) proposed in this PR could not be validated:",
    "",
    lines,
    "",
    "---",
    "_Please amend your PR and push again. The workflow will re-run automatically._",
  ].join("\n");

  const res = await fetch(`${base}/issues/${github.issueNumber}/comments`, {
    method: "POST",
    headers,
    body: JSON.stringify({ body }),
  });

  if (!res.ok) throw new Error(`GitHub API error: ${res.status} ${await res.text()}`);
}

async function approve() {
  const res = await fetch(`${base}/pulls/${github.issueNumber}/reviews`, {
    method: "POST",
    headers,
    body: JSON.stringify({
      event: "APPROVE",
      body: "✅ All proposed tools validated successfully via `uvx`. Ready for merge.",
    }),
  });

  if (!res.ok) throw new Error(`GitHub API error: ${res.status} ${await res.text()}`);
}

if (github.action === "comment_failure") {
  await commentFailure();
} else if (github.action === "approve") {
  await approve();
} else {
  throw new Error(`Unknown ACTION: ${github.action}`);
}
