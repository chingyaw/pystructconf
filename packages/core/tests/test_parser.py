# Minimal parser test for M0 baseline
import json
from pathlib import Path
from pystructconf_core import parse_file


def test_minimal_case():
    base = Path(__file__).parent / "data"
    input_path = base / "input.txt"
    config_path = base / "config.yaml"
    expected_path = base / "expected.json"

    result = parse_file(str(input_path), str(config_path))
    expected = json.loads(expected_path.read_text(encoding="utf-8"))

    assert result == expected
