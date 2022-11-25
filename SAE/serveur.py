#!/usr/bin/env python3
import sys, socket, subprocess, threading
# info of the server
host= ''
port= int(sys.argv[1])

#uping the server
server_s= socket.socket()
server_s.bind((host, port))
server_s.listen()
data=''
if __name__ == '__main__':
    try:
        while data != 'arret':
            print("Je suis en attente")
            try:
                conn, address = server_s.accept()
                print("Je suis connecté")
                data = ''
                while data != 'bye' and data !='arret':
                    data = conn.recv(1024).decode()
                    p = subprocess.Popen(data, stdout=subprocess.PIPE, shell=True)
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
        server_s.close()