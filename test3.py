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

        self.number1 = QLabel(self)
        self.number1.setText('Number 1: ')
        self.line = QLineEdit(self)
        self.line1 = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.number1.move(20, 20)

        self.number2 = QLabel(self)
        self.number2.setText('Number2: ')

        self.line1.move(80, 60)
        self.line1.resize(200, 32)
        self.number2.move(20, 60)

        pybutton = QPushButton('Calculate', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200, 32)
        pybutton.move(80, 100)

        self.answer = QLabel(self)
        # self.answer.setText('Answer')
        self.answer.move(20, 160)

    def clickMethod(self):
        self.a = int(self.line.text())
        self.b = int(self.line1.text())
        c = self.a+self.b
        print("Sum: "+str(c))
        self.answer.setText("Sum: "+str(c))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
