#!/usr/bin/env python3

# Examen NE PAS CHANGER !!!!!

import socket
import sys
if __name__ == '__main__':
    try:
        host= "127.0.0.1"
        port = 10000
        server_socket = socket.socket()
        server_socket.bind((host, port))
        server_socket.listen(1)
        data=''
        while data != 'bye':
            print("Serveur> Je suis en attente")
            try:
                conn, address = server_socket.accept()
                print(f"Serveur> Je suis connecté avec le client {address}")
                data = ''
                while data != 'bye':
                    data = conn.recv(1024).decode()
                    print (f"{data}")
            except ConnectionResetError:
                print("Serveur> Erreur : perte de connexion")
            except TimeoutError:
                print("Serveur> Erreur : time out")
            except BrokenPipeError:
                print("Serveur> Erreur : connexion perdue")
            finally:
                conn.close()
    except PermissionError:
        print ("le port n'est pas bon")
    finally:
        server_socket.close() 
