#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout,QLineEdit, QPushButton,QTextBrowser
from PyQt5.QtCore import QCoreApplication
from client import Client
from GUIhome import MainWindow

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
        self.__quit = QPushButton("Exit")
        self.__affi = QTextBrowser()
        self.__grid.addWidget(self.__text, 7, 0)
        self.__grid.addWidget(self.__quit, 0, 1)
        self.__grid.addWidget(self.__affi,0,0,6,1)
        self.__quit.clicked.connect(self._actionQuitter)
        self.__text.returnPressed.connect(self._send)
        self.__client = Client(MainWindow.actionConn,self.__affi)
    
    def _actionQuitter(self):
        msg = ':disconnect'
        self.__client.send(msg)
        QCoreApplication.exit(0)

    def _send(self):
        msg = self.__text.text()
        self.__client.send(msg)
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    app.exec()
    