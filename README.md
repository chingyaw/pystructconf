# pyStructConf

[![CI](https://github.com/chingyaw/pystructconf/actions/workflows/ci.yml/badge.svg)](https://github.com/chingyaw/pystructconf/actions/workflows/ci.yml)

Flexible text-to-structured-data toolkit with an optional rule engine. Designed to be embedded in FastAPI backends while remaining usable from the CLI.

> Status: **M0 bootstrap is done** (repo, workspace, CI, tests). Public APIs & implementations will land across M1.

---

## Table of Contents

- [Goals](#goals)
- [Packages (Monorepo)](#packages-monorepo)
- [Supported Python Versions](#supported-python-versions)
- [macOS (Apple Silicon) Notes](#macos-apple-silicon-notes)
- [Installation](#installation)
  - [Using `uv` (recommended)](#using-uv-recommended)
  - [Using `pip`](#using-pip)
- [Quickstart](#quickstart)
  - [Core (contracts)](#core-contracts)
  - [CLI (skeleton)](#cli-skeleton)
  - [FastAPI Integration (skeleton)](#fastapi-integration-skeleton)
- [Quick Usage Examples](#quick-usage-examples)
- [Development](#development)
  - [Repo Setup](#repo-setup)
  - [Running Tests](#running-tests)
  - [Coding Style & Tooling](#coding-style--tooling)
  - [Commit Convention](#commit-convention)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Security](#security)
- [License](#license)

---

## Goals

- **Embed first**: clean, typed, and stable contracts for embedding in **FastAPI** services.
- **CLI friendly**: provide a thin CLI for quick local conversions and demos.
- **Rule engine optionality**: parsing/structuring is core; rule evaluation is opt-in.
- **Pluggable**: parsers and targets as plugins to keep the core lean.
- **Simple maintenance**: minimal moving parts after initial features are in place.

---

## Packages (Monorepo)

```
pystructconf/
├─ packages/
│  ├─ core/                      # Core abstractions and data models
│  ├─ rule-engine/               # Optional rule evaluation (depends on core)
│  ├─ cli/                       # CLI that talks to exposed interfaces
│  └─ integrations-fastapi/      # Optional FastAPI integration
├─ docs/
│  └─ adr/                       # Architecture Decision Records
└─ .github/workflows/ci.yml      # Tests on Python 3.10–3.13
```

**Dependency direction**:

```
core  ←  rule-engine (optional)
core  ←  cli
core  ←  integrations-fastapi (optionally + rule-engine)
```

---

## Supported Python Versions

`>= 3.10, < 3.14`

This applies to all packages in the workspace. The CI matrix runs 3.10–3.13 on `ubuntu-latest`.

---

## macOS (Apple Silicon) Notes

These tips are specific to Apple Silicon (M1/M2/M3/M4) Macs.

### Prerequisites
- **Command Line Tools** (for building fallback wheels):
  ```bash
  xcode-select --install
  ```
- **uv installation** (recommended):
  - Homebrew: `brew install uv` (binary will be at `/opt/homebrew/bin/uv`)
  - Or script:
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # If installed under ~/.local/bin, add it to PATH (zsh):
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc
    ```

### Python interpreters
The project supports `>= 3.10, < 3.14`. You can install multiple interpreters with uv:
```bash
uv python install 3.10 3.11 3.12 3.13
# Create a 3.13 virtualenv for day-to-day dev:
uv venv -p 3.13
```

### Create and use a virtualenv
```bash
# Inside the repo root
uv venv -p 3.13

# Install workspace packages (editable)
uv pip install -e ./packages/core
uv pip install -e ./packages/rule-engine
uv pip install -e ./packages/cli
uv pip install -e ./packages/integrations-fastapi

# Test tools
uv pip install pytest
```

### Architecture sanity checks
- Ensure your shell is **not** running under Rosetta (x86_64), or you may get wheel/arch mismatches:
  ```bash
  uname -m         # should print: arm64
  python -c "import platform; print(platform.machine())"  # should print: arm64
  ```

### PyCharm tips (macOS)
- **Interpreter**: point to `.venv/bin/python` you created above.
- **Sources Root**: mark each `packages/*/src` folder as *Sources Root* so imports like `pystructconf_core` resolve.
- **Run/Debug**: set default test runner to `pytest` (Preferences → Python Integrated Tools).

### Git hygiene on macOS
- `.DS_Store` is ignored in repository `.gitignore`. You can also globally ignore it:
  ```bash
  git config --global core.excludesfile ~/.gitignore_global
  echo ".DS_Store" >> ~/.gitignore_global
  ```

---

## Installation

> For contributors: install from the monorepo workspace in editable mode.

### Using `uv` (recommended)

```bash
# Create a virtual environment and activate commands via uv
uv venv

# Install packages in editable mode
uv pip install -e ./packages/core
uv pip install -e ./packages/rule-engine
uv pip install -e ./packages/cli
uv pip install -e ./packages/integrations-fastapi

# (Optional) test tools
uv pip install pytest
```

### Using `pip`

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

python -m pip install -e ./packages/core
python -m pip install -e ./packages/rule-engine
python -m pip install -e ./packages/cli
python -m pip install -e ./packages/integrations-fastapi

python -m pip install pytest
```

---

## Quickstart

> **Note:** At M0 we only expose minimal “ping” functions so imports work and CI passes. Public interfaces & implementations arrive in M1.

### Core (contracts)

```python
import pystructconf_core as core

print(core.ping())  # "pyStructConf Core is alive"
```

### CLI (skeleton)

The CLI entry point is reserved at `pystructconf` (see `packages/cli/pyproject.toml`).
**Coming in M1**: `pystructconf --version`, `pystructconf ping`, and the first parse command.

```bash
# Placeholder (will work after M1 CLI skeleton lands)
# pystructconf --version
```

### FastAPI Integration (skeleton)

**Coming in M1**: a minimal router (e.g., `/healthz`, `/parse`) that imports contracts from `core` and optionally hooks the rule engine.

```python
# app.py (planned)
# from fastapi import FastAPI
# from pystructconf_integrations_fastapi import router
#
# app = FastAPI()
# app.include_router(router, prefix="/v1/structconf")
```

---

## Quick Usage Examples

These examples work out of the box using the provided `demo_happy` test data.

### Python API

```python
from pystructconf_core import parse_file, parse_with_report

data = parse_file("packages/core/tests/data/demo_happy/input.txt",
                  "packages/core/tests/data/demo_happy/config.yaml")
print(data)

report = parse_with_report("packages/core/tests/data/demo_happy/input.txt",
                           "packages/core/tests/data/demo_happy/config.yaml")
print(report["data"], report["errors"])
```

### CLI
```bash
# print only parsed data
pystructconf -i packages/core/tests/data/demo_happy/input.txt \
             -c packages/core/tests/data/demo_happy/config.yaml

# print full report and fail when errors exist
pystructconf -i packages/core/tests/data/demo_happy/input.txt \
             -c packages/core/tests/data/demo_happy/config.yaml \
             --report --fail-on-errors
```

---

## Development

### Repo Setup

```bash
# Clone
git clone https://github.com/chingyaw/pystructconf.git
cd pystructconf

# Optional but fast: uv
uv venv
uv pip install -e ./packages/core ./packages/rule-engine ./packages/cli ./packages/integrations-fastapi
uv pip install pytest
```

### Running Tests

```bash
pytest -q
```

> CI runs the same tests on 3.10–3.13 via GitHub Actions.

### Coding Style & Tooling

- Comments: **English only**.
- Format/lint/type-check: **Black / Ruff / mypy** (tooling targets are aligned to `py310`).
- We’ll add CI checks for these tools once the first public interfaces land.

### Commit Convention

Use **Conventional Commits**:

- `feat(core): …` – new feature
- `fix(cli): …` – bug fix
- `docs: …` – documentation
- `test: …` – tests
- `chore: …` – non-code / infra / config
- `build(ci): …` – build system or CI changes
- `refactor: …` – internal code changes without behavior change

---

## Roadmap

- **M0 (DONE)**
  - Public repo, workspace, CI (3.10–3.13), minimal tests and package skeletons.

- **M1 (IN PROGRESS)**
  - **Core contracts**: base data models, interfaces for parsers/writers (types only).
  - **CLI skeleton**: `--version`, `ping`, initial parse command scaffold.
  - **FastAPI skeleton**: `/healthz`, `/parse` stub, optional rule-engine wiring.
  - Smoke tests for the above.

- **M2**
  - First concrete parser(s) & target(s) as plugins.
  - Rule engine MVP (opt-in extra).
  - Docs: getting started, examples, ADR updates.

---

## Contributing

Contributions are welcome, but note that the initial focus is internal FastAPI usage.
Please open an issue first to discuss scope. See **CONTRIBUTING.md** for details.

---

## Security

If you discover a security issue, please follow the process in **SECURITY.md**.
Do not open public issues for sensitive reports.

---

## License

Licensed under the **MIT License**.
See [`LICENSE`](./LICENSE) for details.
