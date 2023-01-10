import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel
from functions.game_functions.stages.Stage import *



def addPanelGoals(gameWindow , countMonster , world, stage , countKey) :


    limitePanelGoals = QWidget(gameWindow)
    limitePanelGoals.setGeometry(770 , 378 , 300 , 150)
    limitePanelGoals.setStyleSheet("""
                                        border: 1px black;
                                        background : #ffffff;
                                        border-radius: 22px;
                                        background-color: white;
                                        background-attachment: scroll;
                                """)


    objectivePanel = QLabel("OBJECTIFS :" , limitePanelGoals)
    objectivePanel.setGeometry(100 , 0 , 100 , 40)
    objectivePanel.setStyleSheet("font-size : 18px;" "color : green;" "font-weight : bold;")

    objective1Panel = QLabel("- Monstres tués : {} / {} " .format(countMonster , len(Stage.world[world]["stages"][stage]["monsters"]["coordinate"])) , limitePanelGoals)
    objective1Panel.setGeometry(10 , 50, 200 , 40)
    objective1Panel.setStyleSheet("font-size : 14px;")


    objective2Panel = QLabel("- Clé restante : {} / {} " .format(countKey , len(Stage.world[world]["stages"][stage]["chest"]["coordinate"])) , limitePanelGoals)
    objective2Panel.setGeometry(10 , 80 , 200 , 40)
    objective2Panel.setStyleSheet("font-size : 14px;")