# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Script for validating tools.json following PEP 723 format."""

import json
import logging
from pathlib import Path


def load_tools(tools_path: Path) -> list:
    with open(tools_path) as f:
        return json.load(f)["categories"]


def check_tools():
    logging.basicConfig(
        filename="checks.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    tools_path = Path(__file__).parent.parent / "tools.json"

    try:
        categories = load_tools(tools_path)
        all_valid = True

        for category in categories:
            name = category.get("name", "<unnamed>")
            logging.info(f"Checking category: {name}")

            unknown_keys = set(category.keys()) - {"name", "slug", "tools"}
            if unknown_keys:
                all_valid = False
                logging.error(
                    f"Category '{name}' has unexpected top-level keys: {sorted(unknown_keys)}. "
                    f"Tools must be placed inside the 'tools' object."
                )

            if not category.get("slug"):
                all_valid = False
                logging.error(f"Category '{name}' is missing 'slug'")

            tools = category.get("tools", {})
            if not tools:
                all_valid = False
                logging.error(f"Category '{name}' has no tools")
                continue

            for pkg_name, pkg_data in tools.items():
                required_fields = ["description", "url", "execs"]
                missing_fields = [f for f in required_fields if f not in pkg_data]

                if missing_fields:
                    all_valid = False
                    logging.error(
                        f"Tool '{pkg_name}' in '{name}' is missing required fields: {missing_fields}"
                    )
                    continue

                for field in required_fields:
                    if not pkg_data[field]:
                        all_valid = False
                        logging.error(
                            f"Tool '{pkg_name}' in '{name}' has empty '{field}'"
                        )

                if not isinstance(pkg_data["execs"], list) or not pkg_data["execs"]:
                    all_valid = False
                    logging.error(
                        f"Tool '{pkg_name}' in '{name}' must have at least one executable in 'execs'"
                    )

                if not pkg_data["url"].startswith(("http://", "https://")):
                    all_valid = False
                    logging.error(
                        f"Tool '{pkg_name}' in '{name}' has invalid URL format"
                    )

                # Optional examples field validation
                if "examples" in pkg_data:
                    if not isinstance(pkg_data["examples"], list):
                        all_valid = False
                        logging.error(
                            f"Tool '{pkg_name}' in '{name}': 'examples' must be a list"
                        )
                    else:
                        for i, example in enumerate(pkg_data["examples"]):
                            if not isinstance(example, dict):
                                all_valid = False
                                logging.error(
                                    f"Tool '{pkg_name}' in '{name}': examples[{i}] must be an object"
                                )
                                continue
                            if not example.get("cmd"):
                                all_valid = False
                                logging.error(
                                    f"Tool '{pkg_name}' in '{name}': examples[{i}] is missing 'cmd'"
                                )

        if all_valid:
            logging.info("All checks passed successfully!")
            return 0
        else:
            logging.error("Some checks failed. Please review the logs.")
            return 1

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return 1


if __name__ == "__main__":
    exit(check_tools())
