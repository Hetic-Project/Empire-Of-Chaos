from PySide6.QtWidgets import QWidget


def centralWindow(self):

    centralArea = QWidget()
    centralArea.setStyleSheet("border : 1px solid blue;")
    self.setCentralWidget(centralArea)
    return centralArea
