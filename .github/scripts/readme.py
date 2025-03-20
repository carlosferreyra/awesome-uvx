# /// script
# dependencies = ['jinja2']
# ///
"""Script for generating an updated README following PEP 723 format."""

import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


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


def generate_readme():
    """
    Generate the README file using Jinja2 template and JSON data"""
    try:
        # Get the script's directory
        script_dir = Path(__file__).parent
        # Path to placeholders directory
        placeholders_dir = script_dir / "placeholders"

        # Load all JSON files from placeholders directory
        tree_data = load_json_files(placeholders_dir)

        # Setup Jinja2 environment with proper path
        env = Environment(loader=FileSystemLoader(script_dir / "template"))
        template = env.get_template("README.md.jinja2")

        # Render the template with our data
        readme_content = template.render(
            sections=tree_data,
            total_packages=sum(
                len(section) - 1 for section in tree_data.values()
            ),  # -1 for slug key
        )

        # Write the generated README
        readme_path = script_dir.parent.parent / "README.md"
        with open(readme_path, "w") as f:
            f.write(readme_content)

        print(f"Successfully generated README at {readme_path}")

    except FileNotFoundError as e:
        print(f"Error: Could not find required file: {e.filename}")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    generate_readme()
