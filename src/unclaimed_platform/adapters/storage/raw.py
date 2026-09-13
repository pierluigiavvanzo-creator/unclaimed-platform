from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Mapping, Sequence
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Protocol

from unclaimed_platform.core.audit.writer import AuditEventWriter
from unclaimed_platform.core.policy_engine.model import PolicyEffect
from unclaimed_platform.core.policy_engine.privacy import (
    RawDataGovernanceContext,
    RawDataGovernanceGate,
)

_SHA256_PATTERN = re.compile(r"^[a-f0-9]{64}$")


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
    record_ref: str
    content_hash: str
    record_hash: str
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
    governance_policy_id: str
    governance_policy_version: str
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
    """Content-addressed raw bytes plus append-only immutable provenance records.

    This bounded adapter uses standard-library filesystem primitives for synthetic M3 validation.
    Production backend selection remains behind the ImmutableRawStore protocol.
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

        policy_result = self._governance_gate.evaluate(governance)
        if policy_result.effect is not PolicyEffect.ALLOW:
            raise RawStoragePolicyError(policy_result.reason_code, policy_result.reason)

        policy = self._governance_gate.policy
        if policy is None:
            raise RawStoragePolicyError(
                "PRIVACY_POLICY_REQUIRED",
                "A trusted privacy/data-minimization policy is required before raw persistence.",
            )

        provenance = governance.provenance
        if provenance is None:
            raise RawStoragePolicyError(
                "PROVENANCE_REQUIRED",
                "Required raw-artifact provenance is missing.",
            )

        content_hash = hashlib.sha256(content).hexdigest()
        storage_ref = self._storage_ref(content_hash)
        metadata = dict(sorted((provenance_metadata or {}).items()))
        material: dict[str, Any] = {
            "schema_version": "1.0.0",
            "storage_ref": storage_ref,
            "content_hash": content_hash,
            "byte_count": len(content),
            "content_type": content_type,
            "source_id": governance.source_id,
            "source_uri": provenance.source_uri,
            "authority": provenance.authority,
            "acquisition_method": provenance.acquisition_method,
            "retrieved_at": provenance.retrieved_at,
            "source_revision": provenance.source_revision,
            "approval_reference": governance.approval_reference,
            "terms_review_ref": provenance.terms_review_ref,
            "retention_policy_ref": governance.retention_policy_ref,
            "processing_purpose": governance.processing_purpose,
            "governance_policy_id": policy.policy_id,
            "governance_policy_version": policy.policy_version,
            "data_categories": sorted(governance.data_categories),
            "requested_fields": sorted(governance.requested_fields),
            "provenance_metadata": metadata,
            "synthetic": synthetic,
            "immutable": True,
        }
        record_hash = hashlib.sha256(self._canonical_json(material)).hexdigest()
        record_ref = self._record_ref(content_hash, record_hash)
        record = RawArtifactRecord(
            schema_version="1.0.0",
            storage_ref=storage_ref,
            record_ref=record_ref,
            content_hash=content_hash,
            record_hash=record_hash,
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
            governance_policy_id=policy.policy_id,
            governance_policy_version=policy.policy_version,
            data_categories=tuple(sorted(governance.data_categories)),
            requested_fields=tuple(sorted(governance.requested_fields)),
            provenance_metadata=metadata,
            synthetic=synthetic,
            immutable=True,
        )
        encoded_record = self._encode_record(record)

        artifact_path = self._root / storage_ref
        record_path = self._root / record_ref
        artifact_path.parent.mkdir(parents=True, exist_ok=True)
        record_path.parent.mkdir(parents=True, exist_ok=True)

        artifact_created = self._ensure_immutable_bytes(artifact_path, content)
        record_created = self._ensure_immutable_record(record_path, encoded_record)
        self._verify_record(record)

        if artifact_created or record_created:
            self._audit_writer.append(
                case_id=None,
                event_type="RAW_ARTIFACT_PERSISTED",
                actor_type="SYSTEM",
                actor_id="A01",
                payload={
                    "schema_version": record.schema_version,
                    "storage_ref": record.storage_ref,
                    "record_ref": record.record_ref,
                    "content_hash": record.content_hash,
                    "record_hash": record.record_hash,
                    "byte_count": record.byte_count,
                    "content_type": record.content_type,
                    "source_id": record.source_id,
                    "approval_reference": record.approval_reference,
                    "retention_policy_ref": record.retention_policy_ref,
                    "processing_purpose": record.processing_purpose,
                    "governance_policy_id": record.governance_policy_id,
                    "governance_policy_version": record.governance_policy_version,
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

    def load_record(self, content_hash: str, record_hash: str) -> RawArtifactRecord:
        self._validate_digest(content_hash)
        self._validate_digest(record_hash)
        record_path = self._root / self._record_ref(content_hash, record_hash)
        if not record_path.exists():
            raise RawStorageValidationError(
                "RAW_ARTIFACT_RECORD_NOT_FOUND",
                "No immutable provenance record exists for the requested hashes.",
            )
        raw: object = json.loads(record_path.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise ImmutableArtifactError(
                "IMMUTABLE_PROVENANCE_CORRUPTED",
                "Persisted raw provenance record is not a JSON object.",
            )
        record = self._record_from_mapping(raw)
        if record.content_hash != content_hash or record.record_hash != record_hash:
            raise ImmutableArtifactError(
                "IMMUTABLE_PROVENANCE_CORRUPTED",
                "Persisted provenance hashes do not match the requested hashes.",
            )
        self._verify_record(record)
        return record

    def _verify_record(self, record: RawArtifactRecord) -> None:
        artifact_path = self._root / record.storage_ref
        record_path = self._root / record.record_ref
        if not artifact_path.exists() or not record_path.exists():
            raise ImmutableArtifactError(
                "IMMUTABLE_RECORD_INCOMPLETE",
                "Raw artifact and immutable provenance record must both exist.",
            )

        content = artifact_path.read_bytes()
        digest = hashlib.sha256(content).hexdigest()
        if digest != record.content_hash or len(content) != record.byte_count:
            raise ImmutableArtifactError(
                "IMMUTABLE_ARTIFACT_CORRUPTED",
                "Persisted raw content no longer matches its immutable record.",
            )

        persisted_record = record_path.read_bytes()
        if persisted_record != self._encode_record(record):
            raise ImmutableArtifactError(
                "IMMUTABLE_PROVENANCE_MISMATCH",
                "Persisted provenance differs from the requested immutable record.",
            )

        material = self._record_material(record)
        calculated_record_hash = hashlib.sha256(self._canonical_json(material)).hexdigest()
        if calculated_record_hash != record.record_hash:
            raise ImmutableArtifactError(
                "IMMUTABLE_PROVENANCE_CORRUPTED",
                "Persisted provenance hash does not match its deterministic record material.",
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
        except FileExistsError as error:
            existing = path.read_bytes()
            if existing != content:
                raise ImmutableArtifactError(
                    "IMMUTABLE_ARTIFACT_MODIFICATION_REJECTED",
                    "Existing raw artifact cannot be overwritten or modified.",
                ) from error
            return False
        return True

    def _ensure_immutable_record(self, path: Path, content: bytes) -> bool:
        if path.exists():
            if path.read_bytes() != content:
                raise ImmutableArtifactError(
                    "IMMUTABLE_PROVENANCE_MODIFICATION_REJECTED",
                    "Existing raw provenance cannot be overwritten or modified.",
                )
            return False
        try:
            with path.open("xb") as handle:
                handle.write(content)
        except FileExistsError as error:
            if path.read_bytes() != content:
                raise ImmutableArtifactError(
                    "IMMUTABLE_PROVENANCE_MODIFICATION_REJECTED",
                    "Existing raw provenance cannot be overwritten or modified.",
                ) from error
            return False
        return True

    @staticmethod
    def _storage_ref(content_hash: str) -> str:
        return f"raw/sha256/{content_hash[:2]}/{content_hash[2:4]}/{content_hash}"

    @staticmethod
    def _record_ref(content_hash: str, record_hash: str) -> str:
        return (
            f"provenance/sha256/{content_hash[:2]}/{content_hash[2:4]}/"
            f"{content_hash}/{record_hash}.json"
        )

    @staticmethod
    def _canonical_json(value: Mapping[str, Any]) -> bytes:
        return json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        ).encode("utf-8")

    @classmethod
    def _encode_record(cls, record: RawArtifactRecord) -> bytes:
        return cls._canonical_json(asdict(record)) + b"\n"

    @staticmethod
    def _record_material(record: RawArtifactRecord) -> dict[str, Any]:
        data = asdict(record)
        data.pop("record_ref")
        data.pop("record_hash")
        return data

    @classmethod
    def _record_from_mapping(cls, raw: Mapping[object, object]) -> RawArtifactRecord:
        return RawArtifactRecord(
            schema_version=str(raw["schema_version"]),
            storage_ref=str(raw["storage_ref"]),
            record_ref=str(raw["record_ref"]),
            content_hash=str(raw["content_hash"]),
            record_hash=str(raw["record_hash"]),
            byte_count=int(str(raw["byte_count"])),
            content_type=str(raw["content_type"]),
            source_id=str(raw["source_id"]),
            source_uri=str(raw["source_uri"]),
            authority=str(raw["authority"]),
            acquisition_method=str(raw["acquisition_method"]),
            retrieved_at=cls._optional_string(raw.get("retrieved_at")),
            source_revision=cls._optional_string(raw.get("source_revision")),
            approval_reference=cls._optional_string(raw.get("approval_reference")),
            terms_review_ref=str(raw["terms_review_ref"]),
            retention_policy_ref=str(raw["retention_policy_ref"]),
            processing_purpose=str(raw["processing_purpose"]),
            governance_policy_id=str(raw["governance_policy_id"]),
            governance_policy_version=str(raw["governance_policy_version"]),
            data_categories=cls._string_tuple(raw["data_categories"]),
            requested_fields=cls._string_tuple(raw["requested_fields"]),
            provenance_metadata=cls._metadata_mapping(raw["provenance_metadata"]),
            synthetic=cls._boolean(raw["synthetic"]),
            immutable=cls._boolean(raw["immutable"]),
        )

    @staticmethod
    def _validate_digest(value: str) -> None:
        if _SHA256_PATTERN.fullmatch(value) is None:
            raise RawStorageValidationError(
                "INVALID_SHA256",
                "Raw storage lookup requires a lowercase 64-character SHA-256 digest.",
            )

    @staticmethod
    def _optional_string(value: object) -> str | None:
        if value is None:
            return None
        return str(value)

    @staticmethod
    def _string_tuple(value: object) -> tuple[str, ...]:
        if not isinstance(value, list):
            raise ImmutableArtifactError(
                "IMMUTABLE_PROVENANCE_CORRUPTED",
                "Expected a list in immutable raw provenance.",
            )
        return tuple(str(item) for item in value)

    @staticmethod
    def _metadata_mapping(value: object) -> Mapping[str, str | None]:
        if not isinstance(value, dict):
            raise ImmutableArtifactError(
                "IMMUTABLE_PROVENANCE_CORRUPTED",
                "Expected an object for provenance metadata.",
            )
        return {str(key): None if item is None else str(item) for key, item in value.items()}

    @staticmethod
    def _boolean(value: object) -> bool:
        if not isinstance(value, bool):
            raise ImmutableArtifactError(
                "IMMUTABLE_PROVENANCE_CORRUPTED",
                "Expected a boolean in immutable raw provenance.",
            )
        return value
