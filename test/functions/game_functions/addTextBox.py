from PySide6.QtWidgets import QWidget, QLabel

def addTextBox(gameWindow, text):
    box = QWidget(gameWindow)
    box.setGeometry(35, 540, 1065, 150)
    box.setStyleSheet(" border : 1px solid black;" "background : white")

    message = QLabel("{}".format(text), box)
    message.setGeometry(10,10,700, 50)
    message.setStyleSheet("color : green")
