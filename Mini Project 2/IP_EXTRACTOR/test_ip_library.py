import pytest
# Importing the required functions from the ip_library.
from ip_library import extract_ip, check_ip, filter_ip

def test_extract_ip():
    """
    Tests whether the appropriate IP address is being extracted through the extract_ip function.
    """
    text = "Valid IPs: 192.168.1.1, 10.0.0.1. Invalid IPs: 300.300.300.300, abc.def.ghi.jkl."
    expected = ['192.168.1.1', '10.0.0.1', '300.300.300.300']
    result = extract_ip(text)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_check_ip_valid():
    """
    Tests the check_ip function using only valid IP addresses.
    """
    assert check_ip("192.168.1.1") == True, "Expected True for '192.168.1.1'"
    assert check_ip("10.0.0.1") == True, "Expected True for '10.0.0.1'"
    assert check_ip("255.255.255.255") == True, "Expected True for '255.255.255.255'"

def test_check_ip_invalid():
    """
    Tests the check_ip function using only invalid IP addresses.
    """
    assert check_ip("300.300.300.300") == False, "Expected False for '300.300.300.300'"
    assert check_ip("10.0.0") == False, "Expected False for '10.0.0'"
    assert check_ip("abc.def.ghi.jkl") == False, "Expected False for 'abc.def.ghi.jkl'"

def test_filter_ip():
    """
    Tests whether the appropriate IP addresses are filtered out from the list through the filter_ip function.
    """
    ip_list = ['192.168.1.1', '10.0.0.1', '300.300.300.300', 'invalid_ip']
    expected = ['192.168.1.1', '10.0.0.1']
    result = filter_ip(ip_list)
    assert result == expected, f"Expected {expected}, but got {result}"

# cd "C:\Users\risha\Documents\Mercury repo\Mercury\Mini Project 2\IP_EXTRACTOR"
# python -m pytest test_ip_library.py
