from PySide6.QtWidgets import QWidget, QTextEdit

def addTextBox(gameWindow, text):
    box = QWidget(gameWindow)
    box.setGeometry(35, 540, 690, 150)
    box.setStyleSheet(" border : 1px solid black;" "background : white")

    message = QTextEdit(box)
    message.setEnabled(False)
    message.setText("{}".format(text))
    message.setGeometry(10,10,700, 50)
    message.setStyleSheet("color : green")
