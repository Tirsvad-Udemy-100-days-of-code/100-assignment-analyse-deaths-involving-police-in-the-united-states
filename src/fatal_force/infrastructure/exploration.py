"""@brief Preliminary data exploration (needs the `analysis` extra for polars)."""

import polars as pl

from fatal_force.domain.summary import FrameSummary


def summarise_frame(name: str, frame: pl.DataFrame) -> FrameSummary:
    """@brief Describe the raw state of a frame.

    Empty strings and census placeholders are not counted as missing here;
    cleaning turns them into nulls.

    @param name The name of the frame.
    @param frame The frame to describe.
    @return Rows, columns, null counts per column and duplicate rows.
    """
    nulls = frame.null_count().row(0, named=True)
    return FrameSummary(
        name=name,
        rows=frame.height,
        columns=frame.width,
        column_names=tuple(frame.columns),
        null_counts={column: int(count) for column, count in nulls.items()},
        duplicate_rows=frame.height - frame.unique().height,
    )
