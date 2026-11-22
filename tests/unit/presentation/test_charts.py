from datetime import date

import polars as pl
import pytest
from matplotlib.container import BarContainer
from matplotlib.figure import Figure
from matplotlib.patches import Wedge

from fatal_force.constants import FATALITIES_SOURCE_NOTE, SOURCE_NOTE
from fatal_force.presentation.charts import (
    bar_chart,
    donut_chart,
    dual_axis_line_chart,
    grouped_bar_chart,
    line_chart,
    ranked_bar_chart,
    scatter_with_fit_chart,
    stacked_bar_chart,
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


def _shares() -> pl.DataFrame:
    return pl.DataFrame(
        {
            "state": ["AL", "MS", "NY"],
            "share_white": [60.0, None, 50.0],
            "share_black": [30.0, 70.0, 10.0],
        }
    )


def test_stacked_bar_chart_draws_one_section_per_series_and_state() -> None:
    figure = stacked_bar_chart(
        _shares(), "state", ["share_white", "share_black"], ["White", "Black"], "T", "Y"
    )
    axes = figure.axes[0]
    assert len(axes.containers) == 2
    assert len(axes.patches) == 6
    legend = axes.get_legend()
    assert legend is not None
    assert [t.get_text() for t in legend.get_texts()] == ["White", "Black"]
    assert axes.get_title() == "T"
    assert _has_note(figure)


def test_stacked_bar_chart_rejects_mismatched_labels() -> None:
    with pytest.raises(ValueError, match="same length"):
        stacked_bar_chart(_shares(), "state", ["share_white"], [], "T", "Y")


def test_donut_chart_draws_one_wedge_per_row_with_legend_and_note() -> None:
    frame = pl.DataFrame({"race": ["Black", "White", "Unknown"], "deaths": [3, 2, 1]})
    figure = donut_chart(frame, "race", "deaths", "T")
    axes = figure.axes[0]
    assert len([p for p in axes.patches if isinstance(p, Wedge)]) == 3
    legend = axes.get_legend()
    assert legend is not None
    assert [t.get_text() for t in legend.get_texts()] == ["Black", "White", "Unknown"]
    assert any(text.get_text() == FATALITIES_SOURCE_NOTE for text in figure.texts)
    assert not _has_note(figure)


def test_bar_chart_prints_counts_on_vertical_bars_with_fatalities_note() -> None:
    frame = pl.DataFrame({"value": ["M", "F"], "count": [3, 2]})
    figure = bar_chart(frame, "value", "count", "T", "Deaths")
    axes = figure.axes[0]
    assert len(axes.patches) == 2
    assert [t.get_text() for t in axes.texts] == ["3", "2"]
    assert axes.get_ylabel() == "Deaths"
    assert any(text.get_text() == FATALITIES_SOURCE_NOTE for text in figure.texts)


def test_bar_chart_horizontal_puts_label_on_x_axis_and_custom_note() -> None:
    frame = pl.DataFrame({"value": ["gun", "knife"], "count": [5, 1]})
    figure = bar_chart(frame, "value", "count", "T", "Deaths", True, note="N")
    axes = figure.axes[0]
    assert axes.get_xlabel() == "Deaths"
    assert axes.yaxis_inverted()
    assert any(text.get_text() == "N" for text in figure.texts)


def _timeline() -> pl.DataFrame:
    return pl.DataFrame(
        {
            "month": [date(2015, 1, 1), date(2015, 2, 1), date(2015, 3, 1)],
            "deaths": [5, 7, 6],
            "smooth": [None, 6.0, 6.5],
        }
    )


def test_line_chart_draws_series_and_smoothed_line_with_note() -> None:
    figure = line_chart(_timeline(), "month", "deaths", "T", "Deaths", "smooth")
    axes = figure.axes[0]
    assert len(axes.lines) == 2
    assert axes.get_title() == "T"
    assert axes.get_ylabel() == "Deaths"
    assert axes.get_legend() is not None
    assert any(text.get_text() == FATALITIES_SOURCE_NOTE for text in figure.texts)


def test_line_chart_without_smooth_column_draws_one_line() -> None:
    figure = line_chart(_timeline(), "month", "deaths", "T", "Deaths")
    assert len(figure.axes[0].lines) == 1
    assert figure.axes[0].get_legend() is None


def test_grouped_bar_chart_draws_one_bar_per_row_and_series() -> None:
    frame = pl.DataFrame({"city": ["A", "B"], "W": [1.0, 2.0], "B": [3.0, None]})
    figure = grouped_bar_chart(frame, "city", ["W", "B"], ["White", "Black"], "T", "R")
    axes = figure.axes[0]
    assert len(axes.containers) == 2
    assert [len(c) for c in axes.containers] == [2, 2]
    assert [t.get_text() for t in axes.get_xticklabels()] == ["A", "B"]
    legend = axes.get_legend()
    assert legend is not None
    assert [t.get_text() for t in legend.get_texts()] == ["White", "Black"]


def test_grouped_bar_chart_rejects_mismatched_labels() -> None:
    frame = pl.DataFrame({"city": ["A"], "W": [1.0]})
    with pytest.raises(ValueError, match="same length"):
        grouped_bar_chart(frame, "city", ["W"], [], "T", "R")
