#!/usr/bin/python3

from socket import socket, gethostbyname, gethostname, AF_INET, SOCK_STREAM

client_socket = socket(AF_INET, SOCK_STREAM)

host = gethostbyname(gethostname())

port = 4500

client_socket.connect((host, port))

message = client_socket.recv(1024)

client_socket.close()

print(message.decode())