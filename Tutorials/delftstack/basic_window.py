import sys

from PySide2 import QtWidgets


class basicWindow(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.buttonA = QtWidgets.QPushButton('Click!')
        self.labelA = QtWidgets.QLabel('Show Label')

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.labelA)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buttonA)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.buttonA.setStyleSheet("background-color: red;font-size:18px;font-family:Times New Roman;")
        self.buttonA.clicked.connect(self.clickCallback)

        self.setWindowTitle('Box Layout Example')
        self.setGeometry(100, 100, 300, 200)

    def clickCallback(self):
        self.labelA.setText("Button is clicked")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windowExample = basicWindow()
    windowExample.show()
    sys.exit(app.exec_())
