# M3 California SCO Transport-Preflight Execution

Date: 2026-09-14

Class: **A — Product Critical**

Status: **AUTHORIZED ONE-TIME METADATA-ONLY EXECUTION — OBSERVATION PENDING**

## Owner gate

The owner explicitly authorized proceeding with the next bounded transport-preflight task after
confirming that the external Vercel account had been deleted.

Execution approval reference:

`OWNER_CHAT_APPROVAL_2026-09-14T13:26+02:00`

This approval is limited to one California SCO transport metadata preflight. It does not approve the
source, enable the registry, authorize dataset acquisition, authorize response-body access, authorize
PII processing, beneficiary matching, outreach, or any downstream legal/commercial action.

## Canonical starting point

- Canonical development branch before this candidate: `m2-state-governance-core`.
- Canonical parent SHA: `50887231d39eff793b1968b4a062292533205602`.
- Candidate branch: `m3-ca-sco-transport-preflight-execution`.
- Canonical proposal: `sources/proposals/ca_sco_unclaimed_property_bulk.transport_preflight.v1.json`.

## Pre-execution controls fixed before network access

The execution is intentionally narrower than general acquisition:

- official source page: `https://www.sco.ca.gov/upd_download_property_records.html`;
- target link label: `All properties`;
- endpoint discovery: parse exactly one matching anchor from the official source-page HTML;
- advertised/allowlisted download host: `claimit.ca.gov` only;
- transport method to the discovered download endpoint: `HEAD` only;
- HTTPS only;
- timeout: 10 seconds per request;
- maximum redirects followed: 3;
- redirect targets must remain HTTPS and on `claimit.ca.gov` or execution stops fail-closed;
- response-body bytes allowed/read: `0`;
- response body is never persisted or parsed;
- dataset artifact is never persisted;
- selected safe response headers only are recorded;
- no real PII, beneficiary matching, or outreach.

The exact download endpoint is deliberately not hard-coded or guessed. The runner establishes it from
the official SCO source page immediately before the first `HEAD` request and validates the extracted
endpoint against the fixed HTTPS/host allowlist. A normal `GET` is never sent to the discovered
download endpoint.

## Test-first execution gate

Before the network step, the one-time workflow must pass targeted contract tests proving:

1. the execution observation schema is valid JSON Schema draft 2020-12;
2. unsafe method/body/acquisition/approval/PII/matching/outreach states are schema-invalid;
3. the runner completes a synthetic metadata-only `HEAD` path with zero body bytes;
4. a redirect to a non-allowlisted host stops after the first hop;
5. endpoint-discovery failure prevents any download-endpoint request.

The normal repository CI remains an independent regression gate.

## Observation contract

New contract:

`schemas/common/source_transport_preflight_execution.schema.json`

Synthetic example:

`schemas/examples/ca_sco_transport_preflight_execution.examples.json`

The eventual real observation will record only:

- execution approval reference;
- exact endpoint extracted from the official source page;
- redirect hops observed through `HEAD` requests;
- terminal HTTP status when reached;
- final endpoint/host when allowed;
- selected response headers;
- content type and content length when advertised;
- HTTPS scheme and observation timestamp;
- explicit zero response-body bytes read;
- unchanged fail-closed source/PII/matching/outreach state.

## One-time execution mechanism

A temporary branch-scoped workflow executes only when all of the following are true:

- branch is `m3-ca-sco-transport-preflight-execution`;
- the pushed head commit message is exactly `chore: authorize one-time SCO metadata preflight`;
- targeted validation succeeds first.

After the observation is captured from the workflow log, the temporary execution workflow must be
removed in the next candidate commit so later pushes cannot repeat the network call accidentally.

## Stop condition

After recording and validating the metadata observation, stop at a new human gate. Even a successful
preflight does not authorize source approval, registry activation, a CSV download, row parsing,
real-data normalization, PII processing, beneficiary matching, or outreach.
