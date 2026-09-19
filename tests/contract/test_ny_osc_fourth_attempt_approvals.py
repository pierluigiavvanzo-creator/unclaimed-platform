from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution import (
    build_real_execution_authorization,
)

ROOT = Path(__file__).resolve().parents[2]
LOCAL_SCHEMA = ROOT / "schemas/common/ny_osc_fourth_attempt_transient_local_approval.schema.json"
LOCAL_APPROVAL = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_fourth_attempt_transient_local_approval.v1.json"
)
PII_SCHEMA = ROOT / "schemas/common/ny_osc_fourth_attempt_transient_pii_approval.schema.json"
PII_APPROVAL = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_fourth_attempt_transient_pii_approval.v1.json"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_fourth_attempt_templates_are_valid_and_not_granted() -> None:
    local = _load(LOCAL_APPROVAL)
    pii = _load(PII_APPROVAL)

    Draft202012Validator(_load(LOCAL_SCHEMA)).validate(local)
    Draft202012Validator(_load(PII_SCHEMA)).validate(pii)

    for approval in (local, pii):
        assert approval["status"] == "NOT_GRANTED"
        assert approval["owner_authorization"] is None
        assert approval["granted_on"] is None
        assert approval["execution_approval_ref"] is None
        assert approval["attempt_number"] == 4
        assert approval["single_use"] is True
        assert approval["reusable"] is False
        assert approval["retry_authorized"] is False
        assert approval["runner_checkpoint"] is None
        assert approval["runner_ci_run_id"] is None
        assert approval["runner_ci_conclusion"] is None

    bounds = pii["execution_bounds"]
    assert bounds["downloads_max"] == 1
    assert bounds["retries_max"] == 0
    assert bounds["max_download_bytes"] == 450_000_000
    assert bounds["max_uncompressed_bytes"] == 2_000_000_000
    assert bounds["max_archive_members"] == 1
    assert bounds["expected_documented_field_count"] == 14
    assert bounds["parser_chunk_bytes"] == 65_536
    assert bounds["automatic_widening_allowed"] is False
    assert bounds["automatic_retry_allowed"] is False

    processing = pii["processing_scope"]
    assert processing["owner_rows_persistence_allowed"] is False
    assert processing["owner_field_decoding_allowed"] is False
    assert processing["owner_field_buffering_allowed"] is False
    assert processing["owner_field_logging_allowed"] is False
    assert processing["row_specific_human_inspection_allowed"] is False


def test_not_granted_fourth_attempt_cannot_build_authorization() -> None:
    with pytest.raises(ValueError, match="approval is not available"):
        build_real_execution_authorization(
            LOCAL_APPROVAL,
            PII_APPROVAL,
            expected_attempt_number=4,
        )


def test_consumed_third_attempt_artifacts_are_not_referenced() -> None:
    local = _load(LOCAL_APPROVAL)
    pii = _load(PII_APPROVAL)
    for approval in (local, pii):
        assert "third_attempt" not in approval["proposal_ref"]
        assert approval["proposal_checkpoint"] == "bec3e23325f9d565428e1f7cdeac401010884827"
        assert approval["proposal_ci_run_id"] == 35426399366
