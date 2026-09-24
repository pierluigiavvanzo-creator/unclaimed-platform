import copy
import json
import zipfile
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError

from unclaimed_platform.adapters.sources.ny_owner_name_p1_targetability_local import (
    execute_real_p1_targetability_local,
)
from unclaimed_platform.domain.ny_mvp1_p1_authorization import P1ExecutionAuthorization

ROOT = Path(__file__).resolve().parents[2]
GATE_SCHEMA = ROOT / "schemas/common/ny_mvp1_p1_single_use_gate.schema.json"
PREFLIGHT_SCHEMA = (
    ROOT / "schemas/common/ny_mvp1_p1_fresh_listing_preflight_receipt.schema.json"
)
RESULT_SCHEMA = (
    ROOT / "schemas/common/ny_mvp1_real_p1_targetability_run_result.schema.json"
)
GATE_FILES = (
    "ny_mvp1_p1_transient_local_file_gate.v1.json",
    "ny_mvp1_p1_l1_transient_pii_gate.v1.json",
    "ny_mvp1_p1_fresh_listing_preflight_gate.v1.json",
    "ny_mvp1_p1_l1_execution_gate.v1.json",
    "ny_mvp1_p1_l2a_targetability_pii_gate.v1.json",
    "ny_mvp1_p1_l2a_provider_budget_gate.v1.json",
    "ny_mvp1_p1_l2a_execution_gate.v1.json",
)


def _validator(path: Path) -> Draft202012Validator:
    return Draft202012Validator(json.loads(path.read_text(encoding="utf-8")))


def _authorization() -> P1ExecutionAuthorization:
    return P1ExecutionAuthorization(
        runner_checkpoint="a" * 40,
        source_snapshot_ref="synthetic:snapshot",
        fresh_preflight_receipt_ref="synthetic:preflight",
        authorized_download_started_at_utc="2026-09-24T10:00:10Z",
        local_file_approval_ref="synthetic:local",
        l1_pii_approval_ref="synthetic:l1-pii",
        preflight_authorization_ref="synthetic:preflight-auth",
        l1_execution_authorization_ref="synthetic:l1-exec",
    )


def _archive(tmp_path: Path) -> Path:
    fields = [
        "SECRET-PROPERTY-ID",
        "IN03",
        "SYNTHETIC-DESCRIPTION",
        "1",
        "SECRET-OWNER-NAME",
        "SECRET-ADDRESS",
        "",
        "",
        "SYNTHETIC-CITY",
        "NY",
        "10001",
        "US",
        "SECRET-HOLDER",
        "2000",
    ]
    path = tmp_path / "FINDERS.zip"
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("FINDERS.txt", ("|".join(fields) + "\r\n").encode("ascii"))
    return path


def test_all_seven_gate_templates_validate_and_are_not_granted() -> None:
    validator = _validator(GATE_SCHEMA)
    for filename in GATE_FILES:
        payload = json.loads(
            (ROOT / "sources/proposals" / filename).read_text(encoding="utf-8")
        )
        validator.validate(payload)
        assert payload["status"] == "NOT_GRANTED"
        assert payload["owner_authorization"] is None
        assert payload["execution_approval_ref"] is None


def test_gate_schema_rejects_turning_template_into_grant_without_runner_binding() -> None:
    validator = _validator(GATE_SCHEMA)
    payload = json.loads(
        (
            ROOT
            / "sources/proposals"
            / "ny_mvp1_p1_l1_execution_gate.v1.json"
        ).read_text(encoding="utf-8")
    )
    payload["status"] = "GRANTED_NOT_CONSUMED"
    payload["owner_authorization"] = payload["required_owner_phrase"]
    payload["granted_on"] = "2026-09-24"
    payload["execution_approval_ref"] = "synthetic:approval"
    with pytest.raises(ValidationError):
        validator.validate(payload)


def test_preflight_receipt_contract_is_privacy_bounded() -> None:
    payload = {
        "schema_version": "1.0.0",
        "artifact_id": "ny.mvp1.p1.fresh_listing_preflight_receipt",
        "receipt_ref": "synthetic:receipt",
        "status": "EXACT_MATCH",
        "source_id": "ny.osc.unclaimed_funds.owner_name_file",
        "performed_at_utc": "2026-09-24T10:00:00Z",
        "freshness_window_seconds": 900,
        "remote_name": "FINDERS.zip",
        "remote_size_display": "390.51 MB",
        "remote_last_modified_display": "9/16/2026, 1:33:31 PM",
        "remote_preflight_performed": True,
        "download_performed": False,
        "owner_file_opened": False,
        "owner_pii_processed": False,
        "contains_owner_pii": False,
        "source_snapshot_ref": "synthetic:snapshot",
        "runner_checkpoint": "a" * 40,
        "preflight_authorization_ref": "synthetic:preflight-approval",
    }
    _validator(PREFLIGHT_SCHEMA).validate(payload)

    unsafe = copy.deepcopy(payload)
    unsafe["owner_pii_processed"] = True
    with pytest.raises(ValidationError):
        _validator(PREFLIGHT_SCHEMA).validate(unsafe)


def test_real_p1_runner_output_validates_and_contains_no_transient_values(tmp_path) -> None:
    path = _archive(tmp_path)
    result = execute_real_p1_targetability_local(_authorization(), path)
    payload = result.model_dump(mode="json")

    _validator(RESULT_SCHEMA).validate(payload)
    serialized = json.dumps(payload, sort_keys=True)
    for marker in (
        "SECRET-PROPERTY-ID",
        "SECRET-OWNER-NAME",
        "SECRET-ADDRESS",
        "SECRET-HOLDER",
    ):
        assert marker not in serialized


def test_result_schema_rejects_owner_pii_persistence_expansion(tmp_path) -> None:
    path = _archive(tmp_path)
    payload = execute_real_p1_targetability_local(
        _authorization(), path
    ).model_dump(mode="json")
    payload["safety"]["owner_pii_persisted"] = True

    with pytest.raises(ValidationError):
        _validator(RESULT_SCHEMA).validate(payload)


def test_result_schema_rejects_reusable_execution(tmp_path) -> None:
    path = _archive(tmp_path)
    payload = execute_real_p1_targetability_local(
        _authorization(), path
    ).model_dump(mode="json")
    payload["reusable"] = True

    with pytest.raises(ValidationError):
        _validator(RESULT_SCHEMA).validate(payload)
