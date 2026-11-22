"""@brief Compare where victims died with who lives there (needs polars)."""

import re
from collections.abc import Sequence

import polars as pl

from fatal_force.constants import (
    CITY_COLUMN,
    CITY_LABEL_COLUMN,
    CITY_SUFFIXES,
    DEATHS_COLUMN,
    DEFAULT_TOP_CITIES,
    POPULATION_SHARE_COLUMN,
    RACE_COLUMN,
    RACE_GROUPS,
    RACE_SHARE_COLUMNS,
    RATIO_COLUMN,
    STATE_COLUMN,
    UNKNOWN_LABEL,
    VICTIM_SHARE_COLUMN,
)

_PERCENT = 100.0
_SUFFIX_PATTERN = (
    r"(?:\s+(?:" + "|".join(re.escape(suffix) for suffix in CITY_SUFFIXES) + r"))+$"
)
_KEY_COLUMN = "_city_key"
_CITY_ORDER = "_city_order"
_RACE_ORDER = "_race_order"
_COUNT = "_victims"
_TOTAL = "_known_victims"


def normalise_city_name(name: str) -> str:
    """@brief Lower-case a city name and drop its census place-type suffixes.

    @param name A city name such as `Los Angeles city` or `Abanda CDP`.
    @return The name without trailing suffixes, e.g. `los angeles`.
    """
    return re.sub(_SUFFIX_PATTERN, "", name.strip().lower())


def _normalised_key() -> pl.Expr:
    """@brief Expression that normalises the city column, like `normalise_city_name`.

    @return An expression yielding the matching key of each city.
    """
    return (
        pl.col(CITY_COLUMN)
        .str.strip_chars()
        .str.to_lowercase()
        .str.replace(_SUFFIX_PATTERN, "")
        .alias(_KEY_COLUMN)
    )


def deaths_by_state(fatalities: pl.DataFrame) -> pl.DataFrame:
    """@brief Count the deaths per state, most deaths first.

    @param fatalities The cleaned fatalities frame.
    @return A frame with `state` and `deaths`; ties are ordered by state.
    """
    return (
        fatalities.group_by(STATE_COLUMN)
        .agg(pl.len().alias(DEATHS_COLUMN))
        .sort([DEATHS_COLUMN, STATE_COLUMN], descending=[True, False])
    )


def top_cities(
    fatalities: pl.DataFrame, count: int = DEFAULT_TOP_CITIES
) -> pl.DataFrame:
    """@brief The cities with the most deaths.

    @param fatalities The cleaned fatalities frame.
    @param count How many cities to return.
    @return A frame with `city`, `state` and `deaths`, most deaths first; ties
        are ordered by city, then state.
    """
    return (
        fatalities.group_by(CITY_COLUMN, STATE_COLUMN)
        .agg(pl.len().alias(DEATHS_COLUMN))
        .sort(
            [DEATHS_COLUMN, CITY_COLUMN, STATE_COLUMN], descending=[True, False, False]
        )
        .head(count)
    )


def _known_victims_per_city(fatalities: pl.DataFrame) -> pl.DataFrame:
    """@brief Count the victims of known race per city and race group.

    @param fatalities The cleaned fatalities frame.
    @return A frame with `city`, `state`, `race`, the victim count of that race
        and the number of victims of known race in the same city.
    """
    return (
        fatalities.filter(pl.col(RACE_COLUMN) != UNKNOWN_LABEL)
        .group_by(CITY_COLUMN, STATE_COLUMN, RACE_COLUMN)
        .agg(pl.len().alias(_COUNT))
        .with_columns(
            pl.col(_COUNT).sum().over(CITY_COLUMN, STATE_COLUMN).alias(_TOTAL)
        )
    )


def _population_shares(share_race_city: pl.DataFrame) -> pl.DataFrame:
    """@brief Census shares per matching key, state and race group.

    Census rows that share a key (a city and a CDP of the same name) are
    averaged.

    @param share_race_city The cleaned census frame.
    @return A frame with the key, `state`, `race` and the population share.
    """
    frames = [
        share_race_city.select(
            _normalised_key(),
            pl.col(STATE_COLUMN),
            pl.lit(race).alias(RACE_COLUMN),
            pl.col(column).alias(POPULATION_SHARE_COLUMN),
        )
        for race, column in RACE_SHARE_COLUMNS.items()
    ]
    return (
        pl.concat(frames)
        .group_by(_KEY_COLUMN, STATE_COLUMN, RACE_COLUMN)
        .agg(pl.col(POPULATION_SHARE_COLUMN).mean())
    )


def victim_and_population_shares(
    fatalities: pl.DataFrame, share_race_city: pl.DataFrame, cities: pl.DataFrame
) -> pl.DataFrame:
    """@brief Compare the victim share of each race with its census share.

    @param fatalities The cleaned fatalities frame.
    @param share_race_city The cleaned census frame.
    @param cities A frame with `city` and `state`, one row per city to compare.
    @return One row per city and race group (W, B, H, A, N) in the order of
        `cities`, with `city`, `state`, `race`, `victim_share` (percent of the
        city's victims whose race is known), `population_share` (null without a
        census match) and `ratio` (victim share over population share; null
        when the population share is null or 0).
    """
    races = pl.DataFrame(
        {RACE_COLUMN: list(RACE_GROUPS), _RACE_ORDER: range(len(RACE_GROUPS))}
    )
    grid = (
        cities.select(CITY_COLUMN, STATE_COLUMN)
        .with_row_index(_CITY_ORDER)
        .join(races, how="cross")
    )
    victims = _known_victims_per_city(fatalities)
    totals = victims.select(CITY_COLUMN, STATE_COLUMN, _TOTAL).unique()
    return (
        grid.join(
            victims.drop(_TOTAL),
            on=[CITY_COLUMN, STATE_COLUMN, RACE_COLUMN],
            how="left",
        )
        .join(totals, on=[CITY_COLUMN, STATE_COLUMN], how="left")
        .with_columns(_normalised_key())
        .join(
            _population_shares(share_race_city),
            on=[_KEY_COLUMN, STATE_COLUMN, RACE_COLUMN],
            how="left",
        )
        .with_columns(
            pl.when(pl.col(_TOTAL) > 0)
            .then(_PERCENT * pl.col(_COUNT).fill_null(0) / pl.col(_TOTAL))
            .otherwise(None)
            .alias(VICTIM_SHARE_COLUMN)
        )
        .with_columns(
            pl.when(pl.col(POPULATION_SHARE_COLUMN) > 0)
            .then(pl.col(VICTIM_SHARE_COLUMN) / pl.col(POPULATION_SHARE_COLUMN))
            .otherwise(None)
            .alias(RATIO_COLUMN)
        )
        .sort(_CITY_ORDER, _RACE_ORDER)
        .select(
            CITY_COLUMN,
            STATE_COLUMN,
            RACE_COLUMN,
            VICTIM_SHARE_COLUMN,
            POPULATION_SHARE_COLUMN,
            RATIO_COLUMN,
        )
    )


def ratio_by_city_and_race(shares: pl.DataFrame, races: Sequence[str]) -> pl.DataFrame:
    """@brief Pivot the ratios to one row per city and one column per race.

    @param shares The result of `victim_and_population_shares`.
    @param races The race codes to keep, in column order.
    @return A frame with `city_label` (`City, ST`) and one ratio column named
        after each race code, in the order of the cities in `shares`.
    """
    wide = (
        shares.filter(pl.col(RACE_COLUMN).is_in(list(races)))
        .with_columns(
            pl.format("{}, {}", pl.col(CITY_COLUMN), pl.col(STATE_COLUMN)).alias(
                CITY_LABEL_COLUMN
            )
        )
        .pivot(on=RACE_COLUMN, index=CITY_LABEL_COLUMN, values=RATIO_COLUMN)
    )
    return wide.select(CITY_LABEL_COLUMN, *races)
