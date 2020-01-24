import sys

from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel


def greeting():
    """Slot function."""
    if msg.text():
        msg.setText("")
    else:
        msg.setText("Hello World!")


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Signals and slots')
layout = QVBoxLayout()

btn = QPushButton('Greet')
btn.clicked.connect(greeting)  # Connect clicked to greeting()

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()

sys.exit(app.exec_())
