#!/usr/bin/env python3
import sys
import os
import nmap
import requests
import re
from datetime import datetime as dt

ip_regex = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

class Colors:
    HEADER = '\033[95m'
    IMPORTANT = '\033[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    LOGGING = '\033[34m'

def print_menu():
    print(Colors.NOTICE + '''
        ╔======================================================================================================╗
        ║                                                                                                      ║
        ║             Penetration Testing Tool Suite                                                           ║
        ║             © LPP                                                                                    ║
        ╚======================================================================================================╝
    ''' + Colors.END)

def require_root():
    if os.geteuid() != 0:
        print(Colors.RED + "Root privileges are required to run this program." + Colors.END)
        sys.exit(1)

def run_nmap_scan():
    scanner = nmap.PortScanner()
    host = input("Enter IP address or hostname: ")
    if not re.match(ip_regex, host):
        print(Colors.RED + "Invalid IP address format." + Colors.END)
        return
    scanner.scan(host, '1-65535', '-v -sS -sV -sC -A -O')
    for host in scanner.all_hosts():
        print('Host: %s(%s)' % (host, scanner[host].hostname()))
        print('State: %s' % scanner[host].state())
        for proto in scanner[host].all_protocols():
            print('Protocol: %s' % proto)
            for port in sorted(scanner[host][proto]):
                print('port: %s\tstate: %s' % (port, scanner[host][proto][port]['state']))

def find_hidden_urls():
    host = input("Enter host URL (without 'http://'): ")
    try:
        requests.get("http://" + host)
    except requests.exceptions.ConnectionError:
        print(Colors.RED + "Could not connect to the host." + Colors.END)
        return

    with open('dir_list.txt', 'r') as file:
        for directory in file:
            url = f"http://{host}/{directory.strip()}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(Colors.OKGREEN + f"Found URL: {url}" + Colors.END)
            except requests.exceptions.RequestException:
                continue

def main():
    while True:
        print_menu()
        print("""
            1. IP Full Analysis
            2. Find Hidden URLs
            3. Exit
        """)
        choice = input("Select an option: ")
        if choice == '1':
            require_root()
            run_nmap_scan()
        elif choice == '2':
            find_hidden_urls()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print(Colors.WARNING + "Invalid selection, please choose again." + Colors.END)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram exited.")


