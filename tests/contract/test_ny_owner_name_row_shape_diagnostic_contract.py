from __future__ import annotations

import io
import json
import zipfile
from pathlib import Path

from jsonschema import Draft202012Validator

from unclaimed_platform.adapters.sources.ny_owner_name_row_shape_diagnostic import (
    NyOwnerNameRowShapeDiagnosticAuthorization,
    diagnose_ny_owner_name_row_shape,
)

ROOT = Path(__file__).resolve().parents[2]
AUTH_SCHEMA = (
    ROOT
    / "schemas/agents/ny_owner_name_row_shape_diagnostic_authorization.schema.json"
)
RESULT_SCHEMA = (
    ROOT
    / "schemas/agents/ny_owner_name_row_shape_diagnostic_result.schema.json"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_row_shape_diagnostic_contract_is_non_pii() -> None:
    line = b"|".join([b"x"] * 14)
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("owner_names.txt", line + b"\n")

    authorization = NyOwnerNameRowShapeDiagnosticAuthorization(
        mode="SYNTHETIC_TEST",
        approval_id="synthetic-row-shape-diagnostic",
        max_download_bytes=100_000,
        max_uncompressed_bytes=100_000,
        max_archive_members=1,
        max_physical_lines_to_scan=10,
    )
    result = diagnose_ny_owner_name_row_shape(authorization, buffer.getvalue())

    Draft202012Validator(_load(AUTH_SCHEMA)).validate(
        authorization.model_dump(mode="json")
    )
    Draft202012Validator(_load(RESULT_SCHEMA)).validate(result.model_dump(mode="json"))

    serialized = result.model_dump_json()
    assert "owner_name" not in serialized.lower()
    assert "owner_address" not in serialized.lower()
