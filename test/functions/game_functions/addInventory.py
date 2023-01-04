import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel




def addInventory(gameWindow) :

    yPosition = 6

    title = QLabel("Inventaire" , gameWindow)
    title.setGeometry(751 , 340 , 350 , 40 )
    title.setStyleSheet("font-size : 25px;")

    limiteInventaire = QWidget(gameWindow)
    limiteInventaire.setGeometry(750 ,385 , 350 , 140)
    limiteInventaire.setStyleSheet("border : 1px solid black;" "background : #B03920;")


    for y in range(3) :
        Y = QWidget(limiteInventaire)
        Y.setGeometry(10 , yPosition , 330 , 40)
        Y.setStyleSheet("border : 1px solid black;")
        yPosition = yPosition + 44
        


    





    
