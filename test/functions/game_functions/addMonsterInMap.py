
from functions.interface_functions.centralWindow import *
from functions.game_functions.stages.Stage import *


def addMonsterInMap(mapCell):
    # ajouter des monstres de manière aléatoire sur la map

    for m in Stage.randomMonsterInMap:
        monster = mapCell[m[0]][m[1]]
        monster.setStyleSheet("background: red")
        Stage.infoMonsters.append({
            "y": m[0],
            "x": m[1],
            "name": "Monster-{}".format(m),
            "life": 25,
            "strength": 10,
            "defense": 10,
            "level": 1
        })

    for k in Stage.keyMapArray:
        randKey = mapCell[k[0]][k[1]]
        randKey.setStyleSheet("background: yellow")
        Stage.infoKey.append({"mapPoint": [k[0], k[1]]})

    for t in Stage.targetCellMap:

        cellTargeted = mapCell[t[0]][t[1]]
        cellTargeted.setStyleSheet("background: green")
        Stage.infoTarget.append(
            {"mapPoint": [t[0], t[1]]})
