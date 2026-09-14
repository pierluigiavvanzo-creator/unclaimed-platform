# M3 California SCO $500+ Field Minimization / PII / Retention-Privacy Readiness

Date: 2026-09-14

Status: **CANDIDATE PROPOSAL — NON-AUTHORIZING — NO SCO NETWORK/BODY ACCESS**

## Purpose

Use only the already-canonical 25-label structure evidence from the `$500+` California SCO segment to
define the smallest proposed field scope for the first real-data product purpose, while keeping source
approval, row access, real PII processing, identity resolution, beneficiary matching and outreach blocked.

The proposed purpose is:

`INSURANCE_RELEVANCE_TRIAGE_ONLY`

It allows only a future determination that a source record is plausibly insurance-related and merits
later separately gated review. It does not authorize identifying a beneficiary, resolving a person's
identity, genealogical research, contact, claim submission, fee agreements or claimant verification.

## Evidence basis

No new California request is required or performed by this task.

Canonical structure evidence:
`sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`

The evidence established four CSV members with the same 25-label header candidate and exactly zero CSV
data rows parsed.

## REUSE FIRST

This task reuses rather than replaces:

- JSON Schema draft 2020-12, already canonical under D-003;
- the existing `RawDataGovernanceGate` and its purpose / retention / field-scope / PII fail-closed checks;
- the existing SCO source-access policy and registry as the authority that remains non-authorizing;
- the canonical `$500+` structure evidence instead of performing another source inspection.

No new runtime dependency or privacy framework library is introduced. NIST's public privacy glossary
describes minimization as limiting PII handling to activities directly relevant and necessary to an
authorized purpose and retaining it only as long as necessary. This is used only as design inspiration,
not as legal authority for this project.

## Field-minimization decision

For `INSURANCE_RELEVANCE_TRIAGE_ONLY`, the proposal classifies all 25 verified labels exactly once.

Proposed required / future-row allowlist:

- `PROPERTY_ID`
- `PROPERTY_TYPE`
- `HOLDER_NAME`

Rationale:

- `PROPERTY_ID` preserves source linkage;
- `PROPERTY_TYPE` is the direct property-category triage signal;
- `HOLDER_NAME` is needed to assess whether the holder appears insurance-related.

No optional fields are proposed for the first row-level scope.

Prohibited for this purpose:

- owner name and all owner address/geography fields;
- holder street/city/state/ZIP fields.

These fields are not required to determine insurance relevance. Holder street lines are prohibited as
a conservative project minimization inference even though the earlier deterministic header heuristic
did not list those three labels among its potential-PII indicators.

Unresolved and therefore not allowlisted:

- `CASH_REPORTED`
- `SHARES_REPORTED`
- `NAME_OF_SECURITIES_REPORTED`
- `NO_OF_OWNERS`
- `CURRENT_CASH_BALANCE`
- `NUMBER_OF_PENDING_CLAIMS`
- `NUMBER_OF_PAID_CLAIMS`
- `CUSIP`

Those fields may become relevant to later economic, claims-status, or securities-specific purposes, but
their necessity is not established for insurance-relevance triage.

## PII necessity boundary

Actual PII presence remains unverified because no data row has been sampled.

The canonical structure heuristic marked `HOLDER_NAME` as a potential PII indicator. The proposal
therefore records field-level necessity for triage but does **not** authorize PII processing. Human/legal
review must explicitly approve the necessity/proportionality of processing `HOLDER_NAME` before any
row-level access.

Owner identity/address fields are explicitly unnecessary for this purpose.

## Retention candidate

The package proposes, but does not approve, a seven-day maximum retention candidate for projected
triage records only.

Important: `7 days` is a conservative **project safety candidate**, not a legal requirement and not a
claim about California law.

The draft forbids persistence of:

- the full ZIP archive;
- a full unminimized source row.

Delete-on-stop is required. Activation requires separate human/legal review and an approved retention
policy reference. Until then the canonical source-access policy keeps `retention_policy_ref: null`.

## Privacy-policy candidate

The package proposes a non-trusted internal privacy candidate limited to:

- purpose `INSURANCE_RELEVANCE_TRIAGE_ONLY`;
- fields `PROPERTY_ID`, `PROPERTY_TYPE`, `HOLDER_NAME`;
- encryption at rest;
- least privilege;
- access logging;
- no record values in logs;
- no export;
- no identity resolution;
- no beneficiary matching;
- no outreach.

There is currently no trusted project privacy-policy artifact in the canonical repository. The proposal
therefore keeps `trusted_policy_ref: null`. It must not be wired into `RawDataGovernanceGate` as trusted
configuration until a separate human/legal approval converts an approved policy artifact into canonical
trusted configuration.

## Future row-level contract

A future row-level contract is included only as `DRAFT_NOT_EXECUTABLE`.

It requests exactly:

`PROPERTY_ID`, `PROPERTY_TYPE`, `HOLDER_NAME`

and machine-fixes to `false`:

- row access authorization;
- network execution authorization;
- source-body access authorization;
- raw archive persistence;
- full-row persistence;
- PII authorization;
- identity resolution;
- beneficiary matching;
- outreach.

## Machine-enforced blockers

The readiness result remains:

`BLOCKED_PENDING_POLICY_AND_PII_APPROVAL`

Blocking items:

- retention policy not approved;
- project privacy policy not trusted;
- actual PII presence unverified;
- `HOLDER_NAME` PII necessity not approved;
- real-acquisition client not reviewed;
- source-approval reference missing.

The schema rejects attempts to change this package into source approval, real acquisition authority,
a wider row field request, or an invented trusted privacy-policy reference.

## Files

- `schemas/common/source_field_privacy_readiness.schema.json`
- `schemas/examples/ca_sco_500_plus_field_privacy_readiness.examples.json`
- `sources/proposals/ca_sco_segment_500_plus.field_privacy_readiness.v1.json`
- `tests/contract/test_ca_sco_field_privacy_readiness.py`
- `docs/audits/M3_CA_SCO_FIELD_PRIVACY_READINESS.md`

## Stop condition / next gate

This candidate must stop before:

- updating the source policy to `APPROVED`;
- filling `privacy_policy_ref` or `retention_policy_ref`;
- enabling the registry;
- reading a real row;
- authorizing real PII.

Next gate after candidate CI:

**human review of the field-minimization proposal and the draft retention/privacy controls.**
