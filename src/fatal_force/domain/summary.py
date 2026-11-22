"""@brief The result of the preliminary exploration of one data frame."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class FrameSummary:
    """@brief Shape, columns, missing values and duplicates of one frame.

    @param name The name of the frame.
    @param rows The number of rows.
    @param columns The number of columns.
    @param column_names The column names in order.
    @param null_counts The number of null values per column.
    @param duplicate_rows The number of rows that repeat an earlier row.
    """

    name: str
    rows: int
    columns: int
    column_names: tuple[str, ...]
    null_counts: dict[str, int]
    duplicate_rows: int

    @property
    def null_total(self) -> int:
        """@brief Count all null values of the frame.

        @return The sum of the null counts of every column.
        """
        return sum(self.null_counts.values())
