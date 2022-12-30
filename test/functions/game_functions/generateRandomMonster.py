
import random
from functions.game_functions.drawGameMap import drawGameMap
from functions.interface_functions.centralWindow import *
from functions.game_functions.Hero import Hero
from functions.game_functions.stages.Forest import *


def generateRandomMonster(centralArea):
    # ajouter des monstres de manière aléatoire sur la map

    mapCell = drawGameMap(centralArea, Hero.front)[1]

    randX = random.randint(5, 13)
    randY = random.randint(2, 9)

    count = random.randint(5, 20)
    x = 0
    y = 0

    for m in range(count):
        randX = random.randint(5, 13)
        randY = random.randint(2, 9)
        if x != randX and y != randY:
            monster = QWidget(mapCell[randY][randX])
            monster.setStyleSheet("background: red")
            monster.setGeometry(0, 0, 125, 124)
            Forest.randomMonsterInMap.append([randY, randX])
            x = randX
            y = randY
        else:
            print("coordonée identique")
            m = m-1

    for i in Forest.randomMonsterInMap:

        if randY == i[0] and randX == i[1]:
            print("impossible de placer la clée")
            randX = random.randint(5, 13)
            randY = random.randint(2, 9)
            pass

        else:
            randKey = QWidget(mapCell[randY][randX])
            randKey.setStyleSheet("background: yellow")
            randKey.setGeometry(0, 0, 125, 124)
            Forest.keyMapArray.append([randY, randX])

    for j in Forest.randomMonsterInMap:
        for e in Forest.keyMapArray:
            if randY == j[0] and randX == j[1] and randY == e[0] and randX == e[1]:
                print("impossible de placer la case d'arriver")
                randX = random.randint(5, 13)
                randY = random.randint(2, 9)
            else:
                cellTargeted = QWidget(mapCell[randY][randX])
                cellTargeted.setStyleSheet("background: green")
                cellTargeted.setGeometry(0, 0, 125, 124)
                Forest.targetCellMap.append([randY, randX])
                return
