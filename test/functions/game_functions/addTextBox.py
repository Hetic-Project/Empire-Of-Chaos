<<<<<<< HEAD
from PySide6.QtWidgets import QWidget, QTextEdit
=======
from PySide6.QtWidgets import QWidget, QLabel, QTextEdit, QLineEdit

>>>>>>> 89e3b18af19813387238b011a73bbece0c120c89

def addTextBox(gameWindow, text):
    box = QWidget(gameWindow)
    box.setGeometry(35, 540, 690, 150)
    box.setStyleSheet(""" background : #ffffff; border-radius: 10px;""")

<<<<<<< HEAD
    message = QTextEdit(box)
    message.setEnabled(False)
    message.setText("{}".format(text))
    message.setGeometry(10,10,700, 50)
    message.setStyleSheet("color : green")
=======
    message = QTextEdit("{}".format(text),box) 
    message.setGeometry(10, 20, 670, 70)
    message.setEnabled(False)
    message.lineWrapMode ()
    #message.setWordWrapMode ()
    message.setStyleSheet("""
            border: 3px solid #ffffff;
            border-radius: 10px;
            background : white;
            font-size: 12px;
            background-attachment: scroll;
        """)
>>>>>>> 89e3b18af19813387238b011a73bbece0c120c89
