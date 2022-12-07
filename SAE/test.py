import sys 
import threading
from guiChat import ChatWindow
from GUIhome import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication

def home():
    app = QApplication(sys.argv)
    win1= MainWindow()
    win1.show()
    app.exec()
    monitor = threading.Thread(target=open)
    monitor.start()
def open():
    win = ChatWindow()
    win.show()
home()