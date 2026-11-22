"""@brief Least-squares line fitting with the standard library only."""

import statistics
from collections.abc import Sequence
from dataclasses import dataclass

_MINIMUM_POINTS = 2


@dataclass(frozen=True, slots=True)
class LinearFit:
    """@brief A fitted line y = slope * x + intercept.

    @param slope The slope of the line.
    @param intercept The value of y at x = 0.
    @param r_value The Pearson correlation of the points.
    """

    slope: float
    intercept: float
    r_value: float


def fit_line(xs: Sequence[float], ys: Sequence[float]) -> LinearFit:
    """@brief Fit a least-squares line through the points.

    @param xs The x values.
    @param ys The y values, one per x.
    @return The slope, intercept and correlation.
    @throws ValueError When there are fewer than 2 points or the lengths differ.
    """
    if len(xs) != len(ys):
        raise ValueError("xs and ys must have the same length")
    if len(xs) < _MINIMUM_POINTS:
        raise ValueError(f"at least {_MINIMUM_POINTS} points are needed to fit a line")
    slope, intercept = statistics.linear_regression(xs, ys)
    return LinearFit(slope, intercept, statistics.correlation(xs, ys))
