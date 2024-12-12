import ip_library

def main():
    # File paths (adjust these as needed)
    input_file = 'input_ip_list.txt'   # The file containing the list of IPs
    output_file = 'valid_ip_list.txt'  # The file where valid IPs will be saved

    # Step 1: Read IP addresses from a file
    ip_addresses = ip_library.read_ip(input_file)

    # Step 2: Filter the valid IPs
    valid_ips = ip_library.filter_ip(ip_addresses)

    # Step 3: Write the valid IPs to a new file
    ip_library.write_ip(valid_ips, output_file)

    print(f"Valid IPs have been written to {output_file}")

if __name__ == "__main__":
    main()

# cd "C:\Users\risha\Documents\Mercury repo\Mercury\Mini Project 2\IP_EXTRACTOR"
# python main.py
