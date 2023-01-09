import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel



def addPanelGoals(gameWindow , countMonster , MonsterList , countKey , KeyList) :


    limitePanelGoals = QWidget(gameWindow)
    limitePanelGoals.setGeometry(750 , 340 , 350 , 150)
    limitePanelGoals.setStyleSheet("border: 1px solid black")


    objectivePanel = QLabel("Objectifs :" , gameWindow)
    objectivePanel.setGeometry(870 , 342 , 350 , 40)
    objectivePanel.setStyleSheet("font-size : 20px;")

    objective1Panel = QLabel("- Monstres tués : {} / {} " .format(countMonster , MonsterList) , gameWindow)
    objective1Panel.setGeometry(753 , 380, 500 , 40)
    objective1Panel.setStyleSheet("font-size : 14px;")


    objective2Panel = QLabel("- Clé restante : {} / {} " .format(countKey , KeyList) , gameWindow)
    objective2Panel.setGeometry(753 , 420 , 500 , 40)
    objective2Panel.setStyleSheet("font-size : 14px;")