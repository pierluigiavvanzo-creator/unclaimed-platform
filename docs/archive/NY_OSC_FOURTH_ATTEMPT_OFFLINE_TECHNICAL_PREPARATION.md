# NY OSC Fourth Attempt — Offline Technical Preparation

Date: 2026-09-19

Classification: `A — Product Critical`

## Authorization boundary

The Product Owner authorized only offline technical preparation of the fourth-attempt runner and contracts.

This work performed no NY OSC access, remote listing preflight, download, archive opening, real owner-file processing or owner-PII processing.

## Prepared artifacts

- `scripts/ny_osc_gate4_transient_local.ps1`;
- fourth-attempt transient-local approval schema and `NOT_GRANTED` template;
- fourth-attempt transient-PII approval schema and `NOT_GRANTED` template;
- contract and static fail-closed tests.

## Preserved bounds

- one download maximum;
- zero retries;
- 450,000,000 compressed bytes maximum;
- 2,000,000,000 uncompressed bytes maximum;
- one archive member and exactly one text member;
- pipe delimiter and 14 documented fields;
- 65,536-byte streaming-parser chunks;
- no automatic widening or retry.

## Safety properties

The PowerShell runner checks both new approval artifacts, attempt number, exact phrases, proposal binding, distinct approval references, shared verified runner checkpoint, successful runner CI and all execution bounds before creating a temporary directory.

The prepared templates remain `NOT_GRANTED`, so the runner stops before any download directory or user prompt. Third-attempt approvals remain consumed and are not referenced or reusable.

The runner contains no network client. Any future fresh listing preflight and single download require separate explicit authorization.

## Product contribution

This package removes a technical preparation blocker from the shortest safe path to the first approved real source while keeping the Product Owner out of repetitive QA and preserving privacy and auditability.

## Remaining gate

After CI and integration, the next action is human review of the prepared runner package. Operational approval, preflight and execution remain separate later gates.
