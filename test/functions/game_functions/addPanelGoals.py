import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel
from functions.game_functions.stages.Stage import *



def addPanelGoals(gameWindow , countMonster , world, stage , countKey) :


    limitePanelGoals = QWidget(gameWindow)
    limitePanelGoals.setGeometry(770 , 540 , 320 , 150)
    limitePanelGoals.setStyleSheet("""
                                        border: 1px black;
                                        background : #ffffff;
                                        border-radius: 22px;
                                        background-color: #262626;
                                        background-attachment: scroll;
                                """)


    objectivePanel = QLabel("OBJECTIFS :" , gameWindow)
    objectivePanel.setGeometry(890 , 542 , 350 , 40)
    objectivePanel.setStyleSheet("font-size : 18px;" "color : green;" "font-weight : bold;")

    objective1Panel = QLabel("- Monstres tués : {} / {} " .format(countMonster , len(Stage.world[world]["stages"][stage]["monsters"]["coordinate"])) , gameWindow)
    objective1Panel.setGeometry(753 , 580, 500 , 40)
    objective1Panel.setStyleSheet("font-size : 14px;")


    objective2Panel = QLabel("- Clé restante : {} / {} " .format(countKey , len(Stage.world[world]["stages"][stage]["chest"]["coordinate"])) , gameWindow)
    objective2Panel.setGeometry(753 , 620 , 500 , 40)
    objective2Panel.setStyleSheet("font-size : 14px;")