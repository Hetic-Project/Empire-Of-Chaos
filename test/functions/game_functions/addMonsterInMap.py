
from functions.interface_functions.centralWindow import *
from functions.game_functions.stages.Stage import *
from functions.game_functions.Monster import *
from functions.game_functions.addMonstersSprite import *
from functions.game_functions.Hero import *


def addMonsterInMap(mapCell):
    # ajouter des monstres de manière aléatoire sur la map

    for m in Stage.randomMonsterInMap:

        if m[0] == Hero.y and m[1] == Hero.x+1:
            addMonstersSprite(mapCell, m[0], m[1], Monster.left)

        elif m[0] == Hero.y and m[1] == Hero.x-1:
            addMonstersSprite(mapCell, m[0], m[1], Monster.right)

        elif m[0] == Hero.y+1 and m[1] == Hero.x:
            addMonstersSprite(mapCell, m[0], m[1], Monster.back)

        elif m[0] == Hero.y-1 and m[1] == Hero.x:
            addMonstersSprite(mapCell, m[0], m[1], Monster.front)

        else:
            addMonstersSprite(mapCell, m[0], m[1], Monster.front)

        Stage.infoMonsters.append({
            "y": m[0],
            "x": m[1],
            "name": "Monster-{}".format(m),
            "life": 25,
            "strength": 10,
            "defense": 10,
            "level": 1
        })

    for i in Stage.infoMonsters:
        if i["life"] <= 0:
            addMonstersSprite(mapCell, i["y"], i["x"], Monster.dead)

    for k in Stage.keyMapArray:
        randKey = mapCell[k[0]][k[1]]
        randKey.setStyleSheet("background: yellow")
        Stage.infoKey.append({"mapPoint": [k[0], k[1]]})

    for t in Stage.targetCellMap:

        cellTargeted = mapCell[t[0]][t[1]]
        cellTargeted.setStyleSheet("background: green")
        Stage.infoTarget.append(
            {"mapPoint": [t[0], t[1]]})
