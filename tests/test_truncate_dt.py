from datetime import datetime

import pytest

from cloack import truncate_dt


def test_unsupported_discretization():
    # https://docs.pytest.org/en/stable/reference/reference.html#pytest-raises
    with pytest.raises(
        ValueError,
        match="'hour' is not supported. Available discretizations: 'day', 'month', 'week'.",
    ):
        truncate_dt(datetime(2020, 10, 16, 17, 12, 33), "hour")
