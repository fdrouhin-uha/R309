#!/usr/bin/env python3
import socket
import sys

host= "127.0.0.1"
port = int(sys.argv[1])

if __name__ == '__main__':
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    data = conn.recv(1024).decode()
    while data != 'arret':
        conn.send(data.encode())
        server_socket.listen(1)
        conn = server_socket.accept()
        data = conn.recv(1024).decode()
    else:
        conn.close()


'''server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)
conn, address = server_socket.accept()
data = conn.recv(1024).decode()
conn.send(reply.encode())
conn.close()'''