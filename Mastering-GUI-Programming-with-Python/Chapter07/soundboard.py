import sys
from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc
from PySide2 import QtMultimedia as qtmm


class SoundWidget(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(qtw.QGridLayout())
        self.label = qtw.QLabel('No file loaded')
        self.layout().addWidget(self.label, 0, 0, 1, 2)

        self.play_button = PlayButton()
        self.layout().addWidget(self.play_button, 3, 0, 1, 2)

        self.player = qtmm.QMediaPlayer()
        self.play_button.clicked.connect(self.on_playbutton)
        self.player.stateChanged.connect(self.play_button.on_state_changed)

        self.file_button = qtw.QPushButton('Load File')
        self.file_button.clicked.connect(self.get_file)
        self.layout().addWidget(self.file_button, 4, 0)

        self.position = qtw.QSlider()
        self.position.setMinimum(0)
        self.position.setOrientation(qtc.Qt.Horizontal)
        self.layout().addWidget(self.position, 1, 0, 1, 2)

        self.player.positionChanged.connect(self.position.setSliderPosition)
        self.player.durationChanged.connect(self.position.setMaximum)
        self.position.sliderMoved.connect(self.player.setPosition)


    def on_playbutton(self):
        if self.player.state() == qtmm.QMediaPlayer.PlayingState:
            self.player.stop()
        else:
            self.player.play()

    def get_file(self):
        fn, _ = qtw.QFileDialog.getOpenFileUrl(
            self,
            'Select File',
            qtc.QDir.homePath(),
            'Audio files (*.wav *.flac *.mp3 *.ogg *.aiff);; All files (*)'
        )
        if fn:
            self.set_file(fn)

    def set_file(self, url):
        content = qtmm.QMediaContent(url)
        self.player.setMedia(content)
        self.label.setText(url.fileName())


class PlayButton(qtw.QPushButton):
    play_stylesheet = 'background-color: lightgreen; color: black;'
    stop_stylesheet = 'background-color: darkred; color: white;'

    def __init__(self):
        super().__init__('Play')
        self.setFont(qtg.QFont('Sans', 32, qtg.QFont.Bold))
        self.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
        self.setStyleSheet(self.play_stylesheet)

    def on_state_changed(self, state):
        if state == qtmm.QMediaPlayer.PlayingState:
            self.setStyleSheet(self.stop_stylesheet)
            self.setText('Stop')
        else:
            self.setStyleSheet(self.play_stylesheet)
            self.setText('Play')


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        rows = 3
        columns = 3
        soundboard = qtw.QWidget()
        soundboard.setLayout(qtw.QGridLayout())
        self.setCentralWidget(soundboard)
        for c in range(columns):
            for r in range(rows):
                sw = SoundWidget()
                soundboard.layout().addWidget(sw, c, r)

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
