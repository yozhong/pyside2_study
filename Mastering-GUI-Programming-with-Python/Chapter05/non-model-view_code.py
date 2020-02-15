import sys
from os import path

from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        form = qtw.QWidget()
        self.setCentralWidget(form)
        form.setLayout(qtw.QVBoxLayout())
        self.filename = qtw.QLineEdit()
        self.filecontent = qtw.QTextEdit()
        self.savebutton = qtw.QPushButton('Save', clicked=self.save)

        form.layout().addWidget(self.filename)
        form.layout().addWidget(self.filecontent)
        form.layout().addWidget(self.savebutton)

        self.show()

    def save(self):
        filename = self.filename.text()
        error = ''
        if not filename:
            error = 'File name empty'
        elif path.exists(filename):
            error = f'Will not overwrite {filename}'
        else:
            try:
                with open(filename, 'w') as fh:
                    fh.write(self.filecontent.toPlainText())
            except Exception as e:
                error = f'Cannot write file: {e}'
        if error:
            qtw.QMessageBox.critical(None, 'Error', error)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
