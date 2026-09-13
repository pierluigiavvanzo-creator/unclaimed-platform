from fastapi.testclient import TestClient

from unclaimed_platform.api.app import app


def test_reviewer_console_is_synthetic_and_fail_closed_for_real_work() -> None:
    payload = TestClient(app).get("/api/reviewer/m3/operations").json()

    assert payload["mode"] == "SYNTHETIC_READ_ONLY"
    assert payload["source_registry"]["approved_real_sources"] == 0
    assert payload["source_registry"]["real_acquisition"] == "BLOCKED"
    assert payload["source_registry"]["beneficiary_matching"] == "BLOCKED"
    assert payload["raw_artifact"]["synthetic"] is True
