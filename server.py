#!/usr/bin/python3

from socket import socket, gethostbyname, gethostname, AF_INET, SOCK_STREAM

server_socket = socket(AF_INET, SOCK_STREAM)

host = gethostbyname(gethostname())

port = 4500

server_socket.bind((host, port))

server_socket.listen(5)

while True:
    client_socket, address = server_socket.accept()
    print(f"Got a connection from {str(address)}")
    client_socket.send("You established a connection to the server.".encode())
    client_socket.close()