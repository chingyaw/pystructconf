__version__ = "0.0.1"  # Package version

from .parser import parse_file, parse_with_report


def ping() -> str:
    return "pyStructConf Core is alive"


__all__ = ["__version__", "ping", "parse_file", "parse_with_report"]
