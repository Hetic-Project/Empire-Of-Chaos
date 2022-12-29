from PySide6.QtWidgets import QWidget
from Hero import *
from createCell import *


def drawGameMap(centralArea):
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
    global borderMap
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
    return borderMap
