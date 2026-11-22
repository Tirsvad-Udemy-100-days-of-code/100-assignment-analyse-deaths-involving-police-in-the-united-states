"""@brief Count the deaths over time and fit their trend (needs polars)."""

import polars as pl

from fatal_force.constants import (
    DATE_COLUMN,
    DEATHS_COLUMN,
    MONTH_COLUMN,
    ROLLING_MEAN_SUFFIX,
    YEAR_COLUMN,
)
from fatal_force.domain.regression import LinearFit, fit_line


def deaths_per_month(fatalities: pl.DataFrame) -> pl.DataFrame:
    """@brief Count the deaths per calendar month, gaps filled with 0.

    @param fatalities The cleaned fatalities frame with a `date` column.
    @return A frame with `month` (first day of the month) and `deaths`, one row
        for every month from the first to the last death, in date order; empty
        for an empty input.
    """
    counts = (
        fatalities.select(pl.col(DATE_COLUMN).dt.month_start().alias(MONTH_COLUMN))
        .group_by(MONTH_COLUMN)
        .agg(pl.len().alias(DEATHS_COLUMN))
    )
    if counts.is_empty():
        return counts.select(MONTH_COLUMN, DEATHS_COLUMN).sort(MONTH_COLUMN)
    first, last = counts.select(
        pl.col(MONTH_COLUMN).min().alias("first"),
        pl.col(MONTH_COLUMN).max().alias("last"),
    ).row(0)
    months = pl.date_range(first, last, interval="1mo", eager=True)
    return (
        pl.DataFrame({MONTH_COLUMN: months})
        .join(counts, on=MONTH_COLUMN, how="left")
        .with_columns(pl.col(DEATHS_COLUMN).fill_null(0))
        .sort(MONTH_COLUMN)
    )


def deaths_per_year(fatalities: pl.DataFrame) -> pl.DataFrame:
    """@brief Count the deaths per calendar year.

    @param fatalities The cleaned fatalities frame with a `date` column.
    @return A frame with `year` and `deaths`, in year order; a partial first or
        last year counts only the days present.
    """
    return (
        fatalities.group_by(pl.col(DATE_COLUMN).dt.year().alias(YEAR_COLUMN))
        .agg(pl.len().alias(DEATHS_COLUMN))
        .sort(YEAR_COLUMN)
    )


def rolling_mean(frame: pl.DataFrame, column: str, window: int) -> pl.DataFrame:
    """@brief Add the trailing mean of a column over a window of rows.

    @param frame The frame, in the order to smooth.
    @param column The numeric column to smooth.
    @param window The number of rows averaged, 1 or higher.
    @return The frame with the extra column `<column>_rolling_mean`; the first
        `window - 1` rows are null.
    @throws ValueError When window is lower than 1.
    """
    if window < 1:
        message = f"window must be 1 or higher, got {window}"
        raise ValueError(message)
    return frame.with_columns(
        pl.col(column).rolling_mean(window).alias(column + ROLLING_MEAN_SUFFIX)
    )


def trend(frame: pl.DataFrame) -> LinearFit:
    """@brief Fit a line through the deaths per month.

    @param frame The result of `deaths_per_month`.
    @return The line of deaths against the month index (0 for the first month),
        so the slope is the change in deaths per month.
    @throws ValueError When the frame has fewer than 2 months.
    """
    deaths = [float(value) for value in frame[DEATHS_COLUMN].to_list()]
    return fit_line([float(index) for index in range(len(deaths))], deaths)
