
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from functions.game_functions.drawGameMap import *
from functions.interface_functions.centralWindow import *
from functions.game_functions.generateRandomCoordinate import *
from functions.game_functions.stages.Stage import *
from functions.game_functions.addMonsterInMap import *


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
        monsters = Stage.infoMonsters

        centralArea = centralWindow(self)

        # j'appelle borderMap pour qu'elle soit connue de ma fonction keyPressEvent
        borderMap = drawGameMap(centralArea, Hero.front)[0]

        # aller a droite
        if event.key() == 16777236:  # si l'utilisateur appuie sur la fleche droite
            # cette ligne empèche le personnage de sortir de la map
            if Hero.x <= 12:
                if "Monster-[{}, {}]".format(Hero.y, Hero.x+1) in str(monsters):
                    print("il y a un monstre ici")
                else:
                    Hero.x = Hero.x + 1  # j'ajoute 1 sur l'axe du x du hero
                    borderMap.close()  # J'éfface la map
                    # et je la redéssine la map avec les nouvelle coordonnée du héro et la direction du sprite
                    drawGameMap(centralArea, Hero.right)

        # monter
        if event.key() == 16777235:
            if Hero.y > 0:
                if "Monster-[{}, {}]".format(Hero.y-1, Hero.x) in str(monsters):
                    print("il y a un monstre ici")
                else:
                    Hero.y = Hero.y - 1
                    borderMap.close()
                    drawGameMap(centralArea, Hero.back)

        # decsendre
        if event.key() == 16777237:
            if Hero.y <= 8:
                if "Monster-[{}, {}]".format(Hero.y+1, Hero.x) in str(monsters):
                    print("il y a un monstre ici")
                else:
                    Hero.y = Hero.y + 1
                    borderMap.close()
                    drawGameMap(centralArea, Hero.front)

        # aller a gauche
        if event.key() == 16777234:
            if Hero.x > 0:
                if "Monster-[{}, {}]".format(Hero.y, Hero.x-1) in str(monsters):
                    print("il y a un monstre ici")
                else:
                    Hero.x = Hero.x - 1
                    borderMap.close()
                    drawGameMap(centralArea, Hero.left)

        print(Hero.y, Hero.x)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec())
