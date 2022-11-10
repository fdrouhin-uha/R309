import socket
import sys

host="172.0.0.1"
port = int(sys.argv[1])
message= 'test'
client_socket = socket.socket()
client_socket.connect(host, port)
client_socket.send(message.encode())
data =
client_socket.recv(1024).decode()
client_socket.close()