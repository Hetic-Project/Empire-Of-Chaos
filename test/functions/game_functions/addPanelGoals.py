import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel
from functions.game_functions.stages.Stage import *



def addPanelGoals(gameWindow , countMonster , world, stage , countKey) :


    limitePanelGoals = QWidget(gameWindow)
    limitePanelGoals.setGeometry(40 , 440 , 300 , 150)
    limitePanelGoals.setStyleSheet("""
                                        border: none;
                                        background : none;
                                        border-radius: 22px;
<<<<<<< HEAD
=======
                                        background-color: white;
>>>>>>> 35b277629d9d8b23b58582f39205463bb86fce7a
                                        background-attachment: scroll;
                                """)


    objectivePanel = QLabel("OBJECTIFS :" , limitePanelGoals)
    objectivePanel.setGeometry(75, 0 , 130 , 40)
    objectivePanel.setStyleSheet("font-size : 23px;" "color : white;" "font-weight : bold;")

    objective1Panel = QLabel("-    Monstres tués : {} / {} " .format(countMonster , len(Stage.world[world]["stages"][stage]["monsters"]["coordinate"])) , limitePanelGoals)
    objective1Panel.setGeometry(10 , 50, 200 , 40)
    objective1Panel.setStyleSheet("font-size : 18px; color : white;")


    objective2Panel = QLabel("-    Clé restante : {} / {} " .format(countKey , len(Stage.world[world]["stages"][stage]["chest"]["coordinate"])) , limitePanelGoals)
    objective2Panel.setGeometry(10 , 80 , 200 , 40)
    objective2Panel.setStyleSheet("font-size : 18px; color : white;")