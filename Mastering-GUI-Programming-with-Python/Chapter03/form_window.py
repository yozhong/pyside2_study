import sys
from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc


class FormWindow(qtw.QWidget):
    submitted = qtc.Signal(str)

    def __init__(self):
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())

        self.edit = qtw.QLineEdit()
        self.submit = qtw.QPushButton('Submit')
        self.submit.clicked.connect(self.onSubmit)

        self.layout().addWidget(self.edit)
        self.layout().addWidget(self.submit)

    def onSubmit(self):
        self.submitted.emit(self.edit.text())
        self.close()


class MainWindow(qtw.QWidget):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())

        self.label = qtw.QLabel('Click "change" to change this text.')
        self.change = qtw.QPushButton('Change')
        self.change.clicked.connect(self.onChange)
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.change)

        self.show()

    def onChange(self):
        self.formwindow = FormWindow()
        self.formwindow.submitted.connect(self.label.setText)
        self.formwindow.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
