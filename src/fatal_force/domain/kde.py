"""@brief Gaussian kernel density estimation with the standard library only."""

import math
import statistics
from collections.abc import Sequence

_MINIMUM_VALUES = 2
_SILVERMAN_FACTOR = 0.9
_SILVERMAN_EXPONENT = -1 / 5
_IQR_TO_SIGMA = 1.349
_SQRT_TWO_PI = math.sqrt(2 * math.pi)


def silverman_bandwidth(values: Sequence[float]) -> float:
    """@brief Silverman's rule of thumb for the Gaussian kernel bandwidth.

    Uses 0.9 * min(standard deviation, IQR / 1.349) * n^(-1/5).

    @param values The sample.
    @return The bandwidth.
    @throws ValueError When there are fewer than 2 values or all are equal.
    """
    if len(values) < _MINIMUM_VALUES:
        raise ValueError(f"at least {_MINIMUM_VALUES} values are needed")
    q1, _median, q3 = statistics.quantiles(values, n=4)
    spread: float = min(statistics.stdev(values), (q3 - q1) / _IQR_TO_SIGMA)
    if spread <= 0:
        spread = statistics.stdev(values)
    if spread <= 0:
        raise ValueError("values must not all be equal")
    return _SILVERMAN_FACTOR * spread * math.pow(len(values), _SILVERMAN_EXPONENT)


def gaussian_kde(
    values: Sequence[float], grid: Sequence[float], bandwidth: float | None = None
) -> list[float]:
    """@brief Estimate the probability density of a sample on a grid.

    @param values The sample.
    @param grid The points at which the density is evaluated.
    @param bandwidth The kernel width; Silverman's rule when None.
    @return The density at each grid point.
    @throws ValueError When there are fewer than 2 values or the bandwidth is
        not positive.
    """
    if len(values) < _MINIMUM_VALUES:
        raise ValueError(f"at least {_MINIMUM_VALUES} values are needed")
    width = silverman_bandwidth(values) if bandwidth is None else bandwidth
    if width <= 0:
        raise ValueError("bandwidth must be positive")
    scale = 1 / (len(values) * width * _SQRT_TWO_PI)
    return [
        scale * sum(math.exp(-0.5 * ((point - v) / width) ** 2) for v in values)
        for point in grid
    ]
