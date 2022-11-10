import socket
import sys
host= "172.0.0.1"
port = int(sys.argv[1])
server_socket = socket.socket()
server_socket.bind(host, port)
server_socket.listen(1)
conn, address = server_socket.accept()
data = conn.recv(1024).decode()
conn.send(reply.encode())
conn.close()