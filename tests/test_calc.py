import pytest
from src.calc import add, subtract, multiply, divide


def test_calc():
    assert add(5, 5) == 10
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
    assert add (0, 0) == 0


def test_subtract():
    assert subtract(10, 2) == 8
    assert subtract(-1, 1) == -2
    assert subtract(2, 1) == 1
    assert subtract(0,0) == 0


def test_multiply():
    assert multiply(5, 5) == 25
    assert multiply(8, 0) == 0
    assert multiply(-2,3,) == -6

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-6, -2) == 3
    with pytest.raises(ZeroDivisionError):
        divide(6, 0)
