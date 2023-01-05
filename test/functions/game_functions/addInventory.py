import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel
from functions.game_functions.createcelleInventory import *


def addInventory(gameWindow) :

    yPosition = 6

    rowInventory = []
    MapcellInventory = []

    title = QLabel("Inventaire : " , gameWindow)
    title.setGeometry(751 , 340 , 350 , 40 )
    title.setStyleSheet("font-size : 25px;")

    limiteInventaire = QWidget(gameWindow)
    limiteInventaire.setGeometry(750 ,385 , 350 , 140)
    limiteInventaire.setStyleSheet("border : none;")


    for y in range(3) :
        Y = QWidget(limiteInventaire)
        Y.setGeometry(29 , yPosition , 325 , 40)
        Y.setStyleSheet("border : none;")
        yPosition = yPosition + 44
        
        rowInventory.append(Y)
    
    for i in rowInventory:
        # a chaque itération j'appel la fonction createCellInYPosition qui
        # retourne la liste des QWidget créer pour la ligne i que je stock dans une variable cells
        cellsInv = createCellInYPositionInventory(i)
        # je stock la liste des QWidget pour la ligne i dans la liste mapCell
        MapcellInventory.append(cellsInv)
        # voila a quoi ressemblera mapCell : mapCell [ ligne1[QWidget1, QWidget2 ], ligne2[QWidget1, QWidget2 ], ... ]
        # mapCell contient donc toute les coordonnée X et Y de la map






    
