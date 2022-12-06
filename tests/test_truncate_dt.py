from datetime import datetime

import pytest

from cloack import truncate_dt


def test_unsupported_discretization():
    # https://docs.pytest.org/en/stable/reference/reference.html#pytest-raises
    with pytest.raises(
        ValueError,
        match="'hour' is not supported. Available discretizations: 'day', 'month', 'week'.",
    ):
        truncate_dt(datetime(2022, 12, 6, 9, 52, 45), "hour")


@pytest.mark.parametrize(
    "dt,discretization,expected",
    [
        (datetime(2022, 12, 6, 9, 52, 45), "day", datetime(2022, 12, 6)),
        (datetime(2022, 12, 6, 9, 52, 45), "week", datetime(2022, 12, 5)),
        (datetime(2022, 12, 6, 9, 52, 45), "month", datetime(2022, 12, 1)),
    ],
)
def test_function(dt, discretization, expected):
    assert truncate_dt(dt, discretization) == expected
