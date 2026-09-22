from __future__ import annotations

import io
import json
import tempfile
import zipfile
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError
from referencing import Registry, Resource

from unclaimed_platform.adapters.sources.ny_owner_name_schema_discovery import (
    NY_DOCUMENTED_FIELDS,
)
from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution import (
    NyTransientLocalExecutionAuthorization,
    execute_transient_local_file_discovery,
)

ROOT = Path(__file__).resolve().parents[2]
AUTH_SCHEMA = (
    ROOT / "schemas" / "agents" / "ny_transient_local_execution_authorization.schema.json"
)
RESULT_SCHEMA_V1_0 = (
    ROOT / "schemas" / "agents" / "ny_transient_local_execution_result.schema.json"
)
RESULT_SCHEMA_V1_1 = (
    ROOT
    / "schemas"
    / "agents"
    / "ny_transient_local_execution_result_v1_1.schema.json"
)
DISCOVERY_RESULT_SCHEMA = (
    ROOT / "schemas" / "agents" / "ny_owner_name_schema_discovery_result.schema.json"
)
DIAGNOSTIC_RESULT_SCHEMA = (
    ROOT / "schemas" / "agents" / "ny_owner_name_structural_diagnostic_result.schema.json"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _archive() -> bytes:
    row = "|".join(
        [
            "1",
            "IN03",
            "Synthetic description",
            "1",
            "Synthetic Owner",
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
    payload = ("|".join(NY_DOCUMENTED_FIELDS) + "\n" + row + "\n").encode("utf-8")
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("owner_names.txt", payload)
    return buffer.getvalue()


def test_transient_local_contracts_validate_and_do_not_expose_raw_path() -> None:
    root = Path(tempfile.mkdtemp(prefix="unclaimed-ny-osc-gate2-"))
    archive_path = root / "FINDERS.zip"
    archive_path.write_bytes(_archive())

    authorization = NyTransientLocalExecutionAuthorization(
        mode="SYNTHETIC_TEST",
        local_file_approval_ref="synthetic-local",
        gate2_approval_ref="synthetic-gate2",
        local_file_approval_granted=True,
        gate2_approval_granted=True,
        max_download_bytes=100_000,
        max_uncompressed_bytes=100_000,
        max_archive_members=1,
    )
    result = execute_transient_local_file_discovery(authorization, archive_path)

    auth_schema = _load(AUTH_SCHEMA)
    result_schema_v1_0 = _load(RESULT_SCHEMA_V1_0)
    result_schema_v1_1 = _load(RESULT_SCHEMA_V1_1)
    discovery_schema = _load(DISCOVERY_RESULT_SCHEMA)
    diagnostic_schema = _load(DIAGNOSTIC_RESULT_SCHEMA)
    registry = Registry().with_resource(
        str(discovery_schema["$id"]),
        Resource.from_contents(discovery_schema),
    ).with_resource(
        str(diagnostic_schema["$id"]),
        Resource.from_contents(diagnostic_schema),
    )

    Draft202012Validator(auth_schema).validate(authorization.model_dump(mode="json"))
    Draft202012Validator(result_schema_v1_1, registry=registry).validate(
        result.model_dump(mode="json")
    )
    assert result_schema_v1_0["$id"].endswith(":1.0.0")
    assert result_schema_v1_1["$id"].endswith(":1.1.0")
    assert "structural_diagnostic" not in result_schema_v1_0["properties"]
    assert "archive_path" not in result_schema_v1_1["properties"]
    assert result.contract_version == "1.1.0"
    assert result.structural_diagnostic is None
    assert result.local_file_deleted is True


def test_v1_1_contract_requires_diagnostic_for_field_count_block() -> None:
    values = [
        "1",
        "IN03",
        "Synthetic description",
        "1",
        '"Synthetic Owner',
        '1 Synthetic Street"',
        "",
        "",
        "Albany",
        "NY",
        "12207-0000",
        "USA",
        "Synthetic Holder",
        "2026",
    ]
    payload = ("|".join(values) + "\n").encode("utf-8")
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("owner_names.txt", payload)

    root = Path(tempfile.mkdtemp(prefix="unclaimed-ny-osc-gate2-"))
    archive_path = root / "FINDERS.zip"
    archive_path.write_bytes(buffer.getvalue())

    authorization = NyTransientLocalExecutionAuthorization(
        mode="SYNTHETIC_TEST",
        local_file_approval_ref="synthetic-local",
        gate2_approval_ref="synthetic-gate2",
        local_file_approval_granted=True,
        gate2_approval_granted=True,
        max_download_bytes=100_000,
        max_uncompressed_bytes=100_000,
        max_archive_members=1,
    )
    result = execute_transient_local_file_discovery(authorization, archive_path)

    result_schema = _load(RESULT_SCHEMA_V1_1)
    discovery_schema = _load(DISCOVERY_RESULT_SCHEMA)
    diagnostic_schema = _load(DIAGNOSTIC_RESULT_SCHEMA)
    registry = Registry().with_resource(
        str(discovery_schema["$id"]),
        Resource.from_contents(discovery_schema),
    ).with_resource(
        str(diagnostic_schema["$id"]),
        Resource.from_contents(diagnostic_schema),
    )

    payload_json = result.model_dump(mode="json")
    Draft202012Validator(result_schema, registry=registry).validate(payload_json)

    assert result.reason_code == "UNEXPECTED_DATA_FIELD_COUNT"
    assert result.structural_diagnostic is not None
    assert result.structural_diagnostic.raw_pipe_count == 13
    assert result.structural_diagnostic.structural_pipe_count == 12
    assert result.structural_diagnostic.suppressed_pipe_count == 1

    payload_json["structural_diagnostic"] = None
    with pytest.raises(ValidationError):
        Draft202012Validator(result_schema, registry=registry).validate(payload_json)
