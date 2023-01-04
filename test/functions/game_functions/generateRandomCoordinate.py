
import random
from functions.game_functions.drawGameMap import drawGameMap
from functions.interface_functions.centralWindow import *
from functions.game_functions.Hero import Hero
from functions.game_functions.stages.Stage import *


def generateRandomCoordinate():

    count = random.randint(5, 10)
    x = 0
    y = 0

    # Génération de coordonnées pour les monstres
    for m in range(count):

        randX = random.randint(1, 7)
        randY = random.randint(1, 9)

        if  x != randX and y != randY:
            x = randX
            y = randY
            Stage.randomMonsterInMap.append([randY, randX])
        else:
            count = count -1    

    # Génération de coordonnées pour la clée
    randX = random.randint(8, 10)
    randY = random.randint(0, 9)

    Stage.keyMapArray.append([randY, randX])

    # Génération de coordonnées pour la case d'arriver
    randX = random.randint(11, 13)
    randY = random.randint(0, 9)

    Stage.targetCellMap.append([randY, randX])
