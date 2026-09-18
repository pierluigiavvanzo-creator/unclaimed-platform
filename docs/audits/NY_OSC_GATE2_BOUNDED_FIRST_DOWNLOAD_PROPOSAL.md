# NY OSC Gate 2 — Bounded First Download Proposal

Date: 2026-09-18

Status: `PENDING_HUMAN_AUTHORIZATION_AND_EXECUTION_TRANSPORT_READINESS`

## New current-size evidence

Product Owner supplied a screenshot of the OSC secure-transfer outbound listing.

Observed:

- remote listing name: `FINDERS.zip`;
- displayed size: `390.51 MB`;
- displayed last modified: `9/16/2026, 1:33:31 PM`.

No download occurred.

The portal does not expose exact byte semantics in the screenshot. Therefore both common interpretations are recorded:

- decimal MB: `390,510,000` bytes;
- binary MiB-equivalent ceiling: `409,479,414` bytes.

The proposed compressed transfer cap is:

`max_download_bytes = 450,000,000`

This is a byte-safety ceiling, not a claim about the exact file size. Preflight must also match the observed name, displayed size and last-modified value. Any drift stops execution before download and requires fresh review.

## Proposed expansion bounds

- `max_uncompressed_bytes = 2,000,000,000`;
- `max_archive_members = 1`;
- exactly one text member;
- downloads max = 1;
- retries max = 0.

The uncompressed cap is a safety ceiling only. The ZIP central directory must report a member size inside the cap before any member content is read.

## Filename evidence

Official OSC instructions use multiple filename forms across pages, including `NYSFINDERS.ZIP` and `FINDERS.ZIP`. The current portal listing observed by the Product Owner is `FINDERS.zip`.

The real-execution identity target is therefore the current listing, not a normalized/invented filename.

## Execution-transport blocker

The official OSC instructions describe browser download as saving the ZIP to the user's computer.

Current project policy for Gate 2 requires:

`MEMORY_ONLY`

with:

`raw_file_persistence_allowed = false`

A normal browser save-to-disk therefore does not satisfy the existing privacy/retention boundary.

Gate 2 execution must not occur until one of these is separately resolved:

1. an authenticated transfer path is implemented and verified to keep raw archive bytes memory-only; or
2. the Product Owner explicitly approves a separate transient-local-file policy expansion with immediate deletion and no repository/chat/cloud persistence.

This blocker is operational, not a reason to weaken the existing schema-discovery harness.

## Proposed Gate 2 approval reference

`APPROVE_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_BOUNDED_ONCE`

Single-use, non-reusable, no retry.

Proposal preparation itself does not grant authorization.
