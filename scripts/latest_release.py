# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx"]
# ///
"""Fetch latest release info from PyPI for each tool and update tools.json."""

import json
import logging
from pathlib import Path
from typing import Any

import httpx  # type: ignore[ty:unresolved-import]

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)

TOOLS_JSON = Path(__file__).parent.parent / "tools.json"
PYPI_URL = "https://pypi.org/pypi/{package}/json"


def pypi_package_name(name: str) -> str:
    # strip extras like "fastapi[standard]" -> "fastapi"
    return name.split("[")[0]


def fetch_latest(package: str) -> tuple[str, str | None] | None:
    url = PYPI_URL.format(package=pypi_package_name(package))
    try:
        r = httpx.get(url, timeout=10, follow_redirects=True)
        r.raise_for_status()
        info: dict[str, Any] = r.json()
        version: str = info["info"]["version"]
        # upload_time of the latest version's first file
        releases = info["releases"].get(version, [])
        upload_time = releases[0]["upload_time"] if releases else None
        date = upload_time[:10] if upload_time else None
        return (version, date)
    except Exception as e:
        log.warning("Failed to fetch %s: %s", package, e)
        return None


def main() -> None:
    data = json.loads(TOOLS_JSON.read_text())

    for category in data["categories"]:
        for name, tool in category["tools"].items():
            if tool.get("pypi") is False:
                log.info("Skipping %s (pypi=false)", name)
                continue

            result = fetch_latest(name)
            if result is None:
                continue

            version, date = result
            tool["version"] = version
            tool["last_release"] = date
            log.info("%-30s %s  %s", name, version, date)

    TOOLS_JSON.write_text(json.dumps(data, indent=2) + "\n")
    log.info("tools.json updated.")


if __name__ == "__main__":
    main()
