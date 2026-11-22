import math

import pytest

from fatal_force.domain.kde import gaussian_kde, silverman_bandwidth


def _wide_grid() -> list[float]:
    return [-20.0 + 0.05 * index for index in range(1201)]


def test_gaussian_kde_integrates_to_about_one_on_wide_grid() -> None:
    grid = _wide_grid()
    density = gaussian_kde([1.0, 2.0, 2.5, 4.0], grid)
    assert sum(density) * 0.05 == pytest.approx(1.0, abs=1e-3)


def test_gaussian_kde_peaks_near_the_sample_mean_of_symmetric_data() -> None:
    grid = [0.0, 1.0, 2.0, 3.0, 4.0]
    density = gaussian_kde([1.0, 2.0, 3.0], grid, bandwidth=0.5)
    assert grid[density.index(max(density))] == 2.0


def test_gaussian_kde_matches_single_kernel_formula() -> None:
    density = gaussian_kde([0.0, 0.0], [0.0], bandwidth=2.0)
    assert density == [pytest.approx(1 / (2.0 * math.sqrt(2 * math.pi)))]


def test_gaussian_kde_rejects_fewer_than_two_values() -> None:
    with pytest.raises(ValueError, match="at least 2 values"):
        gaussian_kde([1.0], [0.0])


@pytest.mark.parametrize("bandwidth", [0.0, -1.0])
def test_gaussian_kde_rejects_non_positive_bandwidth(bandwidth: float) -> None:
    with pytest.raises(ValueError, match="bandwidth must be positive"):
        gaussian_kde([1.0, 2.0], [0.0], bandwidth)


def test_silverman_bandwidth_matches_rule_of_thumb() -> None:
    values = [1.0, 2.0, 3.0, 4.0, 5.0]
    # stdev = sqrt(2.5); IQR / 1.349 is larger, so the stdev is used.
    expected = 0.9 * math.sqrt(2.5) * 5 ** (-1 / 5)
    assert silverman_bandwidth(values) == pytest.approx(expected)


def test_silverman_bandwidth_falls_back_to_stdev_when_iqr_is_zero() -> None:
    assert silverman_bandwidth([1.0, 1.0, 1.0, 1.0, 9.0]) > 0


def test_silverman_bandwidth_rejects_constant_values() -> None:
    with pytest.raises(ValueError, match="must not all be equal"):
        silverman_bandwidth([3.0, 3.0, 3.0])


def test_silverman_bandwidth_rejects_fewer_than_two_values() -> None:
    with pytest.raises(ValueError, match="at least 2 values"):
        silverman_bandwidth([])
