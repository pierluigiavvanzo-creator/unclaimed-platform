from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = (
    ROOT
    / "schemas"
    / "common"
    / "ny_osc_first_download_transient_pii_approval.schema.json"
)
APPROVAL = (
    ROOT
    / "sources"
    / "evidence"
    / "ny_osc_owner_name_file_first_download_transient_pii_approval.v1.json"
)


def test_gate2_approval_artifact_validates_and_is_single_use() -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    approval = json.loads(APPROVAL.read_text(encoding="utf-8"))

    Draft202012Validator(schema).validate(approval)

    assert approval["status"] in {
        "GRANTED_NOT_CONSUMED",
        "CONSUMED_SINGLE_USE_NON_REUSABLE",
    }
    assert approval["single_use"] is True
    assert approval["reusable"] is False
    assert approval["retry_authorized"] is False
    assert approval["execution_bounds"]["downloads_max"] == 1
    assert approval["execution_bounds"]["retries_max"] == 0
    assert approval["authorization_does_not_grant"]["beneficiary_matching"] is False
    assert approval["authorization_does_not_grant"]["outreach"] is False
    if approval["status"] == "CONSUMED_SINGLE_USE_NON_REUSABLE":
        assert approval["consumed_on"]
        assert approval["execution_result"] == "BLOCKED_FAIL_CLOSED"
        assert approval["execution_reason_code"]
