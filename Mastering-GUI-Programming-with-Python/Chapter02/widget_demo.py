import sys

from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc


class IPv4Validator(qtg.QValidator):
    """Enforce entry of IPv4 address"""
    def validate(self, string, index):
        octects = string.split('.')
        if len(octects) > 4:
            state = qtg.QValidator.Invalid
        elif not all([x.isdigit() for x in octects if x != '']):
            state = qtg.QValidator.Invalid
        elif not all([0 <= int(x) <= 255 for x in octects if x != '']):
            state = qtg.QValidator.Invalid
        elif len(octects) < 4:
            state = qtg.QValidator.Intermediate
        elif any([x == '' for x in octects]):
            state = qtg.QValidator.Intermediate
        else:
            state = qtg.QValidator.Acceptable
        return state, string, index


class MainWindow(qtw.QWidget):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        self.setWindowTitle('Qt Widget demo')
        self.setToolTip('This is my widget')

        #########################
        # Create widget objects #
        #########################
        # QWidget
        sub_widget = qtw.QWidget(self)
        sub_widget.setToolTip('This is your widget')
        print(sub_widget.toolTip())

        # QLabel
        label = qtw.QLabel(self)
        label.setText('<b>Hello Widgets!</b>')
        label.setMargin(10)

        # QLineEdit
        line_edit = qtw.QLineEdit(self)
        line_edit.setText('default value')
        line_edit.setPlaceholderText('Type here')
        line_edit.setClearButtonEnabled(True)
        line_edit.setMaxLength(20)

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
        datetime_box = qtw.QDateTimeEdit(self)
        datetime_box.setDate(qtc.QDate.currentDate())
        datetime_box.setTime(qtc.QTime(12, 30))
        datetime_box.setCalendarPopup(True)
        datetime_box.setMaximumDate(qtc.QDate(2030, 1, 1))
        datetime_box.setMaximumTime(qtc.QTime(17, 0))
        datetime_box.setDisplayFormat('yyyy-MM-dd HH:mm')

        # QTextEdit
        text_edit = qtw.QTextEdit(self)
        text_edit.setAcceptRichText(False)
        text_edit.setLineWrapMode(qtw.QTextEdit.FixedColumnWidth)
        text_edit.setLineWrapColumnOrWidth(25)
        text_edit.setPlaceholderText('Enter your text here')

        ##################
        # Layout Objects #
        ##################
        layout = qtw.QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(label)
        layout.addWidget(line_edit)

        sub_layout = qtw.QHBoxLayout()
        layout.addLayout(sub_layout)

        sub_layout.addWidget(button)
        sub_layout.addWidget(combobox)

        container = qtw.QWidget(self)
        grid_layout = qtw.QGridLayout()
        container.setLayout(grid_layout)

        grid_layout.addWidget(spinbox, 0, 0)
        grid_layout.addWidget(datetime_box, 0, 1)
        grid_layout.addWidget(text_edit, 1, 0, 2, 2)

        form_layout = qtw.QFormLayout()
        layout.addLayout(form_layout)

        form_layout.addRow('Item 1', qtw.QLineEdit(self))
        form_layout.addRow('Item 2', qtw.QLineEdit(self))
        form_layout.addRow(qtw.QLabel('<b>This is a label-only row</b>'))

        ################
        # Size Control #
        ################
        # Fix at 150 pixels wide by 40 pixels high
        label.setFixedSize(150, 40)

        # Setting minimum and maximum size
        line_edit.setMinimumSize(150, 15)
        line_edit.setMaximumSize(500, 50)

        # set the spinbox to a fixed width
        spinbox.setSizePolicy(qtw.QSizePolicy.Fixed, qtw.QSizePolicy.Preferred)

        # set the text edit to expand
        text_edit.setSizePolicy(qtw.QSizePolicy.MinimumExpanding, qtw.QSizePolicy.MinimumExpanding)
        text_edit.sizeHint = lambda: qtc.QSize(500, 500)

        # use stretch factor
        stretch_layout = qtw.QHBoxLayout()
        layout.addLayout(stretch_layout)

        stretch_layout.addWidget(qtw.QLineEdit('Short'), 1)
        stretch_layout.addWidget(qtw.QLineEdit('Long'), 2)

        #############################
        # Container Widgets         #
        #############################
        tab_widget = qtw.QTabWidget()
        tab_widget.setMovable(True)
        tab_widget.setTabPosition(qtw.QTabWidget.West)
        tab_widget.setTabShape(qtw.QTabWidget.Triangular)
        layout.addWidget(tab_widget)

        tab_widget.addTab(container, 'Tab the first')
        tab_widget.addTab(sub_widget, 'Tab the second')

        group_box = qtw.QGroupBox('Buttons')
        group_box.setCheckable(True)
        group_box.setChecked(True)
        group_box.setAlignment(qtc.Qt.AlignHCenter)
        group_box.setFlat(True)

        group_box.setLayout(qtw.QHBoxLayout())
        group_box.layout().addWidget(qtw.QPushButton('OK'))
        group_box.layout().addWidget(qtw.QPushButton('Cancel'))
        layout.addWidget(group_box)

        ##############
        # Validation #
        ##############
        line_edit.setText('0.0.0.0')
        line_edit.setValidator(IPv4Validator())

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
