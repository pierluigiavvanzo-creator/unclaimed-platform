from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[2]


def load_schema() -> dict[str, object]:
    return json.loads(
        (ROOT / "schemas/agents/a01_raw_artifact_record.schema.json").read_text(
            encoding="utf-8"
        )
    )


def valid_record() -> dict[str, object]:
    content_hash = "a" * 64
    record_hash = "b" * 64
    return {
        "schema_version": "1.0.0",
        "storage_ref": f"raw/sha256/aa/aa/{content_hash}",
        "record_ref": f"provenance/sha256/aa/aa/{content_hash}/{record_hash}.json",
        "content_hash": content_hash,
        "record_hash": record_hash,
        "byte_count": 21,
        "content_type": "application/json",
        "source_id": "synthetic.raw.source",
        "source_uri": "mock://synthetic.raw.source",
        "authority": "Synthetic test fixture only",
        "acquisition_method": "MOCK",
        "retrieved_at": "2026-09-13T16:00:00Z",
        "source_revision": "synthetic-v1",
        "approval_reference": None,
        "terms_review_ref": "docs/audits/M3_RAW_STORAGE_PRIVACY_REUSE_FIRST.md",
        "retention_policy_ref": "retention://synthetic-test/v1",
        "processing_purpose": "SYNTHETIC_RAW_STORAGE_TEST",
        "governance_policy_id": "raw.synthetic.test",
        "governance_policy_version": "1.0.0",
        "data_categories": ["SYNTHETIC_RAW"],
        "requested_fields": ["synthetic_marker"],
        "provenance_metadata": {"fixture": "contract-test"},
        "synthetic": True,
        "immutable": True,
    }


def test_raw_artifact_record_schema_accepts_minimized_synthetic_record() -> None:
    schema = load_schema()
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    validator.validate(valid_record())


def test_raw_artifact_record_schema_rejects_mutable_record() -> None:
    schema = load_schema()
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    payload = valid_record()
    payload["immutable"] = False

    with pytest.raises(ValidationError):
        validator.validate(payload)


def test_raw_artifact_record_schema_requires_retention_policy() -> None:
    schema = load_schema()
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    payload = valid_record()
    del payload["retention_policy_ref"]

    with pytest.raises(ValidationError):
        validator.validate(payload)


def test_raw_artifact_record_schema_requires_governance_policy_version() -> None:
    schema = load_schema()
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    payload = valid_record()
    del payload["governance_policy_version"]

    with pytest.raises(ValidationError):
        validator.validate(payload)
