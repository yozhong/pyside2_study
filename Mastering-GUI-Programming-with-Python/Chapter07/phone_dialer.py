import sys
from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc
from PySide2 import QtMultimedia as qtmm

import resources


class SoundButton(qtw.QPushButton):
    def __init__(self, wav_file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wave_file = wav_file
        self.player = qtmm.QSoundEffect()
        self.player.setSource(qtc.QUrl.fromLocalFile(wav_file))
        self.clicked.connect(self.player.play)


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        dialpad = qtw.QWidget()
        self.setCentralWidget(dialpad)
        dialpad.setLayout(qtw.QGridLayout())

        for i, symbol in enumerate('123456789*0#'):
            button = SoundButton(f':/dtmf/{symbol}.wav', symbol)
            row = i // 3
            column = i % 3
            dialpad.layout().addWidget(button, row, column)

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
