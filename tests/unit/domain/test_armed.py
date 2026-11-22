import pytest

from fatal_force.domain.armed import ArmedShares


def test_armed_shares_percentages_add_up() -> None:
    shares = ArmedShares(total=10, armed=6, unarmed=3, unknown=1)
    assert shares.armed_percent == pytest.approx(60.0)
    assert shares.unarmed_percent == pytest.approx(30.0)
    assert shares.unknown_percent == pytest.approx(10.0)


def test_armed_shares_percentages_are_zero_without_victims() -> None:
    shares = ArmedShares(total=0, armed=0, unarmed=0, unknown=0)
    assert shares.armed_percent == 0.0
