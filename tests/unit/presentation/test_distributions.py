import pytest
from matplotlib.patches import Rectangle

from fatal_force.constants import FATALITIES_SOURCE_NOTE
from fatal_force.presentation.distributions import (
    box_plot_chart,
    histogram_with_kde_chart,
    kde_by_group_chart,
)

_AGES = [20.0, 25.0, 30.0, 35.0, 40.0, 22.0, 28.0]


def test_histogram_with_kde_chart_has_bars_line_and_note() -> None:
    figure = histogram_with_kde_chart(_AGES, "T", "Age", 5)
    axes = figure.axes[0]
    assert len([p for p in axes.patches if isinstance(p, Rectangle)]) == 5
    assert len(axes.lines) == 1
    assert axes.get_title() == "T"
    assert any(text.get_text() == FATALITIES_SOURCE_NOTE for text in figure.texts)


def test_histogram_with_kde_chart_rejects_single_value() -> None:
    with pytest.raises(ValueError, match="at least 2 values"):
        histogram_with_kde_chart([1.0], "T", "Age", 5)


def test_box_plot_chart_draws_one_box_per_group() -> None:
    figure = box_plot_chart({"A": _AGES, "B": _AGES[:4]}, "T", "Age")
    axes = figure.axes[0]
    assert [t.get_text() for t in axes.get_xticklabels()] == ["A", "B"]
    assert len(axes.lines) > 0
    assert any(text.get_text() == FATALITIES_SOURCE_NOTE for text in figure.texts)


def test_kde_by_group_chart_draws_one_line_per_group_with_n_in_legend() -> None:
    figure = kde_by_group_chart({"A": _AGES, "B": _AGES[:4]}, "T", "Age")
    axes = figure.axes[0]
    assert len(axes.lines) == 2
    legend = axes.get_legend()
    assert legend is not None
    assert [t.get_text() for t in legend.get_texts()] == ["A (n=7)", "B (n=4)"]
    assert any(text.get_text() == FATALITIES_SOURCE_NOTE for text in figure.texts)


def test_kde_by_group_chart_skips_group_with_one_value() -> None:
    figure = kde_by_group_chart({"A": _AGES, "B": [30.0]}, "T", "Age")
    assert len(figure.axes[0].lines) == 1
