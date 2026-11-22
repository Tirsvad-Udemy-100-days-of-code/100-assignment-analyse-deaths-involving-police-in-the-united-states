from pathlib import Path

import polars as pl
import pytest
from plotly.graph_objects import Figure  # type: ignore[import-untyped]

from fatal_force.presentation.maps import choropleth_figure, save_plotly_figure


def _frame() -> pl.DataFrame:
    return pl.DataFrame({"state": ["CA", "TX", "NY"], "deaths": [3, 2, 1]})


def test_choropleth_figure_has_one_choropleth_trace_with_states() -> None:
    figure = choropleth_figure(_frame(), "state", "deaths", "Deaths", "Deaths")
    assert len(figure.data) == 1
    trace = figure.data[0]
    assert trace.type == "choropleth"
    assert list(trace.locations) == ["CA", "TX", "NY"]
    assert trace.locationmode == "USA-states"
    assert figure.layout.title.text == "Deaths"


def test_save_plotly_figure_writes_to_screenshot_path(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    calls: list[tuple[Path, int, int]] = []

    def fake_write_image(self: Figure, file: Path, *, width: int, height: int) -> None:
        calls.append((file, width, height))

    monkeypatch.setattr(Figure, "write_image", fake_write_image)
    path = save_plotly_figure(Figure(), 18, "map", tmp_path)
    assert path == tmp_path / "docs" / "screenshots" / "step-18-map.png"
    assert path.parent.is_dir()
    assert calls == [(path, 1100, 650)]


def test_save_plotly_figure_rejects_step_below_one(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="step"):
        save_plotly_figure(Figure(), 0, "x", tmp_path)
