import sys

from PySide2 import QtWidgets


def basicWindow():
    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()
    windowExample.setGeometry(0, 0, 400, 400)
    windowExample.setWindowTitle('Basic Window Example')
    windowExample.show()
    sys.exit(app.exec_())


basicWindow()
