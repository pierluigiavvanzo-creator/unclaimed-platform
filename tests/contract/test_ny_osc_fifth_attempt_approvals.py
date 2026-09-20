from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution import (
    build_real_execution_authorization,
)

ROOT = Path(__file__).resolve().parents[2]
LOCAL_SCHEMA = (
    ROOT
    / "schemas/common"
    / "ny_osc_fifth_attempt_transient_local_approval.schema.json"
)
LOCAL_APPROVAL = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_fifth_attempt_transient_local_approval.v1.json"
)
PII_SCHEMA = (
    ROOT
    / "schemas/common"
    / "ny_osc_fifth_attempt_transient_pii_approval.schema.json"
)
PII_APPROVAL = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_fifth_attempt_transient_pii_approval.v1.json"
)

PROPOSAL_REF = (
    "sources/proposals/"
    "ny_osc_owner_name_file_fifth_bounded_attempt_authorization.v1.json"
)
PROPOSAL_CHECKPOINT = "8ce856ddbeac5d2300f808729a887803e212b240"
PROPOSAL_CI = 35460348569
RUNNER_CHECKPOINT = "4a8412911b3b9ae59525dee3a0565951e2722528"
RUNNER_CI = 35474594533
LOCAL_REF = (
    "OWNER_APPROVAL_2026-09-20_NY_OSC_FIFTH_TRANSIENT_LOCAL_FILE_"
    "BOUNDED_ONCE_4A841291"
)
PII_REF = (
    "OWNER_APPROVAL_2026-09-20_NY_OSC_FIFTH_BOUNDED_TRANSIENT_PII_"
    "ATTEMPT_ONCE_35474594"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_fifth_attempt_approvals_validate_and_are_granted_not_consumed() -> None:
    local = _load(LOCAL_APPROVAL)
    pii = _load(PII_APPROVAL)

    Draft202012Validator(_load(LOCAL_SCHEMA)).validate(local)
    Draft202012Validator(_load(PII_SCHEMA)).validate(pii)

    for approval in (local, pii):
        assert approval["status"] == "GRANTED_NOT_CONSUMED"
        assert approval["granted_on"] == "2026-09-20"
        assert approval["attempt_number"] == 5
        assert approval["proposal_ref"] == PROPOSAL_REF
        assert approval["proposal_checkpoint"] == PROPOSAL_CHECKPOINT
        assert approval["proposal_ci_run_id"] == PROPOSAL_CI
        assert approval["runner_checkpoint"] == RUNNER_CHECKPOINT
        assert approval["runner_ci_run_id"] == RUNNER_CI
        assert approval["runner_ci_conclusion"] == "SUCCESS"
        assert approval["single_use"] is True
        assert approval["reusable"] is False
        assert approval["retry_authorized"] is False

    assert local["owner_authorization"] == (
        "APPROVO NY OSC FIFTH TRANSIENT LOCAL FILE BOUNDED ONCE"
    )
    assert pii["owner_authorization"] == (
        "APPROVO NY OSC OWNER NAME FILE FIFTH BOUNDED TRANSIENT PII "
        "ATTEMPT ONCE"
    )
    assert local["execution_approval_ref"] == LOCAL_REF
    assert pii["execution_approval_ref"] == PII_REF
    assert LOCAL_REF != PII_REF

    bounds = pii["execution_bounds"]
    assert bounds["downloads_max"] == 1
    assert bounds["retries_max"] == 0
    assert bounds["max_download_bytes"] == 450_000_000
    assert bounds["max_uncompressed_bytes"] == 2_000_000_000
    assert bounds["max_archive_members"] == 1
    assert bounds["text_members_required_exactly"] == 1
    assert bounds["expected_delimiter"] == "|"
    assert bounds["expected_documented_field_count"] == 14
    assert bounds["parser_chunk_bytes"] == 65_536
    assert bounds["required_execution_result_contract_version"] == "1.1.0"
    assert bounds["required_structural_diagnostic_contract_version"] == "1.0.0"
    assert bounds["automatic_widening_allowed"] is False
    assert bounds["automatic_retry_allowed"] is False

    scope = pii["processing_scope"]
    assert scope["owner_rows_persistence_allowed"] is False
    assert scope["owner_field_decoding_allowed"] is False
    assert scope["owner_field_buffering_allowed"] is False
    assert scope["owner_field_logging_allowed"] is False
    assert scope["row_specific_human_inspection_allowed"] is False
    assert scope["structural_diagnostic_persistence_allowed"] is True


def test_granted_fifth_approvals_build_runtime_authorization() -> None:
    authorization = build_real_execution_authorization(
        LOCAL_APPROVAL,
        PII_APPROVAL,
        expected_attempt_number=5,
    )
    assert authorization.attempt_number == 5
    assert authorization.local_file_approval_ref == LOCAL_REF
    assert authorization.gate2_approval_ref == PII_REF
    assert authorization.local_file_approval_ref != authorization.gate2_approval_ref
    assert authorization.max_download_bytes == 450_000_000
    assert authorization.max_uncompressed_bytes == 2_000_000_000
    assert authorization.max_archive_members == 1


def test_fourth_attempt_artifacts_are_not_referenced() -> None:
    for approval in (_load(LOCAL_APPROVAL), _load(PII_APPROVAL)):
        assert "fourth_attempt" not in approval["proposal_ref"]
        assert approval["attempt_number"] == 5
