import sys

from PySide2 import QtWidgets, QtGui


def basicWindow():
    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()
    labelA = QtWidgets.QLabel(windowExample)
    labelB = QtWidgets.QLabel(windowExample)
    labelA.setText('Label Example')
    labelB.setPixmap(QtGui.QPixmap('python.png'))
    windowExample.setWindowTitle('Label Example')
    windowExample.setGeometry(100, 100, 300, 200)
    labelA.move(100, 40)
    labelB.move(120, 80)
    windowExample.show()
    sys.exit(app.exec_())


basicWindow()
