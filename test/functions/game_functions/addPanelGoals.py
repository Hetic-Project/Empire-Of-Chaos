import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel



def addPanelGoals(gameWindow , countMonster , MonsterList , countKey , KeyList) :


    limitePanelGoals = QWidget(gameWindow)
    limitePanelGoals.setGeometry(770 , 540 , 320 , 150)
    limitePanelGoals.setStyleSheet("""
                                        border: 1px black;
                                        background : #ffffff;
                                        border-radius: 30px;
                                """)


    objectivePanel = QLabel("OBJECTIFS :" , gameWindow)
    objectivePanel.setGeometry(890 , 542 , 350 , 40)
    objectivePanel.setStyleSheet("font-size : 18px;")

    objective1Panel = QLabel(" - Monstres tués : {} / {} " .format(countMonster , MonsterList) , gameWindow)
    objective1Panel.setGeometry(773 , 580, 500 , 40)
    objective1Panel.setStyleSheet("font-size : 14px;")


    objective2Panel = QLabel(" - Clé restante : {} / {} " .format(countKey , KeyList) , gameWindow)
    objective2Panel.setGeometry(773 , 620 , 500 , 40)
    objective2Panel.setStyleSheet("font-size : 14px;")