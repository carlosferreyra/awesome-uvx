# Contributing to Awesome UVX

Thank you for your interest in contributing to Awesome UVX! This document provides guidelines for
contributing to this curated list of Python CLI tools.

## Adding a New Tool

To add a new CLI tool to the list:

1. The tool must be installable via UVX or PIPX, and it must pass this repo's `uvx` validation
2. The tool must be a command-line interface (CLI) tool
3. The tool should have credible support and remain useful on its documented platforms
4. The tool should be useful for a general audience
5. The tool should offer a clear capability or practical advantage over existing entries

Assess support in context: mature, stable, or feature-complete tools do not need frequent
releases. Explain the tool's distinct value, documented invocation, supported platforms, and
material prerequisites such as accounts, payment, credentials, or external services.

Use official documentation and registry metadata to qualify a proposal. Treat installation and
a meaningful CLI invocation as separate validation, following this repository's checks before
acceptance. Do not claim that metadata or a successful installation alone proves runtime behavior.

GitHub stars may help prioritize research among otherwise suitable candidates. There is no minimum
star count, and popularity alone does not determine addition, retention, replacement, or removal.
Do not disadvantage niche tools, new projects, non-GitHub hosting, or packages in shared monorepos.

### Updating, Replacing, or Removing a Tool

Prefer the smallest correction that restores usefulness: update commands, package names, URLs,
prerequisites, descriptions, or version guidance before proposing removal.

A removal needs a specific, corroborated reason that keeping the entry would mislead or poorly
serve users, such as confirmed package unavailability, persistent failure on a supported platform,
misleading package identity, explicit retirement affecting continued use, or a material unresolved
security problem that cannot reasonably be addressed by an upgrade or usage correction.

Archival, feature completeness, old releases, quiet development, low stars, or a more popular
competitor alone do not justify deletion. Defer when evidence is insufficient, and distinguish
temporary outages or unsupported environments from defects in the tool.

For a replacement, verify the successor and compare essential functionality, platform coverage,
prerequisites, migration costs, and lost capabilities. Explain what users gain and lose, with
evidence and estimated maintainer effort. Choose an explicit outcome: retain, update, replace,
remove, or defer.

### Required Information

Each tool entry needs:

- A unique package name (as it appears on PyPI)
- A brief, clear description
- A link to its documentation or repository
- A list of executable commands the package installs

### Where to Edit

All tool data lives in a single file at the root of the repository: **`tools.json`**.

The file has a top-level `"categories"` array. Find the category that best fits your tool and add
an entry to its `"tools"` object. If no existing category fits, you can propose a new one (see
below).

### JSON Format

```json
{
  "categories": [
    {
      "name": "Category Name",
      "slug": "category-slug",
      "tools": {
        "your-package-name": {
          "description": "Brief description of the tool",
          "url": "https://link-to-documentation-or-repo",
          "execs": ["executable1", "executable2"]
        }
      }
    }
  ]
}
```

**Field reference:**

| Field        | Required | Description                                                   |
| :----------- | :------: | :------------------------------------------------------------ |
| `description`| yes      | One-line description of what the tool does                    |
| `url`        | yes      | Link to official docs or repo (`http://` or `https://` only)  |
| `execs`      | yes      | Non-empty list of binary names installed by the package       |
| `examples`   | no       | List of example objects (see below)                           |

> **Tip:** The package name key is what gets passed to `uvx --from <package>`. If the binary name
> differs from the package name (e.g. package `qrcode` installs binary `qr`), make sure `execs`
> reflects the actual binary name.

### Adding Examples

The `examples` field is optional but encouraged when the invocation is non-obvious — for example
when the package name differs from the binary, piped input is required, or a subcommand is needed
to do anything useful.

Keep examples inside their tool definition in `tools.json`. The README template displays them in
collapsible blocks below the category table.

Each example is an object with a required `cmd` and an optional `description`:

```json
"your-package-name": {
  "description": "...",
  "url": "...",
  "execs": ["binary-name"],
  "examples": [
    {
      "cmd": "uvx --from your-package-name binary-name --some-flag",
      "description": "What this example does"
    }
  ]
}
```

**Example field reference:**

| Field         | Required | Description                                        |
| :------------ | :------: | :------------------------------------------------- |
| `cmd`         | yes      | Full shell command the user can copy and run       |
| `description` | no       | One-line explanation of what the command does      |

Guidelines for writing good examples:

- Always use the full `uvx --from <package> <binary>` form so the command works out of the box
- Prefer short, realistic commands over exhaustive flag lists
- Add multiple examples only when they demonstrate meaningfully different use cases

### Choosing a Category

Choose one existing category based on the tool's primary purpose. Categories reflect this Python
catalog; they do not need to match the JavaScript or Rust lists.

- **Development Tools** covers project generators such as `cookiecutter` and `copier`, debuggers,
  and general developer CLIs. Framework launch and server commands belong in **Web Frameworks &
  Servers**.
- **Packaging & Releases** covers dependency environments, package builds and distribution,
  versioning, and commit conventions used in release workflows, including `commitizen`.
- **Testing & Code Quality** covers test-focused workflows such as `tox` and `nox`.
  General-purpose task execution and orchestration belong in **Automation & Task Runners**.

Keep category-only reorganizations separate from adding tools. When two categories fit, explain
the main use case in the PR. Preserve existing category slugs when changing display names so
README links keep working.

### Adding a New Category

If your tool doesn't fit any existing category, add a new object to the `"categories"` array:

```json
{
  "name": "Human Readable Name",
  "slug": "url-friendly-slug",
  "tools": { ... }
}
```

Keep the slug lowercase, hyphen-separated, and consistent with the name.

## Generated README

After changing `tools.json` or `template/README.md.j2`, run:

```bash
uv run scripts/readme.py
```

Include the generated `README.md` in the same PR. Do not edit it by hand. CI regenerates
it and fails if the committed README is out of date; it does not commit or push updates.

## Pull Request Process

1. Fork the repository
2. Create a new branch for your changes
3. Edit `tools.json` to add your tool to the appropriate category
4. Run `uv run scripts/checks.py` locally to validate your changes
5. Run `uv run scripts/test_clients.py --diff origin/main --output output.log` to test newly added tools with `uvx`
6. Run `uv run scripts/readme.py` and include the generated `README.md`.
7. Make sure all checks pass
8. Create a pull request with a clear description of the tool you're adding

The GitHub Actions workflow will automatically validate `tools.json` and test newly added tools with
`uvx` on every PR.

### Choosing a Pull Request Template

Use the template that best matches your change:

- [Add a new tool](https://github.com/carlosferreyra/awesome-uvx/compare/main...main?quick_pull=1&template=add-tool.md)
- [Update existing tool metadata](https://github.com/carlosferreyra/awesome-uvx/compare/main...main?quick_pull=1&template=update-tool.md)
- [Repo maintenance or refactor](https://github.com/carlosferreyra/awesome-uvx/compare/main...main?quick_pull=1&template=repo-maintenance.md)

After opening one of these links, choose your branch as the compare branch if GitHub does not select
it automatically.

If none of these fit, use the default pull request template and explain the change clearly.

## Validation Checks

Your contribution will be automatically checked for:

- Required fields (`description`, `url`, `execs`)
- Valid URL format (must start with `http://` or `https://`)
- Non-empty executable list
- Valid JSON structure
- Newly added tools can be installed and executed with `uvx`

To run the same validation locally before opening a PR:

```bash
uv run scripts/checks.py
uv run scripts/test_clients.py --diff origin/main --output output.log
uv run scripts/readme.py
```

## Code of Conduct

Please note that this project is released with a Code of Conduct. By participating in this project
you agree to abide by its terms.

## Questions

If you have questions about contributing, please:

1. Check existing issues
2. Create a new issue if needed
3. Tag it appropriately

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT
License.
