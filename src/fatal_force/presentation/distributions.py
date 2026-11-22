"""@brief Matplotlib charts of age distributions.

Figures are built without pyplot; the module never selects a backend.
"""

from collections.abc import Sequence

from matplotlib.figure import Figure

from fatal_force.constants import FATALITIES_SOURCE_NOTE
from fatal_force.domain.kde import gaussian_kde
from fatal_force.presentation.charts import add_source_note

_FIGURE_SIZE = (10.0, 6.0)
_GRID_POINTS = 200
_GRID_MARGIN_FRACTION = 0.1
_HISTOGRAM_COLOR = "tab:blue"
_HISTOGRAM_ALPHA = 0.5
_KDE_COLOR = "tab:red"
_DENSITY_LABEL = "Density"
_KDE_LABEL = "Gaussian KDE"
_LEGEND_LABEL_TEMPLATE = "{group} (n={count})"


def _grid(values: Sequence[float]) -> list[float]:
    """@brief Build an evenly spaced grid that spans the sample with a margin.

    @param values The sample.
    @return The grid points from slightly below the minimum to above the maximum.
    """
    low, high = min(values), max(values)
    margin = (high - low) * _GRID_MARGIN_FRACTION or 1.0
    step = (high - low + 2 * margin) / (_GRID_POINTS - 1)
    return [low - margin + step * index for index in range(_GRID_POINTS)]


def histogram_with_kde_chart(
    values: Sequence[float], title: str, x_label: str, bins: int
) -> Figure:
    """@brief Draw a density histogram with its Gaussian KDE line.

    @param values The sample.
    @param title The chart title.
    @param x_label The label of the x axis.
    @param bins The number of histogram bins.
    @return The figure with one axes.
    @throws ValueError When the sample has fewer than 2 values.
    """
    grid = _grid(values)
    density = gaussian_kde(values, grid)
    figure = Figure(figsize=_FIGURE_SIZE, layout="constrained")
    axes = figure.subplots()
    axes.hist(
        values,
        bins=bins,
        density=True,
        color=_HISTOGRAM_COLOR,
        alpha=_HISTOGRAM_ALPHA,
        label=_DENSITY_LABEL,
    )
    axes.plot(grid, density, color=_KDE_COLOR, label=_KDE_LABEL)
    axes.set_title(title)
    axes.set_xlabel(x_label)
    axes.set_ylabel(_DENSITY_LABEL)
    axes.legend()
    add_source_note(figure, FATALITIES_SOURCE_NOTE)
    return figure


def box_plot_chart(groups: dict[str, list[float]], title: str, y_label: str) -> Figure:
    """@brief Draw one box per group, labelled with the group name.

    @param groups The values per group name.
    @param title The chart title.
    @param y_label The label of the value axis.
    @return The figure with one axes.
    """
    figure = Figure(figsize=_FIGURE_SIZE, layout="constrained")
    axes = figure.subplots()
    axes.boxplot(list(groups.values()), tick_labels=list(groups))
    axes.set_title(title)
    axes.set_ylabel(y_label)
    add_source_note(figure, FATALITIES_SOURCE_NOTE)
    return figure


def kde_by_group_chart(
    groups: dict[str, list[float]], title: str, x_label: str
) -> Figure:
    """@brief Draw one Gaussian KDE line per group; the legend shows each n.

    A group with fewer than 2 values has no density and is left out; all
    lines share one grid.

    @param groups The values per group name.
    @param title The chart title.
    @param x_label The label of the x axis.
    @return The figure with one axes.
    @throws ValueError When no group has 2 values or a group's values are all equal.
    """
    usable = {name: values for name, values in groups.items() if len(values) >= 2}
    figure = Figure(figsize=_FIGURE_SIZE, layout="constrained")
    axes = figure.subplots()
    grid = _grid([value for values in usable.values() for value in values])
    for name, values in usable.items():
        axes.plot(
            grid,
            gaussian_kde(values, grid),
            label=_LEGEND_LABEL_TEMPLATE.format(group=name, count=len(values)),
        )
    axes.set_title(title)
    axes.set_xlabel(x_label)
    axes.set_ylabel(_DENSITY_LABEL)
    axes.legend()
    add_source_note(figure, FATALITIES_SOURCE_NOTE)
    return figure
