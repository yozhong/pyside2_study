import sys
from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        self.text_edit = qtw.QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.statusBar().showMessage('Welcome to text_editor.py')
        char_count = qtw.QLabel('chars: 0')
        self.text_edit.textChanged.connect(
            lambda: char_count.setText(
                'chars: ' + str(len(self.text_edit.toPlainText()))
            )
        )
        self.statusBar().addPermanentWidget(char_count)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        edit_menu = menu_bar.addMenu('Edit')
        help_menu = menu_bar.addMenu('Help')
        open_action = file_menu.addAction('Open')
        save_action = file_menu.addAction('Save')
        quit_action = file_menu.addAction('Quit', self.destroy)
        edit_menu.addAction('Undo', self.text_edit.undo)
        redo_action = qtw.QAction('Redo', self)
        redo_action.triggered.connect(self.text_edit.redo)
        edit_menu.addAction(redo_action)

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
