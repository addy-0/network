import socket
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup


def domain_to_ip():
    domain_name = input("Enter the domain name: ")
    ip_address = socket.gethostbyname(domain_name)
    print("The IP address of", domain_name, "is", ip_address)


def reverse_ip_lookup():
    ip_address = input("Enter the IP address: ")
    reverse_dns = socket.gethostbyaddr(ip_address)
    print("The reverse DNS lookup of", ip_address, "is", reverse_dns[0])


def subdomain_enumeration():
    domain_name = input("Enter the domain name: ")
    ip_address = socket.gethostbyname(domain_name)
    subdomains = []
    for i in range(1, 10):
        subdomain = f"{i}.{domain_name}"
        try:
            socket.gethostbyname(subdomain)
            subdomains.append(subdomain)
        except socket.error:
            pass
    print("The following subdomains were found:")
    for subdomain in subdomains:
        print(subdomain)


def get_website_info():
    url = input("Enter the website URL: ")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("title").get_text()
    meta_desc = ""
    for tag in soup.find_all("meta"):
        if "name" in tag.attrs and tag.attrs["name"].lower() == "description":
            meta_desc = tag.attrs["content"]
            break
    status_code = response.status_code
    ip_address = socket.gethostbyname(urlparse(url).hostname)
    print("Title:", title)
    print("Meta description:", meta_desc)
    print("HTTP status code:", status_code)
    print("IP address:", ip_address)


def help():
    print("This program includes the following functions:")
    print("1. domain_to_ip() - converts a domain name to an IP address")
    print("2. reverse_ip_lookup() - performs a reverse DNS lookup on an IP address")
    print("3. subdomain_enumeration() - enumerates subdomains for a given domain")
    print("4. get_website_info() - retrieves basic information about a website given its URL")


def main():
    while True:
        help()
        option = input("Enter the option number, or enter 'q' to quit: ")

        if option == "1":
            domain_to_ip()
        elif option == "2":
            reverse_ip_lookup()
        elif option == "3":
            subdomain_enumeration()
        elif option == "4":
            get_website_info()
        elif option.lower() == "q":
            break
        else:
            print("Invalid option")


if __name__ == '__main__':
    main()
