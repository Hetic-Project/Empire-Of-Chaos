
import json
import sys
from PySide6 import QtCore
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget


# Une class qui gère le statu du héro et les intéraction
class Hero:

    # Status du héro
    pv = 100
    mp = 100
    force = 50
    defense = 50

    # Coordonné du héro sur la map
    x = 5
    y = 5


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Empire Of Chaos")
        self.setMinimumSize(800, 600)
        self.setWindowIcon(QIcon("test/icons/rpg.png"))

        centralArea = QWidget()
        centralArea.setGeometry(0, 0, 800, 600)
        self.setCentralWidget(centralArea)
        centralArea.setStyleSheet("background: #419eee")

        def createCellInYPosition(widget):

            # Cette fonction récupère en paramettre
            # la ligne créer et y ajoute les cellules
            # Une cellule est un QWidget

            cell = []
            x = 0
            # permet de placer les cellules les une a coté des autres sur une ligne
            xPosition = 0

            for x in range(14):

                X = QWidget(widget)
                X.setGeometry(xPosition, 0, 125, 123)
                X.setStyleSheet("border: 1px solid black;")
                xPosition = xPosition + 49
                x = x + 1
                # Une fois la cellule créer elle est ajouter dans une liste appeler cell
                cell.append(X)
            # la fonction retourne la liste cell qui contient tout les QWidget créer pour une ligne donnée
            return cell
        global drawGameMap

        def drawGameMap():
            # permet de placer les lignes les une en dessous des autres
            yPosition = 0
            # compteur de boucle
            y = 0
            # un tableau qui contient le lignes de la map
            row = []
            # tableau bidimentionnel qui contien toute les coordonner de la map (QWidget)
            global mapCell
            mapCell = []

            # borderMap définie les bordures de la map
            borderMap = QWidget(centralArea)
            borderMap.setGeometry(0, 0, 763, 565)
            borderMap.setStyleSheet(
                "border: 1px solid black;" "margin: auto;")

            # dans borderMap je crée 10 ligne
            while y < 10:

                Y = QWidget(borderMap)
                Y.setGeometry(0, yPosition, 763, 123)
                Y.setStyleSheet("border: 1px solid black;")
                yPosition = yPosition + 49
                y = y + 1

                # chaque ligne créer est un QWidget que j'ajoute dans la liste row
                row.append(Y)

            for i in row:
                # a chaque itération j'appel la fonction createCellInYPosition qui
                # retourne la liste des QWidget créer pour la ligne i que je stock dans une variable cells
                cells = createCellInYPosition(i)
                # je stock la liste des QWidget pour la ligne i dans la liste mapCell
                mapCell.append(cells)
                # voila a quoi ressemblera mapCell : mapCell [ ligne1[QWidget1, QWidget2 ], ligne2[QWidget1, QWidget2 ], ... ]
                # mapCell contient donc toute les coordonnée X et Y de la map

            global hero
            # a l'aide de mapCell je place héro sur la map
            hero = QWidget(mapCell[Hero.y][Hero.x])
            hero.setGeometry(0, 0, 125, 124)
            hero.setStyleSheet(
                "background: url(test/sprites/sprite/Hero.png);" "border: none;")

        drawGameMap()

    def keyPressEvent(self, event):
        x = 0
        y = 0

        print(event.key())
        if event.key() == 16777236:
            drawGameMap()
            Hero.x = Hero.x + 1
            print(Hero.x)
            print("je vais a droite")

        if event.key() == 16777234:
            print("je vais a gauche")

        if event.key() == 16777237:
            print("je monte")

        if event.key() == 16777235:
            print("je decsent")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
