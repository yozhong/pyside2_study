import csv
import sys
from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc


class CsvTableModel(qtc.QAbstractTableModel):
    """The model for a CSV table."""

    def __init__(self, csv_file):
        super().__init__()
        self.filename = csv_file
        with open(self.filename) as fh:
            csv_reader = csv.reader(fh)
            self._headers = next(csv_reader)
            self._data = list(csv_reader)

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._headers)

    def data(self, index, role=None):
        if role == qtc.Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def headerData(self, section, orientation, role=None):
        if orientation == qtc.Qt.Horizontal and role == qtc.Qt.DisplayRole:
            return self._headers[section]
        else:
            return super().headerData(section, orientation, role)

    def sort(self, column, order=None):
        self.layoutAboutToBeChanged.emit()  # needs to be emitted before sort
        self._data.sort(key=lambda x: x[column])
        if order == qtc.Qt.DescendingOrder:
            self._data.reverse()
        self.layoutChanged.emit()  # needs to be emitted after sort

    def flags(self, index):
        return super().flags(index) | qtc.Qt.ItemIsEditable

    def setData(self, index, value, role=None):
        if index.isValid() and role == qtc.Qt.EditRole:
            self._data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index, [role])
            return True
        else:
            return False

    def insertRows(self, position, rows, parent=None):
        self.beginInsertRows(
            parent or qtc.QModelIndex(),
            position,
            position + rows - 1
        )
        for i in range(rows):
            default_row = [''] * len(self._headers)
            self._data.insert(position, default_row)
        self.endInsertRows()

    def removeRows(self, position, rows, parent=None):
        self.beginRemoveRows(
            parent or qtc.QModelIndex(),
            position,
            position + rows - 1
        )
        for i in range(rows):
            del (self._data[position])
        self.endRemoveRows()

    def save_data(self):
        with open(self.filename, 'w', encoding='utf-8') as fh:
            writer = csv.writer(fh)
            writer.writerow(self._headers)
            writer.writerows(self._data)


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        self.tabview = qtw.QTableView()
        self.tabview.setSortingEnabled(True)
        self.setCentralWidget(self.tabview)

        menu = self.menuBar()
        file_menu = menu.addMenu('File')
        file_menu.addAction('Open', self.select_file)
        file_menu.addAction('Save', self.save_file)

        edit_menu = menu.addMenu('Edit')
        edit_menu.addAction('Insert Above', self.insert_above)
        edit_menu.addAction('Insert Below', self.insert_below)
        edit_menu.addAction('Remove Row(s)', self.remove_rows)

        self.show()

    def select_file(self):
        filename, _ = qtw.QFileDialog.getOpenFileName(
            self,
            'Select a CSV file to open...',
            qtc.QDir.homePath(),
            'CSV Files (*.csv) ;; All Files (*)'
        )
        if filename:
            self.model = CsvTableModel(filename)
            self.tabview.setModel(self.model)

    def save_file(self):
        if self.model:
            self.model.save_data()

    def insert_above(self):
        selected = self.tabview.selectedIndexes()
        row = selected[0].row() if selected else 0
        self.model.insertRows(row, 1, None)

    def insert_below(self):
        selected = self.tabview.selectedIndexes()
        row = selected[-1].row() if selected else self.model.rowCount(None)
        self.model.insertRows(row + 1, 1, None)

    def remove_rows(self):
        selected = self.tabview.selectedIndexes()
        if selected:
            self.model.removeRows(selected[0].row(), len(selected), None)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
