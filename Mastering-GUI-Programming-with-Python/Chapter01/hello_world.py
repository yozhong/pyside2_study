from PySide2 import QtWidgets


app = QtWidgets.QApplication([])
window = QtWidgets.QWidget(windowTitle='Hello Qt')
print(window.windowTitle())
window.show()
app.exec_()
