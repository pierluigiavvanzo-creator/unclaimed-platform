from __future__ import annotations

from .contracts import (
    AcquisitionMethod,
    AcquisitionMode,
    AcquisitionProvenance,
    AcquisitionRequest,
    AcquisitionResult,
    AcquisitionStatus,
)

NY_OSC_OWNER_NAME_FILE_SOURCE_ID = "ny.osc.unclaimed_funds.owner_name_file"
NY_OSC_OWNER_NAME_FILE_REQUEST_URL = (
    "https://www.osc.ny.gov/unclaimed-funds/resources/owner-name-file-request-form"
)
NY_SOURCE_CONTRACT_REF = "policies/states/NY/ny_osc_owner_name_file.v1.json"
NY_BENCHMARK_REF = "docs/audits/MVP1_ALTERNATIVE_LAWFUL_REAL_SOURCE_PATHS_BENCHMARK.md"


class NewYorkOSCOwnerNameFileAdapter:
    """Fail-closed boundary for the selected New York OSC Owner Name File candidate.

    This offline adapter intentionally performs no form submission, FTP access, file download,
    parsing, or PII handling. Even with a source approval flag, it remains blocked until the
    first real file has passed a separately authorized memory-only schema-discovery gate.
    """

    source_id = NY_OSC_OWNER_NAME_FILE_SOURCE_ID

    def __init__(self, *, approved_for_use: bool = False) -> None:
        self._approved_for_use = approved_for_use

    def acquire(self, request: AcquisitionRequest) -> AcquisitionResult:
        if request.source_id != self.source_id:
            raise ValueError(f"request source_id {request.source_id!r} does not match adapter")

        if request.jurisdiction != "NY":
            return self._blocked(
                request,
                "JURISDICTION_MISMATCH",
                "The New York OSC Owner Name File requires jurisdiction NY.",
            )

        if request.mode is not AcquisitionMode.REAL:
            return self._blocked(
                request,
                "REAL_SOURCE_REQUIRES_REAL_MODE",
                "The New York OSC Owner Name File requires an explicit REAL request.",
            )

        if request.acquisition_scope != "RAW_INGEST_ONLY":
            return self._blocked(
                request,
                "SCOPE_NOT_ALLOWED",
                "The source boundary permits raw-ingest-only acquisition; downstream identity work is out of scope.",
            )

        if not self._approved_for_use or not request.approval_id:
            return self._blocked(
                request,
                "REAL_SOURCE_NOT_APPROVED",
                "The New York source is candidate-only and real acquisition remains blocked.",
            )

        return self._blocked(
            request,
            "FIRST_FILE_SCHEMA_DISCOVERY_REQUIRED",
            (
                "The source is selected, but the physical file contract has not been observed. "
                "A separately authorized first-file memory-only schema-discovery execution is required."
            ),
        )

    def _blocked(
        self,
        request: AcquisitionRequest,
        reason_code: str,
        reason: str,
    ) -> AcquisitionResult:
        return AcquisitionResult(
            schema_version="1.1.0",
            request_id=request.request_id,
            source_id=self.source_id,
            jurisdiction="NY",
            status=AcquisitionStatus.BLOCKED,
            reason_code=reason_code,
            reason=reason,
            artifact=None,
            provenance=AcquisitionProvenance(
                source_uri=NY_OSC_OWNER_NAME_FILE_REQUEST_URL,
                authority="New York State Office of the State Comptroller, Office of Unclaimed Funds",
                acquisition_method=AcquisitionMethod.OFFICIAL_BULK_DOWNLOAD,
                retrieved_at=None,
                terms_review_ref=NY_BENCHMARK_REF,
                source_revision=None,
                access_notes=(
                    "Source contract boundary only; no request, download, parsing, or real PII processing performed. "
                    f"Machine source contract: {NY_SOURCE_CONTRACT_REF}."
                ),
            ),
        )
