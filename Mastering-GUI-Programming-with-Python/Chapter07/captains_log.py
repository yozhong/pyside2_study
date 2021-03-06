import sys
from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc
from PySide2 import QtMultimedia as qtmm
from PySide2 import QtMultimediaWidgets as qtmmw


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        base_widget = qtw.QWidget()
        base_widget.setLayout(qtw.QHBoxLayout())
        notebook = qtw.QTabWidget()
        base_widget.layout().addWidget(notebook)
        self.file_list = qtw.QListWidget()
        base_widget.layout().addWidget(self.file_list)
        self.setCentralWidget(base_widget)

        toolbar = self.addToolBar('Transport')
        record_act = toolbar.addAction('Rec')
        stop_act = toolbar.addAction('Stop')
        play_act = toolbar.addAction('Play')
        pause_act = toolbar.addAction('Pause')

        self.video_dir = qtc.QDir.home()
        if not self.video_dir.cd('captains_log'):
            qtc.QDir.home().mkdir('captains_log')
            self.video_dir.cd('captains_log')

        self.refresh_video_list()

        self.player = qtmm.QMediaPlayer()
        self.video_widget = qtmmw.QVideoWidget()
        self.player.setVideoOutput(self.video_widget)

        notebook.addTab(self.video_widget, 'Play')
        play_act.triggered.connect(self.player.play)
        pause_act.triggered.connect(self.player.pause)
        stop_act.triggered.connect(self.player.stop)
        play_act.triggered.connect(lambda: notebook.setCurrentWidget(self.video_widget))
        self.file_list.itemDoubleClicked.connect(self.on_file_selected)
        self.file_list.itemDoubleClicked.connect(lambda: notebook.setCurrentWidget(self.video_widget))

        self.camera = self.camera_check()
        if not self.camera:
            self.show()
            return
        self.camera.setCaptureMode(qtmm.QCamera.CaptureVideo)
        self.cvf = qtmmw.QCameraViewfinder()
        self.camera.setViewfinder(self.cvf)
        notebook.addTab(self.cvf, 'Record')
        self.camera.start()

        self.recorder = qtmm.QMediaRecorder(self.camera)

        settings = self.recorder.videoSettings()
        settings.setResolution(640, 480)
        settings.setFrameRate(24.0)
        settings.setQuality(qtmm.QMultimedia.VeryHighQuality)
        self.recorder.setVideoSettings(settings)

        record_act.triggered.connect(self.record)
        record_act.triggered.connect(lambda: notebook.setCurrentWidget(self.cvf))
        pause_act.triggered.connect(self.recorder.pause)
        stop_act.triggered.connect(self.recorder.stop)
        stop_act.triggered.connect(self.refresh_video_list)

        self.show()

    def refresh_video_list(self):
        self.file_list.clear()
        video_files = self.video_dir.entryList(
            ['*.ogg', '*.avi', '*.mov', '*.mp4', '*.mkv'],
            qtc.QDir.Files | qtc.QDir.Readable
        )
        for fn in sorted(video_files):
            self.file_list.addItem(fn)

    def on_file_selected(self, item):
        fn = item.text()
        url = qtc.QUrl.fromLocalFile(self.video_dir.filePath(fn))
        content = qtmm.QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()

    def camera_check(self):
        cameras = qtmm.QCameraInfo.availableCameras()
        if not cameras:
            qtw.QMessageBox.critical(self, 'No cameras', 'No cameras were found, recording disabled.')
        else:
            return qtmm.QCamera(cameras[0])

    def record(self):
        # create a filename
        datestamp = qtc.QDateTime.currentDateTime().toString()
        self.mediafile = qtc.QUrl.fromLocalFile(
            self.video_dir.filePath('log - ' + datestamp)
        )
        self.recorder.setOutputLocation(self.mediafile)
        # start record
        self.recorder.record()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
