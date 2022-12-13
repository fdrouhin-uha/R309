#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton,QTextBrowser,QDialog,QMessageBox
from PyQt5.QtCore import QCoreApplication, Qt
from client import Client
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        self.__grid = QGridLayout()
        widget.setLayout(self.__grid)
        #self.resize(600, 300)
        self.__lab = QLabel("host")
        self.__lab2 = QLabel("port")
        self.__text = QLineEdit("")
        self.__text2 = QLineEdit("")
        self.__conn = QPushButton("connexion")
        self.__affi = QTextBrowser()
        self.__text3 = QLineEdit("")
        self.__lab4 = QLabel("message:")
        self.__send = QPushButton("Envoyer")
        self.__effa = QPushButton("Effacer")
        self.__quit = QPushButton("Quiter")
        self.__grid.addWidget(self.__lab, 0,0)
        self.__grid.addWidget(self.__lab2, 1, 0)
        self.__grid.addWidget(self.__text, 0, 1)
        self.__grid.addWidget(self.__text2, 1, 1)
        self.__grid.addWidget(self.__conn, 2, 0,1,2)
        self.__grid.addWidget(self.__affi,3,0,6,2)
        self.__grid.addWidget(self.__text3, 9,1)
        self.__grid.addWidget(self.__lab4, 9,0)
        self.__grid.addWidget(self.__send, 10, 0,1,2)
        self.__grid.addWidget(self.__effa, 11, 0,1,1)
        self.__grid.addWidget(self.__quit, 11, 1,1,1)
        self.__text3.setEnabled(False)
        self.__send.setEnabled(False)
        self.__conn.clicked.connect(self.actionConn)
        self.__send.clicked.connect(self._send)
        self.__effa.clicked.connect(self._effacer)
        self.__quit.clicked.connect(self._quit)
    
    def actionConn(self):
        HOST = self.__text.text()
        p = self.__text2.text()
        PORT = int(p)
        self.__client = Client(HOST,PORT,self.__affi)
        self.__text3.setEnabled(True)
        self.__send.setEnabled(True)
        self.__conn = QPushButton("Deconnexion")


    def _send(self):
        msg = self.__text3.text()
        self.__affi.append(msg)
        self.__affi.setAlignment(Qt.AlignRight)
        self.__client.send(msg)
    
    
    def _effacer(self):
        self.__text3 = QLineEdit("")

    def _quit(self):
        self.__client.send("deco-server")
        QCoreApplication.exit(0)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()