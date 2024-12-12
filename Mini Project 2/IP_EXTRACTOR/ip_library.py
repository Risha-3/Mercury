import re

ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

def extract_ip(text):
    return re.findall(ip_pattern, text)

def check_ip(ip):
    try:
        # Split the IP into octets and check the range
        octets = ip.split('.')
        return len(octets) == 4 and all(0 <= int(octet) <= 255 for octet in octets)
    except ValueError:
        # Handle cases where conversion to int fails
        return False

def filter_ip(ip_list):
    return [ip for ip in ip_list if check_ip(ip)]