#!/usr/bin/env python3
import socket
import sys
import threading
HOST = "127.0.0.1"


class Client:

    def __init__(self, host: str, port: int) -> None:
        self.client = socket.socket()
        self.data = ""
        self.addr = (host, port)
        self.__connexion()

    def __connexion(self):
        self.client.connect(self.addr)
        client_condi = threading.Thread(
            target=self.__condi, args=[self.client])
        client_condi.start()

    def __condi(self, conn):
        while self.data != 'disconnect' and self.data != 'kill':
            self.data = self.client.recv(1024).decode()
            print(self.data)

    def send(self, msg):
        self.client.send(msg.encode())


if __name__ == "__main__":
    test =  Client(HOST, int(sys.argv[1]))
    msg=''
    while msg != 'disconnect' and msg != 'kill':
        msg = input('commande: ')
        test.send(msg)