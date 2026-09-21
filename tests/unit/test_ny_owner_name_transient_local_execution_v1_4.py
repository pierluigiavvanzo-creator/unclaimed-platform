from __future__ import annotations

import io
import json
import tempfile
import zipfile
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest

from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution_v1_4 import (
    EXPECTED_PROPOSAL_CHECKPOINT,
    NyTransientLocalExecutionAuthorizationV1_3,
    build_real_execution_authorization_v1_3,
    execute_transient_local_file_discovery_v1_4,
)

RUNNER = "a" * 40
PROPOSAL_REF = (
    "sources/proposals/"
    "ny_osc_owner_name_file_seventh_bounded_attempt_authorization.v1.json"
)
PROPOSAL_CI = 35653220457


def _zip_payload(payload: bytes) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("owner_names.txt", payload)
    return buffer.getvalue()


def _row(
    *,
    owner_name: str = "Synthetic Owner Alpha",
    address1: str = "1 Synthetic Street",
) -> str:
    return "|".join(
        [
            "1",
            "IN03",
            "Synthetic description",
            "1",
            owner_name,
            address1,
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


def _common() -> dict[str, object]:
    return {
        "attempt_number": 7,
        "proposal_ref": PROPOSAL_REF,
        "proposal_checkpoint": EXPECTED_PROPOSAL_CHECKPOINT,
        "proposal_ci_run_id": PROPOSAL_CI,
        "runner_checkpoint": RUNNER,
        "runner_ci_run_id": 999001,
        "runner_ci_conclusion": "SUCCESS",
    }


def _local() -> dict[str, object]:
    return {
        **_common(),
        "schema_version": "1.0.0",
        "authorization_gate": (
            "HUMAN_NY_OSC_SEVENTH_TRANSIENT_LOCAL_FILE_RETENTION_AUTHORIZATION"
        ),
        "required_owner_authorization": (
            "APPROVO NY OSC SEVENTH TRANSIENT LOCAL FILE BOUNDED ONCE"
        ),
        "owner_authorization": (
            "APPROVO NY OSC SEVENTH TRANSIENT LOCAL FILE BOUNDED ONCE"
        ),
        "granted_on": "2026-09-21",
        "execution_approval_ref": "seventh-local-ref",
        "status": "GRANTED_NOT_CONSUMED",
        "single_use": True,
        "reusable": False,
        "retry_authorized": False,
        "scope": {
            "expected_local_filename": "FINDERS.zip",
            "max_download_bytes": 450000000,
            "dedicated_os_temp_directory_required": True,
            "immediate_logical_deletion_required": True,
            "durable_raw_persistence_allowed": False,
            "repository_persistence_allowed": False,
            "cloud_sync_allowed": False,
            "chat_upload_allowed": False,
            "physical_secure_erasure_guaranteed": False,
        },
        "authorization_does_not_grant": {
            "source_network_access": False,
            "remote_preflight": False,
            "download": False,
            "owner_pii_processing": False,
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


def _pii() -> dict[str, object]:
    return {
        **_common(),
        "schema_version": "1.0.0",
        "authorization_gate": "HUMAN_NY_OSC_SEVENTH_TRANSIENT_PII_AUTHORIZATION",
        "required_owner_authorization": (
            "APPROVO NY OSC OWNER NAME FILE SEVENTH BOUNDED TRANSIENT PII ATTEMPT ONCE"
        ),
        "owner_authorization": (
            "APPROVO NY OSC OWNER NAME FILE SEVENTH BOUNDED TRANSIENT PII ATTEMPT ONCE"
        ),
        "granted_on": "2026-09-21",
        "execution_approval_ref": "seventh-pii-ref",
        "status": "GRANTED_NOT_CONSUMED",
        "single_use": True,
        "reusable": False,
        "retry_authorized": False,
        "source_identity": {
            "source_id": "ny.osc.unclaimed_funds.owner_name_file",
            "expected_remote_name": "FINDERS.zip",
            "historical_size_display_for_preflight_only": "390.51 MB",
            "historical_last_modified_display_for_preflight_only": (
                "9/16/2026, 1:33:31 PM"
            ),
            "fresh_preflight_required": True,
        },
        "execution_bounds": {
            "downloads_max": 1,
            "retries_max": 0,
            "max_download_bytes": 450000000,
            "max_uncompressed_bytes": 2000000000,
            "max_archive_members": 1,
            "text_members_required_exactly": 1,
            "expected_delimiter": "|",
            "expected_documented_field_count": 14,
            "parser_chunk_bytes": 65536,
            "required_transient_execution_authorization_contract_version": "1.3.0",
            "required_execution_result_contract_version": "1.4.0",
            "required_quote_dialect_mode": "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY",
            "required_structural_diagnostic_contract_version": "1.0.0",
            "quote_dialect_diagnostic_required_null": True,
            "automatic_widening_allowed": False,
            "automatic_retry_allowed": False,
        },
        "processing_scope": {
            "transient_owner_pii_in_memory_allowed": True,
            "owner_rows_persistence_allowed": False,
            "owner_field_decoding_allowed": False,
            "owner_field_buffering_allowed": False,
            "owner_field_logging_allowed": False,
            "row_specific_human_inspection_allowed": False,
            "derived_non_pii_schema_metadata_persistence_allowed": True,
            "structural_diagnostic_persistence_allowed": True,
            "quote_dialect_diagnostic_persistence_allowed": False,
        },
        "authorization_does_not_grant": {
            "source_network_access": False,
            "remote_preflight": False,
            "download": False,
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


def _preflight(performed_at: datetime) -> dict[str, object]:
    stamp = performed_at.astimezone(UTC).isoformat().replace("+00:00", "Z")
    listing = {
        "remote_name": "FINDERS.zip",
        "size_display": "390.51 MB",
        "last_modified_display": "9/16/2026, 1:33:31 PM",
    }
    return {
        **_common(),
        "schema_version": "1.0.0",
        "artifact_id": "ny.osc.owner_name_file.seventh_fresh_listing_preflight_receipt",
        "receipt_ref": "seventh-preflight-ref",
        "source_id": "ny.osc.unclaimed_funds.owner_name_file",
        "status": "EXACT_MATCH",
        "remote_preflight_performed": True,
        "preflight_authorization_ref": "seventh-preflight-auth-ref",
        "performed_at_utc": stamp,
        "freshness_window_seconds": 900,
        "expected_listing": listing,
        "observed_listing": listing,
        "download_performed": False,
        "owner_file_opened": False,
        "owner_pii_processed": False,
        "contains_owner_pii": False,
    }


def _execution() -> dict[str, object]:
    return {
        **_common(),
        "schema_version": "1.0.0",
        "authorization_gate": "HUMAN_NY_OSC_SEVENTH_EXECUTION_AUTHORIZATION",
        "required_owner_authorization": (
            "AUTHORIZE_NY_OSC_SEVENTH_BOUNDED_EXECUTION_ONCE"
        ),
        "owner_authorization": "AUTHORIZE_NY_OSC_SEVENTH_BOUNDED_EXECUTION_ONCE",
        "granted_on": "2026-09-21",
        "execution_approval_ref": "seventh-execution-ref",
        "status": "GRANTED_NOT_CONSUMED",
        "single_use": True,
        "reusable": False,
        "retry_authorized": False,
        "fresh_preflight_receipt_ref": "seventh-preflight-ref",
        "fresh_preflight_status": "EXACT_MATCH",
        "download_authority": "ONE_MANUAL_DOWNLOAD_TO_DEDICATED_OS_TEMP",
        "execution_authority": "ONE_BOUND_GATE7_EXECUTION",
        "authorization_scope": {
            "manual_download_allowed": True,
            "direct_network_client_allowed": False,
            "downloads_max": 1,
            "gate7_executions_max": 1,
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


def _build(tmp_path: Path, *, performed_at: datetime, now: datetime) -> NyTransientLocalExecutionAuthorizationV1_3:
    return build_real_execution_authorization_v1_3(
        _write(tmp_path / "local.json", _local()),
        _write(tmp_path / "pii.json", _pii()),
        _write(tmp_path / "preflight.json", _preflight(performed_at)),
        _write(tmp_path / "execution.json", _execution()),
        expected_runner_checkpoint=RUNNER,
        now_utc=now,
    )


def _temp_archive(contents: bytes) -> Path:
    root = Path(tempfile.mkdtemp(prefix="unclaimed-ny-osc-gate2-seventh-"))
    path = root / "FINDERS.zip"
    path.write_bytes(contents)
    return path


def test_builder_requires_four_fresh_attempt7_bindings(tmp_path: Path) -> None:
    now = datetime(2026, 9, 21, 20, 5, tzinfo=UTC)
    authorization = _build(
        tmp_path,
        performed_at=now - timedelta(minutes=5),
        now=now,
    )

    assert authorization.contract_version == "1.3.0"
    assert authorization.mode == "AUTHORIZED_REAL_ONCE"
    assert authorization.attempt_number == 7
    assert authorization.seventh_transient_local_approval_ref == "seventh-local-ref"
    assert authorization.seventh_transient_pii_approval_ref == "seventh-pii-ref"
    assert authorization.seventh_fresh_preflight_receipt_ref == "seventh-preflight-ref"
    assert authorization.seventh_execution_authorization_ref == "seventh-execution-ref"
    assert authorization.runner_checkpoint == RUNNER
    assert authorization.downloads_max == 1
    assert authorization.retries_max == 0
    assert authorization.direct_network_client_allowed is False


def test_builder_rejects_stale_preflight(tmp_path: Path) -> None:
    now = datetime(2026, 9, 21, 20, 30, tzinfo=UTC)

    with pytest.raises(ValueError, match="stale or future-dated"):
        _build(
            tmp_path,
            performed_at=now - timedelta(minutes=16),
            now=now,
        )


def test_builder_rejects_execution_preflight_ref_mismatch(tmp_path: Path) -> None:
    now = datetime(2026, 9, 21, 20, 5, tzinfo=UTC)
    execution = _execution()
    execution["fresh_preflight_receipt_ref"] = "wrong-preflight-ref"

    with pytest.raises(ValueError, match="preflight receipt binding mismatch"):
        build_real_execution_authorization_v1_3(
            _write(tmp_path / "local.json", _local()),
            _write(tmp_path / "pii.json", _pii()),
            _write(tmp_path / "preflight.json", _preflight(now)),
            _write(tmp_path / "execution.json", execution),
            expected_runner_checkpoint=RUNNER,
            now_utc=now,
        )


def test_v1_4_real_capable_runtime_discovers_synthetic_raw14_without_owner_output(
    tmp_path: Path,
) -> None:
    now = datetime(2026, 9, 21, 20, 5, tzinfo=UTC)
    authorization = _build(tmp_path, performed_at=now, now=now)
    payload = (
        _row(address1='"1 Synthetic Street')
        + "\n"
        + _row(owner_name="Synthetic Owner Beta", address1="2 Synthetic Street")
        + "\n"
    ).encode()
    archive = _temp_archive(_zip_payload(payload))

    result = execute_transient_local_file_discovery_v1_4(authorization, archive)

    assert result.contract_version == "1.4.0"
    assert result.execution_mode == "AUTHORIZED_REAL_ONCE"
    assert result.attempt_number == 7
    assert result.status == "DISCOVERED"
    assert result.reason_code == "DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED"
    assert result.runner_checkpoint == RUNNER
    assert result.execution_authorization_ref == "seventh-execution-ref"
    assert result.execution_authorization_consumption_provenance == {
        "single_use": True,
        "reusable": False,
        "retry_authorized": False,
        "consumed_by_execution": True,
        "status_after_execution": "CONSUMED_SINGLE_USE_NON_REUSABLE",
        "owner_pii_included": False,
    }
    assert result.quote_dialect_diagnostic is None
    assert archive.exists() is False

    serialized = result.model_dump_json()
    assert "Synthetic Owner Alpha" not in serialized
    assert "Synthetic Owner Beta" not in serialized
    assert "Synthetic Street" not in serialized


def test_v1_4_real_capable_runtime_raw15_stays_fail_closed(tmp_path: Path) -> None:
    now = datetime(2026, 9, 21, 20, 5, tzinfo=UTC)
    authorization = _build(tmp_path, performed_at=now, now=now)
    archive = _temp_archive(
        _zip_payload((_row(owner_name='"Synthetic | Owner"') + "\n").encode())
    )

    result = execute_transient_local_file_discovery_v1_4(authorization, archive)

    assert result.status == "BLOCKED"
    assert result.reason_code == "UNEXPECTED_DATA_FIELD_COUNT"
    assert result.structural_diagnostic is not None
    assert result.quote_dialect_diagnostic is None
    assert archive.exists() is False


def test_v1_4_module_has_no_cli_or_network_client() -> None:
    import unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution_v1_4 as runtime

    source = Path(runtime.__file__).read_text(encoding="utf-8").lower()

    assert "def main(" not in source
    assert "argparse" not in source
    assert "httpx" not in source
    assert "requests" not in source
    assert "urllib.request" not in source
