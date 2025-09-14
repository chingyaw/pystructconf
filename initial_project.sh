touch README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md SECURITY.md LICENSE .editorconfig .gitignore
touch docs/getting-started.md docs/roadmap.md docs/adr/0001-monorepo-vs-polyrepo.md docs/adr/0002-tooling-uv-hatch.md docs/adr/0003-licensing.md
touch pyproject.toml
touch .github/PULL_REQUEST_TEMPLATE.md .github/ISSUE_TEMPLATE/bug_report.md .github/ISSUE_TEMPLATE/feature_request.md .github/workflows/ci.yml
touch packages/core/pyproject.toml packages/rule-engine/pyproject.toml packages/cli/pyproject.toml packages/integrations-fastapi/pyproject.toml
mkdir -p packages/core/src/pystructconf_core packages/rule-engine/src/pystructconf_rule_engine packages/cli/src/pystructconf_cli packages/integrations-fastapi/src/pystructconf_integrations_fastapi

