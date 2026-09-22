from __future__ import annotations

from dataclasses import dataclass

from .model import PolicyEffect, PolicyResult


@dataclass(frozen=True, slots=True)
class ProvenanceContext:
    source_uri: str
    authority: str
    acquisition_method: str
    terms_review_ref: str
    retrieved_at: str | None
    source_revision: str | None


@dataclass(frozen=True, slots=True)
class RawDataGovernancePolicy:
    policy_id: str
    policy_version: str
    source_id: str
    synthetic_only: bool
    source_approval_required: bool
    authorized_processing_purposes: frozenset[str]
    authorized_data_categories: frozenset[str]
    allowed_fields: frozenset[str]
    authorized_retention_policy_refs: frozenset[str]
    allow_pii: bool


@dataclass(frozen=True, slots=True)
class RawDataGovernanceContext:
    source_id: str
    synthetic: bool
    approval_reference: str | None
    processing_purpose: str
    data_categories: frozenset[str]
    requested_fields: frozenset[str]
    retention_policy_ref: str | None
    contains_pii: bool
    pii_required_for_purpose: bool
    retrieved_timestamp_required: bool
    provenance: ProvenanceContext | None


class RawDataGovernanceGate:
    """Deterministic fail-closed gate using a separately supplied trusted policy."""

    rule_id = "M3_RAW_DATA_GOVERNANCE_V1"

    def __init__(self, policy: RawDataGovernancePolicy | None = None) -> None:
        self._policy = policy

    @property
    def policy(self) -> RawDataGovernancePolicy | None:
        return self._policy

    def evaluate(self, context: RawDataGovernanceContext) -> PolicyResult:
        policy = self._policy
        if policy is None:
            return self._stop(
                "PRIVACY_POLICY_REQUIRED",
                "A trusted privacy/data-minimization policy is required before raw persistence.",
            )

        if policy.source_id != context.source_id:
            return self._stop(
                "SOURCE_POLICY_MISMATCH",
                "The governance policy does not authorize the requested source.",
            )

        if not context.synthetic and policy.synthetic_only:
            return self._stop(
                "REAL_DATA_NOT_AUTHORIZED",
                "This governance policy authorizes synthetic artifacts only.",
            )

        provenance = context.provenance
        if provenance is None or not all(
            (
                provenance.source_uri.strip() if provenance else "",
                provenance.authority.strip() if provenance else "",
                provenance.acquisition_method.strip() if provenance else "",
                provenance.terms_review_ref.strip() if provenance else "",
            )
        ):
            return self._stop(
                "PROVENANCE_REQUIRED",
                "Required raw-artifact provenance is missing or incomplete.",
            )

        if context.retrieved_timestamp_required and not provenance.retrieved_at:
            return self._stop(
                "RETRIEVED_TIMESTAMP_REQUIRED",
                "A retrieval timestamp is required for this acquisition context.",
            )

        if (not context.synthetic or policy.source_approval_required) and not (
            context.approval_reference
        ):
            return self._stop(
                "SOURCE_APPROVAL_REQUIRED",
                "Explicit source approval is required before raw persistence.",
            )

        if (
            not context.processing_purpose
            or context.processing_purpose not in policy.authorized_processing_purposes
        ):
            return self._stop(
                "PROCESSING_PURPOSE_NOT_AUTHORIZED",
                "The declared processing purpose is not authorized.",
            )

        if not context.retention_policy_ref:
            return self._stop(
                "RETENTION_POLICY_REQUIRED",
                "A retention policy reference is required before raw persistence.",
            )

        if context.retention_policy_ref not in policy.authorized_retention_policy_refs:
            return self._stop(
                "RETENTION_POLICY_NOT_AUTHORIZED",
                "The declared retention policy is not authorized for this source and purpose.",
            )

        if not context.data_categories.issubset(policy.authorized_data_categories):
            return self._stop(
                "DATA_SCOPE_NOT_AUTHORIZED",
                "The requested dataset or data category exceeds the authorized scope.",
            )

        if context.requested_fields and not context.requested_fields.issubset(
            policy.allowed_fields
        ):
            return self._stop(
                "FIELD_SCOPE_NOT_MINIMIZED",
                "One or more requested fields exceed the allowed minimized field scope.",
            )

        if context.contains_pii and not policy.allow_pii:
            return self._stop(
                "PII_NOT_AUTHORIZED",
                "PII is present but the trusted governance policy does not authorize PII.",
            )

        if context.contains_pii and not context.pii_required_for_purpose:
            return self._stop(
                "UNNECESSARY_PII",
                "PII is present but is not necessary for the authorized processing purpose.",
            )

        return PolicyResult(
            effect=PolicyEffect.ALLOW,
            reason_code="RAW_DATA_GOVERNANCE_ALLOWED",
            reason="Raw persistence governance checks passed.",
            rule_id=self.rule_id,
        )

    def _stop(self, reason_code: str, reason: str) -> PolicyResult:
        return PolicyResult(
            effect=PolicyEffect.STOP,
            reason_code=reason_code,
            reason=reason,
            rule_id=self.rule_id,
        )
