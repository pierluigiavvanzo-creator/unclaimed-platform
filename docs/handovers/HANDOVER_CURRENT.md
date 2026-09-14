# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-14

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository and branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Canonical promoted transport-proposal SHA:
  `171dc2e55f85b89f1bba81b1cc676d0ed2b7f3d3`
- Stable `main` HEAD: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`
- Promoted SCO governance candidate: `m3-ca-sco-source-governance`
- Promoted SCO approval-readiness candidate: `m3-ca-sco-approval-readiness`
- Promoted SCO transport-preflight proposal candidate: `m3-ca-sco-transport-preflight-proposal`
- Never develop directly on `main`; promote verified checkpoints only after explicit owner approval.

## Verified baseline

- M0 VERIFIED.
- M1 VERIFIED.
- M2 VERIFIED.
- M3 California source/legal readiness COMPLETE.
- M3 acquisition contracts/adapters CANONICAL + CI VERIFIED.
- M3 immutable raw storage/provenance + privacy/data-minimization CANONICAL + CI VERIFIED.
- Streamlit M3 reviewer CANONICAL + CI VERIFIED + REMOTE FUNCTIONAL/VISUAL SMOKE PASS.
- California SCO source governance CANONICAL + CI VERIFIED.
- California SCO approval-readiness evidence CANONICAL + CI VERIFIED.
- California SCO transport-preflight proposal CANONICAL + CI VERIFIED.
- SCO registry remains `enabled: false` and `approved_for_use: false`.
- SCO source-access policy remains `PROPOSED`; real acquisition authorization remains `false`.
- Approved real source count remains `0`.
- No California dataset has been downloaded or parsed.
- No transport-preflight request has been executed against a download endpoint.
- Real acquisition BLOCKED.
- Beneficiary matching BLOCKED.
- Real PII BLOCKED.
- Supabase untouched.
- `main` unchanged.

## California SCO transport-preflight proposal promotion

Candidate branch: `m3-ca-sco-transport-preflight-proposal`.

Promoted SHA:
`171dc2e55f85b89f1bba81b1cc676d0ed2b7f3d3`

Immediately before promotion, the candidate was 1 commit ahead and 0 behind canonical with merge-base
at `f34d2123b8d5664dc3260a942c454085c48d3308`.

Owner explicitly approved promotion. The canonical branch was advanced without force to the candidate
SHA.

Candidate CI run `34832293876`: PASS.
Canonical post-promotion CI run `34835032368`: PASS.

Verified gates on the promoted SHA include:

- Ruff PASS;
- mypy PASS;
- contract tests PASS;
- smoke tests PASS;
- full pytest PASS;
- frontend lint/typecheck/build regression gates PASS;
- Streamlit safety smoke PASS;
- Streamlit startup smoke PASS.

## Canonical transport-preflight proposal artifacts

- `schemas/common/source_transport_preflight_proposal.schema.json`
- `schemas/examples/ca_sco_transport_preflight_proposal.examples.json`
- `sources/proposals/ca_sco_unclaimed_property_bulk.transport_preflight.v1.json`
- `tests/contract/test_ca_sco_transport_preflight_proposal.py`
- `docs/audits/M3_CA_SCO_TRANSPORT_PREFLIGHT_PROPOSAL.md`

The proposal is deliberately non-executable. It requires fail-closed state including:

- `network_execution_authorized = false`;
- `network_request_performed = false`;
- `acquisition_performed = false`;
- `source_approved = false`;
- `source_enabled = false`;
- `response_body_bytes_allowed = 0`;
- no response-body persistence/parsing;
- no dataset persistence;
- no real PII;
- no beneficiary matching;
- no outreach.

## Current unresolved transport controls

Do not invent or silently fill:

- exact download endpoint;
- request method;
- timeout;
- redirect limit;
- approved host allowlist;
- execution approval reference;
- observed HTTP status;
- observed final host;
- observed content type;
- observed content length.

The advertised host `claimit.ca.gov` remains evidence only and is not automatically an approved
allowlist entry.

## Safety boundaries still in force

Do not enable without later explicit gates:

- any transport-preflight network execution;
- real California acquisition;
- source policy `APPROVED` state;
- source registry `enabled` / `approved_for_use`;
- response-body persistence/parsing during a metadata preflight;
- beneficiary matching on real data;
- real claimant/beneficiary/decedent/family PII;
- autonomous outreach;
- claimant verification;
- fee agreement execution;
- claim submission;
- unapproved scraping or restricted-source access.

## SINGLE NEXT ACTION

**HUMAN GATE ONLY:** the owner must decide whether to authorize one bounded California SCO
transport-preflight execution limited to metadata observation under the canonical proposal.

If the owner explicitly approves execution, the next implementation task must:

1. create a new isolated execution branch/task;
2. bind an explicit execution approval reference;
3. establish the exact endpoint, request method, timeout, redirect limit and approved host allowlist
   before sending the request;
4. keep `response_body_bytes_allowed = 0`;
5. persist and parse no response body;
6. acquire no dataset artifact;
7. record only allowed transport metadata/provenance such as endpoint identity, redirect chain, HTTP
   status, final host, headers/content type/content length, TLS scheme and observation time;
8. process no real PII;
9. perform no beneficiary matching or outreach;
10. leave source approval, registry activation and real retrieval blocked;
11. stop after the metadata observation and require a new human gate.

If the owner does not explicitly approve this network execution, do not send any request to a SCO
download endpoint.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 source/legal readiness: COMPLETE
M3 acquisition/raw persistence/privacy: CANONICAL + VERIFIED
M3 SCO source governance: CANONICAL + CI VERIFIED
M3 SCO approval readiness: CANONICAL + CI VERIFIED
M3 SCO transport-preflight proposal: CANONICAL + CI VERIFIED
SCO governance SHA: 463c6d6c972fa955a8aa0d3c97208c3029e202a8
SCO approval-readiness SHA: 73c6ffc130fdeffad7fb5cdaf86fa2185b8853a6
SCO transport proposal SHA: 171dc2e55f85b89f1bba81b1cc676d0ed2b7f3d3
SCO transport proposal candidate CI: 34832293876 PASS
SCO transport proposal canonical CI: 34835032368 PASS
SCO registry: DISABLED + NOT APPROVED
SCO policy: PROPOSED + NON-AUTHORIZING
Approved real sources: 0
Transport preflight execution: BLOCKED PENDING EXPLICIT OWNER APPROVAL
Real acquisition: BLOCKED
Beneficiary matching: BLOCKED
Real PII: BLOCKED
Supabase: UNTOUCHED
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e UNCHANGED
NEXT: owner decision on one bounded metadata-only transport-preflight execution
CONTEXT HEALTH: coherent; repository is source of truth
```
