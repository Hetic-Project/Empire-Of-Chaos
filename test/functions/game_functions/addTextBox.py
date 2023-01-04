from PySide6.QtWidgets import QWidget

def addTextBox(gameWindow):
    box = QWidget(gameWindow)
    box.setGeometry(30, 595, 1070, 100)
    box.setStyleSheet(" border : 1px solid black;" "background : black")