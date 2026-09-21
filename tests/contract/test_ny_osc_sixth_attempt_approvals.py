from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError

from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution import (
    build_real_execution_authorization_v1_1,
)

ROOT = Path(__file__).resolve().parents[2]
LOCAL_SCHEMA = (
    ROOT / "schemas/common/ny_osc_sixth_attempt_transient_local_approval.schema.json"
)
PII_SCHEMA = (
    ROOT / "schemas/common/ny_osc_sixth_attempt_transient_pii_approval.schema.json"
)
LOCAL_APPROVAL = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_sixth_attempt_transient_local_approval.v1.json"
)
PII_APPROVAL = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_sixth_attempt_transient_pii_approval.v1.json"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _not_granted_pair() -> tuple[dict[str, object], dict[str, object]]:
    local = deepcopy(_load(LOCAL_APPROVAL))
    pii = deepcopy(_load(PII_APPROVAL))

    for approval in (local, pii):
        approval["status"] = "NOT_GRANTED"
        approval["owner_authorization"] = None
        approval["granted_on"] = None
        approval["execution_approval_ref"] = None
        approval["runner_checkpoint"] = None
        approval["runner_ci_run_id"] = None
        approval["runner_ci_conclusion"] = None
        approval.pop("consumed_on", None)
        approval.pop("execution_result_ref", None)

    return local, pii


def _granted_pair() -> tuple[dict[str, object], dict[str, object]]:
    local, pii = _not_granted_pair()
    runner_checkpoint = "a" * 40

    local.update(
        {
            "status": "GRANTED_NOT_CONSUMED",
            "owner_authorization": (
                "APPROVO NY OSC SIXTH TRANSIENT LOCAL FILE BOUNDED ONCE"
            ),
            "granted_on": "2026-09-21",
            "execution_approval_ref": "SIXTH_LOCAL_APPROVAL_REF",
            "runner_checkpoint": runner_checkpoint,
            "runner_ci_run_id": 123456,
            "runner_ci_conclusion": "SUCCESS",
        }
    )
    pii.update(
        {
            "status": "GRANTED_NOT_CONSUMED",
            "owner_authorization": (
                "APPROVO NY OSC OWNER NAME FILE SIXTH BOUNDED "
                "TRANSIENT PII ATTEMPT ONCE"
            ),
            "granted_on": "2026-09-21",
            "execution_approval_ref": "SIXTH_PII_APPROVAL_REF",
            "runner_checkpoint": runner_checkpoint,
            "runner_ci_run_id": 123456,
            "runner_ci_conclusion": "SUCCESS",
        }
    )
    return local, pii


def test_current_sixth_approval_artifacts_validate_against_contracts() -> None:
    Draft202012Validator(_load(LOCAL_SCHEMA)).validate(_load(LOCAL_APPROVAL))
    Draft202012Validator(_load(PII_SCHEMA)).validate(_load(PII_APPROVAL))


def test_sixth_not_granted_fixture_validates_and_is_fail_closed() -> None:
    local, pii = _not_granted_pair()

    Draft202012Validator(_load(LOCAL_SCHEMA)).validate(local)
    Draft202012Validator(_load(PII_SCHEMA)).validate(pii)

    for approval in (local, pii):
        assert approval["status"] == "NOT_GRANTED"
        assert approval["runner_checkpoint"] is None
        assert approval["runner_ci_run_id"] is None
        assert approval["owner_authorization"] is None
        assert approval["execution_approval_ref"] is None


def test_sixth_granted_approvals_validate_and_build_runtime_v1_1(
    tmp_path: Path,
) -> None:
    local, pii = _granted_pair()
    Draft202012Validator(_load(LOCAL_SCHEMA)).validate(local)
    Draft202012Validator(_load(PII_SCHEMA)).validate(pii)

    local_path = tmp_path / "local.json"
    pii_path = tmp_path / "pii.json"
    local_path.write_text(json.dumps(local), encoding="utf-8")
    pii_path.write_text(json.dumps(pii), encoding="utf-8")

    authorization = build_real_execution_authorization_v1_1(
        local_path,
        pii_path,
        expected_attempt_number=6,
    )
    assert authorization.contract_version == "1.1.0"
    assert authorization.attempt_number == 6
    assert authorization.quote_dialect_mode == "LINE_LOCAL_ARBITRATION"


def test_sixth_consumed_approvals_validate_but_cannot_build_runtime(
    tmp_path: Path,
) -> None:
    local, pii = _granted_pair()
    for approval in (local, pii):
        approval["status"] = "CONSUMED_SINGLE_USE_NON_REUSABLE"
        approval["consumed_on"] = "2026-09-21"
        approval["execution_result_ref"] = (
            "sources/evidence/"
            "ny_osc_owner_name_file_sixth_attempt_execution_result.v1.json"
        )

    Draft202012Validator(_load(LOCAL_SCHEMA)).validate(local)
    Draft202012Validator(_load(PII_SCHEMA)).validate(pii)

    local_path = tmp_path / "local.json"
    pii_path = tmp_path / "pii.json"
    local_path.write_text(json.dumps(local), encoding="utf-8")
    pii_path.write_text(json.dumps(pii), encoding="utf-8")

    with pytest.raises(ValueError, match="approval is not available"):
        build_real_execution_authorization_v1_1(
            local_path,
            pii_path,
            expected_attempt_number=6,
        )


def test_sixth_granted_approval_rejects_non_git_runner_checkpoint() -> None:
    local, _ = _granted_pair()
    local["runner_checkpoint"] = "runner-not-a-git-sha"

    with pytest.raises(ValidationError):
        Draft202012Validator(_load(LOCAL_SCHEMA)).validate(local)


def test_sixth_not_granted_fixture_rejects_grant_or_consumption_fields() -> None:
    local, pii = _not_granted_pair()

    local["owner_authorization"] = (
        "APPROVO NY OSC SIXTH TRANSIENT LOCAL FILE BOUNDED ONCE"
    )
    with pytest.raises(ValidationError):
        Draft202012Validator(_load(LOCAL_SCHEMA)).validate(local)

    pii["consumed_on"] = "2026-09-21"
    with pytest.raises(ValidationError):
        Draft202012Validator(_load(PII_SCHEMA)).validate(pii)


def test_current_sixth_approvals_are_consumed_and_non_reusable(
    tmp_path: Path,
) -> None:
    local = _load(LOCAL_APPROVAL)
    pii = _load(PII_APPROVAL)

    for approval in (local, pii):
        assert approval["status"] == "CONSUMED_SINGLE_USE_NON_REUSABLE"
        assert approval["reusable"] is False
        assert approval["retry_authorized"] is False
        assert approval["consumed_on"] == "2026-09-21"
        assert approval["execution_result_ref"] == (
            "sources/evidence/"
            "ny_osc_owner_name_file_sixth_attempt_execution_result.v1.json"
        )

    local_path = tmp_path / "local.json"
    pii_path = tmp_path / "pii.json"
    local_path.write_text(json.dumps(local), encoding="utf-8")
    pii_path.write_text(json.dumps(pii), encoding="utf-8")

    with pytest.raises(ValueError, match="approval is not available"):
        build_real_execution_authorization_v1_1(
            local_path,
            pii_path,
            expected_attempt_number=6,
        )
