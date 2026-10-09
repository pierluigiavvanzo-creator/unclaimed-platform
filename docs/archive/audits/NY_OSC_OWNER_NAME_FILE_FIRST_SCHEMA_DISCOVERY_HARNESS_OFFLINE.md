# NY OSC Owner Name File — First Schema Discovery Harness Offline

Date: 2026-09-18

Classification: `A — Product Critical`

Status: `IMPLEMENTED_SYNTHETIC_ONLY_PENDING_GATE2`

## Objective

Prepare the bounded, memory-only schema-discovery execution path that will be needed immediately after a separately approved Gate 2.

This implementation does not perform network access and does not authorize or execute the real Owner Name File download.

## Official instruction evidence now available

The OSC instructions received after Gate 1 document:

- secure FTP retrieval;
- archive name `NYSFINDERS.ZIP`;
- a pipe-delimited text file;
- a 14-field KAPS layout in this order:
  1. Property ID
  2. Property Type Code
  3. Property Type Code Description
  4. Property Owner Count
  5. Owner Name
  6. Owner Address 1
  7. Owner Address 2
  8. Owner Address 3
  9. Owner City
  10. Owner Address State
  11. Owner Zip Code
  12. Owner Country Code
  13. Holder Name
  14. Holder Report Year.

The official screenshot also shows a `Size` column in the secure file-transfer listing before download. Its historical example value is not treated as the current archive size and is not used to set `max_download_bytes`.

The instructions do not state the current archive size or text encoding.

## Reuse-first decision

Reused:

- existing A01 acquisition concepts: explicit approval reference and max-byte bound;
- existing NY source contract and Gate 2 identifier;
- project fail-closed and no-PII-persistence rules;
- Python standard library `io` + `zipfile`;
- existing Pydantic v2 + JSON Schema contract pattern.

No external ZIP/parser/encoding-detection dependency is added.

## Runtime boundary

Serializable authorization contains only non-content controls:

- Gate 2 approval reference;
- `max_download_bytes`;
- `max_uncompressed_bytes`;
- `max_archive_members`;
- documented archive/delimiter expectations;
- hard false flags for raw persistence, row persistence, owner-field logging and row-specific human inspection.

Archive bytes are accepted only as an in-memory function argument. They never appear in JSON contracts.

## Discovery behavior

The harness:

1. checks archive byte length before ZIP parsing;
2. validates ZIP structure in memory;
3. checks member-count cap from ZIP central-directory metadata;
4. requires exactly one `.txt` member;
5. checks that member's uncompressed size before opening it;
6. reads rows as bytes;
7. validates the documented pipe delimiter and 14-field width;
8. persists header names only if the first record is an exact byte-for-byte match to the documented 14-field header;
9. otherwise treats the first record as data and persists no header values;
10. inspects only the documented non-owner `Property Type Code` position for ASCII/alphanumeric shape;
11. returns only aggregate/non-owner schema metadata.

Owner name/address fields are never decoded, logged or returned.

## Persistable outputs

- observed archive byte count;
- archive member count;
- selected text-member presence and uncompressed size;
- observed delimiter;
- documented/observed field count;
- exact documented header names only when actually observed;
- aggregate complete-record count;
- aggregate property-type ASCII-record count;
- deterministic property-type column position mapping state;
- safety flags confirming no raw/row persistence.

Member names are intentionally not persisted by this implementation even though the source policy permits non-owner-identifying names.

## Encoding

Encoding is deliberately not guessed. This first harness performs byte-level layout validation and returns:

`NOT_EVALUATED_BYTE_LEVEL_DISCOVERY_ONLY`

A future Gate 2 execution design may add an explicitly bounded encoding observation if needed; no default encoding is invented here.

## Safety

This package uses synthetic ZIP fixtures only.

It does not:

- connect to OSC secure FTP;
- use received credentials;
- download `NYSFINDERS.ZIP`;
- process real owner PII;
- persist raw bytes or owner rows;
- classify a real property row;
- activate the source;
- perform beneficiary matching or outreach.

## Gate state

Gate 2 remains:

`NOT GRANTED / NOT READY`

The current blocker remains evidence-based current archive size and final Gate 2 authorization.
