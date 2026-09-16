# M3 California SCO — PROPERTY_TYPE Transport + Archive-Layout Baseline Refresh Proposal

Date: 2026-09-16

Status: **PROPOSAL PREPARED — REPOSITORY-ONLY — NETWORK NOT AUTHORIZED — NO REBASELINE PERFORMED**

## Proposal gate

`PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL`

## Base checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- base branch: `m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-evidence-review`
- base HEAD: `9dbdc3c6f1ef05c577c26c9e3524ba74fdbfda56`
- base CI: `35125609902` — **SUCCESS**
- evidence-review result: `PASS_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_ACCEPTED_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_JUSTIFIED_NO_REBASELINE_RETRY_OR_RUNTIME_CHANGE_AUTHORIZED`

This proposal is repository-only. It performs no California SCO request, no HEAD, no Range GET, no authority retrieval, no archive download, no source-body inspection and no retry.

## Objective

Define the smallest deterministic and fail-closed design by which a later separately authorized task could establish a fresh candidate transport identity **and** fresh candidate ZIP local-header offsets for the four canonical `$500+` CSV members without silently adopting the one-shot drift observation and without broad archive acquisition.

The proposal does not change the current runner. It does not declare the historical offsets wrong. It does not adopt the observed ETag or content length. It does not authorize a future execution by itself.

Machine-readable proposal:

`sources/proposals/ca_sco_segment_500_plus.property_type_transport_archive_layout_baseline_refresh.v1.json`

Schema:

`schemas/common/property_type_transport_archive_layout_baseline_refresh_proposal.schema.json`

Contract test:

`tests/contract/test_ca_sco_property_type_transport_archive_layout_baseline_refresh_proposal.py`

## REUSE FIRST result

The design reuses the already reviewed project boundaries rather than creating a new acquisition path:

- existing exact segment endpoint `https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`;
- existing exact host `claimit.ca.gov` and HTTPS-only posture;
- prior metadata-only transport-preflight pattern;
- existing semantic-runner request limits: one HEAD, at most four Range requests, five HTTP requests total;
- existing `131072` byte maximum per Range response;
- existing `524288` byte maximum total source response-body budget;
- existing `If-Match` same-object protection concept;
- current four canonical member names;
- current fail-closed governance and human-gate model.

No central-directory/EOCD runtime implementation currently exists in the repository. This proposal therefore describes the future structural verifier contract only; it does not add such a parser to production or execution code.

## Evidence boundary

The accepted one-shot evidence establishes only:

- a HEAD request succeeded with HTTP `200`;
- live content length was `162560390` rather than pinned `162416884`;
- live ETag was `"222dd79f04c2a0a8fff166b01c8da746"` rather than pinned `"b25b315b6cd8007624387c3a00d4b1fe"`;
- media type remained `application/zip`;
- `Accept-Ranges` remained `bytes`;
- the runner stopped `STOPPED_FAIL_CLOSED / TRANSPORT_METADATA_DRIFT`;
- zero source-body bytes and zero rows were read.

Those observed values remain evidence from one observation. They are **not** a replacement baseline.

The historical canonical member offsets remain:

1. `From_500_To_Beyond_1_of_4.csv` → `0`;
2. `From_500_To_Beyond_2_of_4.csv` → `59747797`;
3. `From_500_To_Beyond_3_of_4.csv` → `96862896`;
4. `From_500_To_Beyond_4_of_4.csv` → `134174190`.

They are stale for future execution planning but not proven invalid.

## Strategy assessment

Four deterministic options were evaluated.

### 1. HEAD-only transport refresh — rejected

A new HEAD could establish a fresh transport observation but cannot establish the current ZIP member layout or local-header offsets. Updating only content length and ETag would leave the runner coupled to unverified historical offsets.

### 2. Arithmetic member-offset rebase — rejected

The archive-length delta gives no evidence about where bytes were added or removed. Adding that delta to historical offsets, proportionally scaling offsets or using any similar arithmetic inference would invent source structure and is forbidden.

### 3. Full archive download and inspection — rejected

A full ZIP download is unnecessary to answer the layout question and would violate the current privacy-minimized, byte-bounded approach.

### 4. Bounded ZIP central-directory metadata revalidation — proposed for human review

A later authorized verifier may first obtain a same-session HEAD observation, then use bounded Range requests to inspect only ZIP structural metadata near the archive tail and, if needed, the central-directory region. The central directory provides member names and relative local-header offsets without requiring decompression or CSV-row parsing.

This option is proposed, not approved.

## Proposed later execution design

### Phase A — transport identity

A future separately authorized verifier would perform at most one HEAD request to the exact existing endpoint and record:

- HTTP status;
- content length;
- ETag;
- content type;
- Accept-Ranges;
- Last-Modified when present;
- observation timestamp.

No candidate value is precommitted by this proposal.

### Phase B — bounded ZIP structural metadata

Only after Phase A succeeds, a later verifier may use at most four Range requests, each at most `131072` bytes, with a total source response-body ceiling of `524288` bytes.

The intended method is:

1. inspect a bounded archive-tail window to locate a classic ZIP End of Central Directory record;
2. derive the central-directory location from that ZIP metadata, not from historical member offsets;
3. if required and still within the same reviewed budgets, request only the bounded central-directory bytes needed for structural parsing;
4. extract only the four canonical member names and their central-directory `relative offset of local header` values;
5. verify that each canonical name is unique and each candidate offset lies within the HEAD-observed archive length.

Every Range must be bound to the same observed object through `If-Match`/ETag consistency. `Content-Range` totals must agree with the HEAD-observed content length.

The structural verifier must not:

- decompress member data;
- parse CSV;
- inspect rows or fields;
- use historical offsets to discover the new offsets;
- infer offsets from the content-length delta;
- fall back to a full-body download;
- widen byte/request limits automatically;
- retry automatically.

Classic ZIP layout is the only proposed structural path. ZIP64, multi-disk ZIP, missing/ambiguous EOCD, missing/duplicate canonical members, object identity changes, or inability to complete the structural read within existing budgets must stop fail-closed with no candidate-baseline adoption.

## Why the existing caps are preserved

The evidence review required preservation of current sample/privacy/request boundaries unless a separately reviewed design justified changing them. This proposal does **not** widen them:

- HEAD max: `1`;
- Range max: `4`;
- HTTP total max: `5`;
- Range response max each: `131072` bytes;
- total source response-body max: `524288` bytes;
- no full-body fallback;
- no automatic widening;
- no automatic retry.

If the live ZIP central directory cannot be resolved inside these limits, the correct result is a fail-closed stop and a new design gate, not a larger implicit request.

## Privacy design

A tail Range may contain opaque compressed bytes adjacent to ZIP structural metadata even when no payload is parsed. Therefore a later network execution must require a **fresh single-use structural-byte privacy approval** in addition to a fresh single-use execution approval.

The future privacy boundary is:

- Range bytes memory-only;
- retention `0` days;
- immediate disposal;
- raw Range bytes not persisted;
- compressed payload not decompressed or interpreted;
- CSV not parsed;
- no row, `PROPERTY_TYPE`, `PROPERTY_ID`, owner/holder or other protected field observed;
- noncanonical member names not persisted;
- only bounded derived transport/layout evidence may persist.

Allowed derived evidence is limited to transport metadata, observation time, canonical member names, canonical local-header offsets, canonical-match status, aggregate additional-member count, revalidation result and stop reason.

No current privacy approval is reusable. No fresh approval is granted by this proposal.

## Baseline adoption boundary

A future successful structural execution may produce a **candidate** replacement baseline only. It may not update the semantic runner in the same task.

Adoption requires, in order:

1. separately authorized bounded revalidation;
2. persisted privacy-safe candidate evidence;
3. human evidence review;
4. a separate implementation gate before modifying `EXPECTED_LENGTH`, `EXPECTED_ETAG` or canonical member offsets;
5. CI-green verification of that later implementation.

Therefore all candidate replacement values remain `null` in the present proposal.

## Runtime and D-008 non-impact

Unchanged:

- runner: `scripts/ca_sco_property_type_semantic_verification.py`;
- runtime contract: `1.2.0`;
- `PROPERTY_TYPE` regex: `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- parser/projector behavior;
- trimming/casing/normalization behavior;
- D-008 `WHOLE_SOURCE_STOP` policy;
- `ADDITIVE_VERSIONED_CONTROL_DISPOSITION` implementation strategy.

This proposal makes no new claim about `PROPERTY_TYPE` semantics and does not authorize another semantic sample.

## Source/downstream governance

Still closed:

- network execution authorization: `false`;
- workflow creation authorization: `false`;
- retry authorization: `false`;
- source policy: `PROPOSED`;
- registry enabled: `false`;
- registry approved for use: `false`;
- approved real sources: `0`;
- source continuation: `false`;
- semantic compatibility resolved: `false`;
- production classification: inactive;
- identity resolution: blocked;
- genealogy: blocked;
- beneficiary matching: blocked;
- outreach: blocked;
- claim submission: blocked.

`DECISIONS.md` is not changed because this is a bounded proposal for review under existing deterministic/fail-closed governance, not an accepted architectural decision.

## Next gate

Stop at:

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_REVIEW`

That review may accept, reject or require revision of the proposed bounded central-directory strategy. It must not itself perform a source request unless a later handover explicitly makes a separately authorized execution the single next action.
