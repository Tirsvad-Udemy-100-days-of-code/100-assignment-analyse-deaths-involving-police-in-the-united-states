**English** · [Dansk](Racial-Demographics-da) · [Bahasa Malaysia](Racial-Demographics-ms)

# Steps 7 and 8: racial makeup and deaths by race

## What the steps do

Step 7 shows the racial makeup of every state as a stacked bar chart, using the census shares averaged over the cities of each state. Step 8 shows how many of the 2,535 people in the Washington Post database belong to each race, as a donut chart.

![Racial makeup of each state](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-07-racial-makeup-by-state.png)

![Deaths by race](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-08-deaths-by-race.png)

## What we gained

- **Know what a number measures.** The census treats Hispanic as an ethnicity that overlaps the race groups, so the five shares of a state can add up to more than 100 %. The stacked bars therefore rise above 100 for some states, which is a property of the data, not a bug.
- **An average of cities is not the population share.** Cities are not weighted by population. Iowa (96.7 % white) and Hawaii (33.4 % white) sit at the two ends.
- **Counts are not rates.** White people are 47.4 % of the people killed (1,201), Black people 24.4 % (618) and Hispanic people 16.7 % (423). Race is unknown for 7.7 % (195). These are shares of a count; they do not say how likely a person of a given race is to be killed, because the groups differ in size.
- **Show missing data.** The *Unknown* slice stays visible instead of being dropped.
- **A donut chart needs few slices.** It works for seven categories, and a legend keeps small slices readable.

## Where the code is

`racial_makeup_by_state` and `deaths_by_race` in `fatal_force.infrastructure.aggregation`; `stacked_bar_chart` and `donut_chart` in `fatal_force.presentation.charts`.
