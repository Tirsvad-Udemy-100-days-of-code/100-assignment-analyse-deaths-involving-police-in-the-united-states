"""@brief Matplotlib charts for the poverty and graduation analysis.

Figures are built without pyplot; the module never selects a backend.
"""

from collections.abc import Sequence
from typing import Literal

import polars as pl
from matplotlib.figure import Figure

from fatal_force.constants import FATALITIES_SOURCE_NOTE, SOURCE_NOTE
from fatal_force.domain.regression import fit_line

_BAR_WIDTH = 9.0
_BAR_ROW_HEIGHT = 0.28
_BAR_BASE_HEIGHT = 2.0
_BAR_FONT_SIZE = 8
_HIGHLIGHT_COLOR = "tab:red"
_BAR_COLOR = "tab:blue"
_LEFT_COLOR = "tab:red"
_RIGHT_COLOR = "tab:blue"
_LINE_FIGURE_SIZE = (12.0, 6.0)
_SCATTER_FIGURE_SIZE = (8.0, 6.0)
_LABEL_ROTATION = 90
_LABEL_FONT_SIZE = 8
_POINT_ALPHA = 0.8
_NOTE_X = 0.99
_NOTE_Y = 0.01
_NOTE_FONT_SIZE = 8
_FIT_POINTS = 2
_LEGEND_LOCATION: Literal["upper right"] = "upper right"
_FIT_COLOR = "black"
_NOTE_MARGIN = 0.03
_STACKED_FIGURE_SIZE = (14.0, 6.0)
_DONUT_FIGURE_SIZE = (8.0, 6.0)
_COUNT_FIGURE_SIZE = (10.0, 6.0)
_DONUT_WIDTH = 0.4
_DONUT_PERCENT_FORMAT = "%1.1f%%"
_DONUT_PERCENT_DISTANCE = 0.8
_DONUT_LEGEND_LOCATION: Literal["center left"] = "center left"
_DONUT_LEGEND_ANCHOR = (1.0, 0.5)


def add_source_note(figure: Figure, note: str = SOURCE_NOTE) -> None:
    """@brief Put the data source at the bottom right of the figure.

    @param figure The figure to annotate.
    @param note The source text; defaults to the census note.
    """
    figure.tight_layout(rect=(0, _NOTE_MARGIN, 1, 1))
    figure.text(
        _NOTE_X, _NOTE_Y, note, ha="right", va="bottom", fontsize=_NOTE_FONT_SIZE
    )


def ranked_bar_chart(
    frame: pl.DataFrame,
    label_column: str,
    value_column: str,
    title: str,
    x_label: str,
    highlight_first: int = 1,
) -> Figure:
    """@brief Draw a horizontal bar chart in the order of the frame, first row on top.

    @param frame The frame holding the labels and values.
    @param label_column The column with the bar labels.
    @param value_column The column with the bar lengths.
    @param title The chart title.
    @param x_label The label of the value axis.
    @param highlight_first How many leading bars get the highlight color.
    @return The figure with one axes.
    """
    labels = frame[label_column].to_list()
    values = frame[value_column].to_list()
    height = _BAR_BASE_HEIGHT + _BAR_ROW_HEIGHT * len(labels)
    figure = Figure(figsize=(_BAR_WIDTH, height), layout="constrained")
    axes = figure.subplots()
    colors = [
        _HIGHLIGHT_COLOR if index < highlight_first else _BAR_COLOR
        for index in range(len(labels))
    ]
    axes.barh(labels, values, color=colors)
    axes.invert_yaxis()
    axes.tick_params(axis="y", labelsize=_BAR_FONT_SIZE)
    axes.set_title(title)
    axes.set_xlabel(x_label)
    add_source_note(figure)
    return figure


def dual_axis_line_chart(
    frame: pl.DataFrame,
    label_column: str,
    left_column: str,
    right_column: str,
    title: str,
    left_label: str,
    right_label: str,
) -> Figure:
    """@brief Draw two lines on separate y axes over the labels in the x axis.

    @param frame The frame holding the labels and both series.
    @param label_column The column with the x axis labels.
    @param left_column The series drawn against the left axis.
    @param right_column The series drawn against the right axis.
    @param title The chart title.
    @param left_label The label of the left axis and its legend entry.
    @param right_label The label of the right axis and its legend entry.
    @return The figure with a left and a right axes.
    """
    labels = frame[label_column].to_list()
    figure = Figure(figsize=_LINE_FIGURE_SIZE, layout="constrained")
    left_axes = figure.subplots()
    right_axes = left_axes.twinx()
    (left_line,) = left_axes.plot(
        labels, frame[left_column].to_list(), color=_LEFT_COLOR, label=left_label
    )
    (right_line,) = right_axes.plot(
        labels, frame[right_column].to_list(), color=_RIGHT_COLOR, label=right_label
    )
    left_axes.set_ylabel(left_label, color=_LEFT_COLOR)
    right_axes.set_ylabel(right_label, color=_RIGHT_COLOR)
    left_axes.tick_params(
        axis="x", labelrotation=_LABEL_ROTATION, labelsize=_LABEL_FONT_SIZE
    )
    left_axes.set_title(title)
    left_axes.legend(handles=[left_line, right_line], loc=_LEGEND_LOCATION)
    add_source_note(figure)
    return figure


def scatter_with_fit_chart(
    frame: pl.DataFrame,
    x_column: str,
    y_column: str,
    title: str,
    x_label: str,
    y_label: str,
    label_column: str,
) -> Figure:
    """@brief Draw a scatter plot with its least-squares line and r.

    @param frame The frame holding the points.
    @param x_column The column for the x values.
    @param y_column The column for the y values.
    @param title The chart title.
    @param x_label The label of the x axis.
    @param y_label The label of the y axis.
    @param label_column The column naming each point; shown next to it.
    @return The figure with one axes.
    @throws ValueError When the frame has fewer than 2 rows.
    """
    xs = frame[x_column].to_list()
    ys = frame[y_column].to_list()
    labels = frame[label_column].to_list()
    fit = fit_line(xs, ys)
    figure = Figure(figsize=_SCATTER_FIGURE_SIZE, layout="constrained")
    axes = figure.subplots()
    axes.scatter(xs, ys, alpha=_POINT_ALPHA, label="States")
    for x, y, text in zip(xs, ys, labels, strict=True):
        axes.annotate(text, (x, y), fontsize=_LABEL_FONT_SIZE)
    line_xs = [min(xs), max(xs)][:_FIT_POINTS]
    axes.plot(
        line_xs,
        [fit.slope * x + fit.intercept for x in line_xs],
        color=_FIT_COLOR,
        label=f"Linear fit (r = {fit.r_value:.2f})",
    )
    axes.set_title(title)
    axes.set_xlabel(x_label)
    axes.set_ylabel(y_label)
    axes.legend()
    add_source_note(figure)
    return figure


def stacked_bar_chart(
    frame: pl.DataFrame,
    label_column: str,
    value_columns: Sequence[str],
    series_labels: Sequence[str],
    title: str,
    y_label: str,
) -> Figure:
    """@brief Draw one stacked bar per row, one section per value column.

    @param frame The frame holding the labels and the series.
    @param label_column The column with the bar labels.
    @param value_columns The columns stacked from the bottom, in order.
    @param series_labels The legend text of each value column.
    @param title The chart title.
    @param y_label The label of the value axis.
    @return The figure with one axes.
    @throws ValueError When the columns and the labels differ in number.
    """
    if len(value_columns) != len(series_labels):
        raise ValueError("value_columns and series_labels must have the same length")
    labels = frame[label_column].to_list()
    bottoms = [0.0] * len(labels)
    figure = Figure(figsize=_STACKED_FIGURE_SIZE, layout="constrained")
    axes = figure.subplots()
    for column, series_label in zip(value_columns, series_labels, strict=True):
        values = [value or 0.0 for value in frame[column].to_list()]
        axes.bar(labels, values, bottom=bottoms, label=series_label)
        bottoms = [
            bottom + value for bottom, value in zip(bottoms, values, strict=True)
        ]
    axes.tick_params(
        axis="x", labelrotation=_LABEL_ROTATION, labelsize=_LABEL_FONT_SIZE
    )
    axes.set_title(title)
    axes.set_ylabel(y_label)
    axes.legend(loc=_LEGEND_LOCATION)
    add_source_note(figure)
    return figure


def donut_chart(
    frame: pl.DataFrame, label_column: str, value_column: str, title: str
) -> Figure:
    """@brief Draw a donut with the percentage of each slice and a legend.

    @param frame The frame holding the labels and the counts.
    @param label_column The column naming each slice.
    @param value_column The column with the slice sizes.
    @param title The chart title.
    @return The figure with one axes.
    """
    labels = frame[label_column].to_list()
    figure = Figure(figsize=_DONUT_FIGURE_SIZE, layout="constrained")
    axes = figure.subplots()
    wedges, _texts, _percents = axes.pie(
        frame[value_column].to_list(),
        autopct=_DONUT_PERCENT_FORMAT,
        pctdistance=_DONUT_PERCENT_DISTANCE,
        wedgeprops={"width": _DONUT_WIDTH},
    )
    axes.legend(
        wedges,
        labels,
        loc=_DONUT_LEGEND_LOCATION,
        bbox_to_anchor=_DONUT_LEGEND_ANCHOR,
    )
    axes.set_title(title)
    add_source_note(figure, FATALITIES_SOURCE_NOTE)
    return figure


def bar_chart(
    frame: pl.DataFrame,
    label_column: str,
    value_column: str,
    title: str,
    y_label: str,
    horizontal: bool = False,
    note: str = FATALITIES_SOURCE_NOTE,
) -> Figure:
    """@brief Draw one bar per row with the value printed on the bar.

    @param frame The frame holding the labels and values.
    @param label_column The column with the bar labels.
    @param value_column The column with the bar lengths.
    @param title The chart title.
    @param y_label The label of the value axis.
    @param horizontal True to draw horizontal bars, first row on top.
    @param note The source note; defaults to the fatalities note.
    @return The figure with one axes.
    """
    labels = [str(label) for label in frame[label_column].to_list()]
    values = frame[value_column].to_list()
    figure = Figure(figsize=_COUNT_FIGURE_SIZE, layout="constrained")
    axes = figure.subplots()
    if horizontal:
        container = axes.barh(labels, values, color=_BAR_COLOR)
        axes.invert_yaxis()
        axes.set_xlabel(y_label)
    else:
        container = axes.bar(labels, values, color=_BAR_COLOR)
        axes.set_ylabel(y_label)
    axes.bar_label(container, fontsize=_BAR_FONT_SIZE)
    axes.set_title(title)
    add_source_note(figure, note)
    return figure
