import pytest
from fuel import convert, gauge

def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("5/10") == 50
    assert convert("3/4") == 75

def test_convert_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_numerator_greater_than_denominator():
    with pytest.raises(ValueError):
        convert("5/4")

def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("x/y")
    with pytest.raises(ValueError):
        convert("3/xyz")

# Test case for gauge function
def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_percent():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"