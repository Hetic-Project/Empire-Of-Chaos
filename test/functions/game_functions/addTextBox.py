from PySide6.QtWidgets import QWidget, QLabel, QTextEdit, QLineEdit


def addTextBox(gameWindow, text):
    box = QWidget(gameWindow)
    box.setGeometry(390, 645, 690, 150)
    box.setStyleSheet(""" background : #ffffff; border-radius: 10px;""")

    message = QTextEdit("{}".format(text),box) 
    message.setGeometry(10, 20, 670, 70)
    message.setEnabled(False)
    #message.lineWrapMode ()
    message.setText(text)

    #message.setWordWrapMode ()
    message.setStyleSheet("""
            border: 3px solid #ffffff;
            border-radius: 10px;
            background : white;
            font-size: 14px;
            background-attachment: scroll;
            font-weight : bold;
        """)
