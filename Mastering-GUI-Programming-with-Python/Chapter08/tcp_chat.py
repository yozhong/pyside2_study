import sys
from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc
from PySide2 import QtNetwork as qtn


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


class UdpChatInterface(qtc.QObject):
    port = 7777
    delimiter = '||'
    received = qtc.Signal(str, str)
    error = qtc.Signal(str)

    def __init__(self, username):
        super().__init__()
        self.username = username

        self.socket = qtn.QUdpSocket()
        self.socket.bind(qtn.QHostAddress(qtn.QHostAddress.Any), self.port)
        self.socket.readyRead.connect(self.process_datagrams)
        self.socket.error.connect(self.on_error)

    def on_error(self, socket_error):
        error_index = qtn.QAbstractSocket.staticMetaObject.indexOfEnumerator('SocketError')
        error = qtn.QAbstractSocket.staticMetaObect.enumerator(error_index).valueToKey(socket_error)
        message = f'There was a network error: {error}'
        self.error.emit(message)

    def process_datagrams(self):
        while self.socket.hasPendingDatagrams():
            datagram = self.socket.receiveDatagram()
            raw_message = bytes(datagram.data()).decode('utf-8')
            if self.delimiter not in raw_message:
                continue
            username, message = raw_message.split(self.delimiter, 1)
            self.received.emit(username, message)

    def send_message(self, message):
        msg_bytes = f'{self.username}{self.delimiter}{message}'.encode('utf-8')
        self.socket.writeDatagram(qtc.QByteArray(msg_bytes), qtn.QHostAddress.Broadcast, self.port)


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        self.cw = ChatWindow()
        self.setCentralWidget(self.cw)

        username = qtc.QDir.home().dirName()
        self.interface = UdpChatInterface(username)
        self.cw.submitted.connect(self.interface.send_message)
        self.interface.received.connect(self.cw.write_message)
        self.interface.error.connect(lambda x: qtw.QMessageBox.critical(None, 'Error', x))

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
