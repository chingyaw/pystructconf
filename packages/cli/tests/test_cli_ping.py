# Tests for pystructconf_cli
import pystructconf_cli as cli


def test_ping_cli():
    assert cli.ping() == "pyStructConf CLI is alive"
