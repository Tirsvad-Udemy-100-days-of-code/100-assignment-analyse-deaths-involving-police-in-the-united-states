# MIL-001 Project Foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 (stand-in) | Accepted after review [RC-004]; autonomous mode, not independent | pending |

---

## Purpose

Project skeleton and tooling are in place so every later step is runnable, tested and documented.

## Deliverable

A repository with `pyproject.toml`, a local `.venv` recipe, a Python `.gitignore`, `src/`, `tests/`, `docs/`, `constants.py`, a `Doxyfile`, a README from the framework template, a local Opengrep script, and repository description and topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Unit tests pass with Python 3.14 in a fresh `.venv` | `python -m pytest` reports 0 failures | Any failure |
| 2 | Local Opengrep run is clean | No finding of error severity | One or more findings |
| 3 | Documentation is present | README exists and `check-readme.sh` passes | Any missing |
| 4 | Review | Latest `RC-*` for this milestone's pull request says Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First milestone |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives O3, O5 | [BC-001] Objectives |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-25 — no deadline in the Business Case; the date orders the work.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Project configuration | Create `pyproject.toml` with `requires-python >= 3.14`, the `src` layout, pytest configuration and an optional `analysis` extra (pandas, matplotlib, seaborn, plotly, jupyter) so the package itself has no runtime dependencies. | No | |
| 2 | Virtual environment instructions | Document creating a local `.venv` with `py -3.14 -m venv .venv`, activating it, and `python -m pip install --upgrade pip`, in the README, for Windows PowerShell and POSIX shells. | No | |
| 3 | Gitignore and editorconfig | Add a Python `.gitignore` (also ignoring `.env`, `.venv`, `data/`, the local prompt log folder) and the root `.editorconfig` from the framework baseline; run `check-editorconfig.sh`. | No | |
| 4 | Source and test skeleton | Create `src/fatal_force/` with `constants.py` and a first tested function, plus `tests/` with a pytest smoke test, so `python -m pytest` runs from a fresh `.venv`. | No | |
| 5 | Doxygen configuration | Add a `Doxyfile` for `src/` and document the Doxygen comment style used in source files. | No | |
| 6 | README from template | Create `README.md` from `framework/templates/README-template.md` with run and test instructions and a placeholder section for screenshots; validate it with `check-readme.sh`. | No | |
| 7 | Local Opengrep run | Add a script that runs `~/.opengrep/cli/latest/opengrep.exe` on `src/` and `tests/` and document that it must be clean before each push. | No | |
| 8 | ADR for data and screenshots | Record in an ADR where the course data lives (outside git, with the download steps) and how a screenshot per lecture step is produced and stored under `docs/screenshots/`. | No | |
| 9 | Repository description and topics | Set the repository description and topics on the git host through its API with the repository token from `.env`; the token is read by the shell only and never by project code. | No | |

---

[BC-001]: ../business-case.md
[RC-004]: ../sqa/reviews/rc-004-mil-001.md
