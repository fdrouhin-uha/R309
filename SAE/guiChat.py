#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import QCoreApplication
from client import Client


class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        self.__grid = QGridLayout()
        widget.setLayout(self.__grid)
        self.resize(700, 400)
        self.setWindowTitle("monitoring")
        self.__text = QLineEdit("")
        self.__lab = QLabel("")
        self.__lab2 = QLabel("")
        self.__lab3 = QLabel("")
        self.__lab4 = QLabel("")
        self.__send = QPushButton("send")
        self.__quit = QPushButton("Exit")
        self.__grid.addWidget(self.__text, 7, 0)
        self.__grid.addWidget(self.__send, 7, 1)
        self.__grid.addWidget(self.__quit, 0, 1)
        self.__grid.addWidget(self.__lab, 0, 0)
        self.__grid.addWidget(self.__lab2, 1, 0)
        self.__grid.addWidget(self.__lab3, 2, 0)
        self.__grid.addWidget(self.__lab4, 3, 0)
        self.__quit.clicked.connect(self._actionQuitter)
        self.__send.clicked.connect(self._send)
        self.__client = Client("127.0.0.1",10000)
    
    def _actionQuitter(self):
        msg = ':disconnect'
        self.__client.send(msg)
        QCoreApplication.exit(0)

    def _send(self):
        msg = self.__text.text()
        self.__client.send(msg)
        recv = self.__client.__condi()
        self.__lab3.setText(msg)
        self.__lab4.setText(recv)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    app.exec()
    