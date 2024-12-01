import pytest
from fuel import convert, gauge

# The four test cases for the convert function are below.
# Function to test for valid fractions.
def test_convert_normal():
    assert convert("5/10") == 50
    assert convert("0/1") == 0

# Function to test for when Y in X/Y is zero.
def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("10/0")

# Function to test for when X in X/Y is greater than Y.
def test_convert_improper_fraction():
    with pytest.raises(ValueError):
        convert("10/9")

# Function to test for cases when X or Y in X/Y is not an integer.
def test_convert_non_integer():
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("5.5/10")

# The three test cases for the gauge function are below.
# Function to test whether "E" is returned for 0% and 1%.
def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

# Function to test the mid-range percentages.
def test_gauge_percent():
    assert gauge(50) == "50%"

# Function to test whether "F" is returned for 99% and 100%.
def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

# cd "C:\Users\risha\Documents\Mercury repo\Mercury\Assignment 4 TEST"
# python -m pytest test_fuel.py
