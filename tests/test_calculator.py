# tests/test_calculator.py
import pytest
from calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_subtract():
    assert calc.subtract(10, 4) == 6

def test_multiply():
    assert calc.multiply(3, 4) == 12

def test_divide():
    assert calc.divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError, match='Nolga bolish mumkin emas'):
        calc.divide(5, 0)
