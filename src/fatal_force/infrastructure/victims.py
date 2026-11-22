"""@brief Count and describe the victims of the fatalities frame (needs polars)."""

import polars as pl

from fatal_force.constants import (
    AGE_COLUMN,
    ARMED_COLUMN,
    COUNT_COLUMN,
    DEATHS_COLUMN,
    FLEE_COLUMN,
    GENDER_COLUMN,
    MANNER_COLUMN,
    MENTAL_ILLNESS_COLUMN,
    THREAT_LEVEL_COLUMN,
    UNARMED_LABEL,
    UNKNOWN_LABEL,
    VALUE_COLUMN,
)
from fatal_force.domain.armed import ArmedShares

_PERCENT = 100.0


def value_counts(frame: pl.DataFrame, column: str) -> pl.DataFrame:
    """@brief Count the rows per distinct value of a column.

    @param frame The frame to count.
    @param column The column whose values are counted.
    @return A frame with `value` and `count`, most frequent first; ties are
        ordered by value.
    """
    return (
        frame.group_by(column)
        .agg(pl.len().alias(COUNT_COLUMN))
        .rename({column: VALUE_COLUMN})
        .sort([COUNT_COLUMN, VALUE_COLUMN], descending=[True, False])
    )


def deaths_by_gender(fatalities: pl.DataFrame) -> pl.DataFrame:
    """@brief Count the deaths per gender.

    @param fatalities The cleaned fatalities frame.
    @return A frame with `value` and `count`, most deaths first.
    """
    return value_counts(fatalities, GENDER_COLUMN)


def deaths_by_manner(fatalities: pl.DataFrame) -> pl.DataFrame:
    """@brief Count the deaths per gender and manner of death.

    @param fatalities The cleaned fatalities frame.
    @return A frame with `gender`, `manner_of_death` and `deaths`, sorted by
        gender and manner.
    """
    return (
        fatalities.group_by(GENDER_COLUMN, MANNER_COLUMN)
        .agg(pl.len().alias(DEATHS_COLUMN))
        .sort(GENDER_COLUMN, MANNER_COLUMN)
    )


def ages_by_group(
    fatalities: pl.DataFrame, group_column: str
) -> dict[str, list[float]]:
    """@brief Collect the known ages of each group.

    @param fatalities The cleaned fatalities frame.
    @param group_column The column that defines the groups.
    @return The ages per group, groups sorted by name; rows without an age are
        dropped and a group left with no age is absent.
    """
    known = fatalities.drop_nulls(AGE_COLUMN).sort(group_column)
    return {
        str(key[0]): [float(age) for age in group[AGE_COLUMN].to_list()]
        for key, group in known.group_by(group_column, maintain_order=True)
    }


def armed_counts(fatalities: pl.DataFrame) -> pl.DataFrame:
    """@brief Count the deaths per weapon label.

    @param fatalities The cleaned fatalities frame.
    @return A frame with `value` and `count`, most frequent first.
    """
    return value_counts(fatalities, ARMED_COLUMN)


def armed_shares(fatalities: pl.DataFrame) -> ArmedShares:
    """@brief Split the victims into armed, unarmed and unknown.

    @param fatalities The cleaned fatalities frame.
    @return The counts; armed is every label other than unarmed and unknown.
    """
    armed = fatalities[ARMED_COLUMN]
    unarmed = int((armed == UNARMED_LABEL).sum())
    unknown = int((armed == UNKNOWN_LABEL).sum())
    return ArmedShares(
        total=fatalities.height,
        armed=fatalities.height - unarmed - unknown,
        unarmed=unarmed,
        unknown=unknown,
    )


def share_under_age(fatalities: pl.DataFrame, limit: int) -> float:
    """@brief Percentage of victims with a known age below a limit.

    @param fatalities The cleaned fatalities frame.
    @param limit The age limit, exclusive.
    @return The percentage of known ages below the limit; 0.0 with no ages.
    """
    ages = fatalities[AGE_COLUMN].drop_nulls()
    if ages.is_empty():
        return 0.0
    return _PERCENT * int((ages < limit).sum()) / ages.len()


def mental_illness_share(fatalities: pl.DataFrame) -> float:
    """@brief Percentage of victims showing signs of mental illness.

    @param fatalities The cleaned fatalities frame.
    @return The percentage; 0.0 for an empty frame.
    """
    if fatalities.is_empty():
        return 0.0
    flagged = int(fatalities[MENTAL_ILLNESS_COLUMN].sum())
    return _PERCENT * flagged / fatalities.height


def threat_level_counts(fatalities: pl.DataFrame) -> pl.DataFrame:
    """@brief Count the deaths per threat level.

    @param fatalities The cleaned fatalities frame.
    @return A frame with `value` and `count`, most frequent first.
    """
    return value_counts(fatalities, THREAT_LEVEL_COLUMN)


def flee_counts(fatalities: pl.DataFrame) -> pl.DataFrame:
    """@brief Count the deaths per way of fleeing.

    @param fatalities The cleaned fatalities frame.
    @return A frame with `value` and `count`, most frequent first.
    """
    return value_counts(fatalities, FLEE_COLUMN)
