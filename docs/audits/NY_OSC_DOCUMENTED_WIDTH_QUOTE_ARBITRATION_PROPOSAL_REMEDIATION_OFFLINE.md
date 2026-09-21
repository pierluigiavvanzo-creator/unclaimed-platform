# NY OSC Documented-Width Quote Arbitration — Proposal Remediation Offline

Date: 2026-09-21

Classification: `A — Product Critical / Offline Proposal Remediation`

Status:

`REMEDIATED_PROPOSED_NOT_IMPLEMENTED / REPOSITORY_ONLY / ZERO SOURCE ACCESS`

## Requested action

`REMEDIATE_NY_OSC_DOCUMENTED_WIDTH_QUOTE_ARBITRATION_PROPOSAL_OFFLINE`

Additional Product Owner decision:

- prefer the statistically better-supported interpretation only when support clears a
  66% decision threshold;
- if the available evidence does not credibly clear that threshold, treat `"` as a
  literal character and use RAW pipe structure as the Product Owner fallback.

This is recorded as an owner policy. It is not represented as an OSC specification or
source fact.

## Review finding remediated

The prior proposal used documented width to automatically select a grammar:

- RAW 14 / quote-aware !=14 -> accept RAW;
- RAW !=14 / quote-aware 14 -> accept quote-aware.

Review found that this can confuse schema conformity with proof of source dialect.

The remediation separates:

1. **structural classification** — what each candidate interpretation produces;
2. **interpretation policy** — how a candidate is selected when OSC quote semantics are
   not authoritative in the repository.

The existing same-line quote-aware logic is now explicitly called:

`CANDIDATE_SAME_LINE_QUOTE_INTERPRETATION_NOT_OSC_SOURCE_TRUTH`

## Statistical audit of retained evidence

### Non-discriminating evidence

The sixth attempt accepted `165,438` complete records before the first
quote-dialect ambiguity.

Those records are useful evidence that the line-local scanner advanced safely, but they
do not identify which quote grammar is correct when raw and candidate quote-aware
interpretations diverge. They are therefore excluded from the dialect-discriminating
sample.

The fifth attempt strongly rejects unrestricted multiline quote carry because:

`(17,543 + 1) * 13 = 228,072`

but it also does not independently identify whether a double quote on a single physical
line is semantic quoting or literal data.

### Discriminating evidence

The retained sixth blocking diagnostic supplies one discriminating physical record:

- raw field count: `14`;
- candidate quote-aware field count: `6`;
- raw pipe count: `13`;
- candidate quote-aware structural pipes: `5`;
- suppressed pipes: `8`;
- quote-open events: `1`;
- quote-close events: `0`;
- ended inside quote: `true`.

Therefore:

- discriminating records: `1`;
- raw documented-width support: `1`;
- candidate quote-aware documented-width support: `0`;
- raw point estimate among retained discriminating records: `100%`.

A point estimate from one observation is not treated as a reliable probability that RAW
is the true OSC dialect.

To avoid overstating a sample of one, the proposal stores a conservative Wilson
two-sided 95% lower confidence bound for RAW support:

`0.2065432915` (about `20.65%`).

This is below the Product Owner threshold:

`0.66`.

The threshold is therefore recorded as:

`NOT ROBUSTLY MET`.

This does not mean RAW has only a 20.65% probability of being correct. The Wilson value
is a confidence bound on the observed success proportion, not a posterior probability
of the OSC dialect.

## Product Owner fallback

Because the retained evidence is insufficient to establish source semantics above the
66% threshold with robust statistical support, the explicit Product Owner fallback is
activated:

`RAW_PIPE_WITH_DOUBLE_QUOTE_LITERAL`

Basis:

`PRODUCT_OWNER_FALLBACK_DUE_INSUFFICIENT_STATISTICAL_CONFIDENCE`

This selection is intentionally labeled:

`source_truth_claimed = false`.

It is a deterministic product policy for a future implementation candidate, not an
assertion that OSC documents `"` as literal.

## Remediated structural decision matrix

The structural classification now comes before policy resolution:

| Raw | Candidate quote-aware | Quote closed | Structural class | Current owner-policy result |
|---:|---:|---|---|---|
| 14 | 14 | either | `EQUIVALENT_DOCUMENTED_WIDTH` | `ACCEPT_EQUIVALENT_STRUCTURE` |
| 14 | !=14 | either | `RAW_WIDTH_ONLY_DIALECT_UNRESOLVED` | `ACCEPT_RAW_UNDER_CURRENT_OWNER_FALLBACK` |
| !=14 | 14 | yes | `QUOTE_WIDTH_ONLY_DIALECT_UNRESOLVED` | `BLOCK_UNDER_CURRENT_RAW_OWNER_FALLBACK` |
| all other cases | | | `NO_DOCUMENTED_WIDTH_INTERPRETATION` | `BLOCK_FAIL_CLOSED` |

A candidate quote-aware 14-field result is not automatically accepted merely because it
matches documented width.

## Sixth-shape result under current owner policy

The retained sixth shape:

`RAW 14 / candidate quote-aware 6 / open at EOL`

is structurally classified as:

`RAW_WIDTH_ONLY_DIALECT_UNRESOLVED`

and, under the current Product Owner fallback, would resolve to:

`ACCEPT_RAW_UNDER_CURRENT_OWNER_FALLBACK`.

This future behavior is not implemented by this remediation.

## Future statistical evidence

The proposal retains an optional future non-PII full-file structural scan concept for
counting:

- equivalent documented-width records;
- raw-width-only records;
- quote-width-only records;
- neither-width records.

Its purpose would be to increase the dialect-discriminating sample without persisting
owner values, raw rows, row offsets or row hashes.

That scan is:

`PROPOSED_NOT_AUTHORIZED`.

No execution, runtime bridge or persistence contract for it is granted here.

If future evidence robustly supports a candidate interpretation above the Product Owner
66% threshold, that evidence may be brought to a separate human review. Until then, RAW
literal remains the explicit owner fallback.

## Preserved boundaries

No parser implementation.
No runtime activation.
No runtime bridge change.
No execution-result contract change.
No runner change.
No approval creation.
No OSC access.
No remote preflight.
No download.
No owner-PII processing.
No sixth retry.
No seventh-attempt proposal or execution.
No source activation.
No matching or outreach.

The historical `MULTILINE_LEGACY` and `LINE_LOCAL_ARBITRATION` modes remain
unchanged.

## Next gate

`HUMAN_REVIEW_NY_OSC_DOCUMENTED_WIDTH_QUOTE_ARBITRATION_PROPOSAL_REMEDIATION_OFFLINE`
