from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution import (
    build_real_execution_authorization,
)

ROOT = Path(__file__).resolve().parents[2]

LOCAL_SCHEMA = (
    ROOT
    / "schemas/common/ny_osc_second_attempt_transient_local_approval.schema.json"
)
LOCAL_APPROVAL = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_second_attempt_transient_local_approval.v1.json"
)
PII_SCHEMA = (
    ROOT
    / "schemas/common/ny_osc_second_attempt_transient_pii_approval.schema.json"
)
PII_APPROVAL = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_second_attempt_transient_pii_approval.v1.json"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_second_attempt_approvals_are_single_use_and_bounded() -> None:
    local_schema = _load(LOCAL_SCHEMA)
    local = _load(LOCAL_APPROVAL)
    pii_schema = _load(PII_SCHEMA)
    pii = _load(PII_APPROVAL)

    Draft202012Validator(local_schema).validate(local)
    Draft202012Validator(pii_schema).validate(pii)

    assert local["status"] == "CONSUMED_SINGLE_USE_NON_REUSABLE"
    assert local["consumed_on"] == "2026-09-18"
    assert local["execution_result_ref"].endswith(
        "ny_osc_owner_name_file_second_attempt_execution_result.v1.json"
    )
    assert local["single_use"] is True
    assert local["reusable"] is False
    assert local["retry_authorized"] is False

    assert pii["status"] == "CONSUMED_SINGLE_USE_NON_REUSABLE"
    assert pii["consumed_on"] == "2026-09-18"
    assert pii["execution_result_ref"] == local["execution_result_ref"]
    assert pii["single_use"] is True
    assert pii["reusable"] is False
    assert pii["retry_authorized"] is False
    assert pii["execution_bounds"]["downloads_max"] == 1
    assert pii["execution_bounds"]["retries_max"] == 0
    assert pii["execution_bounds"]["max_download_bytes"] == 450_000_000
    assert pii["authorization_does_not_grant"]["beneficiary_matching"] is False
    assert pii["authorization_does_not_grant"]["outreach"] is False


def test_consumed_second_attempt_approvals_cannot_build_runtime_authorization() -> None:
    with pytest.raises(ValueError, match="approval is not available"):
        build_real_execution_authorization(LOCAL_APPROVAL, PII_APPROVAL)
