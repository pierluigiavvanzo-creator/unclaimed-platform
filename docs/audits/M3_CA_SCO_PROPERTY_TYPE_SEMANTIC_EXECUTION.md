# M3 California SCO — PROPERTY_TYPE Semantic Execution Audit

Date: 2026-09-15

## Scope

This audit records the single owner-authorized bounded real semantic verification of `PROPERTY_TYPE` for the California SCO `$500+` segment.

The execution was limited to the previously canonical caps and did not authorize source approval, registry activation, identity resolution, beneficiary matching, outreach, claim submission, or production classification.

## Human Authorization

Owner instruction:
`autorizzo`

This was interpreted in the immediately preceding explicit gate as authorization for both:

- bounded semantic execution;
- bounded transient-row privacy exposure.

Machine references:

- execution: `OWNER_CHAT_APPROVAL_2026-09-15_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`;
- privacy: `OWNER_CHAT_APPROVAL_2026-09-15_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`.

Authorization package commit:
`6ba8d62824f0f0e8eaaa0eefbb8dc1bfdb58898e`.

Authorization CI:
`34964924686` — SUCCESS for `quality` and `streamlit-candidate` before the network workflow was added.

## Execution Identity

Execution branch:
`m3-ca-sco-property-type-semantic-execution`

One-shot workflow commit:
`dd5dc80a22307586c341b703de8fe03d6861df29`

Workflow:
`.github/workflows/ca-sco-property-type-semantic-verification-once.yml`

Workflow run:
`34965097988`

Job:
`bounded-semantic-verification`

Job ID:
`104367570457`

Result:
`SUCCESS` at the workflow level because a schema-valid fail-closed STOP is an accepted governance outcome.

## Observed Result

Execution evidence status:
`STOPPED_FAIL_CLOSED`

Stop reason:
`PROPERTY_TYPE_FORMAT_UNEXPECTED`

Request/body counters:

- HEAD requests: `1`;
- Range GET requests: `1`;
- HTTP requests total: `2`;
- source response-body bytes read: `131072`;
- maximum authorized body bytes: `524288`.

Sample counters:

- accepted/examined data rows: `0`;
- rows examined in each of the four canonical members: `0`;
- distinct accepted `PROPERTY_TYPE` codes: `[]`;
- distinct accepted insurance codes: `[]`.

The runner necessarily processed transient bytes far enough into the first member to evaluate a candidate `PROPERTY_TYPE` and trigger the format guard. No full row was accepted as an examined sample row, and the offending value was not persisted or logged. This audit does not infer or reconstruct that value.

No retry was performed. No second Range GET was issued. No cap was widened.

## Transport Verification

The bounded run verified:

- HEAD status `200`;
- Content-Length `162416884`;
- Content-Type `application/zip`;
- Accept-Ranges `bytes`;
- ETag `"b25b315b6cd8007624387c3a00d4b1fe"`;
- Last-Modified `Wed, 09 Sep 2026 16:32:34 GMT`.

These matched the execution evidence expectations.

## Safety / Persistence

All persisted execution safety flags are `false`, including:

- full archive downloaded;
- raw body persisted;
- temporary source files created;
- full rows persisted;
- `PROPERTY_ID` persisted;
- per-row `PROPERTY_TYPE` persisted;
- owner/holder values persisted;
- identity resolution performed;
- beneficiary matching performed;
- outreach performed;
- production classification activated.

The transient privacy authorization was bounded to in-memory processing with zero-day retention and immediate disposal after projection or STOP.

## Artifact Provenance

Artifact name:
`ca-sco-property-type-semantic-execution-2026-09-15`

Artifact ID:
`10394467215`

Artifact size:
`1283` bytes (ZIP).

Artifact ZIP SHA-256:
`24a39a739872b0d9b3f0bff9a17c22f8ab1a443ddbcf82b7f9126d546ed1a66d`

Contained file:
`ca_sco_segment_500_plus.property_type_semantic.execution.v1.json`

Contained JSON size:
`2730` bytes.

Contained JSON SHA-256 before repository persistence:
`790dabcf1c04946ad930de467f204cb0af6fe78c25bae86b1ca541e4fc07b96a`

Repository evidence path:
`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1.json`

The workflow's evidence-validation step printed:
`BOUNDED_EVIDENCE_VALIDATED`.

## Ephemeral Workflow CI Behavior

The ordinary repository CI triggered by the temporary workflow commit was run `34965098018`.

- `streamlit-candidate`: SUCCESS;
- `quality`: FAILED at contract tests only.

The three failures were the pre-existing steady-state guards that require the one-shot workflow path to be absent. They failed because the workflow deliberately existed during the authorized execution window. Those tests were not weakened or edited.

After the one-shot completed, the workflow was deleted at commit:
`bc1b0a955037d35dfa1a37b0c29497c219a04609`.

There is therefore no remaining workflow capable of automatically repeating the real execution.

## Governance State After Execution

Still closed:

- source policy remains `PROPOSED`;
- real acquisition remains unauthorized by source policy;
- registry remains disabled and not approved;
- approved real sources remain `0`;
- identity resolution remains blocked;
- beneficiary matching remains blocked;
- outreach remains blocked;
- production classification remains inactive.

The bounded execution approval was consumed for this single run. It is not interpreted as authorization to retry.

## Conclusion

The execution demonstrated correct fail-closed behavior but did **not** establish the intended semantic compatibility of `PROPERTY_TYPE`.

The only supported conclusion is:

`PROPERTY_TYPE` semantic verification is unresolved because the first bounded attempt stopped on `PROPERTY_TYPE_FORMAT_UNEXPECTED` before accepting any sample row.

No claim should be made about the offending value or about dataset-wide `PROPERTY_TYPE` semantics.

## Next Gate

`HUMAN_PROPERTY_TYPE_SEMANTIC_EXECUTION_EVIDENCE_REVIEW`

Recommended next work after that human review is diagnosis/design using persisted derived evidence and synthetic reproduction first. A second real network execution requires a new explicit human authorization and must not be inferred from the authorization recorded here.
