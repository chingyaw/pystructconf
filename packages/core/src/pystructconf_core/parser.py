from pathlib import Path
import yaml


def _cast_value(value: str, type_name: str):
    """
    Minimal type casting used by the MVP parser.
    Extend when you add more types (e.g., datetime normalization).
    """
    t = (type_name or "str").lower()
    if t == "int":
        return int(value)
    if t == "float":
        return float(value)
    if t == "bool":
        return value.lower() in ("true", "1", "yes", "y")
    if t == "date":
        # Keep raw string for M1; normalize later if needed.
        return value
    return value  # default: str


def parse_file(input_path: str, config_path: str) -> dict:
    """
    Parse a key:value text file based on rules defined in a YAML config.
    This is the MVP for M1 and intentionally simple.
    """
    cfg_text = Path(config_path).read_text(encoding="utf-8")
    cfg = yaml.safe_load(cfg_text) or {}

    rules = (cfg.get("parse_rules") or {}).get("fields") or {}
    ignore = cfg.get("ignore") or {}
    comment_prefix = ignore.get("comment_prefix", "#")
    ignore_empty = bool(ignore.get("empty_lines", True))

    lines = Path(input_path).read_text(encoding="utf-8").splitlines()

    # Step 1: collect raw key:value pairs (strings)
    raw = {}
    for line in lines:
        s = line.strip()
        if not s and ignore_empty:
            continue
        if comment_prefix and s.startswith(comment_prefix):
            continue
        if ":" not in s:
            continue
        key, val = s.split(":", 1)
        raw[key.strip()] = val.strip()

    # Step 2: map to output and perform type casting
    out = {}
    for out_key, spec in rules.items():
        src = spec.get("source_key", out_key)
        typ = spec.get("type", "str")
        if src in raw:
            out[out_key] = _cast_value(raw[src], typ)

    return out
