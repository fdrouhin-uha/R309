#!/usr/bin/env python3
import socket
import sys
if __name__ == '__main__':
    try :
        host="127.0.0.1"
        port = int(sys.argv[1])
        client_socket = socket.socket()
        client_socket.connect((host, port))
        data=''
        message=''
        try:
            while message != 'disconnect' and message !='kill' and message !='reset' :
                message = input('votre message: ')
                client_socket.send(message.encode())
                data = client_socket.recv(1024).decode()
                print(data)

        except ConnectionResetError:
            print("perte de connexion")
        except TimeoutError:
            print("time out")
        except BrokenPipeError:
            print("connexion perdue")
        except KeyboardInterrupt:
            print("Interruption clavier : ^C")
        finally:
            client_socket.send("disconnect".encode())
            client_socket.close()
    except PermissionError:
        print ("le port n'est pas bon")
    except socket.gaierror:
        print("le nom de l'hote est invalide")