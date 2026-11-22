[English](Data-Exploration-and-Cleaning) · **Dansk** · [Bahasa Malaysia](Data-Exploration-and-Cleaning-ms)

# Trin 1 og 2: dataudforskning og datarensning

## Hvad trinene gør

Trin 1 ser på de rå data: hvor mange rækker og kolonner hver af de fem filer har, hvor mange værdier der mangler, og om rækker gentages. Trin 2 renser data, så de senere diagrammer bygger på pålidelige tal.

![Udforskning af rå data](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-01-data-exploration.png)

![Data efter rensning](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-02-data-cleaning.png)

## Hvad vi fik ud af det

- **Kig, før du tegner.** Dødsfaldsfilen har 2535 rækker og 346 manglende værdier (alder 77, race 195, flugt 65, bevæbnet 9) og ingen dublerede id'er. Census-filerne har hver cirka 29 000 byrækker.
- **Rigtige filer er rodede.** CSV-filerne bruger Windows-1252-tekst og et enkelt vognretur som linjeskift, så en almindelig indlæsning fejler. En lille læsefunktion skjuler nu dette.
- **Pladsholdere er ikke tal.** Værdier som `(X)`, `-` og `250,000+` bliver til manglende værdier eller almindelige tal. Manglende census-værdier forbliver manglende i stedet for at blive nul, fordi nul ville trække gennemsnit ned.
- **Tests holder rensningen ærlig.** Rensefunktionerne har enhedstests på små filer, så en ændring, der ødelægger dem, opdages med det samme.
- **Et skærmbillede pr. trin** gemmes af kode i `docs/screenshots/`, så det kan genskabes.

## Hvor koden er

`fatal_force.infrastructure.csv_reader`, `exploration` og `cleaning`; figurhjælperen er `fatal_force.presentation.screenshots`.
