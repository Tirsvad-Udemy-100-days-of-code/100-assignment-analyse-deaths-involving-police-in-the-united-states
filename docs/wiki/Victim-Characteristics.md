**English** · [Dansk](Victim-Characteristics-da) · [Bahasa Malaysia](Victim-Characteristics-ms)

# Steps 9 to 15: who the people killed were

## What the steps do

These steps describe the 2,535 people in the Washington Post database: gender, age, manner of death, whether they were armed, age by race, signs of mental illness, threat level and whether they fled.

![Deaths by gender](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-09-deaths-by-gender.png)

![Age distribution](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-10-age-distribution.png)

![Age by manner of death](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-11-age-by-manner-of-death.png)

![Armed and unarmed](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-12-armed-and-unarmed.png)

![Age by race](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-13-age-by-race.png)

![Mental illness](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-14-mental-illness.png)

![Threat level and fleeing](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-15-threat-and-fleeing.png)

## What we gained

- **Most of the people killed were men.** 2,428 (95.8 %) were men and 107 (4.2 %) were women. The manner of death is *shot* for 2,363 and *shot and Tasered* for 172.
- **Age.** The median age is 34 (2,458 known ages) and 18.3 % of those with a known age were under 25. A histogram with a KDE line shows the shape; a box plot compares groups.
- **Armed does not mean one thing.** 92.9 % are recorded as armed, 6.7 % (171) as unarmed and 0.4 % as unknown. The armed group includes *undetermined* (117) and *toy weapon* (104), so the headline number depends on the definition. A gun is the most common weapon (1,398).
- **Distributions by group.** Density lines for each race peak at different ages (Black and Hispanic around 25, White around 33), but small groups give rough lines, so the legend shows each group's size.
- **Context matters.** 25.0 % of the records note signs of mental illness. Threat level is *attack* for 1,611, *other* for 766 and *undetermined* for 158; 1,695 were not fleeing.
- **Write your own KDE.** A Gaussian kernel density estimate with Silverman's bandwidth takes about twenty lines of standard Python and needs no extra library; it has its own tests.

## Where the code is

`fatal_force.infrastructure.victims`, `fatal_force.domain.kde` and `armed`, `fatal_force.presentation.charts` and `distributions`.
