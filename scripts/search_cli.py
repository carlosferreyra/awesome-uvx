# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx"]
# ///
"""Search PyPI for uvx-runnable CLI packages not yet listed in tools.json.

The script iterates over a cartesian product of short lowercase strings and
queries the PyPI JSON API for each candidate. When a package is found, it
heuristically tests whether it exposes a CLI via `uvx` (either directly or
through `uvx --from <pkg> <binary>`) and appends matching commands to
`.env.found` (gitignored).

Designed to be run locally over long sessions — interrupt with Ctrl+C at any
time and pick up again later (re-runs will re-check from the start, but
duplicate matches are avoided via the existing `.env.found` contents).
"""

from __future__ import annotations

import itertools
import json
import random
import re
import string
import subprocess
import sys
import time
from pathlib import Path

import httpx

# --- configuration ---

MAX_SIZE: int = 10
MIN_SIZE: int = 2
ALPHABET: str = string.ascii_lowercase + "-"
PYPI_URL: str = "https://pypi.org/pypi/{package}/json"
OUTPUT_FILE: str = "clis.txt"
CURSOR_FILE: str = ".search_cursor"
CURSOR_FLUSH_EVERY: int = 25
SLEEP_MIN: float = 0.1
SLEEP_MAX: float = 0.3
HTTP_TIMEOUT: float = 10.0
UVX_TIMEOUT: int = 1

# Classifiers that strongly suggest a console-oriented package.
CLI_CLASSIFIERS: frozenset[str] = frozenset(
    {
        "Environment :: Console",
        "Environment :: Console :: Curses",
        "Topic :: Utilities",
        "Topic :: Terminals",
        "Topic :: System :: Shells",
    }
)
CLI_KEYWORDS: tuple[str, ...] = (
    "command-line",
    "command line",
    " cli ",
    "cli.",
    "terminal",
)

# Regexes used to tease apart uvx stderr when the default binary is missing.
AVAILABLE_BINS_RE = re.compile(
    r"(?:Available executables?|executable names?)[^:]*:\s*([^\n]+)",
    re.IGNORECASE,
)
NO_EXECUTABLE_RE = re.compile(
    r"(no executable|executable .* not found|no such file|command not found)",
    re.IGNORECASE,
)


# --- helpers ---


def load_existing_packages() -> set[str]:
    """Flatten tools.json into a set of lowercase package names to skip."""
    tools_path = Path(__file__).parent.parent / "tools.json"
    with open(tools_path) as f:
        data = json.load(f)
    packages: set[str] = set()
    for category in data.get("categories", []):
        for pkg in category.get("tools", {}):
            packages.add(pkg.lower())
    return packages


def load_already_found(output_path: Path) -> set[str]:
    """Read previously-found commands so we can deduplicate across runs."""
    if not output_path.exists():
        return set()
    with open(output_path) as f:
        return {line.strip() for line in f if line.strip()}


def is_valid_pypi_name(candidate: str) -> bool:
    """Cheap filter to avoid obviously-invalid PyPI names."""
    if candidate[0] in "-" or candidate[-1] in "-":
        return False
    if "--" in candidate:
        return False
    return True


def is_likely_cli(info: dict) -> bool:
    """Heuristic: does the PyPI metadata smell like a CLI tool?"""
    classifiers = info.get("classifiers") or []
    if any(c in CLI_CLASSIFIERS for c in classifiers):
        return True
    text = " ".join(
        (info.get("summary") or "", (info.get("description") or "")[:500])
    ).lower()
    return any(k in text for k in CLI_KEYWORDS)


def run_cmd(command: list[str]) -> tuple[int, str, str]:
    """Run a command capturing output with a hard timeout."""
    try:
        result = subprocess.run(
            command,
            text=True,
            capture_output=True,
            timeout=UVX_TIMEOUT,
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "timeout"
    except FileNotFoundError as e:
        return -1, "", str(e)


def parse_available_bins(output: str) -> list[str]:
    """Parse uvx's 'Available executables' hint when default binary missing."""
    m = AVAILABLE_BINS_RE.search(output)
    if not m:
        return []
    raw = m.group(1)
    parts = re.split(r"[,\s]+", raw)
    return [p.strip("`'\"[]") for p in parts if p.strip("`'\"[],. ")]


def try_uvx(package: str) -> str | None:
    """Return a working `uvx ...` command string, or None if nothing works."""
    # Method 1: assume the default binary matches the package name.
    code, out, err = run_cmd(["uvx", package, "--help"])
    match code:
        case 0:
            return f"uvx {package}"
        case -1:
            return None

    # Method 2: if uvx complained about a missing binary, try the suggestions.
    combined = out + "\n" + err
    if NO_EXECUTABLE_RE.search(combined):
        for bin_name in parse_available_bins(combined):
            if not bin_name or bin_name == package:
                continue
            code2, _, _ = run_cmd(["uvx", "--from", package, bin_name, "--help"])
            match code2:
                case 0:
                    return f"uvx --from {package} {bin_name}"
                case _:
                    continue
    return None


def load_cursor(cursor_path: Path) -> str | None:
    """Read the last queried candidate so we can resume past it."""
    if not cursor_path.exists():
        return None
    text = cursor_path.read_text().strip()
    return text or None


def save_cursor(cursor_path: Path, candidate: str) -> None:
    cursor_path.write_text(candidate + "\n")


def iter_candidates(existing: set[str], resume_after: str | None):
    """Yield candidate names, skipping anything up to and including resume_after."""
    skipping = resume_after is not None
    for length in range(MIN_SIZE, MAX_SIZE + 1):
        for combo in itertools.product(ALPHABET, repeat=length):
            candidate = "".join(combo)
            if skipping:
                if candidate == resume_after:
                    skipping = False
                continue
            if not is_valid_pypi_name(candidate):
                continue
            if candidate.lower() in existing:
                continue
            yield candidate


# SIGINT keeps Python's default behavior (raises KeyboardInterrupt), so it
# unwinds out of `subprocess.run` immediately. The main loop catches it and
# still prints the final stats / flushes the cursor.


# --- main loop ---


def main() -> int:
    repo_root = Path(__file__).parent.parent
    output_path = repo_root / OUTPUT_FILE
    cursor_path = repo_root / CURSOR_FILE

    existing = load_existing_packages()
    already_found = load_already_found(output_path)
    resume_after = load_cursor(cursor_path)
    print(f"Skipping {len(existing)} known packages from tools.json")
    print(f"Resuming with {len(already_found)} previously-found entries")
    print(f"Alphabet: {ALPHABET!r} | length range: {MIN_SIZE}..{MAX_SIZE}")
    if resume_after:
        print(f"Resuming after cursor: {resume_after!r}")
    print(f"Writing matches to {output_path}\n")

    queried = 0
    matches = 0
    last_candidate: str | None = resume_after
    interrupted = False

    try:
        with httpx.Client(
            timeout=HTTP_TIMEOUT,
            follow_redirects=True,
            headers={"User-Agent": "awesome-uvx-search/1.0"},
        ) as client:
            for candidate in iter_candidates(existing, resume_after):
                last_candidate = candidate
                time.sleep(random.uniform(SLEEP_MIN, SLEEP_MAX))
                url = PYPI_URL.format(package=candidate)
                try:
                    response = client.get(url)
                except httpx.HTTPError as e:
                    print(f"  [warn] {candidate}: {e}")
                    continue

                queried += 1
                if queried % CURSOR_FLUSH_EVERY == 0:
                    save_cursor(cursor_path, candidate)

                match response.status_code:
                    case 200:
                        try:
                            info = response.json().get("info", {}) or {}
                        except ValueError:
                            continue
                        if not is_likely_cli(info):
                            print(f"  [skip] {candidate}: metadata not CLI-like")
                            continue
                        print(f"  [probe] {candidate}: testing via uvx...")
                        cmd = try_uvx(candidate)
                        match cmd:
                            case None:
                                print("    x  no runnable binary found")
                            case _ if cmd in already_found:
                                print(f"    =  already recorded: {cmd}")
                            case _:
                                print(f"    +  match: {cmd}")
                                with open(output_path, "a") as f:
                                    f.write(cmd + "\n")
                                already_found.add(cmd)
                                matches += 1
                    case 404:
                        # Unknown package name — the common case, stay quiet.
                        pass
                    case 429:
                        print("  [rate-limit] backing off 10s...")
                        time.sleep(10.0)
                    case code:
                        print(f"  [http {code}] {candidate}")
    except KeyboardInterrupt:
        interrupted = True

    if last_candidate is not None:
        save_cursor(cursor_path, last_candidate)

    reason = "interrupted" if interrupted else "completed"
    print(
        f"\nRun {reason}. matches={matches} queries={queried} "
        f"last_candidate={last_candidate!r}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
