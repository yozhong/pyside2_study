import sys
from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc


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

        self.show()

    def refresh_video_list(self):
        self.file_list.clear()
        video_files = self.video_dir.entryList(
            ['*.ogg', '*.avi', '*.mov', '*.mp4', '*.mkv'],
            qtc.QDir.Files | qtc.QDir.Readable
        )
        for fn in sorted(video_files):
            self.file_list.addItem(fn)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
