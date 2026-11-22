import polars as pl

from fatal_force.infrastructure.exploration import summarise_frame


def test_summarise_frame_reports_shape_nulls_and_duplicates() -> None:
    frame = pl.DataFrame({"a": ["1", "1", None], "b": ["x", "x", "y"]})
    summary = summarise_frame("demo", frame)
    assert (summary.name, summary.rows, summary.columns) == ("demo", 3, 2)
    assert summary.column_names == ("a", "b")
    assert summary.null_counts == {"a": 1, "b": 0}
    assert summary.duplicate_rows == 1


def test_summarise_frame_keeps_placeholders_as_present() -> None:
    summary = summarise_frame("demo", pl.DataFrame({"a": ["(X)", "-", ""]}))
    assert summary.null_counts == {"a": 0}


def test_summarise_frame_handles_empty_frame() -> None:
    summary = summarise_frame("e", pl.DataFrame({"a": []}))
    assert (summary.rows, summary.duplicate_rows) == (0, 0)
