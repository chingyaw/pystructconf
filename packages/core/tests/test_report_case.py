import json
from pathlib import Path
from pystructconf_core import parse_with_report


def test_report_demo_happy():
    base = Path(__file__).parent / "data" / "demo_happy"
    report = parse_with_report(str(base / "input.txt"), str(base / "config.yaml"))
    expected = json.loads((base / "expected.json").read_text(encoding="utf-8"))
    assert report == expected
