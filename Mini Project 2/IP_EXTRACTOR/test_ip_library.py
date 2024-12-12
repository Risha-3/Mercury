import unittest
from ip_library import extract_ip, check_ip, filter_ip

# Test function for extract_ip
def test_extract_ip():
    text = "Valid IPs: 192.168.1.1, 10.0.0.1. Invalid IPs: 300.300.300.300, abc.def.ghi.jkl."
    expected = ['192.168.1.1', '10.0.0.1', '300.300.300.300']
    assert extract_ip(text) == expected, f"Expected {expected} but got {extract_ip(text)}"

# Test function for check_ip with valid IPs
def test_check_ip_valid():
    assert check_ip("192.168.1.1") == True, "Expected True for '192.168.1.1'"
    assert check_ip("10.0.0.1") == True, "Expected True for '10.0.0.1'"
    assert check_ip("255.255.255.255") == True, "Expected True for '255.255.255.255'"

# Test function for check_ip with invalid IPs
def test_check_ip_invalid():
    assert check_ip("300.300.300.300") == False, "Expected False for '300.300.300.300'"
    assert check_ip("10.0.0") == False, "Expected False for '10.0.0'"
    assert check_ip("abc.def.ghi.jkl") == False, "Expected False for 'abc.def.ghi.jkl'"

# Test function for filter_ip
def test_filter_ip():
    ip_list = ['192.168.1.1', '10.0.0.1', '300.300.300.300', 'invalid_ip']
    expected = ['192.168.1.1', '10.0.0.1']
    assert filter_ip(ip_list) == expected, f"Expected {expected} but got {filter_ip(ip_list)}"

# Running the tests
if __name__ == "__main__":
    test_extract_ip()
    test_check_ip_valid()
    test_check_ip_invalid()
    test_filter_ip()
    print("All tests passed!")
