# M3 California SCO — Transport + Archive-Layout Baseline Refresh Proposal

Date: 2026-09-17

Class: **A — Product Critical / MVP-1 critical-path enabler**

Status: **PROPOSAL ONLY — REPOSITORY-ONLY — NO NETWORK EXECUTION AUTHORIZED**

## 1. Product purpose

This proposal exists only to remove the current source blocker on the shortest safe path to:

`MVP-1 — First Economically Actionable Case`.

It is not an open-ended archive diagnostic and does not expand the platform architecture.

The current real-source runner stopped correctly on `TRANSPORT_METADATA_DRIFT` before reading any source-body bytes. The accepted evidence review established that both transport identity and the four pinned ZIP local-header offsets are stale for future execution planning and cannot be refreshed independently.

This proposal defines the minimum deterministic method for a later, separately authorized metadata/structure-only revalidation.

## 2. Current blocker

The reviewed runner currently pins:

- content length `162416884`;
- ETag `"b25b315b6cd8007624387c3a00d4b1fe"`;
- media type `application/zip`;
- `Accept-Ranges: bytes`;
- four local-header offsets:
  - `From_500_To_Beyond_1_of_4.csv` -> `0`;
  - `From_500_To_Beyond_2_of_4.csv` -> `59747797`;
  - `From_500_To_Beyond_3_of_4.csv` -> `96862896`;
  - `From_500_To_Beyond_4_of_4.csv` -> `134174190`.

The single authorized real-source execution observed a different content length and ETag and therefore stopped before any Range request.

No new baseline has been adopted.

## 3. Design principle

Do not rediscover local-header offsets by scanning CSV data, downloading the archive, probing historical offsets or arithmetically rebasing old offsets.

Use the ZIP format's own structural metadata:

`HEAD -> bounded ZIP tail -> End Of Central Directory -> exact Central Directory range -> canonical member offsets`

This path reads ZIP structure only and does not decompress or inspect CSV record contents.

## 4. Strategies considered

### Option A — ZIP Central Directory revalidation

Method:

1. verify current transport identity with one `HEAD`;
2. fetch only the bounded ZIP tail needed to locate the End Of Central Directory (EOCD);
3. derive the Central Directory byte range from EOCD metadata;
4. fetch only that exact bounded Central Directory range if it is not already fully present in the tail response;
5. parse canonical filenames and their recorded relative local-header offsets;
6. persist only derived transport/archive-layout evidence;
7. do not modify runner constants during the execution.

Benefits:

- deterministic;
- does not depend on historical offsets;
- does not inspect CSV rows;
- bounded to at most two small body ranges after HEAD;
- directly produces the values needed to evaluate a fresh baseline;
- preserves fail-closed behavior.

Decision: **RECOMMENDED**.

### Option B — Probe around historical local-header offsets

Method:

Request small ranges around the four old offsets and search for ZIP local headers.

Problem:

- assumes historical layout remains approximately correct;
- can miss members after arbitrary archive re-layout;
- risks creating repeated probing logic;
- does not independently establish the archive directory.

Decision: **REJECT**.

### Option C — Arithmetic rebasing from content-length delta

Method:

Shift historical offsets according to archive-size change.

Problem:

- has no ZIP structural basis;
- a size delta does not identify where bytes changed;
- explicitly conflicts with the accepted evidence-review boundary.

Decision: **REJECT**.

### Option D — Sequential archive scan

Method:

Walk local headers from byte zero until all members are found.

Problem:

- can require many requests or substantial compressed-body traversal;
- larger body exposure than necessary;
- inferior to using the Central Directory.

Decision: **REJECT**.

### Option E — Full ZIP download

Problem:

- unnecessary for archive-layout verification;
- violates current bounded/privacy posture;
- materially increases cost and risk without improving the immediate MVP-1 blocker resolution.

Decision: **REJECT**.

## 5. Proposed future execution boundary

This proposal itself performs **zero** network requests.

A later execution may occur only after separate human review and fresh single-use authorization.

### Request budget

Maximum:

- HEAD requests: `1`;
- Range GET requests: `2`;
- total HTTP requests: `3`;
- maximum bytes per Range response: `131072`;
- maximum total response-body bytes: `262144`;
- full-body fallback: `false`;
- automatic range widening: `false`.

This is stricter than the prior semantic-run total HTTP/body caps and is sufficient for the proposed structural method if the archive remains within the supported bounded ZIP shape.

### Request 1 — HEAD

Required conditions:

- exact reviewed endpoint;
- HTTPS;
- exact allowlisted host;
- status `200`;
- media type `application/zip`;
- `Accept-Ranges: bytes`;
- positive parseable content length;
- non-empty ETag suitable for an `If-Match` guard.

Persistable derived transport evidence:

- observation timestamp;
- endpoint/host;
- status;
- content length;
- media type;
- Accept-Ranges;
- ETag;
- Last-Modified if present.

Failure of any required condition -> `STOPPED_FAIL_CLOSED`.

### Request 2 — bounded ZIP tail

Use `If-Match` with the HEAD ETag.

Request the final `65577` bytes when the object is at least that large, otherwise the complete object only if its full length is itself <= `65577` and the execution contract explicitly permits that bounded case.

Rationale for `65577`:

- maximum classic ZIP comment length: `65535` bytes;
- EOCD fixed record: `22` bytes;
- additional room: `20` bytes for deterministic detection of a ZIP64 locator immediately before EOCD.

The execution must not treat ZIP64 as implicitly supported.

Required validation:

- HTTP `206` for a ranged object;
- exact `Content-Range` consistent with the HEAD length;
- ETag/If-Match identity preserved;
- one valid EOCD record whose comment-length field makes the EOCD terminate exactly at archive end;
- single-disk classic ZIP values;
- no ZIP64 sentinel values and no ZIP64 locator requiring extended parsing.

ZIP64 detection -> fail closed with a dedicated structural reason. Supporting ZIP64 would require a separate reviewed design, not automatic widening.

### EOCD-derived Central Directory checks

Derive:

- total entry count;
- Central Directory offset;
- Central Directory byte size.

Validate before another request:

- offset and size are non-negative and within the HEAD content length;
- `central_directory_offset + central_directory_size` does not exceed archive length;
- Central Directory size <= `131072`;
- entry count is bounded and parseable under the proposal contract.

If the full Central Directory is already contained in the tail response, do not issue Request 3.

### Request 3 — exact Central Directory range, only if needed

Request exactly:

`central_directory_offset .. central_directory_offset + central_directory_size - 1`

with `If-Match` set to the HEAD ETag.

Required:

- HTTP `206`;
- exact `Content-Range`;
- body length exactly equals EOCD-declared Central Directory size;
- no response outside the declared byte range.

No local-file compressed data is intentionally requested by this step.

## 6. Central Directory parser boundary

The parser must be purpose-built and bounded to ZIP structural records only.

It may inspect only fields needed to establish:

- entry boundaries;
- filename encoding flag;
- filename;
- relative local-header offset;
- ZIP64 requirement indicators;
- record count consistency.

It must not:

- decompress file data;
- access CSV contents;
- parse rows;
- inspect PROPERTY_ID, PROPERTY_TYPE, owner or holder fields;
- infer source semantics.

### Canonical member requirement

The following names must each occur exactly once:

- `From_500_To_Beyond_1_of_4.csv`;
- `From_500_To_Beyond_2_of_4.csv`;
- `From_500_To_Beyond_3_of_4.csv`;
- `From_500_To_Beyond_4_of_4.csv`.

For the first refresh execution, use an exact-set policy: any additional Central Directory member or any missing/duplicate canonical member causes fail-closed structural review rather than silent acceptance.

The four derived local-header offsets must be:

- distinct;
- non-negative;
- strictly before the Central Directory offset;
- within the current HEAD content length.

The refresh task does **not** fetch those local headers and does not inspect their compressed payloads. Existing semantic execution already verifies the local-header signature and canonical filename before decompression; that verification remains in the later semantic-run layer.

## 7. Proposed output evidence

A later refresh execution may persist only non-record transport/archive metadata:

- execution id and timestamp;
- approval reference;
- endpoint identity;
- HEAD transport metadata;
- request/byte counters;
- EOCD status;
- ZIP64 detected boolean;
- Central Directory offset and size;
- Central Directory entry count;
- exact canonical member names;
- derived relative local-header offsets;
- structural result status / reason code;
- safety flags proving no CSV/file-data/row access.

It must not persist raw range bytes.

Resulting values are a **baseline candidate**, not automatically adopted runtime constants.

Suggested success status:

`BASELINE_CANDIDATE_STRUCTURALLY_VERIFIED`

Suggested failure family:

- `TRANSPORT_METADATA_INVALID`;
- `RANGE_IDENTITY_MISMATCH`;
- `EOCD_NOT_UNIQUELY_RESOLVED`;
- `ZIP64_UNSUPPORTED_BOUNDED_REFRESH`;
- `CENTRAL_DIRECTORY_BOUNDS_INVALID`;
- `CENTRAL_DIRECTORY_CAP_EXCEEDED`;
- `CENTRAL_DIRECTORY_PARSE_ERROR`;
- `CANONICAL_MEMBER_SET_MISMATCH`;
- `LOCAL_HEADER_OFFSET_INVALID`.

Exact machine-contract vocabulary, if implemented, must be versioned and tested before execution.

## 8. Privacy boundary

This structural refresh is designed not to expose record data.

Permitted transient bytes:

- ZIP tail containing archive-directory structures/comment bytes;
- exact Central Directory bytes.

Prohibited:

- local member compressed payloads;
- decompressed CSV bytes;
- rows or fields;
- PII processing;
- identity resolution;
- genealogy;
- beneficiary matching;
- outreach;
- claim activity.

If implementation analysis shows that a required Range can overlap local file payload beyond structural bytes in a way that exceeds the reviewed privacy boundary, execution must stop and a separate privacy review is required.

## 9. Adoption boundary

A successful structural refresh execution does not itself update:

- `EXPECTED_LENGTH`;
- `EXPECTED_ETAG`;
- `CANONICAL_MEMBERS` offsets;
- source policy;
- registry approval;
- production classification.

After successful evidence is produced, a human review must decide whether the candidate baseline is sufficiently coherent to adopt.

Only after that review may a separate repository task update the runner pins and tests.

No consumed approval may be reused for either refresh execution or subsequent semantic execution.

## 10. MVP-1 acceleration rule

Once a coherent baseline is reviewed and adopted, the next priority is not another archive diagnostic.

The project should move directly to the smallest freshly authorized real-source semantic verification needed to determine whether the source can become approved and then enter the MVP-1 vertical slice.

Do not add unrelated infrastructure, multi-state support, genealogy automation or additional agent layers while this critical path remains blocked.

## 11. REUSE FIRST result

No external ZIP library is required for the proposal itself.

For a later implementation, use Python standard-library `struct` plus a small bounded structural parser unless repository scouting identifies a mature component that can parse Central Directory metadata from caller-supplied bounded byte buffers without performing its own file/network reads or widening access.

Do not adopt a general archive extraction library merely for popularity if it requires seekable/full-file access or obscures byte-access boundaries.

## 12. Acceptance criteria for this proposal

PASS only if the proposal:

1. performs no network access;
2. does not adopt the observed 2026-09-16 content length/ETag;
3. does not infer or rebase member offsets;
4. derives future offsets only from ZIP Central Directory structure;
5. limits future execution to <= 1 HEAD + <= 2 Range requests;
6. keeps total response-body access <= 262144 bytes;
7. performs no CSV decompression or row access;
8. fails closed on ZIP64, structural ambiguity, cap excess or canonical-member mismatch;
9. requires fresh single-use authorization before any network request;
10. keeps source policy, registry, production classification and downstream gates closed;
11. treats any execution output as a candidate baseline requiring later human adoption review;
12. explicitly serves the MVP-1 first-approved-real-source critical path.

## 13. Next gate

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_REVIEW`

The review may approve, amend or reject this design.

Approval of the proposal would authorize only a later implementation/preparation task unless the owner explicitly grants a fresh execution authorization. It does not by itself authorize any network request.
