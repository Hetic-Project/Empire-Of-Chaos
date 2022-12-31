
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


class GameWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Empire Of Chaos")
        self.setMinimumSize(1275, 1000)
        self.setWindowIcon(QIcon("test/icons/rpg.png"))

        centralArea = centralWindow(self)

        generateRandomCoordinate()
        drawGameMap(centralArea, Hero.front)
        print(Stage.infoMonsters)

    # keyPressEvent est une fonction native a Qt elle permet de gérer les évènement

    def keyPressEvent(self, event):

        centralArea = centralWindow(self)

        # j'appelle borderMap pour qu'elle soit connue de ma fonction keyPressEvent
        borderMap = drawGameMap(centralArea, Hero.front)[0]
        mapCell = drawGameMap(centralArea, Hero.front)[1]

        # aller a droite
        if event.key() == 16777236:  # si l'utilisateur appuie sur la fleche droite
            # cette ligne empèche le personnage de sortir de la map
            if Hero.x <= 12:
                if "Monster-[{}, {}]".format(Hero.y, Hero.x+1) in str(Stage.infoMonsters):
                    print("il y a un monstre ici")
                    # un bouton attaquer apparais
                    attaqueBTN = QPushButton("Attaquer",  centralArea)
                    attaqueBTN.setGeometry(40, 550, 125, 50)
                    attaqueBTN.clicked.connect(attackFunction)
                    # Voire les stats du monstre
                    drawGameMap(centralArea, Hero.right)
                    for i in Stage.infoMonsters:
                        if i["y"] == Hero.y and i["x"] == Hero.x+1:
                            print(i["name"])
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
                    borderMap.close()  # J'éfface la map
                    # et je la redéssine la map avec les nouvelle coordonnée du héro et la direction du sprite
                    drawGameMap(centralArea, Hero.right)

        # monter
        if event.key() == 16777235:
            if Hero.y > 0:
                if "Monster-[{}, {}]".format(Hero.y-1, Hero.x) in str(Stage.infoMonsters):
                    print("il y a un monstre ici")
                    attaqueBTN = QPushButton("Attaquer",  centralArea)
                    attaqueBTN.setGeometry(40, 550, 125, 50)
                    attaqueBTN.clicked.connect(attackFunction)
                    drawGameMap(centralArea, Hero.back)

                elif "'mapPoint': [{}, {}]".format(Hero.y-1, Hero.x) in str(Stage.infoKey):
                    print("Voila la clée")
                    pickUpBTN = QPushButton("Ramasser",  centralArea)
                    pickUpBTN.setGeometry(40, 550, 125, 50)
                    pickUpBTN.clicked.connect(pickUpFunction)
                    drawGameMap(centralArea, Hero.back)
                else:
                    Hero.y = Hero.y - 1
                    borderMap.close()
                    drawGameMap(centralArea, Hero.back)

        # decsendre
        if event.key() == 16777237:
            if Hero.y <= 8:
                if "Monster-[{}, {}]".format(Hero.y+1, Hero.x) in str(Stage.infoMonsters):
                    print("il y a un monstre ici")
                    attaqueBTN = QPushButton("Attaquer",  centralArea)
                    attaqueBTN.setGeometry(40, 550, 125, 50)
                    attaqueBTN.clicked.connect(attackFunction)
                    drawGameMap(centralArea, Hero.front)

                elif "'mapPoint': [{}, {}]".format(Hero.y+1, Hero.x) in str(Stage.infoKey):
                    print("Voila la clée")
                    pickUpBTN = QPushButton("Ramasser",  centralArea)
                    pickUpBTN.setGeometry(40, 550, 125, 50)
                    pickUpBTN.clicked.connect(pickUpFunction)
                    drawGameMap(centralArea, Hero.front)

                else:
                    Hero.y = Hero.y + 1
                    borderMap.close()
                    drawGameMap(centralArea, Hero.front)

        # aller a gauche
        if event.key() == 16777234:
            if Hero.x > 0:
                if "Monster-[{}, {}]".format(Hero.y, Hero.x-1) in str(Stage.infoMonsters):
                    print("il y a un monstre ici")
                    attaqueBTN = QPushButton("Attaquer",  centralArea)
                    attaqueBTN.setGeometry(40, 550, 125, 50)
                    attaqueBTN.clicked.connect(attackFunction)
                    Stage.monsterTarget.append([Hero.y, Hero.x-1])
                    drawGameMap(centralArea, Hero.left)

                elif "'mapPoint': [{}, {}]".format(Hero.y, Hero.x-1) in str(Stage.infoKey):
                    print("Voila la clée")
                    pickUpBTN = QPushButton("Ramasser",  centralArea)
                    pickUpBTN.setGeometry(40, 550, 125, 50)
                    pickUpBTN.clicked.connect(pickUpFunction)
                    drawGameMap(centralArea, Hero.left)

                else:
                    Hero.x = Hero.x - 1
                    borderMap.close()
                    drawGameMap(centralArea, Hero.left)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec())
