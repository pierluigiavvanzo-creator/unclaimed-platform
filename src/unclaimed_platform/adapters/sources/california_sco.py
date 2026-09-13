from __future__ import annotations

from .contracts import (
    AcquisitionMethod,
    AcquisitionMode,
    AcquisitionProvenance,
    AcquisitionRequest,
    AcquisitionResult,
    AcquisitionStatus,
)

CA_SCO_BULK_SOURCE_ID = "ca.sco.unclaimed_property.bulk"
CA_SCO_DOWNLOAD_PAGE = "https://www.sco.ca.gov/upd_download_property_records.html"
M3_TERMS_REVIEW_REF = "docs/audits/M3_CALIFORNIA_SOURCE_READINESS.md"


class CaliforniaSCOBulkAdapter:
    """Fail-closed boundary for the California SCO public bulk download.

    M3 contract work intentionally does not implement network retrieval. Even after a source
    approval flag is supplied, acquisition remains blocked until a later task implements and tests
    bounded retrieval, immutable raw storage, and privacy controls.
    """

    source_id = CA_SCO_BULK_SOURCE_ID

    def __init__(self, *, approved_for_use: bool = False) -> None:
        self._approved_for_use = approved_for_use

    def acquire(self, request: AcquisitionRequest) -> AcquisitionResult:
        if request.source_id != self.source_id:
            raise ValueError(f"request source_id {request.source_id!r} does not match adapter")

        if request.mode is not AcquisitionMode.REAL:
            return self._blocked(
                request,
                "REAL_SOURCE_REQUIRES_REAL_MODE",
                "California SCO bulk acquisition requires an explicit REAL request.",
            )

        if request.acquisition_scope != "RAW_INGEST_ONLY":
            return self._blocked(
                request,
                "SCOPE_NOT_ALLOWED",
                "M3 permits raw-ingest-only acquisition; downstream matching is out of scope.",
            )

        if not self._approved_for_use or not request.approval_id:
            return self._blocked(
                request,
                "REAL_SOURCE_NOT_APPROVED",
                "Real acquisition is blocked until explicit source approval is recorded.",
            )

        return self._blocked(
            request,
            "REAL_NETWORK_ACQUISITION_NOT_IMPLEMENTED",
            (
                "The adapter boundary is defined, but network retrieval is intentionally "
                "not implemented."
            ),
        )

    def _blocked(
        self,
        request: AcquisitionRequest,
        reason_code: str,
        reason: str,
    ) -> AcquisitionResult:
        return AcquisitionResult(
            schema_version="1.0.0",
            request_id=request.request_id,
            source_id=self.source_id,
            jurisdiction="CA",
            status=AcquisitionStatus.BLOCKED,
            reason_code=reason_code,
            reason=reason,
            artifact=None,
            provenance=AcquisitionProvenance(
                source_uri=CA_SCO_DOWNLOAD_PAGE,
                authority="California State Controller's Office",
                acquisition_method=AcquisitionMethod.OFFICIAL_BULK_DOWNLOAD,
                retrieved_at=None,
                terms_review_ref=M3_TERMS_REVIEW_REF,
                source_revision=None,
                access_notes="Boundary only; no network access performed.",
            ),
        )
