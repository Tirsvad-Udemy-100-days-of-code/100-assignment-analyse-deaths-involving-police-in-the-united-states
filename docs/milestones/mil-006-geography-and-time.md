# MIL-006 Geography and Time

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [7a5f122] |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 (stand-in) | Accepted after review [RC-009]; autonomous mode, not independent | [7a5f122] |

---

## Purpose

Killings are shown by state and over time, including a map.

## Deliverable

Tested aggregation functions, a state choropleth map and a time series, with screenshots and wiki pages.

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
| MIL-005 | Its deliverable is the input of this step |

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

2026-12-05 — no deadline in the Business Case; the date orders the work.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Killings by state | Count killings per state and per capita using census population, with a bar chart, a unit test and a screenshot. | No | |
| 2 | Choropleth map | Draw the killings per state on a map of the United States with plotly, with a screenshot; plotly stays in the optional analysis extra. | No | |
| 3 | Deaths over time | Chart the number of deaths per month and year with a rolling average, with a screenshot and a unit test. | No | |
| 4 | Journal of the assignment | Write the assignment's journal questions (approach, hard and easy parts, biggest learning, what to do differently) as a wiki page in three languages. | No | |
| 5 | Wiki pages in three languages | Write the English, Danish and Bahasa Malaysia wiki pages for steps 13 to 16: what the step taught, with its screenshot, under `docs/wiki/`. | No | |

---

[BC-001]: ../business-case.md
[RC-009]: ../sqa/reviews/rc-009-mil-006.md
[7a5f122]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/commit/7a5f122ced31642b5b69abdb4cf3a98e4941268f
