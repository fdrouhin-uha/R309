import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QComboBox
from PyQt5.QtCore import QCoreApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        self.__grid = QGridLayout()
        widget.setLayout(self.__grid)
        self.__lab1 = QLabel("Température")
        self.__text1 = QLineEdit("")
        self.__lab2 = QLabel("°C")
        self.__conv = QPushButton("Convertir")
        self.__lab6 = QLabel("")
        self.__selec = QComboBox()
        self.__lab3 = QLabel("Conversion")
        self.__lab4 = QLabel("")
        self.__lab5 = QLabel("K")
        self.__selec.addItem("°C -> K")
        self.__selec.addItem("K -> °C")
        self.__grid.addWidget(self.__lab1, 0, 0)
        self.__grid.addWidget(self.__text1, 0, 1)
        self.__grid.addWidget(self.__lab2, 0, 2)
        self.__grid.addWidget(self.__lab6, 1, 0)
        self.__grid.addWidget(self.__conv, 1, 1)
        self.__grid.addWidget(self.__selec, 1, 2)
        self.__grid.addWidget(self.__lab3, 2, 0)
        self.__grid.addWidget(self.__lab4, 2, 1)
        self.__grid.addWidget(self.__lab5, 2, 2)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()