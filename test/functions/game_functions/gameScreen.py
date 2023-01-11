from PySide6.QtWidgets import QWidget
from functions.game_functions.generateRandomCoordinate import *
from functions.game_functions.drawGameMap import *
from functions.game_functions.createHeroPanel import *
from functions.game_functions.addInventory import *
from functions.game_functions.addAttackIndication import *
from functions.game_functions.addTextBox import *
from functions.game_functions.addPanelGoals import *


def gameScreen(world, stage, centralArea, text):

    gameWindow = QWidget(centralArea)
    gameWindow.setGeometry(0, 0, 1275, 900)
    gameWindow.setStyleSheet("background-color: #149414;")

    drawGameMap(world, stage, gameWindow, Hero.front)
    addTextBox(gameWindow, text)
    addInventory(gameWindow)
    return gameWindow
