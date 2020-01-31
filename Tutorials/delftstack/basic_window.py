import sys

from PySide2 import QtWidgets


class basicWindow(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.buttonA = QtWidgets.QPushButton(self)
        self.labelA = QtWidgets.QLabel(self)

        self.buttonA.setStyleSheet("background-color: red;font-size:18px;font-family:Times New Roman;")
        self.buttonA.clicked.connect(self.clickCallback)

        self.buttonA.setText('Click!')
        self.labelA.setText('Show Label')

        self.setWindowTitle('Push Button Example')

        self.buttonA.move(100, 50)
        self.labelA.move(110, 100)

        self.setGeometry(100, 100, 300, 200)

    def clickCallback(self):
        self.labelA.setText("Button is clicked")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windowExample = basicWindow()
    windowExample.show()
    sys.exit(app.exec_())
