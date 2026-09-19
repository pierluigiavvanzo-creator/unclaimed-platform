from __future__ import annotations

import json
from pathlib import Path

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


def test_fourth_attempt_approvals_are_valid_granted_and_not_consumed() -> None:
    local = _load(LOCAL_APPROVAL)
    pii = _load(PII_APPROVAL)

    Draft202012Validator(_load(LOCAL_SCHEMA)).validate(local)
    Draft202012Validator(_load(PII_SCHEMA)).validate(pii)

    for approval in (local, pii):
        assert approval["status"] == "GRANTED_NOT_CONSUMED"
        assert approval["granted_on"] == "2026-09-19"
        assert approval["attempt_number"] == 4
        assert approval["single_use"] is True
        assert approval["reusable"] is False
        assert approval["retry_authorized"] is False
        assert approval["runner_checkpoint"] == (
            "1c4be944004c85936d53506a5998b9aeffc9aed0"
        )
        assert approval["runner_ci_run_id"] == 35428062292
        assert approval["runner_ci_conclusion"] == "SUCCESS"

    assert local["owner_authorization"] == (
        "APPROVO NY OSC FOURTH TRANSIENT LOCAL FILE BOUNDED ONCE"
    )
    assert pii["owner_authorization"] == (
        "APPROVO NY OSC OWNER NAME FILE FOURTH BOUNDED TRANSIENT PII ATTEMPT ONCE"
    )
    assert local["execution_approval_ref"] != pii["execution_approval_ref"]

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


def test_granted_fourth_attempt_builds_bound_authorization() -> None:
    authorization = build_real_execution_authorization(
        LOCAL_APPROVAL,
        PII_APPROVAL,
        expected_attempt_number=4,
    )

    assert authorization.mode == "AUTHORIZED_REAL_ONCE"
    assert authorization.attempt_number == 4
    assert authorization.local_file_approval_ref.endswith("1C4BE944")
    assert authorization.gate2_approval_ref.endswith("35428062")
    assert authorization.max_download_bytes == 450_000_000
    assert authorization.max_uncompressed_bytes == 2_000_000_000
    assert authorization.max_archive_members == 1
    assert authorization.delete_local_file_immediately is True


def test_consumed_third_attempt_artifacts_are_not_referenced() -> None:
    local = _load(LOCAL_APPROVAL)
    pii = _load(PII_APPROVAL)
    for approval in (local, pii):
        assert "third_attempt" not in approval["proposal_ref"]
        assert approval["proposal_checkpoint"] == (
            "bec3e23325f9d565428e1f7cdeac401010884827"
        )
        assert approval["proposal_ci_run_id"] == 35426399366
