**English** · [Dansk](Journal-da) · [Bahasa Malaysia](Journal-ms)

# Journal of the assignment

The assignment asks five questions. These are our answers.

## How did we approach the project?

We planned first: a Business Case, stakeholders, seven milestones and a task list, each reviewed before any code. Then each milestone followed the lecture steps in order: load and clean the data, then one chart per step. The logic went into a small tested package, and the Jupyter notebook only calls it and shows the result. Every step saves its chart as a screenshot, and every step has a wiki page in three languages.

## What was hard?

- The data files looked simple but were not: Windows-1252 text and a bare carriage return as line ending, placeholders such as `(X)` and `250,000+` in number columns, and a Hispanic share that overlaps the race shares.
- A sensitive topic. A chart of counts invites a reading as a rate or a cause. We added the limits beside each chart instead of leaving them to the reader.
- Matching cities between the two sources: the census writes "Los Angeles city", the police database "Los Angeles".

## What was easy?

- Once the cleaning functions existed, every chart was a short grouping and a drawing function.
- Tests on tiny tables caught mistakes early, such as ties in a ranking and missing months in a time series.

## What would we improve next time?

- Decide the screenshot method before the first chart, so the figures look the same from the start.
- Weight the state averages by city population. The census file has no population column, so this needs another source.
- Add rates per 100,000 people, which the assignment hints at but the supplied files cannot give directly.

## What was the biggest learning?

Cleaning and checking the data takes more care than drawing it, and a chart answers only the question it is built for. A bar of counts is not a rate, a correlation is not a cause, and missing data should stay visible.

## What would we do differently?

Start with a data dictionary (what each column means and which values are placeholders) and write the cleaning tests from it. That would have found the carriage-return line endings and the number placeholders on the first day.
