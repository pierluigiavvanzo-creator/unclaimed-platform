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
    / "ny_osc_third_attempt_transient_local_approval.schema.json"
)
LOCAL_APPROVAL = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_third_attempt_transient_local_approval.v1.json"
)
PII_SCHEMA = (
    ROOT
    / "schemas/common"
    / "ny_osc_third_attempt_transient_pii_approval.schema.json"
)
PII_APPROVAL = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_third_attempt_transient_pii_approval.v1.json"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_third_attempt_approvals_are_valid_granted_and_single_use() -> None:
    local = _load(LOCAL_APPROVAL)
    pii = _load(PII_APPROVAL)

    Draft202012Validator(_load(LOCAL_SCHEMA)).validate(local)
    Draft202012Validator(_load(PII_SCHEMA)).validate(pii)

    for approval in (local, pii):
        assert approval["status"] == "GRANTED_NOT_CONSUMED"
        assert approval["granted_on"] == "2026-09-18"
        assert approval["attempt_number"] == 3
        assert approval["single_use"] is True
        assert approval["reusable"] is False
        assert approval["retry_authorized"] is False
        assert approval["runner_checkpoint"] == (
            "2d871ee041abe9cccc0e0fa32b849bbe223bdfa2"
        )
        assert approval["runner_ci_run_id"] == 35385157576
        assert approval["runner_ci_conclusion"] == "SUCCESS"

    assert local["owner_authorization"] == (
        "APPROVO NY OSC THIRD TRANSIENT LOCAL FILE BOUNDED ONCE"
    )
    assert pii["owner_authorization"] == (
        "APPROVO NY OSC OWNER NAME FILE THIRD BOUNDED TRANSIENT PII ATTEMPT ONCE"
    )
    assert local["execution_approval_ref"] != pii["execution_approval_ref"]

    bounds = pii["execution_bounds"]
    assert bounds["downloads_max"] == 1
    assert bounds["retries_max"] == 0
    assert bounds["max_download_bytes"] == 450_000_000
    assert bounds["max_uncompressed_bytes"] == 2_000_000_000
    assert bounds["max_archive_members"] == 1
    assert bounds["automatic_widening_allowed"] is False
    assert bounds["automatic_retry_allowed"] is False


def test_granted_third_attempt_approvals_build_bound_authorization() -> None:
    authorization = build_real_execution_authorization(
        LOCAL_APPROVAL,
        PII_APPROVAL,
        expected_attempt_number=3,
    )

    assert authorization.mode == "AUTHORIZED_REAL_ONCE"
    assert authorization.attempt_number == 3
    assert authorization.local_file_approval_ref != authorization.gate2_approval_ref
    assert authorization.max_download_bytes == 450_000_000
    assert authorization.max_uncompressed_bytes == 2_000_000_000
    assert authorization.max_archive_members == 1
