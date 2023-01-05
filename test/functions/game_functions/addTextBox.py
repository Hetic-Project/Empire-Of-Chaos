from PySide6.QtWidgets import QWidget

def addTextBox(gameWindow):
    box = QWidget(gameWindow)
    box.setGeometry(35, 540, 690, 150)
    box.setStyleSheet(" border : 1px solid black;" "background : white")