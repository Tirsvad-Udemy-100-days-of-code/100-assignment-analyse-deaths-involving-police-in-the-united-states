import datetime

import polars as pl

from fatal_force.infrastructure.cleaning import (
    clean_all,
    clean_census_frame,
    clean_fatalities,
    missing_census_values_as_zero,
)
from fatal_force.infrastructure.csv_reader import Datasets


def _census() -> pl.DataFrame:
    return pl.DataFrame(
        {
            "Geographic Area": ["AL", "AK", "TX", "TX"],
            "City": [" A ", "B", "C", "D"],
            "Median Income": ["11,207", "(X)", "250,000+", "-"],
        }
    )


def test_clean_census_frame_turns_placeholders_into_null() -> None:
    result = clean_census_frame(_census(), ["Median Income"])
    assert result["Median Income"].to_list() == [11207.0, None, 250000.0, None]
    assert result["Median Income"].dtype == pl.Float64


def test_clean_census_frame_renames_and_strips() -> None:
    result = clean_census_frame(_census(), ["Median Income"])
    assert result.columns == ["state", "city", "Median Income"]
    assert result["city"][0] == "A"


def test_clean_census_frame_accepts_lowercase_area_spelling() -> None:
    frame = pl.DataFrame({"Geographic area": ["AL"], "City": ["A"], "v": ["1.5"]})
    assert clean_census_frame(frame, ["v"]).columns == ["state", "city", "v"]


def test_missing_census_values_as_zero_replaces_nulls_only_when_called() -> None:
    cleaned = clean_census_frame(_census(), ["Median Income"])
    assert cleaned["Median Income"].null_count() == 2
    filled = missing_census_values_as_zero(cleaned, ["Median Income"])
    assert filled["Median Income"].to_list() == [11207.0, 0.0, 250000.0, 0.0]


def _fatalities() -> pl.DataFrame:
    return pl.DataFrame(
        {
            "id": ["1", "1", "2"],
            "date": ["02/01/15", "02/01/15", "31/12/16"],
            "age": ["53", "53", None],
            "armed": ["gun", "gun", None],
            "race": [None, None, "W"],
            "gender": ["M", "M", None],
            "flee": [None, None, "Car"],
            "signs_of_mental_illness": ["TRUE", "TRUE", "FALSE"],
            "body_camera": ["FALSE", "FALSE", "TRUE"],
        }
    )


def test_clean_fatalities_drops_duplicate_ids() -> None:
    assert clean_fatalities(_fatalities())["id"].to_list() == [1, 2]


def test_clean_fatalities_parses_dates_and_booleans() -> None:
    result = clean_fatalities(_fatalities())
    assert result["date"].to_list() == [
        datetime.date(2015, 1, 2),
        datetime.date(2016, 12, 31),
    ]
    assert result["signs_of_mental_illness"].to_list() == [True, False]
    assert result["body_camera"].dtype == pl.Boolean


def test_clean_fatalities_fills_unknown_but_keeps_age_null() -> None:
    result = clean_fatalities(_fatalities())
    assert result["armed"].to_list() == ["gun", "unknown"]
    assert result["race"].to_list() == ["unknown", "W"]
    assert result["flee"].to_list() == ["unknown", "Car"]
    assert result["age"].to_list() == [53, None]


def test_clean_all_cleans_every_frame() -> None:
    raw = Datasets(
        hh_income=_census(),
        pct_poverty=pl.DataFrame(
            {"Geographic Area": ["AL"], "City": ["A"], "poverty_rate": ["-"]}
        ),
        pct_completed_hs=pl.DataFrame(
            {"Geographic Area": ["AL"], "City": ["A"], "percent_completed_hs": ["2"]}
        ),
        share_race_city=pl.DataFrame(
            {
                "Geographic area": ["AL"],
                "City": ["A"],
                "share_white": ["(X)"],
                "share_black": ["1"],
                "share_native_american": ["1"],
                "share_asian": ["1"],
                "share_hispanic": ["1"],
            }
        ),
        fatalities=_fatalities(),
    )
    cleaned = clean_all(raw)
    assert cleaned.pct_poverty["poverty_rate"].null_count() == 1
    assert cleaned.share_race_city["share_white"].null_count() == 1
    assert cleaned.fatalities.height == 2
