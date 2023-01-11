import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel
from functions.game_functions.stages.Stage import *
from functions.interface_functions.centralWindow import *
from functions.game_functions.stages.Stage import *
from functions.game_functions.addMonsterInMap import *
from functions.game_functions.gameScreen import *
from functions.game_functions.createMonsterPanel import *
from functions.game_functions.addSprite import *
from functions.interface_functions.gameMainTitleScreen import *
from functions.game_functions.addAttackIndication import *
from functions.game_functions.closeFunction import *
from functions.game_functions.stages.nextStage import *
from functions.game_functions.stages.nextStage import *





def UseItems(i):

    if i == Stage.dropInfo["petite potion de hp"]["image"]:
        if Hero.life <= 50:
            Hero.life = Hero.life + 50
        else:
            Hero.life = Hero.maxlife
    elif i == Stage.dropInfo["petit bouclier"]["image"]:
        Hero.defense = Hero.defense + 20

    