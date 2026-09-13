from __future__ import annotations

from dataclasses import replace
from pathlib import Path

import pytest

from unclaimed_platform.adapters.storage.raw import (
    FileSystemRawStore,
    ImmutableArtifactError,
    RawStoragePolicyError,
    RawStorageValidationError,
)
from unclaimed_platform.core.audit import AuditEventWriter
from unclaimed_platform.core.policy_engine.privacy import (
    ProvenanceContext,
    RawDataGovernanceContext,
    RawDataGovernanceGate,
)


def governance(
    *,
    synthetic: bool = True,
    approval_required: bool = False,
    approval_reference: str | None = None,
    provenance: ProvenanceContext | None = None,
    processing_purpose: str = "SYNTHETIC_RAW_STORAGE_TEST",
    authorized_processing_purposes: frozenset[str] | None = None,
    data_categories: frozenset[str] | None = None,
    authorized_data_categories: frozenset[str] | None = None,
    requested_fields: frozenset[str] | None = None,
    allowed_fields: frozenset[str] | None = None,
    retention_policy_ref: str | None = "retention://synthetic-test/v1",
    contains_pii: bool = False,
    pii_required_for_purpose: bool = False,
) -> RawDataGovernanceContext:
    purpose_set = authorized_processing_purposes or frozenset({processing_purpose})
    categories = data_categories or frozenset({"SYNTHETIC_RAW"})
    authorized_categories = authorized_data_categories or frozenset({"SYNTHETIC_RAW"})
    fields = requested_fields or frozenset({"synthetic_marker"})
    minimized_fields = allowed_fields or frozenset({"synthetic_marker"})
    default_provenance = ProvenanceContext(
        source_uri="mock://synthetic.raw.source",
        authority="Synthetic test fixture only",
        acquisition_method="MOCK",
        terms_review_ref="docs/audits/M3_RAW_STORAGE_PRIVACY_REUSE_FIRST.md",
        retrieved_at="2026-09-13T16:00:00Z",
        source_revision="synthetic-v1",
    )
    return RawDataGovernanceContext(
        source_id="synthetic.raw.source",
        synthetic=synthetic,
        source_approval_required=approval_required,
        approval_reference=approval_reference,
        processing_purpose=processing_purpose,
        authorized_processing_purposes=purpose_set,
        data_categories=categories,
        authorized_data_categories=authorized_categories,
        requested_fields=fields,
        allowed_fields=minimized_fields,
        retention_policy_ref=retention_policy_ref,
        contains_pii=contains_pii,
        pii_required_for_purpose=pii_required_for_purpose,
        retrieved_timestamp_required=True,
        provenance=provenance if provenance is not None else default_provenance,
    )


def store(tmp_path: Path, audit: AuditEventWriter | None = None) -> FileSystemRawStore:
    return FileSystemRawStore(tmp_path, audit_writer=audit or AuditEventWriter())


def test_synthetic_artifact_happy_path_is_immutable_deterministic_and_audited(
    tmp_path: Path,
) -> None:
    audit = AuditEventWriter()
    raw_store = store(tmp_path, audit)
    payload = b'{"synthetic":true}\n'

    first = raw_store.persist(
        content=payload,
        content_type="application/json",
        governance=governance(),
        synthetic=True,
        expected_byte_count=len(payload),
        expected_content_types=("application/json",),
        provenance_metadata={"fixture": "unit-test"},
    )
    second = raw_store.persist(
        content=payload,
        content_type="application/json",
        governance=governance(),
        synthetic=True,
        expected_byte_count=len(payload),
        expected_content_types=("application/json",),
        provenance_metadata={"fixture": "unit-test"},
    )

    assert first == second
    assert first.immutable is True
    assert first.synthetic is True
    assert first.storage_ref.endswith(first.content_hash)
    assert raw_store.read(first) == payload
    assert raw_store.load_record(first.content_hash) == first
    assert len(audit.events) == 1
    assert audit.events[0].event_type == "RAW_ARTIFACT_PERSISTED"
    assert audit.verify_chain()


def test_existing_raw_artifact_tampering_is_detected(tmp_path: Path) -> None:
    raw_store = store(tmp_path)
    record = raw_store.persist(
        content=b"synthetic-original",
        content_type="application/octet-stream",
        governance=governance(),
        synthetic=True,
    )

    (tmp_path / record.storage_ref).write_bytes(b"synthetic-tampered")

    with pytest.raises(ImmutableArtifactError) as error:
        raw_store.read(record)

    assert error.value.reason_code == "IMMUTABLE_ARTIFACT_CORRUPTED"


def test_existing_manifest_cannot_be_rewritten_for_same_content(tmp_path: Path) -> None:
    raw_store = store(tmp_path)
    payload = b"same-raw-bytes"
    raw_store.persist(
        content=payload,
        content_type="application/octet-stream",
        governance=governance(),
        synthetic=True,
    )
    changed = replace(
        governance(),
        processing_purpose="SECOND_AUTHORIZED_PURPOSE",
        authorized_processing_purposes=frozenset({"SECOND_AUTHORIZED_PURPOSE"}),
    )

    with pytest.raises(ImmutableArtifactError) as error:
        raw_store.persist(
            content=payload,
            content_type="application/octet-stream",
            governance=changed,
            synthetic=True,
        )

    assert error.value.reason_code == "IMMUTABLE_METADATA_MODIFICATION_REJECTED"


def test_byte_count_and_content_type_are_validated(tmp_path: Path) -> None:
    raw_store = store(tmp_path)

    with pytest.raises(RawStorageValidationError) as byte_error:
        raw_store.persist(
            content=b"123",
            content_type="application/octet-stream",
            governance=governance(),
            synthetic=True,
            expected_byte_count=4,
        )
    assert byte_error.value.reason_code == "BYTE_COUNT_MISMATCH"

    with pytest.raises(RawStorageValidationError) as media_error:
        raw_store.persist(
            content=b"123",
            content_type="application/octet-stream",
            governance=governance(),
            synthetic=True,
            expected_content_types=("application/json",),
        )
    assert media_error.value.reason_code == "CONTENT_TYPE_NOT_ALLOWED"


def test_missing_provenance_fails_closed(tmp_path: Path) -> None:
    raw_store = store(tmp_path)
    context = replace(governance(), provenance=None)

    with pytest.raises(RawStoragePolicyError) as error:
        raw_store.persist(
            content=b"synthetic",
            content_type="application/octet-stream",
            governance=context,
            synthetic=True,
        )

    assert error.value.reason_code == "PROVENANCE_REQUIRED"


def test_real_artifact_requires_source_approval_even_without_optional_flag(tmp_path: Path) -> None:
    raw_store = store(tmp_path)
    context = governance(
        synthetic=False,
        approval_required=False,
        approval_reference=None,
    )

    with pytest.raises(RawStoragePolicyError) as error:
        raw_store.persist(
            content=b"synthetic-placeholder-no-real-data",
            content_type="application/octet-stream",
            governance=context,
            synthetic=False,
        )

    assert error.value.reason_code == "SOURCE_APPROVAL_REQUIRED"


def test_synthetic_marker_mismatch_fails_closed(tmp_path: Path) -> None:
    raw_store = store(tmp_path)

    with pytest.raises(RawStoragePolicyError) as error:
        raw_store.persist(
            content=b"synthetic",
            content_type="application/octet-stream",
            governance=governance(synthetic=True),
            synthetic=False,
        )

    assert error.value.reason_code == "SYNTHETIC_MARKER_MISMATCH"


def test_missing_retention_policy_fails_closed(tmp_path: Path) -> None:
    raw_store = store(tmp_path)
    context = governance(retention_policy_ref=None)

    with pytest.raises(RawStoragePolicyError) as error:
        raw_store.persist(
            content=b"synthetic",
            content_type="application/octet-stream",
            governance=context,
            synthetic=True,
        )

    assert error.value.reason_code == "RETENTION_POLICY_REQUIRED"


def test_unauthorized_processing_purpose_fails_closed(tmp_path: Path) -> None:
    raw_store = store(tmp_path)
    context = governance(authorized_processing_purposes=frozenset({"OTHER_PURPOSE"}))

    with pytest.raises(RawStoragePolicyError) as error:
        raw_store.persist(
            content=b"synthetic",
            content_type="application/octet-stream",
            governance=context,
            synthetic=True,
        )

    assert error.value.reason_code == "PROCESSING_PURPOSE_NOT_AUTHORIZED"


def test_dataset_and_field_scope_must_be_minimized(tmp_path: Path) -> None:
    raw_store = store(tmp_path)
    dataset_context = governance(
        data_categories=frozenset({"SYNTHETIC_RAW", "EXCESS_CATEGORY"}),
        authorized_data_categories=frozenset({"SYNTHETIC_RAW"}),
    )

    with pytest.raises(RawStoragePolicyError) as dataset_error:
        raw_store.persist(
            content=b"synthetic",
            content_type="application/octet-stream",
            governance=dataset_context,
            synthetic=True,
        )
    assert dataset_error.value.reason_code == "DATA_SCOPE_NOT_AUTHORIZED"

    field_context = governance(
        requested_fields=frozenset({"synthetic_marker", "excess_field"}),
        allowed_fields=frozenset({"synthetic_marker"}),
    )
    with pytest.raises(RawStoragePolicyError) as field_error:
        raw_store.persist(
            content=b"synthetic",
            content_type="application/octet-stream",
            governance=field_context,
            synthetic=True,
        )
    assert field_error.value.reason_code == "FIELD_SCOPE_NOT_MINIMIZED"


def test_unnecessary_pii_fails_closed(tmp_path: Path) -> None:
    raw_store = store(tmp_path)
    context = governance(contains_pii=True, pii_required_for_purpose=False)

    with pytest.raises(RawStoragePolicyError) as error:
        raw_store.persist(
            content=b"synthetic-no-real-pii",
            content_type="application/octet-stream",
            governance=context,
            synthetic=True,
        )

    assert error.value.reason_code == "UNNECESSARY_PII"


def test_failure_reason_is_deterministic() -> None:
    gate = RawDataGovernanceGate()
    context = governance(retention_policy_ref=None)

    first = gate.evaluate(context)
    second = gate.evaluate(context)

    assert first == second
    assert first.reason_code == "RETENTION_POLICY_REQUIRED"
