from __future__ import annotations

import io
import json
import tempfile
import zipfile
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest

from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution_v1_5 import (
    EXPECTED_PROPOSAL_CHECKPOINT,
    EXPECTED_PROPOSAL_CI_RUN_ID,
    NyTransientLocalExecutionAuthorizationV1_4,
    build_real_execution_authorization_v1_4,
    execute_transient_local_file_discovery_v1_5,
)

RUNNER = "b" * 40
PROPOSAL_REF = (
    "sources/proposals/ny_osc_owner_name_file_eighth_bounded_attempt_authorization.v1.json"
)


def _stamp(value: datetime) -> str:
    return value.astimezone(UTC).isoformat().replace("+00:00", "Z")


def _common() -> dict[str, object]:
    return {
        "attempt_number": 8,
        "proposal_ref": PROPOSAL_REF,
        "proposal_checkpoint": EXPECTED_PROPOSAL_CHECKPOINT,
        "proposal_ci_run_id": EXPECTED_PROPOSAL_CI_RUN_ID,
        "runner_checkpoint": RUNNER,
        "runner_ci_run_id": 999008,
        "runner_ci_conclusion": "SUCCESS",
    }


def _local() -> dict[str, object]:
    return {
        **_common(),
        "execution_approval_ref": "eighth-local-ref",
        "status": "GRANTED_NOT_CONSUMED",
        "scope": {
            "expected_local_filename": "FINDERS.zip",
            "max_download_bytes": 450000000,
            "dedicated_os_temp_directory_required": True,
            "immediate_logical_deletion_required": True,
            "durable_raw_persistence_allowed": False,
            "repository_persistence_allowed": False,
            "cloud_sync_allowed": False,
            "chat_upload_allowed": False,
        },
    }


def _pii() -> dict[str, object]:
    return {
        **_common(),
        "execution_approval_ref": "eighth-pii-ref",
        "status": "GRANTED_NOT_CONSUMED",
        "execution_bounds": {
            "downloads_max": 1,
            "retries_max": 0,
            "max_download_bytes": 450000000,
            "max_uncompressed_bytes": 2000000000,
            "max_archive_members": 1,
            "required_transient_execution_authorization_contract_version": "1.4.0",
            "required_execution_result_contract_version": "1.5.0",
            "required_quote_dialect_mode": "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY",
            "automatic_retry_allowed": False,
        },
        "processing_scope": {
            "transient_owner_pii_in_memory_allowed": True,
            "owner_rows_persistence_allowed": False,
            "owner_field_decoding_allowed": False,
            "owner_field_buffering_allowed": False,
            "owner_field_logging_allowed": False,
            "row_specific_human_inspection_allowed": False,
        },
    }


def _preflight(performed: datetime) -> dict[str, object]:
    return {
        **_common(),
        "receipt_ref": "eighth-preflight-ref",
        "status": "EXACT_MATCH",
        "remote_preflight_performed": True,
        "performed_at_utc": _stamp(performed),
        "freshness_window_seconds": 900,
        "download_performed": False,
        "owner_file_opened": False,
        "owner_pii_processed": False,
        "contains_owner_pii": False,
    }


def _execution() -> dict[str, object]:
    return {
        **_common(),
        "execution_approval_ref": "eighth-execution-ref",
        "status": "GRANTED_NOT_CONSUMED",
        "fresh_preflight_receipt_ref": "eighth-preflight-ref",
        "fresh_preflight_status": "EXACT_MATCH",
        "download_authority": "ONE_MANUAL_DOWNLOAD_TO_DEDICATED_OS_TEMP",
        "execution_authority": "ONE_BOUND_GATE8_EXECUTION",
        "authorization_scope": {
            "manual_download_allowed": True,
            "direct_network_client_allowed": False,
            "downloads_max": 1,
            "gate8_executions_max": 1,
            "retries_max": 0,
            "source_activation": False,
            "production_classification_activation": False,
            "identity_resolution": False,
            "beneficiary_matching": False,
            "outreach": False,
            "fee_agreement": False,
            "representation": False,
            "claim_activity": False,
        },
    }


def _write(path: Path, payload: dict[str, object]) -> Path:
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def _build(
    tmp_path: Path,
    *,
    performed: datetime,
    started: datetime,
    now: datetime,
) -> NyTransientLocalExecutionAuthorizationV1_4:
    return build_real_execution_authorization_v1_4(
        _write(tmp_path / "local.json", _local()),
        _write(tmp_path / "pii.json", _pii()),
        _write(tmp_path / "preflight.json", _preflight(performed)),
        _write(tmp_path / "execution.json", _execution()),
        expected_runner_checkpoint=RUNNER,
        authorized_download_started_at_utc=_stamp(started),
        now_utc=now,
    )


def _zip_payload(payload: bytes) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("owner_names.txt", payload)
    return buffer.getvalue()


def _row(owner_name: str) -> str:
    return "|".join(
        [
            "1",
            "IN03",
            "Synthetic description",
            "1",
            owner_name,
            "1 Synthetic Street",
            "",
            "",
            "Albany",
            "NY",
            "12207-0000",
            "USA",
            "Synthetic Holder",
            "2026",
        ]
    )


def _temp_archive(contents: bytes) -> Path:
    root = Path(tempfile.mkdtemp(prefix="unclaimed-ny-osc-gate2-eighth-"))
    path = root / "FINDERS.zip"
    path.write_bytes(contents)
    return path


def test_attempt8_builder_accepts_valid_start_even_when_runtime_is_later(tmp_path: Path) -> None:
    performed = datetime(2026, 9, 22, 14, 39, 31, tzinfo=UTC)
    started = performed + timedelta(minutes=14)
    now = performed + timedelta(minutes=40)

    auth = _build(tmp_path, performed=performed, started=started, now=now)

    assert auth.contract_version == "1.4.0"
    assert auth.attempt_number == 8
    assert auth.eighth_execution_authorization_ref == "eighth-execution-ref"
    assert auth.authorized_download_started_at_utc == _stamp(started)
    assert auth.downloads_max == 1
    assert auth.retries_max == 0
    assert auth.direct_network_client_allowed is False


def test_attempt8_builder_rejects_start_after_freshness_deadline(tmp_path: Path) -> None:
    performed = datetime(2026, 9, 22, 14, 39, 31, tzinfo=UTC)
    started = performed + timedelta(seconds=901)

    with pytest.raises(ValueError, match="outside fresh preflight window"):
        _build(tmp_path, performed=performed, started=started, now=started)


def test_attempt8_runtime_reuses_reviewed_data_path_and_returns_attempt8_non_pii_result(
    tmp_path: Path,
) -> None:
    performed = datetime(2026, 9, 22, 14, 39, 31, tzinfo=UTC)
    started = performed + timedelta(minutes=1)
    auth = _build(
        tmp_path,
        performed=performed,
        started=started,
        now=performed + timedelta(minutes=30),
    )
    archive = _temp_archive(_zip_payload((_row("Synthetic Owner Alpha") + "\n").encode()))

    result = execute_transient_local_file_discovery_v1_5(auth, archive)

    assert result.contract_version == "1.5.0"
    assert result.attempt_number == 8
    assert result.status == "DISCOVERED"
    assert result.reason_code == "DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED"
    assert result.execution_authorization_ref == "eighth-execution-ref"
    assert result.authorized_download_started_at_utc == _stamp(started)
    assert result.freshness_bound_to_download_start is True
    assert archive.exists() is False
    serialized = result.model_dump_json()
    assert "Synthetic Owner Alpha" not in serialized
    assert "Synthetic Street" not in serialized


def test_attempt8_runtime_module_has_no_cli_or_network_client() -> None:
    from unclaimed_platform.adapters.sources import (
        ny_owner_name_transient_local_execution_v1_5 as runtime,
    )

    source = Path(runtime.__file__).read_text(encoding="utf-8").lower()
    assert "def main(" not in source
    assert "argparse" not in source
    assert "httpx" not in source
    assert "requests" not in source
    assert "urllib.request" not in source
