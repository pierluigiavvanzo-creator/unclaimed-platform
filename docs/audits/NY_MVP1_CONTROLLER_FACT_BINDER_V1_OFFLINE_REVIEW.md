# NY MVP-1 CONTROLLER FACT BINDER V1 — OFFLINE REVIEW

Date: 2026-09-24

Classification: A — Product Critical

Mode: OFFLINE / SYNTHETIC / NON-PII / NO SOURCE ACCESS

## Result

IMPLEMENTED_OFFLINE_PENDING_GITHUB_CI_AND_HUMAN_ENTITY_FORMATION

## Objective

Reduce the elapsed time between formation of the real US controller entity and preparation of the fresh single-use P1 gate packet without inventing entity facts and without allowing controller fact binding to become an execution authorization.

## Scope

The binder accepts human-supplied controller facts only after entity formation, validates the required Stage B factual shape and emits a non-sensitive readiness assessment.

The output does not persist:

- controller legal name;
- entity type;
- formation jurisdiction;
- principal business address;
- privacy contact value;
- contracting entity name;
- fee-receiving entity name.

It persists only presence/route booleans needed to decide the next human gate.

## Fail-closed routes

`NOT_YET_FORMED`

-> `BLOCKED_ENTITY_NOT_FORMED`

-> `HUMAN_DECIDE_AND_FORM_US_CONTROLLER_ENTITY_FOR_REAL_P1`

A formed controller with any of the following:

- relevant EU branch/office/employee/agent/stable arrangement;
- EU person/entity live owner-PII access;
- market not US-only;
- EU targeting;
- EU monitoring;

routes to:

`ROUTE_TO_HUMAN_LEGAL_PRIVACY_REVIEW`

A formed controller with the preferred US-only fact pattern routes to:

`FACTS_BOUND_US_TRACK_PENDING_PROFESSIONAL_REVIEW`

-> `HUMAN_VERIFY_US_TAX_NY_NEXUS_AND_LEGAL_READINESS`

This is not a legal determination.

## Authorization boundary

The binder always outputs:

- `real_p1_execution_allowed = false`;
- `all_seven_p1_gates_state = NOT_GRANTED`;
- all `authorization_does_not_grant` values = `false`.

It cannot authorize:

- source access;
- preflight;
- download;
- real candidate materialization;
- owner PII processing;
- external PII query;
- identity resolution;
- genealogy;
- beneficiary matching;
- outreach;
- value research;
- fee agreement;
- representation;
- claim activity;
- any P1 gate.

## Public repository boundary

The GitHub repository is public. Real controller input containing legal identity/address data should not be committed automatically merely because it validates. The binder is designed so the input can remain local or in an appropriately controlled record while the non-sensitive assessment can be persisted in the repository.

A future Product Owner decision may explicitly classify specific controller facts as suitable for repository publication, but this implementation does not make that decision.

## Compatibility

The existing null-safe pre-formation artifact:

`sources/proposals/ny_mvp1_stage_b_us_controller_fact_binding.v1.json`

remains unchanged and valid.

This binder is additive and does not supersede D-012, D-013 or D-014.

## Test evidence

Local isolated validation before GitHub integration covers:

- Draft 2020-12 schema validity;
- synthetic `NOT_YET_FORMED` input;
- synthetic formed-US input;
- rejection of invented identity on the not-formed path;
- rejection of incomplete formed facts;
- US-only route to professional review, not execution;
- EU/live-PII/non-US route to human legal/privacy review;
- non-persistence of legal name/address in output;
- invariant that all seven P1 gates remain `NOT_GRANTED`.

Canonical verification remains GitHub CI on Python 3.11 after branch integration.

## Remaining blocker

`HUMAN_DECIDE_AND_FORM_US_CONTROLLER_ENTITY_FOR_REAL_P1`

No real entity/controller fact has been supplied or inferred by this work.
