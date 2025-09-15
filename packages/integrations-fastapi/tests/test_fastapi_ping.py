# Tests for pystructconf_integrations_fastapi
import pystructconf_integrations_fastapi as fa


def test_ping_fastapi_integration():
    assert fa.ping() == "pyStructConf FastAPI integration is alive"
