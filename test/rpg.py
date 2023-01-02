
import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from functions.game_functions.drawGameMap import *
from functions.interface_functions.centralWindow import *
from functions.game_functions.generateRandomCoordinate import *
from functions.game_functions.stages.Stage import *
from functions.game_functions.addMonsterInMap import *
from functions.game_functions.attackFunction import *
from functions.game_functions.pickUpFunction import *
from functions.game_functions.createHeroPanel import *
from functions.game_functions.createMonsterPanel import *
from functions.game_functions.Monster import *
from functions.game_functions.addMonstersSprite import *


class GameWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Empire Of Chaos")
        self.setMinimumSize(1275, 1000)
        self.setWindowIcon(QIcon("test/icons/rpg.png"))

        centralArea = centralWindow(self)

        generateRandomCoordinate()
        mapCell = drawGameMap(centralArea, Hero.front)[1]
        createHeroPanel(centralArea)

    # keyPressEvent est une fonction native a Qt elle permet de gérer les évènement

    def keyPressEvent(self, event):

        centralArea = centralWindow(self)
        createHeroPanel(centralArea)

        # j'appelle borderMap pour qu'elle soit connue de ma fonction keyPressEvent
        mapCell = drawGameMap(centralArea, Hero.front)[1]

        # aller a droite
        if event.key() == 16777236:  # si l'utilisateur appuie sur la fleche droite
            # cette ligne empèche le personnage de sortir de la map
            if Hero.x <= 12:
                if "Monster-[{}, {}]".format(Hero.y, Hero.x+1) in str(Stage.infoMonsters):
                    for i in Stage.infoMonsters:

                        if i["y"] == Hero.y and i["x"] == Hero.x+1:
                            # Voire les stats du monstre
                            createMonsterPanel(
                                centralArea, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)
                            drawGameMap(centralArea, Hero.right)
                            return

                elif "'mapPoint': [{}, {}]".format(Hero.y, Hero.x+1) in str(Stage.infoKey):
                    print("Voila la clée")
                    # un boutton rammaser apparais
                    pickUpBTN = QPushButton("Ramasser",  centralArea)
                    pickUpBTN.setGeometry(40, 550, 125, 50)
                    pickUpBTN.clicked.connect(pickUpFunction)
                    drawGameMap(centralArea, Hero.right)

                else:
                    Hero.x = Hero.x + 1  # j'ajoute 1 sur l'axe du x du hero
                    # et je la redéssine la map avec les nouvelle coordonnée du héro et la direction du sprite
                    drawGameMap(centralArea, Hero.right)
                    for i in Stage.randomMonsterInMap:
                        addMonstersSprite(mapCell, i[0], i[1], Monster.front)

        # monter
        elif event.key() == 16777235:
            if Hero.y > 0:
                if "Monster-[{}, {}]".format(Hero.y-1, Hero.x) in str(Stage.infoMonsters):
                    for i in Stage.infoMonsters:
                        if i["y"] == Hero.y-1 and i["x"] == Hero.x:
                            createMonsterPanel(
                                centralArea, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)
                            drawGameMap(centralArea, Hero.back)
                            return

                elif "'mapPoint': [{}, {}]".format(Hero.y-1, Hero.x) in str(Stage.infoKey):
                    print("Voila la clée")
                    pickUpBTN = QPushButton("Ramasser",  centralArea)
                    pickUpBTN.setGeometry(40, 550, 125, 50)
                    pickUpBTN.clicked.connect(pickUpFunction)
                    drawGameMap(centralArea, Hero.back)
                else:
                    Hero.y = Hero.y - 1
                    drawGameMap(centralArea, Hero.back)

        # decsendre
        elif event.key() == 16777237:
            if Hero.y <= 8:
                if "Monster-[{}, {}]".format(Hero.y+1, Hero.x) in str(Stage.infoMonsters):
                    for i in Stage.infoMonsters:
                        if i["y"] == Hero.y+1 and i["x"] == Hero.x:

                            createMonsterPanel(
                                centralArea, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)
                            drawGameMap(centralArea, Hero.front)
                            return

                elif "'mapPoint': [{}, {}]".format(Hero.y+1, Hero.x) in str(Stage.infoKey):
                    print("Voila la clée")
                    pickUpBTN = QPushButton("Ramasser",  centralArea)
                    pickUpBTN.setGeometry(40, 550, 125, 50)
                    pickUpBTN.clicked.connect(pickUpFunction)
                    drawGameMap(centralArea, Hero.front)

                else:
                    Hero.y = Hero.y + 1
                    drawGameMap(centralArea, Hero.front)

        # aller a gauche
        elif event.key() == 16777234:
            if Hero.x > 0:
                if "Monster-[{}, {}]".format(Hero.y, Hero.x-1) in str(Stage.infoMonsters):
                    for i in Stage.infoMonsters:
                        if i["y"] == Hero.y and i["x"] == Hero.x-1:
                            createMonsterPanel(
                                centralArea, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)
                            drawGameMap(centralArea, Hero.left)
                            return

                elif "'mapPoint': [{}, {}]".format(Hero.y, Hero.x-1) in str(Stage.infoKey):
                    print("Voila la clée")
                    pickUpBTN = QPushButton("Ramasser",  centralArea)
                    pickUpBTN.setGeometry(40, 550, 125, 50)
                    pickUpBTN.clicked.connect(pickUpFunction)
                    drawGameMap(centralArea, Hero.left)

                else:
                    Hero.x = Hero.x - 1
                    drawGameMap(centralArea, Hero.left)

        # si j'appuie sur entrer j'attaque
        elif event.key() == 16777220:
            for i in Stage.infoMonsters:

                if i["y"] == Hero.y and i["x"] == Hero.x+1:
                    createMonsterPanel(
                        centralArea, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)

                    if i["life"] <= 0:
                        print("le monstre est mort")
                        drawGameMap(centralArea, Hero.right)
                    else:

                        attack = int(
                            Hero.strength/(i["defense"]/2)*Hero.level)
                        i["life"] = i["life"] - attack
                        drawGameMap(centralArea, Hero.right)
                        return

                elif i["y"] == Hero.y-1 and i["x"] == Hero.x:
                    createMonsterPanel(
                        centralArea, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)
                    if i["life"] <= 0:
                        print("le monstre est mort")
                        drawGameMap(centralArea, Hero.back)
                    else:

                        attack = int(
                            Hero.strength/(i["defense"]/2)*Hero.level)
                        i["life"] = i["life"] - attack
                        drawGameMap(centralArea, Hero.back)
                    return

                elif i["y"] == Hero.y+1 and i["x"] == Hero.x:
                    createMonsterPanel(
                        centralArea, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)

                    if i["life"] <= 0:
                        print("le monstre est mort")
                        drawGameMap(centralArea, Hero.front)
                    else:
                        attack = int(
                            Hero.strength/(i["defense"]/2)*Hero.level)
                        i["life"] = i["life"] - attack
                        drawGameMap(centralArea, Hero.front)
                    return

                elif i["y"] == Hero.y and i["x"] == Hero.x-1:
                    createMonsterPanel(
                        centralArea, i["name"], i["life"], i["strength"], i["defense"], i["level"], Monster.face)
                    if i["life"] <= 0:
                        print("le monstre est mort")
                        drawGameMap(centralArea, Hero.left)
                    else:
                        attack = int(
                            Hero.strength/(i["defense"]/2)*Hero.level)
                        i["life"] = i["life"] - attack
                        drawGameMap(centralArea, Hero.left)
                    return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec())
