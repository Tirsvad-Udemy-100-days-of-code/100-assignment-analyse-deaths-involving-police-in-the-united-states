"""@brief Plotly maps that save step screenshots (needs the `analysis` extra).

Plotly and kaleido come with the `analysis` extra; kaleido renders the PNG.
"""

from pathlib import Path

# plotly ships no type information; the two imports are the only untyped spots.
import plotly.express as px  # type: ignore[import-untyped]
import polars as pl
from plotly.graph_objects import Figure  # type: ignore[import-untyped]

from fatal_force.constants import MAP_HEIGHT, MAP_WIDTH
from fatal_force.infrastructure.paths import screenshot_file

_LOCATION_MODE = "USA-states"
_SCOPE = "usa"


def choropleth_figure(
    frame: pl.DataFrame,
    state_column: str,
    value_column: str,
    title: str,
    color_label: str,
) -> Figure:
    """@brief Colour the US states by a value.

    @param frame A polars frame with one row per state.
    @param state_column The column with the two-letter state codes.
    @param value_column The column that sets the colour of each state.
    @param title The map title.
    @param color_label The label of the colour bar.
    @return A figure with one choropleth trace.
    """
    return px.choropleth(
        frame,
        locations=state_column,
        color=value_column,
        locationmode=_LOCATION_MODE,
        scope=_SCOPE,
        title=title,
        labels={value_column: color_label},
    )


def save_plotly_figure(
    figure: Figure, step: int, slug: str, root: Path | None = None
) -> Path:
    """@brief Save a plotly figure as the screenshot of an analysis step.

    @param figure The figure to save.
    @param step The step number, 1 or higher.
    @param slug A short name for the step.
    @param root The root directory; defaults to the repository root.
    @return The path of the saved file.
    @throws ValueError When step is lower than 1.
    """
    path = screenshot_file(step, slug, root)
    path.parent.mkdir(parents=True, exist_ok=True)
    figure.write_image(path, width=MAP_WIDTH, height=MAP_HEIGHT)
    return path
