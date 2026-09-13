from fastapi.testclient import TestClient

from unclaimed_platform.api.app import app


def test_reviewer_operations_summary_smoke() -> None:
    response = TestClient(app).get("/api/v1/reviewer/operations-summary")

    assert response.status_code == 200
    payload = response.json()
    assert payload["read_only"] is True
    assert payload["data_mode"] == "GOVERNED_SYNTHETIC_PREVIEW"
    assert payload["source_registry"]["approved_real_sources"] == 0
