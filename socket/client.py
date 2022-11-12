#!/usr/bin/env python3
import socket
import sys

host="127.0.0.1"
port = int(sys.argv[1])
message= 'test'

client_socket = socket.socket()
client_socket.connect((host, port))
client_socket.send(message.encode())
data = client_socket.recv(1024).decode()
print(data)
client_socket.close()