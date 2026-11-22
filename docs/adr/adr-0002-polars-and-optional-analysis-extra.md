# ADR-0002 Polars and an optional analysis extra

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0002 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [97a0c3e] |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 (stand-in) | Accepted after review [RC-012]; autonomous mode, not independent | [97a0c3e] |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The project rules prefer polars over pandas and keep dataframes in the outer layers. Stakeholder S03 expects no runtime dependencies, while the notebook needs a dataframe library, plotting and Jupyter.

Options: (a) pandas as a required dependency, as the course teaches; (b) polars as an optional `analysis` extra, with the package core free of third-party imports; (c) no dataframe library, plain Python lists.

## Decision

Use polars, declared only in the optional `analysis` extra of `pyproject.toml`; the core package has no runtime dependencies.

## Consequences

**Positive:**

- `pip install fatal-force` needs nothing else, as S03 expects.
- Polars gives fast, expression-based aggregation.

**Negative:**

- Course solutions that use pandas differ in syntax from this code, so S02 must translate.
- Readers need the extra to run the notebook.

## Affected Artifacts

- [BC-001] — Constraints: no runtime dependencies unless needed.

---

[BC-001]: ../business-case.md
[RC-012]: ../sqa/reviews/rc-012-adr-0002.md
[97a0c3e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/commit/97a0c3e2dbda6cc2d82cb8783b2fc5f3a2a9c60a
