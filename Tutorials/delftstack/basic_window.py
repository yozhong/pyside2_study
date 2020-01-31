import sys

from PySide2 import QtWidgets, QtGui, QtCore


def basicWindow():
    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()

    labelLeft = QtWidgets.QLabel(windowExample)
    labelRight = QtWidgets.QLabel(windowExample)
    labelCenter = QtWidgets.QLabel(windowExample)

    labelLeft.setText('Left Align')
    labelRight.setText('Right Align')
    labelCenter.setText('Center Align')

    windowExample.setWindowTitle('Label Align Example')
    windowExample.setGeometry(100, 100, 300, 200)

    labelLeft.setFixedWidth(160)
    labelRight.setFixedWidth(160)
    labelCenter.setFixedWidth(160)

    labelLeft.setStyleSheet("border-radius: 25px;border: 1px solid red;")
    labelRight.setStyleSheet("border-radius: 25px;border: 1px solid green;")
    labelCenter.setStyleSheet("border-radius: 25px;border: 1px solid blue;")

    labelLeft.setAlignment(QtCore.Qt.AlignLeft)
    labelRight.setAlignment(QtCore.Qt.AlignRight)
    labelCenter.setAlignment(QtCore.Qt.AlignCenter)

    labelLeft.move(80, 40)
    labelRight.move(80, 80)
    labelCenter.move(80, 120)

    windowExample.show()
    sys.exit(app.exec_())


basicWindow()
