import polars as pl
import pytest

from fatal_force.infrastructure.geography import (
    deaths_by_state,
    normalise_city_name,
    ratio_by_city_and_race,
    top_cities,
    victim_and_population_shares,
)


def _fatalities() -> pl.DataFrame:
    return pl.DataFrame(
        {
            "city": ["Aville", "Aville", "Aville", "Aville", "Bton", "Bton", "Cburg"],
            "state": ["TX", "TX", "TX", "TX", "CA", "CA", "NY"],
            "race": ["W", "B", "B", "unknown", "H", "H", "W"],
        }
    )


def _census() -> pl.DataFrame:
    return pl.DataFrame(
        {
            "state": ["TX", "CA", "CA"],
            "city": ["Aville city", "Bton CDP", "Bton city"],
            "share_white": [50.0, 10.0, 30.0],
            "share_black": [0.0, 2.0, 4.0],
            "share_native_american": [1.0, None, None],
            "share_asian": [1.0, 1.0, 1.0],
            "share_hispanic": [10.0, 60.0, 80.0],
        }
    )


def _row(frame: pl.DataFrame, city: str, race: str) -> dict[str, object]:
    return frame.filter((pl.col("city") == city) & (pl.col("race") == race)).row(
        0, named=True
    )


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("Los Angeles city", "los angeles"),
        ("Abbeville town", "abbeville"),
        ("Abanda CDP", "abanda"),
        ("Milford city (balance)", "milford"),
        ("Foo urban county", "foo"),
        ("Juneau city and borough", "juneau"),
        ("Plain", "plain"),
        ("Town", "town"),
        ("Cityville", "cityville"),
    ],
)
def test_normalise_city_name_strips_suffixes(name: str, expected: str) -> None:
    assert normalise_city_name(name) == expected


def test_deaths_by_state_sorts_descending_then_by_state() -> None:
    frame = pl.DataFrame({"state": ["TX", "CA", "NY", "NY", "CA", "TX", "AL"]})
    result = deaths_by_state(frame)
    assert result.to_dicts() == [
        {"state": "CA", "deaths": 2},
        {"state": "NY", "deaths": 2},
        {"state": "TX", "deaths": 2},
        {"state": "AL", "deaths": 1},
    ]


def test_top_cities_orders_ties_by_city_and_limits() -> None:
    result = top_cities(_fatalities(), count=3)
    assert result.to_dicts() == [
        {"city": "Aville", "state": "TX", "deaths": 4},
        {"city": "Bton", "state": "CA", "deaths": 2},
        {"city": "Cburg", "state": "NY", "deaths": 1},
    ]


def test_top_cities_keeps_same_name_in_two_states_apart() -> None:
    frame = pl.DataFrame({"city": ["X", "X"], "state": ["AL", "TX"]})
    assert top_cities(frame).height == 2


def test_shares_cover_every_city_and_race_group() -> None:
    cities = top_cities(_fatalities(), count=2)
    result = victim_and_population_shares(_fatalities(), _census(), cities)
    assert result.columns == [
        "city",
        "state",
        "race",
        "victim_share",
        "population_share",
        "ratio",
    ]
    assert result["race"].to_list() == ["W", "B", "H", "A", "N"] * 2
    assert result["city"].to_list()[:5] == ["Aville"] * 5


def test_victim_share_ignores_unknown_race() -> None:
    cities = pl.DataFrame({"city": ["Aville"], "state": ["TX"]})
    result = victim_and_population_shares(_fatalities(), _census(), cities)
    assert _row(result, "Aville", "W")["victim_share"] == pytest.approx(100 / 3)
    assert _row(result, "Aville", "B")["victim_share"] == pytest.approx(200 / 3)
    assert _row(result, "Aville", "H")["victim_share"] == 0.0


def test_ratio_is_victim_share_over_population_share() -> None:
    cities = pl.DataFrame({"city": ["Aville"], "state": ["TX"]})
    result = victim_and_population_shares(_fatalities(), _census(), cities)
    row = _row(result, "Aville", "W")
    assert row["population_share"] == 50.0
    assert row["ratio"] == pytest.approx(100 / 3 / 50.0)


def test_ratio_is_null_when_population_share_is_zero() -> None:
    cities = pl.DataFrame({"city": ["Aville"], "state": ["TX"]})
    row = _row(
        victim_and_population_shares(_fatalities(), _census(), cities), "Aville", "B"
    )
    assert row["population_share"] == 0.0
    assert row["ratio"] is None


def test_ratio_is_null_when_population_share_is_null() -> None:
    cities = pl.DataFrame({"city": ["Bton"], "state": ["CA"]})
    row = _row(
        victim_and_population_shares(_fatalities(), _census(), cities), "Bton", "N"
    )
    assert row["population_share"] is None
    assert row["ratio"] is None


def test_census_rows_with_same_normalised_name_are_averaged() -> None:
    cities = pl.DataFrame({"city": ["Bton"], "state": ["CA"]})
    row = _row(
        victim_and_population_shares(_fatalities(), _census(), cities), "Bton", "W"
    )
    assert row["population_share"] == pytest.approx(20.0)


def test_city_without_census_match_has_null_population_share() -> None:
    cities = pl.DataFrame({"city": ["Cburg"], "state": ["NY"]})
    result = victim_and_population_shares(_fatalities(), _census(), cities)
    assert result["population_share"].null_count() == 5
    assert result["ratio"].null_count() == 5
    assert _row(result, "Cburg", "W")["victim_share"] == 100.0


def test_city_with_only_unknown_race_has_null_victim_share() -> None:
    fatalities = pl.DataFrame({"city": ["D"], "state": ["TX"], "race": ["unknown"]})
    cities = pl.DataFrame({"city": ["D"], "state": ["TX"]})
    result = victim_and_population_shares(fatalities, _census(), cities)
    assert result["victim_share"].null_count() == 5


def test_ratio_by_city_and_race_pivots_in_city_order() -> None:
    cities = pl.DataFrame({"city": ["Bton", "Aville"], "state": ["CA", "TX"]})
    shares = victim_and_population_shares(_fatalities(), _census(), cities)
    result = ratio_by_city_and_race(shares, ["W", "H"])
    assert result.columns == ["city_label", "W", "H"]
    assert result["city_label"].to_list() == ["Bton, CA", "Aville, TX"]
    assert result["H"][0] == pytest.approx(100.0 / 70.0)
