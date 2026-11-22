from collections.abc import Callable
from pathlib import Path

import pytest

from fatal_force import constants
from fatal_force.domain.errors import DataFileNotFoundError
from fatal_force.infrastructure.csv_reader import load_datasets, read_course_csv

WriteCsv = Callable[[str, list[str]], Path]


def test_read_course_csv_decodes_cp1252_and_bare_cr(write_csv: WriteCsv) -> None:
    path = write_csv("a.csv", ["City,n", "Cañon,1", "Zürich,2"])
    frame = read_course_csv(path)
    assert frame.shape == (2, 2)
    assert frame["City"].to_list() == ["Cañon", "Zürich"]


def test_read_course_csv_handles_crlf(tmp_path: Path) -> None:
    path = tmp_path / "a.csv"
    path.write_bytes(b"a,b\r\n1,2\r\n")
    assert read_course_csv(path).shape == (1, 2)


def test_read_course_csv_keeps_values_as_text(write_csv: WriteCsv) -> None:
    frame = read_course_csv(write_csv("a.csv", ["a", "(X)", "1"]))
    assert frame["a"].to_list() == ["(X)", "1"]


def test_read_course_csv_raises_when_file_missing(tmp_path: Path) -> None:
    with pytest.raises(DataFileNotFoundError, match="README.md"):
        read_course_csv(tmp_path / "missing.csv")


def test_load_datasets_reads_five_files(tmp_path: Path) -> None:
    names = [
        constants.MEDIAN_HOUSEHOLD_INCOME_FILE,
        constants.POVERTY_FILE,
        constants.HIGH_SCHOOL_COMPLETION_FILE,
        constants.SHARE_RACE_BY_CITY_FILE,
        constants.FATALITIES_FILE,
    ]
    for name in names:
        (tmp_path / name).write_bytes(b"a,b\r1,2")
    datasets = load_datasets(tmp_path)
    assert datasets.fatalities.shape == (1, 2)
    assert datasets.hh_income.shape == (1, 2)


def test_load_datasets_raises_when_a_file_is_missing(tmp_path: Path) -> None:
    with pytest.raises(DataFileNotFoundError):
        load_datasets(tmp_path)
