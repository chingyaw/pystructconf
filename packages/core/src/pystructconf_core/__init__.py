__version__ = "0.0.1"  # Package version

from .parser import parse_file


def ping() -> str:
    return "pyStructConf Core is alive"


__all__ = ["__version__", "ping", "parse_file"]
