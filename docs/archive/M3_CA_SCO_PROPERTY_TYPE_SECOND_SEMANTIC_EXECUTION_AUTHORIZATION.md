# M3 — CA SCO PROPERTY_TYPE Second Bounded Semantic Execution Authorization

Date: 2026-09-15  
Status: **AUTHORIZED FOR ONE BOUNDED EXECUTION — NOT YET CONSUMED**

## 1. Human approvals received

The owner explicitly granted both fresh approvals required by the reviewed proposal:

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`

These approvals are new and are not derived from, or replacements for, the approvals consumed by the
historical first execution.

## 2. Reviewed proposal

Reviewed proposal branch:
`m3-ca-sco-property-type-second-execution-proposal`

Reviewed proposal SHA:
`ac6d234dda19b1eb8c8f8ceb0206730bcc419bcb`

Review gate:
`HUMAN_PROPERTY_TYPE_SECOND_SEMANTIC_EXECUTION_REVIEW`

Review result:
`PASS`.

## 3. Authorized scope

The approvals authorize exactly one bounded real execution of the canonical v1.1.0 runner and the
transient in-memory row observation needed to project `PROPERTY_TYPE`.

They also authorize creation of the temporary one-shot workflow required to perform that single run.

They do **not** authorize:

- source approval;
- registry activation;
- production classification;
- identity resolution;
- genealogy;
- beneficiary matching;
- outreach;
- claim submission;
- promotion to `main`.

## 4. Privacy boundary

The authorized transient processing remains:

- memory-only;
- zero-day retention;
- immediate disposal;
- no raw body persistence;
- no full-row persistence;
- no `PROPERTY_ID` persistence;
- no owner/holder persistence;
- no per-row `PROPERTY_TYPE` persistence;
- no offending bytes, hashes or lengths persisted;
- no source record values in logs.

Only the bounded derived execution evidence defined by the v1.1.0 execution schema may be persisted.

## 5. Fixed execution caps

Unchanged from the reviewed proposal:

- 4 canonical members;
- max 4 rows/member;
- max 16 rows total;
- max 1 HEAD;
- max 4 Range GET;
- max 5 HTTP requests total;
- max 131072 response-body bytes per Range;
- max 524288 source-response body bytes total;
- max 262144 uncompressed transient bytes/member;
- max 1048576 uncompressed transient bytes total;
- max 32768 bytes/logical record;
- no extra Range;
- no full-body fallback;
- no automatic widening.

## 6. Execution contract

Runner:
`scripts/ca_sco_property_type_semantic_verification.py`

Execution schema:
`schemas/common/property_type_semantic_verification_execution.v1_1.schema.json`

Execution schema version:
`1.1.0`.

The v1.1.0 diagnostic distinction remains:

- invalid UTF-8 `PROPERTY_TYPE` -> `PROPERTY_TYPE_ENCODING_UNEXPECTED`;
- decoded shape mismatch -> `PROPERTY_TYPE_FORMAT_UNEXPECTED`.

The semantic regex remains unchanged:
`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

## 7. Single-use rule

The two approvals are single-use. They become consumed when the authorized workflow performs the
second real execution, regardless of whether the semantic result is compatible or fail-closed.

No automatic retry is authorized.

## 8. Workflow lifecycle

Authorized temporary workflow path:
`.github/workflows/ca-sco-property-type-semantic-verification-once.yml`

Required sequence:

1. stage and CI-validate authorization evidence with no SCO request;
2. create the temporary workflow using the exact fresh approval refs;
3. allow exactly one workflow-triggered execution;
4. validate the derived evidence against execution schema v1.1.0 and hard caps;
5. persist only the derived evidence/audit required for review;
6. remove the temporary workflow immediately after the run;
7. stop at the evidence-review gate.

## 9. Next gate

After the single execution and workflow removal:

`HUMAN_PROPERTY_TYPE_SECOND_SEMANTIC_EXECUTION_EVIDENCE_REVIEW`

No downstream product gate is opened automatically by the execution result.
