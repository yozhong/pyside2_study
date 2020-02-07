import sys

from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc


class MainWindow(qtw.QWidget):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        self.setWindowTitle('Qt Widget demo')

        #########################
        # Create widget objects #
        #########################
        # QWidget
        subwidget = qtw.QWidget(self)
        self.setToolTip('This is my widget')
        subwidget.setToolTip('This is your widget')
        print(subwidget.toolTip())

        # QLabel
        label = qtw.QLabel(self)
        label.setText('<b>Hello Widgets!</b>')
        label.setMargin(10)

        # QLineEdit
        lineedit = qtw.QLineEdit(self)
        lineedit.setText('default value')
        lineedit.setPlaceholderText('Type here')
        lineedit.setClearButtonEnabled(True)
        lineedit.setMaxLength(20)

        # QPushButton
        button = qtw.QPushButton(self)
        button.setText('Push Me')
        button.setCheckable(True)
        button.setChecked(True)
        button.setShortcut(qtg.QKeySequence('Ctrl+p'))

        # QComboBox
        combobox = qtw.QComboBox(self)
        combobox.setEditable(True)
        combobox.setInsertPolicy(qtw.QComboBox.InsertAtTop)
        combobox.addItem('Lemon', 1)
        combobox.addItem('Peach', 'Ohh I like Peaches!')
        combobox.addItem('Strawberry', qtw.QWidget)
        combobox.insertItem(1, 'Radish', 2)

        # QSpiBox
        spinbox = qtw.QSpinBox(self)
        spinbox.setValue(12)
        spinbox.setMaximum(100)
        spinbox.setMinimum(10)
        spinbox.setPrefix('$')
        spinbox.setSuffix(' + Tax')
        spinbox.setSingleStep(5)

        # QDateTimeEdit
        datetimebox = qtw.QDateTimeEdit(self)
        datetimebox.setDate(qtc.QDate.currentDate())
        datetimebox.setTime(qtc.QTime(12, 30))
        datetimebox.setCalendarPopup(True)
        datetimebox.setMaximumDate(qtc.QDate(2030, 1, 1))
        datetimebox.setMaximumTime(qtc.QTime(17, 0))
        datetimebox.setDisplayFormat('yyyy-MM-dd HH:mm')

        # QTextEdit
        textedit = qtw.QTextEdit(self)
        textedit.setAcceptRichText(False)
        textedit.setLineWrapMode(qtw.QTextEdit.FixedColumnWidth)
        textedit.setLineWrapColumnOrWidth(25)
        textedit.setPlaceholderText('Enter your text here')

        ##################
        # Layout Objects #
        ##################
        layout = qtw.QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(label)
        layout.addWidget(lineedit)

        sublayout = qtw.QHBoxLayout()
        layout.addLayout(sublayout)

        sublayout.addWidget(button)
        sublayout.addWidget(combobox)

        container = qtw.QWidget(self)
        gridlayout = qtw.QGridLayout()
        container.setLayout(gridlayout)

        gridlayout.addWidget(spinbox, 0, 0)
        gridlayout.addWidget(datetimebox, 0, 1)
        gridlayout.addWidget(textedit, 1, 0, 2, 2)

        formlayout = qtw.QFormLayout()
        layout.addLayout(formlayout)

        formlayout.addRow('Item 1', qtw.QLineEdit(self))
        formlayout.addRow('Item 2', qtw.QLineEdit(self))
        formlayout.addRow(qtw.QLabel('<b>This is a label-only row</b>'))

        ################
        # Size Control #
        ################
        # Fix at 150 pixels wide by 40 pixels high
        label.setFixedSize(150, 40)

        # Setting minimum and maximum size
        lineedit.setMinimumSize(150, 15)
        lineedit.setMaximumSize(500, 50)

        # set the spinbox to a fixed width
        spinbox.setSizePolicy(qtw.QSizePolicy.Fixed, qtw.QSizePolicy.Preferred)

        # set the textedit to expand
        textedit.setSizePolicy(qtw.QSizePolicy.MinimumExpanding, qtw.QSizePolicy.MinimumExpanding)
        textedit.sizeHint = lambda: qtc.QSize(500, 500)

        # use stretch factor
        stretchlayout = qtw.QHBoxLayout()
        layout.addLayout(stretchlayout)

        stretchlayout.addWidget(qtw.QLineEdit('Short'), 1)
        stretchlayout.addWidget(qtw.QLineEdit('Long'), 2)

        #############################
        # Container Widgets         #
        #############################
        tabwidget = qtw.QTabWidget()
        tabwidget.setMovable(True)
        tabwidget.setTabPosition(qtw.QTabWidget.West)
        tabwidget.setTabShape(qtw.QTabWidget.Triangular)
        layout.addWidget(tabwidget)

        tabwidget.addTab(container, 'Tab the first')
        tabwidget.addTab(subwidget, 'Tab the second')

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
