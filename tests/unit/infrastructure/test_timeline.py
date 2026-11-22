from datetime import date

import polars as pl
import pytest

from fatal_force.infrastructure.timeline import (
    deaths_per_month,
    deaths_per_year,
    rolling_mean,
    trend,
)


def _fatalities() -> pl.DataFrame:
    return pl.DataFrame(
        {
            "date": [
                date(2015, 1, 31),
                date(2015, 1, 2),
                date(2015, 4, 9),
                date(2016, 1, 1),
            ]
        }
    )


def test_deaths_per_month_fills_empty_months_with_zero() -> None:
    result = deaths_per_month(_fatalities())
    assert result.height == 13
    assert result["month"][0] == date(2015, 1, 1)
    assert result["month"][-1] == date(2016, 1, 1)
    assert result["deaths"].to_list()[:5] == [2, 0, 0, 1, 0]
    assert result["deaths"].sum() == 4


def test_deaths_per_month_of_empty_frame_is_empty() -> None:
    empty = pl.DataFrame({"date": []}, schema={"date": pl.Date})
    assert deaths_per_month(empty).is_empty()


def test_deaths_per_year_counts_and_sorts() -> None:
    assert deaths_per_year(_fatalities()).to_dicts() == [
        {"year": 2015, "deaths": 3},
        {"year": 2016, "deaths": 1},
    ]


def test_rolling_mean_is_null_during_warmup() -> None:
    frame = pl.DataFrame({"deaths": [1, 2, 3, 4]})
    result = rolling_mean(frame, "deaths", 2)
    assert result["deaths_rolling_mean"].to_list() == [None, 1.5, 2.5, 3.5]
    assert result.columns == ["deaths", "deaths_rolling_mean"]


def test_rolling_mean_rejects_window_below_one() -> None:
    with pytest.raises(ValueError, match="window"):
        rolling_mean(pl.DataFrame({"deaths": [1]}), "deaths", 0)


def test_trend_slope_is_change_per_month() -> None:
    frame = pl.DataFrame({"deaths": [10, 12, 14, 16]})
    fit = trend(frame)
    assert fit.slope == pytest.approx(2.0)
    assert fit.intercept == pytest.approx(10.0)


def test_trend_needs_two_months() -> None:
    with pytest.raises(ValueError, match="points"):
        trend(pl.DataFrame({"deaths": [1]}))
