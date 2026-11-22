# ADR-0003 Dataframe code lives in the infrastructure layer

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0003 |
| CrossReference | [BC-001], [ADR-0002] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 (stand-in) | Accepted after review [RC-014]; autonomous mode, not independent | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The project rules keep dataframes in the outer layers and let the inner layers use plain dataclasses. The assignment is mostly dataframe work: reading CSV files, cleaning, grouping and counting. Placing every grouping function in `domain` would make the business layer depend on polars.

Options: (a) all dataframe functions in `domain`; (b) dataframe functions in `infrastructure`, plain dataclasses such as the frame summary in `domain`, plotting in `presentation`; (c) a single flat module.

## Decision

Keep dataframe reading, cleaning and aggregation in `src/fatal_force/infrastructure/`, keep result types as frozen dataclasses in `domain/`, and keep plotting in `presentation/`.

## Consequences

**Positive:**

- `domain` and `application` import nothing third-party, so the layers contract stays checkable with import-linter.
- Plotting can be replaced without touching the aggregation.

**Negative:**

- Functions that a course reader expects "next to the analysis" sit in `infrastructure`, which needs a sentence of explanation in the README and wiki.
- Some mapping between frames and dataclasses is needed.

## Affected Artifacts

- [BC-001] — Constraint: no runtime dependencies unless needed.
- [ADR-0002] — builds on the choice of polars.

---

[BC-001]: ../business-case.md
[ADR-0002]: ./adr-0002-polars-and-optional-analysis-extra.md
[RC-014]: ../sqa/reviews/rc-014-adr-0003.md
