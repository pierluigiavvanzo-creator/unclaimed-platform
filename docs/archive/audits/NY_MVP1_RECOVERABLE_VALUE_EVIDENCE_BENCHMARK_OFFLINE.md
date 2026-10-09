# NY MVP-1 Recoverable Value Evidence Paths — Offline Benchmark

Date: 2026-09-18

Classification: `A — Product Critical`

## Objective

Define the smallest lawful and reproducible economics-evidence path for a future New York OSC `IN03 — Proceeds Due Beneficiaries` candidate while the real Owner Name File remains unavailable and Gate 2 remains ungranted.

This benchmark is offline only. It does not download or inspect the Owner Name File, process real owner PII, contact an owner, create a fee agreement, submit a claim, or perform representation.

## Official-source findings

### 1. Owner Name File cannot provide recoverable value

OSC states that the downloadable Owner Name File includes owner name/last-known address, nature of property, when reported and reporting organization, but dollar values are not included and applicable privacy law does not permit disclosure of item amounts in that list.

Product consequence:

`OWNER_NAME_FILE -> recoverable_value = UNKNOWN_FROM_SOURCE`

No proxy derived from property type, reporting organization or reporting age may be promoted to an exact case-level amount.

### 2. Exact amount requires later claim review / ownership verification

OSC's claimant guidance states that the value of funds is not disclosed until the claim has been reviewed. OSC's Unclaimed Funds page states that once ownership is verified, account details and the amount become available.

Product consequence:

`PRE_CONTACT / PRE_CLAIM -> exact value unavailable`

`POST_REVIEW / VERIFIED OWNERSHIP -> exact value evidence may become available`

The platform must preserve this stage boundary rather than inventing a pre-contact amount.

### 3. Location-service fee cap is 15%, but applicability must remain explicit

OSC's current Location Service Providers page states that the maximum fee allowed by law is 15% of cash or value of securities refunded; the owner pays the provider and OSC does not withhold the provider fee.

New York Abandoned Property Law §1416 applies to abandoned-property location services and makes agreements invalid if the fee exceeds 15% of recoverable property. The statute also contains attorney/accountant exceptions in specified circumstances.

Product consequence:

- `1500 bps` is a statutory cap for the APL §1416 location-service scope, not an assumed business revenue rate.
- the actual agreed fee rate remains unknown until supported by a valid agreement;
- applicability of the location-service rule to the eventual operating structure requires legal-scope confirmation;
- the economics engine must never silently use 15% as the actual fee.

### 4. Follow-up cost is not supplied by OSC

No official OSC source provides a fixed per-case investigation/service-provider cost. The platform therefore must derive expected follow-up cost from measured internal workflow costs and/or explicit authorized external-cost evidence.

Product consequence:

`expected_follow_up_cost = NOT_MEASURED` until supported by explicit evidence.

## Evidence hierarchy

Highest to lowest evidentiary quality for economics:

1. official case-specific amount after permitted claim review / ownership verification;
2. explicit valid fee-rate evidence for the applicable legal scope;
3. measured case-specific or empirically benchmarked follow-up costs with provenance;
4. aggregate/statistical proxies, retained only as proxies and never relabeled as exact case value.

The pre-contact Owner Name File alone cannot satisfy item 1.

## Deterministic economics contract decision

Use integer cents and basis points rather than floating-point monetary values.

Pre-contact state:

- exact recoverable value: unknown;
- Owner Name File amount disclosure: false;
- statutory location-service cap: 1500 bps;
- actual fee rate: unknown;
- expected follow-up cost: not measured;
- commercial actionability: not computable.

Later explicit-input calculation is allowed only when the caller supplies:

- exact recoverable value in cents plus evidence ref;
- agreed fee rate in basis points plus evidence ref;
- measured follow-up cost in cents plus evidence ref;
- explicit confirmation that the calculation is using the APL §1416 location-service scope.

The calculation produces arithmetic only. It does not make a continue/stop recommendation, create an agreement, or authorize outreach/claim activity.

## Reuse decision

Reused:

- existing Pydantic v2 typed-domain pattern;
- existing JSON Schema draft 2020-12 contract pattern;
- deterministic/fail-closed project conventions;
- standard-library `decimal.Decimal` only for cent rounding.

No new rules engine, finance library or currency dependency is justified for three explicit integer inputs and one statutory cap.

Decision:

`REUSE EXISTING STACK > NEW DEPENDENCY`

## Official sources

Accessed 2026-09-18:

- NY OSC — Owner Name File Request Form:
  https://www.osc.ny.gov/unclaimed-funds/resources/owner-name-file-request-form
- NY OSC — Location Service Providers:
  https://www.osc.ny.gov/unclaimed-funds/resources/location-service-providers
- NY OSC — How to Search & Claim Property:
  https://www.osc.ny.gov/unclaimed-funds/claimants/how-search-claim-property
- NY OSC — Unclaimed Funds:
  https://www.osc.ny.gov/unclaimed-funds
- New York Senate Open Legislation — Abandoned Property Law §1416:
  https://www.nysenate.gov/legislation/laws/ABP/1416

## Product contribution

This removes ambiguity from A15 Case Economics before a real NY candidate exists. Once a lawful exact amount, fee-rate evidence and measured cost exist, economics can be computed deterministically without changing the data-source or privacy gates.

Until then, the platform correctly returns `NOT_COMPUTABLE_PRE_CONTACT` instead of manufacturing an expected recovery value.
