from pathlib import Path

import pytest

from fatal_force.infrastructure.paths import data_file, screenshot_file


def test_data_file_joins_root_data_dir_and_name(tmp_path: Path) -> None:
    assert data_file("a.csv", tmp_path) == tmp_path / "data" / "a.csv"


def test_data_file_defaults_to_repository_root() -> None:
    path = data_file("a.csv")
    assert path.name == "a.csv"
    assert (path.parents[1] / "pyproject.toml").is_file()


def test_screenshot_file_pads_step_to_two_digits(tmp_path: Path) -> None:
    expected = tmp_path / "docs" / "screenshots" / "step-03-race.png"
    assert screenshot_file(3, "race", tmp_path) == expected


def test_screenshot_file_keeps_two_digit_step(tmp_path: Path) -> None:
    assert screenshot_file(12, "map", tmp_path).name == "step-12-map.png"


def test_screenshot_file_accepts_first_step(tmp_path: Path) -> None:
    assert screenshot_file(1, "a", tmp_path).name == "step-01-a.png"


def test_screenshot_file_defaults_to_repository_root() -> None:
    path = screenshot_file(1, "a")
    assert (path.parents[2] / "pyproject.toml").is_file()


@pytest.mark.parametrize("step", [0, -1])
def test_screenshot_file_rejects_step_below_one(step: int, tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="step must be 1 or higher"):
        screenshot_file(step, "x", tmp_path)
