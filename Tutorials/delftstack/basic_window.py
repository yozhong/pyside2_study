import sys

from PySide2.QtWidgets import (QApplication, QAction, qApp, QMainWindow)


class basicWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(200, 200, 300, 200)

        self.setWindowTitle('Menu Bar Example')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    windowExample = basicWindow()
    windowExample.show()
    sys.exit(app.exec_())
