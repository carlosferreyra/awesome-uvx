# Awesome UVX

<div align="center">
    <img width="500" height="350" src="https://github.com/sindresorhus/awesome/raw/main/media/logo.svg" alt="Awesome">
    <br>
    <a href="https://awesome.re">
        <img src="https://awesome.re/badge.svg" alt="Awesome">
    </a>
    <p>A collection of Awesome Python CLI Tools available from UVX/PIPX.</p>
    <p>you can use this list to find useful Python CLI tools that are available for installation via UVX or
    PIPX. The list is curated and maintained by the community, so feel free to contribute by adding your
    own favorite tools.</p>
    <p>
        <img src="https://img.shields.io/github/contributors/carlosferreyra/awesome-uvx" alt="Contributors">
        <img src="https://img.shields.io/github/license/carlosferreyra/awesome-uvx" alt="License">
        <img src="https://badges.pufler.dev/visits/carlosferreyra/awesome-uvx" alt="Visits">
        <img src="https://img.shields.io/github/stars/carlosferreyra/awesome-uvx" alt="Stars">
    </p>
    <a href="https://github.com/carlosferreyra/awesome-uvx/actions/workflows/main.yml">
        <img src="https://github.com/carlosferreyra/awesome-uvx/actions/workflows/main.yml/badge.svg" alt="Test Packages">
    </a>
</div>

Inspired by <a href="https://github.com/vinta/awesome-python">awesome-python</a>.



- [Data Processing](#data-processing)

- [Testing & Quality](#testing-quality)

- [Security & Penetration Testing](#security--penetration-testing)

- [Utilities](#utilities)

- [Web Frameworks & Tools](#web-frameworks-and-tools)

- [Development Tools](#development-tools)

- [System & Infrastructure](#system-and-infrastructure)

- [Documentation](#documentation)

- [Database Tools](#database-tools)



## Data Processing

| Name | Description | Executable(s) |
|:-----|:------------|:--------------|
| [csvkit](https://csvkit.readthedocs.io/) | Suite of command-line tools for CSV files | ```csvclean```, ```csvcut```, ```csvformat```, ```csvgrep```, ```csvjoin```, ```csvjson```, ```csvlook```, ```csvpy```, ```csvsort```, ```csvsql```, ```csvstack```, ```csvstat```, ```in2csv```, ```sql2csv``` |
| [dvc](https://github.com/iterative/dvc) | Command-line tool for version control over data used in machine learning projects | ```dvc``` |
| [easyocr](https://www.jaided.ai/easyocr/) | Ready-to-use OCR with 80+ languages supported | ```easyocr``` |
| [mlflow](https://github.com/mlflow/mlflow) | Open source platform for managing the end-to-end machine learning lifecycle | ```mlflow``` |
| [qrcode](https://github.com/lincolnloop/python-qrcode) | Pure Python QR Code generator | ```qr``` |
| [shortuuid](https://github.com/skorokithakis/shortuuid) | Generator for concise, unambiguous, URL-safe UUIDs | ```shortuuid``` |
| [textract](https://textract.readthedocs.io/) | Extract text from various document formats | ```textract``` |



## Testing & Quality

| Name | Description | Executable(s) |
|:-----|:------------|:--------------|
| [coverage](https://coverage.readthedocs.io/) | Code coverage measurement | ```coverage```, ```coverage-3.13```, ```coverage3``` |
| [nox](https://nox.thea.codes/) | Flexible test automation | ```nox```, ```tox-to-nox``` |
| [pytest](https://docs.pytest.org/) | Testing framework | ```py.test```, ```pytest``` |
| [schemathesis](https://schemathesis.readthedocs.io/) | Property-based testing for APIs | ```schemathesis```, ```st``` |
| [tavern](https://github.com/taverntesting/tavern) | pytest plugin, command-line tool, and Python library for automated testing of APIs | ```tavern-ci``` |
| [tox](https://tox.wiki/) | Automate and standardize testing | ```tox``` |



## Security & Penetration Testing

| Name | Description | Executable(s) |
|:-----|:------------|:--------------|
| [detect-secrets](https://github.com/Yelp/detect-secrets) | Enterprise-friendly CLI for auditing, detecting, and preventing secrets in code | ```detect-secrets``` |
| [fsociety](https://github.com/fsociety-team/fsociety) | Modular penetration testing framework | ```fsociety``` |
| [pyinstxtractor](https://github.com/extremecoders-re/pyinstxtractor) | Tool to extract the contents of a PyInstaller generated Windows executable file | ```pyinstxtractor``` |
| [scapy](https://scapy.net/) | Packet manipulation program | ```scapy``` |
| [sqlmap](https://sqlmap.org/) | Automatic SQL injection and database takeover tool | ```sqlmap``` |
| [uncompyle6](https://github.com/rocky/python-uncompyle6) | Native Python cross-version decompiler that translates Python bytecode back into equivalent Python source code | ```uncompyle6``` |



## Utilities

| Name | Description | Executable(s) |
|:-----|:------------|:--------------|
| [celery](https://docs.celeryq.dev/) | Distributed task queue | ```celery``` |
| [cookiecutter](https://cookiecutter.readthedocs.io/) | Project template tool | ```cookiecutter``` |
| [copier](https://copier.readthedocs.io/) | Library for rendering project templates | ```copier``` |
| [doitlive](https://doitlive.readthedocs.io/) | Tool for live presentations in the terminal | ```doitlive``` |
| [faker](https://faker.readthedocs.io/) | Generator for fake data | ```faker``` |
| [howdoi](https://github.com/gleitz/howdoi) | Instant coding answers via the command line | ```howdoi``` |
| [html2text](https://github.com/Alir3z4/html2text/) | Convert HTML to Markdown-formatted text | ```html2text``` |
| [magic-wormhole](https://github.com/magic-wormhole/magic-wormhole) | Tool to get things from one computer to another, safely | ```wormhole``` |
| [plan](https://github.com/fengsp/plan) | Crontab file manager | ```plan-quickstart``` |
| [pyclean](https://github.com/bittner/pyclean) | Pure Python cross-platform pycache cleaner | ```pyclean``` |
| [prefect](https://www.prefect.io/) | Workflow management system | ```prefect``` |
| [ranger](https://github.com/ranger/ranger) | Console file manager with VI key bindings | ```ranger``` |
| [rq](https://python-rq.org/) | Simple job queues for Python | ```rq```, ```rqinfo```, ```rqworker``` |
| [thefuck](https://github.com/nvbn/thefuck) | Magnificent application that corrects your previous console command | ```thefuck```, ```fuck``` |
| [typer](https://typer.tiangolo.com/) | Build CLI applications | ```typer``` |
| [unp](https://github.com/mitsuhiko/unp) | Command line tool that can unpack archives | ```unp``` |
| [speedtest-cli](https://github.com/sivel/speedtest-cli) | Command line interface for testing internet bandwidth using speedtest.net | ```speedtest```, ```speedtest-cli``` |
| [streamlink](https://github.com/streamlink/streamlink) | CLI utility that pipes video streams from various services into a video player | ```streamlink``` |
| [visidata](https://github.com/saulpw/visidata) | Interactive multitool for exploring, analyzing, and converting datasets in the terminal | ```vd```, ```visidata``` |
| [youtube-dl](https://youtube-dl.org/) | Download videos from YouTube and other video sites | ```youtube-dl``` |



## Web Frameworks & Tools

| Name | Description | Executable(s) |
|:-----|:------------|:--------------|
| [django](https://www.djangoproject.com/) | High-level Python web framework | ```django-admin``` |
| [fastapi[standard]](https://fastapi.tiangolo.com/) | Modern, fast web framework for building APIs | ```fastapi``` |
| [flask](https://flask.palletsprojects.com/) | Lightweight WSGI web application framework | ```flask``` |
| [httpie](https://httpie.io/) | User-friendly command-line HTTP client | ```http```, ```httpie```, ```https``` |
| [mitmproxy](https://github.com/mitmproxy/mitmproxy) | Free and open source interactive HTTPS proxy for penetration testers and software developers | ```mitmproxy```, ```mitmdump```, ```mitmweb``` |
| [uvicorn](https://www.uvicorn.org/) | Lightning-fast ASGI server | ```uvicorn``` |
| [websockets](https://github.com/aaugustin/websockets) | Library for building WebSocket servers and clients | ```websockets``` |



## Development Tools

| Name | Description | Executable(s) |
|:-----|:------------|:--------------|
| [black](https://github.com/psf/black) | The uncompromising Python code formatter | ```black``` |
| [invoke](https://github.com/pyinvoke/invoke) | Tool for managing shell-oriented subprocesses and organizing executable Python code into CLI-invokable tasks | ```invoke```, ```inv``` |
| [ipython](https://ipython.org/) | Enhanced interactive Python shell | ```ipython```, ```ipython3``` |
| [jupyter-core](https://jupyter.org/) | Core functionality for Jupyter projects | ```jupyter```, ```jupyter-migrate```, ```jupyter-troubleshoot``` |
| [poetry](https://python-poetry.org/) | Python packaging and dependency management | ```poetry``` |
| [pre-commit](https://github.com/pre-commit/pre-commit) | Framework for managing and maintaining multi-language git hooks | ```pre-commit``` |
| [py2app](https://py2app.readthedocs.io/) | Create standalone Mac OS X applications | ```py2applet``` |
| [pyarmor](https://pyarmor.dashingsoft.com/) | Tool for obfuscating Python scripts | ```pyarmor```, ```pyarmor-7```, ```pyarmor-8```, ```pyarmor-auth``` |
| [pyinstaller](https://www.pyinstaller.org/) | Convert Python programs into stand-alone executables | ```pyi-archive_viewer```, ```pyi-bindepend```, ```pyi-grab_version```, ```pyi-makespec```, ```pyi-set_version```, ```pyinstaller``` |
| [pyright](https://github.com/microsoft/pyright) | Static type checker for Python | ```pyright```, ```pyright-langserver```, ```pyright-python```, ```pyright-python-langserver``` |
| [pudb](https://github.com/inducer/pudb) | Full-screen, console-based visual debugger for Python | ```pudb``` |
| [ruff](https://github.com/astral-sh/ruff) | An extremely fast Python linter | ```ruff``` |
| [shiv](https://github.com/linkedin/shiv) | Build fully self-contained Python zipapps | ```shiv```, ```shiv-info``` |
| [uv](https://github.com/astral-sh/uv) | Extremely fast Python package installer and resolver, written in Rust | ```uv``` |



## System & Infrastructure

| Name | Description | Executable(s) |
|:-----|:------------|:--------------|
| [ansible](https://www.ansible.com/) | Automation tool for IT infrastructure | ```ansible-community``` |
| [aws-cli](https://aws.amazon.com/cli/) | Official command-line interface for Amazon Web Services | ```aws``` |
| [bpytop](https://github.com/aristocratos/bpytop) | Resource monitor that shows usage and stats for processor, memory, disks, network, and processes | ```bpytop``` |
| [conda](https://github.com/conda/conda) | OS-agnostic, system-level binary package and environment manager | ```conda``` |
| [dockly](https://github.com/lirantal/dockly) | Immersive terminal interface for managing Docker containers and services | ```dockly``` |
| [glances](https://github.com/nicolargo/glances) | Cross-platform monitoring tool with curses or Web based interface | ```glances``` |
| [k9s](https://github.com/derailed/k9s) | Terminal-based UI to manage Kubernetes clusters | ```k9s``` |
| [mamba](https://github.com/mamba-org/mamba) | Fast, cross-platform package manager | ```mamba``` |
| [pipx](https://pypa.github.io/pipx/) | Install and run Python applications in isolated environments | ```pipx``` |
| [platformio](https://github.com/platformio/platformio-core) | Open source ecosystem for IoT development with cross-platform IDE and unified debugger | ```platformio```, ```pio``` |
| [spack](https://github.com/spack/spack) | Language-independent package manager for supercomputers, Mac, and Linux | ```spack``` |
| [xonsh](https://xon.sh/) | Python-powered shell | ```xonsh```, ```xonsh-cat```, ```xonsh-uname```, ```xonsh-uptime``` |



## Documentation

| Name | Description | Executable(s) |
|:-----|:------------|:--------------|
| [markdown](https://python-markdown.github.io/) | Python implementation of Markdown | ```markdown_py``` |
| [pdoc](https://pdoc.dev/) | Auto-generate API documentation for Python projects | ```pdoc``` |



## Database Tools

| Name | Description | Executable(s) |
|:-----|:------------|:--------------|
| [fake2db](https://github.com/emirozer/fake2db) | Fake2db is a fake database generator for testing purposes. | ```fake2db``` |
| [harlequin](https://github.com/tconbeer/harlequin) | The SQL IDE for your terminal. A TUI for DuckDB, SQLite, Postgres, and more | ```harlequin``` |
| [iredis](https://github.com/laixintao/iredis) | Iredis is a Redis terminal client with auto-completion and syntax highlighting. | ```iredis``` |
| [litecli](https://litecli.com/) | Litecli is a command line interface for SQLite with auto-completion and syntax highlighting. | ```litecli``` |
| [mycli](https://www.mycli.net/) | Mycli is a command line interface for MySQL with auto-completion and syntax highlighting. | ```mycli``` |
| [peewee](http://docs.peewee-orm.com/) | Peewee is a small, expressive ORM for Python. | ```pwiz.py``` |
| [pgcli](https://www.pgcli.com/) | Pgcli is a command line interface for PostgreSQL with auto-completion and syntax highlighting. | ```pgcli``` |
| [sqlparse](https://github.com/andialbrecht/sqlparse) | Sqlparse is a non-validating SQL parser for Python. | ```sqlformat``` |
| [sqlite-utils](https://github.com/simonw/sqlite-utils) | Python CLI utility and library for manipulating SQLite databases | ```sqlite-utils``` |




## Contributing

Feel free to contribute by opening a pull request with your favorite Python CLI tools that can be
installed via UVX or PIPX!
Please make sure to follow the <a href="CONTRIBUTING.md">contribution guidelines</a> and adhere to the <a href="CODE_OF_CONDUCT.md">code of conduct</a>.
Please also check the <a href="https://github.com/carlosferreyra/awesome-uvx/issues">issues</a> for any open issues or discussions related to the project.

## License

This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.