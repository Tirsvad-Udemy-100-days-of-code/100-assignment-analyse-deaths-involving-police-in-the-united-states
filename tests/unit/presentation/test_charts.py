import polars as pl
import pytest
from matplotlib.container import BarContainer
from matplotlib.figure import Figure

from fatal_force.constants import SOURCE_NOTE
from fatal_force.presentation.charts import (
    dual_axis_line_chart,
    ranked_bar_chart,
    scatter_with_fit_chart,
)


def _frame() -> pl.DataFrame:
    return pl.DataFrame(
        {
            "state": ["AL", "MS", "NY"],
            "poverty_rate": [20.0, 30.0, 10.0],
            "percent_completed_hs": [80.0, 70.0, 90.0],
        }
    )


def _has_note(figure: Figure) -> bool:
    return any(text.get_text() == SOURCE_NOTE for text in figure.texts)


def test_ranked_bar_chart_draws_one_bar_per_row_with_note() -> None:
    figure = ranked_bar_chart(_frame(), "state", "poverty_rate", "T", "X")
    container = figure.axes[0].containers[0]
    assert isinstance(container, BarContainer)
    assert len(container.patches) == 3
    assert figure.axes[0].get_title() == "T"
    assert _has_note(figure)


def test_ranked_bar_chart_highlights_leading_bars() -> None:
    figure = ranked_bar_chart(_frame(), "state", "poverty_rate", "T", "X", 2)
    container = figure.axes[0].containers[0]
    assert isinstance(container, BarContainer)
    colors = [patch.get_facecolor() for patch in container.patches]
    assert colors[0] == colors[1] != colors[2]


def test_dual_axis_line_chart_has_two_axes_and_legend() -> None:
    figure = dual_axis_line_chart(
        _frame(), "state", "poverty_rate", "percent_completed_hs", "T", "L", "R"
    )
    assert len(figure.axes) == 2
    legend = figure.axes[0].get_legend()
    assert legend is not None
    assert [t.get_text() for t in legend.get_texts()] == ["L", "R"]
    assert _has_note(figure)


def test_scatter_with_fit_chart_shows_r_in_legend() -> None:
    figure = scatter_with_fit_chart(
        _frame(), "poverty_rate", "percent_completed_hs", "T", "X", "Y", "state"
    )
    legend = figure.axes[0].get_legend()
    assert legend is not None
    assert any("r = -1.00" in t.get_text() for t in legend.get_texts())
    assert _has_note(figure)


def test_scatter_with_fit_chart_rejects_single_point() -> None:
    with pytest.raises(ValueError, match="at least 2 points"):
        scatter_with_fit_chart(
            _frame().head(1),
            "poverty_rate",
            "percent_completed_hs",
            "T",
            "X",
            "Y",
            "state",
        )
