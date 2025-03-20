# /// script
# dependencies = ['jinja2']
# ///
"""Script for validating each UVX/PIPX client following PEP 723 format."""

import json
import logging
from pathlib import Path


def load_json_files(placeholders_dir: Path) -> dict:
    """
    Load all JSON files from the specified directory and return a dictionary
    """
    sections = {}
    for json_file in placeholders_dir.glob("*.json"):
        section_name = json_file.stem  # Get filename without extension
        with open(json_file) as f:
            content = json.load(f)
            # The first key in the JSON is the slug, and its value contains the packages
            slug, packages = next(iter(content.items()))
            # Add the section with its packages and slug
            sections[section_name] = {"slug": slug, **packages}
    return sections


def check_json_files():
    """
    Check each JSON file in the placeholders directory for missing keys and values.
    """
    # Setup logging
    logging.basicConfig(
        filename="checks.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    script_dir = Path(__file__).parent
    placeholders_dir = script_dir / "placeholders"

    try:
        sections = load_json_files(placeholders_dir)
        all_valid = True

        for section_name, section_data in sections.items():
            logging.info(f"Checking section: {section_name}")

            # Skip the slug key as it's not a package
            packages = {k: v for k, v in section_data.items() if k != "slug"}

            for pkg_name, pkg_data in packages.items():
                # Required fields
                required_fields = ["description", "url", "execs"]
                missing_fields = [
                    field for field in required_fields if field not in pkg_data
                ]

                if missing_fields:
                    all_valid = False
                    logging.error(
                        f"Package '{pkg_name}' in '{section_name}' is missing required fields: {missing_fields}"
                    )
                    continue

                # Check if fields are not empty
                for field in required_fields:
                    if not pkg_data[field]:
                        all_valid = False
                        logging.error(
                            f"Package '{pkg_name}' in '{section_name}' has empty {field}"
                        )

                # Check if execs is a non-empty list
                if not isinstance(pkg_data["execs"], list) or not pkg_data["execs"]:
                    all_valid = False
                    logging.error(
                        f"Package '{pkg_name}' in '{section_name}' must have at least one executable in 'execs'"
                    )

                # Check URL format
                if not pkg_data["url"].startswith(("http://", "https://")):
                    all_valid = False
                    logging.error(
                        f"Package '{pkg_name}' in '{section_name}' has invalid URL format"
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
    exit(check_json_files())
