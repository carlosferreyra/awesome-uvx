# Awesome UVX

<div align="center">
    <img width="500" height="350" src="https://github.com/sindresorhus/awesome/raw/main/media/logo.svg" alt="Awesome">
    <br>
    <a href="https://awesome.re">
        <img src="https://awesome.re/badge.svg" alt="Awesome">
    </a>
    <p>A collection of 107 Python CLI tools across 18 categories, available from UVX/PIPX.</p>
    <p>you can use this list to find useful Python CLI tools that are available for installation via UVX or
    PIPX. The list is curated and maintained by the community, so feel free to contribute by adding your
    own favorite tools.</p>
    <p>
        <img src="https://img.shields.io/github/contributors/carlosferreyra/awesome-uvx" alt="Contributors">
        <img src="https://img.shields.io/github/license/carlosferreyra/awesome-uvx" alt="License">
        <img src="https://badges.pufler.dev/visits/carlosferreyra/awesome-uvx" alt="Visits">
        <img src="https://img.shields.io/github/stars/carlosferreyra/awesome-uvx" alt="Stars">
    </p>
    <a href="https://github.com/carlosferreyra/awesome-uvx/actions/workflows/ci.yml">
        <img src="https://github.com/carlosferreyra/awesome-uvx/actions/workflows/ci.yml/badge.svg" alt="Validation and Sync">
    </a>
</div>

Inspired by <a href="https://github.com/vinta/awesome-python">awesome-python</a>.


## Contents


- [AI & Machine Learning](#ai-and-machine-learning) (5 tools)

- [Data Processing & Exploration](#data-processing-and-exploration) (4 tools)

- [Database & SQL Tools](#database-and-sql-tools) (11 tools)

- [Development Tools](#development-tools) (7 tools)

- [Documentation](#documentation) (3 tools)

- [Documents & Conversion](#documents-and-conversion) (6 tools)

- [HTTP & API Tools](#http-and-api-tools) (4 tools)

- [Web Frameworks & Servers](#web-frameworks-and-servers) (4 tools)

- [Testing & Code Quality](#testing-and-code-quality) (14 tools)

- [Profiling & Performance](#profiling-and-performance) (2 tools)

- [Packaging & Releases](#packaging-and-releases) (10 tools)

- [Security & Auditing](#security-and-auditing) (7 tools)

- [System & Infrastructure](#system-and-infrastructure) (6 tools)

- [Automation & Task Runners](#automation-and-task-runners) (5 tools)

- [Terminal & Shell Tools](#terminal-and-shell-tools) (7 tools)

- [Media & Downloads](#media-and-downloads) (3 tools)

- [Utilities](#utilities) (8 tools)

- [Miscellaneous](#miscellaneous) (1 tools)



<a id="ai-and-machine-learning"></a>

## AI & Machine Learning

| Name | Description | Executable(s) | Latest Release |
|:-----|:------------|:--------------|:--------------|
| [aider-chat](https://github.com/Aider-AI/aider) | AI pair programming in your terminal<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --python 3.12 --from aider-chat aider --help` — Use Python 3.12 for compatibility with pinned dependencies<br></details> | ```aider``` | 0.86.2 \|<br>2026-02-12 |
| [dvc](https://github.com/iterative/dvc) | Command-line tool for version control over data used in machine learning projects | ```dvc``` | 3.67.1 \|<br>2026-03-31 |
| [llm](https://llm.datasette.io/) | Run prompts and conversations with hosted or local language models<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from llm llm --help`<br></details> | ```llm``` | 0.36 \|<br>2026-09-22 |
| [mlflow](https://github.com/mlflow/mlflow) | Open source platform for managing the end-to-end machine learning lifecycle | ```mlflow``` | 3.16.1 \|<br>2026-09-16 |
| [rote-cli](https://github.com/trevhud/rote) | Compile an AI agent skill into a typed, deterministic pipeline with per-step tests<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from rote-cli rote analyze ./my-skill` — Report what a skill would compile to without emitting code<br>`uvx --from rote-cli rote compile ./my-skill --runtime python --out ./build` — Compile a skill into a runnable Python pipeline<br></details> | ```rote``` | — |



<a id="data-processing-and-exploration"></a>

## Data Processing & Exploration

| Name | Description | Executable(s) | Latest Release |
|:-----|:------------|:--------------|:--------------|
| [csvkit](https://csvkit.readthedocs.io/) | Suite of command-line tools for CSV files<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from csvkit csvlook data.csv` — Pretty-print a CSV file as a table<br>`uvx --from csvkit csvcut -c 1,3 data.csv` — Extract columns 1 and 3 from a CSV file<br></details> | ```csvclean```, ```csvcut```, ```csvformat```, ```csvgrep```, ```csvjoin```, ```csvjson```, ```csvlook```, ```csvpy```, ```csvsort```, ```csvsql```, ```csvstack```, ```csvstat```, ```in2csv```, ```sql2csv``` | 2.2.0 \|<br>2025-12-15 |
| [jc](https://github.com/kellyjonbrazil/jc) | Convert command output and file formats to structured JSON<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from jc jc --help`<br></details> | ```jc``` | 1.26.0 \|<br>2026-09-19 |
| [jello](https://github.com/kellyjonbrazil/jello) | Filter JSON and JSON Lines using Python expressions<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from jello jello --help`<br></details> | ```jello``` | 1.6.1 \|<br>2025-05-30 |
| [visidata](https://github.com/saulpw/visidata) | Interactive multitool for exploring, analyzing, and converting datasets in the terminal<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from visidata vd data.csv` — Open a CSV file in the interactive terminal UI<br></details> | ```vd```, ```visidata``` | 3.4 \|<br>2026-07-01 |



<a id="database-and-sql-tools"></a>

## Database & SQL Tools

| Name | Description | Executable(s) | Latest Release |
|:-----|:------------|:--------------|:--------------|
| [datasette](https://datasette.io/) | Explore and publish SQLite databases through a web interface<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from datasette datasette data.db`<br></details> | ```datasette``` | 0.65.5 \|<br>2026-09-17 |
| [fake2db](https://github.com/emirozer/fake2db) | Fake2db is a fake database generator for testing purposes. | ```fake2db``` | 0.5.4 \|<br>2018-02-09 |
| [harlequin](https://github.com/tconbeer/harlequin) | The SQL IDE for your terminal. A TUI for DuckDB, SQLite, Postgres, and more | ```harlequin``` | 2.15.0 \|<br>2026-09-16 |
| [iredis](https://github.com/laixintao/iredis) | Iredis is a Redis terminal client with auto-completion and syntax highlighting. | ```iredis``` | 1.16.1 \|<br>2026-03-27 |
| [litecli](https://litecli.com/) | Litecli is a command line interface for SQLite with auto-completion and syntax highlighting. | ```litecli``` | 1.17.1 \|<br>2026-01-31 |
| [mycli](https://www.mycli.net/) | Mycli is a command line interface for MySQL with auto-completion and syntax highlighting. | ```mycli``` | 2.26.0 \|<br>2026-09-26 |
| [peewee](http://docs.peewee-orm.com/) | Peewee is a small, expressive ORM for Python.<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from peewee pwiz.py -e sqlite mydb.db` — Introspect a SQLite database and generate model code<br></details> | ```pwiz.py``` | 4.5.2 \|<br>2026-09-27 |
| [pgcli](https://www.pgcli.com/) | Pgcli is a command line interface for PostgreSQL with auto-completion and syntax highlighting. | ```pgcli``` | 4.7.1 \|<br>2026-09-20 |
| [sqlfluff](https://www.sqlfluff.com/) | Lint and format SQL across multiple dialects<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from sqlfluff sqlfluff lint --dialect sqlite query.sql`<br></details> | ```sqlfluff``` | 4.4.0 \|<br>2026-10-02 |
| [sqlite-utils](https://github.com/simonw/sqlite-utils) | Python CLI utility and library for manipulating SQLite databases | ```sqlite-utils``` | 4.2.1 \|<br>2026-08-13 |
| [sqlparse](https://github.com/andialbrecht/sqlparse) | Sqlparse is a non-validating SQL parser for Python.<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from sqlparse sqlformat --reindent --keywords upper query.sql` — Reformat a SQL file with uppercase keywords and indentation<br></details> | ```sqlformat``` | 0.6.0 \|<br>2026-08-13 |



<a id="development-tools"></a>

## Development Tools

| Name | Description | Executable(s) | Latest Release |
|:-----|:------------|:--------------|:--------------|
| [cement](https://docs.builtoncement.com) | Advanced CLI Application Framework for Python | ```cement``` | 3.0.16 \|<br>2026-07-13 |
| [cookiecutter](https://cookiecutter.readthedocs.io/) | Project template tool | ```cookiecutter``` | 2.7.1 \|<br>2026-03-04 |
| [copier](https://copier.readthedocs.io/) | Library for rendering project templates | ```copier``` | 9.18.2 \|<br>2026-09-07 |
| [ipython](https://ipython.org/) | Enhanced interactive Python shell | ```ipython```, ```ipython3``` | 9.17.1 \|<br>2026-09-01 |
| [jupyter-core](https://jupyter.org/) | Core functionality for Jupyter projects<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from jupyter-core jupyter notebook` — Launch the Jupyter notebook server<br></details> | ```jupyter```, ```jupyter-migrate```, ```jupyter-troubleshoot``` | 5.9.1 \|<br>2025-10-16 |
| [pudb](https://github.com/inducer/pudb) | Full-screen, console-based visual debugger for Python | ```pudb``` | 2025.1.5 \|<br>2025-12-06 |
| [typer](https://typer.tiangolo.com/) | Build CLI applications | ```typer``` | 0.27.2 \|<br>2026-08-28 |



<a id="documentation"></a>

## Documentation

| Name | Description | Executable(s) | Latest Release |
|:-----|:------------|:--------------|:--------------|
| [markdown](https://python-markdown.github.io/) | Python implementation of Markdown<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from markdown markdown_py README.md > README.html` — Convert a Markdown file to HTML<br></details> | ```markdown_py``` | 3.11 \|<br>2026-09-25 |
| [pdoc](https://pdoc.dev/) | Auto-generate API documentation for Python projects | ```pdoc``` | 16.0.0 \|<br>2025-10-27 |
| [sphinx](https://www.sphinx-doc.org/) | Build project and API documentation in multiple output formats<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from sphinx sphinx-build -b html docs docs/_build/html`<br></details> | ```sphinx-apidoc```, ```sphinx-autogen```, ```sphinx-build```, ```sphinx-quickstart``` | 9.1.0 \|<br>2025-12-31 |



<a id="documents-and-conversion"></a>

## Documents & Conversion

| Name | Description | Executable(s) | Latest Release |
|:-----|:------------|:--------------|:--------------|
| [easyocr](https://www.jaided.ai/easyocr/) | Ready-to-use OCR with 80+ languages supported | ```easyocr``` | 1.7.2 \|<br>2024-09-24 |
| [html2text](https://github.com/Alir3z4/html2text/) | Convert HTML to Markdown-formatted text | ```html2text``` | 2025.4.15 \|<br>2025-04-15 |
| [img2pdf](https://pypi.org/project/img2pdf/) | Convert raster images to PDF without unnecessary re-encoding<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from img2pdf img2pdf photo.jpg -o photos.pdf`<br></details> | ```img2pdf``` | 0.6.3 \|<br>2025-11-05 |
| [markitdown](https://github.com/microsoft/markitdown) | Convert documents and other file formats to Markdown<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from "markitdown[all]" markitdown document.docx -o document.md` — Convert a document with optional format dependencies installed<br></details> | ```markitdown``` | 0.1.8 \|<br>2026-09-21 |
| [ocrmypdf](https://ocrmypdf.readthedocs.io/) | Add a searchable OCR text layer to scanned PDF files<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from ocrmypdf ocrmypdf scanned.pdf searchable.pdf`<br></details> | ```ocrmypdf``` | 17.13.0 \|<br>2026-09-28 |
| [textract](https://textract.readthedocs.io/) | Extract text from various document formats | ```textract``` | 2.1.0 \|<br>2026-09-01 |



<a id="http-and-api-tools"></a>

## HTTP & API Tools

| Name | Description | Executable(s) | Latest Release |
|:-----|:------------|:--------------|:--------------|
| [httpie](https://httpie.io/) | User-friendly command-line HTTP client<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from httpie http GET https://httpbin.org/get` — Make a GET request and pretty-print the response<br>`uvx --from httpie http POST https://httpbin.org/post name=alice` — Send a POST request with a JSON body field<br></details> | ```http```, ```httpie```, ```https``` | 3.2.4 \|<br>2024-11-01 |
| [mitmproxy](https://github.com/mitmproxy/mitmproxy) | Free and open source interactive HTTPS proxy for penetration testers and software developers | ```mitmproxy```, ```mitmdump```, ```mitmweb``` | 12.2.3 \|<br>2026-05-12 |
| [posting](https://posting.sh/) | Terminal HTTP client with saved request collections and OpenAPI imports<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --python 3.13 --from posting posting` — Launch the terminal HTTP client with Python 3.13<br></details> | ```posting``` | 2.11.0 \|<br>2026-09-26 |
| [websockets](https://github.com/aaugustin/websockets) | Library for building WebSocket servers and clients | ```websockets``` | 17.1 \|<br>2026-08-26 |



<a id="web-frameworks-and-servers"></a>

## Web Frameworks & Servers

| Name | Description | Executable(s) | Latest Release |
|:-----|:------------|:--------------|:--------------|
| [django](https://www.djangoproject.com/) | High-level Python web framework<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from django django-admin startproject myproject` — Create a new Django project scaffold<br></details> | ```django-admin``` | 6.1.1 \|<br>2026-09-02 |
| [fastapi[standard]](https://fastapi.tiangolo.com/) | Modern, fast web framework for building APIs | ```fastapi``` | 0.141.1 \|<br>2026-07-29 |
| [flask](https://flask.palletsprojects.com/) | Lightweight WSGI web application framework | ```flask``` | 3.1.3 \|<br>2026-02-19 |
| [uvicorn](https://www.uvicorn.org/) | Lightning-fast ASGI server | ```uvicorn``` | 0.54.0 \|<br>2026-09-25 |



<a id="testing-and-code-quality"></a>

## Testing & Code Quality

| Name | Description | Executable(s) | Latest Release |
|:-----|:------------|:--------------|:--------------|
| [black](https://github.com/psf/black) | The uncompromising Python code formatter | ```black``` | 26.5.1 \|<br>2026-05-18 |
| [coverage](https://coverage.readthedocs.io/) | Code coverage measurement | ```coverage```, ```coverage-3.13```, ```coverage3``` | 7.16.2 \|<br>2026-09-27 |
| [deptry](https://deptry.com/) | Check Python projects for dependency declaration issues<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from deptry deptry .`<br></details> | ```deptry``` | 0.25.1 \|<br>2026-03-18 |
| [mypy](https://mypy.readthedocs.io/) | Optional static typing for Python | ```mypy```, ```mypy-langserver``` | 2.3.1 \|<br>2026-08-15 |
| [nox](https://nox.thea.codes/) | Flexible test automation | ```nox```, ```tox-to-nox``` | 2026.8.17 \|<br>2026-08-18 |
| [pre-commit](https://github.com/pre-commit/pre-commit) | Framework for managing and maintaining multi-language git hooks | ```pre-commit``` | 4.6.2 \|<br>2026-08-10 |
| [pyright](https://github.com/microsoft/pyright) | Static type checker for Python | ```pyright```, ```pyright-langserver```, ```pyright-python```, ```pyright-python-langserver``` | 1.1.414 \|<br>2026-09-10 |
| [pytest](https://docs.pytest.org/) | Testing framework | ```pytest```, ```py.test``` | 9.1.1 \|<br>2026-06-19 |
| [ruff](https://github.com/astral-sh/ruff) | An extremely fast Python linter | ```ruff``` | 0.16.9 \|<br>2026-09-24 |
| [schemathesis](https://schemathesis.readthedocs.io/) | Property-based testing for APIs | ```schemathesis```, ```st``` | 4.28.0 \|<br>2026-09-22 |
| [tavern](https://github.com/taverntesting/tavern) | pytest plugin, command-line tool, and Python library for automated testing of APIs | ```tavern-ci``` | 3.7.0 \|<br>2026-09-25 |
| [tox](https://tox.wiki/) | Automate and standardize testing | ```tox``` | 4.64.4 \|<br>2026-09-27 |
| [ty](https://github.com/astral-sh/ty) | An extremely fast Python type checker and language server | ```ty``` | 0.0.84 \|<br>2026-09-24 |
| [vulture](https://github.com/jendrikseipp/vulture) | Find unused code in Python projects<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from vulture vulture src`<br></details> | ```vulture``` | 2.16 \|<br>2026-03-25 |



<a id="profiling-and-performance"></a>

## Profiling & Performance

| Name | Description | Executable(s) | Latest Release |
|:-----|:------------|:--------------|:--------------|
| [memray](https://github.com/bloomberg/memray) | Track Python memory allocations and generate profiling reports<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from memray memray run script.py`<br></details> | ```memray``` | 1.20.0 \|<br>2026-08-07 |
| [scalene](https://github.com/plasma-umass/scalene) | Profile CPU, GPU, and memory usage in Python programs<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from scalene scalene script.py`<br></details> | ```scalene``` | 2.3.0 \|<br>2026-05-12 |



<a id="packaging-and-releases"></a>

## Packaging & Releases

| Name | Description | Executable(s) | Latest Release |
|:-----|:------------|:--------------|:--------------|
| [bump-my-version](https://callowayproject.github.io/bump-my-version/) | Update version numbers across project files<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from bump-my-version bump-my-version --help`<br></details> | ```bump-my-version``` | 1.5.1 \|<br>2026-08-06 |
| [commitizen](https://commitizen-tools.github.io/commitizen/) | Standardize commit messages, version bumps, and changelogs<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from commitizen cz --help`<br></details> | ```cz```, ```git-cz``` | 4.19.0 \|<br>2026-09-22 |
| [pipx](https://pypa.github.io/pipx/) | Install and run Python applications in isolated environments | ```pipx``` | 1.17.7 \|<br>2026-09-28 |
| [poetry](https://python-poetry.org/) | Python packaging and dependency management | ```poetry``` | 2.5.1 \|<br>2026-09-20 |
| [py2app](https://py2app.readthedocs.io/) | Create standalone Mac OS X applications<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from py2app py2applet --make-setup myscript.py` — Generate a setup.py for bundling a script into a Mac app<br></details> | ```py2applet``` | 0.28.10 \|<br>2026-02-13 |
| [pyarmor](https://pyarmor.dashingsoft.com/) | Tool for obfuscating Python scripts | ```pyarmor```, ```pyarmor-7```, ```pyarmor-8```, ```pyarmor-auth``` | 9.2.7 \|<br>2026-08-29 |
| [pyinstaller](https://www.pyinstaller.org/) | Convert Python programs into stand-alone executables<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from pyinstaller pyinstaller --onefile myscript.py` — Bundle a script into a single standalone executable<br></details> | ```pyi-archive_viewer```, ```pyi-bindepend```, ```pyi-grab_version```, ```pyi-makespec```, ```pyi-set_version```, ```pyinstaller``` | 6.22.3 \|<br>2026-09-12 |
| [shiv](https://github.com/linkedin/shiv) | Build fully self-contained Python zipapps | ```shiv```, ```shiv-info``` | 1.0.8 \|<br>2024-11-01 |
| [uv](https://github.com/astral-sh/uv) | Extremely fast Python package installer and resolver, written in Rust | ```uv``` | 0.12.19 \|<br>2026-09-25 |
| [uv-upsync](https://github.com/pivoshenko/uv-upsync) | uv-upsync is a uv-native tool for automated dependency updates and version bumping in pyproject.toml | ```uv-upsync``` | 2.4.2 \|<br>2026-09-20 |



<a id="security-and-auditing"></a>

## Security & Auditing

| Name | Description | Executable(s) | Latest Release |
|:-----|:------------|:--------------|:--------------|
| [bandit](https://bandit.readthedocs.io/) | Scan Python source code for common security issues<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from bandit bandit -r src`<br></details> | ```bandit```, ```bandit-baseline```, ```bandit-config-generator``` | 1.9.4 \|<br>2026-02-25 |
| [detect-secrets](https://github.com/Yelp/detect-secrets) | Enterprise-friendly CLI for auditing, detecting, and preventing secrets in code | ```detect-secrets``` | 1.5.0 \|<br>2024-05-06 |
| [fsociety](https://github.com/fsociety-team/fsociety) | Modular penetration testing framework | ```fsociety``` | 3.2.9 \|<br>2023-06-16 |
| [pip-audit](https://github.com/pypa/pip-audit) | Audit Python dependencies for known vulnerabilities<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from pip-audit pip-audit -r requirements.txt`<br></details> | ```pip-audit``` | 2.10.1 \|<br>2026-06-10 |
| [scapy](https://scapy.net/) | Packet manipulation program | ```scapy``` | 2.7.0 \|<br>2025-12-26 |
| [sqlmap](https://sqlmap.org/) | Automatic SQL injection and database takeover tool | ```sqlmap``` | 1.10.9 \|<br>2026-09-02 |
| [uncompyle6](https://github.com/rocky/python-uncompyle6) | Native Python cross-version decompiler that translates Python bytecode back into equivalent Python source code | ```uncompyle6``` | 3.9.3 \|<br>2025-09-29 |



<a id="system-and-infrastructure"></a>

## System & Infrastructure

| Name | Description | Executable(s) | Latest Release |
|:-----|:------------|:--------------|:--------------|
| [ansible](https://www.ansible.com/) | Automation tool for IT infrastructure<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from ansible ansible-community --version` — Check the installed Ansible community version<br></details> | ```ansible-community``` | 14.4.0 \|<br>2026-09-08 |
| [awscli](https://aws.amazon.com/cli/) | Official command-line interface for Amazon Web Services | ```aws``` | 1.46.1 \|<br>2026-08-27 |
| [bpytop](https://github.com/aristocratos/bpytop) | Resource monitor that shows usage and stats for processor, memory, disks, network, and processes | ```bpytop``` | 1.0.68 \|<br>2021-12-22 |
| [glances](https://github.com/nicolargo/glances) | Cross-platform monitoring tool with curses or Web based interface | ```glances``` | 4.5.7 \|<br>2026-09-26 |
| [mamba](https://github.com/mamba-org/mamba) | Fast, cross-platform package manager | ```mamba``` | 0.11.3 \|<br>2023-11-09 |
| [platformio](https://github.com/platformio/platformio-core) | Open source ecosystem for IoT development with cross-platform IDE and unified debugger | ```platformio```, ```pio``` | 6.2.0 \|<br>2026-09-05 |



<a id="automation-and-task-runners"></a>

## Automation & Task Runners

| Name | Description | Executable(s) | Latest Release |
|:-----|:------------|:--------------|:--------------|
| [celery](https://docs.celeryq.dev/) | Distributed task queue | ```celery``` | 5.6.3 \|<br>2026-03-26 |
| [invoke](https://github.com/pyinvoke/invoke) | Tool for managing shell-oriented subprocesses and organizing executable Python code into CLI-invokable tasks | ```invoke```, ```inv``` | 3.0.3 \|<br>2026-04-07 |
| [plan](https://github.com/fengsp/plan) | Crontab file manager | ```plan-quickstart``` | 0.5 \|<br>2015-02-16 |
| [prefect](https://www.prefect.io/) | Workflow management system | ```prefect``` | 3.8.7 \|<br>2026-09-27 |
| [rq](https://python-rq.org/) | Simple job queues for Python | ```rq```, ```rqinfo```, ```rqworker``` | 2.12.0 \|<br>2026-08-30 |



<a id="terminal-and-shell-tools"></a>

## Terminal & Shell Tools

| Name | Description | Executable(s) | Latest Release |
|:-----|:------------|:--------------|:--------------|
| [asciinema](https://asciinema.org) | Terminal session recorder<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx asciinema rec demo.cast` — Record a terminal session to a .cast file<br>`uvx asciinema play demo.cast` — Play back a recorded terminal session<br>`uvx asciinema upload demo.cast` — Upload a recording to asciinema.org<br></details> | ```asciinema``` | 2.4.0 \|<br>2023-10-23 |
| [doitlive](https://doitlive.readthedocs.io/) | Tool for live presentations in the terminal | ```doitlive``` | 5.2.1 \|<br>2026-02-16 |
| [rich-cli](https://github.com/Textualize/rich-cli) | Render rich text, Markdown, JSON, and syntax-highlighted code in the terminal | ```rich``` | 1.8.1 \|<br>2025-07-04 |
| [termtosvg](https://github.com/nbedos/termtosvg) | Record terminal sessions as SVG animations<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx termtosvg demo.svg` — Record a terminal session and save as SVG animation<br>`uvx termtosvg --template window_frame --screen-geometry 80x20 demo.svg` — Record with a window frame template at 80x20 geometry<br>`uvx termtosvg -c "ls -la" demo.svg` — Record a single command output as SVG<br></details> | ```termtosvg``` | 1.1.0 \|<br>2020-01-18 |
| [thefuck](https://github.com/nvbn/thefuck) | Magnificent application that corrects your previous console command | ```thefuck```, ```fuck``` | 3.32 \|<br>2022-01-02 |
| [tmuxp](https://tmuxp.git-pull.com) | tmux session manager — save and load tmux sessions via config files<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx tmuxp load mysession.yaml` — Load a tmux session from a YAML config file<br></details> | ```tmuxp``` | 1.74.0 \|<br>2026-07-04 |
| [xonsh](https://xon.sh/) | Python-powered shell | ```xonsh```, ```xonsh-cat```, ```xonsh-uname```, ```xonsh-uptime``` | 0.24.2 \|<br>2026-08-23 |



<a id="media-and-downloads"></a>

## Media & Downloads

| Name | Description | Executable(s) | Latest Release |
|:-----|:------------|:--------------|:--------------|
| [streamlink](https://github.com/streamlink/streamlink) | CLI utility that pipes video streams from various services into a video player | ```streamlink``` | 8.6.1 \|<br>2026-09-16 |
| [youtube-dl](https://youtube-dl.org/) | Download videos from YouTube and other video sites | ```youtube-dl``` | 2021.12.17 \|<br>2021-12-16 |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | Feature-rich audio/video downloader supporting thousands of sites — actively maintained fork of youtube-dl<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx yt-dlp https://www.youtube.com/watch?v=dQw4w9WgXcQ` — Download a YouTube video<br>`uvx yt-dlp -x --audio-format mp3 https://www.youtube.com/watch?v=dQw4w9WgXcQ` — Extract audio as MP3 from a YouTube video<br></details> | ```yt-dlp``` | 2026.8.19 \|<br>2026-08-19 |



<a id="utilities"></a>

## Utilities

| Name | Description | Executable(s) | Latest Release |
|:-----|:------------|:--------------|:--------------|
| [faker](https://faker.readthedocs.io/) | Generator for fake data | ```faker``` | 40.39.0 \|<br>2026-09-14 |
| [howdoi](https://github.com/gleitz/howdoi) | Instant coding answers via the command line | ```howdoi``` | 2.0.20 \|<br>2022-10-03 |
| [magic-wormhole](https://github.com/magic-wormhole/magic-wormhole) | Tool to get things from one computer to another, safely<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx --from magic-wormhole wormhole send myfile.txt` — Send a file to another computer via a one-time code<br>`uvx --from magic-wormhole wormhole receive` — Receive a file using the one-time code from the sender<br></details> | ```wormhole``` | 0.24.0 \|<br>2026-05-05 |
| [pyclean](https://github.com/bittner/pyclean) | Pure Python cross-platform pycache cleaner | ```pyclean``` | 3.7.0 \|<br>2026-05-23 |
| [qrcode](https://github.com/lincolnloop/python-qrcode) | Pure Python QR Code generator<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`echo 'https://example.com' \| uvx --from qrcode qr` — Generate a QR code from a URL<br></details> | ```qr``` | 8.2 \|<br>2025-05-01 |
| [shortuuid](https://github.com/skorokithakis/shortuuid) | Generator for concise, unambiguous, URL-safe UUIDs | ```shortuuid``` | 1.0.13 \|<br>2024-03-11 |
| [speedtest-cli](https://github.com/sivel/speedtest-cli) | Command line interface for testing internet bandwidth using speedtest.net | ```speedtest-cli``` | 2.1.3 \|<br>2021-04-08 |
| [unp](https://github.com/mitsuhiko/unp) | Command line tool that can unpack archives | ```unp``` | 0.3 \|<br>2014-08-24 |



<a id="miscellaneous"></a>

## Miscellaneous

| Name | Description | Executable(s) | Latest Release |
|:-----|:------------|:--------------|:--------------|
| [carlosferreyra](https://github.com/carlosferreyra/carlosferreyra) | Interactive CLI business card for Carlos Ferreyra<br><details><summary><strong><a href="#">Examples</a></strong></summary><br>`uvx carlosferreyra --open github` — Open GitHub profile directly<br></details> | ```carlosferreyra``` | 1.2.15 \|<br>2026-06-23 |




## Contributing

Feel free to contribute by opening a pull request with your favorite Python CLI tools that can be
installed via UVX or PIPX!
Please make sure to follow the <a href="CONTRIBUTING.md">contribution guidelines</a> and adhere to the <a href="CODE_OF_CONDUCT.md">code of conduct</a>.
Please also check the <a href="https://github.com/carlosferreyra/awesome-uvx/issues">issues</a> for any open issues or discussions related to the project.

## License

This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.