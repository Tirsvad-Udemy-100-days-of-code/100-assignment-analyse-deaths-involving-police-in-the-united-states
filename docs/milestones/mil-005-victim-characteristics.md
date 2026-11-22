# MIL-005 Victim Characteristics

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 (stand-in) | Accepted after review [RC-008]; autonomous mode, not independent | pending |

---

## Purpose

Gender, age, armed status and mental illness of the people killed are analysed.

## Deliverable

Tested counting functions and notebook sections with screenshots for gender, age, manner of death, armed status, age by race and mental illness.

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
| MIL-004 | Its deliverable is the input of this step |

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

2026-12-03 — no deadline in the Business Case; the date orders the work.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Deaths by gender | Chart deaths by gender and by manner of death, with a screenshot and a unit test. | No | |
| 2 | Age at death | Chart age at death as a histogram and a box plot by manner of death, with a screenshot and a unit test. | No | |
| 3 | Armed and unarmed | Count deaths by armed status and the share of unarmed victims, with a screenshot and a unit test. | No | |
| 4 | Age distribution by race | Compare age distributions by race with a density plot and a screenshot. | No | |
| 5 | Mental illness | Chart the share of victims with signs of mental illness and show the threat level and flee status counts, with screenshots and a unit test. | No | |
| 6 | Wiki pages in three languages | Write the English, Danish and Bahasa Malaysia wiki pages for steps 8 to 12: what the step taught, with its screenshot, under `docs/wiki/`. | No | |

---

[BC-001]: ../business-case.md
[RC-008]: ../sqa/reviews/rc-008-mil-005.md
