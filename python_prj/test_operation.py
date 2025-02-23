import pytest
from operation import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(-2, 4) == -8

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

    with pytest.raises(ValueError):
        divide(5, 0)  # Should raise division by zero error
