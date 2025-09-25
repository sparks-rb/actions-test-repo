
import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5
    assert pytest.approx(divide(1, 3), rel=1e-6) == 1/3

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
