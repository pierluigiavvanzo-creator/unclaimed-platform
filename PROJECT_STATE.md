# PROJECT_STATE.md

Last updated: 2026-09-17

## Current Product Objective

`MVP-1 — First Economically Actionable Case`

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

The project must now optimize for the shortest lawful path to the first approved real source. Repeated California diagnostics are frozen unless new contradictory evidence appears or the Product Owner explicitly authorizes a semantic-contract redesign.

## Current Engineering Milestone

M3 — Real Source Selection / Validation + Product Visibility

M0, M1 and M2 are VERIFIED.

## Current Working Checkpoint

Current branch:

`m3-ca-sco-v1-2-real-source-execution-once-2026-09-17`

Latest completed package:

`AUTHORIZATION -> EXECUTE ONCE -> EVIDENCE REVIEW -> SOURCE DECISION -> CLEANUP`

Execution trigger checkpoint:

- HEAD `d826492735b6f6665d59ab875e470074005a8191`;
- one-shot workflow run `35222675324` — **SUCCESS**;
- artifact `10496599995`;
- artifact digest `sha256:3e52cdff838de4dfa73bf62b0361af6938be73f2aa381c68ecaf8bc1b1d37fe9`.

## Fresh Authorization State

Execution approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_ED6A22A3`

Transient-row privacy approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_ED6A22A3`

Both are now:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

No retry is authorized.

## Real Execution Result

Persisted derived evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once_2026_09_17.json`

Result:

- transport baseline matched exactly;
- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- D-008 `control_disposition.status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- D-008 `control_disposition.reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- requests used: `1 HEAD + 1 Range = 2 HTTP`;
- body bytes read: `131072`;
- accepted rows in persisted summary: `0`;
- raw/body/row/PROPERTY_ID/owner-holder/per-row PROPERTY_TYPE persistence: `false`;
- identity, beneficiary matching, outreach and production classification: `false`.

## California Source Decision

Evidence review result:

`PASS_EXECUTION_EVIDENCE_ACCEPTED`

Source decision:

`REJECT_CA_SCO_500_PLUS_AS_APPROVED_MVP1_SOURCE_UNDER_CURRENT_V1_2_CONTRACT`

This is contract-specific, not a claim that the source itself is invalid. Under the current unchanged PROPERTY_TYPE regex and D-008 `WHOLE_SOURCE_STOP`, the source cannot continue through the MVP-1 vertical slice.

California source state:

- source policy: `PROPOSED`;
- registry enabled: `false`;
- registry approved: `false`;
- approved real sources: `0`;
- production classification: inactive;
- downstream case work: blocked.

## Product / Commercial State

- approved real sources: `0`;
- first real bounded semantic execution on the adopted baseline: completed;
- California `$500+` candidate under current contract: frozen / not approved;
- real MVP-1 candidate cases: `0`;
- commercial baseline from real cases: not established;
- reviewer surface: Streamlit active;
- next value bottleneck: select and approve a different real source with lower semantic/integration friction.

## Next Recommended Action

Execute:

`SELECT_ALTERNATE_REAL_SOURCE_FOR_MVP1`

Classification:

`A — Product Critical`

Selection criteria:

- lawful/public or otherwise explicitly authorized source;
- explicit provenance and source terms;
- stable/retrievable machine-readable data;
- insurance-relevant or life-policy-relevant signal;
- minimal adaptation to existing acquisition/normalization/classification contracts;
- low privacy/legal burden for the initial bounded validation;
- shortest credible path to one approved source and then the MVP-1 vertical slice.

Use `REUSE > WRAP > INSPIRE > CUSTOM` and avoid further infrastructure or diagnostics that do not directly unblock this source-selection objective.

## Canonical restart

Read in order:

1. `AGENTS.md`
2. `PRODUCT_STRATEGY_MVP1.md`
3. `PROJECT_STATE.md`
4. `ROADMAP.md`
5. `DECISIONS.md`
6. `docs/handovers/HANDOVER_CURRENT.md`
