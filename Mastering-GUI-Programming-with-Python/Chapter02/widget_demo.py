import sys
import datetime

from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc


class Qlabel(object):
    pass


class MainWindow(qtw.QWidget):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__(windowTitle='Qt Widget demo')

        #########################
        # Create widget objects #
        #########################

        # QWidget
        subwidget = qtw.QWidget(self, toolTip='This is my widget')
        subwidget.setToolTip('This is YOUR widget')
        print(subwidget.toolTip())

        # QLabel
        label = qtw.QLabel('<b>Hello Widgets!</b>', self, margin=10)

        # QLineEdit
        line_edit = qtw.QLineEdit(
            'default value',
            self,
            placeholderText='Type here',
            clearButtonEnabled=True,
            maxLength=20
        )

        # QPushButton
        button = qtw.QPushButton(
            'Push Me',
            self,
            checkable=True,
            checked=True,
            shortcut=qtg.QKeySequence('Ctrl+p')
        )

        # QComboBox
        combobox = qtw.QComboBox(
            self,
            editable=True,
            insertPolicy=qtw.QComboBox.InsertAtTop
        )
        combobox.addItem('Lemon', 1)
        combobox.addItem('Peach', 'Ohh I like Peaches!')
        combobox.addItem('Strawberry', qtw.QWidget)
        combobox.insertItem(1, 'Radish', 2)

        # QSpiBox
        spinbox = qtw.QSpinBox(
            self,
            value=12,
            maximum=100,
            minimum=10,
            prefix='$',
            suffix=' + Tax',
            singleStep=5
        )

        # QDateTimeEdit
        datetimebox = qtw.QDateTimeEdit(
            self,
            date=datetime.date.today(),
            time=datetime.time(12, 30),
            calendarPopup=True,
            maximumDate=datetime.date(2030, 1, 1),
            minimumTime=datetime.time(8, 0),
            maximumTime=datetime.time(17, 0),
            displayFormat='yyyy-MM-dd HH:mm'
        )

        # QTextEdit
        textedit = qtw.QTextEdit(
            self,
            acceptRichText=False,
            lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=25,
            placeholderText='Enter your text here'
        )

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
