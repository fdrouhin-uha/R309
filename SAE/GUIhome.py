#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton,QTextBrowser,QDialog
from PyQt5.QtCore import QCoreApplication
from client import Client


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        self.__grid = QGridLayout()
        widget.setLayout(self.__grid)
        self.resize(300, 270)
        self.__lab = QLabel("host")
        self.__lab2 = QLabel("port")
        self.__text = QLineEdit("")
        self.__text2 = QLineEdit("")
        self.__conn = QPushButton("connexion")
        self.__quit = QPushButton("Exit")
        self.__grid.addWidget(self.__lab, 0, 0)
        self.__grid.addWidget(self.__lab2, 2, 0)
        self.__grid.addWidget(self.__text, 1, 0)
        self.__grid.addWidget(self.__text2, 3, 0)
        self.__grid.addWidget(self.__conn, 4, 0)
        self.__grid.addWidget(self.__quit, 5, 0)
        self.__conn.clicked.connect(self.actionConn)
        self.__quit.clicked.connect(self._actionQuitter)
        self.setWindowTitle("home")

    def actionConn(self):
        HOST = self.__text.text()
        p = self.__text2.text()
        PORT = int(p)
        conn = (HOST,PORT)
        diag = ChatWindow(HOST,PORT)
        diag.show()
        diag.exec()
        
    

    def _actionQuitter(self):
        QCoreApplication.exit(0)

class ChatWindow(QDialog):
    
    def __init__(self,HOST,PORT):
        super().__init__()
        self.__grid = QGridLayout()
        self.setLayout(self.__grid)
        self.resize(700, 400)
        self.setWindowTitle("monitoring")
        self.__text = QLineEdit("")
        self.__quit = QPushButton("Exit")
        self.__affi = QTextBrowser()
        self.__grid.addWidget(self.__text, 7, 0)
        self.__grid.addWidget(self.__quit, 0, 1)
        self.__grid.addWidget(self.__affi,0,0,6,1)
        #self.__quit.clicked.connect(self._actionQuitter)
        self.__text.returnPressed.connect(self._send)
        self.__client = Client(HOST,PORT,self.__affi)
    

    def _actionQuitter(self):
        msg = ':disconnect'
        self.__client.send(msg)
        QCoreApplication.exit(0)

    def _send(self):
        msg = self.__text.text()
        self.__client.send(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()