[English](Journal) · **Dansk** · [Bahasa Malaysia](Journal-ms)

# Journal over opgaven

Opgaven stiller fem spørgsmål. Her er vores svar.

## Hvordan greb vi projektet an?

Vi planlagde først: en business case, interessenter, syv milepæle og en opgaveliste, hver gennemgået før nogen kode. Derefter fulgte hver milepæl forelæsningstrinene i rækkefølge: indlæs og rens data, så ét diagram pr. trin. Logikken kom i en lille testet pakke, og Jupyter-notebooken kalder den blot og viser resultatet. Hvert trin gemmer sit diagram som skærmbillede, og hvert trin har en wikiside på tre sprog.

## Hvad var svært?

- Datafilerne så enkle ud, men var det ikke: Windows-1252-tekst og et enkelt vognretur som linjeskift, pladsholdere som `(X)` og `250,000+` i talkolonner og en hispanic-andel, der overlapper race-andelene.
- Et følsomt emne. Et diagram over antal inviterer til at blive læst som en rate eller en årsag. Vi satte begrænsningerne ved siden af hvert diagram i stedet for at overlade dem til læseren.
- At matche byer mellem de to kilder: census skriver "Los Angeles city", politidatabasen "Los Angeles".

## Hvad var let?

- Da rensefunktionerne fandtes, var hvert diagram en kort gruppering og en tegnefunktion.
- Tests på små tabeller fangede fejl tidligt, fx lige placeringer i en rangering og manglende måneder i en tidsserie.

## Hvad ville vi forbedre næste gang?

- Beslutte skærmbilledmetoden før det første diagram, så figurerne ser ens ud fra start.
- Vægte statsgennemsnittene efter byernes befolkning. Census-filen har ingen befolkningskolonne, så det kræver en anden kilde.
- Tilføje rater pr. 100.000 indbyggere, som opgaven antyder, men som de leverede filer ikke direkte kan give.

## Hvad var den største læring?

Rensning og kontrol af data kræver mere omhu end at tegne dem, og et diagram besvarer kun det spørgsmål, det er bygget til. En søjle med antal er ikke en rate, en korrelation er ikke en årsag, og manglende data skal forblive synlige.

## Hvad ville vi gøre anderledes?

Starte med en dataordbog (hvad hver kolonne betyder, og hvilke værdier der er pladsholdere) og skrive rensetestene ud fra den. Det ville have fundet vognretur-linjeskiftene og talpladsholderne den første dag.
