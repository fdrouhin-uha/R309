#!/usr/bin/env python3
import socket
import sys
if __name__ == '__main__':
    try:
        host= "127.0.0.1"
        port = int(sys.argv[1])
        server_socket = socket.socket()
        server_socket.bind((host, port))
        server_socket.listen(1)
        data=''
        while data != 'arret':
            print("Je suis en attente")
            try:
                conn, address = server_socket.accept()
                print("Je suis connecté")
                data = ''
                while data != 'bye' and data !='arret':
                    data = conn.recv(1024).decode()
                    conn.send(data.encode())
                    print (f"E/R: {data}")
            except ConnectionResetError:
                print("perte de connexion")
            except TimeoutError:
                print("time out")
            except BrokenPipeError:
                print("connexion perdue")
            finally:
                conn.close()
    except PermissionError:
        print ("le port n'est pas bon")
    finally:
        server_socket.close() 



'''server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)
conn, address = server_socket.accept()
data = conn.recv(1024).decode()
conn.send(reply.encode())
conn.close()'''