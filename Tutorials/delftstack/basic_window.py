import sys

from PySide2 import QtWidgets


def basicWindow():
    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()

    buttonA = QtWidgets.QPushButton(windowExample)
    labelA = QtWidgets.QLabel(windowExample)

    buttonA.setText('Click!')
    labelA.setText('Show Label')

    windowExample.setWindowTitle('Push Button Example')
    windowExample.setGeometry(100, 100, 300, 200)

    buttonA.move(100, 50)
    labelA.move(110, 100)

    windowExample.show()
    sys.exit(app.exec_())


basicWindow()
