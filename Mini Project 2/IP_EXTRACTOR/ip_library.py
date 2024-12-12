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

def read_ip(file_path):
    with open(file_path, 'r') as file:
        # Read lines from the file and strip any leading/trailing whitespace
        return [line.strip() for line in file.readlines()]

def write_ip(valid_ips, output_file_path):
    """Writes valid IPs to a new text file."""
    with open(output_file_path, 'w') as file:
        for ip in valid_ips:
            file.write(f"{ip}\n")