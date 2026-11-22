# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version of the Day 100 project | pending |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 (stand-in) | Accepted after review [RC-002]; autonomous mode, not independent | pending |

---

## Purpose

This analysis names the people the project serves, ranks their power and interest, and records what each one needs, so that the Business Case, the plan and the code answer real concerns. It uses the power and interest grid and maps each concern to a FURPS+ attribute.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Individual | HIGH | HIGH | Manage Closely | Complete the assignment with a documented, tested result |
| S02 | Udemy coursists | Fellow course participants | Udemy course community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Repository visitors | Public | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, writes and reviews every artifact and accepts every milestone.
- **Keep Informed (S02):** cannot change the project, but their ability to run and understand the code is the main measure of its usefulness.
- **Monitor (S03):** casual visitors; they are served by a good description, topics and README and need no further contact.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Every lecture step of the assignment is solved and shown | Functionality |
| CN-002 | S01 | Each step is planned, reviewed and traceable | Supportability |
| CN-003 | S01 | The wiki explains in three languages what each step taught | Usability |
| CN-004 | S02 | The code is readable and uses the assignment's function names | Usability |
| CN-005 | S02 | The project runs from a fresh clone with the README instructions | Reliability |
| CN-006 | S03 | The repository description, topics and README are clear | Usability |
| CN-007 | S03 | The package needs no runtime dependencies | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CR-001 | Chat | Each milestone | Plan, review summary, pull request link | Every milestone |
| CR-002 | README and wiki | Each milestone | Instructions, screenshots and lecture notes | MIL-001 to MIL-007 |
| CR-003 | Repository description and topics | Once, then on change | Metadata on the git host | MIL-001 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S02 wants readable notebook code, S03 wants no runtime dependencies | S02, S03 | The package itself has no runtime dependencies; pandas, matplotlib and Jupyter sit in an optional `analysis` extra |
| S01 wants thorough review records, S02 wants a short README | S01, S02 | Records stay in `docs/`; the README holds only run instructions and screenshots |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | [BC-001] O1 |
| S01 | CN-002 | [BC-001] O2 |
| S01 | CN-003 | [BC-001] O4 |
| S02 | CN-004 | [BC-001] O2 |
| S02 | CN-005 | [BC-001] O3 |
| S03 | CN-006 | [BC-001] O5 |
| S03 | CN-007 | [BC-001] O3 |

## Sign-Off

| Stakeholder | Decision | Date |
| --- | --- | --- |
| S01 | Pending review | |

---

[BC-001]: ./business-case.md
[RC-002]: ./sqa/reviews/rc-002-stakeholder-analysis.md
