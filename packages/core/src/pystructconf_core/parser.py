from pathlib import Path
import yaml
from typing import Dict, Any, List, Tuple


def _truthy(val: str) -> bool:
    """Basic truthy check, will be enhanced later."""
    return val.lower() in ("true", "1", "yes", "y")


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
        return _truthy(value)
    if t == "date":
        # Keep raw string for M1; normalize later if needed.
        return value
    return value  # default: str


def _load_config(config_path: str) -> Dict[str, Any]:
    cfg_text = Path(config_path).read_text(encoding="utf-8")
    return yaml.safe_load(cfg_text) or {}


def _read_raw_pairs(input_path: str, comment_prefix: str, ignore_empty: bool) -> Dict[str, str]:
    lines = Path(input_path).read_text(encoding="utf-8").splitlines()
    raw: Dict[str, str] = {}
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
    return raw


def _apply_defaults_and_required(
    rules_fields: Dict[str, Any],
    defaults: Dict[str, Any],
    raw: Dict[str, str],
) -> Tuple[Dict[str, Any], List[str]]:
    """
    Build output dict from raw using fields rules.
    Inject defaults and collect required errors.
    """
    out: Dict[str, Any] = {}
    errors: List[str] = []

    for out_key, spec in (rules_fields or {}).items():
        src = spec.get("source_key", out_key)
        typ = spec.get("type", "str")
        required = bool(spec.get("required", False))

        # prefer raw
        if src in raw and raw[src] != "":
            out[out_key] = _cast_value(raw[src], typ)
            continue

        # then defaults (either per-field default or global defaults map)
        if "default" in spec:
            out[out_key] = _cast_value(str(spec["default"]), typ)
        elif defaults and out_key in defaults:
            out[out_key] = _cast_value(str(defaults[out_key]), typ)
        else:
            # missing
            if required:
                errors.append(f"Missing required field: {out_key}")

    return out, errors


def parse_with_report(input_path: str, config_path: str) -> Dict[str, Any]:
    """
    Parse a key:value text file based on rules defined in a YAML config.
    Returns a report with 'data' and 'errors'.
    """
    cfg = _load_config(config_path)
    rules = (cfg.get("parse_rules") or {}).get("fields") or {}
    ignore = cfg.get("ignore") or {}
    comment_prefix = ignore.get("comment_prefix", "#")
    ignore_empty = bool(ignore.get("empty_lines", True))
    defaults = (cfg.get("defaults") or {})  # global defaults block

    raw = _read_raw_pairs(input_path, comment_prefix, ignore_empty)
    data, errors = _apply_defaults_and_required(rules, defaults, raw)

    return {"data": data, "errors": errors}


def parse_file(input_path: str, config_path: str) -> dict:
    """
    Backward-compatible entry used by existing tests.
    Returns only the parsed data (no errors list).
    """
    report = parse_with_report(input_path, config_path)
    return report["data"]
