#!/usr/bin/env python3
import socket
import sys

host= "127.0.0.1"
port = int(sys.argv[1])
server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)
conn, address = server_socket.accept()
data = conn.recv(1024).decode()
print(data)
while data != 'bye' and data != 'arret':
    data = conn.recv(1024).decode()
    conn.send(data.encode())
    print (data)
if data == 'bye':
    conn.send(data.encode())
    server_socket.listen(1)
    conn, address = server_socket.accept()
else:
    conn.send(data.encode())
    conn.close()


'''server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)
conn, address = server_socket.accept()
data = conn.recv(1024).decode()
conn.send(reply.encode())
conn.close()'''