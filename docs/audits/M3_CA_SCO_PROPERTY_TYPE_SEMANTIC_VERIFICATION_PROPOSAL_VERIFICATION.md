# M3 CA SCO PROPERTY_TYPE Semantic Verification Proposal — Verification

Date: 2026-09-15

Status: **CANDIDATE VERIFIED — NON-AUTHORIZING**

## Branch / ancestry

Canonical base:
`830aaaed68bd4d2f9298eaede80b5e67918e935b`.

Candidate branch:
`m3-ca-sco-property-type-semantic-verification-proposal`.

Functional commit:
`6a39502a19f2127b154b95bf0014a8c76c5ae752`.

Before persistent-doc closure the compare was:
- ahead `1`;
- behind `0`;
- merge-base exactly canonical base.

## Functional diff

Exactly five added files:

1. `schemas/common/property_type_semantic_verification_proposal.schema.json`
2. `schemas/examples/ca_sco_500_plus_property_type_semantic_verification.examples.json`
3. `sources/proposals/ca_sco_segment_500_plus.property_type_semantic_verification.v1.json`
4. `tests/contract/test_ca_sco_property_type_semantic_verification_proposal.py`
5. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_SEMANTIC_VERIFICATION_PROPOSAL.md`

No source policy, registry, runtime adapter, execution script, workflow, acquisition client, or source
evidence file was changed.

## CI

Workflow run:
`34942475352`.

Head SHA:
`6a39502a19f2127b154b95bf0014a8c76c5ae752`.

Result:
- `quality` — SUCCESS;
- `streamlit-candidate` — SUCCESS.

Verified steps:
- Ruff PASS;
- mypy PASS;
- contract tests PASS;
- smoke tests PASS;
- full pytest PASS;
- frontend dependency install/lint/typecheck/build PASS;
- Streamlit safety/startup smoke PASS.

## Safety invariants

The candidate fixes:
- proposal-only status;
- network execution false;
- row access false;
- execution approval ref null;
- runner absent;
- network workflow absent;
- 16-row cap;
- 4-Range cap;
- 524,288-byte source-body cap;
- no full-body request;
- no cap widening;
- derived-summary-only persistence;
- raw/full-row/property-ID persistence false;
- transient row privacy approval required before execution;
- source policy and registry unchanged/fail-closed.

## Network/body access

No California SCO network request or source-body read occurred during proposal preparation or CI.

## Next gate

Human promotion decision only:

`m3-ca-sco-property-type-semantic-verification-proposal -> m2-state-governance-core`.

Promotion does not authorize execution.
