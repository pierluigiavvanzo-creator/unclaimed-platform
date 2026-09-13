from __future__ import annotations

from hashlib import sha256

from .contracts import (
    AcquisitionMethod,
    AcquisitionMode,
    AcquisitionProvenance,
    AcquisitionRequest,
    AcquisitionResult,
    AcquisitionStatus,
    RawArtifact,
)

M3_TERMS_REVIEW_REF = "docs/audits/M3_CALIFORNIA_SOURCE_READINESS.md"


class DeferredMockSourceAdapter:
    """Deterministic mock adapter for deferred California sources."""

    def __init__(self, source_id: str, *, payload: bytes = b'{"synthetic":true}\n') -> None:
        self.source_id = source_id
        self._payload = payload

    def acquire(self, request: AcquisitionRequest) -> AcquisitionResult:
        if request.source_id != self.source_id:
            raise ValueError(f"request source_id {request.source_id!r} does not match adapter")

        if request.mode is AcquisitionMode.MOCK and len(self._payload) > request.max_bytes:
            return AcquisitionResult(
                schema_version="1.0.0",
                request_id=request.request_id,
                source_id=self.source_id,
                jurisdiction="CA",
                status=AcquisitionStatus.BLOCKED,
                reason_code="BYTE_BUDGET_EXCEEDED",
                reason="Synthetic payload exceeds the request byte budget.",
                artifact=None,
                provenance=AcquisitionProvenance(
                    source_uri=f"mock://{self.source_id}",
                    authority="Synthetic test fixture only",
                    acquisition_method=AcquisitionMethod.MOCK,
                    retrieved_at=None,
                    terms_review_ref=M3_TERMS_REVIEW_REF,
                    source_revision="synthetic-v1",
                    access_notes="No external access performed.",
                ),
            )

        if request.mode is not AcquisitionMode.MOCK:
            return AcquisitionResult(
                schema_version="1.0.0",
                request_id=request.request_id,
                source_id=self.source_id,
                jurisdiction="CA",
                status=AcquisitionStatus.BLOCKED,
                reason_code="DEFERRED_SOURCE_MOCK_ONLY",
                reason="This source is deferred and may only be represented by synthetic fixtures.",
                artifact=None,
                provenance=AcquisitionProvenance(
                    source_uri=f"mock://{self.source_id}",
                    authority="Synthetic test fixture only",
                    acquisition_method=AcquisitionMethod.MOCK,
                    retrieved_at=None,
                    terms_review_ref=M3_TERMS_REVIEW_REF,
                    source_revision="synthetic-v1",
                    access_notes="No external access performed.",
                ),
            )

        digest = sha256(self._payload).hexdigest()
        return AcquisitionResult(
            schema_version="1.0.0",
            request_id=request.request_id,
            source_id=self.source_id,
            jurisdiction="CA",
            status=AcquisitionStatus.MOCKED,
            reason_code="SYNTHETIC_FIXTURE",
            reason="Synthetic fixture emitted for contract testing.",
            artifact=RawArtifact(
                storage_ref=f"mock/raw/{digest}",
                content_hash=digest,
                byte_count=len(self._payload),
                content_type="application/json",
                immutable_raw=True,
                synthetic=True,
            ),
            provenance=AcquisitionProvenance(
                source_uri=f"mock://{self.source_id}",
                authority="Synthetic test fixture only",
                acquisition_method=AcquisitionMethod.MOCK,
                retrieved_at=request.requested_at,
                terms_review_ref=M3_TERMS_REVIEW_REF,
                source_revision="synthetic-v1",
                access_notes="No real PII or external access performed.",
            ),
        )
