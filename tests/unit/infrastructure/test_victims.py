import polars as pl
import pytest

from fatal_force.domain.armed import ArmedShares
from fatal_force.infrastructure.victims import (
    ages_by_group,
    armed_counts,
    armed_shares,
    deaths_by_gender,
    deaths_by_manner,
    flee_counts,
    mental_illness_share,
    share_under_age,
    threat_level_counts,
    value_counts,
)


def _fatalities() -> pl.DataFrame:
    return pl.DataFrame(
        {
            "manner_of_death": ["shot", "shot", "shot and Tasered", "shot", "shot"],
            "armed": ["gun", "unarmed", "gun", "unknown", "knife"],
            "age": [20, 30, None, 24, 40],
            "gender": ["M", "M", "F", "M", "F"],
            "race": ["W", "B", "B", "W", "unknown"],
            "signs_of_mental_illness": [True, False, False, False, True],
            "threat_level": ["attack", "other", "attack", "attack", "other"],
            "flee": ["Not fleeing", "Car", "Not fleeing", "Foot", "Not fleeing"],
        }
    )


def test_value_counts_sorts_by_count_then_value() -> None:
    frame = pl.DataFrame({"x": ["b", "a", "c", "c", "a", "b", "d"]})
    result = value_counts(frame, "x")
    assert result.columns == ["value", "count"]
    assert result["value"].to_list() == ["a", "b", "c", "d"]
    assert result["count"].to_list() == [2, 2, 2, 1]


def test_value_counts_counts_null_as_its_own_value() -> None:
    result = value_counts(pl.DataFrame({"x": ["a", None, None]}), "x")
    assert result.row(0) == (None, 2)


def test_deaths_by_gender_counts_most_first() -> None:
    result = deaths_by_gender(_fatalities())
    assert result.rows() == [("M", 3), ("F", 2)]


def test_deaths_by_manner_counts_per_gender_and_manner() -> None:
    result = deaths_by_manner(_fatalities())
    assert result.columns == ["gender", "manner_of_death", "deaths"]
    assert result.rows() == [
        ("F", "shot", 1),
        ("F", "shot and Tasered", 1),
        ("M", "shot", 3),
    ]


def test_ages_by_group_drops_nulls_and_sorts_groups() -> None:
    assert ages_by_group(_fatalities(), "race") == {
        "B": [30.0],
        "W": [20.0, 24.0],
        "unknown": [40.0],
    }


def test_ages_by_group_omits_group_without_ages() -> None:
    frame = pl.DataFrame({"race": ["W", "B"], "age": [None, 5]})
    assert ages_by_group(frame, "race") == {"B": [5.0]}


def test_armed_counts_orders_labels_by_frequency() -> None:
    result = armed_counts(_fatalities())
    assert result["value"].to_list() == ["gun", "knife", "unarmed", "unknown"]
    assert result["count"].to_list() == [2, 1, 1, 1]


def test_armed_shares_separates_unarmed_and_unknown() -> None:
    shares = armed_shares(_fatalities())
    assert shares == ArmedShares(total=5, armed=3, unarmed=1, unknown=1)
    assert shares.armed_percent == pytest.approx(60.0)


def test_share_under_age_uses_known_ages_and_excludes_limit() -> None:
    # known ages 20, 30, 24, 40: below 30 are 20 and 24 -> 50 percent.
    assert share_under_age(_fatalities(), 30) == pytest.approx(50.0)


def test_share_under_age_is_zero_without_ages() -> None:
    frame = pl.DataFrame({"age": [None, None]}, schema={"age": pl.Int64})
    assert share_under_age(frame, 25) == 0.0


def test_mental_illness_share_is_percent_of_victims() -> None:
    assert mental_illness_share(_fatalities()) == pytest.approx(40.0)


def test_mental_illness_share_is_zero_for_empty_frame() -> None:
    empty = _fatalities().head(0)
    assert mental_illness_share(empty) == 0.0


def test_threat_level_counts_orders_by_frequency() -> None:
    assert threat_level_counts(_fatalities()).rows() == [("attack", 3), ("other", 2)]


def test_flee_counts_orders_ties_by_value() -> None:
    assert flee_counts(_fatalities()).rows() == [
        ("Not fleeing", 3),
        ("Car", 1),
        ("Foot", 1),
    ]
