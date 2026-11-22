**English** · [Dansk](Poverty-and-Graduation-da) · [Bahasa Malaysia](Poverty-and-Graduation-ms)

# Steps 3 to 6: poverty and high school graduation

## What the steps do

The census files list thousands of cities. Steps 3 and 4 average the city values per state and rank the 51 states (50 states and DC) by poverty rate and by high school graduation rate. Steps 5 and 6 put the two measures side by side: a line chart with two y-axes and a scatter plot with a regression line.

![Poverty rate by state](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-03-poverty-rate.png)

![High school graduation rate by state](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-04-graduation-rate.png)

![Poverty and graduation lines](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-05-poverty-and-graduation-lines.png)

![Scatter with regression line](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-06-poverty-vs-graduation-scatter.png)

## What we gained

- **Aggregate before you rank.** Mississippi has the highest mean poverty rate (26.9 %) and New Jersey the lowest (8.2 %). Texas has the lowest graduation rate (75.7 %) and Massachusetts the highest (92.4 %).
- **A line chart is the wrong tool here.** States have no natural order, so the two lines mostly show noise. The scatter plot shows the relationship far better: Pearson r is -0.86, the fitted line falls 0.83 percentage points of graduation for each extra point of poverty.
- **Correlation is not cause.** The two measures move together, but the data cannot say that poverty causes lower graduation, or the reverse. Both may follow from other factors.
- **Choose a chart for the question.** Ranked bars answer "who is highest", a scatter plot answers "do they move together".
- **Small pure functions are easy to test.** The mean per state, the join and the line fit each have unit tests on tiny tables.

## Where the code is

`fatal_force.infrastructure.aggregation`, `fatal_force.domain.regression` and `fatal_force.presentation.charts`.
