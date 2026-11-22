[English](Geography-and-Time) · **Dansk** · [Bahasa Malaysia](Geography-and-Time-ms)

# Trin 16 til 19: steder og tid

## Hvad trinene gør

Trin 16 rangerer de ti byer med flest drab. Trin 17 sammenligner for de byer hver races andel af de dræbte med dens census-andel. Trin 18 tegner drabene pr. stat på et kort. Trin 19 følger antallet af drab måned for måned.

![De ti største byer](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-16-top-cities.png)

![Forhold efter race i de ti byer](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-17-rate-by-race-top-cities.png)

![Kort over drab pr. stat](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-18-deaths-by-state-map.png)

![Drab over tid](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-19-deaths-over-time.png)

## Hvad vi fik ud af det

- **Antal følger størrelse.** Los Angeles (39), Phoenix (31), Houston (26) og Chicago (25) fører blandt byerne; Californien (424), Texas (225) og Florida (154) fører blandt staterne. Det er de største steder, så antal alene viser ikke, hvor en person løber større risiko.
- **Afstem navne før sammenføjning.** Census skriver "Los Angeles city" og politidatabasen "Los Angeles". En funktion, der normaliserer navne, matchede 1.295 af de 1.534 byer med et dødsfald.
- **Sammenlign andele med omtanke.** I de ti byer udgør sorte 1,1 til 2,9 gange så stor en andel af de dræbte som af byen, og hvide 0,17 til 1,0 gange. Hver by har kun 15 til 39 drab, en gruppe uden drab viser 0, og census' hispanic-andel overlapper race-andelene, så enkelte søjler er ujævne.
- **Et koropletkort kræver en statisk eksport.** plotly tegner det interaktive kort; skærmbilledet kræver pakken `kaleido`, hvilket er grunden til, at den ligger i det valgfri `analysis`-tilvalg.
- **Kend tidsrummet.** Filen dækker januar 2015 til juli 2017 (31 måneder, 991 drab i 2015, 963 i 2016 og 581 i det ufuldstændige 2017). Den rette tendenslinje er næsten vandret (-0,04 pr. måned), og det glidende gennemsnit udjævner månedens støj.

## Hvor koden er

`fatal_force.infrastructure.geography` og `timeline`, `fatal_force.presentation.charts` og `maps`.
