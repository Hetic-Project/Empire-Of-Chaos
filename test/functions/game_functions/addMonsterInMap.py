
from functions.interface_functions.centralWindow import *
from functions.game_functions.stages.Forest import *


def addMonsterInMap(mapCell):
    # ajouter des monstres de manière aléatoire sur la map

    for m in Forest.randomMonsterInMap:
        monster = QWidget(mapCell[m[0]][m[1]])
        monster.setStyleSheet("background: red")
        monster.setGeometry(0, 0, 125, 124)
        Forest.widgetMonsters.append(monster)

    for k in Forest.keyMapArray:

        randKey = QWidget(mapCell[k[0]][k[1]])
        randKey.setStyleSheet("background: yellow")
        randKey.setGeometry(0, 0, 125, 124)
        Forest.widgetKey.append(randKey)

    for t in Forest.targetCellMap:

        cellTargeted = QWidget(mapCell[t[0]][t[1]])
        cellTargeted.setStyleSheet("background: green")
        cellTargeted.setGeometry(0, 0, 125, 124)
        Forest.widgetTarget.append(cellTargeted)
