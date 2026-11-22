"""@brief Matplotlib helpers that save step screenshots (needs the `analysis` extra).

The module never selects a backend; tests and scripts choose one.
"""

from pathlib import Path

from matplotlib.figure import Figure

from fatal_force.domain.summary import FrameSummary
from fatal_force.infrastructure.paths import screenshot_file

_TABLE_HEADER = ["Frame", "Rows", "Columns", "Nulls", "Duplicates"]
_FIGURE_WIDTH = 8.0
_ROW_HEIGHT = 0.5
_BASE_HEIGHT = 1.5
_SCREENSHOT_DPI = 150
_TABLE_SCALE = 1.4


def save_figure(figure: Figure, step: int, slug: str, root: Path | None = None) -> Path:
    """@brief Save a figure as the screenshot of an analysis step.

    @param figure The figure to save.
    @param step The step number, 1 or higher.
    @param slug A short name for the step.
    @param root The root directory; defaults to the repository root.
    @return The path of the saved file.
    @throws ValueError When step is lower than 1.
    """
    path = screenshot_file(step, slug, root)
    path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(path, dpi=_SCREENSHOT_DPI, bbox_inches="tight")
    return path


def summary_table_figure(title: str, summaries: list[FrameSummary]) -> Figure:
    """@brief Render exploration summaries as a table.

    @param title The figure title.
    @param summaries One summary per frame.
    @return A figure with one row per frame.
    """
    height = _BASE_HEIGHT + _ROW_HEIGHT * len(summaries)
    figure = Figure(figsize=(_FIGURE_WIDTH, height))
    axes = figure.subplots()
    axes.axis("off")
    axes.set_title(title)
    rows = [
        [s.name, s.rows, s.columns, s.null_total, s.duplicate_rows] for s in summaries
    ]
    if not rows:
        return figure
    table = axes.table(cellText=rows, colLabels=_TABLE_HEADER, loc="center")
    table.auto_set_font_size(False)
    table.auto_set_column_width(list(range(len(_TABLE_HEADER))))
    table.scale(1, _TABLE_SCALE)
    return figure
