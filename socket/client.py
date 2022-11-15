#!/usr/bin/env python3
import socket
import sys
try :
    host="127.0.0.1"
    port = int(sys.argv[1])
    client_socket = socket.socket()
    client_socket.connect((host, port))
    data=''
    try:
        while data != 'bye' and data !='arret' :
            message = input('votre message: ')
            client_socket.send(message.encode())
            data = client_socket.recv(1024).decode()
            print(data)
        client_socket.close()
    except ConnectionResetError:
        client_socket.close()
except socket.gaierror:
    print("le nom de l'hote est invalide")
except TimeoutError:
    print("time out")
    client_socket.close()
except BrokenPipeError:
    print("connexion perdue")
    client_socket.close()
