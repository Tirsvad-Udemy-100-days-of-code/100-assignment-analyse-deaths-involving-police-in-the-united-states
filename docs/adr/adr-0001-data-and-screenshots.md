# ADR-0001 Course data outside git and screenshots from a script

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 (stand-in) | Accepted after review [RC-011]; autonomous mode, not independent | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The course archive holds the Washington Post file and four census files. The download link is signed and expires, and the redistribution terms of the data are unknown. The assignment also needs one screenshot per lecture step in the README and the wiki.

Options for the data: (a) commit the files to git; (b) keep them in an ignored `data/` folder and document the download. Options for the screenshots: (a) capture the notebook window by hand; (b) save each chart as an image from code, into `docs/screenshots/`, named `step-NN-<slug>.png`.

## Decision

Keep the course data in an ignored `data/` folder outside git and document how to obtain it. Save each lecture step's chart as an image from code, so the screenshots can be regenerated.

## Consequences

**Positive:**

- No licence risk from redistributing the data.
- Screenshots always match the code and can be regenerated.
- The repository stays small.

**Negative:**

- A reader must download the data before running the notebook.
- Charts are rendered images, not captures of the notebook window.

## Affected Artifacts

- [BC-001] — Risks and Constraints are met by this decision.

---

[BC-001]: ../business-case.md
[RC-011]: ../sqa/reviews/rc-011-adr-0001.md
