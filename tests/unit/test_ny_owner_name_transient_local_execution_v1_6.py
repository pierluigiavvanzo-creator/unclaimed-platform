from __future__ import annotations

import zipfile
from pathlib import Path

from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution_v1_6 import (
    NyTransientLocalExecutionAuthorizationV1_5,
    execute_transient_local_file_discovery_v1_6,
)

RUNNER = "b" * 40


def _authorization() -> NyTransientLocalExecutionAuthorizationV1_5:
    return NyTransientLocalExecutionAuthorizationV1_5(
        ninth_transient_local_approval_ref="ninth-local-ref",
        ninth_transient_pii_approval_ref="ninth-pii-ref",
        ninth_fresh_preflight_receipt_ref="ninth-preflight-ref",
        ninth_execution_authorization_ref="ninth-execution-ref",
        authorized_download_started_at_utc="2026-09-22T16:16:25Z",
        local_file_approval_granted=True,
        transient_pii_approval_granted=True,
        fresh_preflight_exact_match=True,
        execution_authorization_granted=True,
        runner_checkpoint=RUNNER,
    )


def _archive(tmp_path: Path, payload: bytes) -> Path:
    path = tmp_path / "FINDERS.zip"
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("owner_names.txt", payload)
    return path


def _row(*, trailing_pipe: bool, extra: bytes = b"") -> bytes:
    fields = [str(index).encode("ascii") for index in range(14)]
    value = b"|".join(fields)
    if trailing_pipe:
        value += b"|"
    return value + extra + b"\n"


def test_attempt9_confirms_terminal_delimiter_and_deletes_archive(
    tmp_path: Path,
) -> None:
    archive = _archive(tmp_path, _row(trailing_pipe=True))

    result = execute_transient_local_file_discovery_v1_6(
        _authorization(),
        archive,
    )

    assert result.status == "DISCOVERED"
    assert (
        result.reason_code
        == "DOCUMENTED_14_FIELDS_WITH_TERMINAL_DELIMITER_CONFIRMED"
    )
    assert result.structural_normalization_allowed is True
    assert result.terminal_empty_field_ignored_for_structural_width is True
    assert result.normalized_documented_field_count == 14
    assert archive.exists() is False
    assert result.local_file_deleted is True
    assert result.no_owner_values_returned is True


def test_attempt9_blocks_nonempty_fifteenth_field_and_deletes_archive(
    tmp_path: Path,
) -> None:
    archive = _archive(
        tmp_path,
        _row(trailing_pipe=True, extra=b"EXTRA"),
    )

    result = execute_transient_local_file_discovery_v1_6(
        _authorization(),
        archive,
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "TRAILING_DELIMITER_HYPOTHESIS_NOT_CONFIRMED"
    assert result.structural_normalization_allowed is False
    assert archive.exists() is False


def test_gate9_runner_uses_dedicated_python_entrypoint_not_python_c() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    runner = repo_root / "scripts" / "ny_osc_gate9_transient_local.ps1"
    source = runner.read_text(encoding="utf-8").lower()

    assert "ny_osc_gate9_execute.py" in source
    assert "python -c" not in source
    assert "invoke-webrequest" not in source
    assert "invoke-restmethod" not in source
    assert "start-bitstransfer" not in source
    assert "retries_max -ne 0" in source
    assert "one_bound_gate9_execution" in source
