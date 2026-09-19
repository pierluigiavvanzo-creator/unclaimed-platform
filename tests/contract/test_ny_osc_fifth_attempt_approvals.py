from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution import (
    build_real_execution_authorization,
)

ROOT = Path(__file__).resolve().parents[2]
LOCAL_SCHEMA = ROOT / "schemas/common/ny_osc_fifth_attempt_transient_local_approval.schema.json"
LOCAL_APPROVAL = (\n    ROOT\n    / "sources/evidence"\n    / "ny_osc_owner_name_file_fifth_attempt_transient_local_approval.v1.json"\n)
PII_SCHEMA = ROOT / "schemas/common/ny_osc_fifth_attempt_transient_pii_approval.schema.json"
PII_APPROVAL = (\n    ROOT\n    / "sources/evidence"\n    / "ny_osc_owner_name_file_fifth_attempt_transient_pii_approval.v1.json"\n)

PROPOSAL_REF = (\n    "sources/proposals/"\n    "ny_osc_owner_name_file_fifth_bounded_attempt_authorization.v1.json"\n)
PROPOSAL_CHECKPOINT = "8ce856ddbeac5d2300f808729a887803e212b240"
PROPOSAL_CI = 35460348569


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_fifth_attempt_templates_validate_and_remain_not_granted() -> None:
    local = _load(LOCAL_APPROVAL)
    pii = _load(PII_APPROVAL)

    Draft202012Validator(_load(LOCAL_SCHEMA)).validate(local)
    Draft202012Validator(_load(PII_SCHEMA)).validate(pii)

    for approval in (local, pii):
        assert approval["status"] == "NOT_GRANTED"
        assert approval["owner_authorization"] is None
        assert approval["granted_on"] is None
        assert approval["execution_approval_ref"] is None
        assert approval["attempt_number"] == 5
        assert approval["proposal_ref"] == PROPOSAL_REF
        assert approval["proposal_checkpoint"] == PROPOSAL_CHECKPOINT
        assert approval["proposal_ci_run_id"] == PROPOSAL_CI
        assert approval["runner_checkpoint"] is None
        assert approval["runner_ci_run_id"] is None
        assert approval["runner_ci_conclusion"] is None
        assert approval["single_use"] is True
        assert approval["reusable"] is False
        assert approval["retry_authorized"] is False

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


def test_not_granted_fifth_templates_cannot_build_authorization() -> None:
    with pytest.raises(ValueError, match="approval is not available"):
        build_real_execution_authorization(
            LOCAL_APPROVAL,
            PII_APPROVAL,
            expected_attempt_number=5,
        )


def test_runtime_bridge_accepts_attempt_five_only_after_new_distinct_grants(
    tmp_path: Path,
) -> None:
    local = copy.deepcopy(_load(LOCAL_APPROVAL))
    pii = copy.deepcopy(_load(PII_APPROVAL))

    local.update(
        status="GRANTED_NOT_CONSUMED",
        owner_authorization="APPROVO NY OSC FIFTH TRANSIENT LOCAL FILE BOUNDED ONCE",
        granted_on="2026-09-20",
        execution_approval_ref="synthetic-fifth-local-ref",
        runner_checkpoint="a" * 40,
        runner_ci_run_id=999999,
        runner_ci_conclusion="SUCCESS",
    )
    pii.update(
        status="GRANTED_NOT_CONSUMED",
        owner_authorization=(\n            "APPROVO NY OSC OWNER NAME FILE FIFTH BOUNDED TRANSIENT PII ATTEMPT ONCE"\n        ),
        granted_on="2026-09-20",
        execution_approval_ref="synthetic-fifth-pii-ref",
        runner_checkpoint="a" * 40,
        runner_ci_run_id=999999,
        runner_ci_conclusion="SUCCESS",
    )

    local_path = tmp_path / "local.json"
    pii_path = tmp_path / "pii.json"
    local_path.write_text(json.dumps(local), encoding="utf-8")
    pii_path.write_text(json.dumps(pii), encoding="utf-8")

    authorization = build_real_execution_authorization(
        local_path,
        pii_path,
        expected_attempt_number=5,
    )
    assert authorization.attempt_number == 5
    assert authorization.local_file_approval_ref == "synthetic-fifth-local-ref"
    assert authorization.gate2_approval_ref == "synthetic-fifth-pii-ref"
    assert authorization.max_download_bytes == 450_000_000
    assert authorization.max_uncompressed_bytes == 2_000_000_000
    assert authorization.max_archive_members == 1


def test_fourth_attempt_artifacts_are_not_referenced() -> None:
    for approval in (_load(LOCAL_APPROVAL), _load(PII_APPROVAL)):
        assert "fourth_attempt" not in approval["proposal_ref"]
        assert approval["attempt_number"] == 5
