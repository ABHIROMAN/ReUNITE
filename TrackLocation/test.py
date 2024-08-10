import requests
import socket
import whois
import dns.resolver
import sublist3r

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

def get_whois_info(domain):
    try:
        whois_info = whois.whois(domain)
        return whois_info
    except whois.parser.PywhoisError:
        return None

def get_dns_records(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        return [ip.address for ip in result]
    except dns.resolver.NXDOMAIN:
        return None

def get_subdomains(domain):
    try:
        subdomains = sublist3r.main(domain, 20, 'domain.txt',ports= None,silent= False,
                                    verbose= False, enable_bruteforce= False, engines=None)
        return subdomains
    except Exception as e:
        print(f"Error retrieving subdomains: {e}")
        return None


def main():
    website = input("Enter the website domain: ")

    # Basic Information
    ip_address = get_ip_address(website)
    print(f"IP Address: {ip_address}")

    whois_info = get_whois_info(website)
    if whois_info:
        print("Whois Information:")
        print(whois_info)

    # DNS Information
    dns_records = get_dns_records(website)
    if dns_records:
        print("DNS Records:")
        for record in dns_records:
            print(record)
    else:
        print("No DNS records found.")

    # Subdomains
    subdomains = get_subdomains(website)
    if subdomains:
        print("Subdomains:")
        for subdomain in subdomains:
            print(subdomain)
    else:
        print("No subdomains found.")

if __name__ == "__main__":
    main()
