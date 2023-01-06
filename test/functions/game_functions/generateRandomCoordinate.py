
import random
from functions.game_functions.drawGameMap import drawGameMap
from functions.interface_functions.centralWindow import *
from functions.game_functions.Hero import Hero
from functions.game_functions.stages.Stage import *


def generateRandomCoordinate():

    count = random.randint(3, 5)
    x=0

    Y = 1
    
    # Génération de coordonnées pour les monstres
    for m in range(count):

        randX = random.randint(1, 7)

        if Y < 9 :

            if  x == randX :
                print("impossible de placer le monstre !")
            else:
                x = randX
                Stage.randomMonsterInMap.append([Y, randX])
                Y = Y + 2   
         

    # Génération de coordonnées pour la clée
    randX = random.randint(8, 10)
    randY = random.randint(0, 9)

    Stage.keyMapArray.append([randY, randX])

    # Génération de coordonnées pour la case d'arriver
    randX = random.randint(11, 13)
    randY = random.randint(0, 9)

    Stage.targetCellMap.append([randY, randX])
