import sys
from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()

        ######################
        # The central widget #
        ######################
        self.text_edit = qtw.QTextEdit()
        self.setCentralWidget(self.text_edit)

        #################
        # The Statusbar #
        #################
        self.statusBar().showMessage('Welcome to text_editor.py')
        char_count = qtw.QLabel('chars: 0')
        self.text_edit.textChanged.connect(
            lambda: char_count.setText(
                'chars: ' + str(len(self.text_edit.toPlainText()))
            )
        )
        self.statusBar().addPermanentWidget(char_count)


        ###############
        # The menubar #
        ###############
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

        ############################
        # The Toolbar and QActions #
        ############################
        tool_bar = self.addToolBar('File')

        tool_bar.setMovable(False)
        tool_bar.setFloatable(False)
        tool_bar.setAllowedAreas(qtc.Qt.TopToolBarArea | qtc.Qt.BottomToolBarArea)

        open_icon = self.style().standardIcon(qtw.QStyle.SP_DirOpenIcon)
        save_icon = self.style().standardIcon(qtw.QStyle.SP_DriveHDIcon)

        open_action.setIcon(open_icon)
        tool_bar.addAction(open_action)
        tool_bar.addAction(save_icon, 'Save', lambda: self.statusBar().showMessage('File Saved!'))
        help_action = qtw.QAction(
            self.style().standardIcon(qtw.QStyle.SP_DialogHelpButton), 'Help', self
        )
        help_action.triggered.connect(lambda: self.statusBar().showMessage('Sorry, no help yet!'))
        tool_bar.addAction(help_action)

        tool_bar2 = qtw.QToolBar('Edit')
        tool_bar2.addAction('Copy', self.text_edit.copy)
        tool_bar2.addAction('Cut', self.text_edit.cut)
        tool_bar2.addAction('Paste', self.text_edit.paste)
        self.addToolBar(qtc.Qt.RightToolBarArea, tool_bar2)

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
