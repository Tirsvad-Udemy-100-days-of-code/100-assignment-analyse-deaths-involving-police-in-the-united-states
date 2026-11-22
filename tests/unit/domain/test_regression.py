import pytest

from fatal_force.domain.regression import fit_line


def test_fit_line_returns_slope_intercept_and_r_for_perfect_line() -> None:
    fit = fit_line([0.0, 1.0, 2.0], [1.0, 3.0, 5.0])
    assert (fit.slope, fit.intercept) == (2.0, 1.0)
    assert fit.r_value == pytest.approx(1.0)


def test_fit_line_gives_negative_r_for_falling_line() -> None:
    assert fit_line([0.0, 1.0, 2.0], [4.0, 2.0, 0.0]).r_value == pytest.approx(-1.0)


def test_fit_line_rejects_fewer_than_two_points() -> None:
    with pytest.raises(ValueError, match="at least 2 points"):
        fit_line([1.0], [1.0])


def test_fit_line_rejects_different_lengths() -> None:
    with pytest.raises(ValueError, match="same length"):
        fit_line([1.0, 2.0], [1.0])
