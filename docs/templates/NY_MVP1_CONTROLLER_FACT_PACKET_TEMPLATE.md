# NY MVP-1 Controller Fact Packet Template

Date: 2026-09-24

Status: TEMPLATE_ONLY_NOT_A_FACTUAL_CONTROLLER_RECORD

Mode: OFFLINE / NO SOURCE ACCESS / NO P1 AUTHORIZATION

## Purpose

Collect the minimum factual controller information needed after a real US entity has been formed so the existing Controller Fact Binder V1 can route the project to the correct human legal/tax/privacy review without inventing entity facts.

This document is a preparation template only. It is not evidence that an LLC exists.

## Public-repository rule

The repository is public.

Do not commit a completed fact packet containing the real controller legal name, principal business address, privacy-contact value, contracting-entity name, fee-receiving entity name or other identifying values unless the Product Owner has explicitly approved that publication.

Preferred handling:

1. complete the real input locally or in an appropriately controlled record;
2. run the offline binder;
3. persist only the non-sensitive binder assessment when appropriate.

## Required factual fields after formation

Record only facts supported by formation documents, provider records or direct Product Owner confirmation.

- formation_state: FORMED
- operating_model: US_CONTROLLER_US_MARKET
- legal_name
- entity_type
- formation_jurisdiction
- principal_business_address
- privacy_contact, if defined
- relevant_eu_branch_office_employee_agent_or_stable_arrangement
- eu_person_or_entity_live_owner_pii_access
- lsp_customer_agreement_signing_entity
- lsp_fee_receiving_entity
- us_only_mvp1_market
- eu_targeting
- eu_monitoring

If the entity has not yet been formed, the only valid factual state is formation_state = NOT_YET_FORMED and all entity/operating facts remain null.

## Pre-formation safe example

    {
      "schema_version": "1.0.0",
      "artifact_id": "ny.mvp1.stage_b.controller_facts_input",
      "formation_state": "NOT_YET_FORMED",
      "operating_model": null,
      "legal_name": null,
      "entity_type": null,
      "formation_jurisdiction": null,
      "principal_business_address": null,
      "privacy_contact": null,
      "relevant_eu_branch_office_employee_agent_or_stable_arrangement": null,
      "eu_person_or_entity_live_owner_pii_access": null,
      "lsp_customer_agreement_signing_entity": null,
      "lsp_fee_receiving_entity": null,
      "us_only_mvp1_market": null,
      "eu_targeting": null,
      "eu_monitoring": null
    }

## Existing machine contract

Input schema:

schemas/common/ny_mvp1_stage_b_controller_facts_input.schema.json

Binder:

src/unclaimed_platform/domain/ny_mvp1_controller_fact_binder.py

Offline CLI:

scripts/ny_mvp1_controller_fact_binder.py

## Local binder command after formation

Use a real input file outside the public repository unless publication has been explicitly approved.

    python scripts/ny_mvp1_controller_fact_binder.py --input <CONTROLLED_LOCAL_CONTROLLER_FACTS.json> --output <NON_SENSITIVE_ASSESSMENT.json>

Expected route is one of:

- BLOCKED_ENTITY_NOT_FORMED
- ROUTE_TO_HUMAN_LEGAL_PRIVACY_REVIEW
- FACTS_BOUND_US_TRACK_PENDING_PROFESSIONAL_REVIEW

The binder cannot grant P1.

The output must preserve:

- real_p1_execution_allowed = false
- all_seven_p1_gates_state = NOT_GRANTED

## Human verification before binding

Before using a FORMED packet, verify:

- formation is genuinely complete;
- legal name exactly matches the formation record;
- jurisdiction is factual;
- business address is factual;
- agreement-signing and fee-receiving entities are factual;
- EU presence/access facts are answered explicitly;
- US-only / EU-targeting / EU-monitoring facts are answered explicitly;
- no placeholder remains.

## Stop condition

If any material field is unknown, disputed or not yet evidenced, do not infer it.

Stop at human review.
