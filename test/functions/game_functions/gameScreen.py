from PySide6.QtWidgets import QWidget
from functions.game_functions.generateRandomCoordinate import *
from functions.game_functions.drawGameMap import *
from functions.game_functions.createHeroPanel import *
from functions.game_functions.addInventory import *
from functions.game_functions.addAttackIndication import *
from functions.game_functions.addTextBox import *
from functions.game_functions.addPanelGoals import *


def gameScreen(centralArea ,countMonster , randomMonsterInMap , countKey , keyMapArray, text):

    gameWindow = QWidget(centralArea)
    gameWindow.setGeometry(0, 0, 1575, 1000)

    drawGameMap(gameWindow, Hero.front)
    createHeroPanel(gameWindow)
    addInventory(gameWindow)
    addTextBox(gameWindow, text)
    addPanelGoals(gameWindow , countMonster , randomMonsterInMap , countKey , keyMapArray)
    return gameWindow
