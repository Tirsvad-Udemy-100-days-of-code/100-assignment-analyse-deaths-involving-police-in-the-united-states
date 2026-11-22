"""@brief Clean the raw data frames (needs the `analysis` extra for polars)."""

import polars as pl

from fatal_force.constants import (
    AGE_COLUMN,
    BOOLEAN_COLUMNS,
    CENSUS_BOUND_PATTERN,
    CENSUS_PLACEHOLDERS,
    CENSUS_THOUSANDS_SEPARATOR,
    CITY_COLUMN,
    CITY_RAW_COLUMN,
    DATE_COLUMN,
    DATE_FORMAT,
    HIGH_SCHOOL_COLUMN,
    ID_COLUMN,
    INCOME_COLUMN,
    POVERTY_COLUMN,
    RAW_STATE_COLUMNS,
    SHARE_COLUMNS,
    STATE_COLUMN,
    TRUE_LABEL,
    UNKNOWN_FILL_COLUMNS,
    UNKNOWN_LABEL,
)
from fatal_force.infrastructure.csv_reader import Datasets


def _census_value(column: str) -> pl.Expr:
    """@brief Build the expression that turns a census text column into Float64.

    Placeholders become null; thousands separators and a trailing bound sign
    (as in "250,000+") are removed before the cast.

    @param column The column name.
    @return The expression producing the cleaned column.
    """
    text = pl.col(column).str.strip_chars()
    return (
        pl.when(text.is_in(list(CENSUS_PLACEHOLDERS)))
        .then(None)
        .otherwise(text)
        .str.replace_all(CENSUS_THOUSANDS_SEPARATOR, "", literal=True)
        .str.replace(CENSUS_BOUND_PATTERN, "")
        .cast(pl.Float64, strict=False)
        .alias(column)
    )


def _rename_location_columns(frame: pl.DataFrame) -> pl.DataFrame:
    """@brief Give the state and city columns their consistent names.

    @param frame A raw census frame.
    @return The frame with columns `state` and `city`.
    """
    mapping = {c: STATE_COLUMN for c in RAW_STATE_COLUMNS if c in frame.columns}
    if CITY_RAW_COLUMN in frame.columns:
        mapping[CITY_RAW_COLUMN] = CITY_COLUMN
    return frame.rename(mapping)


def clean_census_frame(frame: pl.DataFrame, value_columns: list[str]) -> pl.DataFrame:
    """@brief Clean a census frame; missing values stay null.

    @param frame A raw census frame.
    @param value_columns The columns holding numeric values.
    @return The frame with placeholders as null, Float64 values and renamed
        state and city columns.
    """
    text_columns = [c for c in frame.columns if c not in value_columns]
    stripped = frame.with_columns(pl.col(text_columns).str.strip_chars())
    cleaned = stripped.with_columns([_census_value(c) for c in value_columns])
    return _rename_location_columns(cleaned)


def missing_census_values_as_zero(
    frame: pl.DataFrame, columns: list[str]
) -> pl.DataFrame:
    """@brief Replace missing census values by 0, as the lecture suggests.

    This hides missing data, so it is a separate, explicit step and is never
    applied by `clean_census_frame`.

    @param frame A cleaned census frame.
    @param columns The numeric columns to fill.
    @return The frame with nulls in those columns replaced by 0.
    """
    return frame.with_columns(pl.col(columns).fill_null(0.0))


def _drop_duplicate_ids(frame: pl.DataFrame) -> pl.DataFrame:
    """@brief Keep the first row of each id.

    @param frame A raw fatalities frame.
    @return The frame without repeated ids.
    """
    return frame.unique(subset=[ID_COLUMN], keep="first", maintain_order=True)


def _parse_fatality_types(frame: pl.DataFrame) -> pl.DataFrame:
    """@brief Convert date, age, id and boolean columns to their types.

    @param frame A fatalities frame with text columns.
    @return The frame with Date, Int64 and Boolean columns.
    """
    return frame.with_columns(
        pl.col(DATE_COLUMN).str.to_date(DATE_FORMAT),
        pl.col(ID_COLUMN).cast(pl.Int64),
        pl.col(AGE_COLUMN).cast(pl.Int64, strict=False),
        *[pl.col(c).str.to_uppercase() == TRUE_LABEL for c in BOOLEAN_COLUMNS],
    )


def _fill_unknown_labels(frame: pl.DataFrame) -> pl.DataFrame:
    """@brief Replace nulls in the categorical columns by the unknown label.

    @param frame A fatalities frame.
    @return The frame with no nulls in the categorical columns.
    """
    return frame.with_columns(
        pl.col(list(UNKNOWN_FILL_COLUMNS)).fill_null(UNKNOWN_LABEL)
    )


def clean_fatalities(frame: pl.DataFrame) -> pl.DataFrame:
    """@brief Clean the fatalities frame; age stays null when missing.

    @param frame The raw fatalities frame.
    @return The frame without repeated ids, with typed columns and `unknown`
        labels for missing categories.
    """
    return _fill_unknown_labels(_parse_fatality_types(_drop_duplicate_ids(frame)))


def clean_all(datasets: Datasets) -> Datasets:
    """@brief Clean the five datasets.

    @param datasets The raw datasets.
    @return The cleaned datasets.
    """
    return Datasets(
        hh_income=clean_census_frame(datasets.hh_income, [INCOME_COLUMN]),
        pct_poverty=clean_census_frame(datasets.pct_poverty, [POVERTY_COLUMN]),
        pct_completed_hs=clean_census_frame(
            datasets.pct_completed_hs, [HIGH_SCHOOL_COLUMN]
        ),
        share_race_city=clean_census_frame(
            datasets.share_race_city, list(SHARE_COLUMNS)
        ),
        fatalities=clean_fatalities(datasets.fatalities),
    )
