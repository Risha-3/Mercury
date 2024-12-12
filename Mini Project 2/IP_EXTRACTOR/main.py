import ip_library

def main():
    input_file = 'input_ip_list.txt'   # The file containing the list of IP addresses that the user has written.
    output_file = 'valid_ip_list.txt'  # The file where valid IPs will be saved.

    # Reading the IP addresses from the input text file.
    ip_addresses = ip_library.read_ip(input_file)

    # Filtering the valid IP addresses.
    valid_ips = ip_library.filter_ip(ip_addresses)

    # Writing the valid IP addresses to the valid text file.
    ip_library.write_ip(valid_ips, output_file)

    print(f"Valid IPs have been written to {output_file}")

if __name__ == "__main__":
    main()

# cd "C:\Users\risha\Documents\Mercury repo\Mercury\Mini Project 2\IP_EXTRACTOR"
# python main.py
