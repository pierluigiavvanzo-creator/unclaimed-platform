from fastapi.testclient import TestClient

import app as vercel_entrypoint


def test_vercel_entrypoint_exposes_authoritative_fastapi_app() -> None:
    client = TestClient(vercel_entrypoint.app)

    health_response = client.get("/health")
    assert health_response.status_code == 200
    assert health_response.json() == {
        "status": "ok",
        "service": "unclaimed-platform",
    }

    operations_response = client.get("/api/reviewer/m3/operations")
    assert operations_response.status_code == 200

    payload = operations_response.json()
    assert payload["contract_version"] == "1.0.0"
    assert payload["mode"] == "SYNTHETIC_READ_ONLY"
    assert payload["source_registry"] == {
        "approved_real_sources": 0,
        "real_acquisition": "BLOCKED",
        "beneficiary_matching": "BLOCKED",
    }
    assert payload["governance"]["pii_mode"] == "NO_REAL_PII"
