"""Offline controller fact binding for NY MVP-1 Stage B.

This module validates human-supplied controller facts and emits only a non-sensitive
readiness assessment. It performs no network I/O, no source access, no PII processing,
and cannot grant any P1 execution/privacy gate.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Literal, Self

from pydantic import BaseModel, ConfigDict, Field, model_validator


class ControllerFactsInput(BaseModel):
    """Human-supplied controller facts used only for offline readiness routing."""

    model_config = ConfigDict(frozen=True, extra="forbid", str_strip_whitespace=True)

    schema_version: Literal["1.0.0"] = "1.0.0"
    artifact_id: Literal["ny.mvp1.stage_b.controller_facts_input"] = (
        "ny.mvp1.stage_b.controller_facts_input"
    )
    formation_state: Literal["FORMED", "NOT_YET_FORMED"]
    operating_model: Literal["US_CONTROLLER_US_MARKET"] | None = None
    legal_name: str | None = Field(default=None, min_length=1)
    entity_type: str | None = Field(default=None, min_length=1)
    formation_jurisdiction: str | None = Field(default=None, min_length=1)
    principal_business_address: str | None = Field(default=None, min_length=1)
    privacy_contact: str | None = Field(default=None, min_length=1)
    relevant_eu_branch_office_employee_agent_or_stable_arrangement: bool | None = None
    eu_person_or_entity_live_owner_pii_access: bool | None = None
    lsp_customer_agreement_signing_entity: str | None = Field(default=None, min_length=1)
    lsp_fee_receiving_entity: str | None = Field(default=None, min_length=1)
    us_only_mvp1_market: bool | None = None
    eu_targeting: bool | None = None
    eu_monitoring: bool | None = None

    @model_validator(mode="after")
    def validate_fact_shape(self) -> Self:
        identity_fields = (
            self.operating_model,
            self.legal_name,
            self.entity_type,
            self.formation_jurisdiction,
            self.principal_business_address,
            self.privacy_contact,
            self.relevant_eu_branch_office_employee_agent_or_stable_arrangement,
            self.eu_person_or_entity_live_owner_pii_access,
            self.lsp_customer_agreement_signing_entity,
            self.lsp_fee_receiving_entity,
            self.us_only_mvp1_market,
            self.eu_targeting,
            self.eu_monitoring,
        )
        if self.formation_state == "NOT_YET_FORMED":
            if any(value is not None for value in identity_fields):
                raise ValueError(
                    "not-yet-formed controller cannot contain entity or operating facts"
                )
            return self

        required_formed = (
            self.operating_model,
            self.legal_name,
            self.entity_type,
            self.formation_jurisdiction,
            self.principal_business_address,
            self.relevant_eu_branch_office_employee_agent_or_stable_arrangement,
            self.eu_person_or_entity_live_owner_pii_access,
            self.lsp_customer_agreement_signing_entity,
            self.lsp_fee_receiving_entity,
            self.us_only_mvp1_market,
            self.eu_targeting,
            self.eu_monitoring,
        )
        if any(value is None for value in required_formed):
            raise ValueError("formed controller requires all material Stage B facts")
        return self


class AuthorizationDoesNotGrant(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    source_access: Literal[False] = False
    remote_preflight: Literal[False] = False
    download: Literal[False] = False
    real_candidate_materialization: Literal[False] = False
    owner_pii_processing: Literal[False] = False
    external_pii_query: Literal[False] = False
    identity_resolution: Literal[False] = False
    genealogy: Literal[False] = False
    beneficiary_matching: Literal[False] = False
    outreach: Literal[False] = False
    value_research: Literal[False] = False
    fee_agreement: Literal[False] = False
    representation: Literal[False] = False
    claim_activity: Literal[False] = False
    any_p1_gate: Literal[False] = False


class ControllerFactBindingAssessment(BaseModel):
    """Non-sensitive, fail-closed output suitable for repository persistence."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    schema_version: Literal["1.0.0"] = "1.0.0"
    artifact_id: Literal["ny.mvp1.stage_b.controller_fact_binding_assessment"] = (
        "ny.mvp1.stage_b.controller_fact_binding_assessment"
    )
    work_class: Literal["A_PRODUCT_CRITICAL"] = "A_PRODUCT_CRITICAL"
    mode: Literal["OFFLINE_FACT_BINDING_NO_SOURCE_ACCESS"] = (
        "OFFLINE_FACT_BINDING_NO_SOURCE_ACCESS"
    )
    status: Literal[
        "BLOCKED_ENTITY_NOT_FORMED",
        "ROUTE_TO_HUMAN_LEGAL_PRIVACY_REVIEW",
        "FACTS_BOUND_US_TRACK_PENDING_PROFESSIONAL_REVIEW",
    ]
    formation_state: Literal["FORMED", "NOT_YET_FORMED"]
    preferred_track: Literal["US_CONTROLLER_US_MARKET"] = "US_CONTROLLER_US_MARKET"
    facts_complete: bool
    controller_identity_present: bool
    principal_business_address_present: bool
    privacy_contact_defined: bool
    relevant_eu_arrangement_present: bool | None
    eu_live_owner_pii_access_present: bool | None
    us_only_mvp1_market: bool | None
    eu_targeting: bool | None
    eu_monitoring: bool | None
    sensitive_or_identifying_values_persisted: Literal[False] = False
    all_seven_p1_gates_state: Literal["NOT_GRANTED"] = "NOT_GRANTED"
    real_p1_execution_allowed: Literal[False] = False
    authorization_does_not_grant: AuthorizationDoesNotGrant = Field(
        default_factory=AuthorizationDoesNotGrant
    )
    next_action: Literal[
        "HUMAN_DECIDE_AND_FORM_US_CONTROLLER_ENTITY_FOR_REAL_P1",
        "HUMAN_REVIEW_CONTROLLER_TERRITORIAL_SCOPE_AND_LIVE_PII_ACCESS",
        "HUMAN_VERIFY_US_TAX_NY_NEXUS_AND_LEGAL_READINESS",
    ]


def assess_controller_facts(facts: ControllerFactsInput) -> ControllerFactBindingAssessment:
    """Return a non-sensitive readiness route without granting execution authority."""

    if facts.formation_state == "NOT_YET_FORMED":
        return ControllerFactBindingAssessment(
            status="BLOCKED_ENTITY_NOT_FORMED",
            formation_state=facts.formation_state,
            facts_complete=False,
            controller_identity_present=False,
            principal_business_address_present=False,
            privacy_contact_defined=False,
            relevant_eu_arrangement_present=None,
            eu_live_owner_pii_access_present=None,
            us_only_mvp1_market=None,
            eu_targeting=None,
            eu_monitoring=None,
            next_action="HUMAN_DECIDE_AND_FORM_US_CONTROLLER_ENTITY_FOR_REAL_P1",
        )

    review_required = any(
        (
            facts.relevant_eu_branch_office_employee_agent_or_stable_arrangement is True,
            facts.eu_person_or_entity_live_owner_pii_access is True,
            facts.us_only_mvp1_market is not True,
            facts.eu_targeting is True,
            facts.eu_monitoring is True,
        )
    )
    status: Literal[
        "ROUTE_TO_HUMAN_LEGAL_PRIVACY_REVIEW",
        "FACTS_BOUND_US_TRACK_PENDING_PROFESSIONAL_REVIEW",
    ]
    next_action: Literal[
        "HUMAN_REVIEW_CONTROLLER_TERRITORIAL_SCOPE_AND_LIVE_PII_ACCESS",
        "HUMAN_VERIFY_US_TAX_NY_NEXUS_AND_LEGAL_READINESS",
    ]
    if review_required:
        status = "ROUTE_TO_HUMAN_LEGAL_PRIVACY_REVIEW"
        next_action = "HUMAN_REVIEW_CONTROLLER_TERRITORIAL_SCOPE_AND_LIVE_PII_ACCESS"
    else:
        status = "FACTS_BOUND_US_TRACK_PENDING_PROFESSIONAL_REVIEW"
        next_action = "HUMAN_VERIFY_US_TAX_NY_NEXUS_AND_LEGAL_READINESS"

    return ControllerFactBindingAssessment(
        status=status,
        formation_state=facts.formation_state,
        facts_complete=True,
        controller_identity_present=True,
        principal_business_address_present=True,
        privacy_contact_defined=facts.privacy_contact is not None,
        relevant_eu_arrangement_present=(
            facts.relevant_eu_branch_office_employee_agent_or_stable_arrangement
        ),
        eu_live_owner_pii_access_present=facts.eu_person_or_entity_live_owner_pii_access,
        us_only_mvp1_market=facts.us_only_mvp1_market,
        eu_targeting=facts.eu_targeting,
        eu_monitoring=facts.eu_monitoring,
        next_action=next_action,
    )


def load_controller_facts(path: Path) -> ControllerFactsInput:
    try:
        payload: Any = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"unable to read controller facts artifact: {path.name}") from exc
    if not isinstance(payload, dict):
        raise ValueError("controller facts artifact must be a JSON object")
    return ControllerFactsInput.model_validate(payload)
