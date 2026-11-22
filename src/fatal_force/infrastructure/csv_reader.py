"""@brief Read the course CSV files (needs the `analysis` extra for polars)."""

import io
from dataclasses import dataclass
from pathlib import Path

import polars as pl

from fatal_force.constants import (
    DATA_ENCODING,
    FATALITIES_FILE,
    HIGH_SCHOOL_COMPLETION_FILE,
    LINE_TERMINATOR_CR,
    LINE_TERMINATOR_CRLF,
    LINE_TERMINATOR_LF,
    MEDIAN_HOUSEHOLD_INCOME_FILE,
    POVERTY_FILE,
    README_DATA_HINT,
    SHARE_RACE_BY_CITY_FILE,
)
from fatal_force.domain.errors import DataFileNotFoundError
from fatal_force.infrastructure.paths import data_file


@dataclass(frozen=True, slots=True)
class Datasets:
    """@brief The five data frames of the assignment.

    @param hh_income Median household income per city.
    @param pct_poverty Poverty rate per city.
    @param pct_completed_hs High school completion rate per city.
    @param share_race_city Share of each race per city.
    @param fatalities Deaths involving police.
    """

    hh_income: pl.DataFrame
    pct_poverty: pl.DataFrame
    pct_completed_hs: pl.DataFrame
    share_race_city: pl.DataFrame
    fatalities: pl.DataFrame


def _normalise_line_endings(text: str) -> str:
    """@brief Turn CRLF and bare CR line terminators into LF.

    @param text The decoded file content.
    @return The text with LF line terminators only.
    """
    return text.replace(LINE_TERMINATOR_CRLF, LINE_TERMINATOR_LF).replace(
        LINE_TERMINATOR_CR, LINE_TERMINATOR_LF
    )


def read_course_csv(path: Path) -> pl.DataFrame:
    """@brief Read a course CSV file as text columns, exactly as stored.

    Every column is read as a string so that exploration shows the raw state;
    cleaning converts the types.

    @param path The CSV file.
    @return The raw data frame.
    @throws DataFileNotFoundError When the file does not exist.
    """
    if not path.is_file():
        message = f"Data file not found: {path}. {README_DATA_HINT}"
        raise DataFileNotFoundError(message)
    text = _normalise_line_endings(path.read_bytes().decode(DATA_ENCODING))
    return pl.read_csv(io.StringIO(text), infer_schema=False)


def load_datasets(data_dir: Path | None = None) -> Datasets:
    """@brief Read the five course files.

    @param data_dir The directory holding the files; defaults to the data directory.
    @return The raw datasets.
    @throws DataFileNotFoundError When one of the files is missing.
    """

    def read(name: str) -> pl.DataFrame:
        path = data_file(name) if data_dir is None else data_dir / name
        return read_course_csv(path)

    return Datasets(
        hh_income=read(MEDIAN_HOUSEHOLD_INCOME_FILE),
        pct_poverty=read(POVERTY_FILE),
        pct_completed_hs=read(HIGH_SCHOOL_COMPLETION_FILE),
        share_race_city=read(SHARE_RACE_BY_CITY_FILE),
        fatalities=read(FATALITIES_FILE),
    )
