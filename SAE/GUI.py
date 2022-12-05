#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import QCoreApplication
from client import Client

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        self.__grid = QGridLayout()
        widget.setLayout(self.__grid)
        self.__lab = QLabel("host")
        self.__lab2 = QLabel("port")
        self.__text = QLineEdit("")
        self.__text2 = QLineEdit("")
        self.__conn = QPushButton("connexion")
        self.__quit = QPushButton("Quitter")
        self.__grid.addWidget(self.__lab, 0, 0)
        self.__grid.addWidget(self.__lab2, 2, 0)
        self.__grid.addWidget(self.__text, 1, 0)
        self.__grid.addWidget(self.__text2, 3, 0)
        self.__grid.addWidget(self.__ok, 4, 0)
        self.__grid.addWidget(self.__quit, 5, 0)
        self.__conn.clicked.connect(self._actionConn)
        self.__quit.clicked.connect(self._actionQuitter)
        self.setWindowTitle("home")

    def _actionConn(self):
        Client(self.__text,self.__text2)
        


    def _actionQuitter(self):
        QCoreApplication.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()