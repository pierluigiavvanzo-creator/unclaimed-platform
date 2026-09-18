# NY OSC Property Type Field Shape — Offline Root-Cause Remediation

Date: 2026-09-18

Status: `IMPLEMENTED_SYNTHETIC_ONLY / REAL RERUN NOT AUTHORIZED`

## Trigger

The first real bounded schema-discovery execution stopped fail-closed with:

`PROPERTY_TYPE_CODE_FIELD_SHAPE_UNEXPECTED`

The one-shot Gate 2 and transient-local-file approvals are consumed and non-reusable.

## Root-cause finding

The harness coupled physical schema discovery to semantic value-shape validation.

For the physical schema question, the authoritative invariant is:

- one text member;
- pipe-delimited records;
- exactly 14 fields;
- documented Property Type Code position at index 1.

Requiring every observed Property Type Code field to be non-empty ASCII/alphanumeric was stronger than necessary for schema discovery.

The real execution output intentionally did not retain the offending value, so it does not establish whether the trigger was:

- a BOM/header variant; or
- a legitimate non-alphanumeric/blank code representation.

No claim is made about which occurred.

## Remediation

Offline code now:

- recognizes the exact documented header with or without a UTF-8 BOM;
- still fails closed on any non-14-field data record;
- no longer blocks physical schema discovery solely because the Property Type Code field is non-alphanumeric or blank;
- retains only an aggregate count of alphanumeric Property Type Code fields;
- keeps semantic code validation deferred to a later separately authorized stage;
- continues to return no owner values.

Synthetic regression tests cover:

- UTF-8 BOM documented header;
- hyphenated code shape;
- space-containing code shape;
- blank code shape;
- owner-value non-persistence.

## Authorization boundary

No real rerun is authorized by this remediation.

A fresh human authorization is required before any new Owner Name File access.
