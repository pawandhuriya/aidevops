import pytest
from app.calculator import divide_numbers

def test_valid_division():
    assert divide_numbers(10, 2) == 5

def test_divide_by_zero():
    assert divide_numbers(10, 0) is None

def test_invalid_input():
    assert divide_numbers(10, "a") is None