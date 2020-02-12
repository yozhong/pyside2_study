import sys
from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc


class FormWindow(qtw.QWidget):
    submitted = qtc.Signal([str], [int, str])

    def __init__(self):
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())

        self.edit = qtw.QLineEdit()
        self.submit = qtw.QPushButton('Submit')
        self.submit.clicked.connect(self.onSubmit)

        self.layout().addWidget(self.edit)
        self.layout().addWidget(self.submit)

    def onSubmit(self):
        if self.edit.text().isdigit():
            text = self.edit.text()
            self.submitted[int, str].emit(int(text), text)
        else:
            self.submitted[str].emit(self.edit.text())
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

    @qtc.Slot(str)
    def onSubmittedStr(self, string):
        self.label.setText(string)

    @qtc.Slot(int, str)
    def onSubmittedIntStr(self, integer, string):
        text = f'The string {string} become the number {integer}'
        self.label.setText(text)

    def onChange(self):
        self.formwindow = FormWindow()
        self.formwindow.submitted[str].connect(self.onSubmittedStr)
        self.formwindow.submitted[int, str].connect(self.onSubmittedIntStr)
        self.formwindow.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
