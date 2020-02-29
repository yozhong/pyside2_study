import sys
from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc


class ChatWindow(qtw.QWidget):
    submitted = qtc.Signal(str)

    def __init__(self):
        super().__init__()

        self.setLayout(qtw.QGridLayout())
        self.message_view = qtw.QTextEdit()
        self.message_view.setReadOnly(True)
        self.layout().addWidget(self.message_view, 1, 1, 1, 2)
        self.message_entry = qtw.QLineEdit()
        self.layout().addWidget(self.message_entry, 2, 1)
        self.send_btn = qtw.QPushButton('Send')
        self.send_btn.clicked.connect(self.send)
        self.layout().addWidget(self.send_btn, 2, 2)

    def write_message(self, username, message):
        self.message_view.append(f'<b>{username}: </b> {message}<br>')

    def send(self):
        message = self.message_entry.text().strip()
        if message:
            self.submitted.emit(message)
            self.message_entry.clear()


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        self.cw = ChatWindow()
        self.setCentralWidget(self.cw)
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
