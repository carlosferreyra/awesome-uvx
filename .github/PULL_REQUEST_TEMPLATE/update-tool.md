## What tool metadata are you updating?

Package name:

Current category:

## What changed?

Check all that apply:

- [ ] Description
- [ ] URL
- [ ] Executable command(s)
- [ ] Category placement
- [ ] Examples
- [ ] Release metadata
- [ ] Other metadata

## Why is this update needed?

Please briefly explain what was incorrect, outdated, unclear, or missing.

## Checklist

- [ ] I updated only the relevant metadata in `tools.json`.
- [ ] I kept the package name as it appears on PyPI.
- [ ] I ran `uv run scripts/checks.py`.
- [ ] If I changed `execs`, I validated the affected commands with `uvx --from <package> <binary> --help` and recorded the commands and results below.

## Notes for the maintainer

Add any source links, context, or validation notes that will make this easier to review.
The `--diff` validator checks newly added packages; it does not validate executable changes to an
existing tool.
