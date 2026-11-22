[English](Poverty-and-Graduation) · **Dansk** · [Bahasa Malaysia](Poverty-and-Graduation-ms)

# Trin 3 til 6: fattigdom og gennemførelse af high school

## Hvad trinene gør

Census-filerne indeholder tusindvis af byer. Trin 3 og 4 tager gennemsnittet af bytallene pr. stat og rangerer de 51 stater (50 stater og DC) efter fattigdomsrate og efter andel, der har gennemført high school. Trin 5 og 6 sætter de to mål side om side: et liniediagram med to y-akser og et punktdiagram med en regressionslinje.

![Fattigdomsrate pr. stat](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-03-poverty-rate.png)

![Gennemførelse af high school pr. stat](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-04-graduation-rate.png)

![Fattigdom og gennemførelse som linjer](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-05-poverty-and-graduation-lines.png)

![Punktdiagram med regressionslinje](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-06-poverty-vs-graduation-scatter.png)

## Hvad vi fik ud af det

- **Aggregér, før du rangerer.** Mississippi har den højeste gennemsnitlige fattigdomsrate (26,9 %) og New Jersey den laveste (8,2 %). Texas har den laveste gennemførelsesandel (75,7 %) og Massachusetts den højeste (92,4 %).
- **Et liniediagram er det forkerte værktøj her.** Stater har ingen naturlig rækkefølge, så de to linjer viser mest støj. Punktdiagrammet viser sammenhængen langt bedre: Pearsons r er -0,86, og den tilpassede linje falder 0,83 procentpoint i gennemførelse for hvert ekstra procentpoint fattigdom.
- **Korrelation er ikke årsag.** De to mål følger hinanden, men data kan ikke sige, at fattigdom giver lavere gennemførelse, eller omvendt. Begge kan skyldes andre faktorer.
- **Vælg diagram efter spørgsmålet.** Rangerede søjler svarer på "hvem er højest", et punktdiagram svarer på "følges de ad".
- **Små rene funktioner er lette at teste.** Gennemsnit pr. stat, sammenføjningen og linjetilpasningen har hver enhedstests på små tabeller.

## Hvor koden er

`fatal_force.infrastructure.aggregation`, `fatal_force.domain.regression` og `fatal_force.presentation.charts`.
