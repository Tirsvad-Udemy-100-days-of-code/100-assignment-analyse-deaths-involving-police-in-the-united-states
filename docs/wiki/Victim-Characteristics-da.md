[English](Victim-Characteristics) · **Dansk** · [Bahasa Malaysia](Victim-Characteristics-ms)

# Trin 9 til 15: hvem de dræbte var

## Hvad trinene gør

Disse trin beskriver de 2.535 personer i Washington Post-databasen: køn, alder, dødsmåde, om de var bevæbnede, alder efter race, tegn på mental sygdom, trusselsniveau og om de flygtede.

![Dødsfald efter køn](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-09-deaths-by-gender.png)

![Aldersfordeling](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-10-age-distribution.png)

![Alder efter dødsmåde](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-11-age-by-manner-of-death.png)

![Bevæbnet og ubevæbnet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-12-armed-and-unarmed.png)

![Alder efter race](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-13-age-by-race.png)

![Mental sygdom](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-14-mental-illness.png)

![Trusselsniveau og flugt](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-15-threat-and-fleeing.png)

## Hvad vi fik ud af det

- **De fleste dræbte var mænd.** 2.428 (95,8 %) var mænd og 107 (4,2 %) kvinder. Dødsmåden er *shot* for 2.363 og *shot and Tasered* for 172.
- **Alder.** Medianalderen er 34 (2.458 kendte aldre), og 18,3 % af dem med kendt alder var under 25. Et histogram med en KDE-linje viser formen; et boksplot sammenligner grupper.
- **Bevæbnet betyder ikke én ting.** 92,9 % er registreret som bevæbnede, 6,7 % (171) som ubevæbnede og 0,4 % som ukendt. Gruppen af bevæbnede omfatter *undetermined* (117) og *toy weapon* (104), så hovedtallet afhænger af definitionen. En pistol er det mest almindelige våben (1.398).
- **Fordelinger pr. gruppe.** Tæthedslinjerne for hver race topper ved forskellige aldre (sorte og hispanics omkring 25, hvide omkring 33), men små grupper giver ujævne linjer, så signaturforklaringen viser gruppens størrelse.
- **Sammenhæng betyder noget.** 25,0 % af registreringerne nævner tegn på mental sygdom. Trusselsniveauet er *attack* for 1.611, *other* for 766 og *undetermined* for 158; 1.695 flygtede ikke.
- **Skriv din egen KDE.** Et Gaussisk kerneestimat med Silvermans båndbredde fylder cirka tyve linjer almindelig Python og kræver intet ekstra bibliotek; det har sine egne tests.

## Hvor koden er

`fatal_force.infrastructure.victims`, `fatal_force.domain.kde` og `armed`, `fatal_force.presentation.charts` og `distributions`.
