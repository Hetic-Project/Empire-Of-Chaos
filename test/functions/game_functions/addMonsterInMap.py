
import random
from functions.interface_functions.centralWindow import *
from functions.game_functions.stages.Stage import *
from functions.game_functions.Monster import *
from functions.game_functions.addSprite import *
from functions.game_functions.Hero import *
from functions.game_functions.Items import *


def addMonsterInMap(mapCell):
    # ajouter des monstres de manière aléatoire sur la map

    for m in Stage.randomMonsterInMap:

        if m[0] == Hero.y and m[1] == Hero.x+1:
            addSprite(mapCell, m[0], m[1], Monster.left)

        elif m[0] == Hero.y and m[1] == Hero.x-1:
            addSprite(mapCell, m[0], m[1], Monster.right)

        elif m[0] == Hero.y+1 and m[1] == Hero.x:
            addSprite(mapCell, m[0], m[1], Monster.back)

        elif m[0] == Hero.y-1 and m[1] == Hero.x:
            addSprite(mapCell, m[0], m[1], Monster.front)

        else:
            addSprite(mapCell, m[0], m[1], Monster.front)

        Stage.infoMonsters.append({
            "y": m[0],
            "x": m[1],
            "name": "Monster-{}".format(m),
            "life": 25,
            "strength": 35,
            "defense": 10,
            "level": 1
        })

    for i in Stage.infoMonsters:
        if i["life"] <= 0:
            addSprite(mapCell, i["y"], i["x"], "")
            # dropRAND = random.randint(0,1)
            # dropItems = ["aucun item", Items.chest]
            # if  dropRAND == 0 :
            #     print("aucun objet reçus !")
            #     return
            # else:
            #     addSprite(mapCell, i["y"], i["x"], dropItems[dropRAND])
            #     print("oh! un item est apparue")
            #     return
          
         

    

    for k in Stage.keyMapArray:
        randKey = mapCell[k[0]][k[1]]
        Stage.infoKey.append({"mapPoint": [k[0], k[1]]})
        addSprite(mapCell, k[0], k[1], Items.chest)

    for t in Stage.targetCellMap:

        cellTargeted = mapCell[t[0]][t[1]]
        cellTargeted.setStyleSheet("background: green")
        Stage.infoTarget.append(
            {"mapPoint": [t[0], t[1]]})
