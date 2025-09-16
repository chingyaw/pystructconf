# Roadmap

## M0 – Project Bootstrap
- UV workspace set up
- Core package with `src/` layout
- Smoke test (`ping()`) and a minimal parser test
- CI runs pytest

**Status:** Complete ✅

## M1 – Minimal Rule-Based Parser
**Scope**
- Parse key:value text into typed JSON
- Field options: `source_key`, `type`, `required`, `default`, `transforms`, `map`
- Global `defaults` block
- Report mode (`{"data": ..., "errors": [...]}`)
- CLI flags: `--report`, `--fail-on-errors`

**Acceptance**
- Tests for required/defaults, transforms/map, booleans, and E2E (happy/error)
- CLI exits with code `1` when `--fail-on-errors` and errors exist

**Out-of-scope**
- Nested structures, arrays, advanced date parsing, and rule engine severity (planned for M2+)

## Next (M2+)
- Nested mapping (sections, groups, arrays)
- Rule engine (severity, aggregation)
- Integrations (FastAPI, etc.)
