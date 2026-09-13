from __future__ import annotations

from pathlib import Path

from unclaimed_platform.adapters.storage import FileSystemRawStore
from unclaimed_platform.core.audit import AuditEventWriter
from unclaimed_platform.core.policy_engine.privacy import (
    ProvenanceContext,
    RawDataGovernanceContext,
    RawDataGovernanceGate,
    RawDataGovernancePolicy,
)


def test_synthetic_raw_storage_smoke(tmp_path: Path) -> None:
    audit = AuditEventWriter()
    policy = RawDataGovernancePolicy(
        policy_id="raw.synthetic.smoke",
        policy_version="1.0.0",
        source_id="synthetic.raw.smoke",
        synthetic_only=True,
        source_approval_required=False,
        authorized_processing_purposes=frozenset({"SYNTHETIC_RAW_STORAGE_SMOKE"}),
        authorized_data_categories=frozenset({"SYNTHETIC_RAW"}),
        allowed_fields=frozenset(),
        authorized_retention_policy_refs=frozenset({"retention://synthetic-smoke/v1"}),
        allow_pii=False,
    )
    store = FileSystemRawStore(
        tmp_path,
        audit_writer=audit,
        governance_gate=RawDataGovernanceGate(policy),
    )
    governance = RawDataGovernanceContext(
        source_id="synthetic.raw.smoke",
        synthetic=True,
        approval_reference=None,
        processing_purpose="SYNTHETIC_RAW_STORAGE_SMOKE",
        data_categories=frozenset({"SYNTHETIC_RAW"}),
        requested_fields=frozenset(),
        retention_policy_ref="retention://synthetic-smoke/v1",
        contains_pii=False,
        pii_required_for_purpose=False,
        retrieved_timestamp_required=True,
        provenance=ProvenanceContext(
            source_uri="mock://synthetic.raw.smoke",
            authority="Synthetic smoke fixture only",
            acquisition_method="MOCK",
            terms_review_ref="docs/audits/M3_RAW_STORAGE_PRIVACY_REUSE_FIRST.md",
            retrieved_at="2026-09-13T16:00:00Z",
            source_revision="synthetic-smoke-v1",
        ),
    )
    payload = b"synthetic smoke artifact\n"

    record = store.persist(
        content=payload,
        content_type="application/octet-stream",
        governance=governance,
        synthetic=True,
        expected_byte_count=len(payload),
        expected_content_types=("application/octet-stream",),
    )

    assert store.read(record) == payload
    assert store.load_record(record.content_hash, record.record_hash) == record
    assert audit.verify_chain()
    assert audit.events[-1].event_type == "RAW_ARTIFACT_PERSISTED"
