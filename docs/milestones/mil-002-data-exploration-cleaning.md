# MIL-002 Data Exploration and Cleaning

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [7a5f122] |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 (stand-in) | Accepted after review [RC-005]; autonomous mode, not independent | [7a5f122] |

---

## Purpose

The course data is loaded, explored and cleaned by tested functions, so every later chart rests on trustworthy counts.

## Deliverable

A `load` and `clean` module with unit tests, a notebook section for the preliminary exploration and cleaning steps, their screenshots and their wiki pages.

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
| MIL-001 | Its deliverable is the input of this step |

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

2026-11-27 — no deadline in the Business Case; the date orders the work.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Obtain the course data | Download the course archive to `data/` (outside git), verify the file names and sizes and document the steps; stop and report if the signed link has expired. | No | |
| 2 | Load the datasets | Implement loading of the Washington Post file and the four census files, handling their non-UTF-8 encoding, with unit tests on small fixtures. | No | |
| 3 | Preliminary data exploration | Notebook section showing shape, columns, NaN counts and duplicates for each dataset, with a screenshot named `step-01`. | No | |
| 4 | Clean the census data | Replace placeholder values such as `(X)` and `-` with missing values and convert columns to numbers; add unit tests and a before and after screenshot. | No | |
| 5 | Clean the shootings data | Handle missing values and duplicates in the Washington Post data and parse the date column; add unit tests. | No | |
| 6 | Wiki pages in three languages | Write the English, Danish and Bahasa Malaysia wiki pages for steps 1 and 2: what the step taught, with its screenshot, under `docs/wiki/`. | No | |

---

[BC-001]: ../business-case.md
[RC-005]: ../sqa/reviews/rc-005-mil-002.md
[7a5f122]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/commit/7a5f122ced31642b5b69abdb4cf3a98e4941268f
