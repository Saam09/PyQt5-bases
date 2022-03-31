from re import A
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    
 
class MainWindow(QMainWindow):
    def __init__(self):
       
        QMainWindow.__init__(self)
 
        self.setMinimumSize(QSize(500, 500))    
        self.setWindowTitle("Adding two numbers")
 
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Number 1: ')
        self.line = QLineEdit(self)
        self.line1 = QLineEdit(self)
       
        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)
 
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Number2: ')
 
        self.line1.move(80, 60)
        self.line1.resize(200, 32)
        self.nameLabel.move(20, 60)
 
        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 100)        
 
    def clickMethod(self):
        self.a = self.line.text()
        self.b = self.line1.text()
        c=self.a+self.b
        print(c)
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
 

