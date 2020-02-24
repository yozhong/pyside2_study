import sys
import resources
from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        self.setWindowTitle('Fight Fighter Game Lobby')
        cx_form = qtw.QWidget()
        self.setCentralWidget(cx_form)
        cx_form.setLayout(qtw.QFormLayout())
        heading = qtw.QLabel('Fight Fighter!')
        cx_form.layout().addRow(heading)

        inputs = {
            'Server': qtw.QLineEdit(),
            'Name': qtw.QLineEdit(),
            'Password': qtw.QLineEdit(echoMode=qtw.QLineEdit.Password),
            'Team': qtw.QComboBox(),
            'Ready': qtw.QCheckBox('Check when ready')
        }
        teams = ('Crimson Shark', 'Shadow Hawks', 'Night Terrors', 'Blue Crew')
        inputs['Team'].addItems(teams)
        for label, widget in inputs.items():
            cx_form.layout().addRow(label, widget)
        self.submit = qtw.QPushButton('Connect')
        self.submit.clicked.connect(
            lambda: qtw.QMessageBox.information(
                None, 'Connecting', 'Prepare for Battle!'
            )
        )
        self.reset = qtw.QPushButton('Cancel')
        self.reset.clicked.connect(self.close)
        cx_form.layout().addRow(self.submit, self.reset)

        #########
        # Fonts #
        #########
        # Setting a font
        heading_font = qtg.QFont('Impact', 32 , qtg.QFont.Bold)
        heading_font.setStretch(qtg.QFont.ExtraExpanded)
        heading.setFont(heading_font)

        label_font = qtg.QFont()
        label_font.setFamily('Impact')
        label_font.setPointSize(14)
        label_font.setWeight(qtg.QFont.DemiBold)
        label_font.setStyle(qtg.QFont.StyleItalic)

        for inp in inputs.values():
            cx_form.layout().labelForField(inp).setFont(label_font)

        # Dealing with miss fonts
        button_font = qtg.QFont('Totally Nonexistant Font Family XYZ', 15.233)
        print(f'Font is {button_font.family()}')
        actual_font = qtg.QFontInfo(button_font).family()
        print(f'Actual font used is {actual_font}')

        button_font.setStyleHint(qtg.QFont.Fantasy)
        button_font.setStyleStrategy(qtg.QFont.PreferAntialias)
        actual_font = qtg.QFontInfo(button_font)
        print(f'Actual font used is {actual_font.family()}'
              f' {actual_font.pointSize()}')
        self.submit.setFont(button_font)
        self.reset.setFont(button_font)

        ####################
        # Images and Icons #
        ####################
        # Add image
        logo = qtg.QPixmap('logo.png')
        heading.setPixmap(logo)
        if logo.width() > 400:
            logo = logo.scaledToWidth(400, qtc.Qt.SmoothTransformation)

        # Create images
        go_pixmap = qtg.QPixmap(qtc.QSize(32, 32))
        stop_pixmap = qtg.QPixmap(qtc.QSize(32, 32))
        go_pixmap.fill(qtg.QColor('green'))
        stop_pixmap.fill(qtg.QColor('red'))

        # Create icon
        connect_icon = qtg.QIcon()
        connect_icon.addPixmap(go_pixmap, qtg.QIcon.Active)
        connect_icon.addPixmap(stop_pixmap, qtg.QIcon.Disabled)

        self.submit.setIcon(connect_icon)
        self.submit.setDisabled(True)
        inputs['Server'].textChanged.connect(
            lambda x: self.submit.setDisabled(x == '')
        )

        # using resources
        inputs['Team'].setItemIcon(0, qtg.QIcon(':/teams/crimson_sharks.png'))
        inputs['Team'].setItemIcon(1, qtg.QIcon(':/teams/shadow_hawks.png'))
        inputs['Team'].setItemIcon(2, qtg.QIcon(':/teams/night_terrors.png'))
        inputs['Team'].setItemIcon(3, qtg.QIcon(':/teams/blue_crew.png'))

        libsans_id = qtg.QFontDatabase.addApplicationFont(
            ':/fonts/LiberationSans-Regular.ttf'
        )
        family = qtg.QFontDatabase.applicationFontFamilies(libsans_id)[0]
        libsans = qtg.QFont(family)
        inputs['Team'].setFont(libsans)

        ##########
        # Colors #
        ##########
        app = qtw.QApplication.instance()
        palette = app.palette()
        palette.setColor(qtg.QPalette.Button, qtg.QColor('#333'))
        palette.setColor(qtg.QPalette.ButtonText, qtg.QColor('#3F3'))
        palette.setColor(qtg.QPalette.Disabled, qtg.QPalette.Button, qtg.QColor('#888'))
        palette.setColor(qtg.QPalette.Disabled, qtg.QPalette.ButtonText, qtg.QColor('#F88'))
        self.submit.setPalette(palette)
        self.reset.setPalette(palette)

        dotted_brush = qtg.QBrush(qtg.QColor('white'), qtc.Qt.Dense2Pattern)
        gradient = qtg.QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0, qtg.QColor('navy'))
        gradient.setColorAt(0.5, qtg.QColor('darkred'))
        gradient.setColorAt(1, qtg.QColor('orange'))
        gradient_brush = qtg.QBrush(gradient)

        window_palette = app.palette()
        window_palette.setBrush(qtg.QPalette.Window, gradient_brush)
        window_palette.setBrush(qtg.QPalette.Active, qtg.QPalette.WindowText, dotted_brush)
        self.setPalette(window_palette)

        ##################
        # Qt StyleSheets #
        ##################
        stylesheet = """
        QMainWindow {
            background-color: black;
        }
        QWidget {
            background-color: transparent;
            color: #3F3;

        }
        QLineEdit, QComboBox, QCheckBox {
            font-size: 16pt;        
        }
        """

        stylesheet += """
        QPushButton
        {
            background-color: #333;
        }
        QCheckBox::indicator:unchecked
        {
            border: 1px solid silver;
            background-color: darkred;
        }
        QCheckBox::indicator:checked
        {
            border: 1px solid silver;
            background-color: #3F3;
        }
        """

        # Using discrete classes
        stylesheet += """
        .QWidget {
           background: url(tile.png);
        }
        """

        self.submit.setObjectName('SubmitButton')
        stylesheet += """
        #SubmitButton:disabled {
            background-color: #888;
            color: darkred;

        }
        """

        for inp in ('Server', 'Name', 'Password'):
            inp_widget = inputs[inp]
            inp_widget.setStyleSheet('background-color: black')

        self.setStyleSheet(stylesheet)

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    windows_style = qtw.QStyleFactory.create('Windows')
    app.setStyle(windows_style)
    mw = MainWindow()
    sys.exit(app.exec_())
