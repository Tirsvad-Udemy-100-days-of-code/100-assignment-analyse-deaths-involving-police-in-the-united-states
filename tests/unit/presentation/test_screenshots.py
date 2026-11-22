from pathlib import Path

import pytest

from fatal_force.domain.summary import FrameSummary
from fatal_force.presentation.screenshots import save_figure, summary_table_figure


def _summaries() -> list[FrameSummary]:
    return [FrameSummary("fatalities", 10, 3, ("a", "b", "c"), {"a": 2, "b": 1}, 4)]


def test_summary_table_figure_has_header_and_one_row_per_frame() -> None:
    figure = summary_table_figure("Exploration", _summaries())
    table = figure.axes[0].tables[0]
    texts = {cell.get_text().get_text() for cell in table.get_celld().values()}
    assert {"Frame", "fatalities", "10", "3", "4"} <= texts


def test_save_figure_creates_folder_and_png(tmp_path: Path) -> None:
    figure = summary_table_figure("Exploration", _summaries())
    path = save_figure(figure, 1, "explore", tmp_path)
    assert path == tmp_path / "docs" / "screenshots" / "step-01-explore.png"
    assert path.read_bytes().startswith(b"\x89PNG")


def test_save_figure_rejects_step_below_one(tmp_path: Path) -> None:
    figure = summary_table_figure("x", [])
    with pytest.raises(ValueError, match="step"):
        save_figure(figure, 0, "x", tmp_path)
