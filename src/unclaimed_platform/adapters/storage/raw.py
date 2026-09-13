from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping, Sequence
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Protocol

from unclaimed_platform.core.audit.writer import AuditEventWriter
from unclaimed_platform.core.policy_engine.model import PolicyEffect
from unclaimed_platform.core.policy_engine.privacy import (
    RawDataGovernanceContext,
    RawDataGovernanceGate,
)


class RawStorageError(RuntimeError):
    def __init__(self, reason_code: str, message: str) -> None:
        super().__init__(message)
        self.reason_code = reason_code


class RawStorageValidationError(RawStorageError):
    pass


class ImmutableArtifactError(RawStorageError):
    pass


class RawStoragePolicyError(RawStorageError):
    pass


@dataclass(frozen=True, slots=True)
class RawArtifactRecord:
    schema_version: str
    storage_ref: str
    content_hash: str
    byte_count: int
    content_type: str
    source_id: str
    source_uri: str
    authority: str
    acquisition_method: str
    retrieved_at: str | None
    source_revision: str | None
    approval_reference: str | None
    terms_review_ref: str
    retention_policy_ref: str
    processing_purpose: str
    data_categories: tuple[str, ...]
    requested_fields: tuple[str, ...]
    provenance_metadata: Mapping[str, str | None]
    synthetic: bool
    immutable: bool


class ImmutableRawStore(Protocol):
    def persist(
        self,
        *,
        content: bytes,
        content_type: str,
        governance: RawDataGovernanceContext,
        synthetic: bool,
        expected_byte_count: int | None = None,
        expected_content_types: Sequence[str] = (),
        provenance_metadata: Mapping[str, str | None] | None = None,
    ) -> RawArtifactRecord:
        """Persist immutable raw bytes after deterministic governance checks."""


class FileSystemRawStore:
    """Bounded content-addressed raw store for development and synthetic M3 validation.

    This adapter intentionally uses only standard-library filesystem primitives. Production backend
    selection remains behind the ImmutableRawStore protocol.
    """

    def __init__(
        self,
        root: Path,
        *,
        audit_writer: AuditEventWriter,
        governance_gate: RawDataGovernanceGate | None = None,
    ) -> None:
        self._root = root
        self._audit_writer = audit_writer
        self._governance_gate = governance_gate or RawDataGovernanceGate()

    def persist(
        self,
        *,
        content: bytes,
        content_type: str,
        governance: RawDataGovernanceContext,
        synthetic: bool,
        expected_byte_count: int | None = None,
        expected_content_types: Sequence[str] = (),
        provenance_metadata: Mapping[str, str | None] | None = None,
    ) -> RawArtifactRecord:
        if expected_byte_count is not None and len(content) != expected_byte_count:
            raise RawStorageValidationError(
                "BYTE_COUNT_MISMATCH",
                "Raw content byte count does not match the declared byte count.",
            )

        if not content_type.strip():
            raise RawStorageValidationError(
                "CONTENT_TYPE_REQUIRED",
                "Raw content type must be explicit before persistence.",
            )

        allowed_content_types = tuple(expected_content_types)
        if allowed_content_types and content_type not in allowed_content_types:
            raise RawStorageValidationError(
                "CONTENT_TYPE_NOT_ALLOWED",
                "Raw content type is not included in the expected content types.",
            )

        if synthetic is not governance.synthetic:
            raise RawStoragePolicyError(
                "SYNTHETIC_MARKER_MISMATCH",
                "Raw artifact synthetic/real marker does not match the governance context.",
            )

        policy = self._governance_gate.evaluate(governance)
        if policy.effect is not PolicyEffect.ALLOW:
            raise RawStoragePolicyError(policy.reason_code, policy.reason)

        provenance = governance.provenance
        if provenance is None:
            raise RawStoragePolicyError(
                "PROVENANCE_REQUIRED",
                "Required raw-artifact provenance is missing.",
            )

        digest = hashlib.sha256(content).hexdigest()
        storage_ref = self._storage_ref(digest)
        artifact_path = self._root / storage_ref
        manifest_path = self._manifest_path(digest)
        metadata = dict(sorted((provenance_metadata or {}).items()))

        record = RawArtifactRecord(
            schema_version="1.0.0",
            storage_ref=storage_ref,
            content_hash=digest,
            byte_count=len(content),
            content_type=content_type,
            source_id=governance.source_id,
            source_uri=provenance.source_uri,
            authority=provenance.authority,
            acquisition_method=provenance.acquisition_method,
            retrieved_at=provenance.retrieved_at,
            source_revision=provenance.source_revision,
            approval_reference=governance.approval_reference,
            terms_review_ref=provenance.terms_review_ref,
            retention_policy_ref=governance.retention_policy_ref or "",
            processing_purpose=governance.processing_purpose,
            data_categories=tuple(sorted(governance.data_categories)),
            requested_fields=tuple(sorted(governance.requested_fields)),
            provenance_metadata=metadata,
            synthetic=synthetic,
            immutable=True,
        )
        encoded_manifest = self._encode_record(record)

        artifact_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.parent.mkdir(parents=True, exist_ok=True)

        artifact_created = self._ensure_immutable_bytes(artifact_path, content)
        manifest_created = self._ensure_immutable_manifest(manifest_path, encoded_manifest)

        self._verify_record(record)

        if artifact_created or manifest_created:
            self._audit_writer.append(
                case_id=None,
                event_type="RAW_ARTIFACT_PERSISTED",
                actor_type="SYSTEM",
                actor_id="A01",
                payload={
                    "schema_version": record.schema_version,
                    "storage_ref": record.storage_ref,
                    "content_hash": record.content_hash,
                    "byte_count": record.byte_count,
                    "content_type": record.content_type,
                    "source_id": record.source_id,
                    "approval_reference": record.approval_reference,
                    "retention_policy_ref": record.retention_policy_ref,
                    "processing_purpose": record.processing_purpose,
                    "synthetic": record.synthetic,
                    "immutable": record.immutable,
                },
            )

        return record

    def read(self, record: RawArtifactRecord) -> bytes:
        content = (self._root / record.storage_ref).read_bytes()
        digest = hashlib.sha256(content).hexdigest()
        if digest != record.content_hash or len(content) != record.byte_count:
            raise ImmutableArtifactError(
                "IMMUTABLE_ARTIFACT_CORRUPTED",
                "Persisted raw content no longer matches its immutable record.",
            )
        self._verify_record(record)
        return content

    def load_record(self, content_hash: str) -> RawArtifactRecord:
        manifest_path = self._manifest_path(content_hash)
        if not manifest_path.exists():
            raise RawStorageValidationError(
                "RAW_ARTIFACT_NOT_FOUND",
                "No immutable manifest exists for the requested content hash.",
            )
        raw = json.loads(manifest_path.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise ImmutableArtifactError(
                "IMMUTABLE_MANIFEST_CORRUPTED",
                "Persisted raw manifest is not a JSON object.",
            )
        record = RawArtifactRecord(
            schema_version=str(raw["schema_version"]),
            storage_ref=str(raw["storage_ref"]),
            content_hash=str(raw["content_hash"]),
            byte_count=int(raw["byte_count"]),
            content_type=str(raw["content_type"]),
            source_id=str(raw["source_id"]),
            source_uri=str(raw["source_uri"]),
            authority=str(raw["authority"]),
            acquisition_method=str(raw["acquisition_method"]),
            retrieved_at=self._optional_string(raw.get("retrieved_at")),
            source_revision=self._optional_string(raw.get("source_revision")),
            approval_reference=self._optional_string(raw.get("approval_reference")),
            terms_review_ref=str(raw["terms_review_ref"]),
            retention_policy_ref=str(raw["retention_policy_ref"]),
            processing_purpose=str(raw["processing_purpose"]),
            data_categories=self._string_tuple(raw["data_categories"]),
            requested_fields=self._string_tuple(raw["requested_fields"]),
            provenance_metadata=self._metadata_mapping(raw["provenance_metadata"]),
            synthetic=bool(raw["synthetic"]),
            immutable=bool(raw["immutable"]),
        )
        if record.content_hash != content_hash:
            raise ImmutableArtifactError(
                "IMMUTABLE_MANIFEST_CORRUPTED",
                "Manifest content hash does not match the requested hash.",
            )
        self._verify_record(record)
        return record

    def _verify_record(self, record: RawArtifactRecord) -> None:
        artifact_path = self._root / record.storage_ref
        manifest_path = self._manifest_path(record.content_hash)
        if not artifact_path.exists() or not manifest_path.exists():
            raise ImmutableArtifactError(
                "IMMUTABLE_RECORD_INCOMPLETE",
                "Raw artifact and immutable manifest must both exist.",
            )

        content = artifact_path.read_bytes()
        digest = hashlib.sha256(content).hexdigest()
        if digest != record.content_hash or len(content) != record.byte_count:
            raise ImmutableArtifactError(
                "IMMUTABLE_ARTIFACT_CORRUPTED",
                "Persisted raw content no longer matches its immutable record.",
            )

        persisted_manifest = manifest_path.read_bytes()
        if persisted_manifest != self._encode_record(record):
            raise ImmutableArtifactError(
                "IMMUTABLE_METADATA_MISMATCH",
                "Persisted immutable metadata differs from the requested record.",
            )

    def _ensure_immutable_bytes(self, path: Path, content: bytes) -> bool:
        if path.exists():
            existing = path.read_bytes()
            if existing != content:
                raise ImmutableArtifactError(
                    "IMMUTABLE_ARTIFACT_MODIFICATION_REJECTED",
                    "Existing raw artifact cannot be overwritten or modified.",
                )
            return False
        try:
            with path.open("xb") as handle:
                handle.write(content)
        except FileExistsError:
            existing = path.read_bytes()
            if existing != content:
                raise ImmutableArtifactError(
                    "IMMUTABLE_ARTIFACT_MODIFICATION_REJECTED",
                    "Existing raw artifact cannot be overwritten or modified.",
                )
            return False
        return True

    def _ensure_immutable_manifest(self, path: Path, content: bytes) -> bool:
        if path.exists():
            if path.read_bytes() != content:
                raise ImmutableArtifactError(
                    "IMMUTABLE_METADATA_MODIFICATION_REJECTED",
                    "Existing raw artifact metadata cannot be changed.",
                )
            return False
        try:
            with path.open("xb") as handle:
                handle.write(content)
        except FileExistsError:
            if path.read_bytes() != content:
                raise ImmutableArtifactError(
                    "IMMUTABLE_METADATA_MODIFICATION_REJECTED",
                    "Existing raw artifact metadata cannot be changed.",
                )
            return False
        return True

    @staticmethod
    def _storage_ref(content_hash: str) -> str:
        return f"raw/sha256/{content_hash[:2]}/{content_hash[2:4]}/{content_hash}"

    def _manifest_path(self, content_hash: str) -> Path:
        return (
            self._root
            / "metadata"
            / "sha256"
            / content_hash[:2]
            / content_hash[2:4]
            / f"{content_hash}.json"
        )

    @staticmethod
    def _encode_record(record: RawArtifactRecord) -> bytes:
        return (
            json.dumps(
                asdict(record),
                sort_keys=True,
                separators=(",", ":"),
                ensure_ascii=False,
            )
            + "\n"
        ).encode("utf-8")

    @staticmethod
    def _optional_string(value: object) -> str | None:
        if value is None:
            return None
        return str(value)

    @staticmethod
    def _string_tuple(value: object) -> tuple[str, ...]:
        if not isinstance(value, list):
            raise ImmutableArtifactError(
                "IMMUTABLE_MANIFEST_CORRUPTED",
                "Expected a list in immutable raw metadata.",
            )
        return tuple(str(item) for item in value)

    @staticmethod
    def _metadata_mapping(value: object) -> Mapping[str, str | None]:
        if not isinstance(value, dict):
            raise ImmutableArtifactError(
                "IMMUTABLE_MANIFEST_CORRUPTED",
                "Expected an object for provenance metadata.",
            )
        return {str(key): None if item is None else str(item) for key, item in value.items()}
