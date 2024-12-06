#!/usr/bin/python3

from nmap import PortScanner

scanner = PortScanner()

print("Welcome, this is a simple nmap automation tool.")
print("<<<--->>>")
ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

print("Please enter the type of scan you want to run :")
print("1) SYN ACK Scan")
print("2) UDP Scan")
print("3) Comprehensive Scan")
scan_type = input("Your choice: ")
while scan_type not in ["1", "2", "3"]:
    print("Please enter a valid option!")
    scan_type = input("Your valid choice: ")

print("Nmap Version: ", scanner.nmap_version())

def run_scan(ip_addr, scan_type, arguments):
    scanner.scan(ip_addr, arguments=arguments)
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    protocols = ["tcp", "udp"] if scan_type == "3" else ["tcp" if scan_type == "1" else "udp"]
    for protocol in protocols:
        if protocol in scanner[ip_addr]:
            print(f"Open {protocol.upper()} Ports: ", scanner[ip_addr][protocol].keys())
        else:
            print(f"No open {protocol.upper()} ports found.")

if scan_type == "1":
    run_scan(ip_addr, scan_type, "-v -sS -F")
elif scan_type == "2":
    run_scan(ip_addr, scan_type, "-v -sU -F")
else:
    run_scan(ip_addr, scan_type, "-v -sS -sV -sC -A -O")