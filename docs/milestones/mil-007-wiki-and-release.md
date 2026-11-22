# MIL-007 Wiki and Release

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-007 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 (stand-in) | Accepted after review [RC-010]; autonomous mode, not independent | pending |

---

## Purpose

The documentation is complete in three languages and the repository is ready for visitors.

## Deliverable

A reviewed wiki with the same page set in English, Danish and Bahasa Malaysia, the final README with every screenshot, a clean local Opengrep run, and a tagged release.

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
| MIL-006 | Its deliverable is the input of this step |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives O3, O4, O5 | [BC-001] Objectives |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-12-08 — no deadline in the Business Case; the date orders the work.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Wiki home and sidebar | Create `Home`, `_Sidebar` and the language links in all three languages following `framework/process/wiki.md`; review against `QC-WIKI-001`. | No | |
| 2 | Language check | Run `check-languages.sh` and a page-count comparison to prove the three languages have the same page set. | No | |
| 3 | README screenshots | Embed one screenshot per lecture step in the README and check that every image file exists. | No | |
| 4 | Final checks | Run pytest in a fresh `.venv`, run Opengrep, run the framework checks and fix findings. | No | |
| 5 | Release | Tag the first release following `framework/process/release.md`. | No | |

---

[BC-001]: ../business-case.md
[RC-010]: ../sqa/reviews/rc-010-mil-007.md
