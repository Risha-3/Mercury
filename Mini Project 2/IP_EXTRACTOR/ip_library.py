import re

ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

def extract_ip(text):
    """
    This function extracts all of the IP addresses from the text file using the ip_pattern.
    It then returns a list of valid Ip addresses that were found in the text.
    """
    return re.findall(ip_pattern, text)

def check_ip(ip):
    """
    A valid IP address consists of 4 parts in the range of 0-255.
    This function checks if the given IP address is valid. 
    """
    try:
        # Split the IP into parts and checks if each part is inbetween 0 and 255.
        parts = ip.split('.')
        return len(parts) == 4 and all(0 <= int(part) <= 255 for part in parts)
    except ValueError:
        # If the value is a non-numerical, it cannot be converted to an integer so false is returned.
        return False

def filter_ip(ip_list):
    """
    This function filters a list of IP addresses, keeping only the valid ones.
    It then returns a new list containing only the valid IP addresses.
    """
    return [ip for ip in ip_list if check_ip(ip)]

def read_ip(file_path):
    """
    This function reads from a text file and returns a list of strings where each string is an IP address read from the file.
    """
    with open(file_path, 'r') as file:
        # Read lines from the file and strip any whitespaces.
        return [line.strip() for line in file.readlines()]

def write_ip(valid_ips, output_file_path):
    """
    This function writes a list of valid IP addresses to the valid_ip_list text file.
    """
    with open(output_file_path, 'w') as file:
        for ip in valid_ips:
            file.write(f"{ip}\n")
