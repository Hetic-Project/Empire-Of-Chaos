from PySide6.QtWidgets import QWidget
from functions.game_functions.generateRandomCoordinate import *
from functions.game_functions.drawGameMap import *
from functions.game_functions.createHeroPanel import *
from functions.game_functions.addInventory import *
from functions.game_functions.addTextBox import *


def gameScreen(centralArea):

    gameWindow = QWidget(centralArea)
    gameWindow.setGeometry(0, 0, 1175, 900)
    gameWindow.setStyleSheet("border: none")

    drawGameMap(gameWindow, Hero.front)
    createHeroPanel(gameWindow)
    addInventory(gameWindow)
    addTextBox(gameWindow)
    return gameWindow
