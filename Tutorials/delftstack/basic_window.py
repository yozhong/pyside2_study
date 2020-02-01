import sys

from PySide2.QtWidgets import (QApplication, QLabel, QWidget, QRadioButton, QVBoxLayout)


class basicWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.label = QLabel('Which city do you live in?')
        self.rbtn1 = QRadioButton('New York')
        self.rbtn2 = QRadioButton('Houston')
        self.label2 = QLabel("")

        self.rbtn1.toggled.connect(self.onClicked)
        self.rbtn2.toggled.connect(self.onClicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.rbtn1)
        layout.addWidget(self.rbtn2)
        layout.addWidget(self.label2)

        self.setGeometry(200, 200, 300, 150)

        self.setLayout(layout)
        self.setWindowTitle('Radio Button Example')

        self.show()

    def onClicked(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.label2.setText("You live in " + radioBtn.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    windowExample = basicWindow()
    sys.exit(app.exec_())
