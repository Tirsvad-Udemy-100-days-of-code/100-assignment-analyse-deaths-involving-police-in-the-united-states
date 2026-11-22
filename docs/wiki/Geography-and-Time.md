**English** · [Dansk](Geography-and-Time-da) · [Bahasa Malaysia](Geography-and-Time-ms)

# Steps 16 to 19: places and time

## What the steps do

Step 16 ranks the ten cities with the most killings. Step 17 compares, for those cities, each race's share of the people killed with its census share. Step 18 draws the killings per state on a map. Step 19 follows the number of killings month by month.

![Top ten cities](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-16-top-cities.png)

![Ratio by race in the top ten cities](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-17-rate-by-race-top-cities.png)

![Map of killings by state](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-18-deaths-by-state-map.png)

![Killings over time](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-19-deaths-over-time.png)

## What we gained

- **Counts follow size.** Los Angeles (39), Phoenix (31), Houston (26) and Chicago (25) lead the cities; California (424), Texas (225) and Florida (154) lead the states. These are the largest places, so counts alone do not show where a person is at greater risk.
- **Match names before joining.** The census writes "Los Angeles city" and the police database "Los Angeles". A function that normalises names matched 1,295 of the 1,534 cities with a death.
- **Compare shares, with care.** In the ten cities, Black people are 1.1 to 2.9 times as large a share of the people killed as of the city, and White people 0.17 to 1.0 times. Each city has only 15 to 39 killings, a group with no killings shows 0, and the census Hispanic share overlaps the race shares, so single bars are rough.
- **A choropleth needs a static export.** plotly draws the interactive map; the screenshot needs the `kaleido` package, which is why it is in the optional `analysis` extra.
- **Know the time span.** The file covers January 2015 to July 2017 (31 months, 991 killings in 2015, 963 in 2016 and 581 in the partial year 2017). The straight-line trend is almost flat (-0.04 per month), and the rolling mean smooths the monthly noise.

## Where the code is

`fatal_force.infrastructure.geography` and `timeline`, `fatal_force.presentation.charts` and `maps`.
