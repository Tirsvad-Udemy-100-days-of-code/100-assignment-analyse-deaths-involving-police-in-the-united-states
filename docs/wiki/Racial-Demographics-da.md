[English](Racial-Demographics) · **Dansk** · [Bahasa Malaysia](Racial-Demographics-ms)

# Trin 7 og 8: etnisk sammensætning og dødsfald efter race

## Hvad trinene gør

Trin 7 viser den etniske sammensætning i hver stat som et stablet søjlediagram med census-andele, der er middelværdier over statens byer. Trin 8 viser, hvor mange af de 2.535 personer i Washington Post-databasen der tilhører hver race, som et donutdiagram.

![Racemæssig sammensætning pr. stat](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-07-racial-makeup-by-state.png)

![Dødsfald efter race](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-08-deaths-by-race.png)

## Hvad vi fik ud af det

- **Vid, hvad et tal måler.** Census behandler hispanic som en etnicitet, der overlapper racegrupperne, så en stats fem andele kan summere til mere end 100 %. De stablede søjler stiger derfor over 100 for nogle stater, hvilket er en egenskab ved data og ikke en fejl.
- **Et gennemsnit af byer er ikke befolkningsandelen.** Byerne er ikke vægtet efter befolkning. Iowa (96,7 % hvide) og Hawaii (33,4 % hvide) ligger i hver sin ende.
- **Antal er ikke rater.** Hvide udgør 47,4 % af de dræbte (1.201), sorte 24,4 % (618) og hispanics 16,7 % (423). Race er ukendt for 7,7 % (195). Det er andele af et antal; de siger ikke, hvor sandsynligt det er, at en person af en given race bliver dræbt, fordi grupperne har forskellig størrelse.
- **Vis manglende data.** Udsnittet *Ukendt* bliver stående i stedet for at blive fjernet.
- **Et donutdiagram kræver få udsnit.** Det virker til syv kategorier, og en signaturforklaring holder små udsnit læsbare.

## Hvor koden er

`racial_makeup_by_state` og `deaths_by_race` i `fatal_force.infrastructure.aggregation`; `stacked_bar_chart` og `donut_chart` i `fatal_force.presentation.charts`.
