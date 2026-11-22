# MIL-003 Poverty and Graduation Rates

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [7a5f122] |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 (stand-in) | Accepted after review [RC-006]; autonomous mode, not independent | [7a5f122] |

---

## Purpose

The poverty rate and the high school graduation rate by state are charted and compared.

## Deliverable

Notebook sections, tested aggregation functions and screenshots for the poverty chart, the graduation chart and their relationship.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Unit tests pass with Python 3.14 in a fresh `.venv` | `python -m pytest` reports 0 failures | Any failure |
| 2 | Local Opengrep run is clean | No finding of error severity | One or more findings |
| 3 | Documentation is present | README section, wiki pages in en, da, ms and screenshots exist for every step of this milestone | Any missing |
| 4 | Review | Latest `RC-*` for this milestone's pull request says Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | Its deliverable is the input of this step |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives O1, O2, O4 | [BC-001] Objectives |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-29 — no deadline in the Business Case; the date orders the work.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Poverty rate by state | Implement the state aggregation and chart poverty rate by state in descending order; add a screenshot and a unit test for the aggregation. | No | |
| 2 | High school graduation rate by state | Chart the high school graduation rate by state in ascending order, with a screenshot and a unit test. | No | |
| 3 | Poverty and graduation relationship | Visualise the relationship between the two rates (joint plot, scatter with regression line) and describe what it shows and does not show, with a screenshot. | No | |
| 4 | Wiki pages in three languages | Write the English, Danish and Bahasa Malaysia wiki pages for steps 3 to 5: what the step taught, with its screenshot, under `docs/wiki/`. | No | |

---

[BC-001]: ../business-case.md
[RC-006]: ../sqa/reviews/rc-006-mil-003.md
[7a5f122]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/commit/7a5f122ced31642b5b69abdb4cf3a98e4941268f
