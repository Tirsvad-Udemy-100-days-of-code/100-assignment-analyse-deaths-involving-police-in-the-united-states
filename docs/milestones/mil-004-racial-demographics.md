# MIL-004 Racial Demographics

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [7a5f122] |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 (stand-in) | Accepted after review [RC-007]; autonomous mode, not independent | [7a5f122] |

---

## Purpose

The racial makeup of each state and the racial split of the people killed are shown side by side.

## Deliverable

Tested functions for the racial makeup by state and for deaths by race, with notebook sections and screenshots.

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
| MIL-003 | Its deliverable is the input of this step |

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

2026-12-01 — no deadline in the Business Case; the date orders the work.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Racial makeup of each state | Aggregate census racial shares by state and chart them as a grouped bar chart; add a unit test for the aggregation and a screenshot. | No | |
| 2 | Deaths by race | Chart the number of people killed by race as a donut chart, with a unit test for the counting function and a screenshot. | No | |
| 3 | Wiki pages in three languages | Write the English, Danish and Bahasa Malaysia wiki pages for steps 6 and 7: what the step taught, with its screenshot, under `docs/wiki/`. | No | |

---

[BC-001]: ../business-case.md
[RC-007]: ../sqa/reviews/rc-007-mil-004.md
[7a5f122]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/commit/7a5f122ced31642b5b69abdb4cf3a98e4941268f
