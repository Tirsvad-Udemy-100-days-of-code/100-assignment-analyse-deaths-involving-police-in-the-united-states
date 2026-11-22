"""@brief Aggregate the cleaned census frames per state (needs polars)."""

import polars as pl

from fatal_force.constants import HIGH_SCHOOL_COLUMN, POVERTY_COLUMN, STATE_COLUMN


def _mean_by_state(frame: pl.DataFrame, column: str, descending: bool) -> pl.DataFrame:
    """@brief Average the city values of a column per state, ignoring nulls.

    @param frame A cleaned census frame with `state` and the value column.
    @param column The value column to average.
    @param descending True to sort the highest mean first.
    @return A frame with `state` and the column, sorted by the mean.
    """
    return (
        frame.group_by(STATE_COLUMN)
        .agg(pl.col(column).mean())
        .sort([column, STATE_COLUMN], descending=[descending, False], nulls_last=True)
    )


def poverty_rate_by_state(frame: pl.DataFrame) -> pl.DataFrame:
    """@brief Mean poverty rate per state, highest first.

    @param frame The cleaned poverty frame.
    @return A frame with `state` and `poverty_rate`.
    """
    return _mean_by_state(frame, POVERTY_COLUMN, descending=True)


def high_school_rate_by_state(frame: pl.DataFrame) -> pl.DataFrame:
    """@brief Mean high school completion rate per state, lowest first.

    @param frame The cleaned high school frame.
    @return A frame with `state` and `percent_completed_hs`.
    """
    return _mean_by_state(frame, HIGH_SCHOOL_COLUMN, descending=False)


def poverty_and_graduation_by_state(
    poverty_by_state: pl.DataFrame, graduation_by_state: pl.DataFrame
) -> pl.DataFrame:
    """@brief Join the two per-state frames on the state.

    @param poverty_by_state The result of `poverty_rate_by_state`.
    @param graduation_by_state The result of `high_school_rate_by_state`.
    @return The states present in both, sorted by state.
    """
    return poverty_by_state.join(
        graduation_by_state, on=STATE_COLUMN, how="inner"
    ).sort(STATE_COLUMN)


def correlation(frame: pl.DataFrame, left: str, right: str) -> float:
    """@brief Pearson correlation of two columns.

    @param frame The frame holding both columns.
    @param left The first column.
    @param right The second column.
    @return The Pearson coefficient between -1 and 1.
    """
    value = frame.select(pl.corr(left, right)).item()
    return float(value)
