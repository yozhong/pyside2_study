import sys
from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc


class MainWindow(qtw.QWidget):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        # Configure the window
        self.setWindowTitle("My Calendar App")
        self.resize(800, 600)

        # Create our widgets
        self.calendar = qtw.QCalendarWidget()
        self.event_list = qtw.QListWidget()
        self.event_title = qtw.QLineEdit()
        self.event_category = qtw.QComboBox()
        self.event_time = qtw.QTimeEdit(qtc.QTime(8, 0))
        self.allday_check = qtw.QCheckBox('All Day')
        self.event_detail = qtw.QTextEdit()
        self.add_button = qtw.QPushButton('Add/Update')
        self.del_button = qtw.QPushButton('Delete')

        # Add event categories
        self.event_category.addItems(
            ['Select category...', 'New...', 'Work', 'Meeting', 'Doctor', 'Family']
        )
        # disable the first category item
        self.event_category.model().item(0).setEnabled(False)

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
