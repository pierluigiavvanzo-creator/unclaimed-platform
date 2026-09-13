from __future__ import annotations

import hashlib
import json
from pathlib import Path

from fastapi.testclient import TestClient
from jsonschema import Draft202012Validator, FormatChecker

from unclaimed_platform.api.app import app

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schemas" / "common" / "reviewer_operations_summary.schema.json"
SYNTHETIC_RAW = b"synthetic_id,holder_state,amount\nSYN-001,CA,123.45\n"


def test_reviewer_operations_summary_matches_versioned_contract() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    response = TestClient(app).get("/api/v1/reviewer/operations-summary")

    assert response.status_code == 200
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(response.json())


def test_reviewer_summary_is_read_only_synthetic_and_fail_closed() -> None:
    client = TestClient(app)
    response = client.get("/api/v1/reviewer/operations-summary")
    payload = response.json()

    assert payload["contract_version"] == "1.0.0"
    assert payload["data_mode"] == "GOVERNED_SYNTHETIC_PREVIEW"
    assert payload["read_only"] is True
    assert payload["source_registry"]["approved_real_sources"] == 0
    assert payload["source_registry"]["real_source_activation"] == "BLOCKED"
    assert "REAL_ACQUISITION" in payload["blocked_capabilities"]
    assert "BENEFICIARY_MATCHING" in payload["blocked_capabilities"]
    assert payload["raw_artifact"]["synthetic"] is True
    assert payload["governance"]["unnecessary_pii"] == "ABSENT"
    assert client.post("/api/v1/reviewer/operations-summary").status_code == 405


def test_synthetic_raw_preview_hash_and_byte_count_are_deterministic() -> None:
    payload = TestClient(app).get("/api/v1/reviewer/operations-summary").json()

    assert payload["raw_artifact"]["byte_count"] == len(SYNTHETIC_RAW)
    assert payload["raw_artifact"]["content_hash"] == hashlib.sha256(SYNTHETIC_RAW).hexdigest()
