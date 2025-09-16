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
from pystructconf_core import parse_file
print(parse_file("input.txt", "config.yaml"))
```

## Run via CLI
```bash
pystructconf -i input.txt -c config.yaml
```

For full reports and CI-friendly failures:
```bash
pystructconf -i input.txt -c config.yaml --report --fail-on-errors
```
