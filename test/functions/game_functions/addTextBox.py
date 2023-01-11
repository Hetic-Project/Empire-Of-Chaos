from PySide6.QtWidgets import QWidget, QLabel, QTextEdit, QLineEdit, QVBoxLayout
from functions.game_functions.stages.Stage import *

def addTextBox(gameWindow):
    box = QWidget(gameWindow)
    box.setGeometry(35, 645, 690, 150)
    box.setStyleSheet(""" background : #ffffff; border-radius: 10px;""")

    positiony = 0
    #message = QTextEdit(box)
    #message.setEnabled(False)
    #message.append()

    for i in Stage.messageTab:
        message = QTextEdit(box)
        message.setEnabled(False)

        message.setGeometry(10, positiony, 670, 20)
        #message.lineWrapMode ()
        message.append(i)
        #message.setWordWrapMode ()
        message.setStyleSheet("""
                border: 1px solid black;
                border-radius: 10px;
                background : white;
                font-size: 12px;
                background-attachment: scroll;
                """)
        positiony += 29

