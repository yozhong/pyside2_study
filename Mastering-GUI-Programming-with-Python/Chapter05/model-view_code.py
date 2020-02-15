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


class View(qtw.QWidget):
    submitted = qtc.Signal(str, str)

    def __init__(self):
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())
        self.filename = qtw.QLineEdit()
        self.filecontent = qtw.QTextEdit()
        self.savebutton = qtw.QPushButton('Save', clicked=self.submit)
        self.layout().addWidget(self.filename)
        self.layout().addWidget(self.filecontent)
        self.layout().addWidget(self.savebutton)

    def submit(self):
        filename = self.filename.text()
        filecontent = self.filecontent.toPlainText()
        self.submitted.emit(filename, filecontent)

    def showError(self, error):
        qtw.QMessageBox.critical(None, 'Error', error)


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        self.view = View()
        self.setCentralWidget(self.view)

        self.model = Model()

        self.view.submitted.connect(self.model.save)
        self.model.error.connect(self.view.showError)

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
