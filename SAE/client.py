#!/usr/bin/env python3
import socket
import sys
import threading
HOST = "127.0.0.1"


class Client:

    def __init__(self, host: str, port: str) -> None:
        self.client = socket.socket()
        self.data = ""
        self.addr = (host, port)
        self.__connexion()

    def __connexion(self):
        self.client.connect(self.addr)
        client_condi = threading.Thread(target=self.__condi)
        client_condi.start()

    def __condi(self):
        try:
            while self.data != ':disconnect' and self.data != ':kill':
                self.data = self.client.recv(1024).decode()
                print(f'{self.data}')
        except ConnectionResetError:
            print("perte de connexion")
        except TimeoutError:
            print("time out")
        except BrokenPipeError:
            print("connexion perdue")
        except KeyboardInterrupt:
            print("Interruption clavier : ^C")
        finally:
            self.client.close()
    
    def send(self, msg):
        self.client.send(msg.encode())

    def close(self):
        self.client.close()

if __name__ == "__main__":
    test = Client(HOST, int(sys.argv[1]))
    msg = ''
    while msg != ':disconnect' and msg != ':kill':
        print('commande : ')
        msg = input()
        test.send(msg)
    test.close()