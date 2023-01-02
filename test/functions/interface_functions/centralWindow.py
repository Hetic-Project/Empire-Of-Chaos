from PySide6.QtWidgets import QWidget


def centralWindow(self):
    centralArea = QWidget()
    centralArea.setGeometry(0, 0, 800, 600)
    self.setCentralWidget(centralArea)
    centralArea.setStyleSheet(
        "background: url(test/images/map/Grassland.png) no-repeat center center cover ;")
    return centralArea
