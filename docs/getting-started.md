# Getting Started

## Install (development)
```bash
uv pip install -e packages/core
uv pip install -e packages/cli
```

## Minimal Input & Config
**input.txt**
```
name: Alice
age: 30
```

**config.yaml**
```yaml
parse_rules:
  fields:
    name: { source_key: "name", type: "str" }
    age:  { source_key: "age",  type: "int" }

ignore:
  empty_lines: true
  comment_prefix: "#"
```

## Run via Python
```python
from pystructconf_core import parse_file, parse_with_report

data = parse_file("packages/core/tests/data/demo_happy/input.txt",
                  "packages/core/tests/data/demo_happy/config.yaml")
print(data)

report = parse_with_report("packages/core/tests/data/demo_happy/input.txt",
                           "packages/core/tests/data/demo_happy/config.yaml")
print(report["data"], report["errors"])

```

## Run via CLI
```bash
pystructconf -i packages/core/tests/data/demo_happy/input.txt \
             -c packages/core/tests/data/demo_happy/config.yaml

pystructconf -i packages/core/tests/data/demo_happy/input.txt \
             -c packages/core/tests/data/demo_happy/config.yaml \
             --report --fail-on-errors

```

For full reports and CI-friendly failures:
```bash
pystructconf -i input.txt -c config.yaml --report --fail-on-errors
```
