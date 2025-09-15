# Tests for pystructconf_core
import pystructconf_core as core


def test_ping_core():
    assert core.ping() == "pyStructConf Core is alive"
