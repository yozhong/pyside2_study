import sys
from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        self.text_edit = qtw.QTextEdit()
        self.setCentralWidget(self.text_edit)
        self.statusBar().showMessage('Welcome to text_editor.py')

        char_count = qtw.QLabel('chars: 0')
        self.text_edit.textChanged.connect(
            lambda: char_count.setText(
                'chars: ' + str(len(self.text_edit.toPlainText()))
            )
        )
        self.statusBar().addPermanentWidget(char_count)
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
