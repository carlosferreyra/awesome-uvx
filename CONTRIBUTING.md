# Contributing to Awesome UVX

Thank you for your interest in contributing to Awesome UVX! This document provides guidelines for
contributing to this curated list of Python CLI tools.

## Adding a New Tool

To add a new CLI tool to the list:

1. The tool must be installable via UVX or PIPX
2. The tool must be a command-line interface (CLI) tool
3. The tool must be actively maintained
4. The tool should be useful for a general audience

### Required Information

Each tool entry needs:

- Name with a link to its documentation/repository
- A brief, clear description
- List of executable commands provided by the tool
- Must be added to the appropriate category JSON file in `.github/scripts/placeholders/`

### JSON Format

Add your tool to the appropriate category file in `.github/scripts/placeholders/`. The format should
be:

```json
{
	"category-slug": {
		"tool-name": {
			"description": "Brief description of the tool",
			"url": "https://link-to-documentation-or-repo",
			"execs": ["executable1", "executable2"]
		}
	}
}
```

## Pull Request Process

1. Fork the repository
2. Create a new branch for your changes
3. Add your tool to the appropriate JSON file in `.github/scripts/placeholders/`
4. The GitHub Actions workflow will automatically validate your changes and update the README
5. Make sure all checks pass
6. Create a pull request with a clear description of the tool you're adding

## Validation Checks

Your contribution will be automatically checked for:

- Required fields (description, URL, executables)
- Valid URL format (must start with http:// or https://)
- Non-empty executable list
- Proper JSON formatting

## Code of Conduct

Please note that this project is released with a Code of Conduct. By participating in this project
you agree to abide by its terms.

## Questions

If you have questions about contributing, please:

1. Check existing issues
2. Create a new issue if needed
3. Tag it appropriately

## License

By contributing to this project, you agree that your contributions will be licensed under the GNU
General Public License v3.0.
