import sys
from os import path

from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc


class Model(qtc.QObject):
    error = qtc.Signal(str)

    def save(self, filename, content):
        print('save called')
        error = ''
        if not filename:
            error = 'File name empty'
        elif path.exists(filename):
            error = f'Will not overwrite {filename}'
        else:
            try:
                with open(filename, 'w') as fh:
                    fh.write(content)
            except Exception as e:
                error = f'Cannot write file: {e}'
        if error:
            self.error.emit(error)


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        # Main UI code goes here

        # End main UI code
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
