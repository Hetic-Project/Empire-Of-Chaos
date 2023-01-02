from PySide6.QtWidgets import QWidget, QLabel, QProgressBar
from functions.game_functions.Hero import *


def createHeroPanel(centralArea):

    heroPanel = QWidget(centralArea)
    heroPanel.setGeometry(750, 35, 350, 140)
    heroPanel.setStyleSheet("border: 1px solid black")

    face = QWidget(heroPanel)
    face.setGeometry(1, 1, 140, 138)
    face.setStyleSheet(
        "background: url(test/sprites/hero/HeroFace.png);" "border: none")

    labelHero = QLabel("HERO lvl : {}".format(Hero.level), heroPanel)
    labelHero.setGeometry(180, 5, 100, 20)
    labelHero.setStyleSheet("border: none")

    labelPV = QLabel("PV : {}".format(Hero.life), heroPanel)
    labelPV.setGeometry(150, 35, 85, 20)
    labelPV.setStyleSheet("border: none")

    progressPV = QProgressBar(heroPanel)
    progressPV.setValue((Hero.life*100) / Hero.life)
    progressPV.setGeometry(240, 35, 100, 20)
    progressPV.setStyleSheet("text-align: center")

    labelSTR = QLabel("Force : {}".format(Hero.strength), heroPanel)
    labelSTR.setGeometry(150, 60, 100, 20)
    labelSTR.setStyleSheet("border: none")

    labelDEF = QLabel("Défense : {}".format(Hero.defense), heroPanel)
    labelDEF.setGeometry(150, 85, 100, 20)
    labelDEF.setStyleSheet("border: none")

    labelEXP = QLabel("EXP : ", heroPanel)
    labelEXP.setGeometry(150, 110, 40, 20)
    labelEXP.setStyleSheet("border: none")

    progressEXP = QProgressBar(heroPanel)
    progressEXP.setValue(Hero.exp)
    progressEXP.setGeometry(185, 110, 155, 20)
    progressEXP.setStyleSheet("text-align: center")
