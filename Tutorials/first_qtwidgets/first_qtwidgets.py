import sys
from PySide2.QtWidgets import QApplication, QLabel

# create a QApplication instance and pass argument
app = QApplication(sys.argv)

label = QLabel("Hello World!")
label.show()

app.exec_()
