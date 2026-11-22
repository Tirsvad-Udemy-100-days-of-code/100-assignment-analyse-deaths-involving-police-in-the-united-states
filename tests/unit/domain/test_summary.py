import dataclasses

import pytest

from fatal_force.domain.summary import FrameSummary


def _summary() -> FrameSummary:
    return FrameSummary("f", 3, 2, ("a", "b"), {"a": 1, "b": 2}, 0)


def test_null_total_sums_columns() -> None:
    assert _summary().null_total == 3


def test_summary_is_frozen() -> None:
    with pytest.raises(dataclasses.FrozenInstanceError):
        _summary().rows = 1  # type: ignore[misc]
