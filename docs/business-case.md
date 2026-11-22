# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version of the Day 100 project | pending |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 (stand-in) | Accepted after review [RC-001]; autonomous mode, not independent | pending |

---

## Executive Summary

Day 100 of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" asks the participant to analyse fatal shootings by police in the United States since 1 January 2015. The analysis combines the Washington Post database with US census data on poverty, high school graduation, household income and racial demographics. This project delivers that assignment as a readable, runnable Python repository: a Jupyter notebook, a small tested Python package that uses the assignment's function names, a README and a three-language wiki that explains what each lecture step taught. It proceeds because the cost is one person's study time and the result is a reusable reference for other course participants.

## Methodological and Standards Foundation

- Documents follow the SQA and QC framework mounted at `framework/` (plan first, review each step, one `RC-*` per reviewed document).
- Product quality is described with ISO/IEC 25010:2023 characteristics, as the QC checklists tag them.
- Code follows the `coding-conventions` skill for Python and a layered structure from the `clean-architecture` skill.
- Data handling is explicit about provenance: each figure in the notebook is traceable to a named source file.

## Problem Statement

1. The assignment ships as a loose notebook and data files. A participant who wants to compare solutions finds no tested, documented, runnable reference.
2. The topic is sensitive and politically charged. Charts without clear sourcing, method and caveats are easy to misread.
3. A notebook alone gives no way to run the cleaning and aggregation logic outside Jupyter, or to verify it with tests.

## Business Opportunity

A clean repository gives fellow course participants (S02) and repository visitors (S03) a reference they can run in minutes, and it gives the course participant (S01) a documented portfolio piece that shows data cleaning, analysis, testing and documentation practice.

## Objectives

1. O1: Reproduce every analysis step of the Day 100 assignment in a Jupyter notebook, with one screenshot per lecture step.
2. O2: Place the reusable cleaning and aggregation logic in a Python package under `src/`, using the assignment's function names, with unit tests under `tests/`.
3. O3: Make the project runnable from a fresh clone with a local `.venv`, `pyproject.toml` and instructions in the README.
4. O4: Publish a wiki in English, Danish and Bahasa Malaysia that explains what each lecture step taught.
5. O5: Publish the repository with a description, topics and a README built from the framework template.

## Scope

### In Scope

- Data loading, exploration and cleaning of the Washington Post and census files.
- Poverty rate, high school graduation rate, median household income and racial demographics by state.
- Deaths by race, gender, age, armed status, signs of mental illness, threat level and flee status.
- Deaths by state, over time, and the choropleth map of the assignment.
- Doxygen comments in the source and a `Doxyfile`.
- README, wiki (en, da, ms) and screenshots per lecture step.
- A local static-analysis run before each push.
- The learning journal of the assignment, written as a wiki page.

### Out of Scope

- Any claim of causation or policy recommendation.
- A web application, API or database.
- Updating the Washington Post data beyond the files supplied with the course.
- Publishing the package on PyPI.

## Expected Benefits

### Tangible Benefits

- A repository that passes its own tests from a fresh clone.
- Documentation in three languages and a screenshot per lecture step.
- A reusable set of tested functions for cleaning and grouping the data.

### Intangible Benefits

- A documented learning record for the course participant.
- A readable reference that other participants can compare with their own solutions.

## Strategic Alignment

The project supports the participant's goal of completing the 100 Days of Code course with a portfolio of documented, tested work, and the framework's goal that every project is planned, reviewed and traceable.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Assignment steps covered | 100 percent of the lecture steps have a notebook section and a screenshot | Count of steps against count of screenshots in `docs/screenshots/` |
| 2 | Tests pass from a fresh clone | 0 failures with Python 3.14 | `python -m pytest` in a new `.venv` |
| 3 | Wiki languages | 3 languages with the same page set | `check-languages.sh` and a page count per language |
| 4 | Static analysis | 0 findings of error severity before each push | Opengrep report from the local run |
| 5 | Runtime dependencies of the package | 0 outside the analysis extra | `pyproject.toml` dependency list |
| 6 | Repository metadata | Description and at least 5 topics set | Host API response |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The signed download link for the course data has expired | The data cannot be fetched and the project stalls | Stop and report; the course participant downloads the archive from the course page and places it in `data/` |
| Python 3.14 is not the default interpreter on the machine | Tests run on the wrong version | Document `py -3.14 -m venv .venv` and check the version in the first task |
| The topic is sensitive and results can be misread | Readers draw unsupported conclusions | State sources, method and limits beside each chart; make no causal claims |
| Data licence limits redistribution | Data files cannot be committed | Keep the data out of git, document where to obtain it, and record the decision in an ADR |
| The dataset contains encoding and missing-value problems | Wrong counts | Clean in tested functions and show before and after counts |
| Screenshots drift from the code | Documentation misleads | Generate figures with a script and re-generate when the notebook changes |

## Assumptions

- The Product Owner, developer and reviewer is the course participant (S01); S01 is reachable in chat.
- The course archive contains the Washington Post file and the four census files named in the lecture.
- Pandas, matplotlib and Jupyter are acceptable as optional analysis dependencies.
- The Gitea repository under the `Tirsvad-Udemy-100-days-of-code` organisation is the target; its `origin` remote is the source of truth for the exact name.

## Constraints

- Python 3.14 or later, with a local virtual environment created by `venv`.
- Tests use pytest; constants live in `constants.py`.
- Configuration lives in `pyproject.toml`; there are no runtime dependencies unless needed.
- The word for the assistant tool is not written in any artifact.
- Folder structure is `src/`, `tests/` and `docs/`.
- One branch and one pull request per step; the work is reviewed before merging.
- Tokens come from the local `.env` file, which is never read by the project code, tested or committed.
- No deadline; the assignment is estimated at 90 minutes, the project documentation takes longer.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| Study and development time of S01 | A tested, documented reference of the assignment |
| Review time of S01 | Three-language wiki and screenshots |
| No licence or hosting cost beyond the existing Gitea | A portfolio piece for S01 and a reference for S02 and S03 |

The assessment is qualitative: the project is unpaid study work with no revenue, so a monetary return on investment does not apply.

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Completes the assignment, owns the product, develops and reviews |
| S02 | Reads, runs and compares the code with their own solution |
| S03 | Browses the repository for ideas and expects a clear description, topics and README |

## Recommendation

Proceed — the cost is low, the scope is bounded by the assignment and the result is reusable by two further stakeholder groups.

---

[SA-001]: ./stakeholder-analysis.md
[RC-001]: ./sqa/reviews/rc-001-business-case.md
