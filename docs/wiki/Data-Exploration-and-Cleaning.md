**English** · [Dansk](Data-Exploration-and-Cleaning-da) · [Bahasa Malaysia](Data-Exploration-and-Cleaning-ms)

# Steps 1 and 2: data exploration and cleaning

## What the steps do

Step 1 looks at the raw data: how many rows and columns each of the five files has, how many values are missing and whether rows repeat. Step 2 cleans the data so later charts rest on trustworthy numbers.

![Raw data exploration](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-01-data-exploration.png)

![Data after cleaning](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-02-data-cleaning.png)

## What we gained

- **Look before you chart.** The deaths file has 2535 rows and 346 missing values (age 77, race 195, flee 65, armed 9) and no duplicate ids. The census files have about 29 000 city rows each.
- **Real files are messy.** The CSV files use Windows-1252 text and a bare carriage return as the line ending, so a plain read fails. One small reader function now hides this.
- **Placeholders are not numbers.** Values such as `(X)`, `-` and `250,000+` are turned into missing values or plain numbers. Missing census values stay missing instead of becoming zero, because a zero would pull averages down.
- **Tests keep cleaning honest.** The cleaning functions have unit tests on tiny files, so a change that breaks them is caught at once.
- **A screenshot per step** is saved by code into `docs/screenshots/`, so it can be regenerated.

## Where the code is

`fatal_force.infrastructure.csv_reader`, `exploration` and `cleaning`; the figure helper is `fatal_force.presentation.screenshots`.
