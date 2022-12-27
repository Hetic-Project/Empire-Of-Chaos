import sys
from PySide6.QtGui import QIcon, QKeyEvent, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget


class Map(QTableWidget):

    def __init__(self):
        super().__init__()

        centralArea = QWidget()
        self.setCentralWidget(centralArea)
        centralArea.setStyleSheet("background: #419eee")

        # créer un tableau
        map = QTableWidget(11, 13, centralArea)
        map.setFixedSize(800, 600)
        i = 0
        while i < 13:
            map.setColumnWidth(i, 50)
            map.setRowHeight(i, 48)
            i = i+1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    map = Map()
    map.show()
    sys.exit(app.exec())
