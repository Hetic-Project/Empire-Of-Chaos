from PySide6.QtWidgets import QWidget


def centralWindow(self):
    centralArea = QWidget()
    centralArea.setGeometry(0, 0, 800, 600)
    self.setCentralWidget(centralArea)
    # centralArea.setStyleSheet(
    #     "background : white")
    return centralArea
