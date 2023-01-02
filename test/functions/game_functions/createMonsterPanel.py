from PySide6.QtWidgets import QWidget, QLabel, QProgressBar
from functions.game_functions.Hero import *


def createMonsterPanel(centralArea, name, life, strength, defense, level, face_image):

    monsterPanel = QWidget(centralArea)
    monsterPanel.setGeometry(750, 185, 350, 140)
    monsterPanel.setStyleSheet("border: 1px solid black")

    face = QWidget(monsterPanel)
    face.setGeometry(1, 1, 140, 138)
    face.setStyleSheet(
        "{}".format(face_image))

    labelMonster = QLabel("{} lvl : {}".format(name, level), monsterPanel)
    labelMonster.setGeometry(170, 5, 130, 20)
    labelMonster.setStyleSheet("border: none")

    labelPV = QLabel("PV : {}".format(life), monsterPanel)
    labelPV.setGeometry(150, 40, 85, 20)
    labelPV.setStyleSheet("border: none")

    progressPV = QProgressBar(monsterPanel)
    progressPV.setValue(life)
    progressPV.setGeometry(240, 40, 100, 20)
    progressPV.setStyleSheet("text-align: center")

    labelSTR = QLabel("Force : {}".format(strength), monsterPanel)
    labelSTR.setGeometry(150, 65, 100, 20)
    labelSTR.setStyleSheet("border: none")

    labelDEF = QLabel("Défense : {}".format(defense), monsterPanel)
    labelDEF.setGeometry(150, 90, 100, 20)
    labelDEF.setStyleSheet("border: none")
