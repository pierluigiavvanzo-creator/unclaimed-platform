from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Protocol


class AcquisitionMode(StrEnum):
    MOCK = "MOCK"
    REAL = "REAL"


class AcquisitionStatus(StrEnum):
    ACQUIRED = "ACQUIRED"
    MOCKED = "MOCKED"
    BLOCKED = "BLOCKED"
    FAILED = "FAILED"


class AcquisitionMethod(StrEnum):
    OFFICIAL_BULK_DOWNLOAD = "OFFICIAL_BULK_DOWNLOAD"
    MOCK = "MOCK"
    MANUAL_REFERENCE = "MANUAL_REFERENCE"
    CASE_SPECIFIC_REQUEST = "CASE_SPECIFIC_REQUEST"


@dataclass(frozen=True, slots=True)
class AcquisitionRequest:
    schema_version: str
    request_id: str
    source_id: str
    jurisdiction: str
    mode: AcquisitionMode
    requested_at: str
    acquisition_scope: str
    max_bytes: int
    approval_id: str | None
    expected_media_types: tuple[str, ...]
    notes: str | None = None


@dataclass(frozen=True, slots=True)
class RawArtifact:
    storage_ref: str
    content_hash: str
    byte_count: int
    content_type: str
    immutable_raw: bool
    synthetic: bool


@dataclass(frozen=True, slots=True)
class AcquisitionProvenance:
    source_uri: str
    authority: str
    acquisition_method: AcquisitionMethod
    retrieved_at: str | None
    terms_review_ref: str
    source_revision: str | None
    access_notes: str


@dataclass(frozen=True, slots=True)
class AcquisitionResult:
    schema_version: str
    request_id: str
    source_id: str
    jurisdiction: str
    status: AcquisitionStatus
    reason_code: str
    reason: str
    artifact: RawArtifact | None
    provenance: AcquisitionProvenance


class SourceAdapter(Protocol):
    source_id: str

    def acquire(self, request: AcquisitionRequest) -> AcquisitionResult:
        """Acquire or mock a raw source artifact without performing downstream matching."""
