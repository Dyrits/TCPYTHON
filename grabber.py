#!/usr/bin/python3

from socket import socket , gethostbyname, gethostname, AF_INET, SOCK_STREAM

grabber_socket = socket(AF_INET, SOCK_STREAM)

def get_input():
    ip_addr = input("Please enter the IP address you want to grab: ")
    print("The IP you entered is: ", ip_addr)
    port = input("Please enter the port you want to grab: ")
    print("The port you entered is: ", port)
    return ip_addr, port

def banner_grabber(ip_addr, port):
    grabber_socket.connect((ip_addr, int(port)))
    grabber_socket.settimeout(2)
    return grabber_socket.recv(1024).decode().strip("b")

def main():
    print("Welcome to the banner grabber tool.")
    ip_addr, port = get_input()
    banner_grabber(ip_addr, port)

if __name__ == "__main__":
    main()