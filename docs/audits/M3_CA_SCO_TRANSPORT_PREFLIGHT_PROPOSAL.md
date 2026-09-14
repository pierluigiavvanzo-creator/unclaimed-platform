# M3 California SCO Transport-Preflight Proposal

Date: 2026-09-14

Class: **A — Product Critical**

Status: **CANDIDATE PROPOSAL ONLY — NETWORK EXECUTION NOT AUTHORIZED**

## Objective

Define the smallest versioned, machine-readable proposal for a later California State Controller
(SCO) transport metadata preflight without executing any request to a download endpoint.

This task does not approve the source, enable the registry entry, acquire a dataset, parse a CSV,
process real PII, perform beneficiary matching, or enable outreach.

## REUSE FIRST result

The proposal reuses the canonical M3 governance/readiness foundation:

- `SourceAccessGovernance` v1;
- `SourceApprovalReadiness` v1;
- disabled/not-approved `ca.sco.unclaimed_property.bulk` registry entry;
- `PROPOSED` SCO source-access policy;
- canonical approval-readiness evidence;
- existing JSON Schema draft 2020-12 and contract-test infrastructure.

No new runtime dependency or HTTP client behavior is introduced.

## Proposal boundary

The proposal defines which metadata a later separately authorized preflight may inspect:

- exact endpoint identity;
- redirect chain;
- HTTP status;
- final host;
- response headers;
- content type;
- content length;
- TLS scheme;
- observation timestamp.

The proposal also defines provenance fields that a later observation must record.

## Fail-closed execution controls

The machine contract requires:

- `network_execution_authorized = false`;
- `network_request_performed = false`;
- `acquisition_performed = false`;
- `source_approved = false`;
- `source_enabled = false`;
- an explicit execution approval reference before any later execution;
- unresolved request method, timeout, redirect limit and allowlisted hosts;
- `response_body_bytes_allowed = 0`;
- no response-body persistence;
- no response-body parsing;
- no dataset-artifact persistence;
- no real PII processing;
- no beneficiary matching;
- no outreach.

The advertised host `claimit.ca.gov` remains evidence only. It is not silently converted into an
approved transport allowlist.

## Intentionally unresolved

This proposal does not select or infer:

- exact download endpoint;
- request method;
- timeout;
- maximum redirect count;
- approved host allowlist;
- execution approval reference;
- observed content type;
- observed content length.

Those values belong to the later execution gate and must not be filled by general knowledge.

## Acceptance criteria

The candidate is acceptable only if tests prove that:

1. the proposal schema is valid JSON Schema draft 2020-12;
2. the California SCO proposal validates;
3. a proposal claiming network authorization is rejected;
4. a proposal claiming that a request or acquisition occurred is rejected;
5. a proposal allowing response-body bytes is rejected;
6. proposal, readiness evidence, registry and policy use the same source identity and source page;
7. the registry remains disabled/not approved and the policy remains `PROPOSED`;
8. execution controls remain unresolved and body/PII/matching/outreach access remains blocked;
9. existing repository quality/contract/smoke/full-test gates remain green;
10. no request is sent to any California SCO download endpoint.

## Safety boundary

No network request to a download endpoint is part of this candidate. Promotion of this proposal
would not authorize execution. The actual transport preflight requires a separate explicit owner
approval and a new bounded execution task.

## Rollback

Before promotion, abandon the candidate branch. After any later promotion, use a normal
history-preserving revert. Do not force-push.

## Next gate

After candidate tests and CI pass, stop for explicit owner review/promotion. If promoted, the next
step is still a separate human gate deciding whether to authorize one bounded metadata-only transport
preflight. No source approval or real acquisition is implied.
