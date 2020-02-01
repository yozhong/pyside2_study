import sys

from PySide2.QtGui import QIcon, Qt
from PySide2.QtWidgets import (QApplication, QAction, qApp, QMainWindow, QLabel)


class basicWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.label = QLabel("The toggle state is ")
        self.label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(self.label)

        toggleAction = QAction('&Toggle Label', self, checkable=True)
        toggleAction.setStatusTip('Toggle the label')
        toggleAction.triggered.connect(self.toggleLabel)

        exitAction = QAction(QIcon('exit.png'),
                             '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(toggleAction)
        fileMenu.addAction(exitAction)

        self.setGeometry(200, 200, 300, 200)

        self.setWindowTitle('Menu Bar Example')

    def toggleLabel(self, state):
        self.label.setText("The toggle state is {}".format(state))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    windowExample = basicWindow()
    windowExample.show()
    sys.exit(app.exec_())
