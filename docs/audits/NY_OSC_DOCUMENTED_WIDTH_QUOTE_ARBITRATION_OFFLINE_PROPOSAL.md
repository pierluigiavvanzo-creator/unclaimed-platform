# NY OSC Documented-Width Quote Arbitration — Offline Proposal

Date: 2026-09-21

Classification: `A — Product Critical / Offline Parser Proposal`

Status:

`PROPOSED_NOT_IMPLEMENTED / REPOSITORY_ONLY / ZERO SOURCE ACCESS`

## Requested action

`PREPARE_NY_OSC_DOCUMENTED_WIDTH_QUOTE_ARBITRATION_OFFLINE_PROPOSAL`

This package proposes a deterministic parser-arbitration design only. It does not
modify the parser, runtime bridge, execution contracts, runner, approval artifacts or
source policy, and it does not prepare or authorize a seventh attempt.

## Baseline

Source branch:

`ny-osc-sixth-approval-grants`

Baseline checkpoint:

`a8203a8c0d4e741424c68e171b2f5e4e956207a5`

Baseline CI:

`35578442808 — SUCCESS`

The sixth bounded attempt is already:

`CONSUMED_SINGLE_USE_NON_REUSABLE / ZERO RETRY`

## Evidence basis

The official instruction evidence already retained in the repository documents a
pipe-delimited 14-field KAPS layout. The repository does not contain an authoritative
OSC specification that defines double-quote escaping, multiline records or a global
text-qualifier dialect.

Fifth-attempt structural evidence:

- `physical_line_breaks_inside_quotes = 17,543`;
- `raw_pipe_count = 228,072`;
- exact identity: `(17,543 + 1) * 13 = 228,072`.

This shows that a persistent multiline quote interpretation can absorb the structural
equivalent of 17,544 ordinary 14-field physical rows after one quote-open event.

Sixth-attempt line-local evidence:

- result: `BLOCKED / QUOTE_DIALECT_AMBIGUOUS`;
- complete records before block: `165,438`;
- raw fields: `14`;
- quote-aware fields: `6`;
- raw pipes: `13`;
- quote-aware structural pipes: `5`;
- suppressed pipes: `8`;
- quote bytes: `1`;
- quote-open events: `1`;
- quote-close events: `0`;
- ended inside quote: `true`.

For that physical line, raw pipe interpretation has exactly the documented 14-field
width while the same-line quote-aware interpretation does not.

## Bounded conclusions

Supported:

1. Global multiline quote state is not sufficiently supported to be trusted as the
   source-wide dialect.
2. The evidence does not support treating every double quote as structurally
   meaningful.
3. The evidence also does not prove that every double quote is literal data.
4. A seventh real download is not required to design and test a safer offline
   arbitration candidate.

Not claimed:

- the exact source-wide quote dialect;
- that OSC never uses quoted fields;
- that the sixth blocking record was malformed;
- that owner-field values can be inferred from structural counters.

## Proposed algorithm

Candidate mode:

`DOCUMENTED_WIDTH_ARBITRATION`

Physical record boundary:

`LF_OR_CRLF_HARD_BOUNDARY`

Quote state must never cross a physical record boundary.

Each physical line is evaluated under two structural interpretations:

1. raw pipe: every `|` is a structural delimiter;
2. same-line quote-aware: existing same-line quote rules may suppress pipe bytes while
   the quote state is open.

Decision rules:

| Raw fields | Quote-aware fields | Quote closed in line | Proposed result |
|---:|---:|---|---|
| 14 | 14 | either | `ACCEPT_EQUIVALENT_STRUCTURE` |
| 14 | not 14 | either | `ACCEPT_RAW_UNIQUE_DOCUMENTED_WIDTH` |
| not 14 | 14 | yes | `ACCEPT_QUOTE_AWARE_UNIQUE_DOCUMENTED_WIDTH` |
| all other cases | | | `BLOCK_NO_UNIQUE_DOCUMENTED_WIDTH` |

The quote-aware scanner may suppress raw pipe delimiters but may not create new pipe
delimiters. Therefore equal raw and quote-aware field counts imply no structural pipe
suppression.

No source-wide dialect is inferred from any accepted line.

## Sixth-shape consequence

The retained sixth diagnostic maps to:

`raw 14 / quote-aware 6 / ended-inside-quote true`

Under this proposal the line would use:

`ACCEPT_RAW_UNIQUE_DOCUMENTED_WIDTH`

because raw is the only interpretation matching the documented 14-field width.

This is a proposed deterministic structural rule, not an assertion about the semantic
meaning of the double quote.

## Same-line quoted-pipe consequence

A synthetic same-line quoted pipe can produce:

`raw 15 / quote-aware 14 / quote closed`

Under this proposal the quote-aware interpretation is the only documented-width
interpretation and would be selected.

If the quote is still open at the physical line boundary, the same shape must block.

## Synthetic acceptance matrix

The proposal requires synthetic coverage before any implementation can be accepted:

- plain 14-field row;
- balanced quotes without a pipe;
- sixth-shaped `14 / 6 / open` line;
- same-line quoted pipe `15 / 14 / closed`;
- true 13-field row;
- `15 / 15` invalid-width row;
- quote-aware 14 fields but open quote at EOL;
- privacy serialization proving no owner value or raw record escapes.

## Proposed non-PII observability

Future implementation may expose aggregate counters to a diagnostic sink:

- `structure_equivalent_record_count`;
- `raw_unique_documented_width_record_count`;
- `quote_aware_unique_documented_width_record_count`;
- `blocked_no_unique_documented_width_record_count`.

Persistence or runtime bridging of these counters is not authorized by this proposal.

Forbidden:

- raw record bytes;
- owner values;
- row offsets;
- row hashes.

## Implementation boundary

This proposal requires any later implementation to be additive:

- historical `MULTILINE_LEGACY` behavior unchanged;
- historical `LINE_LOCAL_ARBITRATION` behavior unchanged;
- existing default mode unchanged;
- only a new explicit mode may be added.

This proposal does not authorize:

- parser implementation;
- runtime activation;
- execution-result contract changes;
- runner changes;
- approval artifact creation;
- seventh-attempt proposal or execution;
- OSC access, preflight or download;
- source activation or production classification;
- identity resolution, matching, outreach or claim activity.

## Repository artifacts

- `sources/proposals/ny_osc_documented_width_quote_arbitration_offline_proposal.v1.json`;
- `schemas/common/ny_osc_documented_width_quote_arbitration_offline_proposal.schema.json`;
- `tests/contract/test_ny_osc_documented_width_quote_arbitration_offline_proposal.py`;
- this audit.

## Next gate

`HUMAN_REVIEW_NY_OSC_DOCUMENTED_WIDTH_QUOTE_ARBITRATION_OFFLINE_PROPOSAL`


## Verification

Functional verification checkpoint:

`0b659ab9c6429e6f265753f2817d63c8303ac2e2`

GitHub CI:

`35582725552 — SUCCESS`

Results:

- Ruff: PASS;
- mypy core: 19 source files PASS;
- mypy NY OSC runtime: 2 source files PASS;
- contract tests: 377 passed;
- smoke tests: 16 passed;
- full pytest: 540 passed;
- Streamlit safety/startup: PASS;
- frontend lint/typecheck/build: PASS.

No parser/runtime/runner/source behavior was changed by this proposal package.
