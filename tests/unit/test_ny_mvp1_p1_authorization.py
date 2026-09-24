import json
from datetime import UTC, datetime
from pathlib import Path

import pytest

from unclaimed_platform.domain.ny_mvp1_p1_authorization import (
    GATE_PHRASES,
    SCOPE_BLOB_SHA,
    SCOPE_REF,
    build_p1_execution_authorization,
)

RUNNER_SHA = "a" * 40
NOW = datetime(2026, 9, 24, 10, 1, tzinfo=UTC)


def gate(gate_id: str, *, provider=False, status="GRANTED_NOT_CONSUMED"):
    phrase = GATE_PHRASES[gate_id]
    payload = {
        "schema_version": "1.0.0",
        "artifact_id": "ny.mvp1.p1.single_use_gate",
        "gate_id": gate_id,
        "required_owner_phrase": phrase,
        "owner_authorization": phrase if status == "GRANTED_NOT_CONSUMED" else None,
        "granted_on": "2026-09-24" if status == "GRANTED_NOT_CONSUMED" else None,
        "execution_approval_ref": (
            f"synthetic:{gate_id}" if status == "GRANTED_NOT_CONSUMED" else None
        ),
        "status": status,
        "single_use": True,
        "reusable": False,
        "retry_authorized": False,
        "scope_ref": SCOPE_REF,
        "scope_blob_sha": SCOPE_BLOB_SHA,
        "runner_checkpoint": RUNNER_SHA if status == "GRANTED_NOT_CONSUMED" else None,
        "runner_ci_run_id": 12345 if status == "GRANTED_NOT_CONSUMED" else None,
        "runner_ci_conclusion": (
            "SUCCESS" if status == "GRANTED_NOT_CONSUMED" else None
        ),
        "provider_binding": None,
    }
    if provider and status == "GRANTED_NOT_CONSUMED":
        payload["provider_binding"] = {
            "provider_id": "synthetic-provider",
            "provider_terms_review_ref": "synthetic:terms-review",
            "approved_external_cash_budget_cents": 0,
            "approved_manual_research_cap_seconds": 900,
            "paid_api_allowed": False,
            "paid_data_broker_allowed": False,
            "consumer_report_fcra_product_allowed": False,
        }
    return payload


def write_json(path: Path, payload) -> Path:
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def common_paths(tmp_path: Path, *, local_status="GRANTED_NOT_CONSUMED"):
    local = write_json(
        tmp_path / "local.json",
        gate(
            "HUMAN_NY_MVP1_P1_TRANSIENT_LOCAL_FILE_APPROVAL",
            status=local_status,
        ),
    )
    pii = write_json(
        tmp_path / "pii.json",
        gate("HUMAN_NY_MVP1_P1_L1_TRANSIENT_PII_APPROVAL"),
    )
    preflight_gate = write_json(
        tmp_path / "preflight-gate.json",
        gate("HUMAN_NY_MVP1_P1_FRESH_LISTING_PREFLIGHT_AUTHORIZATION"),
    )
    execution = write_json(
        tmp_path / "exec.json",
        gate("HUMAN_NY_MVP1_P1_L1_EXECUTION_AUTHORIZATION"),
    )
    preflight = write_json(
        tmp_path / "preflight.json",
        {
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
            "runner_checkpoint": RUNNER_SHA,
            "preflight_authorization_ref": (
                f"synthetic:HUMAN_NY_MVP1_P1_FRESH_LISTING_PREFLIGHT_AUTHORIZATION"
            ),
        },
    )
    return local, pii, preflight_gate, execution, preflight


def test_builds_l1_authorization_only_from_fresh_granted_gates(tmp_path):
    local, pii, preflight_gate, execution, preflight = common_paths(tmp_path)
    auth = build_p1_execution_authorization(
        local_file_gate_path=local,
        l1_pii_gate_path=pii,
        preflight_gate_path=preflight_gate,
        l1_execution_gate_path=execution,
        preflight_receipt_path=preflight,
        expected_runner_checkpoint=RUNNER_SHA,
        authorized_download_started_at_utc="2026-09-24T10:00:30Z",
        now_utc=NOW,
    )
    assert auth.l2a_enabled is False
    assert auth.provider_binding is None
    assert auth.retries_max == 0
    assert auth.direct_network_client_allowed is False


def test_not_granted_gate_is_rejected(tmp_path):
    local, pii, preflight_gate, execution, preflight = common_paths(
        tmp_path,
        local_status="NOT_GRANTED",
    )
    with pytest.raises(ValueError, match="not granted/not-consumed"):
        build_p1_execution_authorization(
            local_file_gate_path=local,
            l1_pii_gate_path=pii,
            preflight_gate_path=preflight_gate,
            l1_execution_gate_path=execution,
            preflight_receipt_path=preflight,
            expected_runner_checkpoint=RUNNER_SHA,
            authorized_download_started_at_utc="2026-09-24T10:00:30Z",
            now_utc=NOW,
        )


def test_partial_l2a_gate_set_is_rejected(tmp_path):
    local, pii, preflight_gate, execution, preflight = common_paths(tmp_path)
    l2a_pii = write_json(
        tmp_path / "l2a-pii.json",
        gate("HUMAN_NY_MVP1_P1_L2A_TARGETABILITY_PII_SCOPE_APPROVAL"),
    )
    with pytest.raises(ValueError, match="all three"):
        build_p1_execution_authorization(
            local_file_gate_path=local,
            l1_pii_gate_path=pii,
            preflight_gate_path=preflight_gate,
            l1_execution_gate_path=execution,
            preflight_receipt_path=preflight,
            expected_runner_checkpoint=RUNNER_SHA,
            authorized_download_started_at_utc="2026-09-24T10:00:30Z",
            l2a_pii_gate_path=l2a_pii,
            now_utc=NOW,
        )


def test_builds_l2a_only_with_provider_binding_and_all_fresh_gates(tmp_path):
    local, pii, preflight_gate, execution, preflight = common_paths(tmp_path)
    l2a_pii = write_json(
        tmp_path / "l2a-pii.json",
        gate("HUMAN_NY_MVP1_P1_L2A_TARGETABILITY_PII_SCOPE_APPROVAL"),
    )
    provider = write_json(
        tmp_path / "provider.json",
        gate(
            "HUMAN_NY_MVP1_P1_L2A_PROVIDER_AND_BUDGET_APPROVAL",
            provider=True,
        ),
    )
    l2a_exec = write_json(
        tmp_path / "l2a-exec.json",
        gate("HUMAN_NY_MVP1_P1_L2A_EXECUTION_AUTHORIZATION"),
    )

    auth = build_p1_execution_authorization(
        local_file_gate_path=local,
        l1_pii_gate_path=pii,
        preflight_gate_path=preflight_gate,
        l1_execution_gate_path=execution,
        preflight_receipt_path=preflight,
        expected_runner_checkpoint=RUNNER_SHA,
        authorized_download_started_at_utc="2026-09-24T10:00:30Z",
        l2a_pii_gate_path=l2a_pii,
        l2a_provider_budget_gate_path=provider,
        l2a_execution_gate_path=l2a_exec,
        now_utc=NOW,
    )
    assert auth.l2a_enabled is True
    assert auth.provider_binding is not None
    assert auth.provider_binding.provider_id == "synthetic-provider"
    assert auth.provider_binding.approved_external_cash_budget_cents == 0
    assert auth.provider_binding.approved_manual_research_cap_seconds == 900
