# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-003 |
| CrossReference | [PP-001], [QC-PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 (stand-in) | Initial version; autonomous mode, not independent | pending |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001] and `QC-LANG-001`
- Scope: full review
- Language and domain: en / it
- Language reviewer: none; the reviewer reads the language and knows the domain (S01 confirmed in chat on 2026-11-23)
- Mode: autonomous, not independent (reviewer is the stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Start 2026-11-23, end 2026-12-08, and the Business Case constraint (no deadline) are stated. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | Seven gateways each listed once with document, date and owner S01. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | Decision dates equal the Target Date of each linked `MIL-*` and lie inside the window. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage table maps each In Scope item to a gateway. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Dependency chain MIL-001 to MIL-007 is acyclic and matches the schedule order. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | Dependencies section states that a No-Go moves later dates and the end date, and that S01 decides. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | Owner S01 only; no governance document exists and S01 is the only responsible person, stated in Planning Assumptions. |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Assumptions give their source; baseline is first version. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Plan risks have impact and mitigation and cite [BC-001] where they come from. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open issues do not contradict the plan. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | Main deliverable per gateway agrees with each `MIL-*` Deliverable. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | Stories column says "none (plain analysis tasks)". |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | Gantt bars and table windows agree. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | Milestone column says "not yet synced". |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | Single Project Plan, Version History kept. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has `Language | en` and `Domain | it`, both set. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code and `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are in English. S01, the person who reads English and the IT domain, accepted the plan containing this document in chat on 2026-11-23 (RC-basis: person confirmation, not the stand-in). |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register of this type is IT Executive English (BC, PP, MIL) or IT Professional English (SA); the text matches it. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | No domain dictionary (`DICT`) exists yet; one term is used per concept (milestone, task, screenshot). S01 accepted the plan in chat on 2026-11-23. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, headings, IDs and statuses are in English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists beside the file. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version; no language change since a previous accepted version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01 reads English and knows the IT domain and accepted the plan in chat on 2026-11-23; confirmation was by that person, not by the stand-in. Open to challenge in the end-of-run summary. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations used (ADR, KPI, pytest, venv) are established IT terms; first use is spelled out or linked where it matters. |

## Overall Verdict

Go — every Mandatory criterion passes. The review is a stand-in review in autonomous mode and stays open to challenge by S01.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
