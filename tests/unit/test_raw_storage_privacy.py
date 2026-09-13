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
    RawDataGovernancePolicy,
)


def policy(
    *,
    source_id: str = "synthetic.raw.source",
    synthetic_only: bool = True,
    source_approval_required: bool = False,
    authorized_processing_purposes: frozenset[str] | None = None,
    authorized_data_categories: frozenset[str] | None = None,
    allowed_fields: frozenset[str] | None = None,
    authorized_retention_policy_refs: frozenset[str] | None = None,
    allow_pii: bool = False,
) -> RawDataGovernancePolicy:
    return RawDataGovernancePolicy(
        policy_id="raw.synthetic.test",
        policy_version="1.0.0",
        source_id=source_id,
        synthetic_only=synthetic_only,
        source_approval_required=source_approval_required,
        authorized_processing_purposes=authorized_processing_purposes
        or frozenset({"SYNTHETIC_RAW_STORAGE_TEST"}),
        authorized_data_categories=authorized_data_categories or frozenset({"SYNTHETIC_RAW"}),
        allowed_fields=allowed_fields or frozenset({"synthetic_marker"}),
        authorized_retention_policy_refs=authorized_retention_policy_refs
        or frozenset({"retention://synthetic-test/v1"}),
        allow_pii=allow_pii,
    )


def governance(
    *,
    synthetic: bool = True,
    approval_reference: str | None = None,
    provenance: ProvenanceContext | None = None,
    processing_purpose: str = "SYNTHETIC_RAW_STORAGE_TEST",
    data_categories: frozenset[str] | None = None,
    requested_fields: frozenset[str] | None = None,
    retention_policy_ref: str | None = "retention://synthetic-test/v1",
    contains_pii: bool = False,
    pii_required_for_purpose: bool = False,
) -> RawDataGovernanceContext:
    categories = data_categories or frozenset({"SYNTHETIC_RAW"})
    fields = requested_fields or frozenset({"synthetic_marker"})
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
        approval_reference=approval_reference,
        processing_purpose=processing_purpose,
        data_categories=categories,
        requested_fields=fields,
        retention_policy_ref=retention_policy_ref,
        contains_pii=contains_pii,
        pii_required_for_purpose=pii_required_for_purpose,
        retrieved_timestamp_required=True,
        provenance=provenance if provenance is not None else default_provenance,
    )


def store(
    tmp_path: Path,
    audit: AuditEventWriter | None = None,
    governance_policy: RawDataGovernancePolicy | None = None,
) -> FileSystemRawStore:
    gate = RawDataGovernanceGate(governance_policy or policy())
    return FileSystemRawStore(tmp_path, audit_writer=audit or AuditEventWriter(), governance_gate=gate)


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
    assert first.record_ref.endswith(f"{first.record_hash}.json")
    assert first.governance_policy_id == "raw.synthetic.test"
    assert raw_store.read(first) == payload
    assert raw_store.load_record(first.content_hash, first.record_hash) == first
    assert len(audit.events) == 1
    assert audit.events[0].event_type == "RAW_ARTIFACT_PERSISTED"
    assert audit.verify_chain()


def test_same_raw_bytes_accept_append_only_distinct_provenance(tmp_path: Path) -> None:
    audit = AuditEventWriter()
    raw_store = store(tmp_path, audit)
    payload = b"same-synthetic-raw"
    first = raw_store.persist(
        content=payload,
        content_type="application/octet-stream",
        governance=governance(),
        synthetic=True,
    )
    second_context = replace(
        governance(),
        provenance=replace(
            governance().provenance,
            retrieved_at="2026-09-13T16:01:00Z",
            source_revision="synthetic-v2",
        )
        if governance().provenance is not None
        else None,
    )
    second = raw_store.persist(
        content=payload,
        content_type="application/octet-stream",
        governance=second_context,
        synthetic=True,
    )

    assert first.storage_ref == second.storage_ref
    assert first.content_hash == second.content_hash
    assert first.record_hash != second.record_hash
    assert first.record_ref != second.record_ref
    assert raw_store.read(first) == payload
    assert raw_store.read(second) == payload
    assert len(audit.events) == 2
    assert audit.events[1].previous_event_hash == audit.events[0].event_hash
    assert audit.verify_chain()


def test_existing_raw_artifact_tampering_is_detected_and_rejected(tmp_path: Path) -> None:
    raw_store = store(tmp_path)
    payload = b"synthetic-original"
    record = raw_store.persist(
        content=payload,
        content_type="application/octet-stream",
        governance=governance(),
        synthetic=True,
    )

    (tmp_path / record.storage_ref).write_bytes(b"synthetic-tampered")

    with pytest.raises(ImmutableArtifactError) as read_error:
        raw_store.read(record)
    assert read_error.value.reason_code == "IMMUTABLE_ARTIFACT_CORRUPTED"

    with pytest.raises(ImmutableArtifactError) as persist_error:
        raw_store.persist(
            content=payload,
            content_type="application/octet-stream",
            governance=governance(),
            synthetic=True,
        )
    assert persist_error.value.reason_code == "IMMUTABLE_ARTIFACT_MODIFICATION_REJECTED"


def test_existing_provenance_record_cannot_be_overwritten(tmp_path: Path) -> None:
    raw_store = store(tmp_path)
    record = raw_store.persist(
        content=b"synthetic-record",
        content_type="application/octet-stream",
        governance=governance(),
        synthetic=True,
    )
    (tmp_path / record.record_ref).write_text("{}\n", encoding="utf-8")

    with pytest.raises(ImmutableArtifactError) as error:
        raw_store.persist(
            content=b"synthetic-record",
            content_type="application/octet-stream",
            governance=governance(),
            synthetic=True,
        )

    assert error.value.reason_code == "IMMUTABLE_PROVENANCE_MODIFICATION_REJECTED"


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


def test_missing_trusted_privacy_policy_fails_closed(tmp_path: Path) -> None:
    raw_store = FileSystemRawStore(tmp_path, audit_writer=AuditEventWriter())

    with pytest.raises(RawStoragePolicyError) as error:
        raw_store.persist(
            content=b"synthetic",
            content_type="application/octet-stream",
            governance=governance(),
            synthetic=True,
        )

    assert error.value.reason_code == "PRIVACY_POLICY_REQUIRED"


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


def test_real_artifact_requires_real_capable_policy_and_source_approval(tmp_path: Path) -> None:
    real_capable_policy = policy(synthetic_only=False)
    raw_store = store(tmp_path, governance_policy=real_capable_policy)
    context = governance(synthetic=False, approval_reference=None)

    with pytest.raises(RawStoragePolicyError) as error:
        raw_store.persist(
            content=b"synthetic-placeholder-no-real-data",
            content_type="application/octet-stream",
            governance=context,
            synthetic=False,
        )

    assert error.value.reason_code == "SOURCE_APPROVAL_REQUIRED"


def test_synthetic_only_policy_blocks_real_marker_before_storage(tmp_path: Path) -> None:
    raw_store = store(tmp_path)
    context = governance(synthetic=False, approval_reference="approval-placeholder")

    with pytest.raises(RawStoragePolicyError) as error:
        raw_store.persist(
            content=b"synthetic-placeholder-no-real-data",
            content_type="application/octet-stream",
            governance=context,
            synthetic=False,
        )

    assert error.value.reason_code == "REAL_DATA_NOT_AUTHORIZED"


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


def test_unapproved_retention_policy_fails_closed(tmp_path: Path) -> None:
    raw_store = store(tmp_path)
    context = governance(retention_policy_ref="retention://not-authorized/v1")

    with pytest.raises(RawStoragePolicyError) as error:
        raw_store.persist(
            content=b"synthetic",
            content_type="application/octet-stream",
            governance=context,
            synthetic=True,
        )

    assert error.value.reason_code == "RETENTION_POLICY_NOT_AUTHORIZED"


def test_unauthorized_processing_purpose_fails_closed(tmp_path: Path) -> None:
    raw_store = store(tmp_path)
    context = governance(processing_purpose="OTHER_PURPOSE")

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
    )
    with pytest.raises(RawStoragePolicyError) as field_error:
        raw_store.persist(
            content=b"synthetic",
            content_type="application/octet-stream",
            governance=field_context,
            synthetic=True,
        )
    assert field_error.value.reason_code == "FIELD_SCOPE_NOT_MINIMIZED"


def test_unnecessary_pii_fails_closed_even_when_policy_allows_pii(tmp_path: Path) -> None:
    raw_store = store(tmp_path, governance_policy=policy(allow_pii=True))
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
    gate = RawDataGovernanceGate(policy())
    context = governance(retention_policy_ref=None)

    first = gate.evaluate(context)
    second = gate.evaluate(context)

    assert first == second
    assert first.reason_code == "RETENTION_POLICY_REQUIRED"
