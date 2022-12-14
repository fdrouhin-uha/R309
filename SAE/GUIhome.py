#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton,QTextBrowser,QDialog,QMessageBox
from PyQt5.QtCore import QCoreApplication,Qt
from PyQt5.QtGui import QCloseEvent
from client import Client


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        self.__grid = QGridLayout()
        widget.setLayout(self.__grid)
        self.resize(600, 300)
        self.__lab = QLabel("host")
        self.__lab2 = QLabel("port")
        #self.__lab3 = QLabel("login history")
        self.__text = QLineEdit("")
        self.__text2 = QLineEdit("")
        self.__conn = QPushButton("connexion")
        self.__affi = QTextBrowser()
        #self.__grid.addWidget(self.__lab3,0,0)
        #self.__grid.addWidget(self.__affi,1,0,5,1)
        self.__grid.addWidget(self.__lab, 0, 1)
        self.__grid.addWidget(self.__lab2, 2, 1)
        self.__grid.addWidget(self.__text, 1, 1)
        self.__grid.addWidget(self.__text2, 3, 1)
        self.__grid.addWidget(self.__conn, 4, 1)
        self.__conn.clicked.connect(self.actionConn)
        self.setWindowTitle("home")
        #self.f = open('history.txt','r')
        #self.f.read()

    def actionConn(self):
        HOST = self.__text.text()
        p = self.__text2.text()
        PORT = int(p)
        #self.f.write(f"{HOST} / {p}\n")
        diag = ChatWindow(HOST,PORT)
        diag.show()
        diag.exec()
   
    def closeEvent(self, _e: QCloseEvent): 
        box = QMessageBox()
        box.setWindowTitle("Quitter ?")
        box.setText("wanna quit ?")
        box.addButton(QMessageBox.Yes)
        box.addButton(QMessageBox.No)

        ret = box.exec()

        if ret == QMessageBox.Yes:
            QCoreApplication.exit(0)
        else:
            _e.ignore() 
    

   

class ChatWindow(QDialog):
    
    def __init__(self,HOST,PORT):
        super().__init__()
        self.__grid = QGridLayout()
        self.setLayout(self.__grid)
        self.resize(700, 400)
        self.setWindowTitle(f"{HOST}/{PORT}")
        self.__textCmd = QLineEdit("")
 #       self.__oofffff = QPushButton("DISCONNECT")
        self.__resetButton= QPushButton("RESET")
        self.__reset1Button= QPushButton("Disconnect")
        self.__killButton = QPushButton("KILL")
        self.__affi = QTextBrowser()
        self.__grid.addWidget(self.__textCmd, 7, 0)
        self.__grid.addWidget(self.__reset1Button, 0, 1)   #need to be fix 
        self.__grid.addWidget(self.__resetButton, 1, 1)  #need to be fix 
        self.__grid.addWidget(self.__killButton, 2, 1)   #need to be fix 
        self.__grid.addWidget(self.__affi,0,0,6,1)
        
        self.__resetButton.clicked.connect(self.__resetFD)  #need to be fix 
        self.__killButton.clicked.connect(self.__killFD)    #need to be fix 
        self.__textCmd.returnPressed.connect(self.__sendFD)
        self.__client = Client(HOST,PORT,self.__affi)

        self.__reset1Button.clicked.connect(self.__exitFD)
        self.__coucou = 1


    def __exitFD(self):
        if self.__coucou == 2:
            self.__coucou = 1
            return

        box = QMessageBox()
        
        box.setWindowTitle("Exit ?")
        box.setText("wanna log out ?")
        box.addButton(QMessageBox.Yes)
        box.addButton(QMessageBox.No)

        ret = box.exec()

        if ret == QMessageBox.Yes:
            self.__client.send(":disconnect")
            QDialog.exit(0)

    
    def __resetFD(self):
        box = QMessageBox()
        box.setWindowTitle("reset ?")
        box.setText("reset the server ?")
        box.addButton(QMessageBox.Yes)
        box.addButton(QMessageBox.No)

        ret = box.exec()

        if ret == QMessageBox.Yes:
            self.__client.send(":reset")
            QDialog.exit(0)
    
    def __killFD(self):
        box = QMessageBox()
        box.setWindowTitle("kill ?")
        box.setText("kill the server ?")
        box.addButton(QMessageBox.Yes)
        box.addButton(QMessageBox.No)

        ret = box.exec()

        if ret == QMessageBox.Yes:
            self.__client.send(":kill")
            QDialog.exit(0)


    def __sendFD(self):
        self.__coucou = 2
        msg = self.__textCmd.text()
        self.__client.send(msg)
        self.__affi.append(msg)
        self.__affi.setAlignment(Qt.AlignRight)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()