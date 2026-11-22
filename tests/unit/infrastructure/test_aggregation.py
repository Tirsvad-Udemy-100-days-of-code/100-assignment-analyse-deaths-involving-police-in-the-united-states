import polars as pl
import pytest

from fatal_force.infrastructure.aggregation import (
    correlation,
    deaths_by_race,
    high_school_rate_by_state,
    poverty_and_graduation_by_state,
    poverty_rate_by_state,
    racial_makeup_by_state,
)


def _poverty() -> pl.DataFrame:
    return pl.DataFrame(
        {
            "state": ["AL", "AL", "MS", "MS", "NY", "TX"],
            "city": ["a", "b", "c", "d", "e", "f"],
            "poverty_rate": [10.0, 20.0, 30.0, None, 5.0, None],
        }
    )


def _graduation() -> pl.DataFrame:
    return pl.DataFrame(
        {
            "state": ["AL", "AL", "MS", "NY"],
            "city": ["a", "b", "c", "e"],
            "percent_completed_hs": [80.0, 90.0, 70.0, 95.0],
        }
    )


def test_poverty_rate_by_state_means_ignoring_nulls_highest_first() -> None:
    result = poverty_rate_by_state(_poverty())
    assert result.columns == ["state", "poverty_rate"]
    assert result["state"].to_list() == ["MS", "AL", "NY", "TX"]
    assert result["poverty_rate"].to_list()[:3] == [30.0, 15.0, 5.0]
    assert result["poverty_rate"][3] is None


def test_poverty_rate_by_state_places_all_null_state_last() -> None:
    assert poverty_rate_by_state(_poverty())["state"][-1] == "TX"


def test_high_school_rate_by_state_sorts_lowest_first() -> None:
    result = high_school_rate_by_state(_graduation())
    assert result.columns == ["state", "percent_completed_hs"]
    assert result["state"].to_list() == ["MS", "AL", "NY"]
    assert result["percent_completed_hs"].to_list() == [70.0, 85.0, 95.0]


def test_poverty_and_graduation_by_state_inner_joins_sorted_by_state() -> None:
    result = poverty_and_graduation_by_state(
        poverty_rate_by_state(_poverty()), high_school_rate_by_state(_graduation())
    )
    assert result.columns == ["state", "poverty_rate", "percent_completed_hs"]
    assert result["state"].to_list() == ["AL", "MS", "NY"]


def test_correlation_of_perfect_line_is_one() -> None:
    frame = pl.DataFrame({"x": [1.0, 2.0, 3.0], "y": [2.0, 4.0, 6.0]})
    assert correlation(frame, "x", "y") == pytest.approx(1.0)


def test_correlation_of_falling_line_is_minus_one() -> None:
    frame = pl.DataFrame({"x": [1.0, 2.0, 3.0], "y": [6.0, 4.0, 2.0]})
    assert correlation(frame, "x", "y") == pytest.approx(-1.0)


def _shares() -> pl.DataFrame:
    return pl.DataFrame(
        {
            "state": ["NY", "AL", "AL", "TX"],
            "city": ["a", "b", "c", "d"],
            "share_white": [50.0, 60.0, 80.0, None],
            "share_black": [10.0, 30.0, None, None],
            "share_native_american": [1.0, 0.0, 2.0, None],
            "share_asian": [5.0, 1.0, 1.0, None],
            "share_hispanic": [20.0, 5.0, 10.0, None],
        }
    )


def test_racial_makeup_by_state_means_ignoring_nulls_sorted_by_state() -> None:
    result = racial_makeup_by_state(_shares())
    assert result.columns == [
        "state",
        "share_white",
        "share_black",
        "share_native_american",
        "share_asian",
        "share_hispanic",
    ]
    assert result["state"].to_list() == ["AL", "NY", "TX"]
    assert result["share_white"].to_list()[:2] == [70.0, 50.0]
    assert result["share_black"].to_list()[:2] == [30.0, 10.0]


def test_racial_makeup_by_state_keeps_all_null_state_as_null() -> None:
    result = racial_makeup_by_state(_shares())
    assert result["share_white"][2] is None


def _fatalities() -> pl.DataFrame:
    return pl.DataFrame({"race": ["W", "B", "B", "unknown", "H", "H", "W", "B"]})


def test_deaths_by_race_counts_sorted_descending_with_labels() -> None:
    result = deaths_by_race(_fatalities())
    assert result.columns == ["race_code", "race", "deaths"]
    assert result["race_code"].to_list() == ["B", "H", "W", "unknown"]
    assert result["race"].to_list() == ["Black", "Hispanic", "White", "Unknown"]
    assert result["deaths"].to_list() == [3, 2, 2, 1]


def test_deaths_by_race_orders_ties_by_code() -> None:
    result = deaths_by_race(pl.DataFrame({"race": ["W", "A", "N", "A", "W", "N"]}))
    assert result["race_code"].to_list() == ["A", "N", "W"]


def test_deaths_by_race_keeps_unmapped_code_as_its_own_label() -> None:
    result = deaths_by_race(pl.DataFrame({"race": ["Z"]}))
    assert result.row(0) == ("Z", "Z", 1)
