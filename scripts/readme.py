# /// script
# requires-python = ">=3.12"
# dependencies = ["jinja2"]
# ///
"""Script for generating README.md from tools.json."""

import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def load_tools(tools_path: Path) -> list:
    with open(tools_path) as f:
        return json.load(f)["categories"]


def generate_readme():
    try:
        repo_root = Path(__file__).parent.parent
        tools_path = repo_root / "tools.json"
        template_dir = repo_root / "template"

        categories = load_tools(tools_path)
        total_tools = sum(len(cat["tools"]) for cat in categories)

        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template("README.md.jinja2")

        readme_content = template.render(
            categories=categories,
            total_tools=total_tools,
        )

        readme_path = repo_root / "README.md"
        with open(readme_path, "w") as f:
            f.write(readme_content)

        print(f"Successfully generated README at {readme_path}")

    except FileNotFoundError as e:
        print(f"Error: Could not find required file: {e.filename}")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    generate_readme()
