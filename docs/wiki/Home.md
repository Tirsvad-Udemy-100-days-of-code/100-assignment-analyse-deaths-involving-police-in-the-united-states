**English** · [Dansk](Home-da) · [Bahasa Malaysia](Home-ms)

# Fatal Force wiki

This wiki explains what each lecture step of the Day 100 assignment of the Udemy course *100 Days of Code: The Complete Python Pro Bootcamp* taught. The project analyses the Washington Post database of fatal police shootings together with US census data, in a Jupyter notebook backed by a small tested Python package.

The topic is sensitive. The charts show counts and rates, not causes; each page states the limits of its charts.

## Run it

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[analysis,dev]"
python -m pytest
jupyter lab src/notebooks/fatal_force.ipynb
```

Copy the course CSV files into a `data/` folder first (see the README).

## Pages

- [Steps 1 and 2: data exploration and cleaning](Data-Exploration-and-Cleaning)
- [Steps 3 to 6: poverty and high school graduation](Poverty-and-Graduation)
- [Steps 7 and 8: racial makeup and deaths by race](Racial-Demographics)
- [Steps 9 to 15: who the people killed were](Victim-Characteristics)
- [Steps 16 to 19: places and time](Geography-and-Time)
- [Journal of the assignment](Journal)
