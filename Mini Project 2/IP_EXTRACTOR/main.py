from ip_library import extract_ip, filter_ip

def main():
    # Input text with potential IPs
    text = input("Enter text containing IP addresses: ")

    # Extract IPs using the library
    extracted_ips = extract_ip(text)
    print("\nExtracted IP Addresses:")
    print(extracted_ips)

    # Filter valid IPs using the library
    valid_ips = filter_ip(extracted_ips)
    print("\nValid IP Addresses:")
    print(valid_ips)

if __name__ == "__main__":
    main()

# cd "C:\Users\risha\Documents\Mercury repo\Mercury\Mini Project 2"
# python "C:\Users\risha\Documents\Mercury repo\Mercury\Mini Project 2\main.py"
