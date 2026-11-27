import pytest

from calc.ops import add, div, sub


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(5, 3) == 2


def test_div():
    assert div(6, 3) == 2
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
