# Tests for pystructconf_rule_engine
import pystructconf_rule_engine as rule


def test_ping_rule_engine():
    assert rule.ping() == "pyStructConf Rule Engine is alive"
