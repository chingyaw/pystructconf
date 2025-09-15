# Contributing to pyStructConf

Thanks for your interest in contributing! This project aims to provide a flexible, typed toolkit for converting free‑form text into structured data, with an optional rule engine. The initial focus is to embed the library in FastAPI backends while keeping a simple CLI for general use.

> TL;DR: Fork → create a feature branch → make changes with tests → ensure CI passes on Python 3.10–3.13 → open a PR.

---

## Table of Contents
- [Project scope](#project-scope)
- [Supported Python versions](#supported-python-versions)
- [Monorepo layout](#monorepo-layout)
- [Getting started](#getting-started)
- [Development workflow](#development-workflow)
- [Testing](#testing)
- [Style & tooling](#style--tooling)
- [Commit convention](#commit-convention)
- [Pull requests](#pull-requests)
- [Security](#security)
- [License](#license)

---

## Project scope

- **Core first**: stable, typed contracts and minimal runtime dependencies.
- **Optional rule engine**: lives outside the core and can be excluded.
- **FastAPI integration**: a thin integration layer built on top of the core.
- **CLI**: convenience wrapper around public interfaces.
- **Maintainability**: ship small, well‑tested increments.

If you propose features outside this scope, please open an issue for discussion before coding.

---

## Supported Python versions

The workspace supports **Python `>= 3.10, < 3.14`** across all packages.
The CI matrix covers 3.10–3.13 on `ubuntu-latest`.

---

## Monorepo layout

```
pystructconf/
├─ packages/
│  ├─ core/                      # Core abstractions and data models
│  ├─ rule-engine/               # Optional rule evaluation (depends on core)
│  ├─ cli/                       # CLI that talks to exposed interfaces
│  └─ integrations-fastapi/      # Optional FastAPI integration
└─ .github/workflows/ci.yml      # CI for 3.10–3.13
```

Dependency direction:

```
core  ←  rule-engine (optional)
core  ←  cli
core  ←  integrations-fastapi (optionally + rule-engine)
```

---

## Getting started

1. **Fork** this repository and **clone** your fork.
2. Create a virtual environment (Apple Silicon/macOS users: see README “macOS Notes”):
   ```bash
   # Using uv (recommended)
   uv venv -p 3.13
   source .venv/bin/activate  # uv sets this up for you
   ```
3. **Install workspace packages** in editable mode:
   ```bash
   uv pip install -e ./packages/core
   uv pip install -e ./packages/rule-engine
   uv pip install -e ./packages/cli
   uv pip install -e ./packages/integrations-fastapi
   ```
4. **Install test tools** and run tests:
   ```bash
   uv pip install pytest
   pytest -q
   ```

> Prefer `uv`? Great. If you use `pip`/`venv`, commands are the same but replace `uv pip` with `python -m pip`.

---

## Development workflow

- **Create a branch** off `main`:
  ```bash
  git switch -c feat/my-short-title  # or fix/..., chore/..., docs/...
  ```
- **Keep changes focused**: one logical change set per PR.
- **Tests required**: add or update tests under the affected package’s `tests/` folder.
- **English-only comments**: please keep all source comments in English.
- **Docs**: update README or add docs if behavior or APIs change.
- **Rebase or merge main** regularly to avoid large conflict sets.

---

## Testing

- Place tests under the respective package, e.g. `packages/core/tests/`.
- File naming: prefer unique names like `test_core_*.py`, `test_cli_*.py` to avoid module name clashes.
- Run all tests:
  ```bash
  pytest -q
  ```
- Run a subset:
  ```bash
  pytest -q packages/core/tests
  ```
- CI must be green on **all supported Python versions**.

---

## Style & tooling

- **Black** for formatting, **Ruff** for linting, **mypy** for type checking. Tool targets align to **`py310`**.
- We will enable these checks in CI as the public interfaces solidify. In the meantime, you can run them locally:
  ```bash
  uv pip install black ruff mypy
  ruff check .
  black --check .
  mypy .
  ```

---

## Commit convention

We use **Conventional Commits** for clear, machine‑readable history:

```
<type>(<scope>): <subject>

Types: feat | fix | docs | style | refactor | perf | test | build | ci | chore
```

Examples:
- `feat(core): add ParserConfig and ParseResult contracts`
- `fix(cli): handle empty input gracefully`
- `build(ci): run tests on Python 3.10–3.13`
- `chore: sync workspace files and README`

---

## Pull requests

- Open an issue first for non‑trivial changes.
- Keep PRs small and focused; include **tests** and **docs updates**.
- Ensure CI passes (tests must be green on 3.10–3.13).
- Use a descriptive title and reference related issues.

Branch protection is enabled on `main` (PRs are required).

---

## Security

Please do **not** create public issues for security reports.
See **SECURITY.md** for the responsible disclosure process.

---

## License

By contributing to this project, you agree that your contributions will be licensed under the **MIT License** of this repository.
