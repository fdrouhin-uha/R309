import socket
import sys
import threading
from PyQt5.QtWidgets import QTextBrowser
from PyQt5.QtCore import Qt
class Client:

    def __init__(self, host: str, port: int,affi: QTextBrowser) -> None:
        self.client = socket.socket()
        self.data = ""
        self.addr = (host, port)
        self.__connexion()
        self.__affi = affi

    def __connexion(self):
        self.client.connect(self.addr)
        client_condi = threading.Thread(target=self.condi)
        client_condi.start()

    def condi(self):
        try:
            while self.data != "deco-server":
                self.data = self.client.recv(1024).decode()
                self.__affi.append(self.data)
                self.__affi.setAlignment(Qt.AlignLeft)
        except:
            self.client.send("deco-server".encode())
            self.client.close()

    def send(self,msg):
        self.client.send(msg.encode())
    
    def close(self):
        self.client.close()