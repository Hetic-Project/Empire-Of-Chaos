import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel
from functions.game_functions.stages.Stage import *
from functions.game_functions.UseItems import *


def addItemsInInventory(MapCellInventory):
    # elle doit sauvegarder les items dans l'inventaire

    count = 0

    
    for i in Stage.saveDropItems:
        ItemImage = QPushButton(MapCellInventory[count][0])
        ItemImage.setGeometry(0 ,0 , 40 , 40)
        ItemImage.setStyleSheet(i)
        ItemImage.clicked.connect(UseItems(i))
        count = count + 1
        


    



        