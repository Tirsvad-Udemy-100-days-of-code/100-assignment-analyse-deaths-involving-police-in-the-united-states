# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-020 |
| CrossReference | [WIKI-001], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Proposed | Jens Tirsvad Nielsen | S01 (stand-in) | Initial version; verdict Go-with-conditions, criterion 14 pending; autonomous mode, not independent | [07d082c] |

---

## Artifact Under Review

- Instance reviewed: [WIKI-001]
- Checklist used: [QC-WIKI-001]
- Scope: full review
- Language and domain: n/a (wiki pages; the page language is checked by the language line)
- Language reviewer: none (technical type)
- Mode: autonomous, not independent (reviewer is the stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | `docs/wiki/_Sidebar.md` exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Sidebar starts with the bold title, then one list with Home first, in English. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | The list links all seven English pages; a script checked that no link points to a missing page. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | Pass | No related wiki exists, so no Related section is present. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | The Languages section is last with English, Dansk and Bahasa Melayu linking to the Home pages. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | Pass | The sidebar is written by hand and carries a comment that says so. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Each page has the language line. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English, Danish (the second language chosen by S01) and Bahasa Malaysia exist; English is the PO language. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | All seven English pages have `-da` and `-ms` twins; a script compared the sets. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Every page starts with `**English** · [Dansk](..) · [Bahasa Malaysia](..)` with the current language in bold. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Danish pages use `-da`, Malay pages `-ms`. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Commands, code names and file names stay in English in all languages. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pass | Pending: the wiki is published after the merge; the check on the published wiki is made then (see the action item). |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | Pass | No layout rule is changed by this change. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | `docs/wiki/` is flat; no subfolder exists. |

## Overall Verdict

Go-with-conditions — every Mandatory criterion passes except criterion 14, which stays Pending until the wiki is published and its sidebar, pages and links are checked on the host. Stand-in review in autonomous mode; open to challenge by S01.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Check the published wiki (sidebar, every page, every link) and set criterion 14 to Pass or Fail | S01 | 2026-11-24 |

---

[WIKI-001]: ../../wiki
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[07d082c]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/commit/07d082c8204fdbb21fddb18aa264fa5e5e72777b
