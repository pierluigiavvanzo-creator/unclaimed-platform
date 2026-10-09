from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = (
    ROOT
    / "schemas/common/ny_osc_seventh_attempt_transient_local_approval.schema.json"
)
APPROVAL = (
    ROOT
    / "sources/evidence/ny_osc_owner_name_file_seventh_attempt_transient_local_approval.v1.json"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_seventh_transient_local_approval_is_valid_single_use_grant() -> None:
    approval = _load(APPROVAL)
    Draft202012Validator(_load(SCHEMA)).validate(approval)

    assert approval["status"] == "GRANTED_NOT_CONSUMED"
    assert approval["single_use"] is True
    assert approval["reusable"] is False
    assert approval["retry_authorized"] is False
    assert approval["attempt_number"] == 7
    assert approval["owner_authorization"] == (
        "APPROVO NY OSC SEVENTH TRANSIENT LOCAL FILE BOUNDED ONCE"
    )
    assert approval["runner_checkpoint"] == (
        "96d58f6c5e0c54c59ad1b9b4606d34eb1b050f72"
    )
    assert approval["runner_ci_run_id"] == 35657861859
    assert approval["runner_ci_conclusion"] == "SUCCESS"


def test_seventh_transient_local_approval_grants_no_download_or_pii() -> None:
    approval = _load(APPROVAL)
    denied = approval["authorization_does_not_grant"]

    assert isinstance(denied, dict)
    assert denied["source_network_access"] is False
    assert denied["remote_preflight"] is False
    assert denied["download"] is False
    assert denied["owner_pii_processing"] is False
    assert denied["source_activation"] is False
    assert denied["identity_resolution"] is False
    assert denied["beneficiary_matching"] is False
    assert denied["outreach"] is False
    assert denied["fee_agreement"] is False
    assert denied["representation"] is False
    assert denied["claim_activity"] is False


def test_seventh_transient_local_approval_scope_remains_bounded() -> None:
    approval = _load(APPROVAL)
    scope = approval["scope"]

    assert scope == {
        "expected_local_filename": "FINDERS.zip",
        "max_download_bytes": 450000000,
        "dedicated_os_temp_directory_required": True,
        "immediate_logical_deletion_required": True,
        "durable_raw_persistence_allowed": False,
        "repository_persistence_allowed": False,
        "cloud_sync_allowed": False,
        "chat_upload_allowed": False,
        "physical_secure_erasure_guaranteed": False,
    }
