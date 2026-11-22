[English](Home) · **Dansk** · [Bahasa Malaysia](Home-ms)

# Fatal Force wiki

Denne wiki forklarer, hvad hvert forelæsningstrin i Dag 100-opgaven i Udemy-kurset *100 Days of Code: The Complete Python Pro Bootcamp* lærte. Projektet analyserer Washington Posts database over dødelige politiskud sammen med amerikanske census-data i en Jupyter-notebook, støttet af en lille testet Python-pakke.

Emnet er følsomt. Diagrammerne viser antal og rater, ikke årsager; hver side angiver diagrammernes begrænsninger.

## Kør det

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[analysis,dev]"
python -m pytest
jupyter lab src/notebooks/fatal_force.ipynb
```

Kopiér først kursets CSV-filer til en `data/`-mappe (se README).

## Sider

- [Trin 1 og 2: dataudforskning og datarensning](Data-Exploration-and-Cleaning-da)
- [Trin 3 til 6: fattigdom og gennemførelse af high school](Poverty-and-Graduation-da)
- [Trin 7 og 8: etnisk sammensætning og dødsfald efter race](Racial-Demographics-da)
- [Trin 9 til 15: hvem de dræbte var](Victim-Characteristics-da)
- [Trin 16 til 19: steder og tid](Geography-and-Time-da)
- [Journal over opgaven](Journal-da)
